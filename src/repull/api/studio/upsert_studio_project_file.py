from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.studio_error import StudioError
from ...models.upsert_studio_project_file_body import UpsertStudioProjectFileBody
from ...models.upsert_studio_project_file_response_200 import UpsertStudioProjectFileResponse200
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    path: str,
    *,
    body: UpsertStudioProjectFileBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/studio/projects/{id}/files/{path}".format(id=quote(str(id), safe=""),path=quote(str(path), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> StudioError | UpsertStudioProjectFileResponse200 | None:
    if response.status_code == 200:
        response_200 = UpsertStudioProjectFileResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = StudioError.from_dict(response.json())



        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[StudioError | UpsertStudioProjectFileResponse200]:
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
    body: UpsertStudioProjectFileBody,

) -> Response[StudioError | UpsertStudioProjectFileResponse200]:
    """ Upsert a Studio project file

     Creates or replaces a file at the given path. Returns the new sha256 so subsequent writes can use
    optimistic concurrency.

    Args:
        id (UUID):
        path (str):
        body (UpsertStudioProjectFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StudioError | UpsertStudioProjectFileResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
path=path,
body=body,

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
    body: UpsertStudioProjectFileBody,

) -> StudioError | UpsertStudioProjectFileResponse200 | None:
    """ Upsert a Studio project file

     Creates or replaces a file at the given path. Returns the new sha256 so subsequent writes can use
    optimistic concurrency.

    Args:
        id (UUID):
        path (str):
        body (UpsertStudioProjectFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StudioError | UpsertStudioProjectFileResponse200
     """


    return sync_detailed(
        id=id,
path=path,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    path: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpsertStudioProjectFileBody,

) -> Response[StudioError | UpsertStudioProjectFileResponse200]:
    """ Upsert a Studio project file

     Creates or replaces a file at the given path. Returns the new sha256 so subsequent writes can use
    optimistic concurrency.

    Args:
        id (UUID):
        path (str):
        body (UpsertStudioProjectFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StudioError | UpsertStudioProjectFileResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
path=path,
body=body,

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
    body: UpsertStudioProjectFileBody,

) -> StudioError | UpsertStudioProjectFileResponse200 | None:
    """ Upsert a Studio project file

     Creates or replaces a file at the given path. Returns the new sha256 so subsequent writes can use
    optimistic concurrency.

    Args:
        id (UUID):
        path (str):
        body (UpsertStudioProjectFileBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StudioError | UpsertStudioProjectFileResponse200
     """


    return (await asyncio_detailed(
        id=id,
path=path,
client=client,
body=body,

    )).parsed
