from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_availability_update_request import BookingAvailabilityUpdateRequest
from ...models.booking_pricing_update_response import BookingPricingUpdateResponse
from ...models.error import Error
from typing import cast



def _get_kwargs(
    *,
    body: BookingAvailabilityUpdateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/booking/availability",
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
    *,
    client: AuthenticatedClient | Client,
    body: BookingAvailabilityUpdateRequest,

) -> Response[BookingPricingUpdateResponse | Error]:
    r""" Update Booking.com rates/availability

     Write rates, availability and restrictions to a Booking.com property. `type` selects the write:

    - `rates` — nightly prices, plus any length-of-stay / arrival restrictions sent with them.
    - `availability` — inventory (`availableRooms`), the stop-sell flag (`closed`), and restrictions.
    Omit `availableRooms` and `closed` for a restriction-only write.
    - `derived-pricing` — occupancy-derived pricing rules.

    **Dates are inclusive at both ends.** `{ \"start\": \"2026-11-04\", \"end\": \"2026-11-04\" }` is
    exactly one night.

    **A rate amount needs an occupancy.** Booking.com stores the amount against the party size the rate
    plan prices: sent above that number it declines the price in silence, sent below it it answers 400.
    Send `occupancy`, or omit it and Repull resolves it from Booking.com's own data and echoes the value
    and its `source` back in `occupancy[]`. If it cannot be resolved the write is refused with `422`
    naming `updates[N].occupancy`.

    **Restrictions are sent in the same call, on their own wire.** A price and a minimum stay are two
    writes on Booking.com's side. Send them together and the response reports each separately: `price`
    and `restrictions` carry their own state, their own read-back, and — when refused — Booking.com's
    own reason. The top-level `applied` is `partial` when they disagree, so a price that landed is never
    reported as a failure. `minStay`, `maxStay`, `minStayArrival`, `maxStayArrival`, `closedToArrival`
    and `closedToDeparture` are written; `exactStayArrival`, `minAdvanceRes` and `maxAdvanceRes` are
    refused with `422 restriction_not_supported` because Booking.com's notification has no element for
    them — set those on the rate plan in the Extranet. Nothing you send is ever silently ignored.

    **Inventory is not part of a rate update.** `roomsToSell` on a `rates` update returns `422
    inventory_not_in_rate_update`; send it as `type: \"availability\"` instead.

    **The response says what is known.** Booking.com acknowledges a write with no per-date status, so
    the nights are read back — prices and restrictions out of the same read: `applied` is `verified`,
    `mismatch`, `partial`, `rejected` or `unverified` (send `verify: false` to skip the read-back). A
    bare acknowledgement is never reported as \"all updates applied\". Booking.com stores a 1-night
    minimum as no minimum, so `minStay: 1` reads back as `0` and still counts as applied.

    Restrictions never leak across channels — this endpoint writes only to Booking.com. When Booking.com
    refuses a write outright, their own reason comes back as `422 booking_rejected` with `booking_ruid`;
    a genuine outage on their side is `502 booking_error`.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        body (BookingAvailabilityUpdateRequest): Body for `PUT /v1/channels/booking/availability`.
            `type` selects which of Booking.com's writes to perform. Date ranges are inclusive at both
            ends everywhere in this body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingPricingUpdateResponse | Error]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: BookingAvailabilityUpdateRequest,

) -> BookingPricingUpdateResponse | Error | None:
    r""" Update Booking.com rates/availability

     Write rates, availability and restrictions to a Booking.com property. `type` selects the write:

    - `rates` — nightly prices, plus any length-of-stay / arrival restrictions sent with them.
    - `availability` — inventory (`availableRooms`), the stop-sell flag (`closed`), and restrictions.
    Omit `availableRooms` and `closed` for a restriction-only write.
    - `derived-pricing` — occupancy-derived pricing rules.

    **Dates are inclusive at both ends.** `{ \"start\": \"2026-11-04\", \"end\": \"2026-11-04\" }` is
    exactly one night.

    **A rate amount needs an occupancy.** Booking.com stores the amount against the party size the rate
    plan prices: sent above that number it declines the price in silence, sent below it it answers 400.
    Send `occupancy`, or omit it and Repull resolves it from Booking.com's own data and echoes the value
    and its `source` back in `occupancy[]`. If it cannot be resolved the write is refused with `422`
    naming `updates[N].occupancy`.

    **Restrictions are sent in the same call, on their own wire.** A price and a minimum stay are two
    writes on Booking.com's side. Send them together and the response reports each separately: `price`
    and `restrictions` carry their own state, their own read-back, and — when refused — Booking.com's
    own reason. The top-level `applied` is `partial` when they disagree, so a price that landed is never
    reported as a failure. `minStay`, `maxStay`, `minStayArrival`, `maxStayArrival`, `closedToArrival`
    and `closedToDeparture` are written; `exactStayArrival`, `minAdvanceRes` and `maxAdvanceRes` are
    refused with `422 restriction_not_supported` because Booking.com's notification has no element for
    them — set those on the rate plan in the Extranet. Nothing you send is ever silently ignored.

    **Inventory is not part of a rate update.** `roomsToSell` on a `rates` update returns `422
    inventory_not_in_rate_update`; send it as `type: \"availability\"` instead.

    **The response says what is known.** Booking.com acknowledges a write with no per-date status, so
    the nights are read back — prices and restrictions out of the same read: `applied` is `verified`,
    `mismatch`, `partial`, `rejected` or `unverified` (send `verify: false` to skip the read-back). A
    bare acknowledgement is never reported as \"all updates applied\". Booking.com stores a 1-night
    minimum as no minimum, so `minStay: 1` reads back as `0` and still counts as applied.

    Restrictions never leak across channels — this endpoint writes only to Booking.com. When Booking.com
    refuses a write outright, their own reason comes back as `422 booking_rejected` with `booking_ruid`;
    a genuine outage on their side is `502 booking_error`.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        body (BookingAvailabilityUpdateRequest): Body for `PUT /v1/channels/booking/availability`.
            `type` selects which of Booking.com's writes to perform. Date ranges are inclusive at both
            ends everywhere in this body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingPricingUpdateResponse | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BookingAvailabilityUpdateRequest,

) -> Response[BookingPricingUpdateResponse | Error]:
    r""" Update Booking.com rates/availability

     Write rates, availability and restrictions to a Booking.com property. `type` selects the write:

    - `rates` — nightly prices, plus any length-of-stay / arrival restrictions sent with them.
    - `availability` — inventory (`availableRooms`), the stop-sell flag (`closed`), and restrictions.
    Omit `availableRooms` and `closed` for a restriction-only write.
    - `derived-pricing` — occupancy-derived pricing rules.

    **Dates are inclusive at both ends.** `{ \"start\": \"2026-11-04\", \"end\": \"2026-11-04\" }` is
    exactly one night.

    **A rate amount needs an occupancy.** Booking.com stores the amount against the party size the rate
    plan prices: sent above that number it declines the price in silence, sent below it it answers 400.
    Send `occupancy`, or omit it and Repull resolves it from Booking.com's own data and echoes the value
    and its `source` back in `occupancy[]`. If it cannot be resolved the write is refused with `422`
    naming `updates[N].occupancy`.

    **Restrictions are sent in the same call, on their own wire.** A price and a minimum stay are two
    writes on Booking.com's side. Send them together and the response reports each separately: `price`
    and `restrictions` carry their own state, their own read-back, and — when refused — Booking.com's
    own reason. The top-level `applied` is `partial` when they disagree, so a price that landed is never
    reported as a failure. `minStay`, `maxStay`, `minStayArrival`, `maxStayArrival`, `closedToArrival`
    and `closedToDeparture` are written; `exactStayArrival`, `minAdvanceRes` and `maxAdvanceRes` are
    refused with `422 restriction_not_supported` because Booking.com's notification has no element for
    them — set those on the rate plan in the Extranet. Nothing you send is ever silently ignored.

    **Inventory is not part of a rate update.** `roomsToSell` on a `rates` update returns `422
    inventory_not_in_rate_update`; send it as `type: \"availability\"` instead.

    **The response says what is known.** Booking.com acknowledges a write with no per-date status, so
    the nights are read back — prices and restrictions out of the same read: `applied` is `verified`,
    `mismatch`, `partial`, `rejected` or `unverified` (send `verify: false` to skip the read-back). A
    bare acknowledgement is never reported as \"all updates applied\". Booking.com stores a 1-night
    minimum as no minimum, so `minStay: 1` reads back as `0` and still counts as applied.

    Restrictions never leak across channels — this endpoint writes only to Booking.com. When Booking.com
    refuses a write outright, their own reason comes back as `422 booking_rejected` with `booking_ruid`;
    a genuine outage on their side is `502 booking_error`.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        body (BookingAvailabilityUpdateRequest): Body for `PUT /v1/channels/booking/availability`.
            `type` selects which of Booking.com's writes to perform. Date ranges are inclusive at both
            ends everywhere in this body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingPricingUpdateResponse | Error]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: BookingAvailabilityUpdateRequest,

) -> BookingPricingUpdateResponse | Error | None:
    r""" Update Booking.com rates/availability

     Write rates, availability and restrictions to a Booking.com property. `type` selects the write:

    - `rates` — nightly prices, plus any length-of-stay / arrival restrictions sent with them.
    - `availability` — inventory (`availableRooms`), the stop-sell flag (`closed`), and restrictions.
    Omit `availableRooms` and `closed` for a restriction-only write.
    - `derived-pricing` — occupancy-derived pricing rules.

    **Dates are inclusive at both ends.** `{ \"start\": \"2026-11-04\", \"end\": \"2026-11-04\" }` is
    exactly one night.

    **A rate amount needs an occupancy.** Booking.com stores the amount against the party size the rate
    plan prices: sent above that number it declines the price in silence, sent below it it answers 400.
    Send `occupancy`, or omit it and Repull resolves it from Booking.com's own data and echoes the value
    and its `source` back in `occupancy[]`. If it cannot be resolved the write is refused with `422`
    naming `updates[N].occupancy`.

    **Restrictions are sent in the same call, on their own wire.** A price and a minimum stay are two
    writes on Booking.com's side. Send them together and the response reports each separately: `price`
    and `restrictions` carry their own state, their own read-back, and — when refused — Booking.com's
    own reason. The top-level `applied` is `partial` when they disagree, so a price that landed is never
    reported as a failure. `minStay`, `maxStay`, `minStayArrival`, `maxStayArrival`, `closedToArrival`
    and `closedToDeparture` are written; `exactStayArrival`, `minAdvanceRes` and `maxAdvanceRes` are
    refused with `422 restriction_not_supported` because Booking.com's notification has no element for
    them — set those on the rate plan in the Extranet. Nothing you send is ever silently ignored.

    **Inventory is not part of a rate update.** `roomsToSell` on a `rates` update returns `422
    inventory_not_in_rate_update`; send it as `type: \"availability\"` instead.

    **The response says what is known.** Booking.com acknowledges a write with no per-date status, so
    the nights are read back — prices and restrictions out of the same read: `applied` is `verified`,
    `mismatch`, `partial`, `rejected` or `unverified` (send `verify: false` to skip the read-back). A
    bare acknowledgement is never reported as \"all updates applied\". Booking.com stores a 1-night
    minimum as no minimum, so `minStay: 1` reads back as `0` and still counts as applied.

    Restrictions never leak across channels — this endpoint writes only to Booking.com. When Booking.com
    refuses a write outright, their own reason comes back as `422 booking_rejected` with `booking_ruid`;
    a genuine outage on their side is `502 booking_error`.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        body (BookingAvailabilityUpdateRequest): Body for `PUT /v1/channels/booking/availability`.
            `type` selects which of Booking.com's writes to perform. Date ranges are inclusive at both
            ends everywhere in this body.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingPricingUpdateResponse | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
