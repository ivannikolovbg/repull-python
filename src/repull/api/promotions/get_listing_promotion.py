from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.promotion_response import PromotionResponse
from typing import cast



def _get_kwargs(
    id: int,
    promotion_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/{id}/promotions/{promotion_id}".format(id=quote(str(id), safe=""),promotion_id=quote(str(promotion_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PromotionResponse | None:
    if response.status_code == 200:
        response_200 = PromotionResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PromotionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    promotion_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | PromotionResponse]:
    """ Get one promotion

     One promotion on the listing.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        promotion_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PromotionResponse]
     """


    kwargs = _get_kwargs(
        id=id,
promotion_id=promotion_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    promotion_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Error | PromotionResponse | None:
    """ Get one promotion

     One promotion on the listing.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        promotion_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PromotionResponse
     """


    return sync_detailed(
        id=id,
promotion_id=promotion_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    promotion_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | PromotionResponse]:
    """ Get one promotion

     One promotion on the listing.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        promotion_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PromotionResponse]
     """


    kwargs = _get_kwargs(
        id=id,
promotion_id=promotion_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    promotion_id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Error | PromotionResponse | None:
    """ Get one promotion

     One promotion on the listing.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        promotion_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PromotionResponse
     """


    return (await asyncio_detailed(
        id=id,
promotion_id=promotion_id,
client=client,

    )).parsed
