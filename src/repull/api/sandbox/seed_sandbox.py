from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.sandbox_seed_result import SandboxSeedResult
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/sandbox/seed",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SandboxSeedResult | None:
    if response.status_code == 200:
        response_200 = SandboxSeedResult.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SandboxSeedResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | SandboxSeedResult]:
    """ Seed sandbox fixtures

     Provision a deterministic set of test fixtures for contract testing WITHOUT live provider accounts.
    **Requires a test key (`sk_test_*`)** — live or legacy keys are rejected with 403.

    Seeds, scoped to the authenticated test customer: 3 sample listings, 5 reservations across the
    lifecycle (created / modified / cancelled / date-changed / pending), and 2 fake connected provider
    accounts (Airbnb + Booking.com) so the pairing + connection-status flows are testable without real
    OAuth.

    Idempotent — re-seeding upserts the same rows and returns the same ids. The seeded rows are visible
    ONLY under a test key, via the normal read endpoints (`GET /v1/listings`, `/v1/reservations`,
    `/v1/connect`, `/v1/channels/airbnb/listings`, `/v1/channels/airbnb/connection`). They live in a
    data space fully isolated from live inventory.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SandboxSeedResult]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> Error | SandboxSeedResult | None:
    """ Seed sandbox fixtures

     Provision a deterministic set of test fixtures for contract testing WITHOUT live provider accounts.
    **Requires a test key (`sk_test_*`)** — live or legacy keys are rejected with 403.

    Seeds, scoped to the authenticated test customer: 3 sample listings, 5 reservations across the
    lifecycle (created / modified / cancelled / date-changed / pending), and 2 fake connected provider
    accounts (Airbnb + Booking.com) so the pairing + connection-status flows are testable without real
    OAuth.

    Idempotent — re-seeding upserts the same rows and returns the same ids. The seeded rows are visible
    ONLY under a test key, via the normal read endpoints (`GET /v1/listings`, `/v1/reservations`,
    `/v1/connect`, `/v1/channels/airbnb/listings`, `/v1/channels/airbnb/connection`). They live in a
    data space fully isolated from live inventory.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SandboxSeedResult
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | SandboxSeedResult]:
    """ Seed sandbox fixtures

     Provision a deterministic set of test fixtures for contract testing WITHOUT live provider accounts.
    **Requires a test key (`sk_test_*`)** — live or legacy keys are rejected with 403.

    Seeds, scoped to the authenticated test customer: 3 sample listings, 5 reservations across the
    lifecycle (created / modified / cancelled / date-changed / pending), and 2 fake connected provider
    accounts (Airbnb + Booking.com) so the pairing + connection-status flows are testable without real
    OAuth.

    Idempotent — re-seeding upserts the same rows and returns the same ids. The seeded rows are visible
    ONLY under a test key, via the normal read endpoints (`GET /v1/listings`, `/v1/reservations`,
    `/v1/connect`, `/v1/channels/airbnb/listings`, `/v1/channels/airbnb/connection`). They live in a
    data space fully isolated from live inventory.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SandboxSeedResult]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> Error | SandboxSeedResult | None:
    """ Seed sandbox fixtures

     Provision a deterministic set of test fixtures for contract testing WITHOUT live provider accounts.
    **Requires a test key (`sk_test_*`)** — live or legacy keys are rejected with 403.

    Seeds, scoped to the authenticated test customer: 3 sample listings, 5 reservations across the
    lifecycle (created / modified / cancelled / date-changed / pending), and 2 fake connected provider
    accounts (Airbnb + Booking.com) so the pairing + connection-status flows are testable without real
    OAuth.

    Idempotent — re-seeding upserts the same rows and returns the same ids. The seeded rows are visible
    ONLY under a test key, via the normal read endpoints (`GET /v1/listings`, `/v1/reservations`,
    `/v1/connect`, `/v1/channels/airbnb/listings`, `/v1/channels/airbnb/connection`). They live in a
    data space fully isolated from live inventory.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SandboxSeedResult
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
