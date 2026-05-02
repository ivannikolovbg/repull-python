from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_pricing_update_request import BookingPricingUpdateRequest
from ...models.booking_pricing_update_response import BookingPricingUpdateResponse
from ...models.error import Error
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: BookingPricingUpdateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/booking/listings/{id}/pricing".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BookingPricingUpdateResponse | Error | None:
    if response.status_code == 200:
        response_200 = BookingPricingUpdateResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BookingPricingUpdateResponse | Error]:
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
    body: BookingPricingUpdateRequest,

) -> Response[BookingPricingUpdateResponse | Error]:
    """ Update Booking.com pricing for a listing

     Pushes one or more rate updates to Booking.com via `updateRates`. Each update needs `roomId` +
    `rateId` + `dateRange` + `price` + `currency`. Field-level validation runs up front so callers don't
    have to parse Booking's XML error envelope to discover a missing `roomId`.

    Args:
        id (int):
        body (BookingPricingUpdateRequest): Body for `PUT
            /v1/channels/booking/listings/{id}/pricing`. Pricing on Booking is per-room/per-rate-plan,
            so `room_id` + `rate_id` are required on every update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingPricingUpdateResponse | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: BookingPricingUpdateRequest,

) -> BookingPricingUpdateResponse | Error | None:
    """ Update Booking.com pricing for a listing

     Pushes one or more rate updates to Booking.com via `updateRates`. Each update needs `roomId` +
    `rateId` + `dateRange` + `price` + `currency`. Field-level validation runs up front so callers don't
    have to parse Booking's XML error envelope to discover a missing `roomId`.

    Args:
        id (int):
        body (BookingPricingUpdateRequest): Body for `PUT
            /v1/channels/booking/listings/{id}/pricing`. Pricing on Booking is per-room/per-rate-plan,
            so `room_id` + `rate_id` are required on every update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingPricingUpdateResponse | Error
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: BookingPricingUpdateRequest,

) -> Response[BookingPricingUpdateResponse | Error]:
    """ Update Booking.com pricing for a listing

     Pushes one or more rate updates to Booking.com via `updateRates`. Each update needs `roomId` +
    `rateId` + `dateRange` + `price` + `currency`. Field-level validation runs up front so callers don't
    have to parse Booking's XML error envelope to discover a missing `roomId`.

    Args:
        id (int):
        body (BookingPricingUpdateRequest): Body for `PUT
            /v1/channels/booking/listings/{id}/pricing`. Pricing on Booking is per-room/per-rate-plan,
            so `room_id` + `rate_id` are required on every update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingPricingUpdateResponse | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: BookingPricingUpdateRequest,

) -> BookingPricingUpdateResponse | Error | None:
    """ Update Booking.com pricing for a listing

     Pushes one or more rate updates to Booking.com via `updateRates`. Each update needs `roomId` +
    `rateId` + `dateRange` + `price` + `currency`. Field-level validation runs up front so callers don't
    have to parse Booking's XML error envelope to discover a missing `roomId`.

    Args:
        id (int):
        body (BookingPricingUpdateRequest): Body for `PUT
            /v1/channels/booking/listings/{id}/pricing`. Pricing on Booking is per-room/per-rate-plan,
            so `room_id` + `rate_id` are required on every update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingPricingUpdateResponse | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
