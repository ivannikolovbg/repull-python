from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.listing_comps_response import ListingCompsResponse
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    id: int,
    *,
    radius_km: float | Unset = 5.0,
    limit: int | Unset = 20,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["radius_km"] = radius_km

    params["limit"] = limit

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/{id}/comps".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListingCompsResponse | None:
    if response.status_code == 200:
        response_200 = ListingCompsResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListingCompsResponse]:
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
    radius_km: float | Unset = 5.0,
    limit: int | Unset = 20,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,

) -> Response[Error | ListingCompsResponse]:
    """ Comp set for a listing (with daily nightly pricing)

     Returns the actual comp set for a listing — the underlying competitor listings (with daily nightly
    pricing), not just the aggregated `compSummary` from `/pricing`. Each comp comes back with distance,
    bedrooms, ratings, lat/lng, platform link, and a per-day rate/availability series for the requested
    window.

    Powered by Atlas. Comps with no coordinates are excluded — there's no way to rank them by distance.
    Listings without coordinates return `data: []` and a `warning` field.

    Args:
        id (int):
        radius_km (float | Unset):  Default: 5.0.
        limit (int | Unset):  Default: 20.
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingCompsResponse]
     """


    kwargs = _get_kwargs(
        id=id,
radius_km=radius_km,
limit=limit,
start_date=start_date,
end_date=end_date,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    radius_km: float | Unset = 5.0,
    limit: int | Unset = 20,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,

) -> Error | ListingCompsResponse | None:
    """ Comp set for a listing (with daily nightly pricing)

     Returns the actual comp set for a listing — the underlying competitor listings (with daily nightly
    pricing), not just the aggregated `compSummary` from `/pricing`. Each comp comes back with distance,
    bedrooms, ratings, lat/lng, platform link, and a per-day rate/availability series for the requested
    window.

    Powered by Atlas. Comps with no coordinates are excluded — there's no way to rank them by distance.
    Listings without coordinates return `data: []` and a `warning` field.

    Args:
        id (int):
        radius_km (float | Unset):  Default: 5.0.
        limit (int | Unset):  Default: 20.
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingCompsResponse
     """


    return sync_detailed(
        id=id,
client=client,
radius_km=radius_km,
limit=limit,
start_date=start_date,
end_date=end_date,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    radius_km: float | Unset = 5.0,
    limit: int | Unset = 20,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,

) -> Response[Error | ListingCompsResponse]:
    """ Comp set for a listing (with daily nightly pricing)

     Returns the actual comp set for a listing — the underlying competitor listings (with daily nightly
    pricing), not just the aggregated `compSummary` from `/pricing`. Each comp comes back with distance,
    bedrooms, ratings, lat/lng, platform link, and a per-day rate/availability series for the requested
    window.

    Powered by Atlas. Comps with no coordinates are excluded — there's no way to rank them by distance.
    Listings without coordinates return `data: []` and a `warning` field.

    Args:
        id (int):
        radius_km (float | Unset):  Default: 5.0.
        limit (int | Unset):  Default: 20.
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingCompsResponse]
     """


    kwargs = _get_kwargs(
        id=id,
radius_km=radius_km,
limit=limit,
start_date=start_date,
end_date=end_date,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    radius_km: float | Unset = 5.0,
    limit: int | Unset = 20,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,

) -> Error | ListingCompsResponse | None:
    """ Comp set for a listing (with daily nightly pricing)

     Returns the actual comp set for a listing — the underlying competitor listings (with daily nightly
    pricing), not just the aggregated `compSummary` from `/pricing`. Each comp comes back with distance,
    bedrooms, ratings, lat/lng, platform link, and a per-day rate/availability series for the requested
    window.

    Powered by Atlas. Comps with no coordinates are excluded — there's no way to rank them by distance.
    Listings without coordinates return `data: []` and a `warning` field.

    Args:
        id (int):
        radius_km (float | Unset):  Default: 5.0.
        limit (int | Unset):  Default: 20.
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingCompsResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
radius_km=radius_km,
limit=limit,
start_date=start_date,
end_date=end_date,

    )).parsed
