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

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/airbnb/transactions",
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

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

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

) -> Response[Error | SyncAirbnbTransactionsResponse200]:
    """ Sync Airbnb transactions

     Refresh the Airbnb transactions mirror for this workspace by pulling from Airbnb upstream and
    upserting the breakdown that `GET` serves. Optional JSON body `{ start_date, end_date,
    transaction_type }` (`transaction_type` is `COMPLETED` or `UPCOMING`; both are synced when omitted).
    Returns `{ synced, count }`.

    Args:
        body (SyncAirbnbTransactionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyncAirbnbTransactionsResponse200]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: SyncAirbnbTransactionsBody | Unset = UNSET,

) -> Error | SyncAirbnbTransactionsResponse200 | None:
    """ Sync Airbnb transactions

     Refresh the Airbnb transactions mirror for this workspace by pulling from Airbnb upstream and
    upserting the breakdown that `GET` serves. Optional JSON body `{ start_date, end_date,
    transaction_type }` (`transaction_type` is `COMPLETED` or `UPCOMING`; both are synced when omitted).
    Returns `{ synced, count }`.

    Args:
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

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SyncAirbnbTransactionsBody | Unset = UNSET,

) -> Response[Error | SyncAirbnbTransactionsResponse200]:
    """ Sync Airbnb transactions

     Refresh the Airbnb transactions mirror for this workspace by pulling from Airbnb upstream and
    upserting the breakdown that `GET` serves. Optional JSON body `{ start_date, end_date,
    transaction_type }` (`transaction_type` is `COMPLETED` or `UPCOMING`; both are synced when omitted).
    Returns `{ synced, count }`.

    Args:
        body (SyncAirbnbTransactionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyncAirbnbTransactionsResponse200]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SyncAirbnbTransactionsBody | Unset = UNSET,

) -> Error | SyncAirbnbTransactionsResponse200 | None:
    """ Sync Airbnb transactions

     Refresh the Airbnb transactions mirror for this workspace by pulling from Airbnb upstream and
    upserting the breakdown that `GET` serves. Optional JSON body `{ start_date, end_date,
    transaction_type }` (`transaction_type` is `COMPLETED` or `UPCOMING`; both are synced when omitted).
    Returns `{ synced, count }`.

    Args:
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

    )).parsed
