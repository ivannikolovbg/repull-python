from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.tiket_map_listings_request import TiketMapListingsRequest
from ...models.tiket_map_listings_response import TiketMapListingsResponse
from typing import cast



def _get_kwargs(
    *,
    body: TiketMapListingsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/tiket/listings/map",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TiketMapListingsResponse | None:
    if response.status_code == 200:
        response_200 = TiketMapListingsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | TiketMapListingsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiketMapListingsRequest,

) -> Response[Error | TiketMapListingsResponse]:
    """ Map tiket.com room types to listings

     Map each room type of a tiket.com property to a Repull listing — the API-key equivalent of the
    mapping step of the hosted Connect flow, and the counterpart of `POST
    /v1/channels/booking/listings/map`.

    Each mapping is `{ roomTypeCode, listingId }` (`listingId: null` unmaps the room) or `{
    roomTypeCode, create: true }`, which creates a new listing from the room with tiket.com's calendar.

    Mapping a room to an existing listing sends that listing's calendar to tiket.com, and records any
    bookings tiket.com delivered while the room was unmapped (`replayedReservations`).

    Returns `403 listing_inactive` when a target listing is inactive; nothing is changed.

    Args:
        body (TiketMapListingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketMapListingsResponse]
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
    body: TiketMapListingsRequest,

) -> Error | TiketMapListingsResponse | None:
    """ Map tiket.com room types to listings

     Map each room type of a tiket.com property to a Repull listing — the API-key equivalent of the
    mapping step of the hosted Connect flow, and the counterpart of `POST
    /v1/channels/booking/listings/map`.

    Each mapping is `{ roomTypeCode, listingId }` (`listingId: null` unmaps the room) or `{
    roomTypeCode, create: true }`, which creates a new listing from the room with tiket.com's calendar.

    Mapping a room to an existing listing sends that listing's calendar to tiket.com, and records any
    bookings tiket.com delivered while the room was unmapped (`replayedReservations`).

    Returns `403 listing_inactive` when a target listing is inactive; nothing is changed.

    Args:
        body (TiketMapListingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketMapListingsResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiketMapListingsRequest,

) -> Response[Error | TiketMapListingsResponse]:
    """ Map tiket.com room types to listings

     Map each room type of a tiket.com property to a Repull listing — the API-key equivalent of the
    mapping step of the hosted Connect flow, and the counterpart of `POST
    /v1/channels/booking/listings/map`.

    Each mapping is `{ roomTypeCode, listingId }` (`listingId: null` unmaps the room) or `{
    roomTypeCode, create: true }`, which creates a new listing from the room with tiket.com's calendar.

    Mapping a room to an existing listing sends that listing's calendar to tiket.com, and records any
    bookings tiket.com delivered while the room was unmapped (`replayedReservations`).

    Returns `403 listing_inactive` when a target listing is inactive; nothing is changed.

    Args:
        body (TiketMapListingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketMapListingsResponse]
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
    body: TiketMapListingsRequest,

) -> Error | TiketMapListingsResponse | None:
    """ Map tiket.com room types to listings

     Map each room type of a tiket.com property to a Repull listing — the API-key equivalent of the
    mapping step of the hosted Connect flow, and the counterpart of `POST
    /v1/channels/booking/listings/map`.

    Each mapping is `{ roomTypeCode, listingId }` (`listingId: null` unmaps the room) or `{
    roomTypeCode, create: true }`, which creates a new listing from the room with tiket.com's calendar.

    Mapping a room to an existing listing sends that listing's calendar to tiket.com, and records any
    bookings tiket.com delivered while the room was unmapped (`replayedReservations`).

    Returns `403 listing_inactive` when a target listing is inactive; nothing is changed.

    Args:
        body (TiketMapListingsRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketMapListingsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
