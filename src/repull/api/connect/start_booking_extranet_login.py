from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.start_booking_extranet_login_body import StartBookingExtranetLoginBody
from ...models.start_booking_extranet_login_response_200 import StartBookingExtranetLoginResponse200
from typing import cast



def _get_kwargs(
    *,
    body: StartBookingExtranetLoginBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/booking-extranet-login/session",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> StartBookingExtranetLoginResponse200 | None:
    if response.status_code == 200:
        response_200 = StartBookingExtranetLoginResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[StartBookingExtranetLoginResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StartBookingExtranetLoginBody,

) -> Response[StartBookingExtranetLoginResponse200]:
    """ Sign in with a Booking.com Extranet user

     Starts the sign-in with the host's Extranet credentials.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (StartBookingExtranetLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartBookingExtranetLoginResponse200]
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
    body: StartBookingExtranetLoginBody,

) -> StartBookingExtranetLoginResponse200 | None:
    """ Sign in with a Booking.com Extranet user

     Starts the sign-in with the host's Extranet credentials.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (StartBookingExtranetLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartBookingExtranetLoginResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: StartBookingExtranetLoginBody,

) -> Response[StartBookingExtranetLoginResponse200]:
    """ Sign in with a Booking.com Extranet user

     Starts the sign-in with the host's Extranet credentials.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (StartBookingExtranetLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StartBookingExtranetLoginResponse200]
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
    body: StartBookingExtranetLoginBody,

) -> StartBookingExtranetLoginResponse200 | None:
    """ Sign in with a Booking.com Extranet user

     Starts the sign-in with the host's Extranet credentials.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (StartBookingExtranetLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StartBookingExtranetLoginResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
