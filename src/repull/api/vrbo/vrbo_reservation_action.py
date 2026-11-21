from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.vrbo_reservation_action_body import VrboReservationActionBody
from ...models.vrbo_reservation_action_response_200 import VrboReservationActionResponse200
from typing import cast



def _get_kwargs(
    code: str,
    *,
    body: VrboReservationActionBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/vrbo/reservations/{code}".format(code=quote(str(code), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | VrboReservationActionResponse200 | None:
    if response.status_code == 200:
        response_200 = VrboReservationActionResponse200.from_dict(response.json())



        return response_200

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

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | VrboReservationActionResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    code: str,
    *,
    client: AuthenticatedClient | Client,
    body: VrboReservationActionBody,

) -> Response[Error | VrboReservationActionResponse200]:
    """ Accept, decline, cancel, charge or refund a Vrbo reservation

     Act on a Vrbo booking by its confirmation code — the counterpart of `POST
    /v1/channels/airbnb/reservations/{code}`, plus Vrbo's extra charge and refund. **Write-side**:
    Vrbo's own host-app actions, as the account that owns the booking.

    - `accept` — accept a pending booking request. Optional `message` to the guest (≤ 250 characters).
    - `decline` — decline a pending booking request. `reason` is one of Vrbo's decline reasons
    (`?options=decline`); `block_dates: true` also blocks the dates (default: they stay open).
    - `cancel` — cancel a booking as the host. `reason`: `property-sold-or-ownership-change`, `conflict-
    with-house-rules`, `dates-booked-on-another-platform`, `extenuating-circumstance` or `payment-not-
    received` (Vrbo's list, read live: `?options=cancel`); `message` to the guest, 25–250 characters;
    `refund_level` (default `FULL`). **Host cancellations carry Vrbo penalties** — the listing hidden
    for 7 days and a fee from your payout, unless the cancellation was unavoidable.
    - `charge` — request an extra payment from the guest: `fee_type` (Vrbo's list, e.g. `PARKING`,
    `HOT_TUB`, `DEPARTURE_LATE`), `amount` (1–10,000, the booking's currency), `message` (≤ 50
    characters) and `due_date`.
    - `refund` — refund the guest part of what they paid: `reason`, `amount`, `message`. Vrbo offers it
    once the guest has paid.

    **`preview: true`** (cancel, charge, refund) returns Vrbo's own dry run — for a cancel, the terms
    and penalties (`penalties.cancellationFee`, `penalties.listingHidden`, `refundToGuest`); for a
    charge, the guest's total with taxes — and changes nothing. Without it, the dry run runs first and
    the action after, once: a lost answer is `502 vrbo_unconfirmed` (read the booking before retrying),
    never a second cancel.

    Changing dates, times, guests or price is `POST /v1/channels/vrbo/alterations`. The body is
    validated before anything reaches Vrbo; unknown fields are refused by name. Returns `403
    listing_inactive` when the listing is inactive.

    Args:
        code (str):  Example: HA-8K2P3Q.
        body (VrboReservationActionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | VrboReservationActionResponse200]
     """


    kwargs = _get_kwargs(
        code=code,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    code: str,
    *,
    client: AuthenticatedClient | Client,
    body: VrboReservationActionBody,

) -> Error | VrboReservationActionResponse200 | None:
    """ Accept, decline, cancel, charge or refund a Vrbo reservation

     Act on a Vrbo booking by its confirmation code — the counterpart of `POST
    /v1/channels/airbnb/reservations/{code}`, plus Vrbo's extra charge and refund. **Write-side**:
    Vrbo's own host-app actions, as the account that owns the booking.

    - `accept` — accept a pending booking request. Optional `message` to the guest (≤ 250 characters).
    - `decline` — decline a pending booking request. `reason` is one of Vrbo's decline reasons
    (`?options=decline`); `block_dates: true` also blocks the dates (default: they stay open).
    - `cancel` — cancel a booking as the host. `reason`: `property-sold-or-ownership-change`, `conflict-
    with-house-rules`, `dates-booked-on-another-platform`, `extenuating-circumstance` or `payment-not-
    received` (Vrbo's list, read live: `?options=cancel`); `message` to the guest, 25–250 characters;
    `refund_level` (default `FULL`). **Host cancellations carry Vrbo penalties** — the listing hidden
    for 7 days and a fee from your payout, unless the cancellation was unavoidable.
    - `charge` — request an extra payment from the guest: `fee_type` (Vrbo's list, e.g. `PARKING`,
    `HOT_TUB`, `DEPARTURE_LATE`), `amount` (1–10,000, the booking's currency), `message` (≤ 50
    characters) and `due_date`.
    - `refund` — refund the guest part of what they paid: `reason`, `amount`, `message`. Vrbo offers it
    once the guest has paid.

    **`preview: true`** (cancel, charge, refund) returns Vrbo's own dry run — for a cancel, the terms
    and penalties (`penalties.cancellationFee`, `penalties.listingHidden`, `refundToGuest`); for a
    charge, the guest's total with taxes — and changes nothing. Without it, the dry run runs first and
    the action after, once: a lost answer is `502 vrbo_unconfirmed` (read the booking before retrying),
    never a second cancel.

    Changing dates, times, guests or price is `POST /v1/channels/vrbo/alterations`. The body is
    validated before anything reaches Vrbo; unknown fields are refused by name. Returns `403
    listing_inactive` when the listing is inactive.

    Args:
        code (str):  Example: HA-8K2P3Q.
        body (VrboReservationActionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | VrboReservationActionResponse200
     """


    return sync_detailed(
        code=code,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    code: str,
    *,
    client: AuthenticatedClient | Client,
    body: VrboReservationActionBody,

) -> Response[Error | VrboReservationActionResponse200]:
    """ Accept, decline, cancel, charge or refund a Vrbo reservation

     Act on a Vrbo booking by its confirmation code — the counterpart of `POST
    /v1/channels/airbnb/reservations/{code}`, plus Vrbo's extra charge and refund. **Write-side**:
    Vrbo's own host-app actions, as the account that owns the booking.

    - `accept` — accept a pending booking request. Optional `message` to the guest (≤ 250 characters).
    - `decline` — decline a pending booking request. `reason` is one of Vrbo's decline reasons
    (`?options=decline`); `block_dates: true` also blocks the dates (default: they stay open).
    - `cancel` — cancel a booking as the host. `reason`: `property-sold-or-ownership-change`, `conflict-
    with-house-rules`, `dates-booked-on-another-platform`, `extenuating-circumstance` or `payment-not-
    received` (Vrbo's list, read live: `?options=cancel`); `message` to the guest, 25–250 characters;
    `refund_level` (default `FULL`). **Host cancellations carry Vrbo penalties** — the listing hidden
    for 7 days and a fee from your payout, unless the cancellation was unavoidable.
    - `charge` — request an extra payment from the guest: `fee_type` (Vrbo's list, e.g. `PARKING`,
    `HOT_TUB`, `DEPARTURE_LATE`), `amount` (1–10,000, the booking's currency), `message` (≤ 50
    characters) and `due_date`.
    - `refund` — refund the guest part of what they paid: `reason`, `amount`, `message`. Vrbo offers it
    once the guest has paid.

    **`preview: true`** (cancel, charge, refund) returns Vrbo's own dry run — for a cancel, the terms
    and penalties (`penalties.cancellationFee`, `penalties.listingHidden`, `refundToGuest`); for a
    charge, the guest's total with taxes — and changes nothing. Without it, the dry run runs first and
    the action after, once: a lost answer is `502 vrbo_unconfirmed` (read the booking before retrying),
    never a second cancel.

    Changing dates, times, guests or price is `POST /v1/channels/vrbo/alterations`. The body is
    validated before anything reaches Vrbo; unknown fields are refused by name. Returns `403
    listing_inactive` when the listing is inactive.

    Args:
        code (str):  Example: HA-8K2P3Q.
        body (VrboReservationActionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | VrboReservationActionResponse200]
     """


    kwargs = _get_kwargs(
        code=code,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    code: str,
    *,
    client: AuthenticatedClient | Client,
    body: VrboReservationActionBody,

) -> Error | VrboReservationActionResponse200 | None:
    """ Accept, decline, cancel, charge or refund a Vrbo reservation

     Act on a Vrbo booking by its confirmation code — the counterpart of `POST
    /v1/channels/airbnb/reservations/{code}`, plus Vrbo's extra charge and refund. **Write-side**:
    Vrbo's own host-app actions, as the account that owns the booking.

    - `accept` — accept a pending booking request. Optional `message` to the guest (≤ 250 characters).
    - `decline` — decline a pending booking request. `reason` is one of Vrbo's decline reasons
    (`?options=decline`); `block_dates: true` also blocks the dates (default: they stay open).
    - `cancel` — cancel a booking as the host. `reason`: `property-sold-or-ownership-change`, `conflict-
    with-house-rules`, `dates-booked-on-another-platform`, `extenuating-circumstance` or `payment-not-
    received` (Vrbo's list, read live: `?options=cancel`); `message` to the guest, 25–250 characters;
    `refund_level` (default `FULL`). **Host cancellations carry Vrbo penalties** — the listing hidden
    for 7 days and a fee from your payout, unless the cancellation was unavoidable.
    - `charge` — request an extra payment from the guest: `fee_type` (Vrbo's list, e.g. `PARKING`,
    `HOT_TUB`, `DEPARTURE_LATE`), `amount` (1–10,000, the booking's currency), `message` (≤ 50
    characters) and `due_date`.
    - `refund` — refund the guest part of what they paid: `reason`, `amount`, `message`. Vrbo offers it
    once the guest has paid.

    **`preview: true`** (cancel, charge, refund) returns Vrbo's own dry run — for a cancel, the terms
    and penalties (`penalties.cancellationFee`, `penalties.listingHidden`, `refundToGuest`); for a
    charge, the guest's total with taxes — and changes nothing. Without it, the dry run runs first and
    the action after, once: a lost answer is `502 vrbo_unconfirmed` (read the booking before retrying),
    never a second cancel.

    Changing dates, times, guests or price is `POST /v1/channels/vrbo/alterations`. The body is
    validated before anything reaches Vrbo; unknown fields are refused by name. Returns `403
    listing_inactive` when the listing is inactive.

    Args:
        code (str):  Example: HA-8K2P3Q.
        body (VrboReservationActionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | VrboReservationActionResponse200
     """


    return (await asyncio_detailed(
        code=code,
client=client,
body=body,

    )).parsed
