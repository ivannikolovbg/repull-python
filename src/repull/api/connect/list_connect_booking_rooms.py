from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_connect_rooms_response import BookingConnectRoomsResponse
from ...models.error import Error
from typing import cast



def _get_kwargs(
    *,
    session_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["sessionId"] = session_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connect/booking/rooms",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BookingConnectRoomsResponse | Error | None:
    if response.status_code == 200:
        response_200 = BookingConnectRoomsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BookingConnectRoomsResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    session_id: str,

) -> Response[BookingConnectRoomsResponse | Error]:
    """ List Booking.com rooms imported for a Connect session

     Returns the rooms imported from the Booking.com hotel claimed in this Connect session, plus the
    customer's listing options for the mapping dropdowns. Hosted-picker pages poll this endpoint every
    ~2s after `verifyBookingHotel` succeeds; once rooms appear the page transitions to the mapping UI.

    No API key required — the `sessionId` query param is the capability token.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingConnectRoomsResponse | Error]
     """


    kwargs = _get_kwargs(
        session_id=session_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    session_id: str,

) -> BookingConnectRoomsResponse | Error | None:
    """ List Booking.com rooms imported for a Connect session

     Returns the rooms imported from the Booking.com hotel claimed in this Connect session, plus the
    customer's listing options for the mapping dropdowns. Hosted-picker pages poll this endpoint every
    ~2s after `verifyBookingHotel` succeeds; once rooms appear the page transitions to the mapping UI.

    No API key required — the `sessionId` query param is the capability token.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingConnectRoomsResponse | Error
     """


    return sync_detailed(
        client=client,
session_id=session_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    session_id: str,

) -> Response[BookingConnectRoomsResponse | Error]:
    """ List Booking.com rooms imported for a Connect session

     Returns the rooms imported from the Booking.com hotel claimed in this Connect session, plus the
    customer's listing options for the mapping dropdowns. Hosted-picker pages poll this endpoint every
    ~2s after `verifyBookingHotel` succeeds; once rooms appear the page transitions to the mapping UI.

    No API key required — the `sessionId` query param is the capability token.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingConnectRoomsResponse | Error]
     """


    kwargs = _get_kwargs(
        session_id=session_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    session_id: str,

) -> BookingConnectRoomsResponse | Error | None:
    """ List Booking.com rooms imported for a Connect session

     Returns the rooms imported from the Booking.com hotel claimed in this Connect session, plus the
    customer's listing options for the mapping dropdowns. Hosted-picker pages poll this endpoint every
    ~2s after `verifyBookingHotel` succeeds; once rooms appear the page transitions to the mapping UI.

    No API key required — the `sessionId` query param is the capability token.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingConnectRoomsResponse | Error
     """


    return (await asyncio_detailed(
        client=client,
session_id=session_id,

    )).parsed
