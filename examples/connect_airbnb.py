"""Mint a Repull Connect session for Airbnb and poll for the linked account.

Flow:
  1. Create a Connect session — Repull returns a hosted `url` you redirect the
     property manager to.
  2. They land on `connect.repull.dev`, authorise Airbnb, and bounce back to
     your `redirect_url`.
  3. Poll the connection status to confirm linkage.

Run with:
    REPULL_API_KEY=sk_live_... python examples/connect_airbnb.py
"""

import asyncio
import os

from repull import AuthenticatedClient
from repull.api.connect import create_connect_session, get_connect_status
from repull.models.create_connect_session_body import CreateConnectSessionBody


async def main() -> None:
    client = AuthenticatedClient(
        base_url="https://api.repull.dev",
        token=os.environ["REPULL_API_KEY"],
    )

    body = CreateConnectSessionBody(
        redirect_url="https://yourapp.example.com/airbnb/return",
        allowed_providers=["airbnb"],
    )

    async with client as c:
        session = await create_connect_session.asyncio(client=c, body=body)
        print("Send the property manager to:")
        print(f"  {session.url}")
        print(f"  session_id={session.session_id}  expires_at={session.expires_at}")

        status = await get_connect_status.asyncio(provider="airbnb", client=c)
        print(f"Current Airbnb connection status: {status.status}")


if __name__ == "__main__":
    asyncio.run(main())
