from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.update_vrbo_listing_availability_body import UpdateVrboListingAvailabilityBody
from ...models.update_vrbo_listing_availability_response_202 import UpdateVrboListingAvailabilityResponse202
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: UpdateVrboListingAvailabilityBody,
    vrbo_listing_number: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["vrboListingNumber"] = vrbo_listing_number


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/vrbo/listings/{id}/availability".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | UpdateVrboListingAvailabilityResponse202 | None:
    if response.status_code == 202:
        response_202 = UpdateVrboListingAvailabilityResponse202.from_dict(response.json())



        return response_202

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | UpdateVrboListingAvailabilityResponse202]:
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
    body: UpdateVrboListingAvailabilityBody,
    vrbo_listing_number: str | Unset = UNSET,

) -> Response[Error | UpdateVrboListingAvailabilityResponse202]:
    r""" Update the Vrbo calendar

     Write nights to Vrbo only — the counterpart of `PUT /v1/channels/airbnb/listings/{id}/availability`
    with `type: \"calendar\"`, with its operation fields: `daily_price`, `availability`, `min_nights`,
    `closed_to_arrival`, `closed_to_departure`.

    The writes are queued with the account's other Vrbo calendar writes, which Vrbo takes at a pace of
    its own, so this answers `202` with a `jobId`: read its status with `GET …/availability?jobId=`. The
    listing's own calendar is not changed, and its next push for the same nights puts its own values
    back (as on Airbnb). For a change on every channel use `PUT /v1/availability/{propertyId}`.

    Listing-level stay rules (default minimum stay, notice, booking window) are Vrbo's booking settings:
    `PUT /v1/channels/vrbo/listings/{id}/booking-settings` (`type: \"rules\"` is refused with that
    pointer). Nights up to 730 days ahead. Needs full access (`403 vrbo_messaging_access`); `409
    calendar_managed_elsewhere` while another tool manages the account's calendar on Vrbo.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        body (UpdateVrboListingAvailabilityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateVrboListingAvailabilityResponse202]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
vrbo_listing_number=vrbo_listing_number,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateVrboListingAvailabilityBody,
    vrbo_listing_number: str | Unset = UNSET,

) -> Error | UpdateVrboListingAvailabilityResponse202 | None:
    r""" Update the Vrbo calendar

     Write nights to Vrbo only — the counterpart of `PUT /v1/channels/airbnb/listings/{id}/availability`
    with `type: \"calendar\"`, with its operation fields: `daily_price`, `availability`, `min_nights`,
    `closed_to_arrival`, `closed_to_departure`.

    The writes are queued with the account's other Vrbo calendar writes, which Vrbo takes at a pace of
    its own, so this answers `202` with a `jobId`: read its status with `GET …/availability?jobId=`. The
    listing's own calendar is not changed, and its next push for the same nights puts its own values
    back (as on Airbnb). For a change on every channel use `PUT /v1/availability/{propertyId}`.

    Listing-level stay rules (default minimum stay, notice, booking window) are Vrbo's booking settings:
    `PUT /v1/channels/vrbo/listings/{id}/booking-settings` (`type: \"rules\"` is refused with that
    pointer). Nights up to 730 days ahead. Needs full access (`403 vrbo_messaging_access`); `409
    calendar_managed_elsewhere` while another tool manages the account's calendar on Vrbo.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        body (UpdateVrboListingAvailabilityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateVrboListingAvailabilityResponse202
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
vrbo_listing_number=vrbo_listing_number,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateVrboListingAvailabilityBody,
    vrbo_listing_number: str | Unset = UNSET,

) -> Response[Error | UpdateVrboListingAvailabilityResponse202]:
    r""" Update the Vrbo calendar

     Write nights to Vrbo only — the counterpart of `PUT /v1/channels/airbnb/listings/{id}/availability`
    with `type: \"calendar\"`, with its operation fields: `daily_price`, `availability`, `min_nights`,
    `closed_to_arrival`, `closed_to_departure`.

    The writes are queued with the account's other Vrbo calendar writes, which Vrbo takes at a pace of
    its own, so this answers `202` with a `jobId`: read its status with `GET …/availability?jobId=`. The
    listing's own calendar is not changed, and its next push for the same nights puts its own values
    back (as on Airbnb). For a change on every channel use `PUT /v1/availability/{propertyId}`.

    Listing-level stay rules (default minimum stay, notice, booking window) are Vrbo's booking settings:
    `PUT /v1/channels/vrbo/listings/{id}/booking-settings` (`type: \"rules\"` is refused with that
    pointer). Nights up to 730 days ahead. Needs full access (`403 vrbo_messaging_access`); `409
    calendar_managed_elsewhere` while another tool manages the account's calendar on Vrbo.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        body (UpdateVrboListingAvailabilityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateVrboListingAvailabilityResponse202]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
vrbo_listing_number=vrbo_listing_number,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateVrboListingAvailabilityBody,
    vrbo_listing_number: str | Unset = UNSET,

) -> Error | UpdateVrboListingAvailabilityResponse202 | None:
    r""" Update the Vrbo calendar

     Write nights to Vrbo only — the counterpart of `PUT /v1/channels/airbnb/listings/{id}/availability`
    with `type: \"calendar\"`, with its operation fields: `daily_price`, `availability`, `min_nights`,
    `closed_to_arrival`, `closed_to_departure`.

    The writes are queued with the account's other Vrbo calendar writes, which Vrbo takes at a pace of
    its own, so this answers `202` with a `jobId`: read its status with `GET …/availability?jobId=`. The
    listing's own calendar is not changed, and its next push for the same nights puts its own values
    back (as on Airbnb). For a change on every channel use `PUT /v1/availability/{propertyId}`.

    Listing-level stay rules (default minimum stay, notice, booking window) are Vrbo's booking settings:
    `PUT /v1/channels/vrbo/listings/{id}/booking-settings` (`type: \"rules\"` is refused with that
    pointer). Nights up to 730 days ahead. Needs full access (`403 vrbo_messaging_access`); `409
    calendar_managed_elsewhere` while another tool manages the account's calendar on Vrbo.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        body (UpdateVrboListingAvailabilityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateVrboListingAvailabilityResponse202
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
vrbo_listing_number=vrbo_listing_number,

    )).parsed
