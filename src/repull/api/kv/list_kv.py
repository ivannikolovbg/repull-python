from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_kv_response_200 import ListKvResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    project_id: str | Unset = 'default',
    prefix: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["project_id"] = project_id

    params["prefix"] = prefix


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/kv",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListKvResponse200 | None:
    if response.status_code == 200:
        response_200 = ListKvResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListKvResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = 'default',
    prefix: str | Unset = UNSET,

) -> Response[Error | ListKvResponse200]:
    """ List KV entries

     Returns every non-expired key-value row in the given project, sorted ascending by key. Use `prefix`
    to scope to a key namespace (e.g. `prefix=user:42:` to fetch all entries for one user). Hard cap of
    1,000 rows per response — for projects approaching that, paginate by walking prefix buckets.

    Args:
        project_id (str | Unset):  Default: 'default'.
        prefix (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListKvResponse200]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
prefix=prefix,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = 'default',
    prefix: str | Unset = UNSET,

) -> Error | ListKvResponse200 | None:
    """ List KV entries

     Returns every non-expired key-value row in the given project, sorted ascending by key. Use `prefix`
    to scope to a key namespace (e.g. `prefix=user:42:` to fetch all entries for one user). Hard cap of
    1,000 rows per response — for projects approaching that, paginate by walking prefix buckets.

    Args:
        project_id (str | Unset):  Default: 'default'.
        prefix (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListKvResponse200
     """


    return sync_detailed(
        client=client,
project_id=project_id,
prefix=prefix,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = 'default',
    prefix: str | Unset = UNSET,

) -> Response[Error | ListKvResponse200]:
    """ List KV entries

     Returns every non-expired key-value row in the given project, sorted ascending by key. Use `prefix`
    to scope to a key namespace (e.g. `prefix=user:42:` to fetch all entries for one user). Hard cap of
    1,000 rows per response — for projects approaching that, paginate by walking prefix buckets.

    Args:
        project_id (str | Unset):  Default: 'default'.
        prefix (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListKvResponse200]
     """


    kwargs = _get_kwargs(
        project_id=project_id,
prefix=prefix,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    project_id: str | Unset = 'default',
    prefix: str | Unset = UNSET,

) -> Error | ListKvResponse200 | None:
    """ List KV entries

     Returns every non-expired key-value row in the given project, sorted ascending by key. Use `prefix`
    to scope to a key namespace (e.g. `prefix=user:42:` to fetch all entries for one user). Hard cap of
    1,000 rows per response — for projects approaching that, paginate by walking prefix buckets.

    Args:
        project_id (str | Unset):  Default: 'default'.
        prefix (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListKvResponse200
     """


    return (await asyncio_detailed(
        client=client,
project_id=project_id,
prefix=prefix,

    )).parsed
