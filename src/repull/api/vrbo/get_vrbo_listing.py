from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_vrbo_listing_include import GetVrboListingInclude
from ...models.get_vrbo_listing_response_200 import GetVrboListingResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    include: GetVrboListingInclude | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_include: str | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = include.value

    params["include"] = json_include


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/vrbo/listings/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetVrboListingResponse200 | None:
    if response.status_code == 200:
        response_200 = GetVrboListingResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetVrboListingResponse200]:
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
    include: GetVrboListingInclude | Unset = UNSET,

) -> Response[Error | GetVrboListingResponse200]:
    """ Get the Vrbo listing

     Every Vrbo unit linked to the listing (usually one; live ones first), from Repull's own data — no
    Vrbo call: the Vrbo listing number and URL, Vrbo's status, headline, capacity, rooms, check-in/out,
    minimum stay, address, rating, the Vrbo account it is on and that account's access.

    `?include=content` adds the listing-content sections Repull holds for each unit (descriptions,
    amenities, house rules, fees, …), so one call returns everything stored.

    Returns `404` when the listing is not linked to Vrbo and `403 listing_inactive` when the listing is
    inactive.

    Args:
        id (str):
        include (GetVrboListingInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboListingResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
include=include,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    include: GetVrboListingInclude | Unset = UNSET,

) -> Error | GetVrboListingResponse200 | None:
    """ Get the Vrbo listing

     Every Vrbo unit linked to the listing (usually one; live ones first), from Repull's own data — no
    Vrbo call: the Vrbo listing number and URL, Vrbo's status, headline, capacity, rooms, check-in/out,
    minimum stay, address, rating, the Vrbo account it is on and that account's access.

    `?include=content` adds the listing-content sections Repull holds for each unit (descriptions,
    amenities, house rules, fees, …), so one call returns everything stored.

    Returns `404` when the listing is not linked to Vrbo and `403 listing_inactive` when the listing is
    inactive.

    Args:
        id (str):
        include (GetVrboListingInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboListingResponse200
     """


    return sync_detailed(
        id=id,
client=client,
include=include,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    include: GetVrboListingInclude | Unset = UNSET,

) -> Response[Error | GetVrboListingResponse200]:
    """ Get the Vrbo listing

     Every Vrbo unit linked to the listing (usually one; live ones first), from Repull's own data — no
    Vrbo call: the Vrbo listing number and URL, Vrbo's status, headline, capacity, rooms, check-in/out,
    minimum stay, address, rating, the Vrbo account it is on and that account's access.

    `?include=content` adds the listing-content sections Repull holds for each unit (descriptions,
    amenities, house rules, fees, …), so one call returns everything stored.

    Returns `404` when the listing is not linked to Vrbo and `403 listing_inactive` when the listing is
    inactive.

    Args:
        id (str):
        include (GetVrboListingInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboListingResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
include=include,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    include: GetVrboListingInclude | Unset = UNSET,

) -> Error | GetVrboListingResponse200 | None:
    """ Get the Vrbo listing

     Every Vrbo unit linked to the listing (usually one; live ones first), from Repull's own data — no
    Vrbo call: the Vrbo listing number and URL, Vrbo's status, headline, capacity, rooms, check-in/out,
    minimum stay, address, rating, the Vrbo account it is on and that account's access.

    `?include=content` adds the listing-content sections Repull holds for each unit (descriptions,
    amenities, house rules, fees, …), so one call returns everything stored.

    Returns `404` when the listing is not linked to Vrbo and `403 listing_inactive` when the listing is
    inactive.

    Args:
        id (str):
        include (GetVrboListingInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboListingResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
include=include,

    )).parsed
