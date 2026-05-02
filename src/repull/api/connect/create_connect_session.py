from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connect_session import ConnectSession
from ...models.create_connect_session_body import CreateConnectSessionBody
from typing import cast



def _get_kwargs(
    *,
    body: CreateConnectSessionBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConnectSession | None:
    if response.status_code == 201:
        response_201 = ConnectSession.from_dict(response.json())



        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConnectSession]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateConnectSessionBody,

) -> Response[ConnectSession]:
    """ Create a multi-channel Connect picker session

     Mints a session that lands the user on the channel picker at `connect.repull.dev/{sessionId}`
    instead of jumping straight to a single provider. The user picks a channel from the registry, the
    picker page POSTs `selectConnectProvider` to bind the choice, and the per-provider flow takes over.

    Use this when you want one entry point for all 13 channels. Use `POST /v1/connect/{provider}`
    instead when your UI already knows which channel to connect.

    Args:
        body (CreateConnectSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectSession]
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
    body: CreateConnectSessionBody,

) -> ConnectSession | None:
    """ Create a multi-channel Connect picker session

     Mints a session that lands the user on the channel picker at `connect.repull.dev/{sessionId}`
    instead of jumping straight to a single provider. The user picks a channel from the registry, the
    picker page POSTs `selectConnectProvider` to bind the choice, and the per-provider flow takes over.

    Use this when you want one entry point for all 13 channels. Use `POST /v1/connect/{provider}`
    instead when your UI already knows which channel to connect.

    Args:
        body (CreateConnectSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectSession
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateConnectSessionBody,

) -> Response[ConnectSession]:
    """ Create a multi-channel Connect picker session

     Mints a session that lands the user on the channel picker at `connect.repull.dev/{sessionId}`
    instead of jumping straight to a single provider. The user picks a channel from the registry, the
    picker page POSTs `selectConnectProvider` to bind the choice, and the per-provider flow takes over.

    Use this when you want one entry point for all 13 channels. Use `POST /v1/connect/{provider}`
    instead when your UI already knows which channel to connect.

    Args:
        body (CreateConnectSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectSession]
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
    body: CreateConnectSessionBody,

) -> ConnectSession | None:
    """ Create a multi-channel Connect picker session

     Mints a session that lands the user on the channel picker at `connect.repull.dev/{sessionId}`
    instead of jumping straight to a single provider. The user picks a channel from the registry, the
    picker page POSTs `selectConnectProvider` to bind the choice, and the per-provider flow takes over.

    Use this when you want one entry point for all 13 channels. Use `POST /v1/connect/{provider}`
    instead when your UI already knows which channel to connect.

    Args:
        body (CreateConnectSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectSession
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
