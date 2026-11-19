from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_listing_ical_response_200 import GetListingIcalResponse200
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/{id}/ical".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetListingIcalResponse200 | None:
    if response.status_code == 200:
        response_200 = GetListingIcalResponse200.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetListingIcalResponse200]:
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

) -> Response[Error | GetListingIcalResponse200]:
    r""" Repull iCal backup feed

     The listing's Repull iCal backup feed: an iCal calendar named \"Repull\" with the listing's bookings
    and blocks as all-day events, at an unguessable address on `api.repull.dev` (created on first
    request, one per listing). Channels that import iCal close those nights from it on their own
    schedule — availability only, never prices.

    **Vrbo:** Repull imports this feed into every calendar-synced Vrbo unit by itself, as a backup for
    the direct calendar push, and removes other tools' imported feeds while Repull is the unit's master
    calendar. `vrbo` says, per unit, whether Vrbo imports it (as last checked, once a day). When
    `status` is `failed`, ask the host to add `url` in Vrbo → Calendar → Import calendar, named
    \"Repull\". Changes arrive as `listing.ical_feed_changed`.

    The address is a credential: anyone with it can read the listing's booked dates (no guest details).
    Returns `403 listing_inactive` for an inactive listing.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetListingIcalResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetListingIcalResponse200 | None:
    r""" Repull iCal backup feed

     The listing's Repull iCal backup feed: an iCal calendar named \"Repull\" with the listing's bookings
    and blocks as all-day events, at an unguessable address on `api.repull.dev` (created on first
    request, one per listing). Channels that import iCal close those nights from it on their own
    schedule — availability only, never prices.

    **Vrbo:** Repull imports this feed into every calendar-synced Vrbo unit by itself, as a backup for
    the direct calendar push, and removes other tools' imported feeds while Repull is the unit's master
    calendar. `vrbo` says, per unit, whether Vrbo imports it (as last checked, once a day). When
    `status` is `failed`, ask the host to add `url` in Vrbo → Calendar → Import calendar, named
    \"Repull\". Changes arrive as `listing.ical_feed_changed`.

    The address is a credential: anyone with it can read the listing's booked dates (no guest details).
    Returns `403 listing_inactive` for an inactive listing.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetListingIcalResponse200
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetListingIcalResponse200]:
    r""" Repull iCal backup feed

     The listing's Repull iCal backup feed: an iCal calendar named \"Repull\" with the listing's bookings
    and blocks as all-day events, at an unguessable address on `api.repull.dev` (created on first
    request, one per listing). Channels that import iCal close those nights from it on their own
    schedule — availability only, never prices.

    **Vrbo:** Repull imports this feed into every calendar-synced Vrbo unit by itself, as a backup for
    the direct calendar push, and removes other tools' imported feeds while Repull is the unit's master
    calendar. `vrbo` says, per unit, whether Vrbo imports it (as last checked, once a day). When
    `status` is `failed`, ask the host to add `url` in Vrbo → Calendar → Import calendar, named
    \"Repull\". Changes arrive as `listing.ical_feed_changed`.

    The address is a credential: anyone with it can read the listing's booked dates (no guest details).
    Returns `403 listing_inactive` for an inactive listing.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetListingIcalResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetListingIcalResponse200 | None:
    r""" Repull iCal backup feed

     The listing's Repull iCal backup feed: an iCal calendar named \"Repull\" with the listing's bookings
    and blocks as all-day events, at an unguessable address on `api.repull.dev` (created on first
    request, one per listing). Channels that import iCal close those nights from it on their own
    schedule — availability only, never prices.

    **Vrbo:** Repull imports this feed into every calendar-synced Vrbo unit by itself, as a backup for
    the direct calendar push, and removes other tools' imported feeds while Repull is the unit's master
    calendar. `vrbo` says, per unit, whether Vrbo imports it (as last checked, once a day). When
    `status` is `failed`, ask the host to add `url` in Vrbo → Calendar → Import calendar, named
    \"Repull\". Changes arrive as `listing.ical_feed_changed`.

    The address is a credential: anyone with it can read the listing's booked dates (no guest details).
    Returns `403 listing_inactive` for an inactive listing.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetListingIcalResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
