from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.listing_photo_upload_url_request import ListingPhotoUploadUrlRequest
from ...models.listing_photo_upload_url_response import ListingPhotoUploadUrlResponse
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ListingPhotoUploadUrlRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/{id}/photos/upload-url".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListingPhotoUploadUrlResponse | None:
    if response.status_code == 200:
        response_200 = ListingPhotoUploadUrlResponse.from_dict(response.json())



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

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListingPhotoUploadUrlResponse]:
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
    body: ListingPhotoUploadUrlRequest,

) -> Response[Error | ListingPhotoUploadUrlResponse]:
    """ Mint a direct-to-storage photo upload URL

     Mints a short-lived signed upload URL + token for a listing photo. **The client PUTs the raw file
    bytes directly to the returned `uploadUrl` — the file bytes never pass through the Repull API or
    main vanio.** This endpoint only mints the URL; do not POST the file itself here, it will not be
    accepted.

    Flow: (1) POST here with `fileName`/`fileType`/optional `fileSize` to get `{ uploadUrl, token, path,
    publicUrl, expiresIn }`; (2) PUT the raw file bytes to `uploadUrl` from the client; (3) `publicUrl`
    is the durable URL for the uploaded photo — attach it to the listing via `PUT
    /v1/listings/{id}/content` (`photos` field) or list it back via `GET /v1/listings/{id}/photos`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        body (ListingPhotoUploadUrlRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingPhotoUploadUrlResponse]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingPhotoUploadUrlRequest,

) -> Error | ListingPhotoUploadUrlResponse | None:
    """ Mint a direct-to-storage photo upload URL

     Mints a short-lived signed upload URL + token for a listing photo. **The client PUTs the raw file
    bytes directly to the returned `uploadUrl` — the file bytes never pass through the Repull API or
    main vanio.** This endpoint only mints the URL; do not POST the file itself here, it will not be
    accepted.

    Flow: (1) POST here with `fileName`/`fileType`/optional `fileSize` to get `{ uploadUrl, token, path,
    publicUrl, expiresIn }`; (2) PUT the raw file bytes to `uploadUrl` from the client; (3) `publicUrl`
    is the durable URL for the uploaded photo — attach it to the listing via `PUT
    /v1/listings/{id}/content` (`photos` field) or list it back via `GET /v1/listings/{id}/photos`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        body (ListingPhotoUploadUrlRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingPhotoUploadUrlResponse
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingPhotoUploadUrlRequest,

) -> Response[Error | ListingPhotoUploadUrlResponse]:
    """ Mint a direct-to-storage photo upload URL

     Mints a short-lived signed upload URL + token for a listing photo. **The client PUTs the raw file
    bytes directly to the returned `uploadUrl` — the file bytes never pass through the Repull API or
    main vanio.** This endpoint only mints the URL; do not POST the file itself here, it will not be
    accepted.

    Flow: (1) POST here with `fileName`/`fileType`/optional `fileSize` to get `{ uploadUrl, token, path,
    publicUrl, expiresIn }`; (2) PUT the raw file bytes to `uploadUrl` from the client; (3) `publicUrl`
    is the durable URL for the uploaded photo — attach it to the listing via `PUT
    /v1/listings/{id}/content` (`photos` field) or list it back via `GET /v1/listings/{id}/photos`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        body (ListingPhotoUploadUrlRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingPhotoUploadUrlResponse]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingPhotoUploadUrlRequest,

) -> Error | ListingPhotoUploadUrlResponse | None:
    """ Mint a direct-to-storage photo upload URL

     Mints a short-lived signed upload URL + token for a listing photo. **The client PUTs the raw file
    bytes directly to the returned `uploadUrl` — the file bytes never pass through the Repull API or
    main vanio.** This endpoint only mints the URL; do not POST the file itself here, it will not be
    accepted.

    Flow: (1) POST here with `fileName`/`fileType`/optional `fileSize` to get `{ uploadUrl, token, path,
    publicUrl, expiresIn }`; (2) PUT the raw file bytes to `uploadUrl` from the client; (3) `publicUrl`
    is the durable URL for the uploaded photo — attach it to the listing via `PUT
    /v1/listings/{id}/content` (`photos` field) or list it back via `GET /v1/listings/{id}/photos`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        body (ListingPhotoUploadUrlRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingPhotoUploadUrlResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
