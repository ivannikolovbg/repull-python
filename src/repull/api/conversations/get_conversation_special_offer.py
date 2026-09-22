from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_conversation_special_offer_response_200 import GetConversationSpecialOfferResponse200
from typing import cast



def _get_kwargs(
    id: int,
    offer_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/conversations/{id}/special-offers/{offer_id}".format(id=quote(str(id), safe=""),offer_id=quote(str(offer_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetConversationSpecialOfferResponse200 | None:
    if response.status_code == 200:
        response_200 = GetConversationSpecialOfferResponse200.from_dict(response.json())



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

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetConversationSpecialOfferResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    offer_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetConversationSpecialOfferResponse200]:
    """ Get a special offer

     Read a special offer on this conversation back from Airbnb — typically to check its `status`
    (`active` until the guest books it, it expires, or you withdraw it). Read live from Airbnb with the
    conversation’s own Airbnb account.

    Args:
        id (int):
        offer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetConversationSpecialOfferResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
offer_id=offer_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    offer_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetConversationSpecialOfferResponse200 | None:
    """ Get a special offer

     Read a special offer on this conversation back from Airbnb — typically to check its `status`
    (`active` until the guest books it, it expires, or you withdraw it). Read live from Airbnb with the
    conversation’s own Airbnb account.

    Args:
        id (int):
        offer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetConversationSpecialOfferResponse200
     """


    return sync_detailed(
        id=id,
offer_id=offer_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    offer_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetConversationSpecialOfferResponse200]:
    """ Get a special offer

     Read a special offer on this conversation back from Airbnb — typically to check its `status`
    (`active` until the guest books it, it expires, or you withdraw it). Read live from Airbnb with the
    conversation’s own Airbnb account.

    Args:
        id (int):
        offer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetConversationSpecialOfferResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
offer_id=offer_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    offer_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetConversationSpecialOfferResponse200 | None:
    """ Get a special offer

     Read a special offer on this conversation back from Airbnb — typically to check its `status`
    (`active` until the guest books it, it expires, or you withdraw it). Read live from Airbnb with the
    conversation’s own Airbnb account.

    Args:
        id (int):
        offer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetConversationSpecialOfferResponse200
     """


    return (await asyncio_detailed(
        id=id,
offer_id=offer_id,
client=client,

    )).parsed
