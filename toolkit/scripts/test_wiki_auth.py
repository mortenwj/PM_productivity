#!/usr/bin/env python3
"""
Test script to verify wiki authentication
"""

import asyncio
import os
import httpx
from urllib.parse import urljoin


async def test_mediawiki_auth():
    """Test MediaWiki authentication methods"""
    base_url = os.getenv("WIKI_BASE_URL", "").rstrip('/')
    username = os.getenv("WIKI_USERNAME", "")
    password = os.getenv("WIKI_PASSWORD", "")
    auth_token = os.getenv("WIKI_AUTH_TOKEN", "")
    
    if not base_url:
        print("❌ ERROR: WIKI_BASE_URL not set")
        return False
    
    print(f"Testing authentication to: {base_url}")
    print("=" * 60)
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        # Test 1: Check if API is accessible (no auth required)
        print("\n1. Testing API accessibility...")
        try:
            api_url = f"{base_url}/api.php"
            params = {
                "action": "query",
                "meta": "siteinfo",
                "format": "json",
                "formatversion": "2"
            }
            response = await client.get(api_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if "query" in data:
                site_name = data["query"].get("general", {}).get("sitename", "Unknown")
                print(f"   ✅ API is accessible")
                print(f"   📝 Site name: {site_name}")
            else:
                print(f"   ⚠️  API responded but format unexpected")
                print(f"   Response: {response.text[:200]}")
        except Exception as e:
            print(f"   ❌ API not accessible: {e}")
            return False
        
        # Test 2: Try login with username/password (Bot Password format)
        if username and password:
            print(f"\n2. Testing Bot Password authentication...")
            print(f"   Username: {username}")
            print(f"   Password: {'*' * len(password)}")
            
            try:
                # First, get login token
                login_token_params = {
                    "action": "query",
                    "meta": "tokens",
                    "type": "login",
                    "format": "json",
                    "formatversion": "2"
                }
                response = await client.get(api_url, params=login_token_params)
                response.raise_for_status()
                token_data = response.json()
                
                login_token = token_data.get("query", {}).get("tokens", {}).get("logintoken", "")
                
                if not login_token:
                    print(f"   ⚠️  Could not get login token")
                else:
                    # Try to login
                    login_params = {
                        "action": "login",
                        "lgname": username,
                        "lgpassword": password,
                        "lgtoken": login_token,
                        "format": "json",
                        "formatversion": "2"
                    }
                    response = await client.post(api_url, data=login_params)
                    response.raise_for_status()
                    login_data = response.json()
                    
                    if login_data.get("login", {}).get("result") == "Success":
                        print(f"   ✅ Login successful!")
                        user_info = login_data.get("login", {})
                        print(f"   👤 User: {user_info.get('lgusername', 'Unknown')}")
                    else:
                        result = login_data.get("login", {}).get("result", "Unknown")
                        print(f"   ❌ Login failed: {result}")
                        if "reason" in login_data.get("login", {}):
                            print(f"   Reason: {login_data['login']['reason']}")
            except Exception as e:
                print(f"   ❌ Login test failed: {e}")
        
        # Test 3: Try Bearer token authentication (if token provided)
        if auth_token and auth_token != "your-token-here":
            print(f"\n3. Testing Bearer token authentication...")
            headers = {"Authorization": f"Bearer {auth_token}"}
            try:
                params = {
                    "action": "query",
                    "meta": "userinfo",
                    "format": "json",
                    "formatversion": "2"
                }
                response = await client.get(api_url, headers=headers, params=params)
                response.raise_for_status()
                data = response.json()
                
                if "query" in data and "userinfo" in data["query"]:
                    userinfo = data["query"]["userinfo"]
                    if userinfo.get("id") != 0:
                        print(f"   ✅ Bearer token authentication successful!")
                        print(f"   👤 User ID: {userinfo.get('id')}")
                        print(f"   👤 Username: {userinfo.get('name', 'Unknown')}")
                    else:
                        print(f"   ⚠️  Bearer token accepted but user is anonymous")
                else:
                    print(f"   ⚠️  Bearer token test - unexpected response format")
            except httpx.HTTPStatusError as e:
                if e.response.status_code == 401:
                    print(f"   ❌ Bearer token authentication failed (401 Unauthorized)")
                    print(f"   ℹ️  MediaWiki typically doesn't use Bearer tokens")
                else:
                    print(f"   ❌ Bearer token test failed: {e}")
            except Exception as e:
                print(f"   ❌ Bearer token test error: {e}")
        elif auth_token == "your-token-here":
            print(f"\n3. Skipping Bearer token test (placeholder token detected)")
        
        # Test 4: Try to list pages (requires authentication)
        print(f"\n4. Testing page listing (requires auth)...")
        try:
            params = {
                "action": "query",
                "list": "allpages",
                "aplimit": "5",
                "format": "json",
                "formatversion": "2"
            }
            
            # Try with Bearer token if available
            headers = {}
            if auth_token and auth_token != "your-token-here":
                headers["Authorization"] = f"Bearer {auth_token}"
            
            response = await client.get(api_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            if "query" in data and "allpages" in data["query"]:
                pages = data["query"]["allpages"]
                if pages:
                    print(f"   ✅ Successfully retrieved {len(pages)} page(s):")
                    for page in pages[:5]:
                        print(f"      - {page.get('title', 'Unknown')}")
                else:
                    print(f"   ⚠️  API accessible but no pages found (wiki might be empty)")
            elif "error" in data:
                error = data["error"]
                print(f"   ❌ API error: {error.get('code', 'Unknown')}")
                print(f"   Message: {error.get('info', 'No details')}")
                if error.get("code") == "readapidenied":
                    print(f"   ℹ️  This usually means authentication is required")
            else:
                print(f"   ⚠️  Unexpected response format")
        except Exception as e:
            print(f"   ❌ Page listing test failed: {e}")
    
    print("\n" + "=" * 60)
    print("Authentication test complete!")
    print("\nRecommendations:")
    print("1. For MediaWiki, use Bot Passwords (username@botname format)")
    print("2. Set WIKI_USERNAME to your username")
    print("3. Set WIKI_PASSWORD to your bot password")
    print("4. Remove or update WIKI_AUTH_TOKEN (MediaWiki doesn't use Bearer tokens)")
    
    return True


if __name__ == "__main__":
    # Load environment variables from mcp.json if needed
    # For now, rely on environment variables set by MCP server
    asyncio.run(test_mediawiki_auth())




