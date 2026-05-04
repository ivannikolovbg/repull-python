from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_reservation_list_response import AirbnbReservationListResponse
from ...models.list_airbnb_reservations_status import ListAirbnbReservationsStatus
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
    listing_id: str | Unset = UNSET,
    status: ListAirbnbReservationsStatus | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    include_total: bool | Unset = True,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["offset"] = offset

    params["limit"] = limit

    params["listing_id"] = listing_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    params["include_total"] = include_total


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/reservations",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AirbnbReservationListResponse | None:
    if response.status_code == 200:
        response_200 = AirbnbReservationListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AirbnbReservationListResponse]:
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
    limit: int | Unset = 50,
    listing_id: str | Unset = UNSET,
    status: ListAirbnbReservationsStatus | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    include_total: bool | Unset = True,

) -> Response[AirbnbReservationListResponse]:
    r""" List Airbnb reservations

     Cursor-paginated list of reservations sourced directly from Airbnb. Use this when you need Airbnb-
    specific fields (guest payout split, cancellation policy snapshot) that the unified
    `/v1/reservations` endpoint flattens away.

    Walk pages with `?cursor=<pagination.next_cursor>` until `pagination.has_more` is `false`. The
    cursor is opaque — never construct or parse it client-side.

    `?offset=` is also accepted as a first-class alias for shallow paging (0..10000) — see the `offset`
    parameter below. Mutually exclusive with `cursor`. Internally this walks upstream Airbnb cursor
    pages to skip rows, so deep offsets cost N/limit upstream round-trips; cursor remains the better
    choice for deep pagination.

    When `status` is omitted, all statuses are returned (Airbnb defaults to `accepted` only on its own
    surface, but this endpoint normalises to \"all\"). Pass `?status=accepted` to scope.

    Args:
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.
        listing_id (str | Unset):
        status (ListAirbnbReservationsStatus | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbReservationListResponse]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
offset=offset,
limit=limit,
listing_id=listing_id,
status=status,
start_date=start_date,
end_date=end_date,
include_total=include_total,

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
    limit: int | Unset = 50,
    listing_id: str | Unset = UNSET,
    status: ListAirbnbReservationsStatus | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    include_total: bool | Unset = True,

) -> AirbnbReservationListResponse | None:
    r""" List Airbnb reservations

     Cursor-paginated list of reservations sourced directly from Airbnb. Use this when you need Airbnb-
    specific fields (guest payout split, cancellation policy snapshot) that the unified
    `/v1/reservations` endpoint flattens away.

    Walk pages with `?cursor=<pagination.next_cursor>` until `pagination.has_more` is `false`. The
    cursor is opaque — never construct or parse it client-side.

    `?offset=` is also accepted as a first-class alias for shallow paging (0..10000) — see the `offset`
    parameter below. Mutually exclusive with `cursor`. Internally this walks upstream Airbnb cursor
    pages to skip rows, so deep offsets cost N/limit upstream round-trips; cursor remains the better
    choice for deep pagination.

    When `status` is omitted, all statuses are returned (Airbnb defaults to `accepted` only on its own
    surface, but this endpoint normalises to \"all\"). Pass `?status=accepted` to scope.

    Args:
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.
        listing_id (str | Unset):
        status (ListAirbnbReservationsStatus | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbReservationListResponse
     """


    return sync_detailed(
        client=client,
cursor=cursor,
offset=offset,
limit=limit,
listing_id=listing_id,
status=status,
start_date=start_date,
end_date=end_date,
include_total=include_total,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    limit: int | Unset = 50,
    listing_id: str | Unset = UNSET,
    status: ListAirbnbReservationsStatus | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    include_total: bool | Unset = True,

) -> Response[AirbnbReservationListResponse]:
    r""" List Airbnb reservations

     Cursor-paginated list of reservations sourced directly from Airbnb. Use this when you need Airbnb-
    specific fields (guest payout split, cancellation policy snapshot) that the unified
    `/v1/reservations` endpoint flattens away.

    Walk pages with `?cursor=<pagination.next_cursor>` until `pagination.has_more` is `false`. The
    cursor is opaque — never construct or parse it client-side.

    `?offset=` is also accepted as a first-class alias for shallow paging (0..10000) — see the `offset`
    parameter below. Mutually exclusive with `cursor`. Internally this walks upstream Airbnb cursor
    pages to skip rows, so deep offsets cost N/limit upstream round-trips; cursor remains the better
    choice for deep pagination.

    When `status` is omitted, all statuses are returned (Airbnb defaults to `accepted` only on its own
    surface, but this endpoint normalises to \"all\"). Pass `?status=accepted` to scope.

    Args:
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.
        listing_id (str | Unset):
        status (ListAirbnbReservationsStatus | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbReservationListResponse]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
offset=offset,
limit=limit,
listing_id=listing_id,
status=status,
start_date=start_date,
end_date=end_date,
include_total=include_total,

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
    limit: int | Unset = 50,
    listing_id: str | Unset = UNSET,
    status: ListAirbnbReservationsStatus | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    include_total: bool | Unset = True,

) -> AirbnbReservationListResponse | None:
    r""" List Airbnb reservations

     Cursor-paginated list of reservations sourced directly from Airbnb. Use this when you need Airbnb-
    specific fields (guest payout split, cancellation policy snapshot) that the unified
    `/v1/reservations` endpoint flattens away.

    Walk pages with `?cursor=<pagination.next_cursor>` until `pagination.has_more` is `false`. The
    cursor is opaque — never construct or parse it client-side.

    `?offset=` is also accepted as a first-class alias for shallow paging (0..10000) — see the `offset`
    parameter below. Mutually exclusive with `cursor`. Internally this walks upstream Airbnb cursor
    pages to skip rows, so deep offsets cost N/limit upstream round-trips; cursor remains the better
    choice for deep pagination.

    When `status` is omitted, all statuses are returned (Airbnb defaults to `accepted` only on its own
    surface, but this endpoint normalises to \"all\"). Pass `?status=accepted` to scope.

    Args:
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 50.
        listing_id (str | Unset):
        status (ListAirbnbReservationsStatus | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbReservationListResponse
     """


    return (await asyncio_detailed(
        client=client,
cursor=cursor,
offset=offset,
limit=limit,
listing_id=listing_id,
status=status,
start_date=start_date,
end_date=end_date,
include_total=include_total,

    )).parsed
