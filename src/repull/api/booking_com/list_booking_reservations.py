from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_booking_reservations_type import ListBookingReservationsType
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    type_: ListBookingReservationsType | Unset = ListBookingReservationsType.NEW,
    hotel_id: str | Unset = UNSET,
    reservation_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["hotel_id"] = hotel_id

    params["reservation_id"] = reservation_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/booking/reservations",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: ListBookingReservationsType | Unset = ListBookingReservationsType.NEW,
    hotel_id: str | Unset = UNSET,
    reservation_id: str | Unset = UNSET,

) -> Response[Any | Error]:
    """ List Booking.com reservations

     Pull reservations from Booking.com. `type=new` (default) returns un-acknowledged bookings;
    `type=modified` returns changed bookings. Pass both `reservation_id` and `hotel_id` to fetch a
    single reservation's full details. Acknowledge processed reservations with the POST so Booking stops
    re-serving them in the `new` queue.

    Args:
        type_ (ListBookingReservationsType | Unset):  Default: ListBookingReservationsType.NEW.
        hotel_id (str | Unset):
        reservation_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        type_=type_,
hotel_id=hotel_id,
reservation_id=reservation_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    type_: ListBookingReservationsType | Unset = ListBookingReservationsType.NEW,
    hotel_id: str | Unset = UNSET,
    reservation_id: str | Unset = UNSET,

) -> Any | Error | None:
    """ List Booking.com reservations

     Pull reservations from Booking.com. `type=new` (default) returns un-acknowledged bookings;
    `type=modified` returns changed bookings. Pass both `reservation_id` and `hotel_id` to fetch a
    single reservation's full details. Acknowledge processed reservations with the POST so Booking stops
    re-serving them in the `new` queue.

    Args:
        type_ (ListBookingReservationsType | Unset):  Default: ListBookingReservationsType.NEW.
        hotel_id (str | Unset):
        reservation_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        client=client,
type_=type_,
hotel_id=hotel_id,
reservation_id=reservation_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: ListBookingReservationsType | Unset = ListBookingReservationsType.NEW,
    hotel_id: str | Unset = UNSET,
    reservation_id: str | Unset = UNSET,

) -> Response[Any | Error]:
    """ List Booking.com reservations

     Pull reservations from Booking.com. `type=new` (default) returns un-acknowledged bookings;
    `type=modified` returns changed bookings. Pass both `reservation_id` and `hotel_id` to fetch a
    single reservation's full details. Acknowledge processed reservations with the POST so Booking stops
    re-serving them in the `new` queue.

    Args:
        type_ (ListBookingReservationsType | Unset):  Default: ListBookingReservationsType.NEW.
        hotel_id (str | Unset):
        reservation_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        type_=type_,
hotel_id=hotel_id,
reservation_id=reservation_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: ListBookingReservationsType | Unset = ListBookingReservationsType.NEW,
    hotel_id: str | Unset = UNSET,
    reservation_id: str | Unset = UNSET,

) -> Any | Error | None:
    """ List Booking.com reservations

     Pull reservations from Booking.com. `type=new` (default) returns un-acknowledged bookings;
    `type=modified` returns changed bookings. Pass both `reservation_id` and `hotel_id` to fetch a
    single reservation's full details. Acknowledge processed reservations with the POST so Booking stops
    re-serving them in the `new` queue.

    Args:
        type_ (ListBookingReservationsType | Unset):  Default: ListBookingReservationsType.NEW.
        hotel_id (str | Unset):
        reservation_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        client=client,
type_=type_,
hotel_id=hotel_id,
reservation_id=reservation_id,

    )).parsed
