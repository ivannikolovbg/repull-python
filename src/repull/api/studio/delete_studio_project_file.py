from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_studio_project_file_response_200 import DeleteStudioProjectFileResponse200
from ...models.studio_error import StudioError
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    path: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/studio/projects/{id}/files/{path}".format(id=quote(str(id), safe=""),path=quote(str(path), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteStudioProjectFileResponse200 | StudioError | None:
    if response.status_code == 200:
        response_200 = DeleteStudioProjectFileResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = StudioError.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = StudioError.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteStudioProjectFileResponse200 | StudioError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    path: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DeleteStudioProjectFileResponse200 | StudioError]:
    """ Delete a Studio project file

     Removes a single file from the project tree. The deployment is not redeployed automatically —
    trigger a new deployment to apply the change.

    Args:
        id (UUID):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteStudioProjectFileResponse200 | StudioError]
     """


    kwargs = _get_kwargs(
        id=id,
path=path,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    path: str,
    *,
    client: AuthenticatedClient | Client,

) -> DeleteStudioProjectFileResponse200 | StudioError | None:
    """ Delete a Studio project file

     Removes a single file from the project tree. The deployment is not redeployed automatically —
    trigger a new deployment to apply the change.

    Args:
        id (UUID):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteStudioProjectFileResponse200 | StudioError
     """


    return sync_detailed(
        id=id,
path=path,
client=client,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    path: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[DeleteStudioProjectFileResponse200 | StudioError]:
    """ Delete a Studio project file

     Removes a single file from the project tree. The deployment is not redeployed automatically —
    trigger a new deployment to apply the change.

    Args:
        id (UUID):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteStudioProjectFileResponse200 | StudioError]
     """


    kwargs = _get_kwargs(
        id=id,
path=path,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    path: str,
    *,
    client: AuthenticatedClient | Client,

) -> DeleteStudioProjectFileResponse200 | StudioError | None:
    """ Delete a Studio project file

     Removes a single file from the project tree. The deployment is not redeployed automatically —
    trigger a new deployment to apply the change.

    Args:
        id (UUID):
        path (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteStudioProjectFileResponse200 | StudioError
     """


    return (await asyncio_detailed(
        id=id,
path=path,
client=client,

    )).parsed
