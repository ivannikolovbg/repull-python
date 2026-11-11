from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_vrbo_publish_job_response_200 import GetVrboPublishJobResponse200
from typing import cast



def _get_kwargs(
    id: int,
    *,
    job_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["jobId"] = job_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/{id}/publish/vrbo".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetVrboPublishJobResponse200 | None:
    if response.status_code == 200:
        response_200 = GetVrboPublishJobResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetVrboPublishJobResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    job_id: str,

) -> Response[Error | GetVrboPublishJobResponse200]:
    """ Progress of a Vrbo listing creation

     Each step Vrbo has finished, Vrbo's reason when it failed, the new Vrbo listing number once
    published, and photos Vrbo's review refused. When Vrbo has published the listing, this read links
    the new unit to the listing with calendar sync on and queues the whole calendar — poll until
    `linked` is true. A job is remembered while it runs and for a while after; an unknown job is `404`
    (publish again to resume).

    Args:
        id (int):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboPublishJobResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
job_id=job_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    job_id: str,

) -> Error | GetVrboPublishJobResponse200 | None:
    """ Progress of a Vrbo listing creation

     Each step Vrbo has finished, Vrbo's reason when it failed, the new Vrbo listing number once
    published, and photos Vrbo's review refused. When Vrbo has published the listing, this read links
    the new unit to the listing with calendar sync on and queues the whole calendar — poll until
    `linked` is true. A job is remembered while it runs and for a while after; an unknown job is `404`
    (publish again to resume).

    Args:
        id (int):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboPublishJobResponse200
     """


    return sync_detailed(
        id=id,
client=client,
job_id=job_id,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    job_id: str,

) -> Response[Error | GetVrboPublishJobResponse200]:
    """ Progress of a Vrbo listing creation

     Each step Vrbo has finished, Vrbo's reason when it failed, the new Vrbo listing number once
    published, and photos Vrbo's review refused. When Vrbo has published the listing, this read links
    the new unit to the listing with calendar sync on and queues the whole calendar — poll until
    `linked` is true. A job is remembered while it runs and for a while after; an unknown job is `404`
    (publish again to resume).

    Args:
        id (int):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboPublishJobResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
job_id=job_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    job_id: str,

) -> Error | GetVrboPublishJobResponse200 | None:
    """ Progress of a Vrbo listing creation

     Each step Vrbo has finished, Vrbo's reason when it failed, the new Vrbo listing number once
    published, and photos Vrbo's review refused. When Vrbo has published the listing, this read links
    the new unit to the listing with calendar sync on and queues the whole calendar — poll until
    `linked` is true. A job is remembered while it runs and for a while after; an unknown job is `404`
    (publish again to resume).

    Args:
        id (int):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboPublishJobResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
job_id=job_id,

    )).parsed
