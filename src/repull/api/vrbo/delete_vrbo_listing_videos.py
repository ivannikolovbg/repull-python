from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_vrbo_listing_videos_response_200 import DeleteVrboListingVideosResponse200
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    video_id: str,
    vrbo_listing_number: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["videoId"] = video_id

    params["vrboListingNumber"] = vrbo_listing_number


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/channels/vrbo/listings/{id}/videos".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteVrboListingVideosResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = DeleteVrboListingVideosResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

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

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

    if response.status_code == 504:
        response_504 = Error.from_dict(response.json())



        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteVrboListingVideosResponse200 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    video_id: str,
    vrbo_listing_number: str | Unset = UNSET,

) -> Response[DeleteVrboListingVideosResponse200 | Error]:
    """ Remove videos from the Vrbo listing

     Remove videos from the listing's existing Vrbo listing by their `id` (from `GET …/videos`). The
    answer lists the videos Vrbo has left.

    Needs full access (`403 vrbo_messaging_access` otherwise).

    Args:
        id (str):
        video_id (str):  Example: 8a1f2c3d.
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteVrboListingVideosResponse200 | Error]
     """


    kwargs = _get_kwargs(
        id=id,
video_id=video_id,
vrbo_listing_number=vrbo_listing_number,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    video_id: str,
    vrbo_listing_number: str | Unset = UNSET,

) -> DeleteVrboListingVideosResponse200 | Error | None:
    """ Remove videos from the Vrbo listing

     Remove videos from the listing's existing Vrbo listing by their `id` (from `GET …/videos`). The
    answer lists the videos Vrbo has left.

    Needs full access (`403 vrbo_messaging_access` otherwise).

    Args:
        id (str):
        video_id (str):  Example: 8a1f2c3d.
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteVrboListingVideosResponse200 | Error
     """


    return sync_detailed(
        id=id,
client=client,
video_id=video_id,
vrbo_listing_number=vrbo_listing_number,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    video_id: str,
    vrbo_listing_number: str | Unset = UNSET,

) -> Response[DeleteVrboListingVideosResponse200 | Error]:
    """ Remove videos from the Vrbo listing

     Remove videos from the listing's existing Vrbo listing by their `id` (from `GET …/videos`). The
    answer lists the videos Vrbo has left.

    Needs full access (`403 vrbo_messaging_access` otherwise).

    Args:
        id (str):
        video_id (str):  Example: 8a1f2c3d.
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteVrboListingVideosResponse200 | Error]
     """


    kwargs = _get_kwargs(
        id=id,
video_id=video_id,
vrbo_listing_number=vrbo_listing_number,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    video_id: str,
    vrbo_listing_number: str | Unset = UNSET,

) -> DeleteVrboListingVideosResponse200 | Error | None:
    """ Remove videos from the Vrbo listing

     Remove videos from the listing's existing Vrbo listing by their `id` (from `GET …/videos`). The
    answer lists the videos Vrbo has left.

    Needs full access (`403 vrbo_messaging_access` otherwise).

    Args:
        id (str):
        video_id (str):  Example: 8a1f2c3d.
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteVrboListingVideosResponse200 | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
video_id=video_id,
vrbo_listing_number=vrbo_listing_number,

    )).parsed
