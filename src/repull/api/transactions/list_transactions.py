from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_transactions_platform import ListTransactionsPlatform
from ...models.list_transactions_response_200 import ListTransactionsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    platform: ListTransactionsPlatform | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    is_payout: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_platform: str | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform.value

    params["platform"] = json_platform

    params["type"] = type_

    params["status"] = status

    params["is_payout"] = is_payout

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/transactions",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListTransactionsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListTransactionsResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListTransactionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform: ListTransactionsPlatform | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    is_payout: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[ListTransactionsResponse200]:
    """ List transactions & payments (unified ledger)

     Every channel's money in one ledger: payouts that reached the host, reservation charges, refunds and
    adjustments, across Airbnb, Booking.com and Vrbo. Each row carries a normalized `platform` —
    `booking` always means Booking.com however the account was connected (official API or extranet);
    there is no `booking_extranet`, and `?platform=booking` matches all of them. A payout row's `amount`
    is the net the host received; `grossAmount` is what the guest paid and `fees` the deductions
    (commission, payments service fee, processing fee). Cursor-paginated, newest first.

    Args:
        platform (ListTransactionsPlatform | Unset):
        type_ (str | Unset):
        status (str | Unset):
        is_payout (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTransactionsResponse200]
     """


    kwargs = _get_kwargs(
        platform=platform,
type_=type_,
status=status,
is_payout=is_payout,
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
    platform: ListTransactionsPlatform | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    is_payout: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> ListTransactionsResponse200 | None:
    """ List transactions & payments (unified ledger)

     Every channel's money in one ledger: payouts that reached the host, reservation charges, refunds and
    adjustments, across Airbnb, Booking.com and Vrbo. Each row carries a normalized `platform` —
    `booking` always means Booking.com however the account was connected (official API or extranet);
    there is no `booking_extranet`, and `?platform=booking` matches all of them. A payout row's `amount`
    is the net the host received; `grossAmount` is what the guest paid and `fees` the deductions
    (commission, payments service fee, processing fee). Cursor-paginated, newest first.

    Args:
        platform (ListTransactionsPlatform | Unset):
        type_ (str | Unset):
        status (str | Unset):
        is_payout (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTransactionsResponse200
     """


    return sync_detailed(
        client=client,
platform=platform,
type_=type_,
status=status,
is_payout=is_payout,
limit=limit,
cursor=cursor,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    platform: ListTransactionsPlatform | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    is_payout: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[ListTransactionsResponse200]:
    """ List transactions & payments (unified ledger)

     Every channel's money in one ledger: payouts that reached the host, reservation charges, refunds and
    adjustments, across Airbnb, Booking.com and Vrbo. Each row carries a normalized `platform` —
    `booking` always means Booking.com however the account was connected (official API or extranet);
    there is no `booking_extranet`, and `?platform=booking` matches all of them. A payout row's `amount`
    is the net the host received; `grossAmount` is what the guest paid and `fees` the deductions
    (commission, payments service fee, processing fee). Cursor-paginated, newest first.

    Args:
        platform (ListTransactionsPlatform | Unset):
        type_ (str | Unset):
        status (str | Unset):
        is_payout (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTransactionsResponse200]
     """


    kwargs = _get_kwargs(
        platform=platform,
type_=type_,
status=status,
is_payout=is_payout,
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
    platform: ListTransactionsPlatform | Unset = UNSET,
    type_: str | Unset = UNSET,
    status: str | Unset = UNSET,
    is_payout: bool | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> ListTransactionsResponse200 | None:
    """ List transactions & payments (unified ledger)

     Every channel's money in one ledger: payouts that reached the host, reservation charges, refunds and
    adjustments, across Airbnb, Booking.com and Vrbo. Each row carries a normalized `platform` —
    `booking` always means Booking.com however the account was connected (official API or extranet);
    there is no `booking_extranet`, and `?platform=booking` matches all of them. A payout row's `amount`
    is the net the host received; `grossAmount` is what the guest paid and `fees` the deductions
    (commission, payments service fee, processing fee). Cursor-paginated, newest first.

    Args:
        platform (ListTransactionsPlatform | Unset):
        type_ (str | Unset):
        status (str | Unset):
        is_payout (bool | Unset):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTransactionsResponse200
     """


    return (await asyncio_detailed(
        client=client,
platform=platform,
type_=type_,
status=status,
is_payout=is_payout,
limit=limit,
cursor=cursor,

    )).parsed
