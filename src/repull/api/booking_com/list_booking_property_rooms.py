from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_rooms_rates_response import BookingRoomsRatesResponse
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    hotel_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["hotel_id"] = hotel_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/booking/properties/{id}/rooms".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BookingRoomsRatesResponse | Error | None:
    if response.status_code == 200:
        response_200 = BookingRoomsRatesResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BookingRoomsRatesResponse | Error]:
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
    hotel_id: str | Unset = UNSET,

) -> Response[BookingRoomsRatesResponse | Error]:
    """ List Booking.com rooms + rate-plan ids for a listing

     Return every Booking.com room and its rate plans for a listing, each with the `roomId` / `rateId`
    needed to assemble a restriction write via `PUT /v1/channels/booking/availability`.

    `id` is a **Repull listing id**, not a Booking.com hotel id, despite the `properties` segment —
    resolved to the Booking `hotel_id` through the workspace mapping, read from wherever the Connect
    flow recorded it (`listings_booking_rooms` for anything mapped through `POST
    /v1/connect/booking/map-rooms`). A listing with no active Booking.com mapping returns 404, and the
    message says which id space the path takes. When the listing is published under several properties
    the oldest is used, the rest come back in `otherHotelIds`, and `?hotel_id=` names a different one.
    Sourced from Booking's B.XML roomrates feed, which returns rooms and rate plans together (the rooms-
    unit feed alone omits rate-plan ids). This is the API-key surface for the room/rate ids that were
    previously only reachable inside the hosted Connect room-mapping flow.

    `source` says where the answer came from. `booking` means it was read live just now. If Booking.com
    returns nothing usable for the property, the rooms and rate plans recorded at the last import are
    served instead, `source` is `mirror`, and `mirrorReason` names what went wrong live — the ids are
    Booking.com's own and can be written against, but they can be stale, and `maxPersons`, `policy`,
    `policyId`, `pricingType` and `isChildRate` come back `null` because only the live feed states them.
    `rooms` is empty only when Booking.com and the last import both have nothing; a read that failed is
    an error, never an empty list.

    Each rate plan carries `maxPersons` — the party size that rate plan prices, which is the `occupancy`
    a rate amount must be written at. Each room carries `maxAdults`, Booking.com's capacity for the
    room, which is what a rate write falls back to when the rate plan states no `maxPersons`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingRoomsRatesResponse | Error]
     """


    kwargs = _get_kwargs(
        id=id,
hotel_id=hotel_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    hotel_id: str | Unset = UNSET,

) -> BookingRoomsRatesResponse | Error | None:
    """ List Booking.com rooms + rate-plan ids for a listing

     Return every Booking.com room and its rate plans for a listing, each with the `roomId` / `rateId`
    needed to assemble a restriction write via `PUT /v1/channels/booking/availability`.

    `id` is a **Repull listing id**, not a Booking.com hotel id, despite the `properties` segment —
    resolved to the Booking `hotel_id` through the workspace mapping, read from wherever the Connect
    flow recorded it (`listings_booking_rooms` for anything mapped through `POST
    /v1/connect/booking/map-rooms`). A listing with no active Booking.com mapping returns 404, and the
    message says which id space the path takes. When the listing is published under several properties
    the oldest is used, the rest come back in `otherHotelIds`, and `?hotel_id=` names a different one.
    Sourced from Booking's B.XML roomrates feed, which returns rooms and rate plans together (the rooms-
    unit feed alone omits rate-plan ids). This is the API-key surface for the room/rate ids that were
    previously only reachable inside the hosted Connect room-mapping flow.

    `source` says where the answer came from. `booking` means it was read live just now. If Booking.com
    returns nothing usable for the property, the rooms and rate plans recorded at the last import are
    served instead, `source` is `mirror`, and `mirrorReason` names what went wrong live — the ids are
    Booking.com's own and can be written against, but they can be stale, and `maxPersons`, `policy`,
    `policyId`, `pricingType` and `isChildRate` come back `null` because only the live feed states them.
    `rooms` is empty only when Booking.com and the last import both have nothing; a read that failed is
    an error, never an empty list.

    Each rate plan carries `maxPersons` — the party size that rate plan prices, which is the `occupancy`
    a rate amount must be written at. Each room carries `maxAdults`, Booking.com's capacity for the
    room, which is what a rate write falls back to when the rate plan states no `maxPersons`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingRoomsRatesResponse | Error
     """


    return sync_detailed(
        id=id,
client=client,
hotel_id=hotel_id,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    hotel_id: str | Unset = UNSET,

) -> Response[BookingRoomsRatesResponse | Error]:
    """ List Booking.com rooms + rate-plan ids for a listing

     Return every Booking.com room and its rate plans for a listing, each with the `roomId` / `rateId`
    needed to assemble a restriction write via `PUT /v1/channels/booking/availability`.

    `id` is a **Repull listing id**, not a Booking.com hotel id, despite the `properties` segment —
    resolved to the Booking `hotel_id` through the workspace mapping, read from wherever the Connect
    flow recorded it (`listings_booking_rooms` for anything mapped through `POST
    /v1/connect/booking/map-rooms`). A listing with no active Booking.com mapping returns 404, and the
    message says which id space the path takes. When the listing is published under several properties
    the oldest is used, the rest come back in `otherHotelIds`, and `?hotel_id=` names a different one.
    Sourced from Booking's B.XML roomrates feed, which returns rooms and rate plans together (the rooms-
    unit feed alone omits rate-plan ids). This is the API-key surface for the room/rate ids that were
    previously only reachable inside the hosted Connect room-mapping flow.

    `source` says where the answer came from. `booking` means it was read live just now. If Booking.com
    returns nothing usable for the property, the rooms and rate plans recorded at the last import are
    served instead, `source` is `mirror`, and `mirrorReason` names what went wrong live — the ids are
    Booking.com's own and can be written against, but they can be stale, and `maxPersons`, `policy`,
    `policyId`, `pricingType` and `isChildRate` come back `null` because only the live feed states them.
    `rooms` is empty only when Booking.com and the last import both have nothing; a read that failed is
    an error, never an empty list.

    Each rate plan carries `maxPersons` — the party size that rate plan prices, which is the `occupancy`
    a rate amount must be written at. Each room carries `maxAdults`, Booking.com's capacity for the
    room, which is what a rate write falls back to when the rate plan states no `maxPersons`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BookingRoomsRatesResponse | Error]
     """


    kwargs = _get_kwargs(
        id=id,
hotel_id=hotel_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    hotel_id: str | Unset = UNSET,

) -> BookingRoomsRatesResponse | Error | None:
    """ List Booking.com rooms + rate-plan ids for a listing

     Return every Booking.com room and its rate plans for a listing, each with the `roomId` / `rateId`
    needed to assemble a restriction write via `PUT /v1/channels/booking/availability`.

    `id` is a **Repull listing id**, not a Booking.com hotel id, despite the `properties` segment —
    resolved to the Booking `hotel_id` through the workspace mapping, read from wherever the Connect
    flow recorded it (`listings_booking_rooms` for anything mapped through `POST
    /v1/connect/booking/map-rooms`). A listing with no active Booking.com mapping returns 404, and the
    message says which id space the path takes. When the listing is published under several properties
    the oldest is used, the rest come back in `otherHotelIds`, and `?hotel_id=` names a different one.
    Sourced from Booking's B.XML roomrates feed, which returns rooms and rate plans together (the rooms-
    unit feed alone omits rate-plan ids). This is the API-key surface for the room/rate ids that were
    previously only reachable inside the hosted Connect room-mapping flow.

    `source` says where the answer came from. `booking` means it was read live just now. If Booking.com
    returns nothing usable for the property, the rooms and rate plans recorded at the last import are
    served instead, `source` is `mirror`, and `mirrorReason` names what went wrong live — the ids are
    Booking.com's own and can be written against, but they can be stale, and `maxPersons`, `policy`,
    `policyId`, `pricingType` and `isChildRate` come back `null` because only the live feed states them.
    `rooms` is empty only when Booking.com and the last import both have nothing; a read that failed is
    an error, never an empty list.

    Each rate plan carries `maxPersons` — the party size that rate plan prices, which is the `occupancy`
    a rate amount must be written at. Each room carries `maxAdults`, Booking.com's capacity for the
    room, which is what a rate write falls back to when the rate plan states no `maxPersons`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BookingRoomsRatesResponse | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
hotel_id=hotel_id,

    )).parsed
