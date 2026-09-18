from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.set_airbnb_listing_cover_photo_body import SetAirbnbListingCoverPhotoBody
from ...models.set_airbnb_listing_cover_photo_response_200 import SetAirbnbListingCoverPhotoResponse200
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: SetAirbnbListingCoverPhotoBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/airbnb/listings/{id}/photos/cover".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SetAirbnbListingCoverPhotoResponse200 | None:
    if response.status_code == 200:
        response_200 = SetAirbnbListingCoverPhotoResponse200.from_dict(response.json())



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

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SetAirbnbListingCoverPhotoResponse200]:
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
    body: SetAirbnbListingCoverPhotoBody,

) -> Response[Error | SetAirbnbListingCoverPhotoResponse200]:
    r""" Set the Airbnb cover photo

     Choose which photo leads the listing. **Write-side** — calls Airbnb upstream.

    Airbnb has no \"cover\" field: the cover is the first photo of the tour, so this is a position
    write. Usually it is a single upstream request — the chosen photo takes a position below the current
    first one and nothing else moves. When the tour already starts at position 1 and there is no room
    below it, the tour is renumbered instead, one request per photo whose position actually changes,
    with the same stop-at-first-failure reporting as `PUT /photos/order` (`applied`, `failed_photo_id`,
    `not_attempted`; re-send the identical body to finish).

    The listing thumbnail — what every list view renders — is repointed at the new cover, so the change
    is not visible only inside the photo tour.

    The photo must already be in our cached copy of the tour; one uploaded since the last sync returns
    `404`, and `PATCH /photos` can set its position in the meantime.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (SetAirbnbListingCoverPhotoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SetAirbnbListingCoverPhotoResponse200]
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
    body: SetAirbnbListingCoverPhotoBody,

) -> Error | SetAirbnbListingCoverPhotoResponse200 | None:
    r""" Set the Airbnb cover photo

     Choose which photo leads the listing. **Write-side** — calls Airbnb upstream.

    Airbnb has no \"cover\" field: the cover is the first photo of the tour, so this is a position
    write. Usually it is a single upstream request — the chosen photo takes a position below the current
    first one and nothing else moves. When the tour already starts at position 1 and there is no room
    below it, the tour is renumbered instead, one request per photo whose position actually changes,
    with the same stop-at-first-failure reporting as `PUT /photos/order` (`applied`, `failed_photo_id`,
    `not_attempted`; re-send the identical body to finish).

    The listing thumbnail — what every list view renders — is repointed at the new cover, so the change
    is not visible only inside the photo tour.

    The photo must already be in our cached copy of the tour; one uploaded since the last sync returns
    `404`, and `PATCH /photos` can set its position in the meantime.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (SetAirbnbListingCoverPhotoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SetAirbnbListingCoverPhotoResponse200
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
    body: SetAirbnbListingCoverPhotoBody,

) -> Response[Error | SetAirbnbListingCoverPhotoResponse200]:
    r""" Set the Airbnb cover photo

     Choose which photo leads the listing. **Write-side** — calls Airbnb upstream.

    Airbnb has no \"cover\" field: the cover is the first photo of the tour, so this is a position
    write. Usually it is a single upstream request — the chosen photo takes a position below the current
    first one and nothing else moves. When the tour already starts at position 1 and there is no room
    below it, the tour is renumbered instead, one request per photo whose position actually changes,
    with the same stop-at-first-failure reporting as `PUT /photos/order` (`applied`, `failed_photo_id`,
    `not_attempted`; re-send the identical body to finish).

    The listing thumbnail — what every list view renders — is repointed at the new cover, so the change
    is not visible only inside the photo tour.

    The photo must already be in our cached copy of the tour; one uploaded since the last sync returns
    `404`, and `PATCH /photos` can set its position in the meantime.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (SetAirbnbListingCoverPhotoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SetAirbnbListingCoverPhotoResponse200]
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
    body: SetAirbnbListingCoverPhotoBody,

) -> Error | SetAirbnbListingCoverPhotoResponse200 | None:
    r""" Set the Airbnb cover photo

     Choose which photo leads the listing. **Write-side** — calls Airbnb upstream.

    Airbnb has no \"cover\" field: the cover is the first photo of the tour, so this is a position
    write. Usually it is a single upstream request — the chosen photo takes a position below the current
    first one and nothing else moves. When the tour already starts at position 1 and there is no room
    below it, the tour is renumbered instead, one request per photo whose position actually changes,
    with the same stop-at-first-failure reporting as `PUT /photos/order` (`applied`, `failed_photo_id`,
    `not_attempted`; re-send the identical body to finish).

    The listing thumbnail — what every list view renders — is repointed at the new cover, so the change
    is not visible only inside the photo tour.

    The photo must already be in our cached copy of the tour; one uploaded since the last sync returns
    `404`, and `PATCH /photos` can set its position in the meantime.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (SetAirbnbListingCoverPhotoBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SetAirbnbListingCoverPhotoResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
