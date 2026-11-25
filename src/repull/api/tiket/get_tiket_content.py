from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.tiket_content_response import TiketContentResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    property_id: str | Unset = UNSET,
    partner_hotel_code: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["property_id"] = property_id

    params["partner_hotel_code"] = partner_hotel_code


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/tiket/content",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TiketContentResponse | None:
    if response.status_code == 200:
        response_200 = TiketContentResponse.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | TiketContentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    property_id: str | Unset = UNSET,
    partner_hotel_code: str | Unset = UNSET,

) -> Response[Error | TiketContentResponse]:
    """ Read the content Repull sent tiket.com

     tiket.com has no API to read content back, so this is the record of what Repull sent for a property
    — the property, its room types and rate plans — with when each was sent and tiket.com's reference
    for it. Send changes with `POST /v1/listings/{id}/publish/tiket`.

    Name the property with `property_id`, or with `partner_hotel_code` for a property Repull created
    that tiket.com has not assigned an id to yet.

    Args:
        property_id (str | Unset):
        partner_hotel_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketContentResponse]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
partner_hotel_code=partner_hotel_code,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    property_id: str | Unset = UNSET,
    partner_hotel_code: str | Unset = UNSET,

) -> Error | TiketContentResponse | None:
    """ Read the content Repull sent tiket.com

     tiket.com has no API to read content back, so this is the record of what Repull sent for a property
    — the property, its room types and rate plans — with when each was sent and tiket.com's reference
    for it. Send changes with `POST /v1/listings/{id}/publish/tiket`.

    Name the property with `property_id`, or with `partner_hotel_code` for a property Repull created
    that tiket.com has not assigned an id to yet.

    Args:
        property_id (str | Unset):
        partner_hotel_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketContentResponse
     """


    return sync_detailed(
        client=client,
property_id=property_id,
partner_hotel_code=partner_hotel_code,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    property_id: str | Unset = UNSET,
    partner_hotel_code: str | Unset = UNSET,

) -> Response[Error | TiketContentResponse]:
    """ Read the content Repull sent tiket.com

     tiket.com has no API to read content back, so this is the record of what Repull sent for a property
    — the property, its room types and rate plans — with when each was sent and tiket.com's reference
    for it. Send changes with `POST /v1/listings/{id}/publish/tiket`.

    Name the property with `property_id`, or with `partner_hotel_code` for a property Repull created
    that tiket.com has not assigned an id to yet.

    Args:
        property_id (str | Unset):
        partner_hotel_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketContentResponse]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
partner_hotel_code=partner_hotel_code,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    property_id: str | Unset = UNSET,
    partner_hotel_code: str | Unset = UNSET,

) -> Error | TiketContentResponse | None:
    """ Read the content Repull sent tiket.com

     tiket.com has no API to read content back, so this is the record of what Repull sent for a property
    — the property, its room types and rate plans — with when each was sent and tiket.com's reference
    for it. Send changes with `POST /v1/listings/{id}/publish/tiket`.

    Name the property with `property_id`, or with `partner_hotel_code` for a property Repull created
    that tiket.com has not assigned an id to yet.

    Args:
        property_id (str | Unset):
        partner_hotel_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketContentResponse
     """


    return (await asyncio_detailed(
        client=client,
property_id=property_id,
partner_hotel_code=partner_hotel_code,

    )).parsed
