from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_usage_summary_range import GetUsageSummaryRange
from ...models.get_usage_summary_response_200 import GetUsageSummaryResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    range_: GetUsageSummaryRange | Unset = GetUsageSummaryRange.VALUE_1,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_range_: str | Unset = UNSET
    if not isinstance(range_, Unset):
        json_range_ = range_.value

    params["range"] = json_range_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/usage/summary",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetUsageSummaryResponse200 | None:
    if response.status_code == 200:
        response_200 = GetUsageSummaryResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetUsageSummaryResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    range_: GetUsageSummaryRange | Unset = GetUsageSummaryRange.VALUE_1,

) -> Response[Error | GetUsageSummaryResponse200]:
    """ Get usage summary

     Aggregated usage over the requested `range` — tier + plan limits, quota used/remaining, next reset,
    a per-operation breakdown (request/error counts, error rate, avg latency), a daily timeline, status-
    class distribution, and range totals.

    Args:
        range_ (GetUsageSummaryRange | Unset):  Default: GetUsageSummaryRange.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetUsageSummaryResponse200]
     """


    kwargs = _get_kwargs(
        range_=range_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    range_: GetUsageSummaryRange | Unset = GetUsageSummaryRange.VALUE_1,

) -> Error | GetUsageSummaryResponse200 | None:
    """ Get usage summary

     Aggregated usage over the requested `range` — tier + plan limits, quota used/remaining, next reset,
    a per-operation breakdown (request/error counts, error rate, avg latency), a daily timeline, status-
    class distribution, and range totals.

    Args:
        range_ (GetUsageSummaryRange | Unset):  Default: GetUsageSummaryRange.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetUsageSummaryResponse200
     """


    return sync_detailed(
        client=client,
range_=range_,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    range_: GetUsageSummaryRange | Unset = GetUsageSummaryRange.VALUE_1,

) -> Response[Error | GetUsageSummaryResponse200]:
    """ Get usage summary

     Aggregated usage over the requested `range` — tier + plan limits, quota used/remaining, next reset,
    a per-operation breakdown (request/error counts, error rate, avg latency), a daily timeline, status-
    class distribution, and range totals.

    Args:
        range_ (GetUsageSummaryRange | Unset):  Default: GetUsageSummaryRange.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetUsageSummaryResponse200]
     """


    kwargs = _get_kwargs(
        range_=range_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    range_: GetUsageSummaryRange | Unset = GetUsageSummaryRange.VALUE_1,

) -> Error | GetUsageSummaryResponse200 | None:
    """ Get usage summary

     Aggregated usage over the requested `range` — tier + plan limits, quota used/remaining, next reset,
    a per-operation breakdown (request/error counts, error rate, avg latency), a daily timeline, status-
    class distribution, and range totals.

    Args:
        range_ (GetUsageSummaryRange | Unset):  Default: GetUsageSummaryRange.VALUE_1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetUsageSummaryResponse200
     """


    return (await asyncio_detailed(
        client=client,
range_=range_,

    )).parsed
