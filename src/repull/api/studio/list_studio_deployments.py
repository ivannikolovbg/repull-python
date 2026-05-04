from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_studio_deployments_response_200 import ListStudioDeploymentsResponse200
from ...models.list_studio_deployments_status import ListStudioDeploymentsStatus
from ...models.studio_error import StudioError
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    *,
    project_id: UUID | Unset = UNSET,
    status: ListStudioDeploymentsStatus | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_project_id: str | Unset = UNSET
    if not isinstance(project_id, Unset):
        json_project_id = str(project_id)
    params["project_id"] = json_project_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["limit"] = limit

    params["offset"] = offset


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/studio/deployments",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListStudioDeploymentsResponse200 | StudioError | None:
    if response.status_code == 200:
        response_200 = ListStudioDeploymentsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = StudioError.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListStudioDeploymentsResponse200 | StudioError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: UUID | Unset = UNSET,
    status: ListStudioDeploymentsStatus | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,

) -> Response[ListStudioDeploymentsResponse200 | StudioError]:
    """ List Studio deployments

     Returns every deployment across all projects in your account, newest first. Filter by project with
    `project_id`.

    Args:
        project_id (UUID | Unset):
        status (ListStudioDeploymentsStatus | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListStudioDeploymentsResponse200 | StudioError]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
status=status,
limit=limit,
offset=offset,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: UUID | Unset = UNSET,
    status: ListStudioDeploymentsStatus | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,

) -> ListStudioDeploymentsResponse200 | StudioError | None:
    """ List Studio deployments

     Returns every deployment across all projects in your account, newest first. Filter by project with
    `project_id`.

    Args:
        project_id (UUID | Unset):
        status (ListStudioDeploymentsStatus | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListStudioDeploymentsResponse200 | StudioError
     """


    return sync_detailed(
        client=client,
project_id=project_id,
status=status,
limit=limit,
offset=offset,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: UUID | Unset = UNSET,
    status: ListStudioDeploymentsStatus | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,

) -> Response[ListStudioDeploymentsResponse200 | StudioError]:
    """ List Studio deployments

     Returns every deployment across all projects in your account, newest first. Filter by project with
    `project_id`.

    Args:
        project_id (UUID | Unset):
        status (ListStudioDeploymentsStatus | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListStudioDeploymentsResponse200 | StudioError]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
status=status,
limit=limit,
offset=offset,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: UUID | Unset = UNSET,
    status: ListStudioDeploymentsStatus | Unset = UNSET,
    limit: int | Unset = 50,
    offset: int | Unset = 0,

) -> ListStudioDeploymentsResponse200 | StudioError | None:
    """ List Studio deployments

     Returns every deployment across all projects in your account, newest first. Filter by project with
    `project_id`.

    Args:
        project_id (UUID | Unset):
        status (ListStudioDeploymentsStatus | Unset):
        limit (int | Unset):  Default: 50.
        offset (int | Unset):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListStudioDeploymentsResponse200 | StudioError
     """


    return (await asyncio_detailed(
        client=client,
project_id=project_id,
status=status,
limit=limit,
offset=offset,

    )).parsed
