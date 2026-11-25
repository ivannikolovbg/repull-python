from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.sync_tiket_body import SyncTiketBody
from ...models.tiket_sync_response import TiketSyncResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SyncTiketBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/tiket/sync",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TiketSyncResponse | None:
    if response.status_code == 200:
        response_200 = TiketSyncResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | TiketSyncResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SyncTiketBody | Unset = UNSET,

) -> Response[Error | TiketSyncResponse]:
    """ Send every mapped listing's calendar to tiket.com

     Send the full calendar (today to 500 days ahead: rooms to sell, prices, restrictions) of every
    mapped listing of one tiket.com property, or of every active property when `property_id` is omitted.
    `refresh_products: true` re-reads room types and rate plans from tiket.com first. Use it after a
    bulk edit or to re-baseline a property; day-to-day changes are sent automatically.

    Inactive listings are not sold, so they are skipped (`skipped: listing_inactive`).

    Args:
        body (SyncTiketBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketSyncResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SyncTiketBody | Unset = UNSET,

) -> Error | TiketSyncResponse | None:
    """ Send every mapped listing's calendar to tiket.com

     Send the full calendar (today to 500 days ahead: rooms to sell, prices, restrictions) of every
    mapped listing of one tiket.com property, or of every active property when `property_id` is omitted.
    `refresh_products: true` re-reads room types and rate plans from tiket.com first. Use it after a
    bulk edit or to re-baseline a property; day-to-day changes are sent automatically.

    Inactive listings are not sold, so they are skipped (`skipped: listing_inactive`).

    Args:
        body (SyncTiketBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketSyncResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SyncTiketBody | Unset = UNSET,

) -> Response[Error | TiketSyncResponse]:
    """ Send every mapped listing's calendar to tiket.com

     Send the full calendar (today to 500 days ahead: rooms to sell, prices, restrictions) of every
    mapped listing of one tiket.com property, or of every active property when `property_id` is omitted.
    `refresh_products: true` re-reads room types and rate plans from tiket.com first. Use it after a
    bulk edit or to re-baseline a property; day-to-day changes are sent automatically.

    Inactive listings are not sold, so they are skipped (`skipped: listing_inactive`).

    Args:
        body (SyncTiketBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketSyncResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SyncTiketBody | Unset = UNSET,

) -> Error | TiketSyncResponse | None:
    """ Send every mapped listing's calendar to tiket.com

     Send the full calendar (today to 500 days ahead: rooms to sell, prices, restrictions) of every
    mapped listing of one tiket.com property, or of every active property when `property_id` is omitted.
    `refresh_products: true` re-reads room types and rate plans from tiket.com first. Use it after a
    bulk edit or to re-baseline a property; day-to-day changes are sent automatically.

    Inactive listings are not sold, so they are skipped (`skipped: listing_inactive`).

    Args:
        body (SyncTiketBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketSyncResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
