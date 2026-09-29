from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.vrbo_import_status import VrboImportStatus
from typing import cast



def _get_kwargs(
    *,
    session_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["sessionId"] = session_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connect/vrbo-login/session",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> VrboImportStatus | None:
    if response.status_code == 200:
        response_200 = VrboImportStatus.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[VrboImportStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    session_id: str,

) -> Response[VrboImportStatus]:
    """ Import progress of the session's Vrbo account

     After the mapping is confirmed: `importing` (upcoming bookings and the last 30 days of messages) →
    `importing_history` (the rest of the account, in the background) → `imported`.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VrboImportStatus]
     """


    kwargs = _get_kwargs(
        session_id=session_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    session_id: str,

) -> VrboImportStatus | None:
    """ Import progress of the session's Vrbo account

     After the mapping is confirmed: `importing` (upcoming bookings and the last 30 days of messages) →
    `importing_history` (the rest of the account, in the background) → `imported`.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VrboImportStatus
     """


    return sync_detailed(
        client=client,
session_id=session_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    session_id: str,

) -> Response[VrboImportStatus]:
    """ Import progress of the session's Vrbo account

     After the mapping is confirmed: `importing` (upcoming bookings and the last 30 days of messages) →
    `importing_history` (the rest of the account, in the background) → `imported`.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VrboImportStatus]
     """


    kwargs = _get_kwargs(
        session_id=session_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    session_id: str,

) -> VrboImportStatus | None:
    """ Import progress of the session's Vrbo account

     After the mapping is confirmed: `importing` (upcoming bookings and the last 30 days of messages) →
    `importing_history` (the rest of the account, in the background) → `imported`.

    Called by the hosted Connect page. No API key — the session ID is the capability token.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VrboImportStatus
     """


    return (await asyncio_detailed(
        client=client,
session_id=session_id,

    )).parsed
