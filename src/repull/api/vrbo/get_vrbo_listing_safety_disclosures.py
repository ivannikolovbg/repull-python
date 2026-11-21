from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_vrbo_listing_safety_disclosures_response_200 import GetVrboListingSafetyDisclosuresResponse200
from ...models.get_vrbo_listing_safety_disclosures_source import GetVrboListingSafetyDisclosuresSource
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    source: GetVrboListingSafetyDisclosuresSource | Unset = GetVrboListingSafetyDisclosuresSource.STORED,
    vrbo_listing_number: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_source: str | Unset = UNSET
    if not isinstance(source, Unset):
        json_source = source.value

    params["source"] = json_source

    params["vrboListingNumber"] = vrbo_listing_number


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/vrbo/listings/{id}/safety-disclosures".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetVrboListingSafetyDisclosuresResponse200 | None:
    if response.status_code == 200:
        response_200 = GetVrboListingSafetyDisclosuresResponse200.from_dict(response.json())



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
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

    if response.status_code == 504:
        response_504 = Error.from_dict(response.json())



        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetVrboListingSafetyDisclosuresResponse200]:
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
    source: GetVrboListingSafetyDisclosuresSource | Unset = GetVrboListingSafetyDisclosuresSource.STORED,
    vrbo_listing_number: str | Unset = UNSET,

) -> Response[Error | GetVrboListingSafetyDisclosuresResponse200]:
    """ Get the Vrbo safety disclosures

     What the listing tells guests about safety — the same path as Airbnb's safety disclosures. On Vrbo
    these are two amenity groups, field by field like GET …/amenities: `homeSafety` (smoke and carbon-
    monoxide detectors, fire extinguisher, deadbolt lock, exterior lighting, first-aid kit and where it
    is, emergency exit instructions, hospital and police contacts) and `safetyDevices` (smoke and
    carbon-monoxide detectors, gas-powered appliances). The detector questions are choices (`yes` /
    `no`, see each field's `options`).

    Answers from Repull's stored copy of the listing's Vrbo content, like the Airbnb endpoints
    (`dataFreshness.lastSyncedAt` says when it was read from Vrbo). The first read of a section reads
    Vrbo and stores it; a copy over 24 h old answers and is refreshed in the background (`reason:
    refreshing`); every write through Repull stores what Vrbo has after it. `?source=live` reads Vrbo
    now. **Cost:** from the copy, milliseconds; a live read is 2 Vrbo calls.

    Args:
        id (str):
        source (GetVrboListingSafetyDisclosuresSource | Unset):  Default:
            GetVrboListingSafetyDisclosuresSource.STORED.
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboListingSafetyDisclosuresResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
source=source,
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
    source: GetVrboListingSafetyDisclosuresSource | Unset = GetVrboListingSafetyDisclosuresSource.STORED,
    vrbo_listing_number: str | Unset = UNSET,

) -> Error | GetVrboListingSafetyDisclosuresResponse200 | None:
    """ Get the Vrbo safety disclosures

     What the listing tells guests about safety — the same path as Airbnb's safety disclosures. On Vrbo
    these are two amenity groups, field by field like GET …/amenities: `homeSafety` (smoke and carbon-
    monoxide detectors, fire extinguisher, deadbolt lock, exterior lighting, first-aid kit and where it
    is, emergency exit instructions, hospital and police contacts) and `safetyDevices` (smoke and
    carbon-monoxide detectors, gas-powered appliances). The detector questions are choices (`yes` /
    `no`, see each field's `options`).

    Answers from Repull's stored copy of the listing's Vrbo content, like the Airbnb endpoints
    (`dataFreshness.lastSyncedAt` says when it was read from Vrbo). The first read of a section reads
    Vrbo and stores it; a copy over 24 h old answers and is refreshed in the background (`reason:
    refreshing`); every write through Repull stores what Vrbo has after it. `?source=live` reads Vrbo
    now. **Cost:** from the copy, milliseconds; a live read is 2 Vrbo calls.

    Args:
        id (str):
        source (GetVrboListingSafetyDisclosuresSource | Unset):  Default:
            GetVrboListingSafetyDisclosuresSource.STORED.
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboListingSafetyDisclosuresResponse200
     """


    return sync_detailed(
        id=id,
client=client,
source=source,
vrbo_listing_number=vrbo_listing_number,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    source: GetVrboListingSafetyDisclosuresSource | Unset = GetVrboListingSafetyDisclosuresSource.STORED,
    vrbo_listing_number: str | Unset = UNSET,

) -> Response[Error | GetVrboListingSafetyDisclosuresResponse200]:
    """ Get the Vrbo safety disclosures

     What the listing tells guests about safety — the same path as Airbnb's safety disclosures. On Vrbo
    these are two amenity groups, field by field like GET …/amenities: `homeSafety` (smoke and carbon-
    monoxide detectors, fire extinguisher, deadbolt lock, exterior lighting, first-aid kit and where it
    is, emergency exit instructions, hospital and police contacts) and `safetyDevices` (smoke and
    carbon-monoxide detectors, gas-powered appliances). The detector questions are choices (`yes` /
    `no`, see each field's `options`).

    Answers from Repull's stored copy of the listing's Vrbo content, like the Airbnb endpoints
    (`dataFreshness.lastSyncedAt` says when it was read from Vrbo). The first read of a section reads
    Vrbo and stores it; a copy over 24 h old answers and is refreshed in the background (`reason:
    refreshing`); every write through Repull stores what Vrbo has after it. `?source=live` reads Vrbo
    now. **Cost:** from the copy, milliseconds; a live read is 2 Vrbo calls.

    Args:
        id (str):
        source (GetVrboListingSafetyDisclosuresSource | Unset):  Default:
            GetVrboListingSafetyDisclosuresSource.STORED.
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboListingSafetyDisclosuresResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
source=source,
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
    source: GetVrboListingSafetyDisclosuresSource | Unset = GetVrboListingSafetyDisclosuresSource.STORED,
    vrbo_listing_number: str | Unset = UNSET,

) -> Error | GetVrboListingSafetyDisclosuresResponse200 | None:
    """ Get the Vrbo safety disclosures

     What the listing tells guests about safety — the same path as Airbnb's safety disclosures. On Vrbo
    these are two amenity groups, field by field like GET …/amenities: `homeSafety` (smoke and carbon-
    monoxide detectors, fire extinguisher, deadbolt lock, exterior lighting, first-aid kit and where it
    is, emergency exit instructions, hospital and police contacts) and `safetyDevices` (smoke and
    carbon-monoxide detectors, gas-powered appliances). The detector questions are choices (`yes` /
    `no`, see each field's `options`).

    Answers from Repull's stored copy of the listing's Vrbo content, like the Airbnb endpoints
    (`dataFreshness.lastSyncedAt` says when it was read from Vrbo). The first read of a section reads
    Vrbo and stores it; a copy over 24 h old answers and is refreshed in the background (`reason:
    refreshing`); every write through Repull stores what Vrbo has after it. `?source=live` reads Vrbo
    now. **Cost:** from the copy, milliseconds; a live read is 2 Vrbo calls.

    Args:
        id (str):
        source (GetVrboListingSafetyDisclosuresSource | Unset):  Default:
            GetVrboListingSafetyDisclosuresSource.STORED.
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboListingSafetyDisclosuresResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
source=source,
vrbo_listing_number=vrbo_listing_number,

    )).parsed
