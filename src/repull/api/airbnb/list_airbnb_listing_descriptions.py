from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_airbnb_listing_descriptions_response_200 import ListAirbnbListingDescriptionsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    locale: str | Unset = UNSET,
    country: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["locale"] = locale

    params["country"] = country


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/listings/{id}/descriptions".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListAirbnbListingDescriptionsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAirbnbListingDescriptionsResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListAirbnbListingDescriptionsResponse200]:
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
    locale: str | Unset = UNSET,
    country: str | Unset = UNSET,

) -> Response[Error | ListAirbnbListingDescriptionsResponse200]:
    """ List Airbnb descriptions

     List an Airbnb listing's per-locale content (name, summary, house rules, etc). **Pure DB read** from
    `listings_airbnb_descriptions`. Filter to one locale with `?locale=en` (the legacy `?country=` param
    is accepted as a soft alias). Returns `404` when the listing has no Airbnb connection in this
    workspace.

    Args:
        id (str):
        locale (str | Unset):  Example: en.
        country (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbListingDescriptionsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
locale=locale,
country=country,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,
    country: str | Unset = UNSET,

) -> Error | ListAirbnbListingDescriptionsResponse200 | None:
    """ List Airbnb descriptions

     List an Airbnb listing's per-locale content (name, summary, house rules, etc). **Pure DB read** from
    `listings_airbnb_descriptions`. Filter to one locale with `?locale=en` (the legacy `?country=` param
    is accepted as a soft alias). Returns `404` when the listing has no Airbnb connection in this
    workspace.

    Args:
        id (str):
        locale (str | Unset):  Example: en.
        country (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbListingDescriptionsResponse200
     """


    return sync_detailed(
        id=id,
client=client,
locale=locale,
country=country,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,
    country: str | Unset = UNSET,

) -> Response[Error | ListAirbnbListingDescriptionsResponse200]:
    """ List Airbnb descriptions

     List an Airbnb listing's per-locale content (name, summary, house rules, etc). **Pure DB read** from
    `listings_airbnb_descriptions`. Filter to one locale with `?locale=en` (the legacy `?country=` param
    is accepted as a soft alias). Returns `404` when the listing has no Airbnb connection in this
    workspace.

    Args:
        id (str):
        locale (str | Unset):  Example: en.
        country (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbListingDescriptionsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
locale=locale,
country=country,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,
    country: str | Unset = UNSET,

) -> Error | ListAirbnbListingDescriptionsResponse200 | None:
    """ List Airbnb descriptions

     List an Airbnb listing's per-locale content (name, summary, house rules, etc). **Pure DB read** from
    `listings_airbnb_descriptions`. Filter to one locale with `?locale=en` (the legacy `?country=` param
    is accepted as a soft alias). Returns `404` when the listing has no Airbnb connection in this
    workspace.

    Args:
        id (str):
        locale (str | Unset):  Example: en.
        country (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbListingDescriptionsResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
locale=locale,
country=country,

    )).parsed
