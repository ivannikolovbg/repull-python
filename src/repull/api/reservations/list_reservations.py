from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_reservations_status import ListReservationsStatus
from ...models.reservation_list_response import ReservationListResponse
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    platform: str | Unset = UNSET,
    status: ListReservationsStatus | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    check_in_after: datetime.date | Unset = UNSET,
    check_in_before: datetime.date | Unset = UNSET,
    check_in_from: datetime.date | Unset = UNSET,
    check_in_to: datetime.date | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_schema, Unset):
        headers["X-Schema"] = x_schema



    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["offset"] = offset

    params["platform"] = platform

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["listing_id"] = listing_id

    json_check_in_after: str | Unset = UNSET
    if not isinstance(check_in_after, Unset):
        json_check_in_after = check_in_after.isoformat()
    params["check_in_after"] = json_check_in_after

    json_check_in_before: str | Unset = UNSET
    if not isinstance(check_in_before, Unset):
        json_check_in_before = check_in_before.isoformat()
    params["check_in_before"] = json_check_in_before

    json_check_in_from: str | Unset = UNSET
    if not isinstance(check_in_from, Unset):
        json_check_in_from = check_in_from.isoformat()
    params["checkInFrom"] = json_check_in_from

    json_check_in_to: str | Unset = UNSET
    if not isinstance(check_in_to, Unset):
        json_check_in_to = check_in_to.isoformat()
    params["checkInTo"] = json_check_in_to


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/reservations",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ReservationListResponse | None:
    if response.status_code == 200:
        response_200 = ReservationListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ReservationListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    platform: str | Unset = UNSET,
    status: ListReservationsStatus | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    check_in_after: datetime.date | Unset = UNSET,
    check_in_before: datetime.date | Unset = UNSET,
    check_in_from: datetime.date | Unset = UNSET,
    check_in_to: datetime.date | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Response[Any | ReservationListResponse]:
    """ List reservations

     Cursor-paginated list of reservations across all connected PMS platforms. Filter by platform,
    status, listing, or check-in date range.

    **Pagination:** Walk pages with `?cursor=` — pass `pagination.next_cursor` from one response back as
    `?cursor=` on the next request. Stop when `pagination.has_more` is `false`. `limit` defaults to 50,
    max 100; requesting more returns 422 (no silent truncation).

    **Deprecation:** The `?offset=` query param is supported for backward compatibility but is
    deprecated and will be removed after the `Sunset` header date. Responses to offset requests carry a
    `Deprecation: true` header. Migrate to `?cursor=`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):
        platform (str | Unset):
        status (ListReservationsStatus | Unset):
        listing_id (int | Unset):
        check_in_after (datetime.date | Unset):
        check_in_before (datetime.date | Unset):
        check_in_from (datetime.date | Unset):
        check_in_to (datetime.date | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ReservationListResponse]
     """


    kwargs = _get_kwargs(
        limit=limit,
cursor=cursor,
offset=offset,
platform=platform,
status=status,
listing_id=listing_id,
check_in_after=check_in_after,
check_in_before=check_in_before,
check_in_from=check_in_from,
check_in_to=check_in_to,
x_schema=x_schema,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    platform: str | Unset = UNSET,
    status: ListReservationsStatus | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    check_in_after: datetime.date | Unset = UNSET,
    check_in_before: datetime.date | Unset = UNSET,
    check_in_from: datetime.date | Unset = UNSET,
    check_in_to: datetime.date | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Any | ReservationListResponse | None:
    """ List reservations

     Cursor-paginated list of reservations across all connected PMS platforms. Filter by platform,
    status, listing, or check-in date range.

    **Pagination:** Walk pages with `?cursor=` — pass `pagination.next_cursor` from one response back as
    `?cursor=` on the next request. Stop when `pagination.has_more` is `false`. `limit` defaults to 50,
    max 100; requesting more returns 422 (no silent truncation).

    **Deprecation:** The `?offset=` query param is supported for backward compatibility but is
    deprecated and will be removed after the `Sunset` header date. Responses to offset requests carry a
    `Deprecation: true` header. Migrate to `?cursor=`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):
        platform (str | Unset):
        status (ListReservationsStatus | Unset):
        listing_id (int | Unset):
        check_in_after (datetime.date | Unset):
        check_in_before (datetime.date | Unset):
        check_in_from (datetime.date | Unset):
        check_in_to (datetime.date | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ReservationListResponse
     """


    return sync_detailed(
        client=client,
limit=limit,
cursor=cursor,
offset=offset,
platform=platform,
status=status,
listing_id=listing_id,
check_in_after=check_in_after,
check_in_before=check_in_before,
check_in_from=check_in_from,
check_in_to=check_in_to,
x_schema=x_schema,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    platform: str | Unset = UNSET,
    status: ListReservationsStatus | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    check_in_after: datetime.date | Unset = UNSET,
    check_in_before: datetime.date | Unset = UNSET,
    check_in_from: datetime.date | Unset = UNSET,
    check_in_to: datetime.date | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Response[Any | ReservationListResponse]:
    """ List reservations

     Cursor-paginated list of reservations across all connected PMS platforms. Filter by platform,
    status, listing, or check-in date range.

    **Pagination:** Walk pages with `?cursor=` — pass `pagination.next_cursor` from one response back as
    `?cursor=` on the next request. Stop when `pagination.has_more` is `false`. `limit` defaults to 50,
    max 100; requesting more returns 422 (no silent truncation).

    **Deprecation:** The `?offset=` query param is supported for backward compatibility but is
    deprecated and will be removed after the `Sunset` header date. Responses to offset requests carry a
    `Deprecation: true` header. Migrate to `?cursor=`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):
        platform (str | Unset):
        status (ListReservationsStatus | Unset):
        listing_id (int | Unset):
        check_in_after (datetime.date | Unset):
        check_in_before (datetime.date | Unset):
        check_in_from (datetime.date | Unset):
        check_in_to (datetime.date | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ReservationListResponse]
     """


    kwargs = _get_kwargs(
        limit=limit,
cursor=cursor,
offset=offset,
platform=platform,
status=status,
listing_id=listing_id,
check_in_after=check_in_after,
check_in_before=check_in_before,
check_in_from=check_in_from,
check_in_to=check_in_to,
x_schema=x_schema,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = UNSET,
    platform: str | Unset = UNSET,
    status: ListReservationsStatus | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    check_in_after: datetime.date | Unset = UNSET,
    check_in_before: datetime.date | Unset = UNSET,
    check_in_from: datetime.date | Unset = UNSET,
    check_in_to: datetime.date | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Any | ReservationListResponse | None:
    """ List reservations

     Cursor-paginated list of reservations across all connected PMS platforms. Filter by platform,
    status, listing, or check-in date range.

    **Pagination:** Walk pages with `?cursor=` — pass `pagination.next_cursor` from one response back as
    `?cursor=` on the next request. Stop when `pagination.has_more` is `false`. `limit` defaults to 50,
    max 100; requesting more returns 422 (no silent truncation).

    **Deprecation:** The `?offset=` query param is supported for backward compatibility but is
    deprecated and will be removed after the `Sunset` header date. Responses to offset requests carry a
    `Deprecation: true` header. Migrate to `?cursor=`.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):
        platform (str | Unset):
        status (ListReservationsStatus | Unset):
        listing_id (int | Unset):
        check_in_after (datetime.date | Unset):
        check_in_before (datetime.date | Unset):
        check_in_from (datetime.date | Unset):
        check_in_to (datetime.date | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ReservationListResponse
     """


    return (await asyncio_detailed(
        client=client,
limit=limit,
cursor=cursor,
offset=offset,
platform=platform,
status=status,
listing_id=listing_id,
check_in_after=check_in_after,
check_in_before=check_in_before,
check_in_from=check_in_from,
check_in_to=check_in_to,
x_schema=x_schema,

    )).parsed
