# Repull Python SDK

> **Status:** v0.2.0 — beta. API surface stable; minor renames possible before 1.0.

Typed Python client for [api.repull.dev](https://api.repull.dev) — the unified API for vacation-rental tech (50+ PMS platforms, Airbnb / Booking.com / VRBO / Plumguide channels, AI ops, white-label OAuth Connect).

Async by default. Generated from OpenAPI. Fully typed (`attrs` + `httpx`).

## Install

The PyPI package name `repull` is reserved but not yet published. For now, install from git:

```bash
pip install git+https://github.com/ivannikolovbg/repull-python.git
```

Once published:

```bash
pip install repull
```

Requires Python 3.10+.

## Quick start

```python
import asyncio
import os

from repull import AuthenticatedClient
from repull.api.reservations import list_reservations

async def main():
    client = AuthenticatedClient(
        base_url="https://api.repull.dev",
        token=os.environ["REPULL_API_KEY"],
    )
    async with client as c:
        page = await list_reservations.asyncio(client=c, limit=10)

    for r in page.data:
        print(r.id, r.check_in, r.check_out, r.platform)

asyncio.run(main())
```

There is also a sync flavour for every endpoint — drop the `async with` and call `list_reservations.sync(...)` instead.

## Authentication

Every call goes through `AuthenticatedClient(token=...)`. The token is your Repull API key:

- `sk_test_*` — sandbox
- `sk_live_*` — production

Get one at [repull.dev/dashboard](https://repull.dev/dashboard) → **API keys**.

## What's in the SDK

The client is generated tag-by-tag from the OpenAPI spec. The modules mirror the API surface:

| Module | Endpoints |
|---|---|
| `repull.api.system` | `GET /v1/health` |
| `repull.api.properties` | list / get properties |
| `repull.api.reservations` | list / get / create / patch / delete reservations |
| `repull.api.availability` | per-property calendar read + bulk write |
| `repull.api.guests` | guest CRM list + detail |
| `repull.api.conversations` | list threads, read & post messages |
| `repull.api.connect` | white-label OAuth Connect — list, status, create, disconnect |
| `repull.api.webhooks` | manage subscriptions + fire test events |
| `repull.api.airbnb` | listings, pricing, availability, photos, messaging, reservations, reviews, sync |
| `repull.api.booking_com` | properties, availability, content, messaging, sync |
| `repull.api.vrbo` | listings, reservations |
| `repull.api.plumguide` | listings, availability, pricing |
| `repull.api.ai` | run AI operations (autorespond, smart pricing, etc.) |
| `repull.api.billing` | view & change plan |

Everything is fully typed — your editor will autocomplete every parameter and every response field.

## Examples

- [`examples/quickstart.py`](examples/quickstart.py) — list 10 reservations.
- [`examples/connect_airbnb.py`](examples/connect_airbnb.py) — mint a Connect session and poll for the linked Airbnb account.

Run them with a real API key:

```bash
REPULL_API_KEY=sk_live_... python examples/quickstart.py
```

## Connect (OAuth)

Repull Connect lets you link a property manager's Airbnb / Booking.com account in a few lines:

```python
from repull.api.connect import create_connect_session
from repull.models.create_connect_session_body import CreateConnectSessionBody

session = await create_connect_session.asyncio(
    client=c,
    body=CreateConnectSessionBody(
        redirect_url="https://yourapp.example.com/airbnb/return",
        allowed_providers=["airbnb"],
    ),
)
# Send the user to session.url
```

After the user comes back, poll `get_connect_status.asyncio(provider="airbnb", client=c)` to confirm.

## Pagination

Every list endpoint returns the same canonical envelope:

```python
page = await list_reservations.asyncio(client=c, limit=50)
page.data                      # list[Reservation]
page.pagination.next_cursor    # str | None — pass back as `cursor=`
page.pagination.has_more       # bool — stop when False
page.pagination.total          # int | UNSET — present when ?include_total=true
```

Loop until `pagination.has_more` is `False`, threading `pagination.next_cursor`
back as the next call's `cursor` arg. Cursors are opaque base64 — never parse
or construct them by hand.

## Error handling

By default, unexpected HTTP statuses return `None` from the high-level `.asyncio()` / `.sync()` calls. To raise instead:

```python
client = AuthenticatedClient(
    base_url="https://api.repull.dev",
    token=os.environ["REPULL_API_KEY"],
    raise_on_unexpected_status=True,
)
```

You can also call `.asyncio_detailed()` / `.sync_detailed()` to get the full `Response` (status code, headers, raw bytes, parsed body).

## Regenerating the client

The repo snapshots the current spec at [`openapi/v1.json`](openapi/v1.json) so codegen is fully reproducible.

```bash
# Pull a fresh spec from api.repull.dev and regenerate
./scripts/regen.sh

# Use the snapshot in openapi/v1.json without hitting the network
./scripts/regen.sh --offline
```

You'll need [`openapi-python-client`](https://github.com/openapi-generators/openapi-python-client) on your `PATH`:

```bash
uv tool install openapi-python-client
# or
pipx install openapi-python-client
```

## Reference

- API base: <https://api.repull.dev>
- OpenAPI spec: <https://api.repull.dev/openapi.json>
- Product docs: <https://repull.dev/docs>
- Other SDKs: [`repull-sdk`](https://github.com/ivannikolovbg/repull-sdk) (TypeScript), `repull-php`, `repull-go`, `repull-ruby`, `repull-dotnet`

## License

MIT — see [`LICENSE`](LICENSE). The Python client is a thin auto-generated wrapper, free to use anywhere.

(Note: the TypeScript SDK is licensed differently because it ships a hand-written facade plus the demo + channel-manager template. See [`repull-sdk`](https://github.com/ivannikolovbg/repull-sdk) if you need that.)

---

Powered by [Repull](https://repull.dev). AI features powered by [Vanio AI](https://vanio.ai).
