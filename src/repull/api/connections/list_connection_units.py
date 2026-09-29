from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_connection_units_response_200 import ListConnectionUnitsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    session_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["sessionId"] = session_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connections/{id}/units".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListConnectionUnitsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListConnectionUnitsResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListConnectionUnitsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    session_id: str | Unset = UNSET,

) -> Response[ListConnectionUnitsResponse200]:
    """ List a connection's mappable units

     The units of a connected account with their current listing, a safe suggestion, and the workspace's
    listing options. `status: ready` with no units means the account has no properties.

    Auth: a Repull API key, or a Connect session token (`sessionId`) while the hosted flow is mapping.

    `listing_options` carries only the listings the units already point at (mapped or suggested);
    `listing_options_total` says how many the workspace has. Search the rest with `GET
    /v1/connections/{id}/listing-options?q=`.

    Args:
        id (str):
        session_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListConnectionUnitsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
session_id=session_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    session_id: str | Unset = UNSET,

) -> ListConnectionUnitsResponse200 | None:
    """ List a connection's mappable units

     The units of a connected account with their current listing, a safe suggestion, and the workspace's
    listing options. `status: ready` with no units means the account has no properties.

    Auth: a Repull API key, or a Connect session token (`sessionId`) while the hosted flow is mapping.

    `listing_options` carries only the listings the units already point at (mapped or suggested);
    `listing_options_total` says how many the workspace has. Search the rest with `GET
    /v1/connections/{id}/listing-options?q=`.

    Args:
        id (str):
        session_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListConnectionUnitsResponse200
     """


    return sync_detailed(
        id=id,
client=client,
session_id=session_id,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    session_id: str | Unset = UNSET,

) -> Response[ListConnectionUnitsResponse200]:
    """ List a connection's mappable units

     The units of a connected account with their current listing, a safe suggestion, and the workspace's
    listing options. `status: ready` with no units means the account has no properties.

    Auth: a Repull API key, or a Connect session token (`sessionId`) while the hosted flow is mapping.

    `listing_options` carries only the listings the units already point at (mapped or suggested);
    `listing_options_total` says how many the workspace has. Search the rest with `GET
    /v1/connections/{id}/listing-options?q=`.

    Args:
        id (str):
        session_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListConnectionUnitsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
session_id=session_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    session_id: str | Unset = UNSET,

) -> ListConnectionUnitsResponse200 | None:
    """ List a connection's mappable units

     The units of a connected account with their current listing, a safe suggestion, and the workspace's
    listing options. `status: ready` with no units means the account has no properties.

    Auth: a Repull API key, or a Connect session token (`sessionId`) while the hosted flow is mapping.

    `listing_options` carries only the listings the units already point at (mapped or suggested);
    `listing_options_total` says how many the workspace has. Search the rest with `GET
    /v1/connections/{id}/listing-options?q=`.

    Args:
        id (str):
        session_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListConnectionUnitsResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
session_id=session_id,

    )).parsed
