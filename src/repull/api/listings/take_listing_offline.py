from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.listing_market_state_request import ListingMarketStateRequest
from ...models.listing_market_state_response import ListingMarketStateResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ListingMarketStateRequest | Unset = UNSET,
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
        "url": "/v1/listings/{id}/offline".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListingMarketStateResponse | None:
    if response.status_code == 200:
        response_200 = ListingMarketStateResponse.from_dict(response.json())



        return response_200

    if response.status_code == 402:
        response_402 = Error.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListingMarketStateResponse]:
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
    body: ListingMarketStateRequest | Unset = UNSET,
    hotel_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | ListingMarketStateResponse]:
    r""" Take a listing off the market

     Stop this listing being sold, on every channel it is connected to, in one call.

    What that means differs per channel and you do not have to know which is which. On **Airbnb** the
    live listing is deactivated with a valid deactivation reason and then READ BACK — Airbnb accepts
    some deactivations and leaves the listing up, so \"we sent the request\" is never reported as
    success. On **Booking.com** there is no unlist at all; the equivalent is closing the room's
    availability across the whole forward window, which is what happens.

    **This is not the same as deactivating the listing in Repull.** The two get confused because both
    sound like removal, and they have opposite consequences:

    | | Take offline (this endpoint) | Deactivate in Repull (`PATCH /v1/listings/{id}` `{\"active\":
    false}`) |
    |---|---|---|
    | The guest-facing listing | **Stops taking bookings** | Stays live and keeps taking bookings |
    | Billing and plan limits | Unchanged | No longer billed, no longer counts toward the cap |
    | API access to the listing | Unchanged — you can still read and write it | `403 listing_inactive`
    until reactivated |
    | Reverse it with | `POST /v1/listings/{id}/online` | `PATCH /v1/listings/{id}` `{\"active\": true}`
    |
    | Data kept | Yes | Yes, and it keeps syncing |

    Neither one deletes anything, on either side.

    **The answer is per channel item.** A listing can sit on several Airbnb connections and a
    Booking.com property at once; they fail independently and a partial result is the ordinary outcome,
    so every item reports its own `state`, `code` and `message` and there is no top-level success flag
    to mislead you. Nothing is rolled back — re-send the same request to retry the items that did not
    land.

    **Booking.com ambiguity is reported, not fanned out.** A listing mapped to more than one active
    Booking.com property comes back with that item refused (`ambiguous_booking_mapping`) while the
    Airbnb items still run: closing the wrong property's availability takes real inventory off sale, and
    taking a listing off Airbnb is not less urgent because its Booking.com mapping is untidy. Name the
    property with `hotelId` and send it again.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ListingMarketStateRequest | Unset): Optional. Send no body at all unless this
            listing is mapped to more than one Booking.com property.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingMarketStateResponse]
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
    body: ListingMarketStateRequest | Unset = UNSET,
    hotel_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Error | ListingMarketStateResponse | None:
    r""" Take a listing off the market

     Stop this listing being sold, on every channel it is connected to, in one call.

    What that means differs per channel and you do not have to know which is which. On **Airbnb** the
    live listing is deactivated with a valid deactivation reason and then READ BACK — Airbnb accepts
    some deactivations and leaves the listing up, so \"we sent the request\" is never reported as
    success. On **Booking.com** there is no unlist at all; the equivalent is closing the room's
    availability across the whole forward window, which is what happens.

    **This is not the same as deactivating the listing in Repull.** The two get confused because both
    sound like removal, and they have opposite consequences:

    | | Take offline (this endpoint) | Deactivate in Repull (`PATCH /v1/listings/{id}` `{\"active\":
    false}`) |
    |---|---|---|
    | The guest-facing listing | **Stops taking bookings** | Stays live and keeps taking bookings |
    | Billing and plan limits | Unchanged | No longer billed, no longer counts toward the cap |
    | API access to the listing | Unchanged — you can still read and write it | `403 listing_inactive`
    until reactivated |
    | Reverse it with | `POST /v1/listings/{id}/online` | `PATCH /v1/listings/{id}` `{\"active\": true}`
    |
    | Data kept | Yes | Yes, and it keeps syncing |

    Neither one deletes anything, on either side.

    **The answer is per channel item.** A listing can sit on several Airbnb connections and a
    Booking.com property at once; they fail independently and a partial result is the ordinary outcome,
    so every item reports its own `state`, `code` and `message` and there is no top-level success flag
    to mislead you. Nothing is rolled back — re-send the same request to retry the items that did not
    land.

    **Booking.com ambiguity is reported, not fanned out.** A listing mapped to more than one active
    Booking.com property comes back with that item refused (`ambiguous_booking_mapping`) while the
    Airbnb items still run: closing the wrong property's availability takes real inventory off sale, and
    taking a listing off Airbnb is not less urgent because its Booking.com mapping is untidy. Name the
    property with `hotelId` and send it again.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ListingMarketStateRequest | Unset): Optional. Send no body at all unless this
            listing is mapped to more than one Booking.com property.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingMarketStateResponse
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
    body: ListingMarketStateRequest | Unset = UNSET,
    hotel_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | ListingMarketStateResponse]:
    r""" Take a listing off the market

     Stop this listing being sold, on every channel it is connected to, in one call.

    What that means differs per channel and you do not have to know which is which. On **Airbnb** the
    live listing is deactivated with a valid deactivation reason and then READ BACK — Airbnb accepts
    some deactivations and leaves the listing up, so \"we sent the request\" is never reported as
    success. On **Booking.com** there is no unlist at all; the equivalent is closing the room's
    availability across the whole forward window, which is what happens.

    **This is not the same as deactivating the listing in Repull.** The two get confused because both
    sound like removal, and they have opposite consequences:

    | | Take offline (this endpoint) | Deactivate in Repull (`PATCH /v1/listings/{id}` `{\"active\":
    false}`) |
    |---|---|---|
    | The guest-facing listing | **Stops taking bookings** | Stays live and keeps taking bookings |
    | Billing and plan limits | Unchanged | No longer billed, no longer counts toward the cap |
    | API access to the listing | Unchanged — you can still read and write it | `403 listing_inactive`
    until reactivated |
    | Reverse it with | `POST /v1/listings/{id}/online` | `PATCH /v1/listings/{id}` `{\"active\": true}`
    |
    | Data kept | Yes | Yes, and it keeps syncing |

    Neither one deletes anything, on either side.

    **The answer is per channel item.** A listing can sit on several Airbnb connections and a
    Booking.com property at once; they fail independently and a partial result is the ordinary outcome,
    so every item reports its own `state`, `code` and `message` and there is no top-level success flag
    to mislead you. Nothing is rolled back — re-send the same request to retry the items that did not
    land.

    **Booking.com ambiguity is reported, not fanned out.** A listing mapped to more than one active
    Booking.com property comes back with that item refused (`ambiguous_booking_mapping`) while the
    Airbnb items still run: closing the wrong property's availability takes real inventory off sale, and
    taking a listing off Airbnb is not less urgent because its Booking.com mapping is untidy. Name the
    property with `hotelId` and send it again.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ListingMarketStateRequest | Unset): Optional. Send no body at all unless this
            listing is mapped to more than one Booking.com property.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingMarketStateResponse]
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
    body: ListingMarketStateRequest | Unset = UNSET,
    hotel_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Error | ListingMarketStateResponse | None:
    r""" Take a listing off the market

     Stop this listing being sold, on every channel it is connected to, in one call.

    What that means differs per channel and you do not have to know which is which. On **Airbnb** the
    live listing is deactivated with a valid deactivation reason and then READ BACK — Airbnb accepts
    some deactivations and leaves the listing up, so \"we sent the request\" is never reported as
    success. On **Booking.com** there is no unlist at all; the equivalent is closing the room's
    availability across the whole forward window, which is what happens.

    **This is not the same as deactivating the listing in Repull.** The two get confused because both
    sound like removal, and they have opposite consequences:

    | | Take offline (this endpoint) | Deactivate in Repull (`PATCH /v1/listings/{id}` `{\"active\":
    false}`) |
    |---|---|---|
    | The guest-facing listing | **Stops taking bookings** | Stays live and keeps taking bookings |
    | Billing and plan limits | Unchanged | No longer billed, no longer counts toward the cap |
    | API access to the listing | Unchanged — you can still read and write it | `403 listing_inactive`
    until reactivated |
    | Reverse it with | `POST /v1/listings/{id}/online` | `PATCH /v1/listings/{id}` `{\"active\": true}`
    |
    | Data kept | Yes | Yes, and it keeps syncing |

    Neither one deletes anything, on either side.

    **The answer is per channel item.** A listing can sit on several Airbnb connections and a
    Booking.com property at once; they fail independently and a partial result is the ordinary outcome,
    so every item reports its own `state`, `code` and `message` and there is no top-level success flag
    to mislead you. Nothing is rolled back — re-send the same request to retry the items that did not
    land.

    **Booking.com ambiguity is reported, not fanned out.** A listing mapped to more than one active
    Booking.com property comes back with that item refused (`ambiguous_booking_mapping`) while the
    Airbnb items still run: closing the wrong property's availability takes real inventory off sale, and
    taking a listing off Airbnb is not less urgent because its Booking.com mapping is untidy. Name the
    property with `hotelId` and send it again.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ListingMarketStateRequest | Unset): Optional. Send no body at all unless this
            listing is mapped to more than one Booking.com property.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingMarketStateResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
hotel_id=hotel_id,
idempotency_key=idempotency_key,

    )).parsed
