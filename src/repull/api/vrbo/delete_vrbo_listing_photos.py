from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_vrbo_listing_photos_response_200 import DeleteVrboListingPhotosResponse200
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    photo_id: str,
    vrbo_listing_number: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["photoId"] = photo_id

    params["vrboListingNumber"] = vrbo_listing_number


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/channels/vrbo/listings/{id}/photos".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteVrboListingPhotosResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = DeleteVrboListingPhotosResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteVrboListingPhotosResponse200 | Error]:
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
    photo_id: str,
    vrbo_listing_number: str | Unset = UNSET,

) -> Response[DeleteVrboListingPhotosResponse200 | Error]:
    """ Remove Vrbo photos

     Remove photos by `photoId` (comma-separated for several). Photo ids are the `id`s of GET …/photos.

    **When Vrbo refuses** a value the answer is `422 vrbo_rejected` with Vrbo's own message, the refused
    fields in `errors` and what Vrbo has now in `data`. A malformed body is `422 invalid_params` naming
    the field, and nothing is sent to Vrbo.

    Needs a Vrbo account connected with full access: one connected with messaging access answers `403
    vrbo_messaging_access`. Returns `403 listing_inactive` when the listing is inactive.

    Args:
        id (str):
        photo_id (str):  Example: 1234567.
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteVrboListingPhotosResponse200 | Error]
     """


    kwargs = _get_kwargs(
        id=id,
photo_id=photo_id,
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
    photo_id: str,
    vrbo_listing_number: str | Unset = UNSET,

) -> DeleteVrboListingPhotosResponse200 | Error | None:
    """ Remove Vrbo photos

     Remove photos by `photoId` (comma-separated for several). Photo ids are the `id`s of GET …/photos.

    **When Vrbo refuses** a value the answer is `422 vrbo_rejected` with Vrbo's own message, the refused
    fields in `errors` and what Vrbo has now in `data`. A malformed body is `422 invalid_params` naming
    the field, and nothing is sent to Vrbo.

    Needs a Vrbo account connected with full access: one connected with messaging access answers `403
    vrbo_messaging_access`. Returns `403 listing_inactive` when the listing is inactive.

    Args:
        id (str):
        photo_id (str):  Example: 1234567.
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteVrboListingPhotosResponse200 | Error
     """


    return sync_detailed(
        id=id,
client=client,
photo_id=photo_id,
vrbo_listing_number=vrbo_listing_number,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    photo_id: str,
    vrbo_listing_number: str | Unset = UNSET,

) -> Response[DeleteVrboListingPhotosResponse200 | Error]:
    """ Remove Vrbo photos

     Remove photos by `photoId` (comma-separated for several). Photo ids are the `id`s of GET …/photos.

    **When Vrbo refuses** a value the answer is `422 vrbo_rejected` with Vrbo's own message, the refused
    fields in `errors` and what Vrbo has now in `data`. A malformed body is `422 invalid_params` naming
    the field, and nothing is sent to Vrbo.

    Needs a Vrbo account connected with full access: one connected with messaging access answers `403
    vrbo_messaging_access`. Returns `403 listing_inactive` when the listing is inactive.

    Args:
        id (str):
        photo_id (str):  Example: 1234567.
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteVrboListingPhotosResponse200 | Error]
     """


    kwargs = _get_kwargs(
        id=id,
photo_id=photo_id,
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
    photo_id: str,
    vrbo_listing_number: str | Unset = UNSET,

) -> DeleteVrboListingPhotosResponse200 | Error | None:
    """ Remove Vrbo photos

     Remove photos by `photoId` (comma-separated for several). Photo ids are the `id`s of GET …/photos.

    **When Vrbo refuses** a value the answer is `422 vrbo_rejected` with Vrbo's own message, the refused
    fields in `errors` and what Vrbo has now in `data`. A malformed body is `422 invalid_params` naming
    the field, and nothing is sent to Vrbo.

    Needs a Vrbo account connected with full access: one connected with messaging access answers `403
    vrbo_messaging_access`. Returns `403 listing_inactive` when the listing is inactive.

    Args:
        id (str):
        photo_id (str):  Example: 1234567.
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteVrboListingPhotosResponse200 | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
photo_id=photo_id,
vrbo_listing_number=vrbo_listing_number,

    )).parsed
