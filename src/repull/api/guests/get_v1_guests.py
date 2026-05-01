from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_v1_guests_response_200 import GetV1GuestsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    search: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["search"] = search


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/guests",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetV1GuestsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1GuestsResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetV1GuestsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    search: str | Unset = UNSET,

) -> Response[GetV1GuestsResponse200]:
    """ List guests

    Args:
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV1GuestsResponse200]
     """


    kwargs = _get_kwargs(
        limit=limit,
offset=offset,
search=search,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    search: str | Unset = UNSET,

) -> GetV1GuestsResponse200 | None:
    """ List guests

    Args:
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV1GuestsResponse200
     """


    return sync_detailed(
        client=client,
limit=limit,
offset=offset,
search=search,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    search: str | Unset = UNSET,

) -> Response[GetV1GuestsResponse200]:
    """ List guests

    Args:
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV1GuestsResponse200]
     """


    kwargs = _get_kwargs(
        limit=limit,
offset=offset,
search=search,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    search: str | Unset = UNSET,

) -> GetV1GuestsResponse200 | None:
    """ List guests

    Args:
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.
        search (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV1GuestsResponse200
     """


    return (await asyncio_detailed(
        client=client,
limit=limit,
offset=offset,
search=search,

    )).parsed
