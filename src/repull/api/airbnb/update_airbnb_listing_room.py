from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.update_airbnb_listing_room_body import UpdateAirbnbListingRoomBody
from ...models.update_airbnb_listing_room_response_200 import UpdateAirbnbListingRoomResponse200
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: UpdateAirbnbListingRoomBody,
    room_id: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["roomId"] = room_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/airbnb/listings/{id}/rooms".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | UpdateAirbnbListingRoomResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateAirbnbListingRoomResponse200.from_dict(response.json())



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

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | UpdateAirbnbListingRoomResponse200]:
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
    body: UpdateAirbnbListingRoomBody,
    room_id: str,

) -> Response[Error | UpdateAirbnbListingRoomResponse200]:
    """ Update an Airbnb room

     Change a room's type, number, privacy or sleeping arrangement. **Write-side** — calls Airbnb
    upstream. Pass the Airbnb-side room id as `?roomId=` and send only the fields you want to change.

    `beds` REPLACES the room's whole arrangement — that is Airbnb's semantics for the field — so send
    every bed the room has, not just the changed one.

    Airbnb's room endpoints are keyed by room id alone, so the room is proven to belong to the listing
    named in the path before anything is sent; a room from another listing returns `404`, the same
    answer a room that does not exist gets.

    On success both stored copies are rebuilt to match, so a read straight after this write returns the
    new arrangement. `stored` says whether that succeeded.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        room_id (str):
        body (UpdateAirbnbListingRoomBody): At least one field. A body that changes nothing is
            refused rather than reported as a successful write.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbListingRoomResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
room_id=room_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAirbnbListingRoomBody,
    room_id: str,

) -> Error | UpdateAirbnbListingRoomResponse200 | None:
    """ Update an Airbnb room

     Change a room's type, number, privacy or sleeping arrangement. **Write-side** — calls Airbnb
    upstream. Pass the Airbnb-side room id as `?roomId=` and send only the fields you want to change.

    `beds` REPLACES the room's whole arrangement — that is Airbnb's semantics for the field — so send
    every bed the room has, not just the changed one.

    Airbnb's room endpoints are keyed by room id alone, so the room is proven to belong to the listing
    named in the path before anything is sent; a room from another listing returns `404`, the same
    answer a room that does not exist gets.

    On success both stored copies are rebuilt to match, so a read straight after this write returns the
    new arrangement. `stored` says whether that succeeded.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        room_id (str):
        body (UpdateAirbnbListingRoomBody): At least one field. A body that changes nothing is
            refused rather than reported as a successful write.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbListingRoomResponse200
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
room_id=room_id,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAirbnbListingRoomBody,
    room_id: str,

) -> Response[Error | UpdateAirbnbListingRoomResponse200]:
    """ Update an Airbnb room

     Change a room's type, number, privacy or sleeping arrangement. **Write-side** — calls Airbnb
    upstream. Pass the Airbnb-side room id as `?roomId=` and send only the fields you want to change.

    `beds` REPLACES the room's whole arrangement — that is Airbnb's semantics for the field — so send
    every bed the room has, not just the changed one.

    Airbnb's room endpoints are keyed by room id alone, so the room is proven to belong to the listing
    named in the path before anything is sent; a room from another listing returns `404`, the same
    answer a room that does not exist gets.

    On success both stored copies are rebuilt to match, so a read straight after this write returns the
    new arrangement. `stored` says whether that succeeded.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        room_id (str):
        body (UpdateAirbnbListingRoomBody): At least one field. A body that changes nothing is
            refused rather than reported as a successful write.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbListingRoomResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
room_id=room_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAirbnbListingRoomBody,
    room_id: str,

) -> Error | UpdateAirbnbListingRoomResponse200 | None:
    """ Update an Airbnb room

     Change a room's type, number, privacy or sleeping arrangement. **Write-side** — calls Airbnb
    upstream. Pass the Airbnb-side room id as `?roomId=` and send only the fields you want to change.

    `beds` REPLACES the room's whole arrangement — that is Airbnb's semantics for the field — so send
    every bed the room has, not just the changed one.

    Airbnb's room endpoints are keyed by room id alone, so the room is proven to belong to the listing
    named in the path before anything is sent; a room from another listing returns `404`, the same
    answer a room that does not exist gets.

    On success both stored copies are rebuilt to match, so a read straight after this write returns the
    new arrangement. `stored` says whether that succeeded.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        room_id (str):
        body (UpdateAirbnbListingRoomBody): At least one field. A body that changes nothing is
            refused rather than reported as a successful write.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbListingRoomResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
room_id=room_id,

    )).parsed
