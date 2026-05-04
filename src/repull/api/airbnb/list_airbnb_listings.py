from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_listing_list_response import AirbnbListingListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    include: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["include"] = include


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/listings",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AirbnbListingListResponse | None:
    if response.status_code == 200:
        response_200 = AirbnbListingListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AirbnbListingListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    include: str | Unset = UNSET,

) -> Response[AirbnbListingListResponse]:
    """ List Airbnb listings

     List every Airbnb listing this workspace has access to via the connected Airbnb account. Default
    response is a fast DB read pairing each Vanio listing with its `listings_airbnb` connection rows.

    Pass `?include=amenities` to enrich each connection with its current Airbnb amenity set (one extra
    upstream call per unique Airbnb id, fanned out in parallel). Per-connection failures surface in
    `_errors.amenities` rather than failing the whole request.

    Args:
        include (str | Unset):  Example: amenities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbListingListResponse]
     """


    kwargs = _get_kwargs(
        include=include,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    include: str | Unset = UNSET,

) -> AirbnbListingListResponse | None:
    """ List Airbnb listings

     List every Airbnb listing this workspace has access to via the connected Airbnb account. Default
    response is a fast DB read pairing each Vanio listing with its `listings_airbnb` connection rows.

    Pass `?include=amenities` to enrich each connection with its current Airbnb amenity set (one extra
    upstream call per unique Airbnb id, fanned out in parallel). Per-connection failures surface in
    `_errors.amenities` rather than failing the whole request.

    Args:
        include (str | Unset):  Example: amenities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbListingListResponse
     """


    return sync_detailed(
        client=client,
include=include,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include: str | Unset = UNSET,

) -> Response[AirbnbListingListResponse]:
    """ List Airbnb listings

     List every Airbnb listing this workspace has access to via the connected Airbnb account. Default
    response is a fast DB read pairing each Vanio listing with its `listings_airbnb` connection rows.

    Pass `?include=amenities` to enrich each connection with its current Airbnb amenity set (one extra
    upstream call per unique Airbnb id, fanned out in parallel). Per-connection failures surface in
    `_errors.amenities` rather than failing the whole request.

    Args:
        include (str | Unset):  Example: amenities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbListingListResponse]
     """


    kwargs = _get_kwargs(
        include=include,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include: str | Unset = UNSET,

) -> AirbnbListingListResponse | None:
    """ List Airbnb listings

     List every Airbnb listing this workspace has access to via the connected Airbnb account. Default
    response is a fast DB read pairing each Vanio listing with its `listings_airbnb` connection rows.

    Pass `?include=amenities` to enrich each connection with its current Airbnb amenity set (one extra
    upstream call per unique Airbnb id, fanned out in parallel). Per-connection failures surface in
    `_errors.amenities` rather than failing the whole request.

    Args:
        include (str | Unset):  Example: amenities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbListingListResponse
     """


    return (await asyncio_detailed(
        client=client,
include=include,

    )).parsed
