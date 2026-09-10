#!/usr/bin/env python3
"""Stockify MCP Server — stdio-based Model Context Protocol server.

Usage:
    python -m stockify.mcp_stdio

Or configure in your MCP client:
{
  "mcpServers": {
    "stockify": {
      "command": "python",
      "args": ["-m", "stockify.mcp_stdio"],
      "env": {
        "STOCKIFY_URL": "https://feedify.egoic.ai"
      }
    }
  }
}
"""
from __future__ import annotations

import json
import os
import sys
from typing import Any

import httpx

STOCKIFY_URL = os.getenv("STOCKIFY_URL", "https://feedify.egoic.ai")


async def handle_request(method: str, params: dict[str, Any]) -> Any:
    """Handle an MCP JSON-RPC request."""
    if method == "initialize":
        return {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": "stockify", "version": "1.0.0"},
        }

    elif method == "tools/list":
        return {
            "tools": [
                {
                    "name": "stockify_health",
                    "description": "Get Stockify system health status (signals, feeds, sources)",
                    "inputSchema": {"type": "object", "properties": {}},
                },
                {
                    "name": "stockify_signals",
                    "description": "List recent signals from Stockify. Filter by domain (quantum, agents, insiders, etc.)",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "limit": {"type": "integer", "description": "Number of signals (default 20)"},
                            "domain": {"type": "string", "description": "Filter: quantum, agents, insiders, ios, commerce"},
                        },
                    },
                },
                {
                    "name": "stockify_insiders",
                    "description": "List insider trading signals — SEC verified filings and X discovery",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "limit": {"type": "integer", "description": "Number of signals (default 20)"},
                        },
                    },
                },
                {
                    "name": "stockify_frontier",
                    "description": "List quantum × AGI frontier signals from researchers at IonQ, xAI, Anthropic, OpenAI, DeepMind, Axiom",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "limit": {"type": "integer", "description": "Number of signals (default 20)"},
                            "signal_type": {"type": "string", "description": "Filter: CONVERGENCE, AGI_LEAD, QUANTUM_LEAD, OBSERVATION"},
                            "lab": {"type": "string", "description": "Filter: IonQ, xAI, Anthropic, OpenAI, DeepMind, Axiom, Meta MSL"},
                        },
                    },
                },
                {
                    "name": "stockify_graph",
                    "description": "Get the full frontier intelligence graph — persons, signals, convergences across 10 labs",
                    "inputSchema": {"type": "object", "properties": {}},
                },
                {
                    "name": "stockify_chat",
                    "description": "Chat with Stockify AI about any data — ask about signals, people, labs, convergence, insider activity",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "message": {"type": "string", "description": "Your question"},
                            "context": {"type": "string", "description": "Context: general, insiders, frontier"},
                        },
                        "required": ["message"],
                    },
                },
                {
                    "name": "stockify_feeds",
                    "description": "List configured feeds and their prompts",
                    "inputSchema": {"type": "object", "properties": {}},
                },
                {
                    "name": "stockify_sources",
                    "description": "List data sources and their ingestion status",
                    "inputSchema": {"type": "object", "properties": {}},
                },
            ]
        }

    elif method == "tools/call":
        tool_name = params.get("name", "")
        arguments = params.get("arguments", {})
        result = await call_tool(tool_name, arguments)
        return {"content": [{"type": "text", "text": json.dumps(result, indent=2)}]}

    return {"error": {"code": -32601, "message": f"Unknown method: {method}"}}


async def call_tool(tool: str, args: dict[str, Any]) -> Any:
    """Call a Stockify API endpoint."""
    async with httpx.AsyncClient() as client:
        if tool == "stockify_health":
            r = await client.get(f"{STOCKIFY_URL}/api/health", timeout=10)
            return r.json()
        elif tool == "stockify_signals":
            limit = args.get("limit", 20)
            domain = args.get("domain")
            url = f"{STOCKIFY_URL}/api/signals?limit={limit}"
            if domain:
                url += f"&domain={domain}"
            r = await client.get(url, timeout=10)
            return r.json()
        elif tool == "stockify_insiders":
            limit = args.get("limit", 20)
            r = await client.get(f"{STOCKIFY_URL}/api/insiders?limit={limit}", timeout=10)
            return r.json()
        elif tool == "stockify_frontier":
            limit = args.get("limit", 20)
            signal_type = args.get("signal_type")
            lab = args.get("lab")
            url = f"{STOCKIFY_URL}/api/frontier?limit={limit}"
            if signal_type:
                url += f"&signal_type={signal_type}"
            if lab:
                url += f"&lab={lab}"
            r = await client.get(url, timeout=10)
            return r.json()
        elif tool == "stockify_graph":
            r = await client.get(f"{STOCKIFY_URL}/api/frontier/graph", timeout=15)
            return r.json()
        elif tool == "stockify_chat":
            message = args.get("message", "")
            context = args.get("context", "general")
            r = await client.post(
                f"{STOCKIFY_URL}/api/chat",
                json={"message": message, "context": context},
                timeout=60,
            )
            return r.json()
        elif tool == "stockify_feeds":
            r = await client.get(f"{STOCKIFY_URL}/api/feeds", timeout=10)
            return r.json()
        elif tool == "stockify_sources":
            r = await client.get(f"{STOCKIFY_URL}/api/sources", timeout=10)
            return r.json()
        else:
            return {"error": f"Unknown tool: {tool}"}


def main():
    """Run the MCP server over stdio."""
    import asyncio

    async def run():
        while True:
            try:
                line = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)
                if not line:
                    break

                request = json.loads(line)
                method = request.get("method", "")
                params = request.get("params", {})
                req_id = request.get("id")

                result = await handle_request(method, params)

                response = {"jsonrpc": "2.0", "result": result}
                if req_id is not None:
                    response["id"] = req_id

                sys.stdout.write(json.dumps(response) + "\n")
                sys.stdout.flush()
            except Exception as e:
                error_response = {
                    "jsonrpc": "2.0",
                    "error": {"code": -32603, "message": str(e)},
                }
                if req_id is not None:
                    error_response["id"] = req_id
                sys.stdout.write(json.dumps(error_response) + "\n")
                sys.stdout.flush()

    asyncio.run(run())


if __name__ == "__main__":
    main()
