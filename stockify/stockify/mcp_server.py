"""Stockify MCP Server — Model Context Protocol for Stockify intelligence.

Allows AI assistants to query Stockify data directly.
"""
from __future__ import annotations

import json
from typing import Any

import httpx

STOCKIFY_BASE = "https://feedify.egoic.ai"


async def call_tool(tool: str, args: dict[str, Any]) -> Any:
    """Call a Stockify MCP tool."""
    async with httpx.AsyncClient() as client:
        if tool == "stockify_health":
            r = await client.get(f"{STOCKIFY_BASE}/api/health", timeout=10)
            return r.json()

        elif tool == "stockify_signals":
            limit = args.get("limit", 20)
            domain = args.get("domain")
            url = f"{STOCKIFY_BASE}/api/signals?limit={limit}"
            if domain:
                url += f"&domain={domain}"
            r = await client.get(url, timeout=10)
            return r.json()

        elif tool == "stockify_insiders":
            limit = args.get("limit", 20)
            r = await client.get(f"{STOCKIFY_BASE}/api/insiders?limit={limit}", timeout=10)
            return r.json()

        elif tool == "stockify_frontier":
            limit = args.get("limit", 20)
            signal_type = args.get("signal_type")
            lab = args.get("lab")
            url = f"{STOCKIFY_BASE}/api/frontier?limit={limit}"
            if signal_type:
                url += f"&signal_type={signal_type}"
            if lab:
                url += f"&lab={lab}"
            r = await client.get(url, timeout=10)
            return r.json()

        elif tool == "stockify_graph":
            r = await client.get(f"{STOCKIFY_BASE}/api/frontier/graph", timeout=15)
            return r.json()

        elif tool == "stockify_chat":
            message = args.get("message", "")
            context = args.get("context", "general")
            async with client.stream(
                "POST",
                f"{STOCKIFY_BASE}/api/chat",
                json={"message": message, "context": context},
                timeout=60,
            ) as r:
                return await r.aread()

        elif tool == "stockify_feeds":
            r = await client.get(f"{STOCKIFY_BASE}/api/feeds", timeout=10)
            return r.json()

        elif tool == "stockify_sources":
            r = await client.get(f"{STOCKIFY_BASE}/api/sources", timeout=10)
            return r.json()

        else:
            return {"error": f"Unknown tool: {tool}"}


# Tool definitions for MCP
TOOLS = [
    {
        "name": "stockify_health",
        "description": "Get Stockify system health status",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "stockify_signals",
        "description": "List recent signals from Stockify",
        "inputSchema": {
            "type": "object",
            "properties": {
                "limit": {"type": "integer", "description": "Number of signals to return (default 20)"},
                "domain": {"type": "string", "description": "Filter by domain (quantum, agents, insiders, etc.)"},
            },
        },
    },
    {
        "name": "stockify_insiders",
        "description": "List insider trading signals (SEC verified + X discovery)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "limit": {"type": "integer", "description": "Number of signals to return (default 20)"},
            },
        },
    },
    {
        "name": "stockify_frontier",
        "description": "List frontier quantum × AGI signals",
        "inputSchema": {
            "type": "object",
            "properties": {
                "limit": {"type": "integer", "description": "Number of signals to return (default 20)"},
                "signal_type": {"type": "string", "description": "Filter by type (CONVERGENCE, AGI_LEAD, QUANTUM_LEAD, etc.)"},
                "lab": {"type": "string", "description": "Filter by lab (IonQ, xAI, Anthropic, etc.)"},
            },
        },
    },
    {
        "name": "stockify_graph",
        "description": "Get the full frontier intelligence graph (persons, signals, convergences)",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "stockify_chat",
        "description": "Chat with Stockify AI about any data",
        "inputSchema": {
            "type": "object",
            "properties": {
                "message": {"type": "string", "description": "Question or prompt"},
                "context": {"type": "string", "description": "Context: general, insiders, frontier"},
            },
            "required": ["message"],
        },
    },
    {
        "name": "stockify_feeds",
        "description": "List configured feeds",
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "stockify_sources",
        "description": "List data sources and their status",
        "inputSchema": {"type": "object", "properties": {}},
    },
]
