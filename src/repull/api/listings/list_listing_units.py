from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_listing_units_response_200 import ListListingUnitsResponse200
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/{id}/units".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListListingUnitsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListListingUnitsResponse200.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListListingUnitsResponse200]:
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

) -> Response[Error | ListListingUnitsResponse200]:
    """ List a listing's units (rooms)

     The physical rooms under a listing. For a hotel-model PMS (Mews, Cloudbeds) a listing is a room
    type: prices, restrictions and availability are set on the room type, and each reservation is
    assigned one of these rooms (`reservation.unit.id`). A room can belong to more than one room type.

    Any other listing is a single home, which is its own unit, and returns an empty list.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListListingUnitsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Error | ListListingUnitsResponse200 | None:
    """ List a listing's units (rooms)

     The physical rooms under a listing. For a hotel-model PMS (Mews, Cloudbeds) a listing is a room
    type: prices, restrictions and availability are set on the room type, and each reservation is
    assigned one of these rooms (`reservation.unit.id`). A room can belong to more than one room type.

    Any other listing is a single home, which is its own unit, and returns an empty list.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListListingUnitsResponse200
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | ListListingUnitsResponse200]:
    """ List a listing's units (rooms)

     The physical rooms under a listing. For a hotel-model PMS (Mews, Cloudbeds) a listing is a room
    type: prices, restrictions and availability are set on the room type, and each reservation is
    assigned one of these rooms (`reservation.unit.id`). A room can belong to more than one room type.

    Any other listing is a single home, which is its own unit, and returns an empty list.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListListingUnitsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Error | ListListingUnitsResponse200 | None:
    """ List a listing's units (rooms)

     The physical rooms under a listing. For a hotel-model PMS (Mews, Cloudbeds) a listing is a room
    type: prices, restrictions and availability are set on the room type, and each reservation is
    assigned one of these rooms (`reservation.unit.id`). A room can belong to more than one room type.

    Any other listing is a single home, which is its own unit, and returns an empty list.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListListingUnitsResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
