from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_vrbo_listing_location_response_200 import GetVrboListingLocationResponse200
from ...models.get_vrbo_listing_location_source import GetVrboListingLocationSource
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    vrbo_listing_number: str | Unset = UNSET,
    source: GetVrboListingLocationSource | Unset = GetVrboListingLocationSource.STORED,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["vrboListingNumber"] = vrbo_listing_number

    json_source: str | Unset = UNSET
    if not isinstance(source, Unset):
        json_source = source.value

    params["source"] = json_source


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/vrbo/listings/{id}/location".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetVrboListingLocationResponse200 | None:
    if response.status_code == 200:
        response_200 = GetVrboListingLocationResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetVrboListingLocationResponse200]:
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
    vrbo_listing_number: str | Unset = UNSET,
    source: GetVrboListingLocationSource | Unset = GetVrboListingLocationSource.STORED,

) -> Response[Error | GetVrboListingLocationResponse200]:
    """ Get the Vrbo map setting

     The address (read-only: Vrbo changes it only through its support) and whether guests see the exact
    location or an area.

    Answers from Repull's stored copy of the listing's Vrbo content, like the Airbnb endpoints
    (`dataFreshness.lastSyncedAt` says when it was read from Vrbo). The first read of a section reads
    Vrbo and stores it; a copy over 24 h old answers and is refreshed in the background (`reason:
    refreshing`); every write through Repull stores what Vrbo has after it. `?source=live` reads Vrbo
    now. **Cost:** from the copy, milliseconds. A live read is 1 Vrbo call on Vrbo, spaced ~3 s apart
    per account — a few seconds.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        source (GetVrboListingLocationSource | Unset):  Default:
            GetVrboListingLocationSource.STORED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboListingLocationResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
vrbo_listing_number=vrbo_listing_number,
source=source,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    vrbo_listing_number: str | Unset = UNSET,
    source: GetVrboListingLocationSource | Unset = GetVrboListingLocationSource.STORED,

) -> Error | GetVrboListingLocationResponse200 | None:
    """ Get the Vrbo map setting

     The address (read-only: Vrbo changes it only through its support) and whether guests see the exact
    location or an area.

    Answers from Repull's stored copy of the listing's Vrbo content, like the Airbnb endpoints
    (`dataFreshness.lastSyncedAt` says when it was read from Vrbo). The first read of a section reads
    Vrbo and stores it; a copy over 24 h old answers and is refreshed in the background (`reason:
    refreshing`); every write through Repull stores what Vrbo has after it. `?source=live` reads Vrbo
    now. **Cost:** from the copy, milliseconds. A live read is 1 Vrbo call on Vrbo, spaced ~3 s apart
    per account — a few seconds.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        source (GetVrboListingLocationSource | Unset):  Default:
            GetVrboListingLocationSource.STORED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboListingLocationResponse200
     """


    return sync_detailed(
        id=id,
client=client,
vrbo_listing_number=vrbo_listing_number,
source=source,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    vrbo_listing_number: str | Unset = UNSET,
    source: GetVrboListingLocationSource | Unset = GetVrboListingLocationSource.STORED,

) -> Response[Error | GetVrboListingLocationResponse200]:
    """ Get the Vrbo map setting

     The address (read-only: Vrbo changes it only through its support) and whether guests see the exact
    location or an area.

    Answers from Repull's stored copy of the listing's Vrbo content, like the Airbnb endpoints
    (`dataFreshness.lastSyncedAt` says when it was read from Vrbo). The first read of a section reads
    Vrbo and stores it; a copy over 24 h old answers and is refreshed in the background (`reason:
    refreshing`); every write through Repull stores what Vrbo has after it. `?source=live` reads Vrbo
    now. **Cost:** from the copy, milliseconds. A live read is 1 Vrbo call on Vrbo, spaced ~3 s apart
    per account — a few seconds.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        source (GetVrboListingLocationSource | Unset):  Default:
            GetVrboListingLocationSource.STORED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboListingLocationResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
vrbo_listing_number=vrbo_listing_number,
source=source,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    vrbo_listing_number: str | Unset = UNSET,
    source: GetVrboListingLocationSource | Unset = GetVrboListingLocationSource.STORED,

) -> Error | GetVrboListingLocationResponse200 | None:
    """ Get the Vrbo map setting

     The address (read-only: Vrbo changes it only through its support) and whether guests see the exact
    location or an area.

    Answers from Repull's stored copy of the listing's Vrbo content, like the Airbnb endpoints
    (`dataFreshness.lastSyncedAt` says when it was read from Vrbo). The first read of a section reads
    Vrbo and stores it; a copy over 24 h old answers and is refreshed in the background (`reason:
    refreshing`); every write through Repull stores what Vrbo has after it. `?source=live` reads Vrbo
    now. **Cost:** from the copy, milliseconds. A live read is 1 Vrbo call on Vrbo, spaced ~3 s apart
    per account — a few seconds.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        source (GetVrboListingLocationSource | Unset):  Default:
            GetVrboListingLocationSource.STORED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboListingLocationResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
vrbo_listing_number=vrbo_listing_number,
source=source,

    )).parsed
