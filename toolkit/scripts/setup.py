#!/usr/bin/env python3
"""
Setup helper script for Wiki MCP Server
Helps configure environment variables interactively
"""

import os
import json
from pathlib import Path


def setup_config():
    """Interactive setup for wiki configuration"""
    print("Wiki MCP Server Setup")
    print("=" * 40)
    print()
    
    config = {}
    
    # Base URL
    base_url = input("Enter your wiki base URL (e.g., https://wiki.example.com): ").strip()
    if not base_url:
        print("Error: Base URL is required")
        return
    config["base_url"] = base_url
    
    # Wiki Type
    print("\nWiki types:")
    print("1. MediaWiki")
    print("2. Confluence")
    print("3. Wiki.js")
    print("4. Generic REST API")
    wiki_type_choice = input("Select wiki type (1-4, default: 4): ").strip() or "4"
    
    wiki_types = {"1": "mediawiki", "2": "confluence", "3": "wikijs", "4": "generic"}
    config["type"] = wiki_types.get(wiki_type_choice, "generic")
    
    # Authentication
    print("\nAuthentication method:")
    print("1. Token/Bearer")
    print("2. Username/Password (Basic Auth)")
    auth_choice = input("Select authentication method (1-2): ").strip()
    
    if auth_choice == "1":
        token = input("Enter authentication token: ").strip()
        if token:
            config["auth_token"] = token
    elif auth_choice == "2":
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()
        if username:
            config["username"] = username
        if password:
            config["password"] = password
    
    # Save config
    config_file = Path("config.json")
    with open(config_file, "w") as f:
        json.dump({"wiki": config}, f, indent=2)
    
    print(f"\nConfiguration saved to {config_file}")
    print("\nTo use this configuration, set environment variables:")
    print(f"  export WIKI_BASE_URL=\"{config['base_url']}\"")
    print(f"  export WIKI_TYPE=\"{config['type']}\"")
    if config.get("auth_token"):
        print(f"  export WIKI_AUTH_TOKEN=\"{config['auth_token']}\"")
    if config.get("username"):
        print(f"  export WIKI_USERNAME=\"{config['username']}\"")
    if config.get("password"):
        print(f"  export WIKI_PASSWORD=\"{config['password']}\"")


if __name__ == "__main__":
    setup_config()

