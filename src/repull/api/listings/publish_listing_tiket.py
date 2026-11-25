from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.listing_publish_tiket_response import ListingPublishTiketResponse
from ...models.publish_listing_tiket_body import PublishListingTiketBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: PublishListingTiketBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/{id}/publish/tiket".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListingPublishTiketResponse | None:
    if response.status_code == 200:
        response_200 = ListingPublishTiketResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = Error.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListingPublishTiketResponse]:
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
    body: PublishListingTiketBody | Unset = UNSET,

) -> Response[Error | ListingPublishTiketResponse]:
    """ Publish a listing's content to tiket.com

     Send the listing's content to tiket.com (counterpart of `POST /v1/listings/{id}/publish/booking`):
    room content (name, occupancy, beds, facilities, photos, description), rate-plan policies and — for
    a property Repull created — the property content. The result lists each section that landed
    (`sections`) and each that did not, with tiket.com's reason (`errors`).

    tiket.com only accepts content once it has linked Repull's codes to the property: true for a
    property Repull created, and for an existing property after `POST /v1/channels/tiket/setup`
    `request-content-mapping`. Until then the call returns `409 tiket_content_not_mapped`. Prices and
    availability are not content: they are sent automatically, or with `POST /v1/channels/tiket/sync`.

    A listing mapped on more than one tiket.com property takes `hotelId`.

    Args:
        id (int):
        body (PublishListingTiketBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingPublishTiketResponse]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PublishListingTiketBody | Unset = UNSET,

) -> Error | ListingPublishTiketResponse | None:
    """ Publish a listing's content to tiket.com

     Send the listing's content to tiket.com (counterpart of `POST /v1/listings/{id}/publish/booking`):
    room content (name, occupancy, beds, facilities, photos, description), rate-plan policies and — for
    a property Repull created — the property content. The result lists each section that landed
    (`sections`) and each that did not, with tiket.com's reason (`errors`).

    tiket.com only accepts content once it has linked Repull's codes to the property: true for a
    property Repull created, and for an existing property after `POST /v1/channels/tiket/setup`
    `request-content-mapping`. Until then the call returns `409 tiket_content_not_mapped`. Prices and
    availability are not content: they are sent automatically, or with `POST /v1/channels/tiket/sync`.

    A listing mapped on more than one tiket.com property takes `hotelId`.

    Args:
        id (int):
        body (PublishListingTiketBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingPublishTiketResponse
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PublishListingTiketBody | Unset = UNSET,

) -> Response[Error | ListingPublishTiketResponse]:
    """ Publish a listing's content to tiket.com

     Send the listing's content to tiket.com (counterpart of `POST /v1/listings/{id}/publish/booking`):
    room content (name, occupancy, beds, facilities, photos, description), rate-plan policies and — for
    a property Repull created — the property content. The result lists each section that landed
    (`sections`) and each that did not, with tiket.com's reason (`errors`).

    tiket.com only accepts content once it has linked Repull's codes to the property: true for a
    property Repull created, and for an existing property after `POST /v1/channels/tiket/setup`
    `request-content-mapping`. Until then the call returns `409 tiket_content_not_mapped`. Prices and
    availability are not content: they are sent automatically, or with `POST /v1/channels/tiket/sync`.

    A listing mapped on more than one tiket.com property takes `hotelId`.

    Args:
        id (int):
        body (PublishListingTiketBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingPublishTiketResponse]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PublishListingTiketBody | Unset = UNSET,

) -> Error | ListingPublishTiketResponse | None:
    """ Publish a listing's content to tiket.com

     Send the listing's content to tiket.com (counterpart of `POST /v1/listings/{id}/publish/booking`):
    room content (name, occupancy, beds, facilities, photos, description), rate-plan policies and — for
    a property Repull created — the property content. The result lists each section that landed
    (`sections`) and each that did not, with tiket.com's reason (`errors`).

    tiket.com only accepts content once it has linked Repull's codes to the property: true for a
    property Repull created, and for an existing property after `POST /v1/channels/tiket/setup`
    `request-content-mapping`. Until then the call returns `409 tiket_content_not_mapped`. Prices and
    availability are not content: they are sent automatically, or with `POST /v1/channels/tiket/sync`.

    A listing mapped on more than one tiket.com property takes `hotelId`.

    Args:
        id (int):
        body (PublishListingTiketBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingPublishTiketResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
