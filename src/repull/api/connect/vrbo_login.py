from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.vrbo_login_body import VrboLoginBody
from ...models.vrbo_login_response_200 import VrboLoginResponse200
from typing import cast



def _get_kwargs(
    *,
    body: VrboLoginBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/vrbo-login/session",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> VrboLoginResponse200 | None:
    if response.status_code == 200:
        response_200 = VrboLoginResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[VrboLoginResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VrboLoginBody,

) -> Response[VrboLoginResponse200]:
    """ Sign in with a Vrbo host account

     `action: login` checks the email and password and answers in seconds: `connected`, `otp_required`
    (Vrbo sent a code to `destination`) or `failed` with a `reason` (`bad_credentials`, `blocked`, …).
    `action: otp` submits the code; a refused code comes back as `otp_required` with `reason: bad_code`.

    Signing in imports nothing. `accessType` (`full_access` or `messaging`, when the session did not
    lock it) is the host's choice of whether mapped listings push the calendar. The import starts when
    the mapping is confirmed.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (VrboLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VrboLoginResponse200]
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
    body: VrboLoginBody,

) -> VrboLoginResponse200 | None:
    """ Sign in with a Vrbo host account

     `action: login` checks the email and password and answers in seconds: `connected`, `otp_required`
    (Vrbo sent a code to `destination`) or `failed` with a `reason` (`bad_credentials`, `blocked`, …).
    `action: otp` submits the code; a refused code comes back as `otp_required` with `reason: bad_code`.

    Signing in imports nothing. `accessType` (`full_access` or `messaging`, when the session did not
    lock it) is the host's choice of whether mapped listings push the calendar. The import starts when
    the mapping is confirmed.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (VrboLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VrboLoginResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VrboLoginBody,

) -> Response[VrboLoginResponse200]:
    """ Sign in with a Vrbo host account

     `action: login` checks the email and password and answers in seconds: `connected`, `otp_required`
    (Vrbo sent a code to `destination`) or `failed` with a `reason` (`bad_credentials`, `blocked`, …).
    `action: otp` submits the code; a refused code comes back as `otp_required` with `reason: bad_code`.

    Signing in imports nothing. `accessType` (`full_access` or `messaging`, when the session did not
    lock it) is the host's choice of whether mapped listings push the calendar. The import starts when
    the mapping is confirmed.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (VrboLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VrboLoginResponse200]
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
    body: VrboLoginBody,

) -> VrboLoginResponse200 | None:
    """ Sign in with a Vrbo host account

     `action: login` checks the email and password and answers in seconds: `connected`, `otp_required`
    (Vrbo sent a code to `destination`) or `failed` with a `reason` (`bad_credentials`, `blocked`, …).
    `action: otp` submits the code; a refused code comes back as `otp_required` with `reason: bad_code`.

    Signing in imports nothing. `accessType` (`full_access` or `messaging`, when the session did not
    lock it) is the host's choice of whether mapped listings push the calendar. The import starts when
    the mapping is confirmed.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        body (VrboLoginBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VrboLoginResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
