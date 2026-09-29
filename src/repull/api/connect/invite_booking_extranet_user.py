from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.invite_booking_extranet_user_body import InviteBookingExtranetUserBody
from ...models.invite_booking_extranet_user_response_200 import InviteBookingExtranetUserResponse200
from typing import cast



def _get_kwargs(
    *,
    body: InviteBookingExtranetUserBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/booking-extranet-login/invite",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> InviteBookingExtranetUserResponse200 | None:
    if response.status_code == 200:
        response_200 = InviteBookingExtranetUserResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[InviteBookingExtranetUserResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InviteBookingExtranetUserBody,

) -> Response[InviteBookingExtranetUserResponse200]:
    """ Connect Booking.com by inviting a user

     Generates the user the host invites in their Extranet; progress is read from the status route.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (InviteBookingExtranetUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InviteBookingExtranetUserResponse200]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: InviteBookingExtranetUserBody,

) -> InviteBookingExtranetUserResponse200 | None:
    """ Connect Booking.com by inviting a user

     Generates the user the host invites in their Extranet; progress is read from the status route.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (InviteBookingExtranetUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InviteBookingExtranetUserResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: InviteBookingExtranetUserBody,

) -> Response[InviteBookingExtranetUserResponse200]:
    """ Connect Booking.com by inviting a user

     Generates the user the host invites in their Extranet; progress is read from the status route.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (InviteBookingExtranetUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[InviteBookingExtranetUserResponse200]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: InviteBookingExtranetUserBody,

) -> InviteBookingExtranetUserResponse200 | None:
    """ Connect Booking.com by inviting a user

     Generates the user the host invites in their Extranet; progress is read from the status route.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (InviteBookingExtranetUserBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        InviteBookingExtranetUserResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
