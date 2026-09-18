from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.upload_airbnb_listing_photos_body import UploadAirbnbListingPhotosBody
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: UploadAirbnbListingPhotosBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/airbnb/listings/{id}/photos".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
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
    body: UploadAirbnbListingPhotosBody,

) -> Response[Any | Error]:
    """ Upload photos to Airbnb

     Upload one or more photos to an Airbnb listing.

    `image` is base64 image DATA, not a url — a `data:image/jpeg;base64,…` prefix is accepted and
    stripped, and the decoded image must be under 25 MB. (This operation previously documented public
    image urls that Airbnb would fetch. It never did: a url arrived at Airbnb as a ~60-byte image.)

    Airbnb assigns the photo id and CDN urls, so the newly uploaded photos appear in `GET /photos` after
    the next sync. Caption, order and room assignment can be set straight away with `PATCH /photos`,
    `PUT /photos/order` and `PUT /photos/cover`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UploadAirbnbListingPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadAirbnbListingPhotosBody,

) -> Any | Error | None:
    """ Upload photos to Airbnb

     Upload one or more photos to an Airbnb listing.

    `image` is base64 image DATA, not a url — a `data:image/jpeg;base64,…` prefix is accepted and
    stripped, and the decoded image must be under 25 MB. (This operation previously documented public
    image urls that Airbnb would fetch. It never did: a url arrived at Airbnb as a ~60-byte image.)

    Airbnb assigns the photo id and CDN urls, so the newly uploaded photos appear in `GET /photos` after
    the next sync. Caption, order and room assignment can be set straight away with `PATCH /photos`,
    `PUT /photos/order` and `PUT /photos/cover`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UploadAirbnbListingPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadAirbnbListingPhotosBody,

) -> Response[Any | Error]:
    """ Upload photos to Airbnb

     Upload one or more photos to an Airbnb listing.

    `image` is base64 image DATA, not a url — a `data:image/jpeg;base64,…` prefix is accepted and
    stripped, and the decoded image must be under 25 MB. (This operation previously documented public
    image urls that Airbnb would fetch. It never did: a url arrived at Airbnb as a ~60-byte image.)

    Airbnb assigns the photo id and CDN urls, so the newly uploaded photos appear in `GET /photos` after
    the next sync. Caption, order and room assignment can be set straight away with `PATCH /photos`,
    `PUT /photos/order` and `PUT /photos/cover`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UploadAirbnbListingPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadAirbnbListingPhotosBody,

) -> Any | Error | None:
    """ Upload photos to Airbnb

     Upload one or more photos to an Airbnb listing.

    `image` is base64 image DATA, not a url — a `data:image/jpeg;base64,…` prefix is accepted and
    stripped, and the decoded image must be under 25 MB. (This operation previously documented public
    image urls that Airbnb would fetch. It never did: a url arrived at Airbnb as a ~60-byte image.)

    Airbnb assigns the photo id and CDN urls, so the newly uploaded photos appear in `GET /photos` after
    the next sync. Caption, order and room assignment can be set straight away with `PATCH /photos`,
    `PUT /photos/order` and `PUT /photos/cover`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UploadAirbnbListingPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
