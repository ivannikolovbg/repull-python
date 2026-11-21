from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.map_vrbo_listing_body import MapVrboListingBody
from ...models.map_vrbo_listing_response_200 import MapVrboListingResponse200
from typing import cast



def _get_kwargs(
    *,
    body: MapVrboListingBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/vrbo/listings/map",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | MapVrboListingResponse200 | None:
    if response.status_code == 200:
        response_200 = MapVrboListingResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | MapVrboListingResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MapVrboListingBody,

) -> Response[Error | MapVrboListingResponse200]:
    """ Link a Vrbo listing to a Repull listing

     Link a Vrbo unit that is already on the host's connected Vrbo account to a Repull listing — the Vrbo
    counterpart of `POST /v1/channels/airbnb/listings/map`. Send `listingId` to link it to that listing,
    or `create: true` to create a Repull listing from what Vrbo shows. Once linked, the unit's bookings
    and messages are imported (upcoming ones and the last 30 days first).

    `accountId` names the Vrbo account when the workspace has several (`GET /v1/connect/vrbo-login`).
    `syncEnabled: true` also sends the listing's calendar to Vrbo (full access; refused with `409
    calendar_managed_elsewhere` while another tool manages the account's calendar).

    The same write as `POST /v1/connections/{id}/mappings`, for one unit.

    Args:
        body (MapVrboListingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MapVrboListingResponse200]
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
    body: MapVrboListingBody,

) -> Error | MapVrboListingResponse200 | None:
    """ Link a Vrbo listing to a Repull listing

     Link a Vrbo unit that is already on the host's connected Vrbo account to a Repull listing — the Vrbo
    counterpart of `POST /v1/channels/airbnb/listings/map`. Send `listingId` to link it to that listing,
    or `create: true` to create a Repull listing from what Vrbo shows. Once linked, the unit's bookings
    and messages are imported (upcoming ones and the last 30 days first).

    `accountId` names the Vrbo account when the workspace has several (`GET /v1/connect/vrbo-login`).
    `syncEnabled: true` also sends the listing's calendar to Vrbo (full access; refused with `409
    calendar_managed_elsewhere` while another tool manages the account's calendar).

    The same write as `POST /v1/connections/{id}/mappings`, for one unit.

    Args:
        body (MapVrboListingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MapVrboListingResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: MapVrboListingBody,

) -> Response[Error | MapVrboListingResponse200]:
    """ Link a Vrbo listing to a Repull listing

     Link a Vrbo unit that is already on the host's connected Vrbo account to a Repull listing — the Vrbo
    counterpart of `POST /v1/channels/airbnb/listings/map`. Send `listingId` to link it to that listing,
    or `create: true` to create a Repull listing from what Vrbo shows. Once linked, the unit's bookings
    and messages are imported (upcoming ones and the last 30 days first).

    `accountId` names the Vrbo account when the workspace has several (`GET /v1/connect/vrbo-login`).
    `syncEnabled: true` also sends the listing's calendar to Vrbo (full access; refused with `409
    calendar_managed_elsewhere` while another tool manages the account's calendar).

    The same write as `POST /v1/connections/{id}/mappings`, for one unit.

    Args:
        body (MapVrboListingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MapVrboListingResponse200]
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
    body: MapVrboListingBody,

) -> Error | MapVrboListingResponse200 | None:
    """ Link a Vrbo listing to a Repull listing

     Link a Vrbo unit that is already on the host's connected Vrbo account to a Repull listing — the Vrbo
    counterpart of `POST /v1/channels/airbnb/listings/map`. Send `listingId` to link it to that listing,
    or `create: true` to create a Repull listing from what Vrbo shows. Once linked, the unit's bookings
    and messages are imported (upcoming ones and the last 30 days first).

    `accountId` names the Vrbo account when the workspace has several (`GET /v1/connect/vrbo-login`).
    `syncEnabled: true` also sends the listing's calendar to Vrbo (full access; refused with `409
    calendar_managed_elsewhere` while another tool manages the account's calendar).

    The same write as `POST /v1/connections/{id}/mappings`, for one unit.

    Args:
        body (MapVrboListingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MapVrboListingResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
