from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_verify_hotel_request import BookingVerifyHotelRequest
from ...models.booking_verify_hotel_response import BookingVerifyHotelResponse
from ...models.error import Error
from typing import cast



def _get_kwargs(
    *,
    body: BookingVerifyHotelRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/booking/verify",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BookingVerifyHotelResponse | Error | None:
    if response.status_code == 200:
        response_200 = BookingVerifyHotelResponse.from_dict(response.json())



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

    if response.status_code == 412:
        response_412 = Error.from_dict(response.json())



        return response_412

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BookingVerifyHotelResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BookingVerifyHotelRequest,

) -> Response[BookingVerifyHotelResponse | Error]:
    """ Verify a Booking.com hotel ID for a Connect session

     Manual-paste fallback that closes the Booking.com claim flow. Call this after the customer completes
    Stage 1 designation in their Booking Extranet (ticking FantasticStay/Repull as their connectivity
    provider) and pastes their Hotel ID into the hosted picker.

    Validates the hotel against Booking's property API, persists the `pms_connections` row, kicks off
    the room import, and transitions the Connect session to `awaiting_room_mapping`.

    No API key required — the `sessionId` is the capability token. Sessions in any terminal state are
    rejected.

    Args:
        body (BookingVerifyHotelRequest): Body for `POST /v1/connect/booking/verify`. Manual-paste
            fallback that closes a Booking.com Connect session after the customer completes Stage 1
            designation in the Extranet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingVerifyHotelResponse | Error]
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
    body: BookingVerifyHotelRequest,

) -> BookingVerifyHotelResponse | Error | None:
    """ Verify a Booking.com hotel ID for a Connect session

     Manual-paste fallback that closes the Booking.com claim flow. Call this after the customer completes
    Stage 1 designation in their Booking Extranet (ticking FantasticStay/Repull as their connectivity
    provider) and pastes their Hotel ID into the hosted picker.

    Validates the hotel against Booking's property API, persists the `pms_connections` row, kicks off
    the room import, and transitions the Connect session to `awaiting_room_mapping`.

    No API key required — the `sessionId` is the capability token. Sessions in any terminal state are
    rejected.

    Args:
        body (BookingVerifyHotelRequest): Body for `POST /v1/connect/booking/verify`. Manual-paste
            fallback that closes a Booking.com Connect session after the customer completes Stage 1
            designation in the Extranet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingVerifyHotelResponse | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BookingVerifyHotelRequest,

) -> Response[BookingVerifyHotelResponse | Error]:
    """ Verify a Booking.com hotel ID for a Connect session

     Manual-paste fallback that closes the Booking.com claim flow. Call this after the customer completes
    Stage 1 designation in their Booking Extranet (ticking FantasticStay/Repull as their connectivity
    provider) and pastes their Hotel ID into the hosted picker.

    Validates the hotel against Booking's property API, persists the `pms_connections` row, kicks off
    the room import, and transitions the Connect session to `awaiting_room_mapping`.

    No API key required — the `sessionId` is the capability token. Sessions in any terminal state are
    rejected.

    Args:
        body (BookingVerifyHotelRequest): Body for `POST /v1/connect/booking/verify`. Manual-paste
            fallback that closes a Booking.com Connect session after the customer completes Stage 1
            designation in the Extranet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingVerifyHotelResponse | Error]
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
    body: BookingVerifyHotelRequest,

) -> BookingVerifyHotelResponse | Error | None:
    """ Verify a Booking.com hotel ID for a Connect session

     Manual-paste fallback that closes the Booking.com claim flow. Call this after the customer completes
    Stage 1 designation in their Booking Extranet (ticking FantasticStay/Repull as their connectivity
    provider) and pastes their Hotel ID into the hosted picker.

    Validates the hotel against Booking's property API, persists the `pms_connections` row, kicks off
    the room import, and transitions the Connect session to `awaiting_room_mapping`.

    No API key required — the `sessionId` is the capability token. Sessions in any terminal state are
    rejected.

    Args:
        body (BookingVerifyHotelRequest): Body for `POST /v1/connect/booking/verify`. Manual-paste
            fallback that closes a Booking.com Connect session after the customer completes Stage 1
            designation in the Extranet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingVerifyHotelResponse | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
