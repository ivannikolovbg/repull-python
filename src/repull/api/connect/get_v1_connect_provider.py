from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connect_status import ConnectStatus
from typing import cast



def _get_kwargs(
    provider: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connect/{provider}".format(provider=quote(str(provider), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConnectStatus | None:
    if response.status_code == 200:
        response_200 = ConnectStatus.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConnectStatus]:
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

) -> Response[ConnectStatus]:
    """ Get connection status

     Returns the current connection status for a provider, including host metadata (display name +
    avatar) for Airbnb so clients can render an account-level confirmation UI.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectStatus]
     """


    kwargs = _get_kwargs(
        provider=provider,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    provider: str,
    *,
    client: AuthenticatedClient | Client,

) -> ConnectStatus | None:
    """ Get connection status

     Returns the current connection status for a provider, including host metadata (display name +
    avatar) for Airbnb so clients can render an account-level confirmation UI.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectStatus
     """


    return sync_detailed(
        provider=provider,
client=client,

    ).parsed

async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[ConnectStatus]:
    """ Get connection status

     Returns the current connection status for a provider, including host metadata (display name +
    avatar) for Airbnb so clients can render an account-level confirmation UI.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectStatus]
     """


    kwargs = _get_kwargs(
        provider=provider,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    provider: str,
    *,
    client: AuthenticatedClient | Client,

) -> ConnectStatus | None:
    """ Get connection status

     Returns the current connection status for a provider, including host metadata (display name +
    avatar) for Airbnb so clients can render an account-level confirmation UI.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectStatus
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,

    )).parsed
