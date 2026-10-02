from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.reservation_quote_request import ReservationQuoteRequest
from ...models.reservation_quote_response import ReservationQuoteResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: ReservationQuoteRequest,
    x_account_id: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/reservations/quote",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ReservationQuoteResponse | None:
    if response.status_code == 200:
        response_200 = ReservationQuoteResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ReservationQuoteResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReservationQuoteRequest,
    x_account_id: str | Unset = UNSET,

) -> Response[Error | ReservationQuoteResponse]:
    """ Quote a reservation in the PMS

     Prices a stay and checks its availability **in the PMS that manages the listing**, without booking
    anything. It is the same check `POST /v1/reservations` makes before booking when no `totalPrice` is
    sent, so `available: true` with a `total` is what that create would be priced at (dates can still be
    taken in between).

    `available: false` is an answer, not an error: the PMS's reasons are in `restrictions` (minimum
    stay, closed to arrival, taken dates…).

    - A listing **not managed in a PMS** answers `422 pms_not_linked`. Book it directly with `POST
    /v1/reservations`, or price it with `GET /v1/quotes`.
    - A PMS **without a quote API** (Mews, Cloudbeds, iGMS) answers `422 pms_write_unsupported`. You can
    still create the booking; on iGMS a `totalPrice` is required.

    `GET /v1/listings/{id}` → `capabilities.reservations.quote` says whether a listing can be quoted.

    ### Per-PMS limits

    | PMS | create | change | cancel | quote | `totalPrice` | Limits |
    |---|---|---|---|---|---|---|
    | Mews | ✓ | ✓ | ✓ | – | ✓ | — |
    | Cloudbeds | ✓ | ✓ | ✓ | – | – | Books at the rate plan's price; group bookings supported. |
    | Hostaway | ✓ | ✓ | ✓ | ✓ | ✓ | Direct-channel bookings only; a specific unit is refused; a date
    change keeps the booked total. |
    | Guesty | ✓ | ✓ | ✓ | ✓ | ✓ | Cancels direct and Vrbo bookings; other channel bookings are
    cancelled on the channel. |
    | Beds24 | ✓ | ✓ | ✓ | ✓ | ✓ | Needs the `write:bookings` scope; a multi-room property needs
    `unitId`. |
    | BookingSync | ✓ | ✓ | ✓ | ✓ | ✓ | Needs `bookings_write`; fees and taxes are not itemized; no
    guest email. |
    | Lodgify | ✓ | ✓ | ✓ (declines) | ✓ | ✓ | Cancel declines the booking; single-room bookings. |
    | Smoobu | ✓ | ✓ (no dates) | ✓ | ✓ | ✓ | Dates cannot be changed through Smoobu's API — cancel and
    rebook, or change them in Smoobu. |
    | Hospitable | ✓ | ✓ | ✓ | ✓ (Direct plan) | ✓ | Manual reservations only; needs
    `reservation:write`; adds no fees or taxes. |
    | iGMS | ✓ | ✓ | ✓ | – | ✓ (required) | iGMS direct bookings only; a price is required; no tentative
    holds. |
    | OwnerRez | ✓ | ✓ | – | ✓ | – | No cancel through OwnerRez's API; priced by the property's own
    rates; needs the `full` scope. |

    Every PMS except Cloudbeds refuses group bookings, and every vacation-rental PMS refuses to change
    or cancel a booking that came from a channel (Airbnb, Booking.com, Vrbo…) — that is done on the
    channel.

    **Verification.** Mews and Cloudbeds were run end to end on their vendors' sandboxes. Every other
    PMS is **verified against the vendor's API documentation only** — no live account has been written
    to yet. `capabilities.reservations.verifiedAgainst` says which.

    `X-Account-Id` restricts the listing to one connected account. Returns `403 listing_inactive` when
    the listing is inactive.

    Args:
        x_account_id (str | Unset):  Example: 126.
        body (ReservationQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReservationQuoteResponse]
     """


    kwargs = _get_kwargs(
        body=body,
x_account_id=x_account_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ReservationQuoteRequest,
    x_account_id: str | Unset = UNSET,

) -> Error | ReservationQuoteResponse | None:
    """ Quote a reservation in the PMS

     Prices a stay and checks its availability **in the PMS that manages the listing**, without booking
    anything. It is the same check `POST /v1/reservations` makes before booking when no `totalPrice` is
    sent, so `available: true` with a `total` is what that create would be priced at (dates can still be
    taken in between).

    `available: false` is an answer, not an error: the PMS's reasons are in `restrictions` (minimum
    stay, closed to arrival, taken dates…).

    - A listing **not managed in a PMS** answers `422 pms_not_linked`. Book it directly with `POST
    /v1/reservations`, or price it with `GET /v1/quotes`.
    - A PMS **without a quote API** (Mews, Cloudbeds, iGMS) answers `422 pms_write_unsupported`. You can
    still create the booking; on iGMS a `totalPrice` is required.

    `GET /v1/listings/{id}` → `capabilities.reservations.quote` says whether a listing can be quoted.

    ### Per-PMS limits

    | PMS | create | change | cancel | quote | `totalPrice` | Limits |
    |---|---|---|---|---|---|---|
    | Mews | ✓ | ✓ | ✓ | – | ✓ | — |
    | Cloudbeds | ✓ | ✓ | ✓ | – | – | Books at the rate plan's price; group bookings supported. |
    | Hostaway | ✓ | ✓ | ✓ | ✓ | ✓ | Direct-channel bookings only; a specific unit is refused; a date
    change keeps the booked total. |
    | Guesty | ✓ | ✓ | ✓ | ✓ | ✓ | Cancels direct and Vrbo bookings; other channel bookings are
    cancelled on the channel. |
    | Beds24 | ✓ | ✓ | ✓ | ✓ | ✓ | Needs the `write:bookings` scope; a multi-room property needs
    `unitId`. |
    | BookingSync | ✓ | ✓ | ✓ | ✓ | ✓ | Needs `bookings_write`; fees and taxes are not itemized; no
    guest email. |
    | Lodgify | ✓ | ✓ | ✓ (declines) | ✓ | ✓ | Cancel declines the booking; single-room bookings. |
    | Smoobu | ✓ | ✓ (no dates) | ✓ | ✓ | ✓ | Dates cannot be changed through Smoobu's API — cancel and
    rebook, or change them in Smoobu. |
    | Hospitable | ✓ | ✓ | ✓ | ✓ (Direct plan) | ✓ | Manual reservations only; needs
    `reservation:write`; adds no fees or taxes. |
    | iGMS | ✓ | ✓ | ✓ | – | ✓ (required) | iGMS direct bookings only; a price is required; no tentative
    holds. |
    | OwnerRez | ✓ | ✓ | – | ✓ | – | No cancel through OwnerRez's API; priced by the property's own
    rates; needs the `full` scope. |

    Every PMS except Cloudbeds refuses group bookings, and every vacation-rental PMS refuses to change
    or cancel a booking that came from a channel (Airbnb, Booking.com, Vrbo…) — that is done on the
    channel.

    **Verification.** Mews and Cloudbeds were run end to end on their vendors' sandboxes. Every other
    PMS is **verified against the vendor's API documentation only** — no live account has been written
    to yet. `capabilities.reservations.verifiedAgainst` says which.

    `X-Account-Id` restricts the listing to one connected account. Returns `403 listing_inactive` when
    the listing is inactive.

    Args:
        x_account_id (str | Unset):  Example: 126.
        body (ReservationQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReservationQuoteResponse
     """


    return sync_detailed(
        client=client,
body=body,
x_account_id=x_account_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReservationQuoteRequest,
    x_account_id: str | Unset = UNSET,

) -> Response[Error | ReservationQuoteResponse]:
    """ Quote a reservation in the PMS

     Prices a stay and checks its availability **in the PMS that manages the listing**, without booking
    anything. It is the same check `POST /v1/reservations` makes before booking when no `totalPrice` is
    sent, so `available: true` with a `total` is what that create would be priced at (dates can still be
    taken in between).

    `available: false` is an answer, not an error: the PMS's reasons are in `restrictions` (minimum
    stay, closed to arrival, taken dates…).

    - A listing **not managed in a PMS** answers `422 pms_not_linked`. Book it directly with `POST
    /v1/reservations`, or price it with `GET /v1/quotes`.
    - A PMS **without a quote API** (Mews, Cloudbeds, iGMS) answers `422 pms_write_unsupported`. You can
    still create the booking; on iGMS a `totalPrice` is required.

    `GET /v1/listings/{id}` → `capabilities.reservations.quote` says whether a listing can be quoted.

    ### Per-PMS limits

    | PMS | create | change | cancel | quote | `totalPrice` | Limits |
    |---|---|---|---|---|---|---|
    | Mews | ✓ | ✓ | ✓ | – | ✓ | — |
    | Cloudbeds | ✓ | ✓ | ✓ | – | – | Books at the rate plan's price; group bookings supported. |
    | Hostaway | ✓ | ✓ | ✓ | ✓ | ✓ | Direct-channel bookings only; a specific unit is refused; a date
    change keeps the booked total. |
    | Guesty | ✓ | ✓ | ✓ | ✓ | ✓ | Cancels direct and Vrbo bookings; other channel bookings are
    cancelled on the channel. |
    | Beds24 | ✓ | ✓ | ✓ | ✓ | ✓ | Needs the `write:bookings` scope; a multi-room property needs
    `unitId`. |
    | BookingSync | ✓ | ✓ | ✓ | ✓ | ✓ | Needs `bookings_write`; fees and taxes are not itemized; no
    guest email. |
    | Lodgify | ✓ | ✓ | ✓ (declines) | ✓ | ✓ | Cancel declines the booking; single-room bookings. |
    | Smoobu | ✓ | ✓ (no dates) | ✓ | ✓ | ✓ | Dates cannot be changed through Smoobu's API — cancel and
    rebook, or change them in Smoobu. |
    | Hospitable | ✓ | ✓ | ✓ | ✓ (Direct plan) | ✓ | Manual reservations only; needs
    `reservation:write`; adds no fees or taxes. |
    | iGMS | ✓ | ✓ | ✓ | – | ✓ (required) | iGMS direct bookings only; a price is required; no tentative
    holds. |
    | OwnerRez | ✓ | ✓ | – | ✓ | – | No cancel through OwnerRez's API; priced by the property's own
    rates; needs the `full` scope. |

    Every PMS except Cloudbeds refuses group bookings, and every vacation-rental PMS refuses to change
    or cancel a booking that came from a channel (Airbnb, Booking.com, Vrbo…) — that is done on the
    channel.

    **Verification.** Mews and Cloudbeds were run end to end on their vendors' sandboxes. Every other
    PMS is **verified against the vendor's API documentation only** — no live account has been written
    to yet. `capabilities.reservations.verifiedAgainst` says which.

    `X-Account-Id` restricts the listing to one connected account. Returns `403 listing_inactive` when
    the listing is inactive.

    Args:
        x_account_id (str | Unset):  Example: 126.
        body (ReservationQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReservationQuoteResponse]
     """


    kwargs = _get_kwargs(
        body=body,
x_account_id=x_account_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ReservationQuoteRequest,
    x_account_id: str | Unset = UNSET,

) -> Error | ReservationQuoteResponse | None:
    """ Quote a reservation in the PMS

     Prices a stay and checks its availability **in the PMS that manages the listing**, without booking
    anything. It is the same check `POST /v1/reservations` makes before booking when no `totalPrice` is
    sent, so `available: true` with a `total` is what that create would be priced at (dates can still be
    taken in between).

    `available: false` is an answer, not an error: the PMS's reasons are in `restrictions` (minimum
    stay, closed to arrival, taken dates…).

    - A listing **not managed in a PMS** answers `422 pms_not_linked`. Book it directly with `POST
    /v1/reservations`, or price it with `GET /v1/quotes`.
    - A PMS **without a quote API** (Mews, Cloudbeds, iGMS) answers `422 pms_write_unsupported`. You can
    still create the booking; on iGMS a `totalPrice` is required.

    `GET /v1/listings/{id}` → `capabilities.reservations.quote` says whether a listing can be quoted.

    ### Per-PMS limits

    | PMS | create | change | cancel | quote | `totalPrice` | Limits |
    |---|---|---|---|---|---|---|
    | Mews | ✓ | ✓ | ✓ | – | ✓ | — |
    | Cloudbeds | ✓ | ✓ | ✓ | – | – | Books at the rate plan's price; group bookings supported. |
    | Hostaway | ✓ | ✓ | ✓ | ✓ | ✓ | Direct-channel bookings only; a specific unit is refused; a date
    change keeps the booked total. |
    | Guesty | ✓ | ✓ | ✓ | ✓ | ✓ | Cancels direct and Vrbo bookings; other channel bookings are
    cancelled on the channel. |
    | Beds24 | ✓ | ✓ | ✓ | ✓ | ✓ | Needs the `write:bookings` scope; a multi-room property needs
    `unitId`. |
    | BookingSync | ✓ | ✓ | ✓ | ✓ | ✓ | Needs `bookings_write`; fees and taxes are not itemized; no
    guest email. |
    | Lodgify | ✓ | ✓ | ✓ (declines) | ✓ | ✓ | Cancel declines the booking; single-room bookings. |
    | Smoobu | ✓ | ✓ (no dates) | ✓ | ✓ | ✓ | Dates cannot be changed through Smoobu's API — cancel and
    rebook, or change them in Smoobu. |
    | Hospitable | ✓ | ✓ | ✓ | ✓ (Direct plan) | ✓ | Manual reservations only; needs
    `reservation:write`; adds no fees or taxes. |
    | iGMS | ✓ | ✓ | ✓ | – | ✓ (required) | iGMS direct bookings only; a price is required; no tentative
    holds. |
    | OwnerRez | ✓ | ✓ | – | ✓ | – | No cancel through OwnerRez's API; priced by the property's own
    rates; needs the `full` scope. |

    Every PMS except Cloudbeds refuses group bookings, and every vacation-rental PMS refuses to change
    or cancel a booking that came from a channel (Airbnb, Booking.com, Vrbo…) — that is done on the
    channel.

    **Verification.** Mews and Cloudbeds were run end to end on their vendors' sandboxes. Every other
    PMS is **verified against the vendor's API documentation only** — no live account has been written
    to yet. `capabilities.reservations.verifiedAgainst` says which.

    `X-Account-Id` restricts the listing to one connected account. Returns `403 listing_inactive` when
    the listing is inactive.

    Args:
        x_account_id (str | Unset):  Example: 126.
        body (ReservationQuoteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReservationQuoteResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
x_account_id=x_account_id,

    )).parsed
