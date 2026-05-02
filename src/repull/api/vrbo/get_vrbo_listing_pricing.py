from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/vrbo/listings/{id}/pricing".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | None:
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 501:
        response_501 = Error.from_dict(response.json())



        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error]:
    """ Get VRBO pricing (501 — agency model)

     VRBO uses the agency model — VRBO PULLS rates from `/api/webhooks/vrbo/listings-
    xml/rates/{listing}/{unit}` rather than accepting a push API. This endpoint is declared for symmetry
    with the other channel-pricing routes but currently returns **501 Not Implemented** with a pointer
    at the public rate URL VRBO consumes. Use `GET /v1/listings/{id}/calendar` (once wired) to inspect
    the underlying source-of-truth.

    When the listings-XML rate-builder is ported into this repo, this endpoint will return the parsed
    rates VRBO sees.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Error | None:
    """ Get VRBO pricing (501 — agency model)

     VRBO uses the agency model — VRBO PULLS rates from `/api/webhooks/vrbo/listings-
    xml/rates/{listing}/{unit}` rather than accepting a push API. This endpoint is declared for symmetry
    with the other channel-pricing routes but currently returns **501 Not Implemented** with a pointer
    at the public rate URL VRBO consumes. Use `GET /v1/listings/{id}/calendar` (once wired) to inspect
    the underlying source-of-truth.

    When the listings-XML rate-builder is ported into this repo, this endpoint will return the parsed
    rates VRBO sees.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error]:
    """ Get VRBO pricing (501 — agency model)

     VRBO uses the agency model — VRBO PULLS rates from `/api/webhooks/vrbo/listings-
    xml/rates/{listing}/{unit}` rather than accepting a push API. This endpoint is declared for symmetry
    with the other channel-pricing routes but currently returns **501 Not Implemented** with a pointer
    at the public rate URL VRBO consumes. Use `GET /v1/listings/{id}/calendar` (once wired) to inspect
    the underlying source-of-truth.

    When the listings-XML rate-builder is ported into this repo, this endpoint will return the parsed
    rates VRBO sees.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Error | None:
    """ Get VRBO pricing (501 — agency model)

     VRBO uses the agency model — VRBO PULLS rates from `/api/webhooks/vrbo/listings-
    xml/rates/{listing}/{unit}` rather than accepting a push API. This endpoint is declared for symmetry
    with the other channel-pricing routes but currently returns **501 Not Implemented** with a pointer
    at the public rate URL VRBO consumes. Use `GET /v1/listings/{id}/calendar` (once wired) to inspect
    the underlying source-of-truth.

    When the listings-XML rate-builder is ported into this repo, this endpoint will return the parsed
    rates VRBO sees.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
