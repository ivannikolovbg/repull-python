from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connection import Connection
from ...models.create_connection_body import CreateConnectionBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    provider: str,
    *,
    body: CreateConnectionBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/{provider}".format(provider=quote(str(provider), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Connection | None:
    if response.status_code == 200:
        response_200 = Connection.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Connection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateConnectionBody | Unset = UNSET,

) -> Response[Connection]:
    """ Connect to PMS/OTA provider

     Establish a connection to a PMS or OTA platform. Credentials vary by provider — see docs for each
    provider.

    Airbnb-specific: pass `redirectUrl` (where to send the user after consent) and optionally
    `accessType` (`read_only` for calendar-only OAuth scopes, or `full_access` — the default — for full
    host scopes). The response returns a hosted `oauthUrl` to redirect the user to.

    Args:
        provider (str):
        body (CreateConnectionBody | Unset): Provider-specific credentials (apiKey,
            clientId/clientSecret, etc.) or OAuth init params for Airbnb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Connection]
     """


    kwargs = _get_kwargs(
        provider=provider,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateConnectionBody | Unset = UNSET,

) -> Connection | None:
    """ Connect to PMS/OTA provider

     Establish a connection to a PMS or OTA platform. Credentials vary by provider — see docs for each
    provider.

    Airbnb-specific: pass `redirectUrl` (where to send the user after consent) and optionally
    `accessType` (`read_only` for calendar-only OAuth scopes, or `full_access` — the default — for full
    host scopes). The response returns a hosted `oauthUrl` to redirect the user to.

    Args:
        provider (str):
        body (CreateConnectionBody | Unset): Provider-specific credentials (apiKey,
            clientId/clientSecret, etc.) or OAuth init params for Airbnb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Connection
     """


    return sync_detailed(
        provider=provider,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateConnectionBody | Unset = UNSET,

) -> Response[Connection]:
    """ Connect to PMS/OTA provider

     Establish a connection to a PMS or OTA platform. Credentials vary by provider — see docs for each
    provider.

    Airbnb-specific: pass `redirectUrl` (where to send the user after consent) and optionally
    `accessType` (`read_only` for calendar-only OAuth scopes, or `full_access` — the default — for full
    host scopes). The response returns a hosted `oauthUrl` to redirect the user to.

    Args:
        provider (str):
        body (CreateConnectionBody | Unset): Provider-specific credentials (apiKey,
            clientId/clientSecret, etc.) or OAuth init params for Airbnb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Connection]
     """


    kwargs = _get_kwargs(
        provider=provider,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateConnectionBody | Unset = UNSET,

) -> Connection | None:
    """ Connect to PMS/OTA provider

     Establish a connection to a PMS or OTA platform. Credentials vary by provider — see docs for each
    provider.

    Airbnb-specific: pass `redirectUrl` (where to send the user after consent) and optionally
    `accessType` (`read_only` for calendar-only OAuth scopes, or `full_access` — the default — for full
    host scopes). The response returns a hosted `oauthUrl` to redirect the user to.

    Args:
        provider (str):
        body (CreateConnectionBody | Unset): Provider-specific credentials (apiKey,
            clientId/clientSecret, etc.) or OAuth init params for Airbnb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Connection
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,
body=body,

    )).parsed
