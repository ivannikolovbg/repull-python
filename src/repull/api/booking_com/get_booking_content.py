from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_booking_content_type import GetBookingContentType
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    property_id: str,
    type_: GetBookingContentType | Unset = GetBookingContentType.PHOTOS,
    room_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["property_id"] = property_id

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["room_id"] = room_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/booking/content",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    property_id: str,
    type_: GetBookingContentType | Unset = GetBookingContentType.PHOTOS,
    room_id: str | Unset = UNSET,

) -> Response[Any | Error]:
    """ Get Booking.com content

     Read one kind of content for a Booking.com property, straight from Booking.com.

    | `type` | What it is |
    |---|---|
    | `photos` | The property's photos. Add `room_id` to read one room's gallery. |
    | `facilities` | Property facilities, or a room's with `room_id` (Booking.com's ids — `GET` returns
    them). |
    | `description` | The property description. Booking.com rewrites what you send into its own
    multilingual copy; allow about 3 hours to appear. |
    | `settings` | House rules, pets, children, damage deposit, invoice recipient, booking model. |
    | `policies` | Cancellation and prepayment policies. |
    | `licences` | The region's licence rules and the licence on file. |
    | `checkin_methods` | How guests get in (holiday homes). |
    | `contacts` | Who Booking.com contacts about the property. |

    `amenities` is accepted as another name for `facilities`, and `descriptions` for `description`.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        property_id (str):
        type_ (GetBookingContentType | Unset):  Default: GetBookingContentType.PHOTOS.
        room_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
type_=type_,
room_id=room_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    property_id: str,
    type_: GetBookingContentType | Unset = GetBookingContentType.PHOTOS,
    room_id: str | Unset = UNSET,

) -> Any | Error | None:
    """ Get Booking.com content

     Read one kind of content for a Booking.com property, straight from Booking.com.

    | `type` | What it is |
    |---|---|
    | `photos` | The property's photos. Add `room_id` to read one room's gallery. |
    | `facilities` | Property facilities, or a room's with `room_id` (Booking.com's ids — `GET` returns
    them). |
    | `description` | The property description. Booking.com rewrites what you send into its own
    multilingual copy; allow about 3 hours to appear. |
    | `settings` | House rules, pets, children, damage deposit, invoice recipient, booking model. |
    | `policies` | Cancellation and prepayment policies. |
    | `licences` | The region's licence rules and the licence on file. |
    | `checkin_methods` | How guests get in (holiday homes). |
    | `contacts` | Who Booking.com contacts about the property. |

    `amenities` is accepted as another name for `facilities`, and `descriptions` for `description`.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        property_id (str):
        type_ (GetBookingContentType | Unset):  Default: GetBookingContentType.PHOTOS.
        room_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        client=client,
property_id=property_id,
type_=type_,
room_id=room_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    property_id: str,
    type_: GetBookingContentType | Unset = GetBookingContentType.PHOTOS,
    room_id: str | Unset = UNSET,

) -> Response[Any | Error]:
    """ Get Booking.com content

     Read one kind of content for a Booking.com property, straight from Booking.com.

    | `type` | What it is |
    |---|---|
    | `photos` | The property's photos. Add `room_id` to read one room's gallery. |
    | `facilities` | Property facilities, or a room's with `room_id` (Booking.com's ids — `GET` returns
    them). |
    | `description` | The property description. Booking.com rewrites what you send into its own
    multilingual copy; allow about 3 hours to appear. |
    | `settings` | House rules, pets, children, damage deposit, invoice recipient, booking model. |
    | `policies` | Cancellation and prepayment policies. |
    | `licences` | The region's licence rules and the licence on file. |
    | `checkin_methods` | How guests get in (holiday homes). |
    | `contacts` | Who Booking.com contacts about the property. |

    `amenities` is accepted as another name for `facilities`, and `descriptions` for `description`.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        property_id (str):
        type_ (GetBookingContentType | Unset):  Default: GetBookingContentType.PHOTOS.
        room_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
type_=type_,
room_id=room_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    property_id: str,
    type_: GetBookingContentType | Unset = GetBookingContentType.PHOTOS,
    room_id: str | Unset = UNSET,

) -> Any | Error | None:
    """ Get Booking.com content

     Read one kind of content for a Booking.com property, straight from Booking.com.

    | `type` | What it is |
    |---|---|
    | `photos` | The property's photos. Add `room_id` to read one room's gallery. |
    | `facilities` | Property facilities, or a room's with `room_id` (Booking.com's ids — `GET` returns
    them). |
    | `description` | The property description. Booking.com rewrites what you send into its own
    multilingual copy; allow about 3 hours to appear. |
    | `settings` | House rules, pets, children, damage deposit, invoice recipient, booking model. |
    | `policies` | Cancellation and prepayment policies. |
    | `licences` | The region's licence rules and the licence on file. |
    | `checkin_methods` | How guests get in (holiday homes). |
    | `contacts` | Who Booking.com contacts about the property. |

    `amenities` is accepted as another name for `facilities`, and `descriptions` for `description`.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        property_id (str):
        type_ (GetBookingContentType | Unset):  Default: GetBookingContentType.PHOTOS.
        room_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        client=client,
property_id=property_id,
type_=type_,
room_id=room_id,

    )).parsed
