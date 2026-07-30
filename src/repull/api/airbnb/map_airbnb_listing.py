from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.map_airbnb_listing_request import MapAirbnbListingRequest
from ...models.map_airbnb_listing_response import MapAirbnbListingResponse
from typing import cast



def _get_kwargs(
    *,
    body: MapAirbnbListingRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/airbnb/listings/map",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | MapAirbnbListingResponse | None:
    if response.status_code == 200:
        response_200 = MapAirbnbListingResponse.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | MapAirbnbListingResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MapAirbnbListingRequest,

) -> Response[Error | MapAirbnbListingResponse]:
    """ Map an Airbnb listing to a Repull listing

     Link an existing Airbnb listing to a canonical Repull listing/property. **API-key-scoped** (unlike
    the Booking room mapping, which is Connect-session-scoped).

    Discover the `airbnbId` (+ `hostId`) via `GET /v1/channels/airbnb/listings`, then re-point it at the
    `listingId` of your choice — the dedup / consolidation case where the Airbnb sync auto-created its
    own listing but you want the inventory under an existing property.

    Repoints both the Airbnb record and its platform link to the target listing in one transaction.
    Idempotent — re-mapping to the same listing is a 200 no-op (`alreadyMapped: true`). Scope is
    enforced against your workspace on both the target listing and the existing Airbnb record; a listing
    that already links a different Airbnb listing returns 409.

    Args:
        body (MapAirbnbListingRequest): Body for `POST /v1/channels/airbnb/listings/map`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MapAirbnbListingResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: MapAirbnbListingRequest,

) -> Error | MapAirbnbListingResponse | None:
    """ Map an Airbnb listing to a Repull listing

     Link an existing Airbnb listing to a canonical Repull listing/property. **API-key-scoped** (unlike
    the Booking room mapping, which is Connect-session-scoped).

    Discover the `airbnbId` (+ `hostId`) via `GET /v1/channels/airbnb/listings`, then re-point it at the
    `listingId` of your choice — the dedup / consolidation case where the Airbnb sync auto-created its
    own listing but you want the inventory under an existing property.

    Repoints both the Airbnb record and its platform link to the target listing in one transaction.
    Idempotent — re-mapping to the same listing is a 200 no-op (`alreadyMapped: true`). Scope is
    enforced against your workspace on both the target listing and the existing Airbnb record; a listing
    that already links a different Airbnb listing returns 409.

    Args:
        body (MapAirbnbListingRequest): Body for `POST /v1/channels/airbnb/listings/map`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MapAirbnbListingResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MapAirbnbListingRequest,

) -> Response[Error | MapAirbnbListingResponse]:
    """ Map an Airbnb listing to a Repull listing

     Link an existing Airbnb listing to a canonical Repull listing/property. **API-key-scoped** (unlike
    the Booking room mapping, which is Connect-session-scoped).

    Discover the `airbnbId` (+ `hostId`) via `GET /v1/channels/airbnb/listings`, then re-point it at the
    `listingId` of your choice — the dedup / consolidation case where the Airbnb sync auto-created its
    own listing but you want the inventory under an existing property.

    Repoints both the Airbnb record and its platform link to the target listing in one transaction.
    Idempotent — re-mapping to the same listing is a 200 no-op (`alreadyMapped: true`). Scope is
    enforced against your workspace on both the target listing and the existing Airbnb record; a listing
    that already links a different Airbnb listing returns 409.

    Args:
        body (MapAirbnbListingRequest): Body for `POST /v1/channels/airbnb/listings/map`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MapAirbnbListingResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: MapAirbnbListingRequest,

) -> Error | MapAirbnbListingResponse | None:
    """ Map an Airbnb listing to a Repull listing

     Link an existing Airbnb listing to a canonical Repull listing/property. **API-key-scoped** (unlike
    the Booking room mapping, which is Connect-session-scoped).

    Discover the `airbnbId` (+ `hostId`) via `GET /v1/channels/airbnb/listings`, then re-point it at the
    `listingId` of your choice — the dedup / consolidation case where the Airbnb sync auto-created its
    own listing but you want the inventory under an existing property.

    Repoints both the Airbnb record and its platform link to the target listing in one transaction.
    Idempotent — re-mapping to the same listing is a 200 no-op (`alreadyMapped: true`). Scope is
    enforced against your workspace on both the target listing and the existing Airbnb record; a listing
    that already links a different Airbnb listing returns 409.

    Args:
        body (MapAirbnbListingRequest): Body for `POST /v1/channels/airbnb/listings/map`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MapAirbnbListingResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
