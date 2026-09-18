from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.update_airbnb_listing_amenities_body import UpdateAirbnbListingAmenitiesBody
from ...models.update_airbnb_listing_amenities_response_200 import UpdateAirbnbListingAmenitiesResponse200
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: UpdateAirbnbListingAmenitiesBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/airbnb/listings/{id}/amenities".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | UpdateAirbnbListingAmenitiesResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateAirbnbListingAmenitiesResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | UpdateAirbnbListingAmenitiesResponse200]:
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
    body: UpdateAirbnbListingAmenitiesBody,

) -> Response[Error | UpdateAirbnbListingAmenitiesResponse200]:
    """ Update Airbnb amenities

     Set amenities on an Airbnb listing. **Write-side** — calls Airbnb upstream.

    **Partial by design**: only the amenities you name change, so turning one off is a one-line body and
    nothing else on the listing moves. Ids are the `id` values `GET /amenities` returns (e.g.
    `wireless_internet`, `ac`, `kitchen`); case is ignored. Airbnb refuses ids outside its vocabulary —
    that comes back as `422 airbnb_rejected` carrying Airbnb's own message.

    `accessibility_amenities` go to Airbnb's separate accessibility resource, which has **no read side
    at all** — Airbnb offers no endpoint to fetch them back, and the combined amenities GET 404s on
    production listings. What you can read back is our own copy: this endpoint updates it on success,
    and `GET /amenities` returns it under `accessibilityAmenities`. Airbnb may also hold an
    accessibility claim for review until photo evidence is attached; pass `photo_ids` to supply it.

    Our Airbnb copy is updated on success so a read straight after this write returns the new values.
    The platform-neutral copy behind `GET /v1/listings/{id}?include=amenities` uses a different amenity
    vocabulary and is refreshed by the next sync, except where an id happens to be identical in both.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UpdateAirbnbListingAmenitiesBody): At least one amenity across `amenities` and
            `accessibility_amenities`. A body that changes nothing is refused rather than reported as
            a successful write.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbListingAmenitiesResponse200]
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
    body: UpdateAirbnbListingAmenitiesBody,

) -> Error | UpdateAirbnbListingAmenitiesResponse200 | None:
    """ Update Airbnb amenities

     Set amenities on an Airbnb listing. **Write-side** — calls Airbnb upstream.

    **Partial by design**: only the amenities you name change, so turning one off is a one-line body and
    nothing else on the listing moves. Ids are the `id` values `GET /amenities` returns (e.g.
    `wireless_internet`, `ac`, `kitchen`); case is ignored. Airbnb refuses ids outside its vocabulary —
    that comes back as `422 airbnb_rejected` carrying Airbnb's own message.

    `accessibility_amenities` go to Airbnb's separate accessibility resource, which has **no read side
    at all** — Airbnb offers no endpoint to fetch them back, and the combined amenities GET 404s on
    production listings. What you can read back is our own copy: this endpoint updates it on success,
    and `GET /amenities` returns it under `accessibilityAmenities`. Airbnb may also hold an
    accessibility claim for review until photo evidence is attached; pass `photo_ids` to supply it.

    Our Airbnb copy is updated on success so a read straight after this write returns the new values.
    The platform-neutral copy behind `GET /v1/listings/{id}?include=amenities` uses a different amenity
    vocabulary and is refreshed by the next sync, except where an id happens to be identical in both.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UpdateAirbnbListingAmenitiesBody): At least one amenity across `amenities` and
            `accessibility_amenities`. A body that changes nothing is refused rather than reported as
            a successful write.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbListingAmenitiesResponse200
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
    body: UpdateAirbnbListingAmenitiesBody,

) -> Response[Error | UpdateAirbnbListingAmenitiesResponse200]:
    """ Update Airbnb amenities

     Set amenities on an Airbnb listing. **Write-side** — calls Airbnb upstream.

    **Partial by design**: only the amenities you name change, so turning one off is a one-line body and
    nothing else on the listing moves. Ids are the `id` values `GET /amenities` returns (e.g.
    `wireless_internet`, `ac`, `kitchen`); case is ignored. Airbnb refuses ids outside its vocabulary —
    that comes back as `422 airbnb_rejected` carrying Airbnb's own message.

    `accessibility_amenities` go to Airbnb's separate accessibility resource, which has **no read side
    at all** — Airbnb offers no endpoint to fetch them back, and the combined amenities GET 404s on
    production listings. What you can read back is our own copy: this endpoint updates it on success,
    and `GET /amenities` returns it under `accessibilityAmenities`. Airbnb may also hold an
    accessibility claim for review until photo evidence is attached; pass `photo_ids` to supply it.

    Our Airbnb copy is updated on success so a read straight after this write returns the new values.
    The platform-neutral copy behind `GET /v1/listings/{id}?include=amenities` uses a different amenity
    vocabulary and is refreshed by the next sync, except where an id happens to be identical in both.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UpdateAirbnbListingAmenitiesBody): At least one amenity across `amenities` and
            `accessibility_amenities`. A body that changes nothing is refused rather than reported as
            a successful write.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbListingAmenitiesResponse200]
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
    body: UpdateAirbnbListingAmenitiesBody,

) -> Error | UpdateAirbnbListingAmenitiesResponse200 | None:
    """ Update Airbnb amenities

     Set amenities on an Airbnb listing. **Write-side** — calls Airbnb upstream.

    **Partial by design**: only the amenities you name change, so turning one off is a one-line body and
    nothing else on the listing moves. Ids are the `id` values `GET /amenities` returns (e.g.
    `wireless_internet`, `ac`, `kitchen`); case is ignored. Airbnb refuses ids outside its vocabulary —
    that comes back as `422 airbnb_rejected` carrying Airbnb's own message.

    `accessibility_amenities` go to Airbnb's separate accessibility resource, which has **no read side
    at all** — Airbnb offers no endpoint to fetch them back, and the combined amenities GET 404s on
    production listings. What you can read back is our own copy: this endpoint updates it on success,
    and `GET /amenities` returns it under `accessibilityAmenities`. Airbnb may also hold an
    accessibility claim for review until photo evidence is attached; pass `photo_ids` to supply it.

    Our Airbnb copy is updated on success so a read straight after this write returns the new values.
    The platform-neutral copy behind `GET /v1/listings/{id}?include=amenities` uses a different amenity
    vocabulary and is refreshed by the next sync, except where an id happens to be identical in both.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UpdateAirbnbListingAmenitiesBody): At least one amenity across `amenities` and
            `accessibility_amenities`. A body that changes nothing is refused rather than reported as
            a successful write.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbListingAmenitiesResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
