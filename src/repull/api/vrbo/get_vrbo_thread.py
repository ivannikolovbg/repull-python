from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_vrbo_thread_response_200 import GetVrboThreadResponse200
from typing import cast



def _get_kwargs(
    thread_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/vrbo/messaging/{thread_id}".format(thread_id=quote(str(thread_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetVrboThreadResponse200 | None:
    if response.status_code == 200:
        response_200 = GetVrboThreadResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetVrboThreadResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetVrboThreadResponse200]:
    """ Get a Vrbo message thread

     One Vrbo conversation by its Vrbo id — the counterpart of `GET
    /v1/channels/airbnb/messaging/{threadId}`.

    Returns `403 listing_inactive` when the conversation's listing is inactive.

    Args:
        thread_id (str):  Example: vrbo:3f2a9c1e-5b7d-4e2a-9c1f-0a1b2c3d4e5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboThreadResponse200]
     """


    kwargs = _get_kwargs(
        thread_id=thread_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetVrboThreadResponse200 | None:
    """ Get a Vrbo message thread

     One Vrbo conversation by its Vrbo id — the counterpart of `GET
    /v1/channels/airbnb/messaging/{threadId}`.

    Returns `403 listing_inactive` when the conversation's listing is inactive.

    Args:
        thread_id (str):  Example: vrbo:3f2a9c1e-5b7d-4e2a-9c1f-0a1b2c3d4e5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboThreadResponse200
     """


    return sync_detailed(
        thread_id=thread_id,
client=client,

    ).parsed

async def asyncio_detailed(
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetVrboThreadResponse200]:
    """ Get a Vrbo message thread

     One Vrbo conversation by its Vrbo id — the counterpart of `GET
    /v1/channels/airbnb/messaging/{threadId}`.

    Returns `403 listing_inactive` when the conversation's listing is inactive.

    Args:
        thread_id (str):  Example: vrbo:3f2a9c1e-5b7d-4e2a-9c1f-0a1b2c3d4e5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboThreadResponse200]
     """


    kwargs = _get_kwargs(
        thread_id=thread_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetVrboThreadResponse200 | None:
    """ Get a Vrbo message thread

     One Vrbo conversation by its Vrbo id — the counterpart of `GET
    /v1/channels/airbnb/messaging/{threadId}`.

    Returns `403 listing_inactive` when the conversation's listing is inactive.

    Args:
        thread_id (str):  Example: vrbo:3f2a9c1e-5b7d-4e2a-9c1f-0a1b2c3d4e5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboThreadResponse200
     """


    return (await asyncio_detailed(
        thread_id=thread_id,
client=client,

    )).parsed
