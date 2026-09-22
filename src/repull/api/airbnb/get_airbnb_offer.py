from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_airbnb_offer_response_200 import GetAirbnbOfferResponse200
from typing import cast



def _get_kwargs(
    *,
    offer_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["offerId"] = offer_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/offers",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetAirbnbOfferResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAirbnbOfferResponse200.from_dict(response.json())



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

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetAirbnbOfferResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    offer_id: str,

) -> Response[Error | GetAirbnbOfferResponse200]:
    """ Get Airbnb special offer

     Read a pre-approval or special offer from Airbnb by its Airbnb id. **Live read** — calls Airbnb
    upstream. Pass the id as `?offerId=`. The Repull-id equivalent is `GET
    /v1/conversations/{id}/special-offers/{offerId}`, which also confirms the offer belongs to that
    conversation.

    Args:
        offer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetAirbnbOfferResponse200]
     """


    kwargs = _get_kwargs(
        offer_id=offer_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    offer_id: str,

) -> Error | GetAirbnbOfferResponse200 | None:
    """ Get Airbnb special offer

     Read a pre-approval or special offer from Airbnb by its Airbnb id. **Live read** — calls Airbnb
    upstream. Pass the id as `?offerId=`. The Repull-id equivalent is `GET
    /v1/conversations/{id}/special-offers/{offerId}`, which also confirms the offer belongs to that
    conversation.

    Args:
        offer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetAirbnbOfferResponse200
     """


    return sync_detailed(
        client=client,
offer_id=offer_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    offer_id: str,

) -> Response[Error | GetAirbnbOfferResponse200]:
    """ Get Airbnb special offer

     Read a pre-approval or special offer from Airbnb by its Airbnb id. **Live read** — calls Airbnb
    upstream. Pass the id as `?offerId=`. The Repull-id equivalent is `GET
    /v1/conversations/{id}/special-offers/{offerId}`, which also confirms the offer belongs to that
    conversation.

    Args:
        offer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetAirbnbOfferResponse200]
     """


    kwargs = _get_kwargs(
        offer_id=offer_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    offer_id: str,

) -> Error | GetAirbnbOfferResponse200 | None:
    """ Get Airbnb special offer

     Read a pre-approval or special offer from Airbnb by its Airbnb id. **Live read** — calls Airbnb
    upstream. Pass the id as `?offerId=`. The Repull-id equivalent is `GET
    /v1/conversations/{id}/special-offers/{offerId}`, which also confirms the offer belongs to that
    conversation.

    Args:
        offer_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetAirbnbOfferResponse200
     """


    return (await asyncio_detailed(
        client=client,
offer_id=offer_id,

    )).parsed
