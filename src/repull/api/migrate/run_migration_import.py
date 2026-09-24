from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.run_migration_import_body import RunMigrationImportBody
from ...models.run_migration_import_response_202 import RunMigrationImportResponse202
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    workspace_id: int,
    *,
    body: RunMigrationImportBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/migrations/{workspace_id}/import".format(workspace_id=quote(str(workspace_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | RunMigrationImportResponse202 | None:
    if response.status_code == 202:
        response_202 = RunMigrationImportResponse202.from_dict(response.json())



        return response_202

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | RunMigrationImportResponse202]:
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
    body: RunMigrationImportBody | Unset = UNSET,

) -> Response[Error | RunMigrationImportResponse202]:
    """ Run the import again

     Queue another import from the source PMS — for example messages after the first pass, or only
    reservations changed since a date. Progress shows on `GET /v1/migrations/{workspaceId}`.

    Args:
        workspace_id (int):
        body (RunMigrationImportBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RunMigrationImportResponse202]
     """


    kwargs = _get_kwargs(
        workspace_id=workspace_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    workspace_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RunMigrationImportBody | Unset = UNSET,

) -> Error | RunMigrationImportResponse202 | None:
    """ Run the import again

     Queue another import from the source PMS — for example messages after the first pass, or only
    reservations changed since a date. Progress shows on `GET /v1/migrations/{workspaceId}`.

    Args:
        workspace_id (int):
        body (RunMigrationImportBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RunMigrationImportResponse202
     """


    return sync_detailed(
        workspace_id=workspace_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    workspace_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RunMigrationImportBody | Unset = UNSET,

) -> Response[Error | RunMigrationImportResponse202]:
    """ Run the import again

     Queue another import from the source PMS — for example messages after the first pass, or only
    reservations changed since a date. Progress shows on `GET /v1/migrations/{workspaceId}`.

    Args:
        workspace_id (int):
        body (RunMigrationImportBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RunMigrationImportResponse202]
     """


    kwargs = _get_kwargs(
        workspace_id=workspace_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    workspace_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: RunMigrationImportBody | Unset = UNSET,

) -> Error | RunMigrationImportResponse202 | None:
    """ Run the import again

     Queue another import from the source PMS — for example messages after the first pass, or only
    reservations changed since a date. Progress shows on `GET /v1/migrations/{workspaceId}`.

    Args:
        workspace_id (int):
        body (RunMigrationImportBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RunMigrationImportResponse202
     """


    return (await asyncio_detailed(
        workspace_id=workspace_id,
client=client,
body=body,

    )).parsed
