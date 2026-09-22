from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_availability_state_response import BookingAvailabilityStateResponse
from ...models.error import Error
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    *,
    property_id: str,
    start_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = UNSET,
    room_id: str | Unset = UNSET,
    room_level: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["property_id"] = property_id

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    params["number_of_days"] = number_of_days

    params["room_id"] = room_id

    params["room_level"] = room_level


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/booking/availability",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BookingAvailabilityStateResponse | Error | None:
    if response.status_code == 200:
        response_200 = BookingAvailabilityStateResponse.from_dict(response.json())



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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BookingAvailabilityStateResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    property_id: str,
    start_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = UNSET,
    room_id: str | Unset = UNSET,
    room_level: bool | Unset = UNSET,

) -> Response[BookingAvailabilityStateResponse | Error]:
    """ Read current Booking.com rates/availability/restrictions

     Read the current rate, availability, and restriction state for a Booking.com property so you can
    reconcile before writing with the PUT on this path. Keyed by `property_id` (the Booking hotel id),
    symmetric with the PUT.

    Proxies Booking's `getRoomRateAvailability` — the returned fields (price, rooms-to-sell, min/max
    stay, closed-to-arrival/departure, stop-sell) are whatever Booking.com emits for the window. A
    listing-id-keyed equivalent is available at `GET /v1/channels/booking/listings/{id}/pricing`.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        property_id (str):
        start_date (datetime.date | Unset):
        number_of_days (int | Unset):
        room_id (str | Unset):
        room_level (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingAvailabilityStateResponse | Error]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
start_date=start_date,
number_of_days=number_of_days,
room_id=room_id,
room_level=room_level,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    property_id: str,
    start_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = UNSET,
    room_id: str | Unset = UNSET,
    room_level: bool | Unset = UNSET,

) -> BookingAvailabilityStateResponse | Error | None:
    """ Read current Booking.com rates/availability/restrictions

     Read the current rate, availability, and restriction state for a Booking.com property so you can
    reconcile before writing with the PUT on this path. Keyed by `property_id` (the Booking hotel id),
    symmetric with the PUT.

    Proxies Booking's `getRoomRateAvailability` — the returned fields (price, rooms-to-sell, min/max
    stay, closed-to-arrival/departure, stop-sell) are whatever Booking.com emits for the window. A
    listing-id-keyed equivalent is available at `GET /v1/channels/booking/listings/{id}/pricing`.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        property_id (str):
        start_date (datetime.date | Unset):
        number_of_days (int | Unset):
        room_id (str | Unset):
        room_level (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingAvailabilityStateResponse | Error
     """


    return sync_detailed(
        client=client,
property_id=property_id,
start_date=start_date,
number_of_days=number_of_days,
room_id=room_id,
room_level=room_level,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    property_id: str,
    start_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = UNSET,
    room_id: str | Unset = UNSET,
    room_level: bool | Unset = UNSET,

) -> Response[BookingAvailabilityStateResponse | Error]:
    """ Read current Booking.com rates/availability/restrictions

     Read the current rate, availability, and restriction state for a Booking.com property so you can
    reconcile before writing with the PUT on this path. Keyed by `property_id` (the Booking hotel id),
    symmetric with the PUT.

    Proxies Booking's `getRoomRateAvailability` — the returned fields (price, rooms-to-sell, min/max
    stay, closed-to-arrival/departure, stop-sell) are whatever Booking.com emits for the window. A
    listing-id-keyed equivalent is available at `GET /v1/channels/booking/listings/{id}/pricing`.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        property_id (str):
        start_date (datetime.date | Unset):
        number_of_days (int | Unset):
        room_id (str | Unset):
        room_level (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingAvailabilityStateResponse | Error]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
start_date=start_date,
number_of_days=number_of_days,
room_id=room_id,
room_level=room_level,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    property_id: str,
    start_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = UNSET,
    room_id: str | Unset = UNSET,
    room_level: bool | Unset = UNSET,

) -> BookingAvailabilityStateResponse | Error | None:
    """ Read current Booking.com rates/availability/restrictions

     Read the current rate, availability, and restriction state for a Booking.com property so you can
    reconcile before writing with the PUT on this path. Keyed by `property_id` (the Booking hotel id),
    symmetric with the PUT.

    Proxies Booking's `getRoomRateAvailability` — the returned fields (price, rooms-to-sell, min/max
    stay, closed-to-arrival/departure, stop-sell) are whatever Booking.com emits for the window. A
    listing-id-keyed equivalent is available at `GET /v1/channels/booking/listings/{id}/pricing`.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        property_id (str):
        start_date (datetime.date | Unset):
        number_of_days (int | Unset):
        room_id (str | Unset):
        room_level (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingAvailabilityStateResponse | Error
     """


    return (await asyncio_detailed(
        client=client,
property_id=property_id,
start_date=start_date,
number_of_days=number_of_days,
room_id=room_id,
room_level=room_level,

    )).parsed
