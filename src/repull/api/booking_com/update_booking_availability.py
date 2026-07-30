from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_availability_update_request import BookingAvailabilityUpdateRequest
from ...models.error import Error
from typing import cast



def _get_kwargs(
    *,
    body: BookingAvailabilityUpdateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/booking/availability",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BookingAvailabilityUpdateRequest,

) -> Response[Any | Error]:
    """ Update Booking.com rates/availability

     Push availability, rates, and the full restriction set to Booking.com. `type` selects the write
    path:

    - `rates` — nightly price + length-of-stay / arrival restrictions (min/max stay, closed-to-arrival,
    closed-to-departure, advance-reservation window).
    - `availability` — inventory (`availableRooms`), the dedicated stop-sell flag (`closed`), and the
    same restriction set.
    - `derived-pricing` — occupancy-derived pricing rules.

    Restrictions never leak across channels — this endpoint writes only to Booking.com. Errors from
    upstream surface as `booking_error`.

    Args:
        body (BookingAvailabilityUpdateRequest): Body for `PUT /v1/channels/booking/availability`.
            Selects one of Booking's three ARI write paths via `type` and forwards `updates` verbatim
            to the connector.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    body: BookingAvailabilityUpdateRequest,

) -> Any | Error | None:
    """ Update Booking.com rates/availability

     Push availability, rates, and the full restriction set to Booking.com. `type` selects the write
    path:

    - `rates` — nightly price + length-of-stay / arrival restrictions (min/max stay, closed-to-arrival,
    closed-to-departure, advance-reservation window).
    - `availability` — inventory (`availableRooms`), the dedicated stop-sell flag (`closed`), and the
    same restriction set.
    - `derived-pricing` — occupancy-derived pricing rules.

    Restrictions never leak across channels — this endpoint writes only to Booking.com. Errors from
    upstream surface as `booking_error`.

    Args:
        body (BookingAvailabilityUpdateRequest): Body for `PUT /v1/channels/booking/availability`.
            Selects one of Booking's three ARI write paths via `type` and forwards `updates` verbatim
            to the connector.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BookingAvailabilityUpdateRequest,

) -> Response[Any | Error]:
    """ Update Booking.com rates/availability

     Push availability, rates, and the full restriction set to Booking.com. `type` selects the write
    path:

    - `rates` — nightly price + length-of-stay / arrival restrictions (min/max stay, closed-to-arrival,
    closed-to-departure, advance-reservation window).
    - `availability` — inventory (`availableRooms`), the dedicated stop-sell flag (`closed`), and the
    same restriction set.
    - `derived-pricing` — occupancy-derived pricing rules.

    Restrictions never leak across channels — this endpoint writes only to Booking.com. Errors from
    upstream surface as `booking_error`.

    Args:
        body (BookingAvailabilityUpdateRequest): Body for `PUT /v1/channels/booking/availability`.
            Selects one of Booking's three ARI write paths via `type` and forwards `updates` verbatim
            to the connector.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    body: BookingAvailabilityUpdateRequest,

) -> Any | Error | None:
    """ Update Booking.com rates/availability

     Push availability, rates, and the full restriction set to Booking.com. `type` selects the write
    path:

    - `rates` — nightly price + length-of-stay / arrival restrictions (min/max stay, closed-to-arrival,
    closed-to-departure, advance-reservation window).
    - `availability` — inventory (`availableRooms`), the dedicated stop-sell flag (`closed`), and the
    same restriction set.
    - `derived-pricing` — occupancy-derived pricing rules.

    Restrictions never leak across channels — this endpoint writes only to Booking.com. Errors from
    upstream surface as `booking_error`.

    Args:
        body (BookingAvailabilityUpdateRequest): Body for `PUT /v1/channels/booking/availability`.
            Selects one of Booking's three ARI write paths via `type` and forwards `updates` verbatim
            to the connector.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
