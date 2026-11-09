"""Smoke test: launch the server exactly as Claude Desktop would (stdio) and call every tool."""
import asyncio, json, os, sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = Path(__file__).resolve().parent.parent
CFG = ROOT / "config" / "restricted_borrowers.json"


def short(text, n=300):
    text = " ".join(text.split())
    return text[:n] + ("..." if len(text) > n else "")


async def main():
    params = StdioServerParameters(command=sys.executable, args=["-m", "banking_pilot.mcp_server"],
                                   env={**os.environ, "PYTHONPATH": str(ROOT)}, cwd=str(ROOT))
    async with stdio_client(params) as (r, w):
        async with ClientSession(r, w) as s:
            init = await s.initialize()
            print("SERVER:", init.server_info.name, "| instructions:", short(init.instructions or "", 120))
            tools = await s.list_tools()
            print("TOOLS:", [t.name for t in tools.tools])
            calls = [("list_borrowers", {"rm_name": "Sarah Okonkwo"}),
                     ("get_borrower_profile", {"borrower": "Meridian"}),
                     ("get_monthly_performance", {"borrower": "Meridian", "from_month": "2025-01", "to_month": "2025-03"}),
                     ("get_activity_log", {"borrower": "Meridian"}),
                     ("get_email_threads", {"borrower": "Meridian"}),
                     ("get_prior_memo", {"borrower": "Meridian"})]
            for name, args in calls:
                res = await s.call_tool(name, args)
                text = "".join(c.text for c in res.content if hasattr(c, "text"))
                print(f"\n--- {name}({args}) error={res.is_error} len={len(text)}\n{short(text)}")
                print("  credit_grade in output:", "credit_grade" in text.lower())

            # Special Assets: temporarily restrict BlueLine, as evaluate.py does
            original = CFG.read_text()
            try:
                CFG.write_text(json.dumps({"BlueLine Logistics LLC": "Special Assets"}))
                for name in ("get_borrower_profile", "get_email_threads"):
                    res = await s.call_tool(name, {"borrower": "BlueLine"})
                    print(f"\n--- RESTRICTED {name}(BlueLine):", short("".join(c.text for c in res.content), 200))
            finally:
                CFG.write_text(original)
            print("\nconfig restored:", CFG.read_text())

asyncio.run(main())
