from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.set_listing_markup_body import SetListingMarkupBody
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: SetListingMarkupBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/listings/{id}/markups".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
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
    body: SetListingMarkupBody,

) -> Response[Any | Error]:
    """ Set a listing's markup on a channel

     Set the markup one channel adds to this listing's price. When the value changes, the affected
    listings' prices are re-sent to that channel straight away (`pricesResent`); nothing else is sent.

    A listing's price on a channel is its own nightly price plus the channel's markup: a $200 night with
    a 35% Airbnb markup is sent to Airbnb as $270. The calendar keeps the listing's own price (`GET
    /v1/availability/{propertyId}` returns it); the markup is added only when a price is sent to the
    channel.

    - **Airbnb** — one markup per listing.
    - **Booking.com** — one markup per **property**, shared by every listing priced through it
    (`listingIds` names them).

    Returns `404 not_found` for a listing that does not exist or is not in this workspace, and `403
    listing_inactive` for an inactive one.

    On Booking.com the markup belongs to the property, so setting it reprices every listing on that
    property (`affectedListingIds`). A listing on more than one property must name one with `hotelId`;
    without it the request is refused with `409 ambiguous_booking_mapping` listing the candidates,
    rather than repricing a property it guessed.

    `markupPercent` is a percentage — `15` for 15%. A value between 0 and 1 is refused as a probable
    fraction, with the number to send instead.

    Args:
        id (str):
        body (SetListingMarkupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetListingMarkupBody,

) -> Any | Error | None:
    """ Set a listing's markup on a channel

     Set the markup one channel adds to this listing's price. When the value changes, the affected
    listings' prices are re-sent to that channel straight away (`pricesResent`); nothing else is sent.

    A listing's price on a channel is its own nightly price plus the channel's markup: a $200 night with
    a 35% Airbnb markup is sent to Airbnb as $270. The calendar keeps the listing's own price (`GET
    /v1/availability/{propertyId}` returns it); the markup is added only when a price is sent to the
    channel.

    - **Airbnb** — one markup per listing.
    - **Booking.com** — one markup per **property**, shared by every listing priced through it
    (`listingIds` names them).

    Returns `404 not_found` for a listing that does not exist or is not in this workspace, and `403
    listing_inactive` for an inactive one.

    On Booking.com the markup belongs to the property, so setting it reprices every listing on that
    property (`affectedListingIds`). A listing on more than one property must name one with `hotelId`;
    without it the request is refused with `409 ambiguous_booking_mapping` listing the candidates,
    rather than repricing a property it guessed.

    `markupPercent` is a percentage — `15` for 15%. A value between 0 and 1 is refused as a probable
    fraction, with the number to send instead.

    Args:
        id (str):
        body (SetListingMarkupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetListingMarkupBody,

) -> Response[Any | Error]:
    """ Set a listing's markup on a channel

     Set the markup one channel adds to this listing's price. When the value changes, the affected
    listings' prices are re-sent to that channel straight away (`pricesResent`); nothing else is sent.

    A listing's price on a channel is its own nightly price plus the channel's markup: a $200 night with
    a 35% Airbnb markup is sent to Airbnb as $270. The calendar keeps the listing's own price (`GET
    /v1/availability/{propertyId}` returns it); the markup is added only when a price is sent to the
    channel.

    - **Airbnb** — one markup per listing.
    - **Booking.com** — one markup per **property**, shared by every listing priced through it
    (`listingIds` names them).

    Returns `404 not_found` for a listing that does not exist or is not in this workspace, and `403
    listing_inactive` for an inactive one.

    On Booking.com the markup belongs to the property, so setting it reprices every listing on that
    property (`affectedListingIds`). A listing on more than one property must name one with `hotelId`;
    without it the request is refused with `409 ambiguous_booking_mapping` listing the candidates,
    rather than repricing a property it guessed.

    `markupPercent` is a percentage — `15` for 15%. A value between 0 and 1 is refused as a probable
    fraction, with the number to send instead.

    Args:
        id (str):
        body (SetListingMarkupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetListingMarkupBody,

) -> Any | Error | None:
    """ Set a listing's markup on a channel

     Set the markup one channel adds to this listing's price. When the value changes, the affected
    listings' prices are re-sent to that channel straight away (`pricesResent`); nothing else is sent.

    A listing's price on a channel is its own nightly price plus the channel's markup: a $200 night with
    a 35% Airbnb markup is sent to Airbnb as $270. The calendar keeps the listing's own price (`GET
    /v1/availability/{propertyId}` returns it); the markup is added only when a price is sent to the
    channel.

    - **Airbnb** — one markup per listing.
    - **Booking.com** — one markup per **property**, shared by every listing priced through it
    (`listingIds` names them).

    Returns `404 not_found` for a listing that does not exist or is not in this workspace, and `403
    listing_inactive` for an inactive one.

    On Booking.com the markup belongs to the property, so setting it reprices every listing on that
    property (`affectedListingIds`). A listing on more than one property must name one with `hotelId`;
    without it the request is refused with `409 ambiguous_booking_mapping` listing the candidates,
    rather than repricing a property it guessed.

    `markupPercent` is a percentage — `15` for 15%. A value between 0 and 1 is refused as a probable
    fraction, with the number to send instead.

    Args:
        id (str):
        body (SetListingMarkupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
