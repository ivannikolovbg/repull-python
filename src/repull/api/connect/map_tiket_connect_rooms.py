from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.map_tiket_connect_rooms_body import MapTiketConnectRoomsBody
from ...models.tiket_connect_map_rooms_response import TiketConnectMapRoomsResponse
from typing import cast



def _get_kwargs(
    *,
    body: MapTiketConnectRoomsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/tiket/map-rooms",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TiketConnectMapRoomsResponse | None:
    if response.status_code == 200:
        response_200 = TiketConnectMapRoomsResponse.from_dict(response.json())



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

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | TiketConnectMapRoomsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MapTiketConnectRoomsBody,

) -> Response[Error | TiketConnectMapRoomsResponse]:
    r""" Map tiket.com room types to listings in a Connect session

     Called by the hosted Connect page and authorized by the Connect session id, not an API key. Start
    the session with `POST /v1/connect` (`allowedProviders: [\"tiket\"]`) and send the host to its
    `url`.

    Submits the host's room mapping for the property claimed in the session and completes the session.
    Each mapping is `{ roomId, listingId }` (`listingId: null` leaves the room unmapped) or `{ roomId,
    create: true }`, which creates a listing from the room with tiket.com's calendar. Bookings tiket.com
    delivered before the rooms were mapped are recorded (`replayedReservations`). Same flow as `POST
    /v1/connect/booking/map-rooms`.

    Args:
        body (MapTiketConnectRoomsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketConnectMapRoomsResponse]
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
    body: MapTiketConnectRoomsBody,

) -> Error | TiketConnectMapRoomsResponse | None:
    r""" Map tiket.com room types to listings in a Connect session

     Called by the hosted Connect page and authorized by the Connect session id, not an API key. Start
    the session with `POST /v1/connect` (`allowedProviders: [\"tiket\"]`) and send the host to its
    `url`.

    Submits the host's room mapping for the property claimed in the session and completes the session.
    Each mapping is `{ roomId, listingId }` (`listingId: null` leaves the room unmapped) or `{ roomId,
    create: true }`, which creates a listing from the room with tiket.com's calendar. Bookings tiket.com
    delivered before the rooms were mapped are recorded (`replayedReservations`). Same flow as `POST
    /v1/connect/booking/map-rooms`.

    Args:
        body (MapTiketConnectRoomsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketConnectMapRoomsResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MapTiketConnectRoomsBody,

) -> Response[Error | TiketConnectMapRoomsResponse]:
    r""" Map tiket.com room types to listings in a Connect session

     Called by the hosted Connect page and authorized by the Connect session id, not an API key. Start
    the session with `POST /v1/connect` (`allowedProviders: [\"tiket\"]`) and send the host to its
    `url`.

    Submits the host's room mapping for the property claimed in the session and completes the session.
    Each mapping is `{ roomId, listingId }` (`listingId: null` leaves the room unmapped) or `{ roomId,
    create: true }`, which creates a listing from the room with tiket.com's calendar. Bookings tiket.com
    delivered before the rooms were mapped are recorded (`replayedReservations`). Same flow as `POST
    /v1/connect/booking/map-rooms`.

    Args:
        body (MapTiketConnectRoomsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketConnectMapRoomsResponse]
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
    body: MapTiketConnectRoomsBody,

) -> Error | TiketConnectMapRoomsResponse | None:
    r""" Map tiket.com room types to listings in a Connect session

     Called by the hosted Connect page and authorized by the Connect session id, not an API key. Start
    the session with `POST /v1/connect` (`allowedProviders: [\"tiket\"]`) and send the host to its
    `url`.

    Submits the host's room mapping for the property claimed in the session and completes the session.
    Each mapping is `{ roomId, listingId }` (`listingId: null` leaves the room unmapped) or `{ roomId,
    create: true }`, which creates a listing from the room with tiket.com's calendar. Bookings tiket.com
    delivered before the rooms were mapped are recorded (`replayedReservations`). Same flow as `POST
    /v1/connect/booking/map-rooms`.

    Args:
        body (MapTiketConnectRoomsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketConnectMapRoomsResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
