from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_property import BookingProperty
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/booking/properties",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[BookingProperty] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_booking_property_list_response_item_data in (_response_200):
            componentsschemas_booking_property_list_response_item = BookingProperty.from_dict(componentsschemas_booking_property_list_response_item_data)



            response_200.append(componentsschemas_booking_property_list_response_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[BookingProperty]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[BookingProperty]]:
    r""" List Booking.com properties

     List every Booking.com property this workspace holds. Each property is returned ONCE, with the
    Repull listings mapped under it.

    A Booking.com property is a building; its rooms are what guests book, and each room is mapped to one
    Repull listing — so one property routinely carries many listings. `listings[].roomBookingId` is the
    Booking.com room id an ARI write takes.

    A property whose rooms are not mapped yet is still listed, with `mappingStatus: \"unmapped\"` and an
    empty `listings` array. That is a real mid-onboarding state, not an error: finish `POST
    /v1/connect/booking/map-rooms` and the listings appear. Such a property used to be dropped silently,
    which made a mapped-but-unreadable workspace indistinguishable from one with no Booking connection
    at all.

    Inactive listings are left out of `listings`; they keep syncing and reappear once activated. Use
    `GET /v1/listings?status=inactive` to find them.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BookingProperty]]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> list[BookingProperty] | None:
    r""" List Booking.com properties

     List every Booking.com property this workspace holds. Each property is returned ONCE, with the
    Repull listings mapped under it.

    A Booking.com property is a building; its rooms are what guests book, and each room is mapped to one
    Repull listing — so one property routinely carries many listings. `listings[].roomBookingId` is the
    Booking.com room id an ARI write takes.

    A property whose rooms are not mapped yet is still listed, with `mappingStatus: \"unmapped\"` and an
    empty `listings` array. That is a real mid-onboarding state, not an error: finish `POST
    /v1/connect/booking/map-rooms` and the listings appear. Such a property used to be dropped silently,
    which made a mapped-but-unreadable workspace indistinguishable from one with no Booking connection
    at all.

    Inactive listings are left out of `listings`; they keep syncing and reappear once activated. Use
    `GET /v1/listings?status=inactive` to find them.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BookingProperty]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[BookingProperty]]:
    r""" List Booking.com properties

     List every Booking.com property this workspace holds. Each property is returned ONCE, with the
    Repull listings mapped under it.

    A Booking.com property is a building; its rooms are what guests book, and each room is mapped to one
    Repull listing — so one property routinely carries many listings. `listings[].roomBookingId` is the
    Booking.com room id an ARI write takes.

    A property whose rooms are not mapped yet is still listed, with `mappingStatus: \"unmapped\"` and an
    empty `listings` array. That is a real mid-onboarding state, not an error: finish `POST
    /v1/connect/booking/map-rooms` and the listings appear. Such a property used to be dropped silently,
    which made a mapped-but-unreadable workspace indistinguishable from one with no Booking connection
    at all.

    Inactive listings are left out of `listings`; they keep syncing and reappear once activated. Use
    `GET /v1/listings?status=inactive` to find them.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BookingProperty]]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> list[BookingProperty] | None:
    r""" List Booking.com properties

     List every Booking.com property this workspace holds. Each property is returned ONCE, with the
    Repull listings mapped under it.

    A Booking.com property is a building; its rooms are what guests book, and each room is mapped to one
    Repull listing — so one property routinely carries many listings. `listings[].roomBookingId` is the
    Booking.com room id an ARI write takes.

    A property whose rooms are not mapped yet is still listed, with `mappingStatus: \"unmapped\"` and an
    empty `listings` array. That is a real mid-onboarding state, not an error: finish `POST
    /v1/connect/booking/map-rooms` and the listings appear. Such a property used to be dropped silently,
    which made a mapped-but-unreadable workspace indistinguishable from one with no Booking connection
    at all.

    Inactive listings are left out of `listings`; they keep syncing and reappear once activated. Use
    `GET /v1/listings?status=inactive` to find them.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BookingProperty]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
