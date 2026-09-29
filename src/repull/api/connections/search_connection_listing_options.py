from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_connection_listing_options_response_200 import SearchConnectionListingOptionsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    q: str | Unset = UNSET,
    limit: int | Unset = 20,
    session_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit

    params["sessionId"] = session_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connections/{id}/listing-options".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchConnectionListingOptionsResponse200 | None:
    if response.status_code == 200:
        response_200 = SearchConnectionListingOptionsResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchConnectionListingOptionsResponse200]:
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
    q: str | Unset = UNSET,
    limit: int | Unset = 20,
    session_id: str | Unset = UNSET,

) -> Response[SearchConnectionListingOptionsResponse200]:
    """ Search listings a unit can be mapped to

     Search the workspace's active listings by name, city or id, for a mapping picker. A workspace can
    hold tens of thousands of listings, so pickers search here as the user types rather than loading
    them all. Empty `q` returns the first `limit` listings by name.

    Auth: a Repull API key, or a Connect session token (`sessionId`) while the hosted flow is mapping.

    Args:
        id (str):
        q (str | Unset):
        limit (int | Unset):  Default: 20.
        session_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchConnectionListingOptionsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
q=q,
limit=limit,
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
    q: str | Unset = UNSET,
    limit: int | Unset = 20,
    session_id: str | Unset = UNSET,

) -> SearchConnectionListingOptionsResponse200 | None:
    """ Search listings a unit can be mapped to

     Search the workspace's active listings by name, city or id, for a mapping picker. A workspace can
    hold tens of thousands of listings, so pickers search here as the user types rather than loading
    them all. Empty `q` returns the first `limit` listings by name.

    Auth: a Repull API key, or a Connect session token (`sessionId`) while the hosted flow is mapping.

    Args:
        id (str):
        q (str | Unset):
        limit (int | Unset):  Default: 20.
        session_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchConnectionListingOptionsResponse200
     """


    return sync_detailed(
        id=id,
client=client,
q=q,
limit=limit,
session_id=session_id,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 20,
    session_id: str | Unset = UNSET,

) -> Response[SearchConnectionListingOptionsResponse200]:
    """ Search listings a unit can be mapped to

     Search the workspace's active listings by name, city or id, for a mapping picker. A workspace can
    hold tens of thousands of listings, so pickers search here as the user types rather than loading
    them all. Empty `q` returns the first `limit` listings by name.

    Auth: a Repull API key, or a Connect session token (`sessionId`) while the hosted flow is mapping.

    Args:
        id (str):
        q (str | Unset):
        limit (int | Unset):  Default: 20.
        session_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchConnectionListingOptionsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
q=q,
limit=limit,
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
    q: str | Unset = UNSET,
    limit: int | Unset = 20,
    session_id: str | Unset = UNSET,

) -> SearchConnectionListingOptionsResponse200 | None:
    """ Search listings a unit can be mapped to

     Search the workspace's active listings by name, city or id, for a mapping picker. A workspace can
    hold tens of thousands of listings, so pickers search here as the user types rather than loading
    them all. Empty `q` returns the first `limit` listings by name.

    Auth: a Repull API key, or a Connect session token (`sessionId`) while the hosted flow is mapping.

    Args:
        id (str):
        q (str | Unset):
        limit (int | Unset):  Default: 20.
        session_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchConnectionListingOptionsResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
q=q,
limit=limit,
session_id=session_id,

    )).parsed
