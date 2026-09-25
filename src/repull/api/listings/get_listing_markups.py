from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_listing_markups_response_200 import GetListingMarkupsResponse200
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/{id}/markups".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetListingMarkupsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetListingMarkupsResponse200.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetListingMarkupsResponse200]:
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

) -> Response[Error | GetListingMarkupsResponse200]:
    """ Get a listing's channel markups

     The markup each channel adds to this listing's price.

    A listing's price on a channel is its own nightly price plus the channel's markup: a $200 night with
    a 35% Airbnb markup is sent to Airbnb as $270. The calendar keeps the listing's own price (`GET
    /v1/availability/{propertyId}` returns it); the markup is added only when a price is sent to the
    channel.

    - **Airbnb** — one markup per listing.
    - **Booking.com** — one markup per **property**, shared by every listing priced through it
    (`listingIds` names them).

    Returns `404 not_found` for a listing that does not exist or is not in this workspace, and `403
    listing_inactive` for an inactive one.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetListingMarkupsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetListingMarkupsResponse200 | None:
    """ Get a listing's channel markups

     The markup each channel adds to this listing's price.

    A listing's price on a channel is its own nightly price plus the channel's markup: a $200 night with
    a 35% Airbnb markup is sent to Airbnb as $270. The calendar keeps the listing's own price (`GET
    /v1/availability/{propertyId}` returns it); the markup is added only when a price is sent to the
    channel.

    - **Airbnb** — one markup per listing.
    - **Booking.com** — one markup per **property**, shared by every listing priced through it
    (`listingIds` names them).

    Returns `404 not_found` for a listing that does not exist or is not in this workspace, and `403
    listing_inactive` for an inactive one.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetListingMarkupsResponse200
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetListingMarkupsResponse200]:
    """ Get a listing's channel markups

     The markup each channel adds to this listing's price.

    A listing's price on a channel is its own nightly price plus the channel's markup: a $200 night with
    a 35% Airbnb markup is sent to Airbnb as $270. The calendar keeps the listing's own price (`GET
    /v1/availability/{propertyId}` returns it); the markup is added only when a price is sent to the
    channel.

    - **Airbnb** — one markup per listing.
    - **Booking.com** — one markup per **property**, shared by every listing priced through it
    (`listingIds` names them).

    Returns `404 not_found` for a listing that does not exist or is not in this workspace, and `403
    listing_inactive` for an inactive one.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetListingMarkupsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetListingMarkupsResponse200 | None:
    """ Get a listing's channel markups

     The markup each channel adds to this listing's price.

    A listing's price on a channel is its own nightly price plus the channel's markup: a $200 night with
    a 35% Airbnb markup is sent to Airbnb as $270. The calendar keeps the listing's own price (`GET
    /v1/availability/{propertyId}` returns it); the markup is added only when a price is sent to the
    channel.

    - **Airbnb** — one markup per listing.
    - **Booking.com** — one markup per **property**, shared by every listing priced through it
    (`listingIds` names them).

    Returns `404 not_found` for a listing that does not exist or is not in this workspace, and `403
    listing_inactive` for an inactive one.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetListingMarkupsResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
