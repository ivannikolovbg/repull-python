from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_kv_response_200 import GetKvResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    key: str,
    *,
    project_id: str | Unset = 'default',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["project_id"] = project_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/kv/{key}".format(key=quote(str(key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetKvResponse200 | None:
    if response.status_code == 200:
        response_200 = GetKvResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetKvResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    key: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = 'default',

) -> Response[Error | GetKvResponse200]:
    """ Get a KV entry

     Fetches a single key. Returns 404 when the key does not exist OR has expired (rows past `ttl_at` are
    filtered from reads). Cross-tenant lookups also return 404 — the API never reveals existence of
    another customer's keys.

    Args:
        key (str):
        project_id (str | Unset):  Default: 'default'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetKvResponse200]
     """


    kwargs = _get_kwargs(
        key=key,
project_id=project_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    key: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = 'default',

) -> Error | GetKvResponse200 | None:
    """ Get a KV entry

     Fetches a single key. Returns 404 when the key does not exist OR has expired (rows past `ttl_at` are
    filtered from reads). Cross-tenant lookups also return 404 — the API never reveals existence of
    another customer's keys.

    Args:
        key (str):
        project_id (str | Unset):  Default: 'default'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetKvResponse200
     """


    return sync_detailed(
        key=key,
client=client,
project_id=project_id,

    ).parsed

async def asyncio_detailed(
    key: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = 'default',

) -> Response[Error | GetKvResponse200]:
    """ Get a KV entry

     Fetches a single key. Returns 404 when the key does not exist OR has expired (rows past `ttl_at` are
    filtered from reads). Cross-tenant lookups also return 404 — the API never reveals existence of
    another customer's keys.

    Args:
        key (str):
        project_id (str | Unset):  Default: 'default'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetKvResponse200]
     """


    kwargs = _get_kwargs(
        key=key,
project_id=project_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    key: str,
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = 'default',

) -> Error | GetKvResponse200 | None:
    """ Get a KV entry

     Fetches a single key. Returns 404 when the key does not exist OR has expired (rows past `ttl_at` are
    filtered from reads). Cross-tenant lookups also return 404 — the API never reveals existence of
    another customer's keys.

    Args:
        key (str):
        project_id (str | Unset):  Default: 'default'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetKvResponse200
     """


    return (await asyncio_detailed(
        key=key,
client=client,
project_id=project_id,

    )).parsed
