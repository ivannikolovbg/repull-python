from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_tiket_properties_status import ListTiketPropertiesStatus
from ...models.tiket_property_list_response import TiketPropertyListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    status: ListTiketPropertiesStatus | Unset = ListTiketPropertiesStatus.ACTIVE,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/tiket/properties",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TiketPropertyListResponse | None:
    if response.status_code == 200:
        response_200 = TiketPropertyListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | TiketPropertyListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: ListTiketPropertiesStatus | Unset = ListTiketPropertiesStatus.ACTIVE,

) -> Response[Error | TiketPropertyListResponse]:
    r""" List tiket.com properties

     Every tiket.com property connected to this workspace, each returned once with its room types, rate
    plans and the listing each room type is mapped to.

    A tiket.com property is a hotel or building; its room types are what guests book, and each room type
    maps to one Repull listing. A property whose rooms are not mapped yet is still listed, with
    `mappingStatus: \"unmapped\"`. Properties waiting for tiket.com to activate Repull are listed with
    their `activationStatus`.

    Args:
        status (ListTiketPropertiesStatus | Unset):  Default: ListTiketPropertiesStatus.ACTIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketPropertyListResponse]
     """


    kwargs = _get_kwargs(
        status=status,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    status: ListTiketPropertiesStatus | Unset = ListTiketPropertiesStatus.ACTIVE,

) -> Error | TiketPropertyListResponse | None:
    r""" List tiket.com properties

     Every tiket.com property connected to this workspace, each returned once with its room types, rate
    plans and the listing each room type is mapped to.

    A tiket.com property is a hotel or building; its room types are what guests book, and each room type
    maps to one Repull listing. A property whose rooms are not mapped yet is still listed, with
    `mappingStatus: \"unmapped\"`. Properties waiting for tiket.com to activate Repull are listed with
    their `activationStatus`.

    Args:
        status (ListTiketPropertiesStatus | Unset):  Default: ListTiketPropertiesStatus.ACTIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketPropertyListResponse
     """


    return sync_detailed(
        client=client,
status=status,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: ListTiketPropertiesStatus | Unset = ListTiketPropertiesStatus.ACTIVE,

) -> Response[Error | TiketPropertyListResponse]:
    r""" List tiket.com properties

     Every tiket.com property connected to this workspace, each returned once with its room types, rate
    plans and the listing each room type is mapped to.

    A tiket.com property is a hotel or building; its room types are what guests book, and each room type
    maps to one Repull listing. A property whose rooms are not mapped yet is still listed, with
    `mappingStatus: \"unmapped\"`. Properties waiting for tiket.com to activate Repull are listed with
    their `activationStatus`.

    Args:
        status (ListTiketPropertiesStatus | Unset):  Default: ListTiketPropertiesStatus.ACTIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketPropertyListResponse]
     """


    kwargs = _get_kwargs(
        status=status,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: ListTiketPropertiesStatus | Unset = ListTiketPropertiesStatus.ACTIVE,

) -> Error | TiketPropertyListResponse | None:
    r""" List tiket.com properties

     Every tiket.com property connected to this workspace, each returned once with its room types, rate
    plans and the listing each room type is mapped to.

    A tiket.com property is a hotel or building; its room types are what guests book, and each room type
    maps to one Repull listing. A property whose rooms are not mapped yet is still listed, with
    `mappingStatus: \"unmapped\"`. Properties waiting for tiket.com to activate Repull are listed with
    their `activationStatus`.

    Args:
        status (ListTiketPropertiesStatus | Unset):  Default: ListTiketPropertiesStatus.ACTIVE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketPropertyListResponse
     """


    return (await asyncio_detailed(
        client=client,
status=status,

    )).parsed
