from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_reservation import BookingReservation
from ...models.error import Error
from ...models.list_booking_reservations_response_200_type_1 import ListBookingReservationsResponse200Type1
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



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BookingReservation | ListBookingReservationsResponse200Type1 | Error | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> BookingReservation | ListBookingReservationsResponse200Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = BookingReservation.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = ListBookingReservationsResponse200Type1.from_dict(data)



            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BookingReservation | ListBookingReservationsResponse200Type1 | Error]:
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

) -> Response[BookingReservation | ListBookingReservationsResponse200Type1 | Error]:
    """ List Booking.com reservations

     Pull reservations from Booking.com. `type=new` (default) returns un-acknowledged bookings;
    `type=modified` returns changed bookings. Pass both `reservation_id` and `hotel_id` to fetch a
    single reservation's full details. Acknowledge processed reservations with the POST so Booking stops
    re-serving them in the `new` queue.

    Scoped to this workspace. `hotel_id` (or its alias `property_id`) must be a property connected to
    this workspace; any other id returns `404 not_found`, the same as an id that does not exist. Without
    a hotel, `new`/`modified` cover every Booking.com property this workspace holds (and return `404
    not_found` if it holds none). A `reservation_id` that belongs to another workspace returns `404
    not_found`.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        type_ (ListBookingReservationsType | Unset):  Default: ListBookingReservationsType.NEW.
        hotel_id (str | Unset):
        reservation_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingReservation | ListBookingReservationsResponse200Type1 | Error]
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

) -> BookingReservation | ListBookingReservationsResponse200Type1 | Error | None:
    """ List Booking.com reservations

     Pull reservations from Booking.com. `type=new` (default) returns un-acknowledged bookings;
    `type=modified` returns changed bookings. Pass both `reservation_id` and `hotel_id` to fetch a
    single reservation's full details. Acknowledge processed reservations with the POST so Booking stops
    re-serving them in the `new` queue.

    Scoped to this workspace. `hotel_id` (or its alias `property_id`) must be a property connected to
    this workspace; any other id returns `404 not_found`, the same as an id that does not exist. Without
    a hotel, `new`/`modified` cover every Booking.com property this workspace holds (and return `404
    not_found` if it holds none). A `reservation_id` that belongs to another workspace returns `404
    not_found`.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        type_ (ListBookingReservationsType | Unset):  Default: ListBookingReservationsType.NEW.
        hotel_id (str | Unset):
        reservation_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingReservation | ListBookingReservationsResponse200Type1 | Error
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

) -> Response[BookingReservation | ListBookingReservationsResponse200Type1 | Error]:
    """ List Booking.com reservations

     Pull reservations from Booking.com. `type=new` (default) returns un-acknowledged bookings;
    `type=modified` returns changed bookings. Pass both `reservation_id` and `hotel_id` to fetch a
    single reservation's full details. Acknowledge processed reservations with the POST so Booking stops
    re-serving them in the `new` queue.

    Scoped to this workspace. `hotel_id` (or its alias `property_id`) must be a property connected to
    this workspace; any other id returns `404 not_found`, the same as an id that does not exist. Without
    a hotel, `new`/`modified` cover every Booking.com property this workspace holds (and return `404
    not_found` if it holds none). A `reservation_id` that belongs to another workspace returns `404
    not_found`.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        type_ (ListBookingReservationsType | Unset):  Default: ListBookingReservationsType.NEW.
        hotel_id (str | Unset):
        reservation_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingReservation | ListBookingReservationsResponse200Type1 | Error]
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

) -> BookingReservation | ListBookingReservationsResponse200Type1 | Error | None:
    """ List Booking.com reservations

     Pull reservations from Booking.com. `type=new` (default) returns un-acknowledged bookings;
    `type=modified` returns changed bookings. Pass both `reservation_id` and `hotel_id` to fetch a
    single reservation's full details. Acknowledge processed reservations with the POST so Booking stops
    re-serving them in the `new` queue.

    Scoped to this workspace. `hotel_id` (or its alias `property_id`) must be a property connected to
    this workspace; any other id returns `404 not_found`, the same as an id that does not exist. Without
    a hotel, `new`/`modified` cover every Booking.com property this workspace holds (and return `404
    not_found` if it holds none). A `reservation_id` that belongs to another workspace returns `404
    not_found`.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        type_ (ListBookingReservationsType | Unset):  Default: ListBookingReservationsType.NEW.
        hotel_id (str | Unset):
        reservation_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingReservation | ListBookingReservationsResponse200Type1 | Error
     """


    return (await asyncio_detailed(
        client=client,
type_=type_,
hotel_id=hotel_id,
reservation_id=reservation_id,

    )).parsed
