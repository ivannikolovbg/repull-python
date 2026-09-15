from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.reservation_update_request import ReservationUpdateRequest
from ...models.reservation_update_response import ReservationUpdateResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ReservationUpdateRequest,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/reservations/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ReservationUpdateResponse | None:
    if response.status_code == 200:
        response_200 = ReservationUpdateResponse.from_dict(response.json())



        return response_200

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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ReservationUpdateResponse]:
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
    body: ReservationUpdateRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | ReservationUpdateResponse]:
    """ Update a reservation

     Changes the dates, the occupancy, or the unit. Drives the same command path the dashboard does, so
    the side effects come with it: the change audit is appended, bound task due dates re-sync, the old
    calendar dates unblock and the new ones block, the conversation's cached listing is invalidated, and
    `reservation.updated` fires — which is what revokes and re-issues the door code.

    Supply at least one field; an empty body returns 422 rather than a 200 that changed nothing.

    **Moving and re-dating in one call is one operation.** Send `listingId` together with
    `checkIn`/`checkOut` and it is applied as a single move, so the access code is re-issued once rather
    than twice.

    ### Fields this endpoint deliberately does NOT accept

    Each is rejected by name with the reason, never accepted and ignored:

    | Field | Why |
    |---|---|
    | `guest` / `guestDetails` | Guest name, email and phone live on the guest record. The underlying
    command has no branch for them, so accepting them would return a success that changed nothing. |
    | `pricing` / `totalPrice` / `currency` | Repricing writes the price breakdown, the pricing row and
    a pricing-history entry. It belongs to its own endpoint. |
    | `status` | Not a field. Cancelling, confirming and checking out are separate operations with
    materially different side effects — cancellation issues a credit refund and revokes access codes. |
    | `platform` | Immutable: it records where the booking actually originated. |
    | `notes` | `internal_notes` is an append-only audit trail the system writes on every change. |

    **Availability is NOT checked.** A date change that overlaps another booking will be written. Call
    `GET /v1/availability/{propertyId}` first if that matters.

    Returns `403 listing_inactive` when the reservation is on an inactive listing, or when a `listingId`
    move targets one; nothing is changed.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ReservationUpdateRequest): At least one field is required. Guest identity, pricing,
            `status`, `platform` and notes are rejected by name — see the operation description for
            why each is excluded.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReservationUpdateResponse]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
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
    body: ReservationUpdateRequest,
    idempotency_key: str | Unset = UNSET,

) -> Error | ReservationUpdateResponse | None:
    """ Update a reservation

     Changes the dates, the occupancy, or the unit. Drives the same command path the dashboard does, so
    the side effects come with it: the change audit is appended, bound task due dates re-sync, the old
    calendar dates unblock and the new ones block, the conversation's cached listing is invalidated, and
    `reservation.updated` fires — which is what revokes and re-issues the door code.

    Supply at least one field; an empty body returns 422 rather than a 200 that changed nothing.

    **Moving and re-dating in one call is one operation.** Send `listingId` together with
    `checkIn`/`checkOut` and it is applied as a single move, so the access code is re-issued once rather
    than twice.

    ### Fields this endpoint deliberately does NOT accept

    Each is rejected by name with the reason, never accepted and ignored:

    | Field | Why |
    |---|---|
    | `guest` / `guestDetails` | Guest name, email and phone live on the guest record. The underlying
    command has no branch for them, so accepting them would return a success that changed nothing. |
    | `pricing` / `totalPrice` / `currency` | Repricing writes the price breakdown, the pricing row and
    a pricing-history entry. It belongs to its own endpoint. |
    | `status` | Not a field. Cancelling, confirming and checking out are separate operations with
    materially different side effects — cancellation issues a credit refund and revokes access codes. |
    | `platform` | Immutable: it records where the booking actually originated. |
    | `notes` | `internal_notes` is an append-only audit trail the system writes on every change. |

    **Availability is NOT checked.** A date change that overlaps another booking will be written. Call
    `GET /v1/availability/{propertyId}` first if that matters.

    Returns `403 listing_inactive` when the reservation is on an inactive listing, or when a `listingId`
    move targets one; nothing is changed.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ReservationUpdateRequest): At least one field is required. Guest identity, pricing,
            `status`, `platform` and notes are rejected by name — see the operation description for
            why each is excluded.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReservationUpdateResponse
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ReservationUpdateRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | ReservationUpdateResponse]:
    """ Update a reservation

     Changes the dates, the occupancy, or the unit. Drives the same command path the dashboard does, so
    the side effects come with it: the change audit is appended, bound task due dates re-sync, the old
    calendar dates unblock and the new ones block, the conversation's cached listing is invalidated, and
    `reservation.updated` fires — which is what revokes and re-issues the door code.

    Supply at least one field; an empty body returns 422 rather than a 200 that changed nothing.

    **Moving and re-dating in one call is one operation.** Send `listingId` together with
    `checkIn`/`checkOut` and it is applied as a single move, so the access code is re-issued once rather
    than twice.

    ### Fields this endpoint deliberately does NOT accept

    Each is rejected by name with the reason, never accepted and ignored:

    | Field | Why |
    |---|---|
    | `guest` / `guestDetails` | Guest name, email and phone live on the guest record. The underlying
    command has no branch for them, so accepting them would return a success that changed nothing. |
    | `pricing` / `totalPrice` / `currency` | Repricing writes the price breakdown, the pricing row and
    a pricing-history entry. It belongs to its own endpoint. |
    | `status` | Not a field. Cancelling, confirming and checking out are separate operations with
    materially different side effects — cancellation issues a credit refund and revokes access codes. |
    | `platform` | Immutable: it records where the booking actually originated. |
    | `notes` | `internal_notes` is an append-only audit trail the system writes on every change. |

    **Availability is NOT checked.** A date change that overlaps another booking will be written. Call
    `GET /v1/availability/{propertyId}` first if that matters.

    Returns `403 listing_inactive` when the reservation is on an inactive listing, or when a `listingId`
    move targets one; nothing is changed.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ReservationUpdateRequest): At least one field is required. Guest identity, pricing,
            `status`, `platform` and notes are rejected by name — see the operation description for
            why each is excluded.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReservationUpdateResponse]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
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
    body: ReservationUpdateRequest,
    idempotency_key: str | Unset = UNSET,

) -> Error | ReservationUpdateResponse | None:
    """ Update a reservation

     Changes the dates, the occupancy, or the unit. Drives the same command path the dashboard does, so
    the side effects come with it: the change audit is appended, bound task due dates re-sync, the old
    calendar dates unblock and the new ones block, the conversation's cached listing is invalidated, and
    `reservation.updated` fires — which is what revokes and re-issues the door code.

    Supply at least one field; an empty body returns 422 rather than a 200 that changed nothing.

    **Moving and re-dating in one call is one operation.** Send `listingId` together with
    `checkIn`/`checkOut` and it is applied as a single move, so the access code is re-issued once rather
    than twice.

    ### Fields this endpoint deliberately does NOT accept

    Each is rejected by name with the reason, never accepted and ignored:

    | Field | Why |
    |---|---|
    | `guest` / `guestDetails` | Guest name, email and phone live on the guest record. The underlying
    command has no branch for them, so accepting them would return a success that changed nothing. |
    | `pricing` / `totalPrice` / `currency` | Repricing writes the price breakdown, the pricing row and
    a pricing-history entry. It belongs to its own endpoint. |
    | `status` | Not a field. Cancelling, confirming and checking out are separate operations with
    materially different side effects — cancellation issues a credit refund and revokes access codes. |
    | `platform` | Immutable: it records where the booking actually originated. |
    | `notes` | `internal_notes` is an append-only audit trail the system writes on every change. |

    **Availability is NOT checked.** A date change that overlaps another booking will be written. Call
    `GET /v1/availability/{propertyId}` first if that matters.

    Returns `403 listing_inactive` when the reservation is on an inactive listing, or when a `listingId`
    move targets one; nothing is changed.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ReservationUpdateRequest): At least one field is required. Guest identity, pricing,
            `status`, `platform` and notes are rejected by name — see the operation description for
            why each is excluded.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReservationUpdateResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
