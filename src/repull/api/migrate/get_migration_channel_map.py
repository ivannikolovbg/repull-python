from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_migration_channel_map_response_200 import GetMigrationChannelMapResponse200
from typing import cast



def _get_kwargs(
    workspace_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/migrations/{workspace_id}/channel-map".format(workspace_id=quote(str(workspace_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetMigrationChannelMapResponse200 | None:
    if response.status_code == 200:
        response_200 = GetMigrationChannelMapResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetMigrationChannelMapResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetMigrationChannelMapResponse200]:
    """ Get channel links

     The Airbnb, Booking.com and VRBO listing each migrated property is linked to in the source PMS, read
    live. Use it to link each listing to the right property when the channels are reconnected in the
    destination — channel connections themselves cannot be moved between PMSs.

    Args:
        workspace_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetMigrationChannelMapResponse200]
     """


    kwargs = _get_kwargs(
        workspace_id=workspace_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    workspace_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetMigrationChannelMapResponse200 | None:
    """ Get channel links

     The Airbnb, Booking.com and VRBO listing each migrated property is linked to in the source PMS, read
    live. Use it to link each listing to the right property when the channels are reconnected in the
    destination — channel connections themselves cannot be moved between PMSs.

    Args:
        workspace_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetMigrationChannelMapResponse200
     """


    return sync_detailed(
        workspace_id=workspace_id,
client=client,

    ).parsed

async def asyncio_detailed(
    workspace_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetMigrationChannelMapResponse200]:
    """ Get channel links

     The Airbnb, Booking.com and VRBO listing each migrated property is linked to in the source PMS, read
    live. Use it to link each listing to the right property when the channels are reconnected in the
    destination — channel connections themselves cannot be moved between PMSs.

    Args:
        workspace_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetMigrationChannelMapResponse200]
     """


    kwargs = _get_kwargs(
        workspace_id=workspace_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    workspace_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetMigrationChannelMapResponse200 | None:
    """ Get channel links

     The Airbnb, Booking.com and VRBO listing each migrated property is linked to in the source PMS, read
    live. Use it to link each listing to the right property when the channels are reconnected in the
    destination — channel connections themselves cannot be moved between PMSs.

    Args:
        workspace_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetMigrationChannelMapResponse200
     """


    return (await asyncio_detailed(
        workspace_id=workspace_id,
client=client,

    )).parsed
