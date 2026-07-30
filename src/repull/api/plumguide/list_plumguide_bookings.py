from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    listing_id: int | Unset = UNSET,
    booking_code: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["listing_id"] = listing_id

    params["booking_code"] = booking_code


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/plumguide/bookings",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

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
    listing_id: int | Unset = UNSET,
    booking_code: str | Unset = UNSET,

) -> Response[Any | Error]:
    """ List Plumguide bookings

     List Plumguide bookings. Default returns all bookings; pass `listing_id` to filter to one listing,
    or `booking_code` to fetch a single booking.

    Args:
        listing_id (int | Unset):
        booking_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        listing_id=listing_id,
booking_code=booking_code,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    listing_id: int | Unset = UNSET,
    booking_code: str | Unset = UNSET,

) -> Any | Error | None:
    """ List Plumguide bookings

     List Plumguide bookings. Default returns all bookings; pass `listing_id` to filter to one listing,
    or `booking_code` to fetch a single booking.

    Args:
        listing_id (int | Unset):
        booking_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        client=client,
listing_id=listing_id,
booking_code=booking_code,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    listing_id: int | Unset = UNSET,
    booking_code: str | Unset = UNSET,

) -> Response[Any | Error]:
    """ List Plumguide bookings

     List Plumguide bookings. Default returns all bookings; pass `listing_id` to filter to one listing,
    or `booking_code` to fetch a single booking.

    Args:
        listing_id (int | Unset):
        booking_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        listing_id=listing_id,
booking_code=booking_code,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    listing_id: int | Unset = UNSET,
    booking_code: str | Unset = UNSET,

) -> Any | Error | None:
    """ List Plumguide bookings

     List Plumguide bookings. Default returns all bookings; pass `listing_id` to filter to one listing,
    or `booking_code` to fetch a single booking.

    Args:
        listing_id (int | Unset):
        booking_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        client=client,
listing_id=listing_id,
booking_code=booking_code,

    )).parsed
