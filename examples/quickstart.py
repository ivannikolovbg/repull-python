"""Repull quick start: list your most recent reservations.

Run with:
    REPULL_API_KEY=sk_live_... python examples/quickstart.py
"""
import asyncio
import os

from repull import AuthenticatedClient
from repull.api.reservations import get_v1_reservations


async def main() -> None:
    client = AuthenticatedClient(
        base_url="https://api.repull.dev",
        token=os.environ["REPULL_API_KEY"],
    )
    async with client as c:
        page = await get_v1_reservations.asyncio(client=c, limit=10)

    if page is None:
        print("No reservations returned (check your API key).")
        return

    rows = list(page.data) if page.data else []
    if not rows:
        print("Page returned no rows.")
        return

    print(f"{'id':10s}  {'check_in':12s} -> {'check_out':12s}  {'platform':14s} {'status'}")
    for r in rows:
        # Spec currently types this list as Property; the runtime payload is a
        # reservation envelope. Read fields off the parsed object first, fall
        # back to the raw dict via additional_properties for everything else.
        d = r.additional_properties
        rid = getattr(r, "id", None) or d.get("id")
        print(
            f"{str(rid):10s}  {d.get('checkIn', '?'):12s} -> {d.get('checkOut', '?'):12s}  "
            f"{d.get('platform', '?'):14s} {d.get('status', '?')}"
        )


if __name__ == "__main__":
    asyncio.run(main())
