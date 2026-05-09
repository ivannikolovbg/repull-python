from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.set_kv_body import SetKvBody
from ...models.set_kv_response_200 import SetKvResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    key: str,
    *,
    body: SetKvBody,
    project_id: str | Unset = 'default',

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["project_id"] = project_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/kv/{key}".format(key=quote(str(key), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SetKvResponse200 | None:
    if response.status_code == 200:
        response_200 = SetKvResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 413:
        response_413 = Error.from_dict(response.json())



        return response_413

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SetKvResponse200]:
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
    body: SetKvBody,
    project_id: str | Unset = 'default',

) -> Response[Error | SetKvResponse200]:
    """ Set a KV entry

     Upserts a key. The full row is replaced — there is no partial update. Pass `ttl_seconds` (positive
    integer) to auto-expire the row; omit for no expiry. **Caps:** 64 KiB per row (key bytes + value
    JSON bytes), 1 MiB per customer (sum across ALL projects/keys). Over either cap returns 413.

    Args:
        key (str):
        project_id (str | Unset):  Default: 'default'.
        body (SetKvBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SetKvResponse200]
     """


    kwargs = _get_kwargs(
        key=key,
body=body,
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
    body: SetKvBody,
    project_id: str | Unset = 'default',

) -> Error | SetKvResponse200 | None:
    """ Set a KV entry

     Upserts a key. The full row is replaced — there is no partial update. Pass `ttl_seconds` (positive
    integer) to auto-expire the row; omit for no expiry. **Caps:** 64 KiB per row (key bytes + value
    JSON bytes), 1 MiB per customer (sum across ALL projects/keys). Over either cap returns 413.

    Args:
        key (str):
        project_id (str | Unset):  Default: 'default'.
        body (SetKvBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SetKvResponse200
     """


    return sync_detailed(
        key=key,
client=client,
body=body,
project_id=project_id,

    ).parsed

async def asyncio_detailed(
    key: str,
    *,
    client: AuthenticatedClient | Client,
    body: SetKvBody,
    project_id: str | Unset = 'default',

) -> Response[Error | SetKvResponse200]:
    """ Set a KV entry

     Upserts a key. The full row is replaced — there is no partial update. Pass `ttl_seconds` (positive
    integer) to auto-expire the row; omit for no expiry. **Caps:** 64 KiB per row (key bytes + value
    JSON bytes), 1 MiB per customer (sum across ALL projects/keys). Over either cap returns 413.

    Args:
        key (str):
        project_id (str | Unset):  Default: 'default'.
        body (SetKvBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SetKvResponse200]
     """


    kwargs = _get_kwargs(
        key=key,
body=body,
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
    body: SetKvBody,
    project_id: str | Unset = 'default',

) -> Error | SetKvResponse200 | None:
    """ Set a KV entry

     Upserts a key. The full row is replaced — there is no partial update. Pass `ttl_seconds` (positive
    integer) to auto-expire the row; omit for no expiry. **Caps:** 64 KiB per row (key bytes + value
    JSON bytes), 1 MiB per customer (sum across ALL projects/keys). Over either cap returns 413.

    Args:
        key (str):
        project_id (str | Unset):  Default: 'default'.
        body (SetKvBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SetKvResponse200
     """


    return (await asyncio_detailed(
        key=key,
client=client,
body=body,
project_id=project_id,

    )).parsed
