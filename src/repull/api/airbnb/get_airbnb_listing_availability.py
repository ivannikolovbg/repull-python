from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/listings/{id}/availability".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

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

) -> Response[Any | Error]:
    r""" Get Airbnb availability

     Read the per-day availability calendar for an Airbnb listing. Returns one row per day including
    price overrides, min-stay, and blocked status.

    The calendar is served from Repull's stored copy, refreshed by the periodic sync. A successful
    calendar write through `PUT .../availability` or `PUT .../pricing` (`type: \"calendar\"`) updates
    the stored days immediately, so reading back right after a write returns the values you published.
    Changes made directly on Airbnb appear after the next sync (`dataFreshness.lastSyncedAt`).

    **Coverage:** with `start_date` + `end_date`, `data.coverage` gives `{ from, to }`, the first and
    last stored date for the listing (the sync keeps about 12 months ahead). A date outside that window
    is not stored, so a missing date there means \"not covered\", not \"nothing set\". Request it again
    once `coverage.to` reaches it.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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

) -> Any | Error | None:
    r""" Get Airbnb availability

     Read the per-day availability calendar for an Airbnb listing. Returns one row per day including
    price overrides, min-stay, and blocked status.

    The calendar is served from Repull's stored copy, refreshed by the periodic sync. A successful
    calendar write through `PUT .../availability` or `PUT .../pricing` (`type: \"calendar\"`) updates
    the stored days immediately, so reading back right after a write returns the values you published.
    Changes made directly on Airbnb appear after the next sync (`dataFreshness.lastSyncedAt`).

    **Coverage:** with `start_date` + `end_date`, `data.coverage` gives `{ from, to }`, the first and
    last stored date for the listing (the sync keeps about 12 months ahead). A date outside that window
    is not stored, so a missing date there means \"not covered\", not \"nothing set\". Request it again
    once `coverage.to` reaches it.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | Error]:
    r""" Get Airbnb availability

     Read the per-day availability calendar for an Airbnb listing. Returns one row per day including
    price overrides, min-stay, and blocked status.

    The calendar is served from Repull's stored copy, refreshed by the periodic sync. A successful
    calendar write through `PUT .../availability` or `PUT .../pricing` (`type: \"calendar\"`) updates
    the stored days immediately, so reading back right after a write returns the values you published.
    Changes made directly on Airbnb appear after the next sync (`dataFreshness.lastSyncedAt`).

    **Coverage:** with `start_date` + `end_date`, `data.coverage` gives `{ from, to }`, the first and
    last stored date for the listing (the sync keeps about 12 months ahead). A date outside that window
    is not stored, so a missing date there means \"not covered\", not \"nothing set\". Request it again
    once `coverage.to` reaches it.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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

) -> Any | Error | None:
    r""" Get Airbnb availability

     Read the per-day availability calendar for an Airbnb listing. Returns one row per day including
    price overrides, min-stay, and blocked status.

    The calendar is served from Repull's stored copy, refreshed by the periodic sync. A successful
    calendar write through `PUT .../availability` or `PUT .../pricing` (`type: \"calendar\"`) updates
    the stored days immediately, so reading back right after a write returns the values you published.
    Changes made directly on Airbnb appear after the next sync (`dataFreshness.lastSyncedAt`).

    **Coverage:** with `start_date` + `end_date`, `data.coverage` gives `{ from, to }`, the first and
    last stored date for the listing (the sync keeps about 12 months ahead). A date outside that window
    is not stored, so a missing date there means \"not covered\", not \"nothing set\". Request it again
    once `coverage.to` reaches it.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
