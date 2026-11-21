from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_vrbo_transactions_response_200 import ListVrboTransactionsResponse200
from ...models.list_vrbo_transactions_status import ListVrboTransactionsStatus
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    *,
    account_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    status: ListVrboTransactionsStatus | Unset = UNSET,
    type_: str | Unset = UNSET,
    payout_id: str | Unset = UNSET,
    confirmation_code: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,

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

    params["cursor"] = cursor

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/vrbo/transactions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListVrboTransactionsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListVrboTransactionsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListVrboTransactionsResponse200]:
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
    status: ListVrboTransactionsStatus | Unset = UNSET,
    type_: str | Unset = UNSET,
    payout_id: str | Unset = UNSET,
    confirmation_code: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,

) -> Response[Error | ListVrboTransactionsResponse200]:
    """ List Vrbo transactions (payout ledger)

     The Vrbo payout ledger for this workspace — the counterpart of `GET
    /v1/channels/airbnb/transactions`: every bank deposit Vrbo made to the host, each followed by the
    bookings it paid. A deposit's lines' signed `amount`s sum to its `payout.paidOutAmount` exactly; a
    negative line (`type: Adjustment`) is money taken back from that deposit. `status: UPCOMING` lines
    are payouts Vrbo has scheduled and not made yet, with Vrbo's `upcomingStatus` (`Scheduled`,
    `Blocked`).

    **Ids are stable**, so you can upsert on `transactionId`: a Payout row's id is Vrbo's deposit
    reference number; a line's is `<reference>:<confirmationCode>:<n>`.

    **Order:** newest deposit first, each followed by its lines in Vrbo's order (`payout.lineIndex`).
    `start_date` / `end_date` match the deposit's date (a scheduled line's estimated payout date).

    **From Repull's copy.** The ledger is read from the Vrbo account (the last 12 months of deposits,
    and the payouts scheduled for the next 6) and kept: a read answers from it at once. A copy over a
    day old — or never filled — answers and is refreshed in the background (`dataFreshness.reason`:
    `refreshing` / `never_synced`); `POST` refreshes it now.

    Lines on listings that are inactive in Repull are included and flagged `onInactiveListing: true`, so
    every deposit reconciles. **Not in Vrbo's payout reports** (`unavailableFields`): the fee split per
    booking, taxes, and the stay's nights and dates — see the reservation for those.

    Args:
        account_id (str | Unset):  Example: vrbo:7001234.
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        status (ListVrboTransactionsStatus | Unset):
        type_ (str | Unset):  Example: Payout.
        payout_id (str | Unset):
        confirmation_code (str | Unset):  Example: HA-8K2P3Q.
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListVrboTransactionsResponse200]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
start_date=start_date,
end_date=end_date,
status=status,
type_=type_,
payout_id=payout_id,
confirmation_code=confirmation_code,
cursor=cursor,
limit=limit,

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
    status: ListVrboTransactionsStatus | Unset = UNSET,
    type_: str | Unset = UNSET,
    payout_id: str | Unset = UNSET,
    confirmation_code: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,

) -> Error | ListVrboTransactionsResponse200 | None:
    """ List Vrbo transactions (payout ledger)

     The Vrbo payout ledger for this workspace — the counterpart of `GET
    /v1/channels/airbnb/transactions`: every bank deposit Vrbo made to the host, each followed by the
    bookings it paid. A deposit's lines' signed `amount`s sum to its `payout.paidOutAmount` exactly; a
    negative line (`type: Adjustment`) is money taken back from that deposit. `status: UPCOMING` lines
    are payouts Vrbo has scheduled and not made yet, with Vrbo's `upcomingStatus` (`Scheduled`,
    `Blocked`).

    **Ids are stable**, so you can upsert on `transactionId`: a Payout row's id is Vrbo's deposit
    reference number; a line's is `<reference>:<confirmationCode>:<n>`.

    **Order:** newest deposit first, each followed by its lines in Vrbo's order (`payout.lineIndex`).
    `start_date` / `end_date` match the deposit's date (a scheduled line's estimated payout date).

    **From Repull's copy.** The ledger is read from the Vrbo account (the last 12 months of deposits,
    and the payouts scheduled for the next 6) and kept: a read answers from it at once. A copy over a
    day old — or never filled — answers and is refreshed in the background (`dataFreshness.reason`:
    `refreshing` / `never_synced`); `POST` refreshes it now.

    Lines on listings that are inactive in Repull are included and flagged `onInactiveListing: true`, so
    every deposit reconciles. **Not in Vrbo's payout reports** (`unavailableFields`): the fee split per
    booking, taxes, and the stay's nights and dates — see the reservation for those.

    Args:
        account_id (str | Unset):  Example: vrbo:7001234.
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        status (ListVrboTransactionsStatus | Unset):
        type_ (str | Unset):  Example: Payout.
        payout_id (str | Unset):
        confirmation_code (str | Unset):  Example: HA-8K2P3Q.
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListVrboTransactionsResponse200
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
cursor=cursor,
limit=limit,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    status: ListVrboTransactionsStatus | Unset = UNSET,
    type_: str | Unset = UNSET,
    payout_id: str | Unset = UNSET,
    confirmation_code: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,

) -> Response[Error | ListVrboTransactionsResponse200]:
    """ List Vrbo transactions (payout ledger)

     The Vrbo payout ledger for this workspace — the counterpart of `GET
    /v1/channels/airbnb/transactions`: every bank deposit Vrbo made to the host, each followed by the
    bookings it paid. A deposit's lines' signed `amount`s sum to its `payout.paidOutAmount` exactly; a
    negative line (`type: Adjustment`) is money taken back from that deposit. `status: UPCOMING` lines
    are payouts Vrbo has scheduled and not made yet, with Vrbo's `upcomingStatus` (`Scheduled`,
    `Blocked`).

    **Ids are stable**, so you can upsert on `transactionId`: a Payout row's id is Vrbo's deposit
    reference number; a line's is `<reference>:<confirmationCode>:<n>`.

    **Order:** newest deposit first, each followed by its lines in Vrbo's order (`payout.lineIndex`).
    `start_date` / `end_date` match the deposit's date (a scheduled line's estimated payout date).

    **From Repull's copy.** The ledger is read from the Vrbo account (the last 12 months of deposits,
    and the payouts scheduled for the next 6) and kept: a read answers from it at once. A copy over a
    day old — or never filled — answers and is refreshed in the background (`dataFreshness.reason`:
    `refreshing` / `never_synced`); `POST` refreshes it now.

    Lines on listings that are inactive in Repull are included and flagged `onInactiveListing: true`, so
    every deposit reconciles. **Not in Vrbo's payout reports** (`unavailableFields`): the fee split per
    booking, taxes, and the stay's nights and dates — see the reservation for those.

    Args:
        account_id (str | Unset):  Example: vrbo:7001234.
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        status (ListVrboTransactionsStatus | Unset):
        type_ (str | Unset):  Example: Payout.
        payout_id (str | Unset):
        confirmation_code (str | Unset):  Example: HA-8K2P3Q.
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListVrboTransactionsResponse200]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
start_date=start_date,
end_date=end_date,
status=status,
type_=type_,
payout_id=payout_id,
confirmation_code=confirmation_code,
cursor=cursor,
limit=limit,

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
    status: ListVrboTransactionsStatus | Unset = UNSET,
    type_: str | Unset = UNSET,
    payout_id: str | Unset = UNSET,
    confirmation_code: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 100,

) -> Error | ListVrboTransactionsResponse200 | None:
    """ List Vrbo transactions (payout ledger)

     The Vrbo payout ledger for this workspace — the counterpart of `GET
    /v1/channels/airbnb/transactions`: every bank deposit Vrbo made to the host, each followed by the
    bookings it paid. A deposit's lines' signed `amount`s sum to its `payout.paidOutAmount` exactly; a
    negative line (`type: Adjustment`) is money taken back from that deposit. `status: UPCOMING` lines
    are payouts Vrbo has scheduled and not made yet, with Vrbo's `upcomingStatus` (`Scheduled`,
    `Blocked`).

    **Ids are stable**, so you can upsert on `transactionId`: a Payout row's id is Vrbo's deposit
    reference number; a line's is `<reference>:<confirmationCode>:<n>`.

    **Order:** newest deposit first, each followed by its lines in Vrbo's order (`payout.lineIndex`).
    `start_date` / `end_date` match the deposit's date (a scheduled line's estimated payout date).

    **From Repull's copy.** The ledger is read from the Vrbo account (the last 12 months of deposits,
    and the payouts scheduled for the next 6) and kept: a read answers from it at once. A copy over a
    day old — or never filled — answers and is refreshed in the background (`dataFreshness.reason`:
    `refreshing` / `never_synced`); `POST` refreshes it now.

    Lines on listings that are inactive in Repull are included and flagged `onInactiveListing: true`, so
    every deposit reconciles. **Not in Vrbo's payout reports** (`unavailableFields`): the fee split per
    booking, taxes, and the stay's nights and dates — see the reservation for those.

    Args:
        account_id (str | Unset):  Example: vrbo:7001234.
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        status (ListVrboTransactionsStatus | Unset):
        type_ (str | Unset):  Example: Payout.
        payout_id (str | Unset):
        confirmation_code (str | Unset):  Example: HA-8K2P3Q.
        cursor (str | Unset):
        limit (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListVrboTransactionsResponse200
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
cursor=cursor,
limit=limit,

    )).parsed
