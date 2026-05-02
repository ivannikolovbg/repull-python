from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.map_connect_booking_rooms_request import MapConnectBookingRoomsRequest
from ...models.map_connect_booking_rooms_response import MapConnectBookingRoomsResponse
from typing import cast



def _get_kwargs(
    *,
    body: MapConnectBookingRoomsRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/booking/map-rooms",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | MapConnectBookingRoomsResponse | None:
    if response.status_code == 200:
        response_200 = MapConnectBookingRoomsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 410:
        response_410 = Error.from_dict(response.json())



        return response_410

    if response.status_code == 425:
        response_425 = Error.from_dict(response.json())



        return response_425

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | MapConnectBookingRoomsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MapConnectBookingRoomsRequest,

) -> Response[Error | MapConnectBookingRoomsResponse]:
    """ Submit room→listing mappings for a Booking.com Connect session

     Submits the customer's room→listing mapping choices in one transaction. For each mapping, updates
    `listings_booking_rooms.listing_id` and replaces the corresponding `listing_platform_links` row.
    Pass `listingId: null` to explicitly unmap a room.

    On success the Connect session is marked `completed` and the hosted picker page emits a
    `repull:connect:completed` postMessage to the embedding window.

    No API key required — the `sessionId` in the body is the capability token. Each mapping's `roomId`
    must belong to the customer's claimed hotel; mismatched IDs are rejected with 403.

    Args:
        body (MapConnectBookingRoomsRequest): Body for `POST /v1/connect/booking/map-rooms`.
            Submits all room→listing assignments in one transaction; on success the Connect session is
            marked `completed`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MapConnectBookingRoomsResponse]
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
    body: MapConnectBookingRoomsRequest,

) -> Error | MapConnectBookingRoomsResponse | None:
    """ Submit room→listing mappings for a Booking.com Connect session

     Submits the customer's room→listing mapping choices in one transaction. For each mapping, updates
    `listings_booking_rooms.listing_id` and replaces the corresponding `listing_platform_links` row.
    Pass `listingId: null` to explicitly unmap a room.

    On success the Connect session is marked `completed` and the hosted picker page emits a
    `repull:connect:completed` postMessage to the embedding window.

    No API key required — the `sessionId` in the body is the capability token. Each mapping's `roomId`
    must belong to the customer's claimed hotel; mismatched IDs are rejected with 403.

    Args:
        body (MapConnectBookingRoomsRequest): Body for `POST /v1/connect/booking/map-rooms`.
            Submits all room→listing assignments in one transaction; on success the Connect session is
            marked `completed`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MapConnectBookingRoomsResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MapConnectBookingRoomsRequest,

) -> Response[Error | MapConnectBookingRoomsResponse]:
    """ Submit room→listing mappings for a Booking.com Connect session

     Submits the customer's room→listing mapping choices in one transaction. For each mapping, updates
    `listings_booking_rooms.listing_id` and replaces the corresponding `listing_platform_links` row.
    Pass `listingId: null` to explicitly unmap a room.

    On success the Connect session is marked `completed` and the hosted picker page emits a
    `repull:connect:completed` postMessage to the embedding window.

    No API key required — the `sessionId` in the body is the capability token. Each mapping's `roomId`
    must belong to the customer's claimed hotel; mismatched IDs are rejected with 403.

    Args:
        body (MapConnectBookingRoomsRequest): Body for `POST /v1/connect/booking/map-rooms`.
            Submits all room→listing assignments in one transaction; on success the Connect session is
            marked `completed`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MapConnectBookingRoomsResponse]
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
    body: MapConnectBookingRoomsRequest,

) -> Error | MapConnectBookingRoomsResponse | None:
    """ Submit room→listing mappings for a Booking.com Connect session

     Submits the customer's room→listing mapping choices in one transaction. For each mapping, updates
    `listings_booking_rooms.listing_id` and replaces the corresponding `listing_platform_links` row.
    Pass `listingId: null` to explicitly unmap a room.

    On success the Connect session is marked `completed` and the hosted picker page emits a
    `repull:connect:completed` postMessage to the embedding window.

    No API key required — the `sessionId` in the body is the capability token. Each mapping's `roomId`
    must belong to the customer's claimed hotel; mismatched IDs are rejected with 403.

    Args:
        body (MapConnectBookingRoomsRequest): Body for `POST /v1/connect/booking/map-rooms`.
            Submits all room→listing assignments in one transaction; on success the Connect session is
            marked `completed`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MapConnectBookingRoomsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
