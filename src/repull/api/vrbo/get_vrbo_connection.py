from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_vrbo_connection_response_200 import GetVrboConnectionResponse200
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/vrbo/connection",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetVrboConnectionResponse200 | None:
    if response.status_code == 200:
        response_200 = GetVrboConnectionResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetVrboConnectionResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetVrboConnectionResponse200]:
    """ Get the Vrbo connection state

     Whether the workspace's Vrbo accounts are still signed in — the Vrbo counterpart of `GET
    /v1/channels/airbnb/connection`, with the same `status` values: `connected` (every account),
    `reconnect_required` (some), `disconnected` (none), `never_connected` (no Vrbo account). `fixUrl` is
    set whenever an account needs to be reconnected.

    Per account: its `account_id`, name, sign-in state, access (`full_access` or `messaging`), the Vrbo
    units linked through it, when it last synced and its import progress.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboConnectionResponse200]
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

) -> Error | GetVrboConnectionResponse200 | None:
    """ Get the Vrbo connection state

     Whether the workspace's Vrbo accounts are still signed in — the Vrbo counterpart of `GET
    /v1/channels/airbnb/connection`, with the same `status` values: `connected` (every account),
    `reconnect_required` (some), `disconnected` (none), `never_connected` (no Vrbo account). `fixUrl` is
    set whenever an account needs to be reconnected.

    Per account: its `account_id`, name, sign-in state, access (`full_access` or `messaging`), the Vrbo
    units linked through it, when it last synced and its import progress.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboConnectionResponse200
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetVrboConnectionResponse200]:
    """ Get the Vrbo connection state

     Whether the workspace's Vrbo accounts are still signed in — the Vrbo counterpart of `GET
    /v1/channels/airbnb/connection`, with the same `status` values: `connected` (every account),
    `reconnect_required` (some), `disconnected` (none), `never_connected` (no Vrbo account). `fixUrl` is
    set whenever an account needs to be reconnected.

    Per account: its `account_id`, name, sign-in state, access (`full_access` or `messaging`), the Vrbo
    units linked through it, when it last synced and its import progress.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboConnectionResponse200]
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

) -> Error | GetVrboConnectionResponse200 | None:
    """ Get the Vrbo connection state

     Whether the workspace's Vrbo accounts are still signed in — the Vrbo counterpart of `GET
    /v1/channels/airbnb/connection`, with the same `status` values: `connected` (every account),
    `reconnect_required` (some), `disconnected` (none), `never_connected` (no Vrbo account). `fixUrl` is
    set whenever an account needs to be reconnected.

    Per account: its `account_id`, name, sign-in state, access (`full_access` or `messaging`), the Vrbo
    units linked through it, when it last synced and its import progress.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboConnectionResponse200
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
