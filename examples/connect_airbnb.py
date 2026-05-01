"""Mint a Repull Connect session for Airbnb and poll for the linked account.

Flow:
  1. Create a Connect session — Repull returns an `oauthUrl` you redirect the
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
from repull.api.connect import get_v1_connect_provider, post_v1_connect_provider
from repull.models.post_v1_connect_provider_body import PostV1ConnectProviderBody
from repull.models.post_v1_connect_provider_body_access_type import (
    PostV1ConnectProviderBodyAccessType,
)


async def main() -> None:
    client = AuthenticatedClient(
        base_url="https://api.repull.dev",
        token=os.environ["REPULL_API_KEY"],
    )

    body = PostV1ConnectProviderBody(
        redirect_url="https://yourapp.example.com/airbnb/return",
        access_type=PostV1ConnectProviderBodyAccessType.FULL_ACCESS,
    )

    async with client as c:
        session = await post_v1_connect_provider.asyncio(
            provider="airbnb", client=c, body=body
        )
        print("Send the property manager to:")
        print(f"  {session.oauth_url}")
        print(f"  session_id={session.session_id}  expires_at={session.expires_at}")

        status = await get_v1_connect_provider.asyncio(provider="airbnb", client=c)
        print(f"Current Airbnb connection status: {status.status}")


if __name__ == "__main__":
    asyncio.run(main())
