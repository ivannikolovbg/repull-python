from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.listing_market_state_request import ListingMarketStateRequest
from ...models.listing_market_state_response import ListingMarketStateResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ListingMarketStateRequest | Unset = UNSET,
    hotel_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    params: dict[str, Any] = {}

    params["hotel_id"] = hotel_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/{id}/online".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListingMarketStateResponse | None:
    if response.status_code == 200:
        response_200 = ListingMarketStateResponse.from_dict(response.json())



        return response_200

    if response.status_code == 402:
        response_402 = Error.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListingMarketStateResponse]:
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
    body: ListingMarketStateRequest | Unset = UNSET,
    hotel_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | ListingMarketStateResponse]:
    """ Put a listing back on the market

     Put this listing back on sale, on every channel it is connected to. The counterpart of `POST
    /v1/listings/{id}/offline`, which documents the per-item response and the difference between this
    and deactivating a listing in Repull.

    **It does not push content.** On **Airbnb** it re-enables sync and makes the listing available
    again; anything that changed while the listing was down is still unpublished, so follow with `POST
    /v1/listings/{id}/publish/airbnb` if the content moved. On **Booking.com** it re-syncs the true
    calendar rather than opening everything: dates that are genuinely blocked — a reservation, an owner
    stay — stay blocked, and only the closure `offline` wrote lifts. The two directions are not mirror
    images, and that is deliberate.

    **One asymmetry worth planning for.** Taking a listing down passes no billing gate; putting it back
    up goes through the channel-publish gate. So on a workspace whose subscription has lapsed, `offline`
    still works and this endpoint answers `402 payment_required` — a listing can be left off the market
    until billing is sorted out. That refusal is reported as a billing refusal with the action that
    fixes it, never as a channel error: retrying, or reconnecting the channel, does nothing for it.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ListingMarketStateRequest | Unset): Optional. Send no body at all unless this
            listing is mapped to more than one Booking.com property.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingMarketStateResponse]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
hotel_id=hotel_id,
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
    body: ListingMarketStateRequest | Unset = UNSET,
    hotel_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Error | ListingMarketStateResponse | None:
    """ Put a listing back on the market

     Put this listing back on sale, on every channel it is connected to. The counterpart of `POST
    /v1/listings/{id}/offline`, which documents the per-item response and the difference between this
    and deactivating a listing in Repull.

    **It does not push content.** On **Airbnb** it re-enables sync and makes the listing available
    again; anything that changed while the listing was down is still unpublished, so follow with `POST
    /v1/listings/{id}/publish/airbnb` if the content moved. On **Booking.com** it re-syncs the true
    calendar rather than opening everything: dates that are genuinely blocked — a reservation, an owner
    stay — stay blocked, and only the closure `offline` wrote lifts. The two directions are not mirror
    images, and that is deliberate.

    **One asymmetry worth planning for.** Taking a listing down passes no billing gate; putting it back
    up goes through the channel-publish gate. So on a workspace whose subscription has lapsed, `offline`
    still works and this endpoint answers `402 payment_required` — a listing can be left off the market
    until billing is sorted out. That refusal is reported as a billing refusal with the action that
    fixes it, never as a channel error: retrying, or reconnecting the channel, does nothing for it.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ListingMarketStateRequest | Unset): Optional. Send no body at all unless this
            listing is mapped to more than one Booking.com property.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingMarketStateResponse
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
hotel_id=hotel_id,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingMarketStateRequest | Unset = UNSET,
    hotel_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | ListingMarketStateResponse]:
    """ Put a listing back on the market

     Put this listing back on sale, on every channel it is connected to. The counterpart of `POST
    /v1/listings/{id}/offline`, which documents the per-item response and the difference between this
    and deactivating a listing in Repull.

    **It does not push content.** On **Airbnb** it re-enables sync and makes the listing available
    again; anything that changed while the listing was down is still unpublished, so follow with `POST
    /v1/listings/{id}/publish/airbnb` if the content moved. On **Booking.com** it re-syncs the true
    calendar rather than opening everything: dates that are genuinely blocked — a reservation, an owner
    stay — stay blocked, and only the closure `offline` wrote lifts. The two directions are not mirror
    images, and that is deliberate.

    **One asymmetry worth planning for.** Taking a listing down passes no billing gate; putting it back
    up goes through the channel-publish gate. So on a workspace whose subscription has lapsed, `offline`
    still works and this endpoint answers `402 payment_required` — a listing can be left off the market
    until billing is sorted out. That refusal is reported as a billing refusal with the action that
    fixes it, never as a channel error: retrying, or reconnecting the channel, does nothing for it.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ListingMarketStateRequest | Unset): Optional. Send no body at all unless this
            listing is mapped to more than one Booking.com property.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingMarketStateResponse]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
hotel_id=hotel_id,
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
    body: ListingMarketStateRequest | Unset = UNSET,
    hotel_id: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Error | ListingMarketStateResponse | None:
    """ Put a listing back on the market

     Put this listing back on sale, on every channel it is connected to. The counterpart of `POST
    /v1/listings/{id}/offline`, which documents the per-item response and the difference between this
    and deactivating a listing in Repull.

    **It does not push content.** On **Airbnb** it re-enables sync and makes the listing available
    again; anything that changed while the listing was down is still unpublished, so follow with `POST
    /v1/listings/{id}/publish/airbnb` if the content moved. On **Booking.com** it re-syncs the true
    calendar rather than opening everything: dates that are genuinely blocked — a reservation, an owner
    stay — stay blocked, and only the closure `offline` wrote lifts. The two directions are not mirror
    images, and that is deliberate.

    **One asymmetry worth planning for.** Taking a listing down passes no billing gate; putting it back
    up goes through the channel-publish gate. So on a workspace whose subscription has lapsed, `offline`
    still works and this endpoint answers `402 payment_required` — a listing can be left off the market
    until billing is sorted out. That refusal is reported as a billing refusal with the action that
    fixes it, never as a channel error: retrying, or reconnecting the channel, does nothing for it.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ListingMarketStateRequest | Unset): Optional. Send no body at all unless this
            listing is mapped to more than one Booking.com property.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingMarketStateResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
hotel_id=hotel_id,
idempotency_key=idempotency_key,

    )).parsed
