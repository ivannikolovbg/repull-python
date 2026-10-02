from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cancel_reservation_body import CancelReservationBody
from ...models.cancel_reservation_response_200 import CancelReservationResponse200
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: CancelReservationBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/reservations/{id}/cancel".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CancelReservationResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = CancelReservationResponse200.from_dict(response.json())



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

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CancelReservationResponse200 | Error]:
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
    body: CancelReservationBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,

) -> Response[CancelReservationResponse200 | Error]:
    """ Cancel a reservation

     Cancels a reservation where it lives.

    - **A booking managed in a connected PMS** (Mews, Cloudbeds, Hostaway, Guesty, Beds24, BookingSync,
    Lodgify, Smoobu, Hospitable, iGMS): cancelled in the PMS, then read back, so Repull and the PMS
    agree. No cancellation fee is charged. Lodgify *declines* the booking rather than deleting it.
    **OwnerRez's API cannot cancel** — `422 pms_write_unsupported`; cancel it in OwnerRez. `GET
    /v1/listings/{id}` → `capabilities.reservations.cancel` says which applies.
    - **Direct, website or owner bookings**: cancelled in Repull — the nights are released and
    `reservation.cancelled` fires.
    - **A channel booking** (Airbnb, Booking.com, VRBO), including one that came in through a PMS: `409
    reservation_owned_by_channel`. Cancel it on the channel; the cancellation reaches Repull with the
    next sync.

    Cancelling an already-cancelled reservation is not an error: the response carries `alreadyCancelled:
    true`.

    PMS integrations other than Mews and Cloudbeds are verified against the vendor's API documentation
    only.

    `X-Account-Id` restricts the reservation to one connected account. Returns `403 listing_inactive`
    when the listing is inactive.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        x_account_id (str | Unset):  Example: 126.
        body (CancelReservationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelReservationResponse200 | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
idempotency_key=idempotency_key,
x_account_id=x_account_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CancelReservationBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,

) -> CancelReservationResponse200 | Error | None:
    """ Cancel a reservation

     Cancels a reservation where it lives.

    - **A booking managed in a connected PMS** (Mews, Cloudbeds, Hostaway, Guesty, Beds24, BookingSync,
    Lodgify, Smoobu, Hospitable, iGMS): cancelled in the PMS, then read back, so Repull and the PMS
    agree. No cancellation fee is charged. Lodgify *declines* the booking rather than deleting it.
    **OwnerRez's API cannot cancel** — `422 pms_write_unsupported`; cancel it in OwnerRez. `GET
    /v1/listings/{id}` → `capabilities.reservations.cancel` says which applies.
    - **Direct, website or owner bookings**: cancelled in Repull — the nights are released and
    `reservation.cancelled` fires.
    - **A channel booking** (Airbnb, Booking.com, VRBO), including one that came in through a PMS: `409
    reservation_owned_by_channel`. Cancel it on the channel; the cancellation reaches Repull with the
    next sync.

    Cancelling an already-cancelled reservation is not an error: the response carries `alreadyCancelled:
    true`.

    PMS integrations other than Mews and Cloudbeds are verified against the vendor's API documentation
    only.

    `X-Account-Id` restricts the reservation to one connected account. Returns `403 listing_inactive`
    when the listing is inactive.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        x_account_id (str | Unset):  Example: 126.
        body (CancelReservationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelReservationResponse200 | Error
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,
x_account_id=x_account_id,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CancelReservationBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,

) -> Response[CancelReservationResponse200 | Error]:
    """ Cancel a reservation

     Cancels a reservation where it lives.

    - **A booking managed in a connected PMS** (Mews, Cloudbeds, Hostaway, Guesty, Beds24, BookingSync,
    Lodgify, Smoobu, Hospitable, iGMS): cancelled in the PMS, then read back, so Repull and the PMS
    agree. No cancellation fee is charged. Lodgify *declines* the booking rather than deleting it.
    **OwnerRez's API cannot cancel** — `422 pms_write_unsupported`; cancel it in OwnerRez. `GET
    /v1/listings/{id}` → `capabilities.reservations.cancel` says which applies.
    - **Direct, website or owner bookings**: cancelled in Repull — the nights are released and
    `reservation.cancelled` fires.
    - **A channel booking** (Airbnb, Booking.com, VRBO), including one that came in through a PMS: `409
    reservation_owned_by_channel`. Cancel it on the channel; the cancellation reaches Repull with the
    next sync.

    Cancelling an already-cancelled reservation is not an error: the response carries `alreadyCancelled:
    true`.

    PMS integrations other than Mews and Cloudbeds are verified against the vendor's API documentation
    only.

    `X-Account-Id` restricts the reservation to one connected account. Returns `403 listing_inactive`
    when the listing is inactive.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        x_account_id (str | Unset):  Example: 126.
        body (CancelReservationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelReservationResponse200 | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
idempotency_key=idempotency_key,
x_account_id=x_account_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CancelReservationBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,

) -> CancelReservationResponse200 | Error | None:
    """ Cancel a reservation

     Cancels a reservation where it lives.

    - **A booking managed in a connected PMS** (Mews, Cloudbeds, Hostaway, Guesty, Beds24, BookingSync,
    Lodgify, Smoobu, Hospitable, iGMS): cancelled in the PMS, then read back, so Repull and the PMS
    agree. No cancellation fee is charged. Lodgify *declines* the booking rather than deleting it.
    **OwnerRez's API cannot cancel** — `422 pms_write_unsupported`; cancel it in OwnerRez. `GET
    /v1/listings/{id}` → `capabilities.reservations.cancel` says which applies.
    - **Direct, website or owner bookings**: cancelled in Repull — the nights are released and
    `reservation.cancelled` fires.
    - **A channel booking** (Airbnb, Booking.com, VRBO), including one that came in through a PMS: `409
    reservation_owned_by_channel`. Cancel it on the channel; the cancellation reaches Repull with the
    next sync.

    Cancelling an already-cancelled reservation is not an error: the response carries `alreadyCancelled:
    true`.

    PMS integrations other than Mews and Cloudbeds are verified against the vendor's API documentation
    only.

    `X-Account-Id` restricts the reservation to one connected account. Returns `403 listing_inactive`
    when the listing is inactive.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        x_account_id (str | Unset):  Example: 126.
        body (CancelReservationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelReservationResponse200 | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,
x_account_id=x_account_id,

    )).parsed
