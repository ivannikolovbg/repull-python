from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_conversation import BookingConversation
from ...models.error import Error
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/booking/messaging",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | list[BookingConversation] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_booking_conversation_list_response_item_data in (_response_200):
            componentsschemas_booking_conversation_list_response_item = BookingConversation.from_dict(componentsschemas_booking_conversation_list_response_item_data)



            response_200.append(componentsschemas_booking_conversation_list_response_item)

        return response_200

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | list[BookingConversation]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | list[BookingConversation]]:
    """ List Booking.com conversations

     List Booking.com guest conversations. Cursor-paginated. Use the messaging POST to send a reply.

    Scoped to this workspace. With `property_id`, the property must be connected to this workspace — any
    other id returns `404 not_found`. Without it, only messages for this workspace's own Booking.com
    properties are returned.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[BookingConversation]]
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

) -> Error | list[BookingConversation] | None:
    """ List Booking.com conversations

     List Booking.com guest conversations. Cursor-paginated. Use the messaging POST to send a reply.

    Scoped to this workspace. With `property_id`, the property must be connected to this workspace — any
    other id returns `404 not_found`. Without it, only messages for this workspace's own Booking.com
    properties are returned.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[BookingConversation]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | list[BookingConversation]]:
    """ List Booking.com conversations

     List Booking.com guest conversations. Cursor-paginated. Use the messaging POST to send a reply.

    Scoped to this workspace. With `property_id`, the property must be connected to this workspace — any
    other id returns `404 not_found`. Without it, only messages for this workspace's own Booking.com
    properties are returned.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | list[BookingConversation]]
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

) -> Error | list[BookingConversation] | None:
    """ List Booking.com conversations

     List Booking.com guest conversations. Cursor-paginated. Use the messaging POST to send a reply.

    Scoped to this workspace. With `property_id`, the property must be connected to this workspace — any
    other id returns `404 not_found`. Without it, only messages for this workspace's own Booking.com
    properties are returned.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | list[BookingConversation]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
