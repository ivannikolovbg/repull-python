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
    x_account_id: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    if not isinstance(x_account_id, Unset):
        headers["X-Account-Id"] = x_account_id



    

    

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
    x_account_id: str | Unset = UNSET,

) -> Response[Error | ReservationCreateResponse]:
    """ Create a reservation

     Creates a reservation — in the listing's PMS when it has one, otherwise as a direct booking in
    Repull.

    ### Where the booking is made

    - **A listing managed in a connected PMS** (Mews, Cloudbeds, Hostaway, Guesty, Beds24, BookingSync,
    Lodgify, Smoobu, Hospitable, iGMS, OwnerRez): the booking is created **in the PMS first**, then
    recorded in Repull from the PMS's own record, so the next sync lands on the same confirmation code
    and nothing is duplicated. A booking is **never** created only in Repull for such a listing — the
    PMS would keep selling the dates. What the PMS cannot do is refused (`422 pms_write_unsupported`),
    never faked. The PMS checks availability: taken dates answer `409 pms_unavailable`.
    - **Any other listing**: a direct booking made in Repull, with everything that hangs off one — the
    guest, the conversation, the calendar block and the `reservation.created` fan-out that issues the
    door code and starts the messaging automations. Priced by the listing's own rates; **availability is
    NOT checked** (call `GET /v1/availability/{propertyId}` first if that matters).

    `GET /v1/listings/{id}` → `capabilities.reservations` says which applies to a listing and exactly
    what it supports (`create`, `modify`, `cancel`, `quote`, `customPrice`, plus `notes`).

    ### Fields by listing kind

    | Field | PMS listing | Direct-booking listing |
    |---|---|---|
    | `listingId`, `checkIn`, `checkOut`, `guest`, `guestCount`, `adults`, `children` | ✓ | ✓ |
    | `status` | `confirmed` (default) or `tentative` | ✓ |
    | `totalPrice` | ✓ where `capabilities.reservations.customPrice`; otherwise the PMS prices the stay
    | `422 unsupported_field` (priced from the listing's rates) |
    | `notes`, `unitId`, `sendConfirmationEmail` | ✓ | `422 unsupported_field` |
    | `checkInTime`, `checkOutTime`, `currency`, `guestId` | `422 unsupported_field` (the PMS's own
    settings apply) | ✓ |
    | `platform` | `direct` or `website` (`owner` → `422 pms_write_unsupported`; block owner stays in
    the PMS) | `direct`, `website` or `owner` |

    A field a listing cannot take is refused by name, never silently dropped. `platform` never accepts
    `airbnb` / `booking` / `vrbo`: those reservations are owned by the channel and arrive through sync.

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

    ### Idempotency

    **Send `Idempotency-Key`.** A network timeout here is exactly the case it exists for. The key is
    also sent to the PMS as the booking's reference, so even a retry that reaches the PMS again finds
    the booking instead of making a second one (`409 pms_duplicate` with `existing`, or the existing
    booking returned). A completed answer is replayed with `Idempotency-Status: cached` and the PMS is
    not called again. `502 pms_error` (the PMS could not be reached) is NOT stored — retry with the same
    key. `502 reservation_created_in_pms_only` IS stored, unlike every other 5xx: the booking exists in
    the PMS and arrives with the next sync, so a retry replays that answer rather than booking twice.

    ### Partial success

    When the PMS created the booking but a follow-up step did not apply (for example the notes, or a
    tentative state), the response is still `201`, with `pms.partial: true` and the steps in
    `pms.failedSections`. The booking exists — do not create it again.

    `X-Account-Id` restricts the listing to one connected account. Returns `403 listing_inactive` when
    the listing is inactive.

    Args:
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        x_account_id (str | Unset):  Example: 126.
        body (ReservationCreateRequest): Which fields a listing takes depends on whether it is
            managed in a PMS — see the operation description and `GET /v1/listings/{id}` →
            `capabilities.reservations`. A field the listing cannot take is refused by name (`422
            unsupported_field`), never dropped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReservationCreateResponse]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,
x_account_id=x_account_id,

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
    x_account_id: str | Unset = UNSET,

) -> Error | ReservationCreateResponse | None:
    """ Create a reservation

     Creates a reservation — in the listing's PMS when it has one, otherwise as a direct booking in
    Repull.

    ### Where the booking is made

    - **A listing managed in a connected PMS** (Mews, Cloudbeds, Hostaway, Guesty, Beds24, BookingSync,
    Lodgify, Smoobu, Hospitable, iGMS, OwnerRez): the booking is created **in the PMS first**, then
    recorded in Repull from the PMS's own record, so the next sync lands on the same confirmation code
    and nothing is duplicated. A booking is **never** created only in Repull for such a listing — the
    PMS would keep selling the dates. What the PMS cannot do is refused (`422 pms_write_unsupported`),
    never faked. The PMS checks availability: taken dates answer `409 pms_unavailable`.
    - **Any other listing**: a direct booking made in Repull, with everything that hangs off one — the
    guest, the conversation, the calendar block and the `reservation.created` fan-out that issues the
    door code and starts the messaging automations. Priced by the listing's own rates; **availability is
    NOT checked** (call `GET /v1/availability/{propertyId}` first if that matters).

    `GET /v1/listings/{id}` → `capabilities.reservations` says which applies to a listing and exactly
    what it supports (`create`, `modify`, `cancel`, `quote`, `customPrice`, plus `notes`).

    ### Fields by listing kind

    | Field | PMS listing | Direct-booking listing |
    |---|---|---|
    | `listingId`, `checkIn`, `checkOut`, `guest`, `guestCount`, `adults`, `children` | ✓ | ✓ |
    | `status` | `confirmed` (default) or `tentative` | ✓ |
    | `totalPrice` | ✓ where `capabilities.reservations.customPrice`; otherwise the PMS prices the stay
    | `422 unsupported_field` (priced from the listing's rates) |
    | `notes`, `unitId`, `sendConfirmationEmail` | ✓ | `422 unsupported_field` |
    | `checkInTime`, `checkOutTime`, `currency`, `guestId` | `422 unsupported_field` (the PMS's own
    settings apply) | ✓ |
    | `platform` | `direct` or `website` (`owner` → `422 pms_write_unsupported`; block owner stays in
    the PMS) | `direct`, `website` or `owner` |

    A field a listing cannot take is refused by name, never silently dropped. `platform` never accepts
    `airbnb` / `booking` / `vrbo`: those reservations are owned by the channel and arrive through sync.

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

    ### Idempotency

    **Send `Idempotency-Key`.** A network timeout here is exactly the case it exists for. The key is
    also sent to the PMS as the booking's reference, so even a retry that reaches the PMS again finds
    the booking instead of making a second one (`409 pms_duplicate` with `existing`, or the existing
    booking returned). A completed answer is replayed with `Idempotency-Status: cached` and the PMS is
    not called again. `502 pms_error` (the PMS could not be reached) is NOT stored — retry with the same
    key. `502 reservation_created_in_pms_only` IS stored, unlike every other 5xx: the booking exists in
    the PMS and arrives with the next sync, so a retry replays that answer rather than booking twice.

    ### Partial success

    When the PMS created the booking but a follow-up step did not apply (for example the notes, or a
    tentative state), the response is still `201`, with `pms.partial: true` and the steps in
    `pms.failedSections`. The booking exists — do not create it again.

    `X-Account-Id` restricts the listing to one connected account. Returns `403 listing_inactive` when
    the listing is inactive.

    Args:
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        x_account_id (str | Unset):  Example: 126.
        body (ReservationCreateRequest): Which fields a listing takes depends on whether it is
            managed in a PMS — see the operation description and `GET /v1/listings/{id}` →
            `capabilities.reservations`. A field the listing cannot take is refused by name (`422
            unsupported_field`), never dropped.

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
x_account_id=x_account_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReservationCreateRequest,
    idempotency_key: str | Unset = UNSET,
    x_account_id: str | Unset = UNSET,

) -> Response[Error | ReservationCreateResponse]:
    """ Create a reservation

     Creates a reservation — in the listing's PMS when it has one, otherwise as a direct booking in
    Repull.

    ### Where the booking is made

    - **A listing managed in a connected PMS** (Mews, Cloudbeds, Hostaway, Guesty, Beds24, BookingSync,
    Lodgify, Smoobu, Hospitable, iGMS, OwnerRez): the booking is created **in the PMS first**, then
    recorded in Repull from the PMS's own record, so the next sync lands on the same confirmation code
    and nothing is duplicated. A booking is **never** created only in Repull for such a listing — the
    PMS would keep selling the dates. What the PMS cannot do is refused (`422 pms_write_unsupported`),
    never faked. The PMS checks availability: taken dates answer `409 pms_unavailable`.
    - **Any other listing**: a direct booking made in Repull, with everything that hangs off one — the
    guest, the conversation, the calendar block and the `reservation.created` fan-out that issues the
    door code and starts the messaging automations. Priced by the listing's own rates; **availability is
    NOT checked** (call `GET /v1/availability/{propertyId}` first if that matters).

    `GET /v1/listings/{id}` → `capabilities.reservations` says which applies to a listing and exactly
    what it supports (`create`, `modify`, `cancel`, `quote`, `customPrice`, plus `notes`).

    ### Fields by listing kind

    | Field | PMS listing | Direct-booking listing |
    |---|---|---|
    | `listingId`, `checkIn`, `checkOut`, `guest`, `guestCount`, `adults`, `children` | ✓ | ✓ |
    | `status` | `confirmed` (default) or `tentative` | ✓ |
    | `totalPrice` | ✓ where `capabilities.reservations.customPrice`; otherwise the PMS prices the stay
    | `422 unsupported_field` (priced from the listing's rates) |
    | `notes`, `unitId`, `sendConfirmationEmail` | ✓ | `422 unsupported_field` |
    | `checkInTime`, `checkOutTime`, `currency`, `guestId` | `422 unsupported_field` (the PMS's own
    settings apply) | ✓ |
    | `platform` | `direct` or `website` (`owner` → `422 pms_write_unsupported`; block owner stays in
    the PMS) | `direct`, `website` or `owner` |

    A field a listing cannot take is refused by name, never silently dropped. `platform` never accepts
    `airbnb` / `booking` / `vrbo`: those reservations are owned by the channel and arrive through sync.

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

    ### Idempotency

    **Send `Idempotency-Key`.** A network timeout here is exactly the case it exists for. The key is
    also sent to the PMS as the booking's reference, so even a retry that reaches the PMS again finds
    the booking instead of making a second one (`409 pms_duplicate` with `existing`, or the existing
    booking returned). A completed answer is replayed with `Idempotency-Status: cached` and the PMS is
    not called again. `502 pms_error` (the PMS could not be reached) is NOT stored — retry with the same
    key. `502 reservation_created_in_pms_only` IS stored, unlike every other 5xx: the booking exists in
    the PMS and arrives with the next sync, so a retry replays that answer rather than booking twice.

    ### Partial success

    When the PMS created the booking but a follow-up step did not apply (for example the notes, or a
    tentative state), the response is still `201`, with `pms.partial: true` and the steps in
    `pms.failedSections`. The booking exists — do not create it again.

    `X-Account-Id` restricts the listing to one connected account. Returns `403 listing_inactive` when
    the listing is inactive.

    Args:
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        x_account_id (str | Unset):  Example: 126.
        body (ReservationCreateRequest): Which fields a listing takes depends on whether it is
            managed in a PMS — see the operation description and `GET /v1/listings/{id}` →
            `capabilities.reservations`. A field the listing cannot take is refused by name (`422
            unsupported_field`), never dropped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReservationCreateResponse]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,
x_account_id=x_account_id,

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
    x_account_id: str | Unset = UNSET,

) -> Error | ReservationCreateResponse | None:
    """ Create a reservation

     Creates a reservation — in the listing's PMS when it has one, otherwise as a direct booking in
    Repull.

    ### Where the booking is made

    - **A listing managed in a connected PMS** (Mews, Cloudbeds, Hostaway, Guesty, Beds24, BookingSync,
    Lodgify, Smoobu, Hospitable, iGMS, OwnerRez): the booking is created **in the PMS first**, then
    recorded in Repull from the PMS's own record, so the next sync lands on the same confirmation code
    and nothing is duplicated. A booking is **never** created only in Repull for such a listing — the
    PMS would keep selling the dates. What the PMS cannot do is refused (`422 pms_write_unsupported`),
    never faked. The PMS checks availability: taken dates answer `409 pms_unavailable`.
    - **Any other listing**: a direct booking made in Repull, with everything that hangs off one — the
    guest, the conversation, the calendar block and the `reservation.created` fan-out that issues the
    door code and starts the messaging automations. Priced by the listing's own rates; **availability is
    NOT checked** (call `GET /v1/availability/{propertyId}` first if that matters).

    `GET /v1/listings/{id}` → `capabilities.reservations` says which applies to a listing and exactly
    what it supports (`create`, `modify`, `cancel`, `quote`, `customPrice`, plus `notes`).

    ### Fields by listing kind

    | Field | PMS listing | Direct-booking listing |
    |---|---|---|
    | `listingId`, `checkIn`, `checkOut`, `guest`, `guestCount`, `adults`, `children` | ✓ | ✓ |
    | `status` | `confirmed` (default) or `tentative` | ✓ |
    | `totalPrice` | ✓ where `capabilities.reservations.customPrice`; otherwise the PMS prices the stay
    | `422 unsupported_field` (priced from the listing's rates) |
    | `notes`, `unitId`, `sendConfirmationEmail` | ✓ | `422 unsupported_field` |
    | `checkInTime`, `checkOutTime`, `currency`, `guestId` | `422 unsupported_field` (the PMS's own
    settings apply) | ✓ |
    | `platform` | `direct` or `website` (`owner` → `422 pms_write_unsupported`; block owner stays in
    the PMS) | `direct`, `website` or `owner` |

    A field a listing cannot take is refused by name, never silently dropped. `platform` never accepts
    `airbnb` / `booking` / `vrbo`: those reservations are owned by the channel and arrive through sync.

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

    ### Idempotency

    **Send `Idempotency-Key`.** A network timeout here is exactly the case it exists for. The key is
    also sent to the PMS as the booking's reference, so even a retry that reaches the PMS again finds
    the booking instead of making a second one (`409 pms_duplicate` with `existing`, or the existing
    booking returned). A completed answer is replayed with `Idempotency-Status: cached` and the PMS is
    not called again. `502 pms_error` (the PMS could not be reached) is NOT stored — retry with the same
    key. `502 reservation_created_in_pms_only` IS stored, unlike every other 5xx: the booking exists in
    the PMS and arrives with the next sync, so a retry replays that answer rather than booking twice.

    ### Partial success

    When the PMS created the booking but a follow-up step did not apply (for example the notes, or a
    tentative state), the response is still `201`, with `pms.partial: true` and the steps in
    `pms.failedSections`. The booking exists — do not create it again.

    `X-Account-Id` restricts the listing to one connected account. Returns `403 listing_inactive` when
    the listing is inactive.

    Args:
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        x_account_id (str | Unset):  Example: 126.
        body (ReservationCreateRequest): Which fields a listing takes depends on whether it is
            managed in a PMS — see the operation description and `GET /v1/listings/{id}` →
            `capabilities.reservations`. A field the listing cannot take is refused by name (`422
            unsupported_field`), never dropped.

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
x_account_id=x_account_id,

    )).parsed
