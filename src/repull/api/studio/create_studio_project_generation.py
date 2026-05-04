from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_studio_project_generation_body import CreateStudioProjectGenerationBody
from ...models.create_studio_project_generation_response_201 import CreateStudioProjectGenerationResponse201
from ...models.studio_error import StudioError
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    body: CreateStudioProjectGenerationBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/studio/projects/{id}/generations".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateStudioProjectGenerationResponse201 | StudioError | None:
    if response.status_code == 201:
        response_201 = CreateStudioProjectGenerationResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = StudioError.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = StudioError.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = StudioError.from_dict(response.json())



        return response_404

    if response.status_code == 429:
        response_429 = StudioError.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateStudioProjectGenerationResponse201 | StudioError]:
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
    body: CreateStudioProjectGenerationBody,

) -> Response[CreateStudioProjectGenerationResponse201 | StudioError]:
    """ Run a Studio generation

     Records a generation run scoped to a single project — Repull AI takes the prompt, generates the
    response, and stores it on the project timeline. Use this when you want generation history; for one-
    shot completions without persistence use `POST /api/studio/generate`.

    Args:
        id (UUID):
        body (CreateStudioProjectGenerationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateStudioProjectGenerationResponse201 | StudioError]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateStudioProjectGenerationBody,

) -> CreateStudioProjectGenerationResponse201 | StudioError | None:
    """ Run a Studio generation

     Records a generation run scoped to a single project — Repull AI takes the prompt, generates the
    response, and stores it on the project timeline. Use this when you want generation history; for one-
    shot completions without persistence use `POST /api/studio/generate`.

    Args:
        id (UUID):
        body (CreateStudioProjectGenerationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateStudioProjectGenerationResponse201 | StudioError
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateStudioProjectGenerationBody,

) -> Response[CreateStudioProjectGenerationResponse201 | StudioError]:
    """ Run a Studio generation

     Records a generation run scoped to a single project — Repull AI takes the prompt, generates the
    response, and stores it on the project timeline. Use this when you want generation history; for one-
    shot completions without persistence use `POST /api/studio/generate`.

    Args:
        id (UUID):
        body (CreateStudioProjectGenerationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateStudioProjectGenerationResponse201 | StudioError]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CreateStudioProjectGenerationBody,

) -> CreateStudioProjectGenerationResponse201 | StudioError | None:
    """ Run a Studio generation

     Records a generation run scoped to a single project — Repull AI takes the prompt, generates the
    response, and stores it on the project timeline. Use this when you want generation history; for one-
    shot completions without persistence use `POST /api/studio/generate`.

    Args:
        id (UUID):
        body (CreateStudioProjectGenerationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateStudioProjectGenerationResponse201 | StudioError
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
