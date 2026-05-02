from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_listing_segments_level import GetListingSegmentsLevel
from ...models.listing_segments_response import ListingSegmentsResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    level: GetListingSegmentsLevel | Unset = GetListingSegmentsLevel.COMP_SET,
    radius_km: float | Unset = 5.0,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_level: str | Unset = UNSET
    if not isinstance(level, Unset):
        json_level = level.value

    params["level"] = json_level

    params["radius_km"] = radius_km


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/{id}/segments".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListingSegmentsResponse | None:
    if response.status_code == 200:
        response_200 = ListingSegmentsResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListingSegmentsResponse]:
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
    level: GetListingSegmentsLevel | Unset = GetListingSegmentsLevel.COMP_SET,
    radius_km: float | Unset = 5.0,

) -> Response[Error | ListingSegmentsResponse]:
    """ Atlas DNA segment intelligence for a listing

     Aggregates Atlas DNA segment signal (quality tier, design style, bedrooms) across the listing's
    geographic neighborhood (default: 5km radius) or the whole city, so consumers can answer:
    - What segments dominate my market?
    - Which segment does my listing match best?
    - What's the ADR uplift for moving up a tier?

    DNA coverage is still ramping — segments are scored asynchronously. Cities and radii without scored
    comps return `totalCompsAnalyzed: 0` plus a `low_dna_coverage` recommendation rather than fabricated
    data.

    Args:
        id (int):
        level (GetListingSegmentsLevel | Unset):  Default: GetListingSegmentsLevel.COMP_SET.
        radius_km (float | Unset):  Default: 5.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingSegmentsResponse]
     """


    kwargs = _get_kwargs(
        id=id,
level=level,
radius_km=radius_km,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    level: GetListingSegmentsLevel | Unset = GetListingSegmentsLevel.COMP_SET,
    radius_km: float | Unset = 5.0,

) -> Error | ListingSegmentsResponse | None:
    """ Atlas DNA segment intelligence for a listing

     Aggregates Atlas DNA segment signal (quality tier, design style, bedrooms) across the listing's
    geographic neighborhood (default: 5km radius) or the whole city, so consumers can answer:
    - What segments dominate my market?
    - Which segment does my listing match best?
    - What's the ADR uplift for moving up a tier?

    DNA coverage is still ramping — segments are scored asynchronously. Cities and radii without scored
    comps return `totalCompsAnalyzed: 0` plus a `low_dna_coverage` recommendation rather than fabricated
    data.

    Args:
        id (int):
        level (GetListingSegmentsLevel | Unset):  Default: GetListingSegmentsLevel.COMP_SET.
        radius_km (float | Unset):  Default: 5.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingSegmentsResponse
     """


    return sync_detailed(
        id=id,
client=client,
level=level,
radius_km=radius_km,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    level: GetListingSegmentsLevel | Unset = GetListingSegmentsLevel.COMP_SET,
    radius_km: float | Unset = 5.0,

) -> Response[Error | ListingSegmentsResponse]:
    """ Atlas DNA segment intelligence for a listing

     Aggregates Atlas DNA segment signal (quality tier, design style, bedrooms) across the listing's
    geographic neighborhood (default: 5km radius) or the whole city, so consumers can answer:
    - What segments dominate my market?
    - Which segment does my listing match best?
    - What's the ADR uplift for moving up a tier?

    DNA coverage is still ramping — segments are scored asynchronously. Cities and radii without scored
    comps return `totalCompsAnalyzed: 0` plus a `low_dna_coverage` recommendation rather than fabricated
    data.

    Args:
        id (int):
        level (GetListingSegmentsLevel | Unset):  Default: GetListingSegmentsLevel.COMP_SET.
        radius_km (float | Unset):  Default: 5.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingSegmentsResponse]
     """


    kwargs = _get_kwargs(
        id=id,
level=level,
radius_km=radius_km,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    level: GetListingSegmentsLevel | Unset = GetListingSegmentsLevel.COMP_SET,
    radius_km: float | Unset = 5.0,

) -> Error | ListingSegmentsResponse | None:
    """ Atlas DNA segment intelligence for a listing

     Aggregates Atlas DNA segment signal (quality tier, design style, bedrooms) across the listing's
    geographic neighborhood (default: 5km radius) or the whole city, so consumers can answer:
    - What segments dominate my market?
    - Which segment does my listing match best?
    - What's the ADR uplift for moving up a tier?

    DNA coverage is still ramping — segments are scored asynchronously. Cities and radii without scored
    comps return `totalCompsAnalyzed: 0` plus a `low_dna_coverage` recommendation rather than fabricated
    data.

    Args:
        id (int):
        level (GetListingSegmentsLevel | Unset):  Default: GetListingSegmentsLevel.COMP_SET.
        radius_km (float | Unset):  Default: 5.0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingSegmentsResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
level=level,
radius_km=radius_km,

    )).parsed
