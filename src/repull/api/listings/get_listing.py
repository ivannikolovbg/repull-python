from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.listing import Listing
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    x_schema: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_schema, Unset):
        headers["X-Schema"] = x_schema



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/{id}".format(id=quote(str(id), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Listing | None:
    if response.status_code == 200:
        response_200 = Listing.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Listing]:
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
    x_schema: str | Unset = UNSET,

) -> Response[Error | Listing]:
    """ Get a listing

     Fetch a single listing by id. Returns the same shape as one element of the `GET /v1/listings`
    response, so you can bind the result to the same model. Cross-tenant access (a listing that belongs
    to a different workspace) returns 404 — never 403, never reveals the listing's existence.

    Args:
        id (int):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Listing]
     """


    kwargs = _get_kwargs(
        id=id,
x_schema=x_schema,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    x_schema: str | Unset = UNSET,

) -> Error | Listing | None:
    """ Get a listing

     Fetch a single listing by id. Returns the same shape as one element of the `GET /v1/listings`
    response, so you can bind the result to the same model. Cross-tenant access (a listing that belongs
    to a different workspace) returns 404 — never 403, never reveals the listing's existence.

    Args:
        id (int):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Listing
     """


    return sync_detailed(
        id=id,
client=client,
x_schema=x_schema,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    x_schema: str | Unset = UNSET,

) -> Response[Error | Listing]:
    """ Get a listing

     Fetch a single listing by id. Returns the same shape as one element of the `GET /v1/listings`
    response, so you can bind the result to the same model. Cross-tenant access (a listing that belongs
    to a different workspace) returns 404 — never 403, never reveals the listing's existence.

    Args:
        id (int):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Listing]
     """


    kwargs = _get_kwargs(
        id=id,
x_schema=x_schema,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    x_schema: str | Unset = UNSET,

) -> Error | Listing | None:
    """ Get a listing

     Fetch a single listing by id. Returns the same shape as one element of the `GET /v1/listings`
    response, so you can bind the result to the same model. Cross-tenant access (a listing that belongs
    to a different workspace) returns 404 — never 403, never reveals the listing's existence.

    Args:
        id (int):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Listing
     """


    return (await asyncio_detailed(
        id=id,
client=client,
x_schema=x_schema,

    )).parsed
