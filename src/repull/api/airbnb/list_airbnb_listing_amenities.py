from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_airbnb_listing_amenities_response_200 import ListAirbnbListingAmenitiesResponse200
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/listings/{id}/amenities".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListAirbnbListingAmenitiesResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAirbnbListingAmenitiesResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListAirbnbListingAmenitiesResponse200]:
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

) -> Response[Error | ListAirbnbListingAmenitiesResponse200]:
    r""" List Airbnb amenities

     List an Airbnb listing's amenities. **Pure DB read** from the local `listings_airbnb_amenities`
    cache — never calls Airbnb upstream. The response splits amenities into `amenities` (regular) and
    `accessibility_amenities` (step-free access, wide doorways, grab rails, disabled parking,
    wheelchair, accessible-height fixtures, hoists, etc). Both are arrays (`[]` when none). Consult
    `data_freshness` to disambiguate \"never synced\" from \"fresh and genuinely empty\". Returns `404`
    when the listing has no Airbnb connection in this workspace.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbListingAmenitiesResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | ListAirbnbListingAmenitiesResponse200 | None:
    r""" List Airbnb amenities

     List an Airbnb listing's amenities. **Pure DB read** from the local `listings_airbnb_amenities`
    cache — never calls Airbnb upstream. The response splits amenities into `amenities` (regular) and
    `accessibility_amenities` (step-free access, wide doorways, grab rails, disabled parking,
    wheelchair, accessible-height fixtures, hoists, etc). Both are arrays (`[]` when none). Consult
    `data_freshness` to disambiguate \"never synced\" from \"fresh and genuinely empty\". Returns `404`
    when the listing has no Airbnb connection in this workspace.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbListingAmenitiesResponse200
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | ListAirbnbListingAmenitiesResponse200]:
    r""" List Airbnb amenities

     List an Airbnb listing's amenities. **Pure DB read** from the local `listings_airbnb_amenities`
    cache — never calls Airbnb upstream. The response splits amenities into `amenities` (regular) and
    `accessibility_amenities` (step-free access, wide doorways, grab rails, disabled parking,
    wheelchair, accessible-height fixtures, hoists, etc). Both are arrays (`[]` when none). Consult
    `data_freshness` to disambiguate \"never synced\" from \"fresh and genuinely empty\". Returns `404`
    when the listing has no Airbnb connection in this workspace.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbListingAmenitiesResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | ListAirbnbListingAmenitiesResponse200 | None:
    r""" List Airbnb amenities

     List an Airbnb listing's amenities. **Pure DB read** from the local `listings_airbnb_amenities`
    cache — never calls Airbnb upstream. The response splits amenities into `amenities` (regular) and
    `accessibility_amenities` (step-free access, wide doorways, grab rails, disabled parking,
    wheelchair, accessible-height fixtures, hoists, etc). Both are arrays (`[]` when none). Consult
    `data_freshness` to disambiguate \"never synced\" from \"fresh and genuinely empty\". Returns `404`
    when the listing has no Airbnb connection in this workspace.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbListingAmenitiesResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
