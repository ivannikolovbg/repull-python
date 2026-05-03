from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_market_browse_sort import ListMarketBrowseSort
from ...models.market_browse_response import MarketBrowseResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    q: str | Unset = UNSET,
    country: str | Unset = UNSET,
    min_listings: int | Unset = 5,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 30,
    sort: ListMarketBrowseSort | Unset = ListMarketBrowseSort.LISTINGS_DESC,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["q"] = q

    params["country"] = country

    params["min_listings"] = min_listings

    params["cursor"] = cursor

    params["limit"] = limit

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/markets/browse",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | MarketBrowseResponse | None:
    if response.status_code == 200:
        response_200 = MarketBrowseResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | MarketBrowseResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    country: str | Unset = UNSET,
    min_listings: int | Unset = 5,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 30,
    sort: ListMarketBrowseSort | Unset = ListMarketBrowseSort.LISTINGS_DESC,

) -> Response[Error | MarketBrowseResponse]:
    """ Paginated discovery catalog

     Cursor-paginated, search-filterable catalog of every Atlas-tracked market the customer could expand
    into. Backed by the precomputed `market_summaries` table (>=5 active comps per city). Supports fuzzy
    `q` substring search (trigram-indexed), `country` (ISO 3166-1 alpha-2) filter, and `sort`
    (`listings_desc` | `name_asc`). Use the `nextCursor` from `pagination` to walk pages — the cursor is
    an opaque base64 token; do not parse it.

    `pagination.total` is the count of markets matching the current `q`/`country`/`min_listings` filter
    (across all pages). Renamed from the upstream's legacy `total_in_filter` so SDK consumers see the
    same `pagination.total` field as on every other list endpoint.

    Args:
        q (str | Unset):
        country (str | Unset):
        min_listings (int | Unset):  Default: 5.
        cursor (str | Unset):
        limit (int | Unset):  Default: 30.
        sort (ListMarketBrowseSort | Unset):  Default: ListMarketBrowseSort.LISTINGS_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MarketBrowseResponse]
     """


    kwargs = _get_kwargs(
        q=q,
country=country,
min_listings=min_listings,
cursor=cursor,
limit=limit,
sort=sort,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    country: str | Unset = UNSET,
    min_listings: int | Unset = 5,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 30,
    sort: ListMarketBrowseSort | Unset = ListMarketBrowseSort.LISTINGS_DESC,

) -> Error | MarketBrowseResponse | None:
    """ Paginated discovery catalog

     Cursor-paginated, search-filterable catalog of every Atlas-tracked market the customer could expand
    into. Backed by the precomputed `market_summaries` table (>=5 active comps per city). Supports fuzzy
    `q` substring search (trigram-indexed), `country` (ISO 3166-1 alpha-2) filter, and `sort`
    (`listings_desc` | `name_asc`). Use the `nextCursor` from `pagination` to walk pages — the cursor is
    an opaque base64 token; do not parse it.

    `pagination.total` is the count of markets matching the current `q`/`country`/`min_listings` filter
    (across all pages). Renamed from the upstream's legacy `total_in_filter` so SDK consumers see the
    same `pagination.total` field as on every other list endpoint.

    Args:
        q (str | Unset):
        country (str | Unset):
        min_listings (int | Unset):  Default: 5.
        cursor (str | Unset):
        limit (int | Unset):  Default: 30.
        sort (ListMarketBrowseSort | Unset):  Default: ListMarketBrowseSort.LISTINGS_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MarketBrowseResponse
     """


    return sync_detailed(
        client=client,
q=q,
country=country,
min_listings=min_listings,
cursor=cursor,
limit=limit,
sort=sort,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    country: str | Unset = UNSET,
    min_listings: int | Unset = 5,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 30,
    sort: ListMarketBrowseSort | Unset = ListMarketBrowseSort.LISTINGS_DESC,

) -> Response[Error | MarketBrowseResponse]:
    """ Paginated discovery catalog

     Cursor-paginated, search-filterable catalog of every Atlas-tracked market the customer could expand
    into. Backed by the precomputed `market_summaries` table (>=5 active comps per city). Supports fuzzy
    `q` substring search (trigram-indexed), `country` (ISO 3166-1 alpha-2) filter, and `sort`
    (`listings_desc` | `name_asc`). Use the `nextCursor` from `pagination` to walk pages — the cursor is
    an opaque base64 token; do not parse it.

    `pagination.total` is the count of markets matching the current `q`/`country`/`min_listings` filter
    (across all pages). Renamed from the upstream's legacy `total_in_filter` so SDK consumers see the
    same `pagination.total` field as on every other list endpoint.

    Args:
        q (str | Unset):
        country (str | Unset):
        min_listings (int | Unset):  Default: 5.
        cursor (str | Unset):
        limit (int | Unset):  Default: 30.
        sort (ListMarketBrowseSort | Unset):  Default: ListMarketBrowseSort.LISTINGS_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MarketBrowseResponse]
     """


    kwargs = _get_kwargs(
        q=q,
country=country,
min_listings=min_listings,
cursor=cursor,
limit=limit,
sort=sort,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    q: str | Unset = UNSET,
    country: str | Unset = UNSET,
    min_listings: int | Unset = 5,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 30,
    sort: ListMarketBrowseSort | Unset = ListMarketBrowseSort.LISTINGS_DESC,

) -> Error | MarketBrowseResponse | None:
    """ Paginated discovery catalog

     Cursor-paginated, search-filterable catalog of every Atlas-tracked market the customer could expand
    into. Backed by the precomputed `market_summaries` table (>=5 active comps per city). Supports fuzzy
    `q` substring search (trigram-indexed), `country` (ISO 3166-1 alpha-2) filter, and `sort`
    (`listings_desc` | `name_asc`). Use the `nextCursor` from `pagination` to walk pages — the cursor is
    an opaque base64 token; do not parse it.

    `pagination.total` is the count of markets matching the current `q`/`country`/`min_listings` filter
    (across all pages). Renamed from the upstream's legacy `total_in_filter` so SDK consumers see the
    same `pagination.total` field as on every other list endpoint.

    Args:
        q (str | Unset):
        country (str | Unset):
        min_listings (int | Unset):  Default: 5.
        cursor (str | Unset):
        limit (int | Unset):  Default: 30.
        sort (ListMarketBrowseSort | Unset):  Default: ListMarketBrowseSort.LISTINGS_DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MarketBrowseResponse
     """


    return (await asyncio_detailed(
        client=client,
q=q,
country=country,
min_listings=min_listings,
cursor=cursor,
limit=limit,
sort=sort,

    )).parsed
