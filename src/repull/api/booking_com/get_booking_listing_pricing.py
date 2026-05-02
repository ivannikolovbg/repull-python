from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_pricing_response import BookingPricingResponse
from ...models.error import Error
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    id: int,
    *,
    start_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = UNSET,
    room_id: str | Unset = UNSET,
    room_level: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

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
        "url": "/v1/channels/booking/listings/{id}/pricing".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BookingPricingResponse | Error | None:
    if response.status_code == 200:
        response_200 = BookingPricingResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BookingPricingResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = UNSET,
    room_id: str | Unset = UNSET,
    room_level: bool | Unset = UNSET,

) -> Response[BookingPricingResponse | Error]:
    """ Get Booking.com pricing for a listing

     Resolves the Vanio listing ID to its Booking.com `hotel_id` (via the `listings_booking` mapping
    owned by the authenticated workspace), then proxies Booking's `getRoomRateAvailability` for the
    requested window. Pricing on Booking is per-room/per-rate-plan, so `room_id` and `room_level` flow
    through query params unchanged.

    Mirrors the per-channel `/listings/{id}/pricing` shape used by Airbnb so SDK consumers can carry a
    Vanio listing ID across channels.

    Args:
        id (int):
        start_date (datetime.date | Unset):
        number_of_days (int | Unset):
        room_id (str | Unset):
        room_level (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingPricingResponse | Error]
     """


    kwargs = _get_kwargs(
        id=id,
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = UNSET,
    room_id: str | Unset = UNSET,
    room_level: bool | Unset = UNSET,

) -> BookingPricingResponse | Error | None:
    """ Get Booking.com pricing for a listing

     Resolves the Vanio listing ID to its Booking.com `hotel_id` (via the `listings_booking` mapping
    owned by the authenticated workspace), then proxies Booking's `getRoomRateAvailability` for the
    requested window. Pricing on Booking is per-room/per-rate-plan, so `room_id` and `room_level` flow
    through query params unchanged.

    Mirrors the per-channel `/listings/{id}/pricing` shape used by Airbnb so SDK consumers can carry a
    Vanio listing ID across channels.

    Args:
        id (int):
        start_date (datetime.date | Unset):
        number_of_days (int | Unset):
        room_id (str | Unset):
        room_level (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingPricingResponse | Error
     """


    return sync_detailed(
        id=id,
client=client,
start_date=start_date,
number_of_days=number_of_days,
room_id=room_id,
room_level=room_level,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = UNSET,
    room_id: str | Unset = UNSET,
    room_level: bool | Unset = UNSET,

) -> Response[BookingPricingResponse | Error]:
    """ Get Booking.com pricing for a listing

     Resolves the Vanio listing ID to its Booking.com `hotel_id` (via the `listings_booking` mapping
    owned by the authenticated workspace), then proxies Booking's `getRoomRateAvailability` for the
    requested window. Pricing on Booking is per-room/per-rate-plan, so `room_id` and `room_level` flow
    through query params unchanged.

    Mirrors the per-channel `/listings/{id}/pricing` shape used by Airbnb so SDK consumers can carry a
    Vanio listing ID across channels.

    Args:
        id (int):
        start_date (datetime.date | Unset):
        number_of_days (int | Unset):
        room_id (str | Unset):
        room_level (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingPricingResponse | Error]
     """


    kwargs = _get_kwargs(
        id=id,
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = UNSET,
    room_id: str | Unset = UNSET,
    room_level: bool | Unset = UNSET,

) -> BookingPricingResponse | Error | None:
    """ Get Booking.com pricing for a listing

     Resolves the Vanio listing ID to its Booking.com `hotel_id` (via the `listings_booking` mapping
    owned by the authenticated workspace), then proxies Booking's `getRoomRateAvailability` for the
    requested window. Pricing on Booking is per-room/per-rate-plan, so `room_id` and `room_level` flow
    through query params unchanged.

    Mirrors the per-channel `/listings/{id}/pricing` shape used by Airbnb so SDK consumers can carry a
    Vanio listing ID across channels.

    Args:
        id (int):
        start_date (datetime.date | Unset):
        number_of_days (int | Unset):
        room_id (str | Unset):
        room_level (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingPricingResponse | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
start_date=start_date,
number_of_days=number_of_days,
room_id=room_id,
room_level=room_level,

    )).parsed
