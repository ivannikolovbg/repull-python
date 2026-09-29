from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_listing_calendar_sync_response_200 import GetListingCalendarSyncResponse200
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/{id}/calendar-sync".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetListingCalendarSyncResponse200 | None:
    if response.status_code == 200:
        response_200 = GetListingCalendarSyncResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetListingCalendarSyncResponse200]:
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

) -> Response[Error | GetListingCalendarSyncResponse200]:
    """ Calendar sync status per channel

     Is this listing's calendar — prices, minimum stays, availability — actually on every channel it is
    connected to, and if not, which nights and why. One shape for every channel.

    Every push records each night's outcome per channel; a night the channel does not show as sent is
    listed in `problems` with the channel's own reason (a price the channel still shows differently, a
    block it refused, a unit that is not live, a night held by a booking or an imported calendar). A
    later successful push clears it.

    **VRBO** pushes run through a paced queue — VRBO accepts about 90 calendar writes a minute per
    account, and only what differs on VRBO is sent — so the `vrbo` entry adds `queue`: whether a push is
    waiting or running now, and what the last one did (prices and minimum stays changed, blocks, calls,
    nights still differing).

    Future nights only. `problems` lists up to 100 nights per channel; `nightsWithProblems` is always
    the full count.

    Returns `403 listing_inactive` for an inactive listing.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetListingCalendarSyncResponse200]
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

) -> Error | GetListingCalendarSyncResponse200 | None:
    """ Calendar sync status per channel

     Is this listing's calendar — prices, minimum stays, availability — actually on every channel it is
    connected to, and if not, which nights and why. One shape for every channel.

    Every push records each night's outcome per channel; a night the channel does not show as sent is
    listed in `problems` with the channel's own reason (a price the channel still shows differently, a
    block it refused, a unit that is not live, a night held by a booking or an imported calendar). A
    later successful push clears it.

    **VRBO** pushes run through a paced queue — VRBO accepts about 90 calendar writes a minute per
    account, and only what differs on VRBO is sent — so the `vrbo` entry adds `queue`: whether a push is
    waiting or running now, and what the last one did (prices and minimum stays changed, blocks, calls,
    nights still differing).

    Future nights only. `problems` lists up to 100 nights per channel; `nightsWithProblems` is always
    the full count.

    Returns `403 listing_inactive` for an inactive listing.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetListingCalendarSyncResponse200
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetListingCalendarSyncResponse200]:
    """ Calendar sync status per channel

     Is this listing's calendar — prices, minimum stays, availability — actually on every channel it is
    connected to, and if not, which nights and why. One shape for every channel.

    Every push records each night's outcome per channel; a night the channel does not show as sent is
    listed in `problems` with the channel's own reason (a price the channel still shows differently, a
    block it refused, a unit that is not live, a night held by a booking or an imported calendar). A
    later successful push clears it.

    **VRBO** pushes run through a paced queue — VRBO accepts about 90 calendar writes a minute per
    account, and only what differs on VRBO is sent — so the `vrbo` entry adds `queue`: whether a push is
    waiting or running now, and what the last one did (prices and minimum stays changed, blocks, calls,
    nights still differing).

    Future nights only. `problems` lists up to 100 nights per channel; `nightsWithProblems` is always
    the full count.

    Returns `403 listing_inactive` for an inactive listing.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetListingCalendarSyncResponse200]
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

) -> Error | GetListingCalendarSyncResponse200 | None:
    """ Calendar sync status per channel

     Is this listing's calendar — prices, minimum stays, availability — actually on every channel it is
    connected to, and if not, which nights and why. One shape for every channel.

    Every push records each night's outcome per channel; a night the channel does not show as sent is
    listed in `problems` with the channel's own reason (a price the channel still shows differently, a
    block it refused, a unit that is not live, a night held by a booking or an imported calendar). A
    later successful push clears it.

    **VRBO** pushes run through a paced queue — VRBO accepts about 90 calendar writes a minute per
    account, and only what differs on VRBO is sent — so the `vrbo` entry adds `queue`: whether a push is
    waiting or running now, and what the last one did (prices and minimum stays changed, blocks, calls,
    nights still differing).

    Future nights only. `problems` lists up to 100 nights per channel; `nightsWithProblems` is always
    the full count.

    Returns `403 listing_inactive` for an inactive listing.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetListingCalendarSyncResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
