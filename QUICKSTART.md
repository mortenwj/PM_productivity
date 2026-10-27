# Quick Start Guide

## 1. Install Dependencies

**First time (Windows):** install uv and sync the project environment:

```powershell
winget install astral-sh.uv --accept-package-agreements --scope user
.\toolkit\scripts\bootstrap-python.ps1
```

uv installs Python 3.12 if needed and creates `.venv/` from `pyproject.toml` + `uv.lock`.

**Run any Python script** from the repo root:

```powershell
uv run python toolkit/scripts/server.py
```

**Flow AI spike (S1 dry-run):**

```powershell
uv run python projects/process-platform/flow/ai-model-creator-spike/generate_draft.py --scenario s1-permit --dry-run
# or
.\toolkit\scripts\run-ai-spike.ps1 --scenario s1-permit --dry-run
```

After pulling dependency changes: `uv sync`

**Windows Note:** Do not rely on bare `python` — use `uv run python ...` so project packages (`openai`, `mcp`, etc.) resolve correctly.

## 2. Configure Your Wiki Connection

### Option A: Using Environment Variables (Recommended)

Set these environment variables before running the server:

**Windows (PowerShell):**
```powershell
$env:WIKI_BASE_URL="https://your-wiki.example.com"
$env:WIKI_TYPE="mediawiki"  # or "confluence", "wikijs", "generic"
$env:WIKI_AUTH_TOKEN="your-token-here"
```

**Windows (CMD):**
```cmd
set WIKI_BASE_URL=https://your-wiki.example.com
set WIKI_TYPE=mediawiki
set WIKI_AUTH_TOKEN=your-token-here
```

**Linux/Mac:**
```bash
export WIKI_BASE_URL="https://your-wiki.example.com"
export WIKI_TYPE="mediawiki"
export WIKI_AUTH_TOKEN="your-token-here"
```

### Option B: Using Setup Script

Run the interactive setup:

```bash
python setup.py
```

This will create a `config.json` file. Note: You'll still need to set environment variables or modify the server to read from the config file.

## 3. Test the Server

Run the server directly to test:

```bash
python server.py
```

The server uses stdio transport, so it expects JSON-RPC messages on stdin/stdout.

## 4. Configure MCP Client

### Claude Desktop

Add to your Claude Desktop configuration file (location varies by OS):

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "wiki": {
      "command": "python",
      "args": ["C:\\path\\to\\server.py"],
      "env": {
        "WIKI_BASE_URL": "https://your-wiki.example.com",
        "WIKI_TYPE": "mediawiki",
        "WIKI_AUTH_TOKEN": "your-token-here"
      }
    }
  }
}
```

### Other MCP Clients

The server uses stdio transport, so configure your MCP client to:
- Command: `python`
- Args: `["/path/to/server.py"]`
- Environment variables: Set `WIKI_BASE_URL`, `WIKI_TYPE`, and authentication variables

## 5. Verify Connection

Once configured, you should be able to use these tools in your MCP client:

- `get_wiki_page` - Retrieve a page by title
- `search_wiki_pages` - Search for pages
- `list_wiki_pages` - List available pages

## Troubleshooting

### "WIKI_BASE_URL environment variable is required"
- Make sure you've set the `WIKI_BASE_URL` environment variable
- Check that the variable is set in the same environment where the server runs

### Authentication Errors
- Verify your token/credentials are correct
- Check if your wiki requires specific authentication headers
- For MediaWiki, ensure OAuth extension is installed

### Connection Timeouts
- Verify the wiki URL is accessible from your machine
- Check firewall and network settings
- Ensure the wiki API is enabled

### Import Errors
- Make sure you've installed all dependencies: `pip install -r requirements.txt`
- Verify Python version is 3.8 or higher

## Next Steps

- Customize the `WikiClient` class for your specific wiki API
- Add more tools (e.g., create page, update page, delete page)
- Implement caching for better performance
- Add logging for debugging

