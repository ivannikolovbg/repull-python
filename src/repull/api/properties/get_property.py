from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_property_include import GetPropertyInclude
from ...models.property_ import Property
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    include: GetPropertyInclude | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_include: str | Unset = UNSET
    if not isinstance(include, Unset):
        json_include = include.value

    params["include"] = json_include


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/properties/{id}".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Property | None:
    if response.status_code == 200:
        response_200 = Property.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Property]:
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
    include: GetPropertyInclude | Unset = UNSET,

) -> Response[Error | Property]:
    """ Get property details

     Fetch a single property by Repull id. Property ids are workspace-scoped — an id from one workspace
    is not valid in another. 404 means the id does not exist OR belongs to a different workspace.

    **Optional expansions:** Pass `?include=amenities` to enrich the response with the property's
    amenities (sourced from the unified `listings_amenities` table). Returns `[]` when the property has
    no amenity rows. The default response stays lean; consumers must opt in.

    Args:
        id (int):
        include (GetPropertyInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Property]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    include: GetPropertyInclude | Unset = UNSET,

) -> Error | Property | None:
    """ Get property details

     Fetch a single property by Repull id. Property ids are workspace-scoped — an id from one workspace
    is not valid in another. 404 means the id does not exist OR belongs to a different workspace.

    **Optional expansions:** Pass `?include=amenities` to enrich the response with the property's
    amenities (sourced from the unified `listings_amenities` table). Returns `[]` when the property has
    no amenity rows. The default response stays lean; consumers must opt in.

    Args:
        id (int):
        include (GetPropertyInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Property
     """


    return sync_detailed(
        id=id,
client=client,
include=include,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    include: GetPropertyInclude | Unset = UNSET,

) -> Response[Error | Property]:
    """ Get property details

     Fetch a single property by Repull id. Property ids are workspace-scoped — an id from one workspace
    is not valid in another. 404 means the id does not exist OR belongs to a different workspace.

    **Optional expansions:** Pass `?include=amenities` to enrich the response with the property's
    amenities (sourced from the unified `listings_amenities` table). Returns `[]` when the property has
    no amenity rows. The default response stays lean; consumers must opt in.

    Args:
        id (int):
        include (GetPropertyInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Property]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    include: GetPropertyInclude | Unset = UNSET,

) -> Error | Property | None:
    """ Get property details

     Fetch a single property by Repull id. Property ids are workspace-scoped — an id from one workspace
    is not valid in another. 404 means the id does not exist OR belongs to a different workspace.

    **Optional expansions:** Pass `?include=amenities` to enrich the response with the property's
    amenities (sourced from the unified `listings_amenities` table). Returns `[]` when the property has
    no amenity rows. The default response stays lean; consumers must opt in.

    Args:
        id (int):
        include (GetPropertyInclude | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Property
     """


    return (await asyncio_detailed(
        id=id,
client=client,
include=include,

    )).parsed
