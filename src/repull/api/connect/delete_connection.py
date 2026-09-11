from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from typing import cast



def _get_kwargs(
    provider: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/connect/{provider}".format(provider=quote(str(provider), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 501:
        response_501 = Error.from_dict(response.json())



        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
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

) -> Response[Any | Error]:
    """ Disconnect provider

     Disconnect a PMS or OTA from this workspace.

    Currently supported for `booking` only: drops the stored connection and stops syncing the mapped
    rooms. Resources already synced remain queryable but become read-only and stop receiving updates.

    Every other provider returns `501 not_implemented` with instructions for disconnecting on the
    provider's side — Airbnb in particular has to be revoked by the host (Account → Privacy & sharing →
    Connected apps), because the OAuth grant lives outside this service. The endpoint used to report
    `200 { disconnected: true }` for every provider while doing nothing; it now tells you the truth.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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

) -> Any | Error | None:
    """ Disconnect provider

     Disconnect a PMS or OTA from this workspace.

    Currently supported for `booking` only: drops the stored connection and stops syncing the mapped
    rooms. Resources already synced remain queryable but become read-only and stop receiving updates.

    Every other provider returns `501 not_implemented` with instructions for disconnecting on the
    provider's side — Airbnb in particular has to be revoked by the host (Account → Privacy & sharing →
    Connected apps), because the OAuth grant lives outside this service. The endpoint used to report
    `200 { disconnected: true }` for every provider while doing nothing; it now tells you the truth.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        provider=provider,
client=client,

    ).parsed

async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Any | Error]:
    """ Disconnect provider

     Disconnect a PMS or OTA from this workspace.

    Currently supported for `booking` only: drops the stored connection and stops syncing the mapped
    rooms. Resources already synced remain queryable but become read-only and stop receiving updates.

    Every other provider returns `501 not_implemented` with instructions for disconnecting on the
    provider's side — Airbnb in particular has to be revoked by the host (Account → Privacy & sharing →
    Connected apps), because the OAuth grant lives outside this service. The endpoint used to report
    `200 { disconnected: true }` for every provider while doing nothing; it now tells you the truth.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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

) -> Any | Error | None:
    """ Disconnect provider

     Disconnect a PMS or OTA from this workspace.

    Currently supported for `booking` only: drops the stored connection and stops syncing the mapped
    rooms. Resources already synced remain queryable but become read-only and stop receiving updates.

    Every other provider returns `501 not_implemented` with instructions for disconnecting on the
    provider's side — Airbnb in particular has to be revoked by the host (Account → Privacy & sharing →
    Connected apps), because the OAuth grant lives outside this service. The endpoint used to report
    `200 { disconnected: true }` for every provider while doing nothing; it now tells you the truth.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,

    )).parsed
