from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_pricing_update_request import BookingPricingUpdateRequest
from ...models.booking_pricing_update_response import BookingPricingUpdateResponse
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: BookingPricingUpdateRequest,
    hotel_id: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["hotel_id"] = hotel_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/booking/listings/{id}/pricing".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BookingPricingUpdateResponse | Error | None:
    if response.status_code == 200:
        response_200 = BookingPricingUpdateResponse.from_dict(response.json())



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

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BookingPricingUpdateResponse | Error]:
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
    body: BookingPricingUpdateRequest,
    hotel_id: str | Unset = UNSET,

) -> Response[BookingPricingUpdateResponse | Error]:
    r""" Update Booking.com pricing for a listing

     Writes nightly prices for a listing's Booking.com room + rate plan. Each update needs `roomId` +
    `rateId` + `dateRange` + `price` + `currency`; `dateRange` is inclusive at both ends, so `start`
    equal to `end` writes exactly one night.

    **Occupancy.** Booking.com stores a rate amount against the party size the rate plan prices. Send
    `occupancy` and that is what is used; omit it and it is resolved from Booking.com's own data for
    that (room, rate plan) and echoed back in `occupancy[]` with its `source`. When it cannot be
    resolved the write is refused with `422` naming `updates[N].occupancy` — a price is never sent at a
    guessed party size, because Booking.com declines such an amount without saying so.

    **Inventory is a separate write.** `roomsToSell` on a rate update returns `422
    inventory_not_in_rate_update`; use `PUT /v1/channels/booking/availability` with `type:
    \"availability\"`.

    **Restrictions ride along, on their own wire.** Send `restrictions` with the price and Booking.com
    receives two writes; the response reports each separately in `price` and `restrictions`, each with
    its own state, read-back and — when refused — Booking.com's own reason. `minStay`, `maxStay`,
    `minStayArrival`, `maxStayArrival`, `closedToArrival` and `closedToDeparture` are written;
    `exactStayArrival`, `minAdvanceRes` and `maxAdvanceRes` are refused with `422
    restriction_not_supported` (Booking.com's notification has no element for them — set those on the
    rate plan in the Extranet). Nothing you send is silently ignored.

    **The response says what is known.** Booking.com acknowledges a write without per-date status, so
    the affected nights are read back — prices and restrictions out of the same read — and `applied`
    reports `verified`, `mismatch`, `partial`, `rejected` or `unverified`. `partial` means one half
    landed and the other did not, which is never reported as a total failure. Send `verify: false` to
    skip the read-back; `applied` is then `unverified`. Booking.com stores a 1-night minimum as no
    minimum, so `minStay: 1` reads back as `0` and still counts as applied.

    `id` is a Repull listing id. When it is published under several Booking.com properties this returns
    `409 ambiguous_booking_mapping` and pushes nothing — name the property with `?hotel_id=` instead.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        body (BookingPricingUpdateRequest): Body for `PUT
            /v1/channels/booking/listings/{id}/pricing`. Pricing on Booking is per-room/per-rate-plan,
            so `room_id` + `rate_id` are required on every update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingPricingUpdateResponse | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
hotel_id=hotel_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: BookingPricingUpdateRequest,
    hotel_id: str | Unset = UNSET,

) -> BookingPricingUpdateResponse | Error | None:
    r""" Update Booking.com pricing for a listing

     Writes nightly prices for a listing's Booking.com room + rate plan. Each update needs `roomId` +
    `rateId` + `dateRange` + `price` + `currency`; `dateRange` is inclusive at both ends, so `start`
    equal to `end` writes exactly one night.

    **Occupancy.** Booking.com stores a rate amount against the party size the rate plan prices. Send
    `occupancy` and that is what is used; omit it and it is resolved from Booking.com's own data for
    that (room, rate plan) and echoed back in `occupancy[]` with its `source`. When it cannot be
    resolved the write is refused with `422` naming `updates[N].occupancy` — a price is never sent at a
    guessed party size, because Booking.com declines such an amount without saying so.

    **Inventory is a separate write.** `roomsToSell` on a rate update returns `422
    inventory_not_in_rate_update`; use `PUT /v1/channels/booking/availability` with `type:
    \"availability\"`.

    **Restrictions ride along, on their own wire.** Send `restrictions` with the price and Booking.com
    receives two writes; the response reports each separately in `price` and `restrictions`, each with
    its own state, read-back and — when refused — Booking.com's own reason. `minStay`, `maxStay`,
    `minStayArrival`, `maxStayArrival`, `closedToArrival` and `closedToDeparture` are written;
    `exactStayArrival`, `minAdvanceRes` and `maxAdvanceRes` are refused with `422
    restriction_not_supported` (Booking.com's notification has no element for them — set those on the
    rate plan in the Extranet). Nothing you send is silently ignored.

    **The response says what is known.** Booking.com acknowledges a write without per-date status, so
    the affected nights are read back — prices and restrictions out of the same read — and `applied`
    reports `verified`, `mismatch`, `partial`, `rejected` or `unverified`. `partial` means one half
    landed and the other did not, which is never reported as a total failure. Send `verify: false` to
    skip the read-back; `applied` is then `unverified`. Booking.com stores a 1-night minimum as no
    minimum, so `minStay: 1` reads back as `0` and still counts as applied.

    `id` is a Repull listing id. When it is published under several Booking.com properties this returns
    `409 ambiguous_booking_mapping` and pushes nothing — name the property with `?hotel_id=` instead.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        body (BookingPricingUpdateRequest): Body for `PUT
            /v1/channels/booking/listings/{id}/pricing`. Pricing on Booking is per-room/per-rate-plan,
            so `room_id` + `rate_id` are required on every update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingPricingUpdateResponse | Error
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
hotel_id=hotel_id,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: BookingPricingUpdateRequest,
    hotel_id: str | Unset = UNSET,

) -> Response[BookingPricingUpdateResponse | Error]:
    r""" Update Booking.com pricing for a listing

     Writes nightly prices for a listing's Booking.com room + rate plan. Each update needs `roomId` +
    `rateId` + `dateRange` + `price` + `currency`; `dateRange` is inclusive at both ends, so `start`
    equal to `end` writes exactly one night.

    **Occupancy.** Booking.com stores a rate amount against the party size the rate plan prices. Send
    `occupancy` and that is what is used; omit it and it is resolved from Booking.com's own data for
    that (room, rate plan) and echoed back in `occupancy[]` with its `source`. When it cannot be
    resolved the write is refused with `422` naming `updates[N].occupancy` — a price is never sent at a
    guessed party size, because Booking.com declines such an amount without saying so.

    **Inventory is a separate write.** `roomsToSell` on a rate update returns `422
    inventory_not_in_rate_update`; use `PUT /v1/channels/booking/availability` with `type:
    \"availability\"`.

    **Restrictions ride along, on their own wire.** Send `restrictions` with the price and Booking.com
    receives two writes; the response reports each separately in `price` and `restrictions`, each with
    its own state, read-back and — when refused — Booking.com's own reason. `minStay`, `maxStay`,
    `minStayArrival`, `maxStayArrival`, `closedToArrival` and `closedToDeparture` are written;
    `exactStayArrival`, `minAdvanceRes` and `maxAdvanceRes` are refused with `422
    restriction_not_supported` (Booking.com's notification has no element for them — set those on the
    rate plan in the Extranet). Nothing you send is silently ignored.

    **The response says what is known.** Booking.com acknowledges a write without per-date status, so
    the affected nights are read back — prices and restrictions out of the same read — and `applied`
    reports `verified`, `mismatch`, `partial`, `rejected` or `unverified`. `partial` means one half
    landed and the other did not, which is never reported as a total failure. Send `verify: false` to
    skip the read-back; `applied` is then `unverified`. Booking.com stores a 1-night minimum as no
    minimum, so `minStay: 1` reads back as `0` and still counts as applied.

    `id` is a Repull listing id. When it is published under several Booking.com properties this returns
    `409 ambiguous_booking_mapping` and pushes nothing — name the property with `?hotel_id=` instead.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        body (BookingPricingUpdateRequest): Body for `PUT
            /v1/channels/booking/listings/{id}/pricing`. Pricing on Booking is per-room/per-rate-plan,
            so `room_id` + `rate_id` are required on every update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingPricingUpdateResponse | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
hotel_id=hotel_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: BookingPricingUpdateRequest,
    hotel_id: str | Unset = UNSET,

) -> BookingPricingUpdateResponse | Error | None:
    r""" Update Booking.com pricing for a listing

     Writes nightly prices for a listing's Booking.com room + rate plan. Each update needs `roomId` +
    `rateId` + `dateRange` + `price` + `currency`; `dateRange` is inclusive at both ends, so `start`
    equal to `end` writes exactly one night.

    **Occupancy.** Booking.com stores a rate amount against the party size the rate plan prices. Send
    `occupancy` and that is what is used; omit it and it is resolved from Booking.com's own data for
    that (room, rate plan) and echoed back in `occupancy[]` with its `source`. When it cannot be
    resolved the write is refused with `422` naming `updates[N].occupancy` — a price is never sent at a
    guessed party size, because Booking.com declines such an amount without saying so.

    **Inventory is a separate write.** `roomsToSell` on a rate update returns `422
    inventory_not_in_rate_update`; use `PUT /v1/channels/booking/availability` with `type:
    \"availability\"`.

    **Restrictions ride along, on their own wire.** Send `restrictions` with the price and Booking.com
    receives two writes; the response reports each separately in `price` and `restrictions`, each with
    its own state, read-back and — when refused — Booking.com's own reason. `minStay`, `maxStay`,
    `minStayArrival`, `maxStayArrival`, `closedToArrival` and `closedToDeparture` are written;
    `exactStayArrival`, `minAdvanceRes` and `maxAdvanceRes` are refused with `422
    restriction_not_supported` (Booking.com's notification has no element for them — set those on the
    rate plan in the Extranet). Nothing you send is silently ignored.

    **The response says what is known.** Booking.com acknowledges a write without per-date status, so
    the affected nights are read back — prices and restrictions out of the same read — and `applied`
    reports `verified`, `mismatch`, `partial`, `rejected` or `unverified`. `partial` means one half
    landed and the other did not, which is never reported as a total failure. Send `verify: false` to
    skip the read-back; `applied` is then `unverified`. Booking.com stores a 1-night minimum as no
    minimum, so `minStay: 1` reads back as `0` and still counts as applied.

    `id` is a Repull listing id. When it is published under several Booking.com properties this returns
    `409 ambiguous_booking_mapping` and pushes nothing — name the property with `?hotel_id=` instead.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        body (BookingPricingUpdateRequest): Body for `PUT
            /v1/channels/booking/listings/{id}/pricing`. Pricing on Booking is per-room/per-rate-plan,
            so `room_id` + `rate_id` are required on every update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingPricingUpdateResponse | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
hotel_id=hotel_id,

    )).parsed
