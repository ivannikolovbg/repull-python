from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.reactivate_workspace_response_200 import ReactivateWorkspaceResponse200
from typing import cast



def _get_kwargs(
    workspace_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/workspaces/{workspace_id}/reactivate".format(workspace_id=quote(str(workspace_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ReactivateWorkspaceResponse200 | None:
    if response.status_code == 200:
        response_200 = ReactivateWorkspaceResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = Error.from_dict(response.json())



        return response_402

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ReactivateWorkspaceResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | ReactivateWorkspaceResponse200]:
    """ Reactivate a workspace

     Undo `POST /v1/workspaces/{workspaceId}/deactivate`. The workspace is active again and the listings
    the deactivation switched off are switched back on; listings that were already inactive before it
    stay inactive. Reactivated listings count toward your plan again, so a reactivation that would
    exceed your plan's listing cap is refused with `402 listings_limit_exceeded` and nothing changes.
    Accounts stay disconnected: have your customer reconnect each one through Connect (`POST
    /v1/connect` with `X-Workspace-Id` set to this workspace). Calling it on an active workspace changes
    nothing.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReactivateWorkspaceResponse200]
     """


    kwargs = _get_kwargs(
        workspace_id=workspace_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | ReactivateWorkspaceResponse200 | None:
    """ Reactivate a workspace

     Undo `POST /v1/workspaces/{workspaceId}/deactivate`. The workspace is active again and the listings
    the deactivation switched off are switched back on; listings that were already inactive before it
    stay inactive. Reactivated listings count toward your plan again, so a reactivation that would
    exceed your plan's listing cap is refused with `402 listings_limit_exceeded` and nothing changes.
    Accounts stay disconnected: have your customer reconnect each one through Connect (`POST
    /v1/connect` with `X-Workspace-Id` set to this workspace). Calling it on an active workspace changes
    nothing.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReactivateWorkspaceResponse200
     """


    return sync_detailed(
        workspace_id=workspace_id,
client=client,

    ).parsed

async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | ReactivateWorkspaceResponse200]:
    """ Reactivate a workspace

     Undo `POST /v1/workspaces/{workspaceId}/deactivate`. The workspace is active again and the listings
    the deactivation switched off are switched back on; listings that were already inactive before it
    stay inactive. Reactivated listings count toward your plan again, so a reactivation that would
    exceed your plan's listing cap is refused with `402 listings_limit_exceeded` and nothing changes.
    Accounts stay disconnected: have your customer reconnect each one through Connect (`POST
    /v1/connect` with `X-Workspace-Id` set to this workspace). Calling it on an active workspace changes
    nothing.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReactivateWorkspaceResponse200]
     """


    kwargs = _get_kwargs(
        workspace_id=workspace_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | ReactivateWorkspaceResponse200 | None:
    """ Reactivate a workspace

     Undo `POST /v1/workspaces/{workspaceId}/deactivate`. The workspace is active again and the listings
    the deactivation switched off are switched back on; listings that were already inactive before it
    stay inactive. Reactivated listings count toward your plan again, so a reactivation that would
    exceed your plan's listing cap is refused with `402 listings_limit_exceeded` and nothing changes.
    Accounts stay disconnected: have your customer reconnect each one through Connect (`POST
    /v1/connect` with `X-Workspace-Id` set to this workspace). Calling it on an active workspace changes
    nothing.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReactivateWorkspaceResponse200
     """


    return (await asyncio_detailed(
        workspace_id=workspace_id,
client=client,

    )).parsed
