from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_kv_response_200 import DeleteKvResponse200
from ...models.error import Error
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
        "method": "delete",
        "url": "/v1/kv/{key}".format(key=quote(str(key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteKvResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = DeleteKvResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteKvResponse200 | Error]:
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

) -> Response[DeleteKvResponse200 | Error]:
    """ Delete a KV entry

     Removes a single key. Returns `{ deleted: true }` if the row was present, `{ deleted: false }` if it
    was already absent — both are 200 (idempotent).

    Args:
        key (str):
        project_id (str | Unset):  Default: 'default'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteKvResponse200 | Error]
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

) -> DeleteKvResponse200 | Error | None:
    """ Delete a KV entry

     Removes a single key. Returns `{ deleted: true }` if the row was present, `{ deleted: false }` if it
    was already absent — both are 200 (idempotent).

    Args:
        key (str):
        project_id (str | Unset):  Default: 'default'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteKvResponse200 | Error
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

) -> Response[DeleteKvResponse200 | Error]:
    """ Delete a KV entry

     Removes a single key. Returns `{ deleted: true }` if the row was present, `{ deleted: false }` if it
    was already absent — both are 200 (idempotent).

    Args:
        key (str):
        project_id (str | Unset):  Default: 'default'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteKvResponse200 | Error]
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

) -> DeleteKvResponse200 | Error | None:
    """ Delete a KV entry

     Removes a single key. Returns `{ deleted: true }` if the row was present, `{ deleted: false }` if it
    was already absent — both are 200 (idempotent).

    Args:
        key (str):
        project_id (str | Unset):  Default: 'default'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteKvResponse200 | Error
     """


    return (await asyncio_detailed(
        key=key,
client=client,
project_id=project_id,

    )).parsed
