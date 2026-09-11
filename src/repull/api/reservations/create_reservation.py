from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.reservation_create_request import ReservationCreateRequest
from ...models.reservation_create_response import ReservationCreateResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: ReservationCreateRequest,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/reservations",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ReservationCreateResponse | None:
    if response.status_code == 201:
        response_201 = ReservationCreateResponse.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ReservationCreateResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReservationCreateRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | ReservationCreateResponse]:
    """ Create a reservation

     Creates a reservation and everything that hangs off one: the guest, the conversation thread, the
    dashboard item, the calendar block, and the `reservation.created` fan-out that issues the door code
    and starts the messaging automations.

    **Platform is restricted to `direct`, `website` and `owner`.** Reservations on Airbnb, Booking.com
    and Vrbo are owned by the channel and arrive through sync — creating one here would mint a local
    booking the channel has never heard of, which then fights the next sync. Create those on the
    channel.

    **Dates are validated** (`YYYY-MM-DD`, and `checkOut` must be after `checkIn`), and an unrecognised
    field is rejected by name rather than silently ignored.

    **This endpoint does not set the price.** There is no `totalPrice` field: the reservation pipeline
    derives the price breakdown from the property's own rates and overwrites anything supplied, so
    accepting a total would be taking a value and discarding it. A reservation created here is priced by
    that engine (`0` when the property has no rates for the range). `currency` IS honoured. Quote a stay
    with `GET /v1/quotes` before booking if you need the figure up front.

    **Availability is NOT checked.** This creates the reservation you asked for even if the dates
    overlap an existing booking. Call `GET /v1/availability/{propertyId}` first if that matters.

    Send `Idempotency-Key` — a network timeout here is exactly the case it exists for: without it, a
    retry books the guest twice.

    Args:
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ReservationCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReservationCreateResponse]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ReservationCreateRequest,
    idempotency_key: str | Unset = UNSET,

) -> Error | ReservationCreateResponse | None:
    """ Create a reservation

     Creates a reservation and everything that hangs off one: the guest, the conversation thread, the
    dashboard item, the calendar block, and the `reservation.created` fan-out that issues the door code
    and starts the messaging automations.

    **Platform is restricted to `direct`, `website` and `owner`.** Reservations on Airbnb, Booking.com
    and Vrbo are owned by the channel and arrive through sync — creating one here would mint a local
    booking the channel has never heard of, which then fights the next sync. Create those on the
    channel.

    **Dates are validated** (`YYYY-MM-DD`, and `checkOut` must be after `checkIn`), and an unrecognised
    field is rejected by name rather than silently ignored.

    **This endpoint does not set the price.** There is no `totalPrice` field: the reservation pipeline
    derives the price breakdown from the property's own rates and overwrites anything supplied, so
    accepting a total would be taking a value and discarding it. A reservation created here is priced by
    that engine (`0` when the property has no rates for the range). `currency` IS honoured. Quote a stay
    with `GET /v1/quotes` before booking if you need the figure up front.

    **Availability is NOT checked.** This creates the reservation you asked for even if the dates
    overlap an existing booking. Call `GET /v1/availability/{propertyId}` first if that matters.

    Send `Idempotency-Key` — a network timeout here is exactly the case it exists for: without it, a
    retry books the guest twice.

    Args:
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ReservationCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReservationCreateResponse
     """


    return sync_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReservationCreateRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | ReservationCreateResponse]:
    """ Create a reservation

     Creates a reservation and everything that hangs off one: the guest, the conversation thread, the
    dashboard item, the calendar block, and the `reservation.created` fan-out that issues the door code
    and starts the messaging automations.

    **Platform is restricted to `direct`, `website` and `owner`.** Reservations on Airbnb, Booking.com
    and Vrbo are owned by the channel and arrive through sync — creating one here would mint a local
    booking the channel has never heard of, which then fights the next sync. Create those on the
    channel.

    **Dates are validated** (`YYYY-MM-DD`, and `checkOut` must be after `checkIn`), and an unrecognised
    field is rejected by name rather than silently ignored.

    **This endpoint does not set the price.** There is no `totalPrice` field: the reservation pipeline
    derives the price breakdown from the property's own rates and overwrites anything supplied, so
    accepting a total would be taking a value and discarding it. A reservation created here is priced by
    that engine (`0` when the property has no rates for the range). `currency` IS honoured. Quote a stay
    with `GET /v1/quotes` before booking if you need the figure up front.

    **Availability is NOT checked.** This creates the reservation you asked for even if the dates
    overlap an existing booking. Call `GET /v1/availability/{propertyId}` first if that matters.

    Send `Idempotency-Key` — a network timeout here is exactly the case it exists for: without it, a
    retry books the guest twice.

    Args:
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ReservationCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReservationCreateResponse]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ReservationCreateRequest,
    idempotency_key: str | Unset = UNSET,

) -> Error | ReservationCreateResponse | None:
    """ Create a reservation

     Creates a reservation and everything that hangs off one: the guest, the conversation thread, the
    dashboard item, the calendar block, and the `reservation.created` fan-out that issues the door code
    and starts the messaging automations.

    **Platform is restricted to `direct`, `website` and `owner`.** Reservations on Airbnb, Booking.com
    and Vrbo are owned by the channel and arrive through sync — creating one here would mint a local
    booking the channel has never heard of, which then fights the next sync. Create those on the
    channel.

    **Dates are validated** (`YYYY-MM-DD`, and `checkOut` must be after `checkIn`), and an unrecognised
    field is rejected by name rather than silently ignored.

    **This endpoint does not set the price.** There is no `totalPrice` field: the reservation pipeline
    derives the price breakdown from the property's own rates and overwrites anything supplied, so
    accepting a total would be taking a value and discarding it. A reservation created here is priced by
    that engine (`0` when the property has no rates for the range). `currency` IS honoured. Quote a stay
    with `GET /v1/quotes` before booking if you need the figure up front.

    **Availability is NOT checked.** This creates the reservation you asked for even if the dates
    overlap an existing booking. Call `GET /v1/availability/{propertyId}` first if that matters.

    Send `Idempotency-Key` — a network timeout here is exactly the case it exists for: without it, a
    retry books the guest twice.

    Args:
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ReservationCreateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReservationCreateResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
