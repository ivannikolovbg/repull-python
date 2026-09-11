from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_channel_health_channel import GetChannelHealthChannel
from ...models.get_channel_health_response_200 import GetChannelHealthResponse200
from typing import cast



def _get_kwargs(
    channel: GetChannelHealthChannel,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/health/channels/{channel}".format(channel=quote(str(channel), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetChannelHealthResponse200 | None:
    if response.status_code == 200:
        response_200 = GetChannelHealthResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetChannelHealthResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    channel: GetChannelHealthChannel,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetChannelHealthResponse200]:
    r""" Per-channel connectivity health

     Reports reachability and auth state for one channel (`airbnb`, `booking`, `vrbo`, `plumguide`). Use
    it to tell \"the channel is down\" apart from \"this workspace's connection expired\".

    Args:
        channel (GetChannelHealthChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetChannelHealthResponse200]
     """


    kwargs = _get_kwargs(
        channel=channel,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    channel: GetChannelHealthChannel,
    *,
    client: AuthenticatedClient | Client,

) -> GetChannelHealthResponse200 | None:
    r""" Per-channel connectivity health

     Reports reachability and auth state for one channel (`airbnb`, `booking`, `vrbo`, `plumguide`). Use
    it to tell \"the channel is down\" apart from \"this workspace's connection expired\".

    Args:
        channel (GetChannelHealthChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetChannelHealthResponse200
     """


    return sync_detailed(
        channel=channel,
client=client,

    ).parsed

async def asyncio_detailed(
    channel: GetChannelHealthChannel,
    *,
    client: AuthenticatedClient | Client,

) -> Response[GetChannelHealthResponse200]:
    r""" Per-channel connectivity health

     Reports reachability and auth state for one channel (`airbnb`, `booking`, `vrbo`, `plumguide`). Use
    it to tell \"the channel is down\" apart from \"this workspace's connection expired\".

    Args:
        channel (GetChannelHealthChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetChannelHealthResponse200]
     """


    kwargs = _get_kwargs(
        channel=channel,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    channel: GetChannelHealthChannel,
    *,
    client: AuthenticatedClient | Client,

) -> GetChannelHealthResponse200 | None:
    r""" Per-channel connectivity health

     Reports reachability and auth state for one channel (`airbnb`, `booking`, `vrbo`, `plumguide`). Use
    it to tell \"the channel is down\" apart from \"this workspace's connection expired\".

    Args:
        channel (GetChannelHealthChannel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetChannelHealthResponse200
     """


    return (await asyncio_detailed(
        channel=channel,
client=client,

    )).parsed
