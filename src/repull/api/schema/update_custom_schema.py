from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.custom_schema import CustomSchema
from ...models.custom_schema_update import CustomSchemaUpdate
from ...models.error import Error
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    body: CustomSchemaUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/schema/custom/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CustomSchema | Error | None:
    if response.status_code == 200:
        response_200 = CustomSchema.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CustomSchema | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CustomSchemaUpdate,

) -> Response[CustomSchema | Error]:
    """ Update a custom schema

     Patch the description, mappings, or active flag of a custom schema. The schema `name` is immutable —
    create a new schema and migrate consumers if you need to rename. Mapping updates are revalidated for
    safety.

    Args:
        id (UUID):
        body (CustomSchemaUpdate): Request body for `PATCH /v1/schema/custom/{id}`. All fields
            optional; omitted fields are left unchanged. `name` is intentionally NOT patchable —
            create a new schema and migrate consumers if you need to rename.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomSchema | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CustomSchemaUpdate,

) -> CustomSchema | Error | None:
    """ Update a custom schema

     Patch the description, mappings, or active flag of a custom schema. The schema `name` is immutable —
    create a new schema and migrate consumers if you need to rename. Mapping updates are revalidated for
    safety.

    Args:
        id (UUID):
        body (CustomSchemaUpdate): Request body for `PATCH /v1/schema/custom/{id}`. All fields
            optional; omitted fields are left unchanged. `name` is intentionally NOT patchable —
            create a new schema and migrate consumers if you need to rename.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomSchema | Error
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CustomSchemaUpdate,

) -> Response[CustomSchema | Error]:
    """ Update a custom schema

     Patch the description, mappings, or active flag of a custom schema. The schema `name` is immutable —
    create a new schema and migrate consumers if you need to rename. Mapping updates are revalidated for
    safety.

    Args:
        id (UUID):
        body (CustomSchemaUpdate): Request body for `PATCH /v1/schema/custom/{id}`. All fields
            optional; omitted fields are left unchanged. `name` is intentionally NOT patchable —
            create a new schema and migrate consumers if you need to rename.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CustomSchema | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: CustomSchemaUpdate,

) -> CustomSchema | Error | None:
    """ Update a custom schema

     Patch the description, mappings, or active flag of a custom schema. The schema `name` is immutable —
    create a new schema and migrate consumers if you need to rename. Mapping updates are revalidated for
    safety.

    Args:
        id (UUID):
        body (CustomSchemaUpdate): Request body for `PATCH /v1/schema/custom/{id}`. All fields
            optional; omitted fields are left unchanged. `name` is intentionally NOT patchable —
            create a new schema and migrate consumers if you need to rename.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CustomSchema | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
