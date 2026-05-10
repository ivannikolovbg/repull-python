from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_listings_status import ListListingsStatus
from ...models.listing_list_response import ListingListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    q: str | Unset = UNSET,
    status: ListListingsStatus | Unset = UNSET,
    channel: str | Unset = UNSET,
    include: str | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_schema, Unset):
        headers["X-Schema"] = x_schema



    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["offset"] = offset

    params["limit"] = limit

    params["q"] = q

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["channel"] = channel

    params["include"] = include


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListingListResponse | None:
    if response.status_code == 200:
        response_200 = ListingListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListingListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    q: str | Unset = UNSET,
    status: ListListingsStatus | Unset = UNSET,
    channel: str | Unset = UNSET,
    include: str | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Response[Error | ListingListResponse]:
    """ List listings

     Cursor-paginated list of listings owned by the authenticated workspace. Use `pagination.nextCursor`
    from one response as the `cursor` query param of the next request to walk the full set. `?offset=`
    is also accepted as a first-class alias for shallow paging (0..10000) — see the `offset` parameter
    below. Mutually exclusive with `cursor`. Filters: `q` (substring on name/street/city), `status`,
    `channel`.

    **Optional expansions:** Pass `?include=content` to enrich each row with the rich content slab
    (summary, description, space, house rules, etc. — sourced from `listings_descriptions` for the `en`
    locale). Pass `?include=details` for the structural slab (bedrooms, bathrooms, person capacity,
    check-in window, wifi, house manual, etc.). Both default to `null` per row when the underlying
    `listings_descriptions` / `listings_details` row is missing — distinct from the field being absent
    (which signals the expansion was not requested). Combine comma-separated, e.g.
    `?include=content,details`. The default response stays lean; consumers must opt in.

    Args:
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        q (str | Unset):
        status (ListListingsStatus | Unset):
        channel (str | Unset):  Example: airbnb.
        include (str | Unset):  Example: content,details.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingListResponse]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
offset=offset,
limit=limit,
q=q,
status=status,
channel=channel,
include=include,
x_schema=x_schema,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    q: str | Unset = UNSET,
    status: ListListingsStatus | Unset = UNSET,
    channel: str | Unset = UNSET,
    include: str | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Error | ListingListResponse | None:
    """ List listings

     Cursor-paginated list of listings owned by the authenticated workspace. Use `pagination.nextCursor`
    from one response as the `cursor` query param of the next request to walk the full set. `?offset=`
    is also accepted as a first-class alias for shallow paging (0..10000) — see the `offset` parameter
    below. Mutually exclusive with `cursor`. Filters: `q` (substring on name/street/city), `status`,
    `channel`.

    **Optional expansions:** Pass `?include=content` to enrich each row with the rich content slab
    (summary, description, space, house rules, etc. — sourced from `listings_descriptions` for the `en`
    locale). Pass `?include=details` for the structural slab (bedrooms, bathrooms, person capacity,
    check-in window, wifi, house manual, etc.). Both default to `null` per row when the underlying
    `listings_descriptions` / `listings_details` row is missing — distinct from the field being absent
    (which signals the expansion was not requested). Combine comma-separated, e.g.
    `?include=content,details`. The default response stays lean; consumers must opt in.

    Args:
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        q (str | Unset):
        status (ListListingsStatus | Unset):
        channel (str | Unset):  Example: airbnb.
        include (str | Unset):  Example: content,details.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingListResponse
     """


    return sync_detailed(
        client=client,
cursor=cursor,
offset=offset,
limit=limit,
q=q,
status=status,
channel=channel,
include=include,
x_schema=x_schema,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    q: str | Unset = UNSET,
    status: ListListingsStatus | Unset = UNSET,
    channel: str | Unset = UNSET,
    include: str | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Response[Error | ListingListResponse]:
    """ List listings

     Cursor-paginated list of listings owned by the authenticated workspace. Use `pagination.nextCursor`
    from one response as the `cursor` query param of the next request to walk the full set. `?offset=`
    is also accepted as a first-class alias for shallow paging (0..10000) — see the `offset` parameter
    below. Mutually exclusive with `cursor`. Filters: `q` (substring on name/street/city), `status`,
    `channel`.

    **Optional expansions:** Pass `?include=content` to enrich each row with the rich content slab
    (summary, description, space, house rules, etc. — sourced from `listings_descriptions` for the `en`
    locale). Pass `?include=details` for the structural slab (bedrooms, bathrooms, person capacity,
    check-in window, wifi, house manual, etc.). Both default to `null` per row when the underlying
    `listings_descriptions` / `listings_details` row is missing — distinct from the field being absent
    (which signals the expansion was not requested). Combine comma-separated, e.g.
    `?include=content,details`. The default response stays lean; consumers must opt in.

    Args:
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        q (str | Unset):
        status (ListListingsStatus | Unset):
        channel (str | Unset):  Example: airbnb.
        include (str | Unset):  Example: content,details.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingListResponse]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
offset=offset,
limit=limit,
q=q,
status=status,
channel=channel,
include=include,
x_schema=x_schema,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 20,
    q: str | Unset = UNSET,
    status: ListListingsStatus | Unset = UNSET,
    channel: str | Unset = UNSET,
    include: str | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Error | ListingListResponse | None:
    """ List listings

     Cursor-paginated list of listings owned by the authenticated workspace. Use `pagination.nextCursor`
    from one response as the `cursor` query param of the next request to walk the full set. `?offset=`
    is also accepted as a first-class alias for shallow paging (0..10000) — see the `offset` parameter
    below. Mutually exclusive with `cursor`. Filters: `q` (substring on name/street/city), `status`,
    `channel`.

    **Optional expansions:** Pass `?include=content` to enrich each row with the rich content slab
    (summary, description, space, house rules, etc. — sourced from `listings_descriptions` for the `en`
    locale). Pass `?include=details` for the structural slab (bedrooms, bathrooms, person capacity,
    check-in window, wifi, house manual, etc.). Both default to `null` per row when the underlying
    `listings_descriptions` / `listings_details` row is missing — distinct from the field being absent
    (which signals the expansion was not requested). Combine comma-separated, e.g.
    `?include=content,details`. The default response stays lean; consumers must opt in.

    Args:
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 20.
        q (str | Unset):
        status (ListListingsStatus | Unset):
        channel (str | Unset):  Example: airbnb.
        include (str | Unset):  Example: content,details.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingListResponse
     """


    return (await asyncio_detailed(
        client=client,
cursor=cursor,
offset=offset,
limit=limit,
q=q,
status=status,
channel=channel,
include=include,
x_schema=x_schema,

    )).parsed
