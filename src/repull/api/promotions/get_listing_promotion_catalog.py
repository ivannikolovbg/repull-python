from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.promotion_catalog_response import PromotionCatalogResponse
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/{id}/promotions/catalog".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PromotionCatalogResponse | None:
    if response.status_code == 200:
        response_200 = PromotionCatalogResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PromotionCatalogResponse]:
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

) -> Response[Error | PromotionCatalogResponse]:
    """ Promotion types a listing can use

     Per channel: whether the listing is connected, and each promotion type with a short description for
    hosts, whether it is new, whether it is available to this listing (and why not), and every field —
    supported or not — with its limits and any value the channel fixes. Booking.com's types and limits
    come from the property itself; seasonal campaigns appear while Booking.com runs them.

    Airbnb asks partners to show newly available discounts with a “New” badge and to grey out fields a
    discount does not support rather than hide them; `isNew` and `fields` carry what that needs.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PromotionCatalogResponse]
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

) -> Error | PromotionCatalogResponse | None:
    """ Promotion types a listing can use

     Per channel: whether the listing is connected, and each promotion type with a short description for
    hosts, whether it is new, whether it is available to this listing (and why not), and every field —
    supported or not — with its limits and any value the channel fixes. Booking.com's types and limits
    come from the property itself; seasonal campaigns appear while Booking.com runs them.

    Airbnb asks partners to show newly available discounts with a “New” badge and to grey out fields a
    discount does not support rather than hide them; `isNew` and `fields` carry what that needs.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PromotionCatalogResponse
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | PromotionCatalogResponse]:
    """ Promotion types a listing can use

     Per channel: whether the listing is connected, and each promotion type with a short description for
    hosts, whether it is new, whether it is available to this listing (and why not), and every field —
    supported or not — with its limits and any value the channel fixes. Booking.com's types and limits
    come from the property itself; seasonal campaigns appear while Booking.com runs them.

    Airbnb asks partners to show newly available discounts with a “New” badge and to grey out fields a
    discount does not support rather than hide them; `isNew` and `fields` carry what that needs.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PromotionCatalogResponse]
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

) -> Error | PromotionCatalogResponse | None:
    """ Promotion types a listing can use

     Per channel: whether the listing is connected, and each promotion type with a short description for
    hosts, whether it is new, whether it is available to this listing (and why not), and every field —
    supported or not — with its limits and any value the channel fixes. Booking.com's types and limits
    come from the property itself; seasonal campaigns appear while Booking.com runs them.

    Airbnb asks partners to show newly available discounts with a “New” badge and to grey out fields a
    discount does not support rather than hide them; `isNew` and `fields` carry what that needs.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PromotionCatalogResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
