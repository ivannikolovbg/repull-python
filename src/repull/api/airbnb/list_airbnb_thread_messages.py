from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_airbnb_thread_messages_response_200 import ListAirbnbThreadMessagesResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    thread_id: str,
    *,
    cursor: str | Unset = UNSET,
    all_: bool | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["all"] = all_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/messaging/{thread_id}/messages".format(thread_id=quote(str(thread_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListAirbnbThreadMessagesResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAirbnbThreadMessagesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListAirbnbThreadMessagesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    all_: bool | Unset = UNSET,

) -> Response[Error | ListAirbnbThreadMessagesResponse200]:
    """ Get Airbnb messages

     Messages stored for an Airbnb thread, as recorded rows (not the unified `Message` shape — use `GET
    /v1/conversations/{id}/messages` for that). By default returns 50 per page, newest first; walk older
    pages with `?cursor=` (the `pagination.nextCursor` of the previous page) until `pagination.hasMore`
    is `false`. `?all=true` returns up to 1000 rows oldest-first in one response, with no `pagination`.

    Each row carries `attachments` — photos and other files on that message, inbound or outbound — in
    the same shape as the unified endpoint.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        thread_id (str):
        cursor (str | Unset):
        all_ (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbThreadMessagesResponse200]
     """


    kwargs = _get_kwargs(
        thread_id=thread_id,
cursor=cursor,
all_=all_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    all_: bool | Unset = UNSET,

) -> Error | ListAirbnbThreadMessagesResponse200 | None:
    """ Get Airbnb messages

     Messages stored for an Airbnb thread, as recorded rows (not the unified `Message` shape — use `GET
    /v1/conversations/{id}/messages` for that). By default returns 50 per page, newest first; walk older
    pages with `?cursor=` (the `pagination.nextCursor` of the previous page) until `pagination.hasMore`
    is `false`. `?all=true` returns up to 1000 rows oldest-first in one response, with no `pagination`.

    Each row carries `attachments` — photos and other files on that message, inbound or outbound — in
    the same shape as the unified endpoint.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        thread_id (str):
        cursor (str | Unset):
        all_ (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbThreadMessagesResponse200
     """


    return sync_detailed(
        thread_id=thread_id,
client=client,
cursor=cursor,
all_=all_,

    ).parsed

async def asyncio_detailed(
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    all_: bool | Unset = UNSET,

) -> Response[Error | ListAirbnbThreadMessagesResponse200]:
    """ Get Airbnb messages

     Messages stored for an Airbnb thread, as recorded rows (not the unified `Message` shape — use `GET
    /v1/conversations/{id}/messages` for that). By default returns 50 per page, newest first; walk older
    pages with `?cursor=` (the `pagination.nextCursor` of the previous page) until `pagination.hasMore`
    is `false`. `?all=true` returns up to 1000 rows oldest-first in one response, with no `pagination`.

    Each row carries `attachments` — photos and other files on that message, inbound or outbound — in
    the same shape as the unified endpoint.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        thread_id (str):
        cursor (str | Unset):
        all_ (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbThreadMessagesResponse200]
     """


    kwargs = _get_kwargs(
        thread_id=thread_id,
cursor=cursor,
all_=all_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    all_: bool | Unset = UNSET,

) -> Error | ListAirbnbThreadMessagesResponse200 | None:
    """ Get Airbnb messages

     Messages stored for an Airbnb thread, as recorded rows (not the unified `Message` shape — use `GET
    /v1/conversations/{id}/messages` for that). By default returns 50 per page, newest first; walk older
    pages with `?cursor=` (the `pagination.nextCursor` of the previous page) until `pagination.hasMore`
    is `false`. `?all=true` returns up to 1000 rows oldest-first in one response, with no `pagination`.

    Each row carries `attachments` — photos and other files on that message, inbound or outbound — in
    the same shape as the unified endpoint.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        thread_id (str):
        cursor (str | Unset):
        all_ (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbThreadMessagesResponse200
     """


    return (await asyncio_detailed(
        thread_id=thread_id,
client=client,
cursor=cursor,
all_=all_,

    )).parsed
