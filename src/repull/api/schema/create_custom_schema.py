from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.custom_schema_create import CustomSchemaCreate
from ...models.custom_schema_create_response import CustomSchemaCreateResponse
from ...models.error import Error
from typing import cast



def _get_kwargs(
    *,
    body: CustomSchemaCreate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/schema/custom",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CustomSchemaCreateResponse | Error | None:
    if response.status_code == 201:
        response_201 = CustomSchemaCreateResponse.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CustomSchemaCreateResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CustomSchemaCreate,

) -> Response[CustomSchemaCreateResponse | Error]:
    """ Create a custom schema

     Create a workspace-scoped field-mapping schema. The schema reshapes the `native` response payload
    into your app's preferred field names. After creation, set `X-Schema: <name>` on any read endpoint
    to apply it.

    **Reserved names:** `calry`, `calry-v1`, `native` are built-in schemas and cannot be used as a
    custom name.

    **Mapping safety:** Each mapping value is parsed by an internal expression engine — `eval`,
    `Function`, `process`, and other unsafe keywords are rejected up front. Field names are capped at
    100 chars and expressions at 500 chars.

    Args:
        body (CustomSchemaCreate): Request body for `POST /v1/schema/custom`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomSchemaCreateResponse | Error]
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
    body: CustomSchemaCreate,

) -> CustomSchemaCreateResponse | Error | None:
    """ Create a custom schema

     Create a workspace-scoped field-mapping schema. The schema reshapes the `native` response payload
    into your app's preferred field names. After creation, set `X-Schema: <name>` on any read endpoint
    to apply it.

    **Reserved names:** `calry`, `calry-v1`, `native` are built-in schemas and cannot be used as a
    custom name.

    **Mapping safety:** Each mapping value is parsed by an internal expression engine — `eval`,
    `Function`, `process`, and other unsafe keywords are rejected up front. Field names are capped at
    100 chars and expressions at 500 chars.

    Args:
        body (CustomSchemaCreate): Request body for `POST /v1/schema/custom`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomSchemaCreateResponse | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CustomSchemaCreate,

) -> Response[CustomSchemaCreateResponse | Error]:
    """ Create a custom schema

     Create a workspace-scoped field-mapping schema. The schema reshapes the `native` response payload
    into your app's preferred field names. After creation, set `X-Schema: <name>` on any read endpoint
    to apply it.

    **Reserved names:** `calry`, `calry-v1`, `native` are built-in schemas and cannot be used as a
    custom name.

    **Mapping safety:** Each mapping value is parsed by an internal expression engine — `eval`,
    `Function`, `process`, and other unsafe keywords are rejected up front. Field names are capped at
    100 chars and expressions at 500 chars.

    Args:
        body (CustomSchemaCreate): Request body for `POST /v1/schema/custom`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomSchemaCreateResponse | Error]
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
    body: CustomSchemaCreate,

) -> CustomSchemaCreateResponse | Error | None:
    """ Create a custom schema

     Create a workspace-scoped field-mapping schema. The schema reshapes the `native` response payload
    into your app's preferred field names. After creation, set `X-Schema: <name>` on any read endpoint
    to apply it.

    **Reserved names:** `calry`, `calry-v1`, `native` are built-in schemas and cannot be used as a
    custom name.

    **Mapping safety:** Each mapping value is parsed by an internal expression engine — `eval`,
    `Function`, `process`, and other unsafe keywords are rejected up front. Field names are capped at
    100 chars and expressions at 500 chars.

    Args:
        body (CustomSchemaCreate): Request body for `POST /v1/schema/custom`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomSchemaCreateResponse | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
