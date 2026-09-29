from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.search_connect_session_listing_options_response_200 import SearchConnectSessionListingOptionsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    session_id: str,
    *,
    q: str | Unset = UNSET,
    limit: int | Unset = 20,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["q"] = q

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connect/sessions/{session_id}/listing-options".format(session_id=quote(str(session_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SearchConnectSessionListingOptionsResponse200 | None:
    if response.status_code == 200:
        response_200 = SearchConnectSessionListingOptionsResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SearchConnectSessionListingOptionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 20,

) -> Response[SearchConnectSessionListingOptionsResponse200]:
    """ Search listings for a Connect mapping picker

     The hosted Connect pages' listing search for their mapping pickers: the session workspace's active
    listings by name, city or id, `limit` at a time.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        session_id (str):
        q (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchConnectSessionListingOptionsResponse200]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
q=q,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 20,

) -> SearchConnectSessionListingOptionsResponse200 | None:
    """ Search listings for a Connect mapping picker

     The hosted Connect pages' listing search for their mapping pickers: the session workspace's active
    listings by name, city or id, `limit` at a time.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        session_id (str):
        q (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchConnectSessionListingOptionsResponse200
     """


    return sync_detailed(
        session_id=session_id,
client=client,
q=q,
limit=limit,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 20,

) -> Response[SearchConnectSessionListingOptionsResponse200]:
    """ Search listings for a Connect mapping picker

     The hosted Connect pages' listing search for their mapping pickers: the session workspace's active
    listings by name, city or id, `limit` at a time.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        session_id (str):
        q (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchConnectSessionListingOptionsResponse200]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
q=q,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    limit: int | Unset = 20,

) -> SearchConnectSessionListingOptionsResponse200 | None:
    """ Search listings for a Connect mapping picker

     The hosted Connect pages' listing search for their mapping pickers: the session workspace's active
    listings by name, city or id, `limit` at a time.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        session_id (str):
        q (str | Unset):
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchConnectSessionListingOptionsResponse200
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
q=q,
limit=limit,

    )).parsed
