from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_availability_update_request import BookingAvailabilityUpdateRequest
from ...models.booking_derived_pricing_write_response import BookingDerivedPricingWriteResponse
from ...models.booking_pricing_update_response import BookingPricingUpdateResponse
from ...models.booking_restriction_write_response import BookingRestrictionWriteResponse
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



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BookingDerivedPricingWriteResponse | BookingPricingUpdateResponse | BookingRestrictionWriteResponse | Error | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> BookingDerivedPricingWriteResponse | BookingPricingUpdateResponse | BookingRestrictionWriteResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = BookingPricingUpdateResponse.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = BookingRestrictionWriteResponse.from_dict(data)



                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = BookingDerivedPricingWriteResponse.from_dict(data)



            return response_200_type_2

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BookingDerivedPricingWriteResponse | BookingPricingUpdateResponse | BookingRestrictionWriteResponse | Error]:
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

) -> Response[BookingDerivedPricingWriteResponse | BookingPricingUpdateResponse | BookingRestrictionWriteResponse | Error]:
    r""" Update Booking.com rates/availability

     Write rates, availability and restrictions to a Booking.com property. `type` selects the write:

    - `rates` — nightly prices, plus any length-of-stay / arrival restrictions sent with them.
    - `availability` — inventory (`availableRooms`), the stop-sell flag (`closed`), and restrictions.
    Omit `availableRooms` and `closed` for a restriction-only write.
    - `derived-pricing` — occupancy-based pricing: what a smaller party pays relative to the nightly
    price (see below).

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

    **Length-of-stay limits.** Booking.com keeps a maximum stay of 1–90 nights and a minimum of 1–91;
    `0` removes the limit. A value outside that is refused with `422 restriction_out_of_range` naming
    the field — Booking.com would acknowledge it and then store something else (a `maxStayArrival` of
    365 is stored as no maximum), so send `0` for \"no limit\". `minStay`/`maxStay` are stay-through
    limits (any stay covering the night); `minStayArrival`/`maxStayArrival` apply only to stays that
    start on the night.

    **Occupancy-based pricing (`type: \"derived-pricing\"`).** The nightly price you write with `type:
    \"rates\"` is the price for `leadingOccupancy` guests (the rate plan's `maxPersons`). Each item in
    `occupancies` prices another party size relative to it: `additional` is a signed amount in the rate
    currency, `percentage` a signed percent. The rule applies to every night, date-specific prices
    included. A write replaces the rate plan's whole rule set; `\"occupancies\": []` removes every rule.
    Example — EUR 12.01 off for 1 and 2 guests on a 3-guest rate: `{\"type\":\"derived-pricing\",\"prope
    rty_id\":\"17610853\",\"updates\":[{\"roomId\":\"1761085301\",\"rateId\":\"70596570\",\"leadingOccup
    ancy\":3,\"occupancies\":[{\"persons\":2,\"additional\":-12.01},{\"persons\":1,\"additional\":-
    12.01}]}]}`. The rules are read back after the write, and at any time on `GET
    /v1/channels/booking/properties/{id}/rooms` (`rates[].occupancyPricing`). A wrong shape is `422
    invalid_params` naming the field; a rule Booking.com refuses is `422 booking_rejected` with its
    code.

    **Inventory is not part of a rate update.** `roomsToSell` on a `rates` update returns `422
    inventory_not_in_rate_update`; send it as `type: \"availability\"` instead.

    **The response says what is known.** Booking.com acknowledges a write with no per-date status, so
    the nights are read back — prices and restrictions out of the same read: `applied` is `verified`,
    `mismatch`, `partial`, `rejected` or `unverified` (send `verify: false` to skip the read-back). A
    restriction-only `availability` write is read back the same way. Every night is read, however long
    the range. A bare acknowledgement is never reported as \"all updates applied\". Booking.com stores a
    1-night minimum as no minimum, so `minStay: 1` reads back as `0` and still counts as applied.

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
            ends everywhere in this body. Example: {'type': 'derived-pricing', 'property_id':
            '17610853', 'updates': [{'roomId': '1761085301', 'rateId': '70596570', 'leadingOccupancy':
            3, 'occupancies': [{'persons': 2, 'additional': -12.01}, {'persons': 1, 'additional':
            -12.01}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingDerivedPricingWriteResponse | BookingPricingUpdateResponse | BookingRestrictionWriteResponse | Error]
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

) -> BookingDerivedPricingWriteResponse | BookingPricingUpdateResponse | BookingRestrictionWriteResponse | Error | None:
    r""" Update Booking.com rates/availability

     Write rates, availability and restrictions to a Booking.com property. `type` selects the write:

    - `rates` — nightly prices, plus any length-of-stay / arrival restrictions sent with them.
    - `availability` — inventory (`availableRooms`), the stop-sell flag (`closed`), and restrictions.
    Omit `availableRooms` and `closed` for a restriction-only write.
    - `derived-pricing` — occupancy-based pricing: what a smaller party pays relative to the nightly
    price (see below).

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

    **Length-of-stay limits.** Booking.com keeps a maximum stay of 1–90 nights and a minimum of 1–91;
    `0` removes the limit. A value outside that is refused with `422 restriction_out_of_range` naming
    the field — Booking.com would acknowledge it and then store something else (a `maxStayArrival` of
    365 is stored as no maximum), so send `0` for \"no limit\". `minStay`/`maxStay` are stay-through
    limits (any stay covering the night); `minStayArrival`/`maxStayArrival` apply only to stays that
    start on the night.

    **Occupancy-based pricing (`type: \"derived-pricing\"`).** The nightly price you write with `type:
    \"rates\"` is the price for `leadingOccupancy` guests (the rate plan's `maxPersons`). Each item in
    `occupancies` prices another party size relative to it: `additional` is a signed amount in the rate
    currency, `percentage` a signed percent. The rule applies to every night, date-specific prices
    included. A write replaces the rate plan's whole rule set; `\"occupancies\": []` removes every rule.
    Example — EUR 12.01 off for 1 and 2 guests on a 3-guest rate: `{\"type\":\"derived-pricing\",\"prope
    rty_id\":\"17610853\",\"updates\":[{\"roomId\":\"1761085301\",\"rateId\":\"70596570\",\"leadingOccup
    ancy\":3,\"occupancies\":[{\"persons\":2,\"additional\":-12.01},{\"persons\":1,\"additional\":-
    12.01}]}]}`. The rules are read back after the write, and at any time on `GET
    /v1/channels/booking/properties/{id}/rooms` (`rates[].occupancyPricing`). A wrong shape is `422
    invalid_params` naming the field; a rule Booking.com refuses is `422 booking_rejected` with its
    code.

    **Inventory is not part of a rate update.** `roomsToSell` on a `rates` update returns `422
    inventory_not_in_rate_update`; send it as `type: \"availability\"` instead.

    **The response says what is known.** Booking.com acknowledges a write with no per-date status, so
    the nights are read back — prices and restrictions out of the same read: `applied` is `verified`,
    `mismatch`, `partial`, `rejected` or `unverified` (send `verify: false` to skip the read-back). A
    restriction-only `availability` write is read back the same way. Every night is read, however long
    the range. A bare acknowledgement is never reported as \"all updates applied\". Booking.com stores a
    1-night minimum as no minimum, so `minStay: 1` reads back as `0` and still counts as applied.

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
            ends everywhere in this body. Example: {'type': 'derived-pricing', 'property_id':
            '17610853', 'updates': [{'roomId': '1761085301', 'rateId': '70596570', 'leadingOccupancy':
            3, 'occupancies': [{'persons': 2, 'additional': -12.01}, {'persons': 1, 'additional':
            -12.01}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingDerivedPricingWriteResponse | BookingPricingUpdateResponse | BookingRestrictionWriteResponse | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BookingAvailabilityUpdateRequest,

) -> Response[BookingDerivedPricingWriteResponse | BookingPricingUpdateResponse | BookingRestrictionWriteResponse | Error]:
    r""" Update Booking.com rates/availability

     Write rates, availability and restrictions to a Booking.com property. `type` selects the write:

    - `rates` — nightly prices, plus any length-of-stay / arrival restrictions sent with them.
    - `availability` — inventory (`availableRooms`), the stop-sell flag (`closed`), and restrictions.
    Omit `availableRooms` and `closed` for a restriction-only write.
    - `derived-pricing` — occupancy-based pricing: what a smaller party pays relative to the nightly
    price (see below).

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

    **Length-of-stay limits.** Booking.com keeps a maximum stay of 1–90 nights and a minimum of 1–91;
    `0` removes the limit. A value outside that is refused with `422 restriction_out_of_range` naming
    the field — Booking.com would acknowledge it and then store something else (a `maxStayArrival` of
    365 is stored as no maximum), so send `0` for \"no limit\". `minStay`/`maxStay` are stay-through
    limits (any stay covering the night); `minStayArrival`/`maxStayArrival` apply only to stays that
    start on the night.

    **Occupancy-based pricing (`type: \"derived-pricing\"`).** The nightly price you write with `type:
    \"rates\"` is the price for `leadingOccupancy` guests (the rate plan's `maxPersons`). Each item in
    `occupancies` prices another party size relative to it: `additional` is a signed amount in the rate
    currency, `percentage` a signed percent. The rule applies to every night, date-specific prices
    included. A write replaces the rate plan's whole rule set; `\"occupancies\": []` removes every rule.
    Example — EUR 12.01 off for 1 and 2 guests on a 3-guest rate: `{\"type\":\"derived-pricing\",\"prope
    rty_id\":\"17610853\",\"updates\":[{\"roomId\":\"1761085301\",\"rateId\":\"70596570\",\"leadingOccup
    ancy\":3,\"occupancies\":[{\"persons\":2,\"additional\":-12.01},{\"persons\":1,\"additional\":-
    12.01}]}]}`. The rules are read back after the write, and at any time on `GET
    /v1/channels/booking/properties/{id}/rooms` (`rates[].occupancyPricing`). A wrong shape is `422
    invalid_params` naming the field; a rule Booking.com refuses is `422 booking_rejected` with its
    code.

    **Inventory is not part of a rate update.** `roomsToSell` on a `rates` update returns `422
    inventory_not_in_rate_update`; send it as `type: \"availability\"` instead.

    **The response says what is known.** Booking.com acknowledges a write with no per-date status, so
    the nights are read back — prices and restrictions out of the same read: `applied` is `verified`,
    `mismatch`, `partial`, `rejected` or `unverified` (send `verify: false` to skip the read-back). A
    restriction-only `availability` write is read back the same way. Every night is read, however long
    the range. A bare acknowledgement is never reported as \"all updates applied\". Booking.com stores a
    1-night minimum as no minimum, so `minStay: 1` reads back as `0` and still counts as applied.

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
            ends everywhere in this body. Example: {'type': 'derived-pricing', 'property_id':
            '17610853', 'updates': [{'roomId': '1761085301', 'rateId': '70596570', 'leadingOccupancy':
            3, 'occupancies': [{'persons': 2, 'additional': -12.01}, {'persons': 1, 'additional':
            -12.01}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingDerivedPricingWriteResponse | BookingPricingUpdateResponse | BookingRestrictionWriteResponse | Error]
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

) -> BookingDerivedPricingWriteResponse | BookingPricingUpdateResponse | BookingRestrictionWriteResponse | Error | None:
    r""" Update Booking.com rates/availability

     Write rates, availability and restrictions to a Booking.com property. `type` selects the write:

    - `rates` — nightly prices, plus any length-of-stay / arrival restrictions sent with them.
    - `availability` — inventory (`availableRooms`), the stop-sell flag (`closed`), and restrictions.
    Omit `availableRooms` and `closed` for a restriction-only write.
    - `derived-pricing` — occupancy-based pricing: what a smaller party pays relative to the nightly
    price (see below).

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

    **Length-of-stay limits.** Booking.com keeps a maximum stay of 1–90 nights and a minimum of 1–91;
    `0` removes the limit. A value outside that is refused with `422 restriction_out_of_range` naming
    the field — Booking.com would acknowledge it and then store something else (a `maxStayArrival` of
    365 is stored as no maximum), so send `0` for \"no limit\". `minStay`/`maxStay` are stay-through
    limits (any stay covering the night); `minStayArrival`/`maxStayArrival` apply only to stays that
    start on the night.

    **Occupancy-based pricing (`type: \"derived-pricing\"`).** The nightly price you write with `type:
    \"rates\"` is the price for `leadingOccupancy` guests (the rate plan's `maxPersons`). Each item in
    `occupancies` prices another party size relative to it: `additional` is a signed amount in the rate
    currency, `percentage` a signed percent. The rule applies to every night, date-specific prices
    included. A write replaces the rate plan's whole rule set; `\"occupancies\": []` removes every rule.
    Example — EUR 12.01 off for 1 and 2 guests on a 3-guest rate: `{\"type\":\"derived-pricing\",\"prope
    rty_id\":\"17610853\",\"updates\":[{\"roomId\":\"1761085301\",\"rateId\":\"70596570\",\"leadingOccup
    ancy\":3,\"occupancies\":[{\"persons\":2,\"additional\":-12.01},{\"persons\":1,\"additional\":-
    12.01}]}]}`. The rules are read back after the write, and at any time on `GET
    /v1/channels/booking/properties/{id}/rooms` (`rates[].occupancyPricing`). A wrong shape is `422
    invalid_params` naming the field; a rule Booking.com refuses is `422 booking_rejected` with its
    code.

    **Inventory is not part of a rate update.** `roomsToSell` on a `rates` update returns `422
    inventory_not_in_rate_update`; send it as `type: \"availability\"` instead.

    **The response says what is known.** Booking.com acknowledges a write with no per-date status, so
    the nights are read back — prices and restrictions out of the same read: `applied` is `verified`,
    `mismatch`, `partial`, `rejected` or `unverified` (send `verify: false` to skip the read-back). A
    restriction-only `availability` write is read back the same way. Every night is read, however long
    the range. A bare acknowledgement is never reported as \"all updates applied\". Booking.com stores a
    1-night minimum as no minimum, so `minStay: 1` reads back as `0` and still counts as applied.

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
            ends everywhere in this body. Example: {'type': 'derived-pricing', 'property_id':
            '17610853', 'updates': [{'roomId': '1761085301', 'rateId': '70596570', 'leadingOccupancy':
            3, 'occupancies': [{'persons': 2, 'additional': -12.01}, {'persons': 1, 'additional':
            -12.01}]}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingDerivedPricingWriteResponse | BookingPricingUpdateResponse | BookingRestrictionWriteResponse | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
