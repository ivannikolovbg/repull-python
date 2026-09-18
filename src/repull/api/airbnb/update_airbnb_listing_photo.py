from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.update_airbnb_listing_photo_body import UpdateAirbnbListingPhotoBody
from ...models.update_airbnb_listing_photo_response_200 import UpdateAirbnbListingPhotoResponse200
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: UpdateAirbnbListingPhotoBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/channels/airbnb/listings/{id}/photos".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | UpdateAirbnbListingPhotoResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateAirbnbListingPhotoResponse200.from_dict(response.json())



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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | UpdateAirbnbListingPhotoResponse200]:
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
    body: UpdateAirbnbListingPhotoBody,

) -> Response[Error | UpdateAirbnbListingPhotoResponse200]:
    """ Update an Airbnb photo

     Change one photo's caption, its position in the tour, the room it is filed under, or its metadata.
    **Write-side** — calls Airbnb upstream.

    Airbnb's photo endpoints are keyed by photo id alone, so the photo is proven to belong to the
    listing named in the path before anything is sent; a photo from another listing returns `404`, the
    same answer a photo that does not exist gets.

    On success both stored copies are updated — the Airbnb mirror `GET /photos` serves AND the canonical
    photo tour behind `GET /v1/listings/{id}` — so a read straight after this write returns the new
    value instead of waiting for the next sync. `stored` says whether that succeeded; `false` means
    Airbnb accepted the change but our copy will only catch up at the next sync.

    To move several photos at once use `PUT /photos/order`: it is one call instead of N, it validates
    the whole order before writing anything, and it reports exactly what landed if Airbnb refuses part-
    way.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UpdateAirbnbListingPhotoBody): `photo_id` plus at least one of `caption`,
            `sort_order`, `room_id`, `metadata`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbListingPhotoResponse200]
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
    body: UpdateAirbnbListingPhotoBody,

) -> Error | UpdateAirbnbListingPhotoResponse200 | None:
    """ Update an Airbnb photo

     Change one photo's caption, its position in the tour, the room it is filed under, or its metadata.
    **Write-side** — calls Airbnb upstream.

    Airbnb's photo endpoints are keyed by photo id alone, so the photo is proven to belong to the
    listing named in the path before anything is sent; a photo from another listing returns `404`, the
    same answer a photo that does not exist gets.

    On success both stored copies are updated — the Airbnb mirror `GET /photos` serves AND the canonical
    photo tour behind `GET /v1/listings/{id}` — so a read straight after this write returns the new
    value instead of waiting for the next sync. `stored` says whether that succeeded; `false` means
    Airbnb accepted the change but our copy will only catch up at the next sync.

    To move several photos at once use `PUT /photos/order`: it is one call instead of N, it validates
    the whole order before writing anything, and it reports exactly what landed if Airbnb refuses part-
    way.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UpdateAirbnbListingPhotoBody): `photo_id` plus at least one of `caption`,
            `sort_order`, `room_id`, `metadata`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbListingPhotoResponse200
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
    body: UpdateAirbnbListingPhotoBody,

) -> Response[Error | UpdateAirbnbListingPhotoResponse200]:
    """ Update an Airbnb photo

     Change one photo's caption, its position in the tour, the room it is filed under, or its metadata.
    **Write-side** — calls Airbnb upstream.

    Airbnb's photo endpoints are keyed by photo id alone, so the photo is proven to belong to the
    listing named in the path before anything is sent; a photo from another listing returns `404`, the
    same answer a photo that does not exist gets.

    On success both stored copies are updated — the Airbnb mirror `GET /photos` serves AND the canonical
    photo tour behind `GET /v1/listings/{id}` — so a read straight after this write returns the new
    value instead of waiting for the next sync. `stored` says whether that succeeded; `false` means
    Airbnb accepted the change but our copy will only catch up at the next sync.

    To move several photos at once use `PUT /photos/order`: it is one call instead of N, it validates
    the whole order before writing anything, and it reports exactly what landed if Airbnb refuses part-
    way.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UpdateAirbnbListingPhotoBody): `photo_id` plus at least one of `caption`,
            `sort_order`, `room_id`, `metadata`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbListingPhotoResponse200]
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
    body: UpdateAirbnbListingPhotoBody,

) -> Error | UpdateAirbnbListingPhotoResponse200 | None:
    """ Update an Airbnb photo

     Change one photo's caption, its position in the tour, the room it is filed under, or its metadata.
    **Write-side** — calls Airbnb upstream.

    Airbnb's photo endpoints are keyed by photo id alone, so the photo is proven to belong to the
    listing named in the path before anything is sent; a photo from another listing returns `404`, the
    same answer a photo that does not exist gets.

    On success both stored copies are updated — the Airbnb mirror `GET /photos` serves AND the canonical
    photo tour behind `GET /v1/listings/{id}` — so a read straight after this write returns the new
    value instead of waiting for the next sync. `stored` says whether that succeeded; `false` means
    Airbnb accepted the change but our copy will only catch up at the next sync.

    To move several photos at once use `PUT /photos/order`: it is one call instead of N, it validates
    the whole order before writing anything, and it reports exactly what landed if Airbnb refuses part-
    way.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UpdateAirbnbListingPhotoBody): `photo_id` plus at least one of `caption`,
            `sort_order`, `room_id`, `metadata`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbListingPhotoResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
