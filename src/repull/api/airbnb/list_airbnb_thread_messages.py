from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.message_list_response import MessageListResponse
from typing import cast



def _get_kwargs(
    thread_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/messaging/{thread_id}/messages".format(thread_id=quote(str(thread_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | MessageListResponse | None:
    if response.status_code == 200:
        response_200 = MessageListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

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
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | MessageListResponse]:
    """ Get Airbnb messages

     Fetch the full message log for an Airbnb thread, ordered oldest-to-newest. Walk pages with
    `?cursor=` until `pagination.hasMore` is `false`.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        thread_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MessageListResponse]
     """


    kwargs = _get_kwargs(
        thread_id=thread_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | MessageListResponse | None:
    """ Get Airbnb messages

     Fetch the full message log for an Airbnb thread, ordered oldest-to-newest. Walk pages with
    `?cursor=` until `pagination.hasMore` is `false`.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        thread_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MessageListResponse
     """


    return sync_detailed(
        thread_id=thread_id,
client=client,

    ).parsed

async def asyncio_detailed(
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | MessageListResponse]:
    """ Get Airbnb messages

     Fetch the full message log for an Airbnb thread, ordered oldest-to-newest. Walk pages with
    `?cursor=` until `pagination.hasMore` is `false`.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        thread_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MessageListResponse]
     """


    kwargs = _get_kwargs(
        thread_id=thread_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | MessageListResponse | None:
    """ Get Airbnb messages

     Fetch the full message log for an Airbnb thread, ordered oldest-to-newest. Walk pages with
    `?cursor=` until `pagination.hasMore` is `false`.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        thread_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MessageListResponse
     """


    return (await asyncio_detailed(
        thread_id=thread_id,
client=client,

    )).parsed
