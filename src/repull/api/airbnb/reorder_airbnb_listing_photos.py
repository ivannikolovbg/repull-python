from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.reorder_airbnb_listing_photos_body import ReorderAirbnbListingPhotosBody
from ...models.reorder_airbnb_listing_photos_response_200 import ReorderAirbnbListingPhotosResponse200
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: ReorderAirbnbListingPhotosBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/airbnb/listings/{id}/photos/order".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ReorderAirbnbListingPhotosResponse200 | None:
    if response.status_code == 200:
        response_200 = ReorderAirbnbListingPhotosResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ReorderAirbnbListingPhotosResponse200]:
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
    body: ReorderAirbnbListingPhotosBody,

) -> Response[Error | ReorderAirbnbListingPhotosResponse200]:
    r""" Reorder the Airbnb photo tour

     Set the order of a listing's photo tour in one call. **Write-side** — calls Airbnb upstream.

    Send the photo ids in the order you want them shown, first photo first. Ids you leave out keep their
    current relative order behind the ones you list, so moving one photo to the front is
    `{\"photo_ids\": [\"<id>\"]}`. Positions are then written as a dense run starting at 1.

    Airbnb has no bulk photo endpoint — order is one `sort_order` per photo — so this saves a loop of up
    to 200 requests against your rate limit and makes the partial-failure case reportable. How much is
    atomic:

    - Everything is validated before anything is written. A duplicate id, an id that is not on this
    listing, an inactive listing or a missing connection all fail with **zero** upstream writes.
    - Only photos whose position actually changes are written; re-sending the order you already have
    writes nothing.
    - On the first upstream failure the run stops — nothing after it is attempted. The error carries
    `applied`, `failed_photo_id` and `not_attempted`, uses Airbnb's own status (`422` rejected / `403`
    reauth / `429` / `502`), and the operation is idempotent: re-send the identical body to finish the
    run.
    - Our stored copy records what actually landed, never the intent.

    Validation is against our cached copy of the tour, so a listing whose photos have never synced
    returns `404` — use `PATCH /photos` (which needs no cache) until the first sync lands.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (ReorderAirbnbListingPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReorderAirbnbListingPhotosResponse200]
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
    body: ReorderAirbnbListingPhotosBody,

) -> Error | ReorderAirbnbListingPhotosResponse200 | None:
    r""" Reorder the Airbnb photo tour

     Set the order of a listing's photo tour in one call. **Write-side** — calls Airbnb upstream.

    Send the photo ids in the order you want them shown, first photo first. Ids you leave out keep their
    current relative order behind the ones you list, so moving one photo to the front is
    `{\"photo_ids\": [\"<id>\"]}`. Positions are then written as a dense run starting at 1.

    Airbnb has no bulk photo endpoint — order is one `sort_order` per photo — so this saves a loop of up
    to 200 requests against your rate limit and makes the partial-failure case reportable. How much is
    atomic:

    - Everything is validated before anything is written. A duplicate id, an id that is not on this
    listing, an inactive listing or a missing connection all fail with **zero** upstream writes.
    - Only photos whose position actually changes are written; re-sending the order you already have
    writes nothing.
    - On the first upstream failure the run stops — nothing after it is attempted. The error carries
    `applied`, `failed_photo_id` and `not_attempted`, uses Airbnb's own status (`422` rejected / `403`
    reauth / `429` / `502`), and the operation is idempotent: re-send the identical body to finish the
    run.
    - Our stored copy records what actually landed, never the intent.

    Validation is against our cached copy of the tour, so a listing whose photos have never synced
    returns `404` — use `PATCH /photos` (which needs no cache) until the first sync lands.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (ReorderAirbnbListingPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReorderAirbnbListingPhotosResponse200
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
    body: ReorderAirbnbListingPhotosBody,

) -> Response[Error | ReorderAirbnbListingPhotosResponse200]:
    r""" Reorder the Airbnb photo tour

     Set the order of a listing's photo tour in one call. **Write-side** — calls Airbnb upstream.

    Send the photo ids in the order you want them shown, first photo first. Ids you leave out keep their
    current relative order behind the ones you list, so moving one photo to the front is
    `{\"photo_ids\": [\"<id>\"]}`. Positions are then written as a dense run starting at 1.

    Airbnb has no bulk photo endpoint — order is one `sort_order` per photo — so this saves a loop of up
    to 200 requests against your rate limit and makes the partial-failure case reportable. How much is
    atomic:

    - Everything is validated before anything is written. A duplicate id, an id that is not on this
    listing, an inactive listing or a missing connection all fail with **zero** upstream writes.
    - Only photos whose position actually changes are written; re-sending the order you already have
    writes nothing.
    - On the first upstream failure the run stops — nothing after it is attempted. The error carries
    `applied`, `failed_photo_id` and `not_attempted`, uses Airbnb's own status (`422` rejected / `403`
    reauth / `429` / `502`), and the operation is idempotent: re-send the identical body to finish the
    run.
    - Our stored copy records what actually landed, never the intent.

    Validation is against our cached copy of the tour, so a listing whose photos have never synced
    returns `404` — use `PATCH /photos` (which needs no cache) until the first sync lands.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (ReorderAirbnbListingPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReorderAirbnbListingPhotosResponse200]
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
    body: ReorderAirbnbListingPhotosBody,

) -> Error | ReorderAirbnbListingPhotosResponse200 | None:
    r""" Reorder the Airbnb photo tour

     Set the order of a listing's photo tour in one call. **Write-side** — calls Airbnb upstream.

    Send the photo ids in the order you want them shown, first photo first. Ids you leave out keep their
    current relative order behind the ones you list, so moving one photo to the front is
    `{\"photo_ids\": [\"<id>\"]}`. Positions are then written as a dense run starting at 1.

    Airbnb has no bulk photo endpoint — order is one `sort_order` per photo — so this saves a loop of up
    to 200 requests against your rate limit and makes the partial-failure case reportable. How much is
    atomic:

    - Everything is validated before anything is written. A duplicate id, an id that is not on this
    listing, an inactive listing or a missing connection all fail with **zero** upstream writes.
    - Only photos whose position actually changes are written; re-sending the order you already have
    writes nothing.
    - On the first upstream failure the run stops — nothing after it is attempted. The error carries
    `applied`, `failed_photo_id` and `not_attempted`, uses Airbnb's own status (`422` rejected / `403`
    reauth / `429` / `502`), and the operation is idempotent: re-send the identical body to finish the
    run.
    - Our stored copy records what actually landed, never the intent.

    Validation is against our cached copy of the tour, so a listing whose photos have never synced
    returns `404` — use `PATCH /photos` (which needs no cache) until the first sync lands.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (ReorderAirbnbListingPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReorderAirbnbListingPhotosResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
