from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_conversation_messages_order import ListConversationMessagesOrder
from ...models.message_list_response import MessageListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    order: ListConversationMessagesOrder | Unset = ListConversationMessagesOrder.DESC,
    x_schema: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_schema, Unset):
        headers["X-Schema"] = x_schema



    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    json_order: str | Unset = UNSET
    if not isinstance(order, Unset):
        json_order = order.value

    params["order"] = json_order


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/conversations/{id}/messages".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | MessageListResponse | None:
    if response.status_code == 200:
        response_200 = MessageListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | MessageListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    order: ListConversationMessagesOrder | Unset = ListConversationMessagesOrder.DESC,
    x_schema: str | Unset = UNSET,

) -> Response[Error | MessageListResponse]:
    """ List messages in a conversation

     Cursor-paginated messages within one thread. Defaults to newest-first (`?order=desc`); pass
    `?order=asc` for chronological replay. Use `pagination.next_cursor` from one response as the
    `cursor` query param of the next request.

    Args:
        id (int):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        order (ListConversationMessagesOrder | Unset):  Default:
            ListConversationMessagesOrder.DESC.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MessageListResponse]
     """


    kwargs = _get_kwargs(
        id=id,
cursor=cursor,
limit=limit,
order=order,
x_schema=x_schema,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    order: ListConversationMessagesOrder | Unset = ListConversationMessagesOrder.DESC,
    x_schema: str | Unset = UNSET,

) -> Error | MessageListResponse | None:
    """ List messages in a conversation

     Cursor-paginated messages within one thread. Defaults to newest-first (`?order=desc`); pass
    `?order=asc` for chronological replay. Use `pagination.next_cursor` from one response as the
    `cursor` query param of the next request.

    Args:
        id (int):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        order (ListConversationMessagesOrder | Unset):  Default:
            ListConversationMessagesOrder.DESC.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MessageListResponse
     """


    return sync_detailed(
        id=id,
client=client,
cursor=cursor,
limit=limit,
order=order,
x_schema=x_schema,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    order: ListConversationMessagesOrder | Unset = ListConversationMessagesOrder.DESC,
    x_schema: str | Unset = UNSET,

) -> Response[Error | MessageListResponse]:
    """ List messages in a conversation

     Cursor-paginated messages within one thread. Defaults to newest-first (`?order=desc`); pass
    `?order=asc` for chronological replay. Use `pagination.next_cursor` from one response as the
    `cursor` query param of the next request.

    Args:
        id (int):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        order (ListConversationMessagesOrder | Unset):  Default:
            ListConversationMessagesOrder.DESC.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MessageListResponse]
     """


    kwargs = _get_kwargs(
        id=id,
cursor=cursor,
limit=limit,
order=order,
x_schema=x_schema,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    order: ListConversationMessagesOrder | Unset = ListConversationMessagesOrder.DESC,
    x_schema: str | Unset = UNSET,

) -> Error | MessageListResponse | None:
    """ List messages in a conversation

     Cursor-paginated messages within one thread. Defaults to newest-first (`?order=desc`); pass
    `?order=asc` for chronological replay. Use `pagination.next_cursor` from one response as the
    `cursor` query param of the next request.

    Args:
        id (int):
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        order (ListConversationMessagesOrder | Unset):  Default:
            ListConversationMessagesOrder.DESC.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MessageListResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
cursor=cursor,
limit=limit,
order=order,
x_schema=x_schema,

    )).parsed
