#!/usr/bin/env python3
"""
Simple script to generate the morning report.
This can be run directly or invoked via the MCP tool.
"""

import sys
import os

# Add the current directory to the path so we can import server
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# This script will trigger the good_morning_report tool
# Since the tool is designed to work through MCP, we'll provide instructions
# for the easiest way to invoke it

print("""
To generate your morning report, you have several options:

1. **In Cursor/Agent Interface (Easiest):**
   Simply type: "good morning" or "good_morning_report"
   The agent will automatically generate the report with today's date.

2. **Direct MCP Tool Call:**
   The tool is available as 'good_morning_report' in your MCP server.
   You can call it with optional parameters:
   - team: "Core-Process-platform" (default)
   - project: "360" (default)

3. **Via Command Line (if you set up MCP CLI):**
   You would need an MCP client CLI tool to call it directly.

The report will be saved as: outputs/morning/morning_report.md
""")

if __name__ == "__main__":
    print("\nNote: This script is informational. To actually generate the report,")
    print("use the 'good morning' command in your Cursor agent interface.")
    print("\nThe MCP server must be running and configured for this to work.")












