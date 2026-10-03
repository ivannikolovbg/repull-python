from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.resume_connect_response_400 import ResumeConnectResponse400
from ...models.resume_connect_response_500 import ResumeConnectResponse500
from typing import cast



def _get_kwargs(
    *,
    t: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["t"] = t


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connect/resume",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ResumeConnectResponse400 | ResumeConnectResponse500 | None:
    if response.status_code == 302:
        response_302 = cast(Any, None)
        return response_302

    if response.status_code == 400:
        response_400 = ResumeConnectResponse400.from_dict(response.json())



        return response_400

    if response.status_code == 500:
        response_500 = ResumeConnectResponse500.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ResumeConnectResponse400 | ResumeConnectResponse500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    t: str,

) -> Response[Any | ResumeConnectResponse400 | ResumeConnectResponse500]:
    """ Open a connection's fix link

     The target of a connection's `fixUrl`. Open it in the host's browser to send them back into Connect
    for an EXISTING connection — for example to grant the Booking.com extranet user full access after a
    `needs_permissions` state, or to reconnect a Smoobu account that still uses a legacy single API key
    with an API key + secret.

    Each open starts a fresh, short-lived Connect session bound to that connection and redirects (302)
    to the hosted Connect page, which shows the connection's current state. The link itself does not
    expire on its own schedule — store `fixUrl` and open it whenever the connection needs attention.

    No API key — the signed `t` token is the capability. Supported for Booking.com extranet login and
    Smoobu connections.

    Args:
        t (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ResumeConnectResponse400 | ResumeConnectResponse500]
     """


    kwargs = _get_kwargs(
        t=t,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    t: str,

) -> Any | ResumeConnectResponse400 | ResumeConnectResponse500 | None:
    """ Open a connection's fix link

     The target of a connection's `fixUrl`. Open it in the host's browser to send them back into Connect
    for an EXISTING connection — for example to grant the Booking.com extranet user full access after a
    `needs_permissions` state, or to reconnect a Smoobu account that still uses a legacy single API key
    with an API key + secret.

    Each open starts a fresh, short-lived Connect session bound to that connection and redirects (302)
    to the hosted Connect page, which shows the connection's current state. The link itself does not
    expire on its own schedule — store `fixUrl` and open it whenever the connection needs attention.

    No API key — the signed `t` token is the capability. Supported for Booking.com extranet login and
    Smoobu connections.

    Args:
        t (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ResumeConnectResponse400 | ResumeConnectResponse500
     """


    return sync_detailed(
        client=client,
t=t,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    t: str,

) -> Response[Any | ResumeConnectResponse400 | ResumeConnectResponse500]:
    """ Open a connection's fix link

     The target of a connection's `fixUrl`. Open it in the host's browser to send them back into Connect
    for an EXISTING connection — for example to grant the Booking.com extranet user full access after a
    `needs_permissions` state, or to reconnect a Smoobu account that still uses a legacy single API key
    with an API key + secret.

    Each open starts a fresh, short-lived Connect session bound to that connection and redirects (302)
    to the hosted Connect page, which shows the connection's current state. The link itself does not
    expire on its own schedule — store `fixUrl` and open it whenever the connection needs attention.

    No API key — the signed `t` token is the capability. Supported for Booking.com extranet login and
    Smoobu connections.

    Args:
        t (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ResumeConnectResponse400 | ResumeConnectResponse500]
     """


    kwargs = _get_kwargs(
        t=t,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    t: str,

) -> Any | ResumeConnectResponse400 | ResumeConnectResponse500 | None:
    """ Open a connection's fix link

     The target of a connection's `fixUrl`. Open it in the host's browser to send them back into Connect
    for an EXISTING connection — for example to grant the Booking.com extranet user full access after a
    `needs_permissions` state, or to reconnect a Smoobu account that still uses a legacy single API key
    with an API key + secret.

    Each open starts a fresh, short-lived Connect session bound to that connection and redirects (302)
    to the hosted Connect page, which shows the connection's current state. The link itself does not
    expire on its own schedule — store `fixUrl` and open it whenever the connection needs attention.

    No API key — the signed `t` token is the capability. Supported for Booking.com extranet login and
    Smoobu connections.

    Args:
        t (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ResumeConnectResponse400 | ResumeConnectResponse500
     """


    return (await asyncio_detailed(
        client=client,
t=t,

    )).parsed
