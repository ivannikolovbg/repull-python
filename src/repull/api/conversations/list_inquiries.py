from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_inquiries_response_200 import ListInquiriesResponse200
from ...models.list_inquiries_status import ListInquiriesStatus
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    status: ListInquiriesStatus | Unset = ListInquiriesStatus.OPEN,
    listing_id: int | Unset = UNSET,
    conversation_id: int | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    include_total: bool | Unset = True,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["listing_id"] = listing_id

    params["conversation_id"] = conversation_id

    params["limit"] = limit

    params["cursor"] = cursor

    params["offset"] = offset

    params["include_total"] = include_total


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/inquiries",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListInquiriesResponse200 | None:
    if response.status_code == 200:
        response_200 = ListInquiriesResponse200.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListInquiriesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: ListInquiriesStatus | Unset = ListInquiriesStatus.OPEN,
    listing_id: int | Unset = UNSET,
    conversation_id: int | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    include_total: bool | Unset = True,

) -> Response[Error | ListInquiriesResponse200]:
    """ List inquiries

     Airbnb inquiries — guests asking about dates before booking — newest first. By default only `open`
    ones: nobody has answered and the stay is still ahead. Answer one with `POST
    /v1/conversations/{conversationId}/pre-approval` (accept their dates and price) or `POST
    /v1/conversations/{conversationId}/special-offers` (your own terms).

    Booking **requests** are not inquiries: they are reservations with status `pending` — list them with
    `GET /v1/reservations?status=pending` and answer with `POST /v1/reservations/{id}/accept` or
    `/decline`.

    **Pagination:** pass `pagination.nextCursor` back as `?cursor=` until `pagination.hasMore` is
    `false`. `?offset=` also works (0..10000). `limit` defaults to 50, max 100.

    Inquiries on inactive listings are left out; `?listing_id=` naming an inactive listing returns `403
    listing_inactive`. `X-Account-Id` narrows to one connected account.

    Args:
        status (ListInquiriesStatus | Unset):  Default: ListInquiriesStatus.OPEN.
        listing_id (int | Unset):
        conversation_id (int | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListInquiriesResponse200]
     """


    kwargs = _get_kwargs(
        status=status,
listing_id=listing_id,
conversation_id=conversation_id,
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
    status: ListInquiriesStatus | Unset = ListInquiriesStatus.OPEN,
    listing_id: int | Unset = UNSET,
    conversation_id: int | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    include_total: bool | Unset = True,

) -> Error | ListInquiriesResponse200 | None:
    """ List inquiries

     Airbnb inquiries — guests asking about dates before booking — newest first. By default only `open`
    ones: nobody has answered and the stay is still ahead. Answer one with `POST
    /v1/conversations/{conversationId}/pre-approval` (accept their dates and price) or `POST
    /v1/conversations/{conversationId}/special-offers` (your own terms).

    Booking **requests** are not inquiries: they are reservations with status `pending` — list them with
    `GET /v1/reservations?status=pending` and answer with `POST /v1/reservations/{id}/accept` or
    `/decline`.

    **Pagination:** pass `pagination.nextCursor` back as `?cursor=` until `pagination.hasMore` is
    `false`. `?offset=` also works (0..10000). `limit` defaults to 50, max 100.

    Inquiries on inactive listings are left out; `?listing_id=` naming an inactive listing returns `403
    listing_inactive`. `X-Account-Id` narrows to one connected account.

    Args:
        status (ListInquiriesStatus | Unset):  Default: ListInquiriesStatus.OPEN.
        listing_id (int | Unset):
        conversation_id (int | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListInquiriesResponse200
     """


    return sync_detailed(
        client=client,
status=status,
listing_id=listing_id,
conversation_id=conversation_id,
limit=limit,
cursor=cursor,
offset=offset,
include_total=include_total,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: ListInquiriesStatus | Unset = ListInquiriesStatus.OPEN,
    listing_id: int | Unset = UNSET,
    conversation_id: int | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    include_total: bool | Unset = True,

) -> Response[Error | ListInquiriesResponse200]:
    """ List inquiries

     Airbnb inquiries — guests asking about dates before booking — newest first. By default only `open`
    ones: nobody has answered and the stay is still ahead. Answer one with `POST
    /v1/conversations/{conversationId}/pre-approval` (accept their dates and price) or `POST
    /v1/conversations/{conversationId}/special-offers` (your own terms).

    Booking **requests** are not inquiries: they are reservations with status `pending` — list them with
    `GET /v1/reservations?status=pending` and answer with `POST /v1/reservations/{id}/accept` or
    `/decline`.

    **Pagination:** pass `pagination.nextCursor` back as `?cursor=` until `pagination.hasMore` is
    `false`. `?offset=` also works (0..10000). `limit` defaults to 50, max 100.

    Inquiries on inactive listings are left out; `?listing_id=` naming an inactive listing returns `403
    listing_inactive`. `X-Account-Id` narrows to one connected account.

    Args:
        status (ListInquiriesStatus | Unset):  Default: ListInquiriesStatus.OPEN.
        listing_id (int | Unset):
        conversation_id (int | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListInquiriesResponse200]
     """


    kwargs = _get_kwargs(
        status=status,
listing_id=listing_id,
conversation_id=conversation_id,
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
    status: ListInquiriesStatus | Unset = ListInquiriesStatus.OPEN,
    listing_id: int | Unset = UNSET,
    conversation_id: int | Unset = UNSET,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    include_total: bool | Unset = True,

) -> Error | ListInquiriesResponse200 | None:
    """ List inquiries

     Airbnb inquiries — guests asking about dates before booking — newest first. By default only `open`
    ones: nobody has answered and the stay is still ahead. Answer one with `POST
    /v1/conversations/{conversationId}/pre-approval` (accept their dates and price) or `POST
    /v1/conversations/{conversationId}/special-offers` (your own terms).

    Booking **requests** are not inquiries: they are reservations with status `pending` — list them with
    `GET /v1/reservations?status=pending` and answer with `POST /v1/reservations/{id}/accept` or
    `/decline`.

    **Pagination:** pass `pagination.nextCursor` back as `?cursor=` until `pagination.hasMore` is
    `false`. `?offset=` also works (0..10000). `limit` defaults to 50, max 100.

    Inquiries on inactive listings are left out; `?listing_id=` naming an inactive listing returns `403
    listing_inactive`. `X-Account-Id` narrows to one connected account.

    Args:
        status (ListInquiriesStatus | Unset):  Default: ListInquiriesStatus.OPEN.
        listing_id (int | Unset):
        conversation_id (int | Unset):
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListInquiriesResponse200
     """


    return (await asyncio_detailed(
        client=client,
status=status,
listing_id=listing_id,
conversation_id=conversation_id,
limit=limit,
cursor=cursor,
offset=offset,
include_total=include_total,

    )).parsed
