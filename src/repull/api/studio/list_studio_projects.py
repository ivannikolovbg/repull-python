from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_studio_projects_response_200 import ListStudioProjectsResponse200
from ...models.studio_error import StudioError
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/studio/projects",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListStudioProjectsResponse200 | StudioError | None:
    if response.status_code == 200:
        response_200 = ListStudioProjectsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = StudioError.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = StudioError.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListStudioProjectsResponse200 | StudioError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[ListStudioProjectsResponse200 | StudioError]:
    """ List Studio projects

     Returns every Studio project owned by the authenticated account, excluding soft-deleted ones. Use
    this to populate a project picker or dashboard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListStudioProjectsResponse200 | StudioError]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> ListStudioProjectsResponse200 | StudioError | None:
    """ List Studio projects

     Returns every Studio project owned by the authenticated account, excluding soft-deleted ones. Use
    this to populate a project picker or dashboard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListStudioProjectsResponse200 | StudioError
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[ListStudioProjectsResponse200 | StudioError]:
    """ List Studio projects

     Returns every Studio project owned by the authenticated account, excluding soft-deleted ones. Use
    this to populate a project picker or dashboard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListStudioProjectsResponse200 | StudioError]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> ListStudioProjectsResponse200 | StudioError | None:
    """ List Studio projects

     Returns every Studio project owned by the authenticated account, excluding soft-deleted ones. Use
    this to populate a project picker or dashboard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListStudioProjectsResponse200 | StudioError
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
