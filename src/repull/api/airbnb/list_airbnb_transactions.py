from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_airbnb_transactions_response_200 import ListAirbnbTransactionsResponse200
from ...models.list_airbnb_transactions_status import ListAirbnbTransactionsStatus
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    *,
    account_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    status: ListAirbnbTransactionsStatus | Unset = UNSET,
    type_: str | Unset = UNSET,
    payout_id: str | Unset = UNSET,
    confirmation_code: str | Unset = UNSET,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["account_id"] = account_id

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["type"] = type_

    params["payout_id"] = payout_id

    params["confirmation_code"] = confirmation_code

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/transactions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListAirbnbTransactionsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAirbnbTransactionsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListAirbnbTransactionsResponse200]:
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
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    status: ListAirbnbTransactionsStatus | Unset = UNSET,
    type_: str | Unset = UNSET,
    payout_id: str | Unset = UNSET,
    confirmation_code: str | Unset = UNSET,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,

) -> Response[Error | ListAirbnbTransactionsResponse200]:
    """ List Airbnb transactions (settlement ledger)

     The Airbnb settlement ledger for this workspace: every payout Airbnb sent to the host, each followed
    by the lines it paid — reservations and their installments, adjustments, resolution payouts and
    adjustments, cancellation fees. A payout's lines' signed `amount`s sum to its `payout.paidOutAmount`
    exactly, negative lines included (an adjustment offset against a later payout appears under that
    payout). `status: UPCOMING` lines are expected earnings not paid out yet; they belong to no payout.

    **Ids are stable.** Airbnb sends no line id and no payout id on lines, so Repull derives them
    deterministically: a Payout row's id is Airbnb's payout id; a line's is
    `<payoutId>:<type>:<confirmationCode>:<n>`. The same line has the same id on every refresh and every
    page, so you can upsert on `transactionId`. A payout that nets to $0.00 has no Airbnb id; it gets a
    derived `Z-<date>-<hash>` id with `payout.payoutIdSynthetic: true`.

    **Order:** newest first by the payout's date; each Payout row is followed by its lines in Airbnb's
    order (`payout.lineIndex`).

    **Dates:** `start_date` / `end_date` match the payout's date for settled lines (a line can be dated
    the day before its payout, and is still returned with it) and the line's own date for UPCOMING
    lines.

    **Pure DB read** — never calls Airbnb. Refresh with `POST` on this path. `dataFreshness` reports
    when each account's ledger was last refreshed.

    Lines on listings that are inactive in Repull are included and flagged `onInactiveListing: true`, so
    every payout reconciles. Lines Repull cannot match to a reservation keep `reservationId: null`.

    **Not in Airbnb's transaction history** (listed in `unavailableFields`): taxes Airbnb collects and
    remits itself, and the guest-paid total (see the reservation's financial breakdown); pass-through
    occupancy tax paid to the host does appear, as its own `Pass Through Tot` lines, the original line a
    refund or reversal reverses (it names the stay and the resolution), and currency-conversion amounts
    (only the payout currency is reported).

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        status (ListAirbnbTransactionsStatus | Unset):
        type_ (str | Unset):
        payout_id (str | Unset):
        confirmation_code (str | Unset):
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbTransactionsResponse200]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
start_date=start_date,
end_date=end_date,
status=status,
type_=type_,
payout_id=payout_id,
confirmation_code=confirmation_code,
limit=limit,
cursor=cursor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    status: ListAirbnbTransactionsStatus | Unset = UNSET,
    type_: str | Unset = UNSET,
    payout_id: str | Unset = UNSET,
    confirmation_code: str | Unset = UNSET,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,

) -> Error | ListAirbnbTransactionsResponse200 | None:
    """ List Airbnb transactions (settlement ledger)

     The Airbnb settlement ledger for this workspace: every payout Airbnb sent to the host, each followed
    by the lines it paid — reservations and their installments, adjustments, resolution payouts and
    adjustments, cancellation fees. A payout's lines' signed `amount`s sum to its `payout.paidOutAmount`
    exactly, negative lines included (an adjustment offset against a later payout appears under that
    payout). `status: UPCOMING` lines are expected earnings not paid out yet; they belong to no payout.

    **Ids are stable.** Airbnb sends no line id and no payout id on lines, so Repull derives them
    deterministically: a Payout row's id is Airbnb's payout id; a line's is
    `<payoutId>:<type>:<confirmationCode>:<n>`. The same line has the same id on every refresh and every
    page, so you can upsert on `transactionId`. A payout that nets to $0.00 has no Airbnb id; it gets a
    derived `Z-<date>-<hash>` id with `payout.payoutIdSynthetic: true`.

    **Order:** newest first by the payout's date; each Payout row is followed by its lines in Airbnb's
    order (`payout.lineIndex`).

    **Dates:** `start_date` / `end_date` match the payout's date for settled lines (a line can be dated
    the day before its payout, and is still returned with it) and the line's own date for UPCOMING
    lines.

    **Pure DB read** — never calls Airbnb. Refresh with `POST` on this path. `dataFreshness` reports
    when each account's ledger was last refreshed.

    Lines on listings that are inactive in Repull are included and flagged `onInactiveListing: true`, so
    every payout reconciles. Lines Repull cannot match to a reservation keep `reservationId: null`.

    **Not in Airbnb's transaction history** (listed in `unavailableFields`): taxes Airbnb collects and
    remits itself, and the guest-paid total (see the reservation's financial breakdown); pass-through
    occupancy tax paid to the host does appear, as its own `Pass Through Tot` lines, the original line a
    refund or reversal reverses (it names the stay and the resolution), and currency-conversion amounts
    (only the payout currency is reported).

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        status (ListAirbnbTransactionsStatus | Unset):
        type_ (str | Unset):
        payout_id (str | Unset):
        confirmation_code (str | Unset):
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbTransactionsResponse200
     """


    return sync_detailed(
        client=client,
account_id=account_id,
start_date=start_date,
end_date=end_date,
status=status,
type_=type_,
payout_id=payout_id,
confirmation_code=confirmation_code,
limit=limit,
cursor=cursor,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    status: ListAirbnbTransactionsStatus | Unset = UNSET,
    type_: str | Unset = UNSET,
    payout_id: str | Unset = UNSET,
    confirmation_code: str | Unset = UNSET,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,

) -> Response[Error | ListAirbnbTransactionsResponse200]:
    """ List Airbnb transactions (settlement ledger)

     The Airbnb settlement ledger for this workspace: every payout Airbnb sent to the host, each followed
    by the lines it paid — reservations and their installments, adjustments, resolution payouts and
    adjustments, cancellation fees. A payout's lines' signed `amount`s sum to its `payout.paidOutAmount`
    exactly, negative lines included (an adjustment offset against a later payout appears under that
    payout). `status: UPCOMING` lines are expected earnings not paid out yet; they belong to no payout.

    **Ids are stable.** Airbnb sends no line id and no payout id on lines, so Repull derives them
    deterministically: a Payout row's id is Airbnb's payout id; a line's is
    `<payoutId>:<type>:<confirmationCode>:<n>`. The same line has the same id on every refresh and every
    page, so you can upsert on `transactionId`. A payout that nets to $0.00 has no Airbnb id; it gets a
    derived `Z-<date>-<hash>` id with `payout.payoutIdSynthetic: true`.

    **Order:** newest first by the payout's date; each Payout row is followed by its lines in Airbnb's
    order (`payout.lineIndex`).

    **Dates:** `start_date` / `end_date` match the payout's date for settled lines (a line can be dated
    the day before its payout, and is still returned with it) and the line's own date for UPCOMING
    lines.

    **Pure DB read** — never calls Airbnb. Refresh with `POST` on this path. `dataFreshness` reports
    when each account's ledger was last refreshed.

    Lines on listings that are inactive in Repull are included and flagged `onInactiveListing: true`, so
    every payout reconciles. Lines Repull cannot match to a reservation keep `reservationId: null`.

    **Not in Airbnb's transaction history** (listed in `unavailableFields`): taxes Airbnb collects and
    remits itself, and the guest-paid total (see the reservation's financial breakdown); pass-through
    occupancy tax paid to the host does appear, as its own `Pass Through Tot` lines, the original line a
    refund or reversal reverses (it names the stay and the resolution), and currency-conversion amounts
    (only the payout currency is reported).

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        status (ListAirbnbTransactionsStatus | Unset):
        type_ (str | Unset):
        payout_id (str | Unset):
        confirmation_code (str | Unset):
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbTransactionsResponse200]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
start_date=start_date,
end_date=end_date,
status=status,
type_=type_,
payout_id=payout_id,
confirmation_code=confirmation_code,
limit=limit,
cursor=cursor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    status: ListAirbnbTransactionsStatus | Unset = UNSET,
    type_: str | Unset = UNSET,
    payout_id: str | Unset = UNSET,
    confirmation_code: str | Unset = UNSET,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,

) -> Error | ListAirbnbTransactionsResponse200 | None:
    """ List Airbnb transactions (settlement ledger)

     The Airbnb settlement ledger for this workspace: every payout Airbnb sent to the host, each followed
    by the lines it paid — reservations and their installments, adjustments, resolution payouts and
    adjustments, cancellation fees. A payout's lines' signed `amount`s sum to its `payout.paidOutAmount`
    exactly, negative lines included (an adjustment offset against a later payout appears under that
    payout). `status: UPCOMING` lines are expected earnings not paid out yet; they belong to no payout.

    **Ids are stable.** Airbnb sends no line id and no payout id on lines, so Repull derives them
    deterministically: a Payout row's id is Airbnb's payout id; a line's is
    `<payoutId>:<type>:<confirmationCode>:<n>`. The same line has the same id on every refresh and every
    page, so you can upsert on `transactionId`. A payout that nets to $0.00 has no Airbnb id; it gets a
    derived `Z-<date>-<hash>` id with `payout.payoutIdSynthetic: true`.

    **Order:** newest first by the payout's date; each Payout row is followed by its lines in Airbnb's
    order (`payout.lineIndex`).

    **Dates:** `start_date` / `end_date` match the payout's date for settled lines (a line can be dated
    the day before its payout, and is still returned with it) and the line's own date for UPCOMING
    lines.

    **Pure DB read** — never calls Airbnb. Refresh with `POST` on this path. `dataFreshness` reports
    when each account's ledger was last refreshed.

    Lines on listings that are inactive in Repull are included and flagged `onInactiveListing: true`, so
    every payout reconciles. Lines Repull cannot match to a reservation keep `reservationId: null`.

    **Not in Airbnb's transaction history** (listed in `unavailableFields`): taxes Airbnb collects and
    remits itself, and the guest-paid total (see the reservation's financial breakdown); pass-through
    occupancy tax paid to the host does appear, as its own `Pass Through Tot` lines, the original line a
    refund or reversal reverses (it names the stay and the resolution), and currency-conversion amounts
    (only the payout currency is reported).

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        status (ListAirbnbTransactionsStatus | Unset):
        type_ (str | Unset):
        payout_id (str | Unset):
        confirmation_code (str | Unset):
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbTransactionsResponse200
     """


    return (await asyncio_detailed(
        client=client,
account_id=account_id,
start_date=start_date,
end_date=end_date,
status=status,
type_=type_,
payout_id=payout_id,
confirmation_code=confirmation_code,
limit=limit,
cursor=cursor,

    )).parsed
