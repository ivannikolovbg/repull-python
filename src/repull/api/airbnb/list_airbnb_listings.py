from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_listing_list_response import AirbnbListingListResponse
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    account_id: str | Unset = UNSET,
    include: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params["include"] = include


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/listings",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AirbnbListingListResponse | Error | None:
    if response.status_code == 200:
        response_200 = AirbnbListingListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AirbnbListingListResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
    include: str | Unset = UNSET,

) -> Response[AirbnbListingListResponse | Error]:
    """ List Airbnb listings

     List every Airbnb listing this workspace has access to via the connected Airbnb account. **Pure DB
    read — never calls Airbnb upstream.** The connect flow is what populates the local cache; the API
    serves what's already there. Customers with a disconnected host still see their last-synced data,
    with the top-level `dataFreshness` envelope flagging the staleness and pointing at the reconnect
    URL.

    Pass `?include=amenities` to enrich each connection with its locally-cached amenity set. Returns
    `null` per connection when the cache is empty.

    Pass `?include=thumbnail` to add `thumbnailUrl` to each listing — one extra column on the query that
    already runs, so a selection screen renders from a single request instead of one call per listing.
    `null` when the listing has no thumbnail stored. Combine comma-separated, e.g.
    `?include=amenities,thumbnail`.

    **Can this listing be written to?** Every connection carries `syncCategory` — Airbnb's own per-
    listing API sync decision (`sync_all`, `sync_rates_and_availability`, or `none`) — and `writable`,
    which is `false` exactly when that category is `none`. Airbnb authorises sync one listing at a time,
    so a connected account can still hold listings Airbnb refuses every write to; a write to one of
    those returns `403 listing_not_api_connected` before anything is sent, and reconnecting the account
    does not change it (the host must switch the listing on in Airbnb). Check `writable` here before a
    portfolio-wide push instead of discovering it one 403 at a time.

    Inactive listings are left out; they keep syncing and reappear once activated. Use `GET
    /v1/listings?status=inactive` to find them.

    **Several Airbnb accounts?** A workspace can connect more than one. By default this returns every
    connected account's rows; pass `?account_id=<airbnb host id>` to scope to one. Every row carries
    `accountId` + `accountName` either way, and `dataFreshness.accounts[]` reports each account's
    freshness separately, so one disconnected host no longer marks the whole response stale.

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.
        include (str | Unset):  Example: amenities,thumbnail.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbListingListResponse | Error]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
include=include,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
    include: str | Unset = UNSET,

) -> AirbnbListingListResponse | Error | None:
    """ List Airbnb listings

     List every Airbnb listing this workspace has access to via the connected Airbnb account. **Pure DB
    read — never calls Airbnb upstream.** The connect flow is what populates the local cache; the API
    serves what's already there. Customers with a disconnected host still see their last-synced data,
    with the top-level `dataFreshness` envelope flagging the staleness and pointing at the reconnect
    URL.

    Pass `?include=amenities` to enrich each connection with its locally-cached amenity set. Returns
    `null` per connection when the cache is empty.

    Pass `?include=thumbnail` to add `thumbnailUrl` to each listing — one extra column on the query that
    already runs, so a selection screen renders from a single request instead of one call per listing.
    `null` when the listing has no thumbnail stored. Combine comma-separated, e.g.
    `?include=amenities,thumbnail`.

    **Can this listing be written to?** Every connection carries `syncCategory` — Airbnb's own per-
    listing API sync decision (`sync_all`, `sync_rates_and_availability`, or `none`) — and `writable`,
    which is `false` exactly when that category is `none`. Airbnb authorises sync one listing at a time,
    so a connected account can still hold listings Airbnb refuses every write to; a write to one of
    those returns `403 listing_not_api_connected` before anything is sent, and reconnecting the account
    does not change it (the host must switch the listing on in Airbnb). Check `writable` here before a
    portfolio-wide push instead of discovering it one 403 at a time.

    Inactive listings are left out; they keep syncing and reappear once activated. Use `GET
    /v1/listings?status=inactive` to find them.

    **Several Airbnb accounts?** A workspace can connect more than one. By default this returns every
    connected account's rows; pass `?account_id=<airbnb host id>` to scope to one. Every row carries
    `accountId` + `accountName` either way, and `dataFreshness.accounts[]` reports each account's
    freshness separately, so one disconnected host no longer marks the whole response stale.

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.
        include (str | Unset):  Example: amenities,thumbnail.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbListingListResponse | Error
     """


    return sync_detailed(
        client=client,
account_id=account_id,
include=include,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
    include: str | Unset = UNSET,

) -> Response[AirbnbListingListResponse | Error]:
    """ List Airbnb listings

     List every Airbnb listing this workspace has access to via the connected Airbnb account. **Pure DB
    read — never calls Airbnb upstream.** The connect flow is what populates the local cache; the API
    serves what's already there. Customers with a disconnected host still see their last-synced data,
    with the top-level `dataFreshness` envelope flagging the staleness and pointing at the reconnect
    URL.

    Pass `?include=amenities` to enrich each connection with its locally-cached amenity set. Returns
    `null` per connection when the cache is empty.

    Pass `?include=thumbnail` to add `thumbnailUrl` to each listing — one extra column on the query that
    already runs, so a selection screen renders from a single request instead of one call per listing.
    `null` when the listing has no thumbnail stored. Combine comma-separated, e.g.
    `?include=amenities,thumbnail`.

    **Can this listing be written to?** Every connection carries `syncCategory` — Airbnb's own per-
    listing API sync decision (`sync_all`, `sync_rates_and_availability`, or `none`) — and `writable`,
    which is `false` exactly when that category is `none`. Airbnb authorises sync one listing at a time,
    so a connected account can still hold listings Airbnb refuses every write to; a write to one of
    those returns `403 listing_not_api_connected` before anything is sent, and reconnecting the account
    does not change it (the host must switch the listing on in Airbnb). Check `writable` here before a
    portfolio-wide push instead of discovering it one 403 at a time.

    Inactive listings are left out; they keep syncing and reappear once activated. Use `GET
    /v1/listings?status=inactive` to find them.

    **Several Airbnb accounts?** A workspace can connect more than one. By default this returns every
    connected account's rows; pass `?account_id=<airbnb host id>` to scope to one. Every row carries
    `accountId` + `accountName` either way, and `dataFreshness.accounts[]` reports each account's
    freshness separately, so one disconnected host no longer marks the whole response stale.

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.
        include (str | Unset):  Example: amenities,thumbnail.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbListingListResponse | Error]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
include=include,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
    include: str | Unset = UNSET,

) -> AirbnbListingListResponse | Error | None:
    """ List Airbnb listings

     List every Airbnb listing this workspace has access to via the connected Airbnb account. **Pure DB
    read — never calls Airbnb upstream.** The connect flow is what populates the local cache; the API
    serves what's already there. Customers with a disconnected host still see their last-synced data,
    with the top-level `dataFreshness` envelope flagging the staleness and pointing at the reconnect
    URL.

    Pass `?include=amenities` to enrich each connection with its locally-cached amenity set. Returns
    `null` per connection when the cache is empty.

    Pass `?include=thumbnail` to add `thumbnailUrl` to each listing — one extra column on the query that
    already runs, so a selection screen renders from a single request instead of one call per listing.
    `null` when the listing has no thumbnail stored. Combine comma-separated, e.g.
    `?include=amenities,thumbnail`.

    **Can this listing be written to?** Every connection carries `syncCategory` — Airbnb's own per-
    listing API sync decision (`sync_all`, `sync_rates_and_availability`, or `none`) — and `writable`,
    which is `false` exactly when that category is `none`. Airbnb authorises sync one listing at a time,
    so a connected account can still hold listings Airbnb refuses every write to; a write to one of
    those returns `403 listing_not_api_connected` before anything is sent, and reconnecting the account
    does not change it (the host must switch the listing on in Airbnb). Check `writable` here before a
    portfolio-wide push instead of discovering it one 403 at a time.

    Inactive listings are left out; they keep syncing and reappear once activated. Use `GET
    /v1/listings?status=inactive` to find them.

    **Several Airbnb accounts?** A workspace can connect more than one. By default this returns every
    connected account's rows; pass `?account_id=<airbnb host id>` to scope to one. Every row carries
    `accountId` + `accountName` either way, and `dataFreshness.accounts[]` reports each account's
    freshness separately, so one disconnected host no longer marks the whole response stale.

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.
        include (str | Unset):  Example: amenities,thumbnail.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbListingListResponse | Error
     """


    return (await asyncio_detailed(
        client=client,
account_id=account_id,
include=include,

    )).parsed
