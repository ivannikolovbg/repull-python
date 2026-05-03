"""Repull quick start: list your most recent reservations.

Run with:
    REPULL_API_KEY=sk_live_... python examples/quickstart.py
"""
import asyncio
import os

from repull import AuthenticatedClient
from repull.api.reservations import list_reservations


async def main() -> None:
    client = AuthenticatedClient(
        base_url="https://api.repull.dev",
        token=os.environ["REPULL_API_KEY"],
    )
    async with client as c:
        page = await list_reservations.asyncio(client=c, limit=10)

    if page is None:
        print("No reservations returned (check your API key).")
        return

    rows = list(page.data) if page.data else []
    if not rows:
        print("Page returned no rows.")
        return

    print(f"{'id':10s}  {'check_in':12s} -> {'check_out':12s}  {'platform':14s} {'status'}")
    for r in rows:
        # Wire fields are camelCase; the SDK exposes them as snake_case Python
        # attributes. Anything not in the canonical schema lives on
        # additional_properties (raw camelCase keys).
        d = r.additional_properties
        print(
            f"{str(r.id):10s}  {str(r.check_in):12s} -> {str(r.check_out):12s}  "
            f"{str(r.platform):14s} {d.get('status', '?')}"
        )


if __name__ == "__main__":
    asyncio.run(main())
