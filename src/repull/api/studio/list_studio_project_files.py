from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_studio_project_files_response_200 import ListStudioProjectFilesResponse200
from ...models.studio_error import StudioError
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/studio/projects/{id}/files".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListStudioProjectFilesResponse200 | StudioError | None:
    if response.status_code == 200:
        response_200 = ListStudioProjectFilesResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListStudioProjectFilesResponse200 | StudioError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ListStudioProjectFilesResponse200 | StudioError]:
    """ List Studio project files

     Returns every file in the project tree with its content, sha256, and size. Use the digests to detect
    drift before writing.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListStudioProjectFilesResponse200 | StudioError]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> ListStudioProjectFilesResponse200 | StudioError | None:
    """ List Studio project files

     Returns every file in the project tree with its content, sha256, and size. Use the digests to detect
    drift before writing.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListStudioProjectFilesResponse200 | StudioError
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ListStudioProjectFilesResponse200 | StudioError]:
    """ List Studio project files

     Returns every file in the project tree with its content, sha256, and size. Use the digests to detect
    drift before writing.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListStudioProjectFilesResponse200 | StudioError]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> ListStudioProjectFilesResponse200 | StudioError | None:
    """ List Studio project files

     Returns every file in the project tree with its content, sha256, and size. Use the digests to detect
    drift before writing.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListStudioProjectFilesResponse200 | StudioError
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
