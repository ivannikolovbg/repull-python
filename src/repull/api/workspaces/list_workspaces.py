from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_workspaces_response_200 import ListWorkspacesResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    limit: int | Unset = 25,
    cursor: str | Unset = UNSET,
    external_ref: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["externalRef"] = external_ref


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/workspaces",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListWorkspacesResponse200 | None:
    if response.status_code == 200:
        response_200 = ListWorkspacesResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListWorkspacesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 25,
    cursor: str | Unset = UNSET,
    external_ref: str | Unset = UNSET,

) -> Response[Error | ListWorkspacesResponse200]:
    """ List workspaces

     Every sub-workspace your workspace has opened, newest first: one per customer of yours, created by
    `POST /v1/connect` with `workspace` (or by Repull Migrate). Read or write a workspace's data by
    sending its `workspaceId` as `X-Workspace-Id`. Its webhook events arrive on your own webhook
    endpoints, tagged with `workspaceId`. Page with `pagination.nextCursor`.

    Args:
        limit (int | Unset):  Default: 25.
        cursor (str | Unset):
        external_ref (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListWorkspacesResponse200]
     """


    kwargs = _get_kwargs(
        limit=limit,
cursor=cursor,
external_ref=external_ref,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 25,
    cursor: str | Unset = UNSET,
    external_ref: str | Unset = UNSET,

) -> Error | ListWorkspacesResponse200 | None:
    """ List workspaces

     Every sub-workspace your workspace has opened, newest first: one per customer of yours, created by
    `POST /v1/connect` with `workspace` (or by Repull Migrate). Read or write a workspace's data by
    sending its `workspaceId` as `X-Workspace-Id`. Its webhook events arrive on your own webhook
    endpoints, tagged with `workspaceId`. Page with `pagination.nextCursor`.

    Args:
        limit (int | Unset):  Default: 25.
        cursor (str | Unset):
        external_ref (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListWorkspacesResponse200
     """


    return sync_detailed(
        client=client,
limit=limit,
cursor=cursor,
external_ref=external_ref,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 25,
    cursor: str | Unset = UNSET,
    external_ref: str | Unset = UNSET,

) -> Response[Error | ListWorkspacesResponse200]:
    """ List workspaces

     Every sub-workspace your workspace has opened, newest first: one per customer of yours, created by
    `POST /v1/connect` with `workspace` (or by Repull Migrate). Read or write a workspace's data by
    sending its `workspaceId` as `X-Workspace-Id`. Its webhook events arrive on your own webhook
    endpoints, tagged with `workspaceId`. Page with `pagination.nextCursor`.

    Args:
        limit (int | Unset):  Default: 25.
        cursor (str | Unset):
        external_ref (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListWorkspacesResponse200]
     """


    kwargs = _get_kwargs(
        limit=limit,
cursor=cursor,
external_ref=external_ref,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 25,
    cursor: str | Unset = UNSET,
    external_ref: str | Unset = UNSET,

) -> Error | ListWorkspacesResponse200 | None:
    """ List workspaces

     Every sub-workspace your workspace has opened, newest first: one per customer of yours, created by
    `POST /v1/connect` with `workspace` (or by Repull Migrate). Read or write a workspace's data by
    sending its `workspaceId` as `X-Workspace-Id`. Its webhook events arrive on your own webhook
    endpoints, tagged with `workspaceId`. Page with `pagination.nextCursor`.

    Args:
        limit (int | Unset):  Default: 25.
        cursor (str | Unset):
        external_ref (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListWorkspacesResponse200
     """


    return (await asyncio_detailed(
        client=client,
limit=limit,
cursor=cursor,
external_ref=external_ref,

    )).parsed
