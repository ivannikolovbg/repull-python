from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.map_booking_room_request import MapBookingRoomRequest
from ...models.map_booking_room_response import MapBookingRoomResponse
from typing import cast



def _get_kwargs(
    *,
    body: MapBookingRoomRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/booking/listings/map",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | MapBookingRoomResponse | None:
    if response.status_code == 200:
        response_200 = MapBookingRoomResponse.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | MapBookingRoomResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MapBookingRoomRequest,

) -> Response[Error | MapBookingRoomResponse]:
    """ Map a Booking.com room to a Repull listing

     Link a Booking.com room to a canonical Repull listing — the API-key equivalent of the room mapping
    the hosted Connect flow performs, and the counterpart of `POST /v1/channels/airbnb/listings/map`.

    Discover `roomBookingId` with `GET /v1/channels/booking/properties/{id}/rooms`, which returns every
    room of a property with the `roomId` this route takes.

    Booking.com attaches at the ROOM level: a property is a building and its rooms are what a guest
    books, so each room maps to one listing. Pass `listingId: null` to unmap a room and remove its
    channel link.

    The room mapping and its channel link are repointed together in one transaction, so a link can never
    outlive the mapping it describes — a stale link keeps routing that room's reservations to the
    previous listing. Re-sending a mapping that is already in place writes nothing (`alreadyMapped:
    true`).

    **The property's reservations are pulled as part of the call.** Once the room is mapped, every
    active reservation Booking.com holds for the property is imported and attached to its listing —
    `reservationsImported` says how many were processed. One already present is left as it is, so re-
    sending never duplicates. You do not need a follow-up call: reservations that arrived before the
    room was mapped are never picked up by the regular sync, so this is the moment they are brought in.
    It runs on every successful map, including a re-send, so re-sending retries an import that did not
    run. If the import cannot run, the mapping still stands and `reservationsImported` is `null`. A
    property with a long booking history can take tens of seconds. Unmapping pulls nothing.

    Unlike the Airbnb route, there is no conflict when the target listing already carries another
    Booking.com room: one listing served by several rooms is a normal arrangement and is not refused.

    Scope is enforced on both sides against your workspace — the room's property and the target listing.
    A room or listing belonging to another workspace returns the same 404 as one that does not exist.

    Returns `403 listing_inactive` when the target listing, or the listing the room is mapped to now, is
    inactive; nothing is changed.

    Args:
        body (MapBookingRoomRequest): Body for `POST /v1/channels/booking/listings/map`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MapBookingRoomResponse]
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
    body: MapBookingRoomRequest,

) -> Error | MapBookingRoomResponse | None:
    """ Map a Booking.com room to a Repull listing

     Link a Booking.com room to a canonical Repull listing — the API-key equivalent of the room mapping
    the hosted Connect flow performs, and the counterpart of `POST /v1/channels/airbnb/listings/map`.

    Discover `roomBookingId` with `GET /v1/channels/booking/properties/{id}/rooms`, which returns every
    room of a property with the `roomId` this route takes.

    Booking.com attaches at the ROOM level: a property is a building and its rooms are what a guest
    books, so each room maps to one listing. Pass `listingId: null` to unmap a room and remove its
    channel link.

    The room mapping and its channel link are repointed together in one transaction, so a link can never
    outlive the mapping it describes — a stale link keeps routing that room's reservations to the
    previous listing. Re-sending a mapping that is already in place writes nothing (`alreadyMapped:
    true`).

    **The property's reservations are pulled as part of the call.** Once the room is mapped, every
    active reservation Booking.com holds for the property is imported and attached to its listing —
    `reservationsImported` says how many were processed. One already present is left as it is, so re-
    sending never duplicates. You do not need a follow-up call: reservations that arrived before the
    room was mapped are never picked up by the regular sync, so this is the moment they are brought in.
    It runs on every successful map, including a re-send, so re-sending retries an import that did not
    run. If the import cannot run, the mapping still stands and `reservationsImported` is `null`. A
    property with a long booking history can take tens of seconds. Unmapping pulls nothing.

    Unlike the Airbnb route, there is no conflict when the target listing already carries another
    Booking.com room: one listing served by several rooms is a normal arrangement and is not refused.

    Scope is enforced on both sides against your workspace — the room's property and the target listing.
    A room or listing belonging to another workspace returns the same 404 as one that does not exist.

    Returns `403 listing_inactive` when the target listing, or the listing the room is mapped to now, is
    inactive; nothing is changed.

    Args:
        body (MapBookingRoomRequest): Body for `POST /v1/channels/booking/listings/map`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MapBookingRoomResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MapBookingRoomRequest,

) -> Response[Error | MapBookingRoomResponse]:
    """ Map a Booking.com room to a Repull listing

     Link a Booking.com room to a canonical Repull listing — the API-key equivalent of the room mapping
    the hosted Connect flow performs, and the counterpart of `POST /v1/channels/airbnb/listings/map`.

    Discover `roomBookingId` with `GET /v1/channels/booking/properties/{id}/rooms`, which returns every
    room of a property with the `roomId` this route takes.

    Booking.com attaches at the ROOM level: a property is a building and its rooms are what a guest
    books, so each room maps to one listing. Pass `listingId: null` to unmap a room and remove its
    channel link.

    The room mapping and its channel link are repointed together in one transaction, so a link can never
    outlive the mapping it describes — a stale link keeps routing that room's reservations to the
    previous listing. Re-sending a mapping that is already in place writes nothing (`alreadyMapped:
    true`).

    **The property's reservations are pulled as part of the call.** Once the room is mapped, every
    active reservation Booking.com holds for the property is imported and attached to its listing —
    `reservationsImported` says how many were processed. One already present is left as it is, so re-
    sending never duplicates. You do not need a follow-up call: reservations that arrived before the
    room was mapped are never picked up by the regular sync, so this is the moment they are brought in.
    It runs on every successful map, including a re-send, so re-sending retries an import that did not
    run. If the import cannot run, the mapping still stands and `reservationsImported` is `null`. A
    property with a long booking history can take tens of seconds. Unmapping pulls nothing.

    Unlike the Airbnb route, there is no conflict when the target listing already carries another
    Booking.com room: one listing served by several rooms is a normal arrangement and is not refused.

    Scope is enforced on both sides against your workspace — the room's property and the target listing.
    A room or listing belonging to another workspace returns the same 404 as one that does not exist.

    Returns `403 listing_inactive` when the target listing, or the listing the room is mapped to now, is
    inactive; nothing is changed.

    Args:
        body (MapBookingRoomRequest): Body for `POST /v1/channels/booking/listings/map`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MapBookingRoomResponse]
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
    body: MapBookingRoomRequest,

) -> Error | MapBookingRoomResponse | None:
    """ Map a Booking.com room to a Repull listing

     Link a Booking.com room to a canonical Repull listing — the API-key equivalent of the room mapping
    the hosted Connect flow performs, and the counterpart of `POST /v1/channels/airbnb/listings/map`.

    Discover `roomBookingId` with `GET /v1/channels/booking/properties/{id}/rooms`, which returns every
    room of a property with the `roomId` this route takes.

    Booking.com attaches at the ROOM level: a property is a building and its rooms are what a guest
    books, so each room maps to one listing. Pass `listingId: null` to unmap a room and remove its
    channel link.

    The room mapping and its channel link are repointed together in one transaction, so a link can never
    outlive the mapping it describes — a stale link keeps routing that room's reservations to the
    previous listing. Re-sending a mapping that is already in place writes nothing (`alreadyMapped:
    true`).

    **The property's reservations are pulled as part of the call.** Once the room is mapped, every
    active reservation Booking.com holds for the property is imported and attached to its listing —
    `reservationsImported` says how many were processed. One already present is left as it is, so re-
    sending never duplicates. You do not need a follow-up call: reservations that arrived before the
    room was mapped are never picked up by the regular sync, so this is the moment they are brought in.
    It runs on every successful map, including a re-send, so re-sending retries an import that did not
    run. If the import cannot run, the mapping still stands and `reservationsImported` is `null`. A
    property with a long booking history can take tens of seconds. Unmapping pulls nothing.

    Unlike the Airbnb route, there is no conflict when the target listing already carries another
    Booking.com room: one listing served by several rooms is a normal arrangement and is not refused.

    Scope is enforced on both sides against your workspace — the room's property and the target listing.
    A room or listing belonging to another workspace returns the same 404 as one that does not exist.

    Returns `403 listing_inactive` when the target listing, or the listing the room is mapped to now, is
    inactive; nothing is changed.

    Args:
        body (MapBookingRoomRequest): Body for `POST /v1/channels/booking/listings/map`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MapBookingRoomResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
