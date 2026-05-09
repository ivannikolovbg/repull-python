from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_connection_response import AirbnbConnectionResponse
from ...models.error import Error
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/connection",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AirbnbConnectionResponse | Error | None:
    if response.status_code == 200:
        response_200 = AirbnbConnectionResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AirbnbConnectionResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AirbnbConnectionResponse | Error]:
    """ Get Airbnb connection state

     Returns the workspace's Airbnb host connection state in one envelope. Use this instead of inferring
    connection health from per-listing 401s on `GET /v1/channels/airbnb/listings` — that's noisy (every
    per-listing call has to fail before you know) and ambiguous (a single 5xx looks identical to a
    deauth).

    Pure DB read — does NOT touch Airbnb's API, so it's cheap to poll from a status-page surface.

    The response includes one row per Airbnb host the workspace has linked. Each row carries
    `isConnected`, `lastSyncedAt`, `deactivatedAt`, and `lastDisconnectReason` (most recent non-backfill
    row in `airbnb_host_events`).

    A self-serve `fixUrl` is included whenever `status` is anything other than `connected` — points at
    the dashboard where the host re-authorizes (or initiates the first OAuth flow for `never_connected`
    workspaces).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbConnectionResponse | Error]
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

) -> AirbnbConnectionResponse | Error | None:
    """ Get Airbnb connection state

     Returns the workspace's Airbnb host connection state in one envelope. Use this instead of inferring
    connection health from per-listing 401s on `GET /v1/channels/airbnb/listings` — that's noisy (every
    per-listing call has to fail before you know) and ambiguous (a single 5xx looks identical to a
    deauth).

    Pure DB read — does NOT touch Airbnb's API, so it's cheap to poll from a status-page surface.

    The response includes one row per Airbnb host the workspace has linked. Each row carries
    `isConnected`, `lastSyncedAt`, `deactivatedAt`, and `lastDisconnectReason` (most recent non-backfill
    row in `airbnb_host_events`).

    A self-serve `fixUrl` is included whenever `status` is anything other than `connected` — points at
    the dashboard where the host re-authorizes (or initiates the first OAuth flow for `never_connected`
    workspaces).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbConnectionResponse | Error
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[AirbnbConnectionResponse | Error]:
    """ Get Airbnb connection state

     Returns the workspace's Airbnb host connection state in one envelope. Use this instead of inferring
    connection health from per-listing 401s on `GET /v1/channels/airbnb/listings` — that's noisy (every
    per-listing call has to fail before you know) and ambiguous (a single 5xx looks identical to a
    deauth).

    Pure DB read — does NOT touch Airbnb's API, so it's cheap to poll from a status-page surface.

    The response includes one row per Airbnb host the workspace has linked. Each row carries
    `isConnected`, `lastSyncedAt`, `deactivatedAt`, and `lastDisconnectReason` (most recent non-backfill
    row in `airbnb_host_events`).

    A self-serve `fixUrl` is included whenever `status` is anything other than `connected` — points at
    the dashboard where the host re-authorizes (or initiates the first OAuth flow for `never_connected`
    workspaces).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbConnectionResponse | Error]
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

) -> AirbnbConnectionResponse | Error | None:
    """ Get Airbnb connection state

     Returns the workspace's Airbnb host connection state in one envelope. Use this instead of inferring
    connection health from per-listing 401s on `GET /v1/channels/airbnb/listings` — that's noisy (every
    per-listing call has to fail before you know) and ambiguous (a single 5xx looks identical to a
    deauth).

    Pure DB read — does NOT touch Airbnb's API, so it's cheap to poll from a status-page surface.

    The response includes one row per Airbnb host the workspace has linked. Each row carries
    `isConnected`, `lastSyncedAt`, `deactivatedAt`, and `lastDisconnectReason` (most recent non-backfill
    row in `airbnb_host_events`).

    A self-serve `fixUrl` is included whenever `status` is anything other than `connected` — points at
    the dashboard where the host re-authorizes (or initiates the first OAuth flow for `never_connected`
    workspaces).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbConnectionResponse | Error
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
