#!/usr/bin/env python3
"""
MCP Server for Internal Wiki
Provides tools to interact with internal wiki systems.
"""

import asyncio
import os
from datetime import datetime
from typing import Any, Optional
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent
import httpx
from urllib.parse import quote, urljoin


class WikiClient:
    """Base class for wiki clients - supports multiple wiki types"""
    
    def __init__(self, base_url: str, auth_token: Optional[str] = None, 
                 wiki_type: str = "generic", username: Optional[str] = None,
                 password: Optional[str] = None):
        self.base_url = base_url.rstrip('/')
        self.auth_token = auth_token
        self.wiki_type = wiki_type.lower()
        self.username = username
        self.password = password
        self.client = httpx.AsyncClient(timeout=30.0)
        self._mediawiki_logged_in = False
    
    async def _login_mediawiki(self) -> bool:
        """Login to MediaWiki using username/password (Bot Password format)"""
        if self._mediawiki_logged_in:
            return True
        
        if not self.username or not self.password:
            username_status = "set" if self.username else "not set"
            password_status = "set" if self.password else "not set"
            raise ValueError(
                f"MediaWiki authentication requires WIKI_USERNAME and WIKI_PASSWORD. "
                f"Current status: WIKI_USERNAME={username_status}, WIKI_PASSWORD={password_status}"
            )
        
        try:
            api_url = f"{self.base_url}/api.php"
            
            # Step 1: Get login token
            params = {
                "action": "query",
                "meta": "tokens",
                "type": "login",
                "format": "json",
                "formatversion": "2"
            }
            response = await self.client.get(api_url, params=params)
            response.raise_for_status()
            token_data = response.json()
            
            login_token = token_data.get("query", {}).get("tokens", {}).get("logintoken", "")
            if not login_token:
                raise ValueError("Failed to obtain MediaWiki login token")
            
            # Step 2: Perform login
            login_params = {
                "action": "login",
                "lgname": self.username,
                "lgpassword": self.password,
                "lgtoken": login_token,
                "format": "json",
                "formatversion": "2"
            }
            response = await self.client.post(api_url, data=login_params)
            response.raise_for_status()
            login_data = response.json()
            
            login_result = login_data.get("login", {})
            if login_result.get("result") == "Success":
                self._mediawiki_logged_in = True
                return True
            else:
                error_msg = login_result.get("reason", "Unknown error")
                raise ValueError(f"MediaWiki login failed: {error_msg}")
        except httpx.HTTPStatusError as e:
            raise ValueError(f"MediaWiki login HTTP error: {e.response.status_code} - {e.response.text[:200]}")
        except Exception as e:
            if isinstance(e, ValueError):
                raise
            raise ValueError(f"MediaWiki login error: {str(e)}")
    
    async def _get_headers(self) -> dict:
        """Get authentication headers based on wiki type"""
        headers = {"Accept": "application/json"}
        
        if self.wiki_type == "mediawiki":
            # MediaWiki uses session cookies from login, not Bearer tokens
            # Login will be handled separately via _login_mediawiki()
            pass
        elif self.wiki_type == "confluence":
            if self.username and self.password:
                # Basic auth for Confluence
                import base64
                credentials = base64.b64encode(
                    f"{self.username}:{self.password}".encode()
                ).decode()
                headers["Authorization"] = f"Basic {credentials}"
        elif self.wiki_type == "wikijs":
            if self.auth_token:
                headers["Authorization"] = f"Bearer {self.auth_token}"
        else:  # generic
            if self.auth_token:
                headers["Authorization"] = f"Bearer {self.auth_token}"
            elif self.username and self.password:
                import base64
                credentials = base64.b64encode(
                    f"{self.username}:{self.password}".encode()
                ).decode()
                headers["Authorization"] = f"Basic {credentials}"
        
        return headers
    
    async def get_page(self, page_title: str) -> dict:
        """Retrieve a wiki page by title"""
        headers = await self._get_headers()
        
        if self.wiki_type == "mediawiki":
            # Login if needed
            await self._login_mediawiki()
            
            # MediaWiki API
            params = {
                "action": "query",
                "titles": page_title,
                "prop": "revisions",
                "rvprop": "content",
                "format": "json",
                "formatversion": "2"
            }
            url = f"{self.base_url}/api.php"
            response = await self.client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            if "query" in data and "pages" in data["query"]:
                pages = data["query"]["pages"]
                if pages and len(pages) > 0:
                    page = pages[0]
                    return {
                        "title": page.get("title", page_title),
                        "content": page.get("revisions", [{}])[0].get("content", ""),
                        "exists": "missing" not in page
                    }
            return {"title": page_title, "content": "", "exists": False}
            
        elif self.wiki_type == "confluence":
            # Confluence REST API
            page_title_encoded = quote(page_title)
            url = f"{self.base_url}/rest/api/content"
            params = {"title": page_title, "expand": "body.storage,version"}
            response = await self.client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            if "results" in data and len(data["results"]) > 0:
                page = data["results"][0]
                return {
                    "title": page.get("title", page_title),
                    "content": page.get("body", {}).get("storage", {}).get("value", ""),
                    "exists": True,
                    "url": page.get("_links", {}).get("webui", "")
                }
            return {"title": page_title, "content": "", "exists": False}
            
        elif self.wiki_type == "wikijs":
            # Wiki.js API
            page_title_encoded = quote(page_title)
            url = f"{self.base_url}/api/v1/pages/{page_title_encoded}"
            response = await self.client.get(url, headers=headers)
            
            if response.status_code == 404:
                return {"title": page_title, "content": "", "exists": False}
            
            response.raise_for_status()
            data = response.json()
            return {
                "title": data.get("title", page_title),
                "content": data.get("content", ""),
                "exists": True,
                "url": data.get("path", "")
            }
            
        else:  # generic REST API
            # Assume generic REST API structure
            page_title_encoded = quote(page_title)
            url = f"{self.base_url}/api/pages/{page_title_encoded}"
            response = await self.client.get(url, headers=headers)
            
            if response.status_code == 404:
                return {"title": page_title, "content": "", "exists": False}
            
            response.raise_for_status()
            data = response.json()
            return {
                "title": data.get("title", page_title),
                "content": data.get("content", data.get("body", "")),
                "exists": True
            }
    
    async def search_pages(self, query: str, limit: int = 10) -> list:
        """Search for wiki pages"""
        headers = await self._get_headers()
        
        if self.wiki_type == "mediawiki":
            # Login if needed
            await self._login_mediawiki()
            
            params = {
                "action": "query",
                "list": "search",
                "srsearch": query,
                "srlimit": limit,
                "format": "json",
                "formatversion": "2"
            }
            url = f"{self.base_url}/api.php"
            response = await self.client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            results = []
            if "query" in data and "search" in data["query"]:
                for item in data["query"]["search"]:
                    results.append({
                        "title": item.get("title", ""),
                        "snippet": item.get("snippet", "")
                    })
            return results
            
        elif self.wiki_type == "confluence":
            url = f"{self.base_url}/rest/api/content/search"
            params = {"cql": f"text ~ \"{query}\"", "limit": limit}
            response = await self.client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            results = []
            if "results" in data:
                for item in data["results"]:
                    results.append({
                        "title": item.get("title", ""),
                        "url": item.get("_links", {}).get("webui", "")
                    })
            return results
            
        elif self.wiki_type == "wikijs":
            url = f"{self.base_url}/api/v1/search"
            params = {"query": query, "limit": limit}
            response = await self.client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            results = []
            if "results" in data:
                for item in data["results"]:
                    results.append({
                        "title": item.get("title", ""),
                        "path": item.get("path", "")
                    })
            return results
            
        else:  # generic
            url = f"{self.base_url}/api/search"
            params = {"q": query, "limit": limit}
            response = await self.client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            return data.get("results", [])
    
    async def list_pages(self, namespace: Optional[str] = None, limit: int = 50) -> list:
        """List wiki pages"""
        headers = await self._get_headers()
        
        if self.wiki_type == "mediawiki":
            # Login if needed
            await self._login_mediawiki()
            
            params = {
                "action": "query",
                "list": "allpages",
                "aplimit": limit,
                "format": "json",
                "formatversion": "2"
            }
            if namespace:
                params["apnamespace"] = namespace
            
            url = f"{self.base_url}/api.php"
            response = await self.client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            results = []
            if "query" in data and "allpages" in data["query"]:
                for item in data["query"]["allpages"]:
                    results.append({"title": item.get("title", "")})
            return results
            
        elif self.wiki_type == "confluence":
            url = f"{self.base_url}/rest/api/content"
            params = {"limit": limit}
            if namespace:
                params["space"] = namespace
            response = await self.client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            results = []
            if "results" in data:
                for item in data["results"]:
                    results.append({
                        "title": item.get("title", ""),
                        "type": item.get("type", "")
                    })
            return results
            
        elif self.wiki_type == "wikijs":
            url = f"{self.base_url}/api/v1/pages"
            params = {"limit": limit}
            response = await self.client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            return data.get("pages", [])
            
        else:  # generic
            url = f"{self.base_url}/api/pages"
            params = {"limit": limit}
            response = await self.client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            return data.get("pages", data.get("results", []))
    
    async def close(self):
        """Close the HTTP client"""
        await self.client.aclose()


# Initialize wiki client from environment variables
def get_wiki_client() -> WikiClient:
    """Create wiki client from environment configuration"""
    base_url = os.getenv("WIKI_BASE_URL", "")
    if not base_url:
        raise ValueError("WIKI_BASE_URL environment variable is required")
    
    wiki_type = os.getenv("WIKI_TYPE", "generic").lower()
    auth_token = os.getenv("WIKI_AUTH_TOKEN")
    # Try both WIKI_USERNAME and WIKI_USER (fallback)
    username = os.getenv("WIKI_USERNAME") or os.getenv("WIKI_USER")
    # Try both WIKI_PASSWORD and WIKI_PASS (fallback)
    password = os.getenv("WIKI_PASSWORD") or os.getenv("WIKI_PASS")
    
    return WikiClient(
        base_url=base_url,
        auth_token=auth_token,
        wiki_type=wiki_type,
        username=username,
        password=password
    )


# Initialize MCP server
server = Server("wiki-mcp-server")
wiki_client: Optional[WikiClient] = None


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools"""
    return [
        Tool(
            name="get_wiki_page",
            description="Retrieve a wiki page by its title. Returns the page content and metadata.",
            inputSchema={
                "type": "object",
                "properties": {
                    "page_title": {
                        "type": "string",
                        "description": "The title of the wiki page to retrieve"
                    }
                },
                "required": ["page_title"]
            }
        ),
        Tool(
            name="search_wiki_pages",
            description="Search for wiki pages by query string. Returns a list of matching pages.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query string"
                    },
                    "limit": {
                        "type": "number",
                        "description": "Maximum number of results to return (default: 10)",
                        "default": 10
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="list_wiki_pages",
            description="List wiki pages. Returns a list of available pages.",
            inputSchema={
                "type": "object",
                "properties": {
                    "namespace": {
                        "type": "string",
                        "description": "Optional namespace or space to filter pages (wiki-specific)"
                    },
                    "limit": {
                        "type": "number",
                        "description": "Maximum number of pages to return (default: 50)",
                        "default": 50
                    }
                }
            }
        ),
        Tool(
            name="get_wiki_auth_info",
            description="Get authentication information and URLs for the configured wiki. Returns instructions and links to authenticate and obtain tokens.",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="check_wiki_env",
            description="Check which wiki-related environment variables are set (diagnostic tool).",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="good_morning_report",
            description="Generate a morning report for the Process Platform team. This tool triggers the agent to gather information from Azure DevOps about the team's current iteration, work items, and recent activity, then formats it into a brief summary report.",
            inputSchema={
                "type": "object",
                "properties": {
                    "team": {
                        "type": "string",
                        "description": "The team name (default: 'Core-Process-platform')",
                        "default": "Core-Process-platform"
                    },
                    "project": {
                        "type": "string",
                        "description": "The Azure DevOps project name (default: '360')",
                        "default": "360"
                    }
                }
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls"""
    global wiki_client
    
    # Don't initialize client for auth info tool
    if name != "get_wiki_auth_info":
        if wiki_client is None:
            try:
                wiki_client = get_wiki_client()
            except ValueError as e:
                return [TextContent(
                    type="text",
                    text=f"Configuration Error: {str(e)}\n\nUse the 'get_wiki_auth_info' tool to get authentication instructions."
                )]
    
    try:
        if name == "get_wiki_page":
            page_title = arguments.get("page_title")
            if not page_title:
                return [TextContent(
                    type="text",
                    text="Error: page_title is required"
                )]
            
            result = await wiki_client.get_page(page_title)
            if not result.get("exists"):
                return [TextContent(
                    type="text",
                    text=f"Page '{page_title}' not found in the wiki."
                )]
            
            response_text = f"Title: {result.get('title', page_title)}\n\n"
            response_text += f"Content:\n{result.get('content', '')}\n"
            if result.get('url'):
                response_text += f"\nURL: {result.get('url')}"
            
            return [TextContent(type="text", text=response_text)]
        
        elif name == "search_wiki_pages":
            query = arguments.get("query")
            if not query:
                return [TextContent(
                    type="text",
                    text="Error: query is required"
                )]
            
            limit = arguments.get("limit", 10)
            results = await wiki_client.search_pages(query, limit)
            
            if not results:
                return [TextContent(
                    type="text",
                    text=f"No pages found matching '{query}'"
                )]
            
            response_text = f"Found {len(results)} result(s) for '{query}':\n\n"
            for i, result in enumerate(results, 1):
                response_text += f"{i}. {result.get('title', 'Untitled')}\n"
                if result.get('snippet'):
                    response_text += f"   {result.get('snippet')}\n"
                if result.get('url'):
                    response_text += f"   URL: {result.get('url')}\n"
                if result.get('path'):
                    response_text += f"   Path: {result.get('path')}\n"
                response_text += "\n"
            
            return [TextContent(type="text", text=response_text)]
        
        elif name == "list_wiki_pages":
            namespace = arguments.get("namespace")
            limit = arguments.get("limit", 50)
            results = await wiki_client.list_pages(namespace, limit)
            
            if not results:
                return [TextContent(
                    type="text",
                    text="No pages found in the wiki."
                )]
            
            response_text = f"Found {len(results)} page(s):\n\n"
            for i, result in enumerate(results, 1):
                response_text += f"{i}. {result.get('title', 'Untitled')}\n"
            
            return [TextContent(type="text", text=response_text)]
        
        elif name == "get_wiki_auth_info":
            base_url = os.getenv("WIKI_BASE_URL", "")
            wiki_type = os.getenv("WIKI_TYPE", "generic").lower()
            
            if not base_url:
                return [TextContent(
                    type="text",
                    text="Error: WIKI_BASE_URL environment variable is not set."
                )]
            
            response_text = f"Authentication Information for {wiki_type.upper()} Wiki\n"
            response_text += "=" * 50 + "\n\n"
            response_text += f"Wiki URL: {base_url}\n\n"
            
            if wiki_type == "mediawiki":
                response_text += "MediaWiki Authentication Methods:\n\n"
                response_text += "1. Bot Password (Recommended for API access):\n"
                response_text += f"   • Go to: {base_url}/wiki/Special:BotPasswords\n"
                response_text += "   • Click 'Create bot password'\n"
                response_text += "   • Enter a name for your bot password (e.g., 'MCP Server')\n"
                response_text += "   • Grant the necessary permissions (read, write, etc.)\n"
                response_text += "   • Copy the generated bot password\n"
                response_text += "   • Use format: Username@BotPasswordName\n"
                response_text += "   • Example: MyUser@MCP Server\n\n"
                response_text += "2. OAuth 2.0 (If OAuth extension is installed):\n"
                response_text += f"   • OAuth Consumer Registration: {base_url}/wiki/Special:OAuthConsumerRegistration\n"
                response_text += "   • After registering, you'll get a consumer key and secret\n"
                response_text += "   • Use these to complete OAuth flow\n\n"
                response_text += "3. Personal Access Token:\n"
                response_text += f"   • Go to: {base_url}/wiki/Special:Preferences#mw-prefsection-userinfo\n"
                response_text += "   • Navigate to 'Personal access tokens' section\n"
                response_text += "   • Generate a new token with appropriate permissions\n\n"
                response_text += "After obtaining your token:\n"
                response_text += "• Set WIKI_AUTH_TOKEN environment variable to your token\n"
                response_text += "• Or update your MCP configuration file with the token\n"
                
            elif wiki_type == "confluence":
                response_text += "Confluence Authentication Methods:\n\n"
                response_text += "1. Personal Access Token (Recommended):\n"
                response_text += f"   • Go to: {base_url}/plugins/servlet/ac/io.thedocs.atlaskit.jira.jira-oauth-client-plugin/oauth/authorize?redirect_uri=\n"
                response_text += "   • Or go to Account Settings > Personal Access Tokens\n"
                response_text += "   • Create a new token with appropriate permissions\n"
                response_text += "   • Use this token as WIKI_AUTH_TOKEN\n\n"
                response_text += "2. Username/Password (Basic Auth):\n"
                response_text += "   • Set WIKI_USERNAME and WIKI_PASSWORD environment variables\n"
                response_text += "   • Note: This is less secure than tokens\n"
                
            elif wiki_type == "wikijs":
                response_text += "Wiki.js Authentication Methods:\n\n"
                response_text += "1. API Token:\n"
                response_text += f"   • Log in to: {base_url}\n"
                response_text += "   • Go to Administration > API Access\n"
                response_text += "   • Create a new API token\n"
                response_text += "   • Copy the token and use it as WIKI_AUTH_TOKEN\n\n"
                
            else:  # generic
                response_text += "Generic Wiki Authentication:\n\n"
                response_text += "Check your wiki's documentation for:\n"
                response_text += "• API token generation\n"
                response_text += "• OAuth configuration\n"
                response_text += "• Authentication endpoints\n\n"
                response_text += "Common locations:\n"
                response_text += f"• {base_url}/api/auth\n"
                response_text += f"• {base_url}/api/tokens\n"
                response_text += f"• {base_url}/settings/api\n"
            
            response_text += "\n" + "=" * 50 + "\n"
            response_text += "Current Configuration:\n"
            response_text += f"Wiki Type: {wiki_type}\n"
            has_token = "Yes (configured)" if os.getenv("WIKI_AUTH_TOKEN") else "No"
            has_username = "Yes (configured)" if os.getenv("WIKI_USERNAME") else "No"
            response_text += f"Authentication Token: {has_token}\n"
            response_text += f"Username: {has_username}\n"
            
            return [TextContent(type="text", text=response_text)]
        
        elif name == "check_wiki_env":
            # Diagnostic tool to check environment variables
            response_text = "Wiki Environment Variables Check\n"
            response_text += "=" * 50 + "\n\n"
            
            env_vars = {
                "WIKI_BASE_URL": os.getenv("WIKI_BASE_URL"),
                "WIKI_TYPE": os.getenv("WIKI_TYPE"),
                "WIKI_USERNAME": os.getenv("WIKI_USERNAME"),
                "WIKI_USER": os.getenv("WIKI_USER"),
                "WIKI_PASSWORD": os.getenv("WIKI_PASSWORD"),
                "WIKI_PASS": os.getenv("WIKI_PASS"),
                "WIKI_AUTH_TOKEN": os.getenv("WIKI_AUTH_TOKEN")
            }
            
            for var_name, var_value in env_vars.items():
                if var_value:
                    if "PASSWORD" in var_name or "TOKEN" in var_name:
                        # Mask sensitive values
                        masked = "*" * min(len(var_value), 20)
                        response_text += f"{var_name}: {masked} (set, {len(var_value)} chars)\n"
                    else:
                        response_text += f"{var_name}: {var_value}\n"
                else:
                    response_text += f"{var_name}: NOT SET\n"
            
            response_text += "\n" + "=" * 50 + "\n"
            response_text += "All Environment Variables (first 20):\n"
            all_env = dict(os.environ)
            wiki_env = {k: v for k, v in all_env.items() if "WIKI" in k.upper()}
            if wiki_env:
                for k, v in list(wiki_env.items())[:20]:
                    if "PASSWORD" in k or "TOKEN" in k:
                        response_text += f"{k}: {'*' * min(len(v), 20)}\n"
                    else:
                        response_text += f"{k}: {v}\n"
            else:
                response_text += "No WIKI_* environment variables found\n"
            
            return [TextContent(type="text", text=response_text)]
        
        elif name == "good_morning_report":
            project = arguments.get("project", "360")
            team = arguments.get("team", "Core-Process-platform")
            current_date = datetime.now().strftime("%Y-%m-%d")
            filename = "outputs/morning/morning_report.md"
            
            # Return instructions for the agent to gather data from Azure DevOps and save as markdown
            instructions = f"""Generate a morning report for the Process Platform team and save it as a markdown file.

**Time window:** Use "last 2 workdays" (not 48 hours). Workdays = weekdays (Mon–Fri); exclude weekends. Cutoff = start of the day that is 2 workdays ago (e.g. if today is Tuesday, cutoff = Friday 00:00 UTC; if today is Monday, cutoff = Thursday 00:00 UTC). Filter work items changed, comments, and sprint closed count by this cutoff.

Please follow these steps:

1. Get the current iteration for team '{team}' in project '{project}':
   - Use: mcp_azure-devops_work_list_team_iterations with project="{project}", team="{team}", timeframe="current"

2. Get work items for the current iteration:
   - Use: mcp_azure-devops_wit_get_work_items_for_iteration with the iteration ID from step 1

3. Fetch detailed information for the work items:
   - Extract work item IDs from step 2
   - Use: mcp_azure-devops_wit_get_work_items_batch_by_ids to get full details
   - Request these fields: System.Title, System.State, System.AssignedTo, System.WorkItemType, System.CreatedDate, System.ChangedDate

4. Check for items requiring attention (mentions/tags without responses):
   - Get work items assigned to you: mcp_azure-devops_wit_my_work_items with project="{project}", type="assignedtome"
   - **IMPORTANT:** Also get "My activity" items (includes items where you're @mentioned but NOT assigned):
     mcp_azure-devops_wit_my_work_items with project="{project}", type="myactivity", top=30
   - For BOTH assigned items AND myactivity items, get comments: mcp_azure-devops_wit_list_work_item_comments
   - Identify items requiring attention where:
     * You are mentioned/tagged in comments (check comment.mentions array, or @mentions in comment text)
     * The comment is recent (within last 7 days)
     * You haven't responded yet (no subsequent comment from you after the mention)
     * Work items assigned to you with recent comments from others (last 2 workdays) but no response from you
   - **Include items from myactivity** even if not assigned to you – e.g. #411840 where you were @mentioned
   - Focus on work items that are Active, New, or Resolved (not Closed)

5. Fetch GitHub development activities (commits and pull requests):
   - For each repo in config (or default te-industry-public360/core-bl): Use mcp_github_list_commits with owner, repo, sha="master" (or branch from config), perPage=30.
   - **MANDATORY – Team filter:** The core-bl repo is shared across teams. The Development activities section must show ONLY Process Platform team work. Read config.json (or config.example.json) → morning_report.team_github_users for GitHub login names. Filter commits where author.login is in team_github_users; filter PRs where user.login is in team_github_users. Exclude all commits and PRs from non-team members. If team_github_users is missing or empty, show a note that team filter is not configured.
   - Filter commits by date: commit.commit.author.date within the **last 2 workdays** (same cutoff as work items; weekdays only; exclude weekends).
   - For each repo: Use mcp_github_list_pull_requests with owner, repo, state="open", per_page=50 (fetch more to find team PRs). Filter to include ONLY PRs where user.login is in team_github_users.
   - Format: Commits table (Date | Author | Message | Link); PRs table (PR | Title | Author | Branch | Link). Section header: "Development activities – Process Platform team only".

6. Format a comprehensive morning report in markdown format with:
   - Title: "Morning Report - {current_date}"
   - **Recent-activity window:** Last 2 workdays (not 48 hours)
   - Current iteration name and dates
   - **REQUIRES ATTENTION** section (at the top) listing:
     * Work items where you're mentioned but haven't responded
     * Work items assigned to you with recent activity requiring response
     * Include work item ID, title, who mentioned/tagged you, and when
     * **IMPORTANT:** Include direct links to each work item in format: [##workItemId - Title](https://tieto-si.visualstudio.com/{project}/_workitems/edit/workItemId)
   - Summary of work items by state (New, Active, Resolved, Closed, etc.)
   - Active work items (in progress) - **include links to each work item**
   - Recently resolved items - **include links to each work item**
   - Recent activity (items changed in last 2 workdays) - **include links to each work item**. Workdays = weekdays (Mon–Fri); cutoff = start of the day 2 workdays ago (e.g. Tuesday → cutoff = Friday 00:00 UTC).
   - **Development activities (last 2 workdays) – Process Platform team only** – include ONLY commits and PRs from team_github_users:
     * Commits: table with Date | Author | Message | Repo | Link (html_url) – exclude non-team authors
     * Pull requests: table with PR # | Title | Author | Branch | Link (html_url) – exclude non-team authors
   - Brief overview of what the team is working on
   - **For ALL work items mentioned in the report, format them as clickable links: [##workItemId - Title](https://tieto-si.visualstudio.com/{project}/_workitems/edit/workItemId)**

7. Save the report as a markdown file:
   - Filename: "{filename}"
   - Use the write tool to save the formatted markdown content
   - Save it in the current workspace directory

Keep the report concise and actionable - aim for 1-2 minutes of reading time. Prioritize the "Requires Attention" section."""
            
            return [TextContent(type="text", text=instructions)]
        
        else:
            return [TextContent(
                type="text",
                text=f"Unknown tool: {name}"
            )]
    
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Error: {str(e)}"
        )]


async def main():
    """Main entry point"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())

