from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.sync_vrbo_transactions_body import SyncVrboTransactionsBody
from ...models.sync_vrbo_transactions_response_200 import SyncVrboTransactionsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SyncVrboTransactionsBody | Unset = UNSET,
    account_id: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["account_id"] = account_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/vrbo/transactions",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SyncVrboTransactionsResponse200 | None:
    if response.status_code == 200:
        response_200 = SyncVrboTransactionsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SyncVrboTransactionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SyncVrboTransactionsBody | Unset = UNSET,
    account_id: str | Unset = UNSET,

) -> Response[Error | SyncVrboTransactionsResponse200]:
    """ Refresh the Vrbo payout ledger

     Read the ledger from Vrbo now — every connected Vrbo account, or the one in `?account_id=` — and
    keep it; then read it with GET. Body (optional): `start_date` / `end_date` (YYYY-MM-DD) for the
    deposits to read; without them, the last 12 months. The payouts Vrbo has scheduled are always read
    again. One account failing never stops the others: it carries `error` in `accounts[]`. About 15
    seconds per account.

    Args:
        account_id (str | Unset):  Example: vrbo:7001234.
        body (SyncVrboTransactionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyncVrboTransactionsResponse200]
     """


    kwargs = _get_kwargs(
        body=body,
account_id=account_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SyncVrboTransactionsBody | Unset = UNSET,
    account_id: str | Unset = UNSET,

) -> Error | SyncVrboTransactionsResponse200 | None:
    """ Refresh the Vrbo payout ledger

     Read the ledger from Vrbo now — every connected Vrbo account, or the one in `?account_id=` — and
    keep it; then read it with GET. Body (optional): `start_date` / `end_date` (YYYY-MM-DD) for the
    deposits to read; without them, the last 12 months. The payouts Vrbo has scheduled are always read
    again. One account failing never stops the others: it carries `error` in `accounts[]`. About 15
    seconds per account.

    Args:
        account_id (str | Unset):  Example: vrbo:7001234.
        body (SyncVrboTransactionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyncVrboTransactionsResponse200
     """


    return sync_detailed(
        client=client,
body=body,
account_id=account_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SyncVrboTransactionsBody | Unset = UNSET,
    account_id: str | Unset = UNSET,

) -> Response[Error | SyncVrboTransactionsResponse200]:
    """ Refresh the Vrbo payout ledger

     Read the ledger from Vrbo now — every connected Vrbo account, or the one in `?account_id=` — and
    keep it; then read it with GET. Body (optional): `start_date` / `end_date` (YYYY-MM-DD) for the
    deposits to read; without them, the last 12 months. The payouts Vrbo has scheduled are always read
    again. One account failing never stops the others: it carries `error` in `accounts[]`. About 15
    seconds per account.

    Args:
        account_id (str | Unset):  Example: vrbo:7001234.
        body (SyncVrboTransactionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyncVrboTransactionsResponse200]
     """


    kwargs = _get_kwargs(
        body=body,
account_id=account_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SyncVrboTransactionsBody | Unset = UNSET,
    account_id: str | Unset = UNSET,

) -> Error | SyncVrboTransactionsResponse200 | None:
    """ Refresh the Vrbo payout ledger

     Read the ledger from Vrbo now — every connected Vrbo account, or the one in `?account_id=` — and
    keep it; then read it with GET. Body (optional): `start_date` / `end_date` (YYYY-MM-DD) for the
    deposits to read; without them, the last 12 months. The payouts Vrbo has scheduled are always read
    again. One account failing never stops the others: it carries `error` in `accounts[]`. About 15
    seconds per account.

    Args:
        account_id (str | Unset):  Example: vrbo:7001234.
        body (SyncVrboTransactionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyncVrboTransactionsResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,
account_id=account_id,

    )).parsed
