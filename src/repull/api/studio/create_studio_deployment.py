from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_studio_deployment_body import CreateStudioDeploymentBody
from ...models.create_studio_deployment_response_201 import CreateStudioDeploymentResponse201
from ...models.studio_error import StudioError
from typing import cast



def _get_kwargs(
    *,
    body: CreateStudioDeploymentBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/studio/deployments",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateStudioDeploymentResponse201 | StudioError | None:
    if response.status_code == 201:
        response_201 = CreateStudioDeploymentResponse201.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateStudioDeploymentResponse201 | StudioError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateStudioDeploymentBody,

) -> Response[CreateStudioDeploymentResponse201 | StudioError]:
    """ Trigger a Studio deployment

     Kicks off a new deployment for a project — Repull provisions a Fly.io machine, writes the subdomain
    DNS record, and builds the project. The response returns immediately with `provisioning` status;
    poll `GET /api/studio/deployments/{id}` until `live`.

    Args:
        body (CreateStudioDeploymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateStudioDeploymentResponse201 | StudioError]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateStudioDeploymentBody,

) -> CreateStudioDeploymentResponse201 | StudioError | None:
    """ Trigger a Studio deployment

     Kicks off a new deployment for a project — Repull provisions a Fly.io machine, writes the subdomain
    DNS record, and builds the project. The response returns immediately with `provisioning` status;
    poll `GET /api/studio/deployments/{id}` until `live`.

    Args:
        body (CreateStudioDeploymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateStudioDeploymentResponse201 | StudioError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateStudioDeploymentBody,

) -> Response[CreateStudioDeploymentResponse201 | StudioError]:
    """ Trigger a Studio deployment

     Kicks off a new deployment for a project — Repull provisions a Fly.io machine, writes the subdomain
    DNS record, and builds the project. The response returns immediately with `provisioning` status;
    poll `GET /api/studio/deployments/{id}` until `live`.

    Args:
        body (CreateStudioDeploymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateStudioDeploymentResponse201 | StudioError]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateStudioDeploymentBody,

) -> CreateStudioDeploymentResponse201 | StudioError | None:
    """ Trigger a Studio deployment

     Kicks off a new deployment for a project — Repull provisions a Fly.io machine, writes the subdomain
    DNS record, and builds the project. The response returns immediately with `provisioning` status;
    poll `GET /api/studio/deployments/{id}` until `live`.

    Args:
        body (CreateStudioDeploymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateStudioDeploymentResponse201 | StudioError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
