from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.promotion_list_response import PromotionListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    refresh: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["refresh"] = refresh


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/{id}/promotions".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PromotionListResponse | None:
    if response.status_code == 200:
        response_200 = PromotionListResponse.from_dict(response.json())



        return response_200

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PromotionListResponse]:
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
    refresh: bool | Unset = UNSET,

) -> Response[Error | PromotionListResponse]:
    """ List a listing's promotions

     Airbnb and Booking.com promotions on the listing, in one model. Includes Airbnb promotions running
    or available (the new listing promotion shows as `eligible` when the listing qualifies), Airbnb
    Custom promotions seen on bookings (read-only — they override your prices on Airbnb), and
    Booking.com promotions covering the listing's room, including deactivated ones.

    Pass `refresh=true` to re-read the channels first; otherwise the stored copy is returned (kept
    current by Airbnb's notifications and a sync every 30 minutes).

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        refresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PromotionListResponse]
     """


    kwargs = _get_kwargs(
        id=id,
refresh=refresh,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    refresh: bool | Unset = UNSET,

) -> Error | PromotionListResponse | None:
    """ List a listing's promotions

     Airbnb and Booking.com promotions on the listing, in one model. Includes Airbnb promotions running
    or available (the new listing promotion shows as `eligible` when the listing qualifies), Airbnb
    Custom promotions seen on bookings (read-only — they override your prices on Airbnb), and
    Booking.com promotions covering the listing's room, including deactivated ones.

    Pass `refresh=true` to re-read the channels first; otherwise the stored copy is returned (kept
    current by Airbnb's notifications and a sync every 30 minutes).

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        refresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PromotionListResponse
     """


    return sync_detailed(
        id=id,
client=client,
refresh=refresh,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    refresh: bool | Unset = UNSET,

) -> Response[Error | PromotionListResponse]:
    """ List a listing's promotions

     Airbnb and Booking.com promotions on the listing, in one model. Includes Airbnb promotions running
    or available (the new listing promotion shows as `eligible` when the listing qualifies), Airbnb
    Custom promotions seen on bookings (read-only — they override your prices on Airbnb), and
    Booking.com promotions covering the listing's room, including deactivated ones.

    Pass `refresh=true` to re-read the channels first; otherwise the stored copy is returned (kept
    current by Airbnb's notifications and a sync every 30 minutes).

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        refresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PromotionListResponse]
     """


    kwargs = _get_kwargs(
        id=id,
refresh=refresh,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    refresh: bool | Unset = UNSET,

) -> Error | PromotionListResponse | None:
    """ List a listing's promotions

     Airbnb and Booking.com promotions on the listing, in one model. Includes Airbnb promotions running
    or available (the new listing promotion shows as `eligible` when the listing qualifies), Airbnb
    Custom promotions seen on bookings (read-only — they override your prices on Airbnb), and
    Booking.com promotions covering the listing's room, including deactivated ones.

    Pass `refresh=true` to re-read the channels first; otherwise the stored copy is returned (kept
    current by Airbnb's notifications and a sync every 30 minutes).

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        refresh (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PromotionListResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
refresh=refresh,

    )).parsed
