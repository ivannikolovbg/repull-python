from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_tiket_reservations_status import ListTiketReservationsStatus
from ...models.tiket_reservation_list_response import TiketReservationListResponse
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    *,
    property_id: str | Unset = UNSET,
    status: ListTiketReservationsStatus | Unset = UNSET,
    check_in_from: datetime.date | Unset = UNSET,
    check_in_to: datetime.date | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["property_id"] = property_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_check_in_from: str | Unset = UNSET
    if not isinstance(check_in_from, Unset):
        json_check_in_from = check_in_from.isoformat()
    params["check_in_from"] = json_check_in_from

    json_check_in_to: str | Unset = UNSET
    if not isinstance(check_in_to, Unset):
        json_check_in_to = check_in_to.isoformat()
    params["check_in_to"] = json_check_in_to

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/tiket/reservations",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TiketReservationListResponse | None:
    if response.status_code == 200:
        response_200 = TiketReservationListResponse.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | TiketReservationListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    property_id: str | Unset = UNSET,
    status: ListTiketReservationsStatus | Unset = UNSET,
    check_in_from: datetime.date | Unset = UNSET,
    check_in_to: datetime.date | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,

) -> Response[Error | TiketReservationListResponse]:
    """ List tiket.com reservations as tiket.com sent them

     tiket.com's own record of the bookings it delivered, newest first: one row per booked room (`<id>`,
    `<id>-2`, …) with tiket.com's ids, rate plan, meal plan, cancellation policy, what the guest paid,
    the net amount tiket.com pays the property, how tiket.com pays (`paymentMethod`: `Virtual Credit
    Card` or `Bank Transfer`), and the Repull reservation the room became.

    **Cards.** Card details are never returned by the API, on this route or on `/v1/reservations`.

    **Date changes.** tiket.com sends a date change as a cancellation plus a new booking. Repull applies
    it as a change to the original reservation, so the Repull reservation keeps its id; the new
    tiket.com booking carries `previousTiketReservationId`.

    The same bookings, normalized like every other channel's (`source: tiket`), are on `GET
    /v1/reservations`.

    Args:
        property_id (str | Unset):
        status (ListTiketReservationsStatus | Unset):
        check_in_from (datetime.date | Unset):
        check_in_to (datetime.date | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketReservationListResponse]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
status=status,
check_in_from=check_in_from,
check_in_to=check_in_to,
limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    property_id: str | Unset = UNSET,
    status: ListTiketReservationsStatus | Unset = UNSET,
    check_in_from: datetime.date | Unset = UNSET,
    check_in_to: datetime.date | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,

) -> Error | TiketReservationListResponse | None:
    """ List tiket.com reservations as tiket.com sent them

     tiket.com's own record of the bookings it delivered, newest first: one row per booked room (`<id>`,
    `<id>-2`, …) with tiket.com's ids, rate plan, meal plan, cancellation policy, what the guest paid,
    the net amount tiket.com pays the property, how tiket.com pays (`paymentMethod`: `Virtual Credit
    Card` or `Bank Transfer`), and the Repull reservation the room became.

    **Cards.** Card details are never returned by the API, on this route or on `/v1/reservations`.

    **Date changes.** tiket.com sends a date change as a cancellation plus a new booking. Repull applies
    it as a change to the original reservation, so the Repull reservation keeps its id; the new
    tiket.com booking carries `previousTiketReservationId`.

    The same bookings, normalized like every other channel's (`source: tiket`), are on `GET
    /v1/reservations`.

    Args:
        property_id (str | Unset):
        status (ListTiketReservationsStatus | Unset):
        check_in_from (datetime.date | Unset):
        check_in_to (datetime.date | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketReservationListResponse
     """


    return sync_detailed(
        client=client,
property_id=property_id,
status=status,
check_in_from=check_in_from,
check_in_to=check_in_to,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    property_id: str | Unset = UNSET,
    status: ListTiketReservationsStatus | Unset = UNSET,
    check_in_from: datetime.date | Unset = UNSET,
    check_in_to: datetime.date | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,

) -> Response[Error | TiketReservationListResponse]:
    """ List tiket.com reservations as tiket.com sent them

     tiket.com's own record of the bookings it delivered, newest first: one row per booked room (`<id>`,
    `<id>-2`, …) with tiket.com's ids, rate plan, meal plan, cancellation policy, what the guest paid,
    the net amount tiket.com pays the property, how tiket.com pays (`paymentMethod`: `Virtual Credit
    Card` or `Bank Transfer`), and the Repull reservation the room became.

    **Cards.** Card details are never returned by the API, on this route or on `/v1/reservations`.

    **Date changes.** tiket.com sends a date change as a cancellation plus a new booking. Repull applies
    it as a change to the original reservation, so the Repull reservation keeps its id; the new
    tiket.com booking carries `previousTiketReservationId`.

    The same bookings, normalized like every other channel's (`source: tiket`), are on `GET
    /v1/reservations`.

    Args:
        property_id (str | Unset):
        status (ListTiketReservationsStatus | Unset):
        check_in_from (datetime.date | Unset):
        check_in_to (datetime.date | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketReservationListResponse]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
status=status,
check_in_from=check_in_from,
check_in_to=check_in_to,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    property_id: str | Unset = UNSET,
    status: ListTiketReservationsStatus | Unset = UNSET,
    check_in_from: datetime.date | Unset = UNSET,
    check_in_to: datetime.date | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,

) -> Error | TiketReservationListResponse | None:
    """ List tiket.com reservations as tiket.com sent them

     tiket.com's own record of the bookings it delivered, newest first: one row per booked room (`<id>`,
    `<id>-2`, …) with tiket.com's ids, rate plan, meal plan, cancellation policy, what the guest paid,
    the net amount tiket.com pays the property, how tiket.com pays (`paymentMethod`: `Virtual Credit
    Card` or `Bank Transfer`), and the Repull reservation the room became.

    **Cards.** Card details are never returned by the API, on this route or on `/v1/reservations`.

    **Date changes.** tiket.com sends a date change as a cancellation plus a new booking. Repull applies
    it as a change to the original reservation, so the Repull reservation keeps its id; the new
    tiket.com booking carries `previousTiketReservationId`.

    The same bookings, normalized like every other channel's (`source: tiket`), are on `GET
    /v1/reservations`.

    Args:
        property_id (str | Unset):
        status (ListTiketReservationsStatus | Unset):
        check_in_from (datetime.date | Unset):
        check_in_to (datetime.date | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketReservationListResponse
     """


    return (await asyncio_detailed(
        client=client,
property_id=property_id,
status=status,
check_in_from=check_in_from,
check_in_to=check_in_to,
limit=limit,
offset=offset,

    )).parsed
