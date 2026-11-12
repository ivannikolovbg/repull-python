from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.deactivate_workspace_response_200 import DeactivateWorkspaceResponse200
from ...models.error import Error
from typing import cast



def _get_kwargs(
    workspace_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/workspaces/{workspace_id}/deactivate".format(workspace_id=quote(str(workspace_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeactivateWorkspaceResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = DeactivateWorkspaceResponse200.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeactivateWorkspaceResponse200 | Error]:
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

) -> Response[DeactivateWorkspaceResponse200 | Error]:
    """ Deactivate a workspace

     Offboard one of your customers. Disconnects every account still connected in the sub-workspace
    (Airbnb hosts, Booking.com properties, Vrbo sign-ins, PMSs), deactivates its listings so they stop
    counting toward your plan, and marks the workspace inactive. Nothing is deleted: its listings,
    reservations and conversations are kept, and it stays in `GET /v1/workspaces` with `active: false`
    and `deactivatedAt`. Nothing is changed on the channels themselves. Calling it again is safe. Undo
    it with `POST /v1/workspaces/{workspaceId}/reactivate`. Workspace names don't have to be unique; the
    `workspaceId` (or your own `externalRef`) identifies a workspace.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeactivateWorkspaceResponse200 | Error]
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

) -> DeactivateWorkspaceResponse200 | Error | None:
    """ Deactivate a workspace

     Offboard one of your customers. Disconnects every account still connected in the sub-workspace
    (Airbnb hosts, Booking.com properties, Vrbo sign-ins, PMSs), deactivates its listings so they stop
    counting toward your plan, and marks the workspace inactive. Nothing is deleted: its listings,
    reservations and conversations are kept, and it stays in `GET /v1/workspaces` with `active: false`
    and `deactivatedAt`. Nothing is changed on the channels themselves. Calling it again is safe. Undo
    it with `POST /v1/workspaces/{workspaceId}/reactivate`. Workspace names don't have to be unique; the
    `workspaceId` (or your own `externalRef`) identifies a workspace.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeactivateWorkspaceResponse200 | Error
     """


    return sync_detailed(
        workspace_id=workspace_id,
client=client,

    ).parsed

async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DeactivateWorkspaceResponse200 | Error]:
    """ Deactivate a workspace

     Offboard one of your customers. Disconnects every account still connected in the sub-workspace
    (Airbnb hosts, Booking.com properties, Vrbo sign-ins, PMSs), deactivates its listings so they stop
    counting toward your plan, and marks the workspace inactive. Nothing is deleted: its listings,
    reservations and conversations are kept, and it stays in `GET /v1/workspaces` with `active: false`
    and `deactivatedAt`. Nothing is changed on the channels themselves. Calling it again is safe. Undo
    it with `POST /v1/workspaces/{workspaceId}/reactivate`. Workspace names don't have to be unique; the
    `workspaceId` (or your own `externalRef`) identifies a workspace.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeactivateWorkspaceResponse200 | Error]
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

) -> DeactivateWorkspaceResponse200 | Error | None:
    """ Deactivate a workspace

     Offboard one of your customers. Disconnects every account still connected in the sub-workspace
    (Airbnb hosts, Booking.com properties, Vrbo sign-ins, PMSs), deactivates its listings so they stop
    counting toward your plan, and marks the workspace inactive. Nothing is deleted: its listings,
    reservations and conversations are kept, and it stays in `GET /v1/workspaces` with `active: false`
    and `deactivatedAt`. Nothing is changed on the channels themselves. Calling it again is safe. Undo
    it with `POST /v1/workspaces/{workspaceId}/reactivate`. Workspace names don't have to be unique; the
    `workspaceId` (or your own `externalRef`) identifies a workspace.

    Args:
        workspace_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeactivateWorkspaceResponse200 | Error
     """


    return (await asyncio_detailed(
        workspace_id=workspace_id,
client=client,

    )).parsed
