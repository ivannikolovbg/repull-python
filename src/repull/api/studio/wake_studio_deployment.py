from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.studio_error import StudioError
from ...models.wake_studio_deployment_response_200 import WakeStudioDeploymentResponse200
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/studio/deployments/{id}/wake".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> StudioError | WakeStudioDeploymentResponse200 | None:
    if response.status_code == 200:
        response_200 = WakeStudioDeploymentResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = StudioError.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = StudioError.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = StudioError.from_dict(response.json())



        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[StudioError | WakeStudioDeploymentResponse200]:
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

) -> Response[StudioError | WakeStudioDeploymentResponse200]:
    """ Wake a suspended Studio deployment

     Resumes a previously suspended deployment — Repull restarts the Fly.io machine and the URL becomes
    reachable again once `status` returns to `live`.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StudioError | WakeStudioDeploymentResponse200]
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

) -> StudioError | WakeStudioDeploymentResponse200 | None:
    """ Wake a suspended Studio deployment

     Resumes a previously suspended deployment — Repull restarts the Fly.io machine and the URL becomes
    reachable again once `status` returns to `live`.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StudioError | WakeStudioDeploymentResponse200
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[StudioError | WakeStudioDeploymentResponse200]:
    """ Wake a suspended Studio deployment

     Resumes a previously suspended deployment — Repull restarts the Fly.io machine and the URL becomes
    reachable again once `status` returns to `live`.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StudioError | WakeStudioDeploymentResponse200]
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

) -> StudioError | WakeStudioDeploymentResponse200 | None:
    """ Wake a suspended Studio deployment

     Resumes a previously suspended deployment — Repull restarts the Fly.io machine and the URL becomes
    reachable again once `status` returns to `live`.

    Args:
        id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StudioError | WakeStudioDeploymentResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
