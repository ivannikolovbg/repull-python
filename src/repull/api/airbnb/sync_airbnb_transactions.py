from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.sync_airbnb_transactions_body import SyncAirbnbTransactionsBody
from ...models.sync_airbnb_transactions_response_200 import SyncAirbnbTransactionsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: SyncAirbnbTransactionsBody | Unset = UNSET,
    account_id: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["account_id"] = account_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/airbnb/transactions",
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SyncAirbnbTransactionsResponse200 | None:
    if response.status_code == 200:
        response_200 = SyncAirbnbTransactionsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SyncAirbnbTransactionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SyncAirbnbTransactionsBody | Unset = UNSET,
    account_id: str | Unset = UNSET,

) -> Response[Error | SyncAirbnbTransactionsResponse200]:
    """ Refresh Airbnb transactions

     Pull the transaction history from Airbnb into the ledger `GET` serves. Every connected Airbnb
    account is refreshed, or only `?account_id=`. Without dates: settled lines from the last 12 months
    and the forecast for the next 12. Safe to repeat: settled lines are upserted on their stable ids,
    never duplicated or removed; the UPCOMING forecast inside the fetched window is replaced, so a line
    that has since been paid out moves to its payout. Each account reports its own outcome in
    `accounts[]`: one account Airbnb refuses (a revoked host, a listing Airbnb no longer serves) is
    reported there with Airbnb's reason and does not stop the others. When every account fails, the
    response is Airbnb's answer with its usual code.

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.
        body (SyncAirbnbTransactionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyncAirbnbTransactionsResponse200]
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
    body: SyncAirbnbTransactionsBody | Unset = UNSET,
    account_id: str | Unset = UNSET,

) -> Error | SyncAirbnbTransactionsResponse200 | None:
    """ Refresh Airbnb transactions

     Pull the transaction history from Airbnb into the ledger `GET` serves. Every connected Airbnb
    account is refreshed, or only `?account_id=`. Without dates: settled lines from the last 12 months
    and the forecast for the next 12. Safe to repeat: settled lines are upserted on their stable ids,
    never duplicated or removed; the UPCOMING forecast inside the fetched window is replaced, so a line
    that has since been paid out moves to its payout. Each account reports its own outcome in
    `accounts[]`: one account Airbnb refuses (a revoked host, a listing Airbnb no longer serves) is
    reported there with Airbnb's reason and does not stop the others. When every account fails, the
    response is Airbnb's answer with its usual code.

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.
        body (SyncAirbnbTransactionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyncAirbnbTransactionsResponse200
     """


    return sync_detailed(
        client=client,
body=body,
account_id=account_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SyncAirbnbTransactionsBody | Unset = UNSET,
    account_id: str | Unset = UNSET,

) -> Response[Error | SyncAirbnbTransactionsResponse200]:
    """ Refresh Airbnb transactions

     Pull the transaction history from Airbnb into the ledger `GET` serves. Every connected Airbnb
    account is refreshed, or only `?account_id=`. Without dates: settled lines from the last 12 months
    and the forecast for the next 12. Safe to repeat: settled lines are upserted on their stable ids,
    never duplicated or removed; the UPCOMING forecast inside the fetched window is replaced, so a line
    that has since been paid out moves to its payout. Each account reports its own outcome in
    `accounts[]`: one account Airbnb refuses (a revoked host, a listing Airbnb no longer serves) is
    reported there with Airbnb's reason and does not stop the others. When every account fails, the
    response is Airbnb's answer with its usual code.

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.
        body (SyncAirbnbTransactionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyncAirbnbTransactionsResponse200]
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
    body: SyncAirbnbTransactionsBody | Unset = UNSET,
    account_id: str | Unset = UNSET,

) -> Error | SyncAirbnbTransactionsResponse200 | None:
    """ Refresh Airbnb transactions

     Pull the transaction history from Airbnb into the ledger `GET` serves. Every connected Airbnb
    account is refreshed, or only `?account_id=`. Without dates: settled lines from the last 12 months
    and the forecast for the next 12. Safe to repeat: settled lines are upserted on their stable ids,
    never duplicated or removed; the UPCOMING forecast inside the fetched window is replaced, so a line
    that has since been paid out moves to its payout. Each account reports its own outcome in
    `accounts[]`: one account Airbnb refuses (a revoked host, a listing Airbnb no longer serves) is
    reported there with Airbnb's reason and does not stop the others. When every account fails, the
    response is Airbnb's answer with its usual code.

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.
        body (SyncAirbnbTransactionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyncAirbnbTransactionsResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,
account_id=account_id,

    )).parsed
