from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.tiket_connect_rooms_response import TiketConnectRoomsResponse
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
        "url": "/v1/connect/tiket/rooms",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TiketConnectRoomsResponse | None:
    if response.status_code == 200:
        response_200 = TiketConnectRoomsResponse.from_dict(response.json())



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

    if response.status_code == 425:
        response_425 = Error.from_dict(response.json())



        return response_425

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | TiketConnectRoomsResponse]:
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

) -> Response[Error | TiketConnectRoomsResponse]:
    r""" List the room types of the tiket.com property in a Connect session

     Called by the hosted Connect page and authorized by the Connect session id, not an API key. Start
    the session with `POST /v1/connect` (`allowedProviders: [\"tiket\"]`) and send the host to its
    `url`.

    The room types of the property claimed in the session, for the mapping screen. Same shape as `GET
    /v1/connect/booking/rooms`. `425 not_ready` means the claim is still being saved; retry in a moment.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketConnectRoomsResponse]
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

) -> Error | TiketConnectRoomsResponse | None:
    r""" List the room types of the tiket.com property in a Connect session

     Called by the hosted Connect page and authorized by the Connect session id, not an API key. Start
    the session with `POST /v1/connect` (`allowedProviders: [\"tiket\"]`) and send the host to its
    `url`.

    The room types of the property claimed in the session, for the mapping screen. Same shape as `GET
    /v1/connect/booking/rooms`. `425 not_ready` means the claim is still being saved; retry in a moment.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketConnectRoomsResponse
     """


    return sync_detailed(
        client=client,
session_id=session_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    session_id: str,

) -> Response[Error | TiketConnectRoomsResponse]:
    r""" List the room types of the tiket.com property in a Connect session

     Called by the hosted Connect page and authorized by the Connect session id, not an API key. Start
    the session with `POST /v1/connect` (`allowedProviders: [\"tiket\"]`) and send the host to its
    `url`.

    The room types of the property claimed in the session, for the mapping screen. Same shape as `GET
    /v1/connect/booking/rooms`. `425 not_ready` means the claim is still being saved; retry in a moment.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketConnectRoomsResponse]
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

) -> Error | TiketConnectRoomsResponse | None:
    r""" List the room types of the tiket.com property in a Connect session

     Called by the hosted Connect page and authorized by the Connect session id, not an API key. Start
    the session with `POST /v1/connect` (`allowedProviders: [\"tiket\"]`) and send the host to its
    `url`.

    The room types of the property claimed in the session, for the mapping screen. Same shape as `GET
    /v1/connect/booking/rooms`. `425 not_ready` means the claim is still being saved; retry in a moment.

    Args:
        session_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketConnectRoomsResponse
     """


    return (await asyncio_detailed(
        client=client,
session_id=session_id,

    )).parsed
