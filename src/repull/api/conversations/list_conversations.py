from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.conversation_list_response import ConversationListResponse
from ...models.error import Error
from ...models.list_conversations_platform import ListConversationsPlatform
from ...models.list_conversations_status import ListConversationsStatus
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    platform: ListConversationsPlatform | Unset = UNSET,
    status: ListConversationsStatus | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_schema, Unset):
        headers["X-Schema"] = x_schema



    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    json_platform: str | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform.value

    params["platform"] = json_platform

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/conversations",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConversationListResponse | Error | None:
    if response.status_code == 200:
        response_200 = ConversationListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConversationListResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    platform: ListConversationsPlatform | Unset = UNSET,
    status: ListConversationsStatus | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Response[ConversationListResponse | Error]:
    """ List conversations

     Cursor-paginated list of message threads owned by the workspace. Backed by main vanio's
    `/api/threads/list` which keyset-paginates against `(last_message_at, id)` for constant per-page
    cost. Use `pagination.next_cursor` from one response as the `cursor` query param of the next
    request.

    Filters: `platform` (`airbnb`|`booking`|`vrbo`|`website`|`email`), `status` (`open`|`archived` —
    `archived` is a stable no-op until the bit lands on `message_threads`).

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        platform (ListConversationsPlatform | Unset):
        status (ListConversationsStatus | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationListResponse | Error]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
limit=limit,
platform=platform,
status=status,
x_schema=x_schema,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    platform: ListConversationsPlatform | Unset = UNSET,
    status: ListConversationsStatus | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> ConversationListResponse | Error | None:
    """ List conversations

     Cursor-paginated list of message threads owned by the workspace. Backed by main vanio's
    `/api/threads/list` which keyset-paginates against `(last_message_at, id)` for constant per-page
    cost. Use `pagination.next_cursor` from one response as the `cursor` query param of the next
    request.

    Filters: `platform` (`airbnb`|`booking`|`vrbo`|`website`|`email`), `status` (`open`|`archived` —
    `archived` is a stable no-op until the bit lands on `message_threads`).

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        platform (ListConversationsPlatform | Unset):
        status (ListConversationsStatus | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationListResponse | Error
     """


    return sync_detailed(
        client=client,
cursor=cursor,
limit=limit,
platform=platform,
status=status,
x_schema=x_schema,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    platform: ListConversationsPlatform | Unset = UNSET,
    status: ListConversationsStatus | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Response[ConversationListResponse | Error]:
    """ List conversations

     Cursor-paginated list of message threads owned by the workspace. Backed by main vanio's
    `/api/threads/list` which keyset-paginates against `(last_message_at, id)` for constant per-page
    cost. Use `pagination.next_cursor` from one response as the `cursor` query param of the next
    request.

    Filters: `platform` (`airbnb`|`booking`|`vrbo`|`website`|`email`), `status` (`open`|`archived` —
    `archived` is a stable no-op until the bit lands on `message_threads`).

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        platform (ListConversationsPlatform | Unset):
        status (ListConversationsStatus | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConversationListResponse | Error]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
limit=limit,
platform=platform,
status=status,
x_schema=x_schema,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    platform: ListConversationsPlatform | Unset = UNSET,
    status: ListConversationsStatus | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> ConversationListResponse | Error | None:
    """ List conversations

     Cursor-paginated list of message threads owned by the workspace. Backed by main vanio's
    `/api/threads/list` which keyset-paginates against `(last_message_at, id)` for constant per-page
    cost. Use `pagination.next_cursor` from one response as the `cursor` query param of the next
    request.

    Filters: `platform` (`airbnb`|`booking`|`vrbo`|`website`|`email`), `status` (`open`|`archived` —
    `archived` is a stable no-op until the bit lands on `message_threads`).

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        platform (ListConversationsPlatform | Unset):
        status (ListConversationsStatus | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConversationListResponse | Error
     """


    return (await asyncio_detailed(
        client=client,
cursor=cursor,
limit=limit,
platform=platform,
status=status,
x_schema=x_schema,

    )).parsed
