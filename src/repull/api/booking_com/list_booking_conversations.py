from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_conversation import BookingConversation
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/booking/messaging",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[BookingConversation] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_booking_conversation_list_response_item_data in (_response_200):
            componentsschemas_booking_conversation_list_response_item = BookingConversation.from_dict(componentsschemas_booking_conversation_list_response_item_data)



            response_200.append(componentsschemas_booking_conversation_list_response_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[BookingConversation]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[BookingConversation]]:
    """ List Booking.com conversations

     List Booking.com guest conversations. Cursor-paginated. Use the messaging POST to send a reply.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BookingConversation]]
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

) -> list[BookingConversation] | None:
    """ List Booking.com conversations

     List Booking.com guest conversations. Cursor-paginated. Use the messaging POST to send a reply.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BookingConversation]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[BookingConversation]]:
    """ List Booking.com conversations

     List Booking.com guest conversations. Cursor-paginated. Use the messaging POST to send a reply.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[BookingConversation]]
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

) -> list[BookingConversation] | None:
    """ List Booking.com conversations

     List Booking.com guest conversations. Cursor-paginated. Use the messaging POST to send a reply.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[BookingConversation]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
