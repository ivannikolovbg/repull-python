from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.recheck_booking_extranet_login_body import RecheckBookingExtranetLoginBody
from ...models.recheck_booking_extranet_login_response_200 import RecheckBookingExtranetLoginResponse200
from typing import cast



def _get_kwargs(
    *,
    body: RecheckBookingExtranetLoginBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/booking-extranet-login/recheck",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | RecheckBookingExtranetLoginResponse200 | None:
    if response.status_code == 200:
        response_200 = RecheckBookingExtranetLoginResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 410:
        response_410 = Error.from_dict(response.json())



        return response_410

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | RecheckBookingExtranetLoginResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecheckBookingExtranetLoginBody,

) -> Response[Error | RecheckBookingExtranetLoginResponse200]:
    """ Re-check Booking.com direct-login permissions

     Re-runs the account import for a Booking.com direct-login connection after the host has granted the
    invited user full access in the Booking.com extranet (the `needs_permissions` state). Permissions
    are probed again and, once full access is in place, the connection continues to property details and
    room mapping — no new invitation is sent. Poll `GET /v1/connect/booking-extranet-login/status` for
    the result.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (RecheckBookingExtranetLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RecheckBookingExtranetLoginResponse200]
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
    body: RecheckBookingExtranetLoginBody,

) -> Error | RecheckBookingExtranetLoginResponse200 | None:
    """ Re-check Booking.com direct-login permissions

     Re-runs the account import for a Booking.com direct-login connection after the host has granted the
    invited user full access in the Booking.com extranet (the `needs_permissions` state). Permissions
    are probed again and, once full access is in place, the connection continues to property details and
    room mapping — no new invitation is sent. Poll `GET /v1/connect/booking-extranet-login/status` for
    the result.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (RecheckBookingExtranetLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RecheckBookingExtranetLoginResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RecheckBookingExtranetLoginBody,

) -> Response[Error | RecheckBookingExtranetLoginResponse200]:
    """ Re-check Booking.com direct-login permissions

     Re-runs the account import for a Booking.com direct-login connection after the host has granted the
    invited user full access in the Booking.com extranet (the `needs_permissions` state). Permissions
    are probed again and, once full access is in place, the connection continues to property details and
    room mapping — no new invitation is sent. Poll `GET /v1/connect/booking-extranet-login/status` for
    the result.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (RecheckBookingExtranetLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RecheckBookingExtranetLoginResponse200]
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
    body: RecheckBookingExtranetLoginBody,

) -> Error | RecheckBookingExtranetLoginResponse200 | None:
    """ Re-check Booking.com direct-login permissions

     Re-runs the account import for a Booking.com direct-login connection after the host has granted the
    invited user full access in the Booking.com extranet (the `needs_permissions` state). Permissions
    are probed again and, once full access is in place, the connection continues to property details and
    room mapping — no new invitation is sent. Poll `GET /v1/connect/booking-extranet-login/status` for
    the result.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (RecheckBookingExtranetLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RecheckBookingExtranetLoginResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
