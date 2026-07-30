from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_usage_logs_range import GetUsageLogsRange
from ...models.get_usage_logs_response_200 import GetUsageLogsResponse200
from ...models.get_usage_logs_status import GetUsageLogsStatus
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    range_: GetUsageLogsRange | Unset = GetUsageLogsRange.VALUE_1,
    operation: str | Unset = UNSET,
    status: GetUsageLogsStatus | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    include_total: bool | Unset = True,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_range_: str | Unset = UNSET
    if not isinstance(range_, Unset):
        json_range_ = range_.value

    params["range"] = json_range_

    params["operation"] = operation

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["q"] = q

    params["limit"] = limit

    params["cursor"] = cursor

    params["offset"] = offset

    params["include_total"] = include_total


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/usage/logs",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetUsageLogsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetUsageLogsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetUsageLogsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    range_: GetUsageLogsRange | Unset = GetUsageLogsRange.VALUE_1,
    operation: str | Unset = UNSET,
    status: GetUsageLogsStatus | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    include_total: bool | Unset = True,

) -> Response[Error | GetUsageLogsResponse200]:
    """ List API request logs

     Cursor-paginated raw API request log for the authenticated workspace, newest first. Filter by time
    `range`, `operation` id(s), status class, or free-text `q`. Walk pages with `cursor` from
    `pagination.next_cursor` until `pagination.has_more` is `false`; `offset` is accepted as a shallow
    alias (deep walks must use `cursor`).

    Args:
        range_ (GetUsageLogsRange | Unset):  Default: GetUsageLogsRange.VALUE_1.
        operation (str | Unset):
        status (GetUsageLogsStatus | Unset):
        q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetUsageLogsResponse200]
     """


    kwargs = _get_kwargs(
        range_=range_,
operation=operation,
status=status,
q=q,
limit=limit,
cursor=cursor,
offset=offset,
include_total=include_total,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    range_: GetUsageLogsRange | Unset = GetUsageLogsRange.VALUE_1,
    operation: str | Unset = UNSET,
    status: GetUsageLogsStatus | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    include_total: bool | Unset = True,

) -> Error | GetUsageLogsResponse200 | None:
    """ List API request logs

     Cursor-paginated raw API request log for the authenticated workspace, newest first. Filter by time
    `range`, `operation` id(s), status class, or free-text `q`. Walk pages with `cursor` from
    `pagination.next_cursor` until `pagination.has_more` is `false`; `offset` is accepted as a shallow
    alias (deep walks must use `cursor`).

    Args:
        range_ (GetUsageLogsRange | Unset):  Default: GetUsageLogsRange.VALUE_1.
        operation (str | Unset):
        status (GetUsageLogsStatus | Unset):
        q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetUsageLogsResponse200
     """


    return sync_detailed(
        client=client,
range_=range_,
operation=operation,
status=status,
q=q,
limit=limit,
cursor=cursor,
offset=offset,
include_total=include_total,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    range_: GetUsageLogsRange | Unset = GetUsageLogsRange.VALUE_1,
    operation: str | Unset = UNSET,
    status: GetUsageLogsStatus | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    include_total: bool | Unset = True,

) -> Response[Error | GetUsageLogsResponse200]:
    """ List API request logs

     Cursor-paginated raw API request log for the authenticated workspace, newest first. Filter by time
    `range`, `operation` id(s), status class, or free-text `q`. Walk pages with `cursor` from
    `pagination.next_cursor` until `pagination.has_more` is `false`; `offset` is accepted as a shallow
    alias (deep walks must use `cursor`).

    Args:
        range_ (GetUsageLogsRange | Unset):  Default: GetUsageLogsRange.VALUE_1.
        operation (str | Unset):
        status (GetUsageLogsStatus | Unset):
        q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetUsageLogsResponse200]
     """


    kwargs = _get_kwargs(
        range_=range_,
operation=operation,
status=status,
q=q,
limit=limit,
cursor=cursor,
offset=offset,
include_total=include_total,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    range_: GetUsageLogsRange | Unset = GetUsageLogsRange.VALUE_1,
    operation: str | Unset = UNSET,
    status: GetUsageLogsStatus | Unset = UNSET,
    q: str | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    include_total: bool | Unset = True,

) -> Error | GetUsageLogsResponse200 | None:
    """ List API request logs

     Cursor-paginated raw API request log for the authenticated workspace, newest first. Filter by time
    `range`, `operation` id(s), status class, or free-text `q`. Walk pages with `cursor` from
    `pagination.next_cursor` until `pagination.has_more` is `false`; `offset` is accepted as a shallow
    alias (deep walks must use `cursor`).

    Args:
        range_ (GetUsageLogsRange | Unset):  Default: GetUsageLogsRange.VALUE_1.
        operation (str | Unset):
        status (GetUsageLogsStatus | Unset):
        q (str | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetUsageLogsResponse200
     """


    return (await asyncio_detailed(
        client=client,
range_=range_,
operation=operation,
status=status,
q=q,
limit=limit,
cursor=cursor,
offset=offset,
include_total=include_total,

    )).parsed
