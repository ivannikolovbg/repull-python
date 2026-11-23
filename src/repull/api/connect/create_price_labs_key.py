from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_price_labs_key_body import CreatePriceLabsKeyBody
from ...models.create_price_labs_key_response_201 import CreatePriceLabsKeyResponse201
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: CreatePriceLabsKeyBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/pricelabs/key",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreatePriceLabsKeyResponse201 | Error | None:
    if response.status_code == 201:
        response_201 = CreatePriceLabsKeyResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreatePriceLabsKeyResponse201 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePriceLabsKeyBody | Unset = UNSET,

) -> Response[CreatePriceLabsKeyResponse201 | Error]:
    """ Create a PriceLabs key (headless)

     Issue a PriceLabs key without the hosted page, for platforms that show it in their own app. The key
    is for this workspace, or the one `X-Workspace-Id` names; it is returned once, in `key`, and the
    host pastes it into PriceLabs (add an integration, choose Repull).

    - No `listingIds`: every listing of the workspace, including listings added later. Recommended, with
    the listings PriceLabs should price in their own sub-workspace.
    - `listingIds`: only those listings (they must belong to the workspace). Listings added later are
    not included.

    The key works only inside PriceLabs; it is refused on every Repull API endpoint. The connection
    appears on `GET /v1/connect/pricelabs` with its `health`; `account.created` is sent when PriceLabs
    first uses the key. Revoke it with `DELETE /v1/connect/pricelabs?id=`.

    Args:
        body (CreatePriceLabsKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePriceLabsKeyResponse201 | Error]
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
    body: CreatePriceLabsKeyBody | Unset = UNSET,

) -> CreatePriceLabsKeyResponse201 | Error | None:
    """ Create a PriceLabs key (headless)

     Issue a PriceLabs key without the hosted page, for platforms that show it in their own app. The key
    is for this workspace, or the one `X-Workspace-Id` names; it is returned once, in `key`, and the
    host pastes it into PriceLabs (add an integration, choose Repull).

    - No `listingIds`: every listing of the workspace, including listings added later. Recommended, with
    the listings PriceLabs should price in their own sub-workspace.
    - `listingIds`: only those listings (they must belong to the workspace). Listings added later are
    not included.

    The key works only inside PriceLabs; it is refused on every Repull API endpoint. The connection
    appears on `GET /v1/connect/pricelabs` with its `health`; `account.created` is sent when PriceLabs
    first uses the key. Revoke it with `DELETE /v1/connect/pricelabs?id=`.

    Args:
        body (CreatePriceLabsKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePriceLabsKeyResponse201 | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreatePriceLabsKeyBody | Unset = UNSET,

) -> Response[CreatePriceLabsKeyResponse201 | Error]:
    """ Create a PriceLabs key (headless)

     Issue a PriceLabs key without the hosted page, for platforms that show it in their own app. The key
    is for this workspace, or the one `X-Workspace-Id` names; it is returned once, in `key`, and the
    host pastes it into PriceLabs (add an integration, choose Repull).

    - No `listingIds`: every listing of the workspace, including listings added later. Recommended, with
    the listings PriceLabs should price in their own sub-workspace.
    - `listingIds`: only those listings (they must belong to the workspace). Listings added later are
    not included.

    The key works only inside PriceLabs; it is refused on every Repull API endpoint. The connection
    appears on `GET /v1/connect/pricelabs` with its `health`; `account.created` is sent when PriceLabs
    first uses the key. Revoke it with `DELETE /v1/connect/pricelabs?id=`.

    Args:
        body (CreatePriceLabsKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePriceLabsKeyResponse201 | Error]
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
    body: CreatePriceLabsKeyBody | Unset = UNSET,

) -> CreatePriceLabsKeyResponse201 | Error | None:
    """ Create a PriceLabs key (headless)

     Issue a PriceLabs key without the hosted page, for platforms that show it in their own app. The key
    is for this workspace, or the one `X-Workspace-Id` names; it is returned once, in `key`, and the
    host pastes it into PriceLabs (add an integration, choose Repull).

    - No `listingIds`: every listing of the workspace, including listings added later. Recommended, with
    the listings PriceLabs should price in their own sub-workspace.
    - `listingIds`: only those listings (they must belong to the workspace). Listings added later are
    not included.

    The key works only inside PriceLabs; it is refused on every Repull API endpoint. The connection
    appears on `GET /v1/connect/pricelabs` with its `health`; `account.created` is sent when PriceLabs
    first uses the key. Revoke it with `DELETE /v1/connect/pricelabs?id=`.

    Args:
        body (CreatePriceLabsKeyBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePriceLabsKeyResponse201 | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
