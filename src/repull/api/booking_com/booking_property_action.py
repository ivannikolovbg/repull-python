from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_property_action_request import BookingPropertyActionRequest
from ...models.booking_property_action_response import BookingPropertyActionResponse
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: BookingPropertyActionRequest,
    hotel_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    params: dict[str, Any] = {}

    params["hotel_id"] = hotel_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/booking/properties/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BookingPropertyActionResponse | Error | None:
    if response.status_code == 200:
        response_200 = BookingPropertyActionResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = Error.from_dict(response.json())



        return response_402

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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BookingPropertyActionResponse | Error]:
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
    body: BookingPropertyActionRequest,
    hotel_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[BookingPropertyActionResponse | Error]:
    """ Take a property off sale / put it back (unlist/relist)

     Stop this listing's Booking.com property being sold, or start it again. `id` is a **Repull listing
    id**, not a Booking.com hotel id, as on the GET.

    **Booking.com has no unlist, so this is an availability write.** Airbnb has a real deactivate;
    Booking.com does not. `unlist` closes the mapped room across the whole forward window, so the
    property stops selling. `relist` is not its mirror image: it re-syncs the true calendar, so dates
    that are genuinely blocked (a reservation, an owner stay) stay blocked and only the closure `unlist`
    wrote lifts. Re-opening everything would sell dates that are not for sale.

    **Which property gets closed.** A listing can be mapped to more than one Booking.com property — the
    same unit re-listed under a new property keeps its old mapping, and workspaces routinely sit on five
    or six. With exactly one, send nothing. With several, name one with `hotelId` (or `?hotel_id=`);
    omit it and the request is refused with **`409 ambiguous_booking_mapping`** listing the candidates,
    and nothing is written. That refusal matters more here than on a publish: writing content into the
    wrong property is recoverable, closing the wrong property's availability takes real inventory off
    sale while the property you meant keeps selling. Naming a property this listing is not mapped to is
    a `404` that names the ones it is.

    **This does not change the listing in Repull.** `active` — what Repull bills and serves — is
    untouched by both actions and is deliberately not echoed in the response, so the two ideas can never
    be read as one field. To take a listing off the market on every channel at once, use `POST
    /v1/listings/{id}/offline`.

    Any other action returns a structured `422` naming the ones that are supported. To push content use
    `POST /v1/listings/{id}/publish/booking`; to map rooms use `POST /v1/connect/booking/map-rooms`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (BookingPropertyActionRequest): Take this listing's Booking.com property off sale, or
            put it back.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingPropertyActionResponse | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
hotel_id=hotel_id,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: BookingPropertyActionRequest,
    hotel_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> BookingPropertyActionResponse | Error | None:
    """ Take a property off sale / put it back (unlist/relist)

     Stop this listing's Booking.com property being sold, or start it again. `id` is a **Repull listing
    id**, not a Booking.com hotel id, as on the GET.

    **Booking.com has no unlist, so this is an availability write.** Airbnb has a real deactivate;
    Booking.com does not. `unlist` closes the mapped room across the whole forward window, so the
    property stops selling. `relist` is not its mirror image: it re-syncs the true calendar, so dates
    that are genuinely blocked (a reservation, an owner stay) stay blocked and only the closure `unlist`
    wrote lifts. Re-opening everything would sell dates that are not for sale.

    **Which property gets closed.** A listing can be mapped to more than one Booking.com property — the
    same unit re-listed under a new property keeps its old mapping, and workspaces routinely sit on five
    or six. With exactly one, send nothing. With several, name one with `hotelId` (or `?hotel_id=`);
    omit it and the request is refused with **`409 ambiguous_booking_mapping`** listing the candidates,
    and nothing is written. That refusal matters more here than on a publish: writing content into the
    wrong property is recoverable, closing the wrong property's availability takes real inventory off
    sale while the property you meant keeps selling. Naming a property this listing is not mapped to is
    a `404` that names the ones it is.

    **This does not change the listing in Repull.** `active` — what Repull bills and serves — is
    untouched by both actions and is deliberately not echoed in the response, so the two ideas can never
    be read as one field. To take a listing off the market on every channel at once, use `POST
    /v1/listings/{id}/offline`.

    Any other action returns a structured `422` naming the ones that are supported. To push content use
    `POST /v1/listings/{id}/publish/booking`; to map rooms use `POST /v1/connect/booking/map-rooms`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (BookingPropertyActionRequest): Take this listing's Booking.com property off sale, or
            put it back.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingPropertyActionResponse | Error
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
hotel_id=hotel_id,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: BookingPropertyActionRequest,
    hotel_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[BookingPropertyActionResponse | Error]:
    """ Take a property off sale / put it back (unlist/relist)

     Stop this listing's Booking.com property being sold, or start it again. `id` is a **Repull listing
    id**, not a Booking.com hotel id, as on the GET.

    **Booking.com has no unlist, so this is an availability write.** Airbnb has a real deactivate;
    Booking.com does not. `unlist` closes the mapped room across the whole forward window, so the
    property stops selling. `relist` is not its mirror image: it re-syncs the true calendar, so dates
    that are genuinely blocked (a reservation, an owner stay) stay blocked and only the closure `unlist`
    wrote lifts. Re-opening everything would sell dates that are not for sale.

    **Which property gets closed.** A listing can be mapped to more than one Booking.com property — the
    same unit re-listed under a new property keeps its old mapping, and workspaces routinely sit on five
    or six. With exactly one, send nothing. With several, name one with `hotelId` (or `?hotel_id=`);
    omit it and the request is refused with **`409 ambiguous_booking_mapping`** listing the candidates,
    and nothing is written. That refusal matters more here than on a publish: writing content into the
    wrong property is recoverable, closing the wrong property's availability takes real inventory off
    sale while the property you meant keeps selling. Naming a property this listing is not mapped to is
    a `404` that names the ones it is.

    **This does not change the listing in Repull.** `active` — what Repull bills and serves — is
    untouched by both actions and is deliberately not echoed in the response, so the two ideas can never
    be read as one field. To take a listing off the market on every channel at once, use `POST
    /v1/listings/{id}/offline`.

    Any other action returns a structured `422` naming the ones that are supported. To push content use
    `POST /v1/listings/{id}/publish/booking`; to map rooms use `POST /v1/connect/booking/map-rooms`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (BookingPropertyActionRequest): Take this listing's Booking.com property off sale, or
            put it back.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingPropertyActionResponse | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
hotel_id=hotel_id,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: BookingPropertyActionRequest,
    hotel_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> BookingPropertyActionResponse | Error | None:
    """ Take a property off sale / put it back (unlist/relist)

     Stop this listing's Booking.com property being sold, or start it again. `id` is a **Repull listing
    id**, not a Booking.com hotel id, as on the GET.

    **Booking.com has no unlist, so this is an availability write.** Airbnb has a real deactivate;
    Booking.com does not. `unlist` closes the mapped room across the whole forward window, so the
    property stops selling. `relist` is not its mirror image: it re-syncs the true calendar, so dates
    that are genuinely blocked (a reservation, an owner stay) stay blocked and only the closure `unlist`
    wrote lifts. Re-opening everything would sell dates that are not for sale.

    **Which property gets closed.** A listing can be mapped to more than one Booking.com property — the
    same unit re-listed under a new property keeps its old mapping, and workspaces routinely sit on five
    or six. With exactly one, send nothing. With several, name one with `hotelId` (or `?hotel_id=`);
    omit it and the request is refused with **`409 ambiguous_booking_mapping`** listing the candidates,
    and nothing is written. That refusal matters more here than on a publish: writing content into the
    wrong property is recoverable, closing the wrong property's availability takes real inventory off
    sale while the property you meant keeps selling. Naming a property this listing is not mapped to is
    a `404` that names the ones it is.

    **This does not change the listing in Repull.** `active` — what Repull bills and serves — is
    untouched by both actions and is deliberately not echoed in the response, so the two ideas can never
    be read as one field. To take a listing off the market on every channel at once, use `POST
    /v1/listings/{id}/offline`.

    Any other action returns a structured `422` naming the ones that are supported. To push content use
    `POST /v1/listings/{id}/publish/booking`; to map rooms use `POST /v1/connect/booking/map-rooms`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (BookingPropertyActionRequest): Take this listing's Booking.com property off sale, or
            put it back.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingPropertyActionResponse | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
hotel_id=hotel_id,
idempotency_key=idempotency_key,

    )).parsed
