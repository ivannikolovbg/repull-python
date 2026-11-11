from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_reservation_summary_basis import GetReservationSummaryBasis
from ...models.get_reservation_summary_response_200 import GetReservationSummaryResponse200
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    *,
    account: str | Unset = UNSET,
    from_: datetime.date,
    to: datetime.date,
    basis: GetReservationSummaryBasis | Unset = GetReservationSummaryBasis.STAY,
    group_by: str | Unset = UNSET,
    as_of: datetime.date | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    platform: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["account"] = account

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    json_basis: str | Unset = UNSET
    if not isinstance(basis, Unset):
        json_basis = basis.value

    params["basis"] = json_basis

    params["group_by"] = group_by

    json_as_of: str | Unset = UNSET
    if not isinstance(as_of, Unset):
        json_as_of = as_of.isoformat()
    params["as_of"] = json_as_of

    params["listing_id"] = listing_id

    params["platform"] = platform


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/reservations/summary",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetReservationSummaryResponse200 | None:
    if response.status_code == 200:
        response_200 = GetReservationSummaryResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetReservationSummaryResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account: str | Unset = UNSET,
    from_: datetime.date,
    to: datetime.date,
    basis: GetReservationSummaryBasis | Unset = GetReservationSummaryBasis.STAY,
    group_by: str | Unset = UNSET,
    as_of: datetime.date | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    platform: str | Unset = UNSET,

) -> Response[Error | GetReservationSummaryResponse200]:
    """ Summarize reservations for a period

     Bookings, nights, revenue, payout, average nightly rate, occupancy and cancellations for a period,
    in one small response — optionally grouped by `month`, `listing` and/or `channel`. Use it for
    reporting instead of paging through `GET /v1/reservations`.

    **Counting (`basis`):** `stay` (default) counts the nights that fall inside `from`–`to` and splits
    each reservation’s money across its nights, so a stay crossing the window or a month edge brings
    only its share. `check_in` and `booked` count whole reservations by their check-in or booking date.

    **Pace (`as_of`):** keeps only what was on the books at the end of that day — booked by then and not
    yet cancelled. To compare the next three months with the same months last year like for like, ask
    for last year’s window with `as_of` set to today’s date one year ago.

    Owner stays are reported apart and never count as revenue or occupancy. Pending requests are counted
    in `pending` only. Reservations on inactive listings are left out.

    Args:
        account (str | Unset):  Example: airbnb:79730216.
        from_ (datetime.date):  Example: 2026-11-10.
        to (datetime.date):  Example: 2027-02-09.
        basis (GetReservationSummaryBasis | Unset):  Default: GetReservationSummaryBasis.STAY.
        group_by (str | Unset):  Example: month,listing.
        as_of (datetime.date | Unset):  Example: 2025-11-10.
        listing_id (int | Unset):
        platform (str | Unset):  Example: airbnb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetReservationSummaryResponse200]
     """


    kwargs = _get_kwargs(
        account=account,
from_=from_,
to=to,
basis=basis,
group_by=group_by,
as_of=as_of,
listing_id=listing_id,
platform=platform,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    account: str | Unset = UNSET,
    from_: datetime.date,
    to: datetime.date,
    basis: GetReservationSummaryBasis | Unset = GetReservationSummaryBasis.STAY,
    group_by: str | Unset = UNSET,
    as_of: datetime.date | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    platform: str | Unset = UNSET,

) -> Error | GetReservationSummaryResponse200 | None:
    """ Summarize reservations for a period

     Bookings, nights, revenue, payout, average nightly rate, occupancy and cancellations for a period,
    in one small response — optionally grouped by `month`, `listing` and/or `channel`. Use it for
    reporting instead of paging through `GET /v1/reservations`.

    **Counting (`basis`):** `stay` (default) counts the nights that fall inside `from`–`to` and splits
    each reservation’s money across its nights, so a stay crossing the window or a month edge brings
    only its share. `check_in` and `booked` count whole reservations by their check-in or booking date.

    **Pace (`as_of`):** keeps only what was on the books at the end of that day — booked by then and not
    yet cancelled. To compare the next three months with the same months last year like for like, ask
    for last year’s window with `as_of` set to today’s date one year ago.

    Owner stays are reported apart and never count as revenue or occupancy. Pending requests are counted
    in `pending` only. Reservations on inactive listings are left out.

    Args:
        account (str | Unset):  Example: airbnb:79730216.
        from_ (datetime.date):  Example: 2026-11-10.
        to (datetime.date):  Example: 2027-02-09.
        basis (GetReservationSummaryBasis | Unset):  Default: GetReservationSummaryBasis.STAY.
        group_by (str | Unset):  Example: month,listing.
        as_of (datetime.date | Unset):  Example: 2025-11-10.
        listing_id (int | Unset):
        platform (str | Unset):  Example: airbnb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetReservationSummaryResponse200
     """


    return sync_detailed(
        client=client,
account=account,
from_=from_,
to=to,
basis=basis,
group_by=group_by,
as_of=as_of,
listing_id=listing_id,
platform=platform,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account: str | Unset = UNSET,
    from_: datetime.date,
    to: datetime.date,
    basis: GetReservationSummaryBasis | Unset = GetReservationSummaryBasis.STAY,
    group_by: str | Unset = UNSET,
    as_of: datetime.date | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    platform: str | Unset = UNSET,

) -> Response[Error | GetReservationSummaryResponse200]:
    """ Summarize reservations for a period

     Bookings, nights, revenue, payout, average nightly rate, occupancy and cancellations for a period,
    in one small response — optionally grouped by `month`, `listing` and/or `channel`. Use it for
    reporting instead of paging through `GET /v1/reservations`.

    **Counting (`basis`):** `stay` (default) counts the nights that fall inside `from`–`to` and splits
    each reservation’s money across its nights, so a stay crossing the window or a month edge brings
    only its share. `check_in` and `booked` count whole reservations by their check-in or booking date.

    **Pace (`as_of`):** keeps only what was on the books at the end of that day — booked by then and not
    yet cancelled. To compare the next three months with the same months last year like for like, ask
    for last year’s window with `as_of` set to today’s date one year ago.

    Owner stays are reported apart and never count as revenue or occupancy. Pending requests are counted
    in `pending` only. Reservations on inactive listings are left out.

    Args:
        account (str | Unset):  Example: airbnb:79730216.
        from_ (datetime.date):  Example: 2026-11-10.
        to (datetime.date):  Example: 2027-02-09.
        basis (GetReservationSummaryBasis | Unset):  Default: GetReservationSummaryBasis.STAY.
        group_by (str | Unset):  Example: month,listing.
        as_of (datetime.date | Unset):  Example: 2025-11-10.
        listing_id (int | Unset):
        platform (str | Unset):  Example: airbnb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetReservationSummaryResponse200]
     """


    kwargs = _get_kwargs(
        account=account,
from_=from_,
to=to,
basis=basis,
group_by=group_by,
as_of=as_of,
listing_id=listing_id,
platform=platform,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account: str | Unset = UNSET,
    from_: datetime.date,
    to: datetime.date,
    basis: GetReservationSummaryBasis | Unset = GetReservationSummaryBasis.STAY,
    group_by: str | Unset = UNSET,
    as_of: datetime.date | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    platform: str | Unset = UNSET,

) -> Error | GetReservationSummaryResponse200 | None:
    """ Summarize reservations for a period

     Bookings, nights, revenue, payout, average nightly rate, occupancy and cancellations for a period,
    in one small response — optionally grouped by `month`, `listing` and/or `channel`. Use it for
    reporting instead of paging through `GET /v1/reservations`.

    **Counting (`basis`):** `stay` (default) counts the nights that fall inside `from`–`to` and splits
    each reservation’s money across its nights, so a stay crossing the window or a month edge brings
    only its share. `check_in` and `booked` count whole reservations by their check-in or booking date.

    **Pace (`as_of`):** keeps only what was on the books at the end of that day — booked by then and not
    yet cancelled. To compare the next three months with the same months last year like for like, ask
    for last year’s window with `as_of` set to today’s date one year ago.

    Owner stays are reported apart and never count as revenue or occupancy. Pending requests are counted
    in `pending` only. Reservations on inactive listings are left out.

    Args:
        account (str | Unset):  Example: airbnb:79730216.
        from_ (datetime.date):  Example: 2026-11-10.
        to (datetime.date):  Example: 2027-02-09.
        basis (GetReservationSummaryBasis | Unset):  Default: GetReservationSummaryBasis.STAY.
        group_by (str | Unset):  Example: month,listing.
        as_of (datetime.date | Unset):  Example: 2025-11-10.
        listing_id (int | Unset):
        platform (str | Unset):  Example: airbnb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetReservationSummaryResponse200
     """


    return (await asyncio_detailed(
        client=client,
account=account,
from_=from_,
to=to,
basis=basis,
group_by=group_by,
as_of=as_of,
listing_id=listing_id,
platform=platform,

    )).parsed
