from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.listing_generate_content_request import ListingGenerateContentRequest
from ...models.listing_generate_content_response import ListingGenerateContentResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ListingGenerateContentRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/{id}/generate-content".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | ListingGenerateContentResponse | None:
    if response.status_code == 200:
        response_200 = ListingGenerateContentResponse.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 502:
        response_502 = cast(Any, None)
        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error | ListingGenerateContentResponse]:
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
    body: ListingGenerateContentRequest | Unset = UNSET,

) -> Response[Any | Error | ListingGenerateContentResponse]:
    """ AI-generate listing content

     Generate guest-facing copy (title, summary, description, amenities, etc.) for a listing using Kimi
    K2. When `photos` are provided the vision model is used for photo-grounded copy. Persists into the
    listing by default.

    Args:
        id (int):
        body (ListingGenerateContentRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | ListingGenerateContentResponse]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingGenerateContentRequest | Unset = UNSET,

) -> Any | Error | ListingGenerateContentResponse | None:
    """ AI-generate listing content

     Generate guest-facing copy (title, summary, description, amenities, etc.) for a listing using Kimi
    K2. When `photos` are provided the vision model is used for photo-grounded copy. Persists into the
    listing by default.

    Args:
        id (int):
        body (ListingGenerateContentRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | ListingGenerateContentResponse
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingGenerateContentRequest | Unset = UNSET,

) -> Response[Any | Error | ListingGenerateContentResponse]:
    """ AI-generate listing content

     Generate guest-facing copy (title, summary, description, amenities, etc.) for a listing using Kimi
    K2. When `photos` are provided the vision model is used for photo-grounded copy. Persists into the
    listing by default.

    Args:
        id (int):
        body (ListingGenerateContentRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | ListingGenerateContentResponse]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingGenerateContentRequest | Unset = UNSET,

) -> Any | Error | ListingGenerateContentResponse | None:
    """ AI-generate listing content

     Generate guest-facing copy (title, summary, description, amenities, etc.) for a listing using Kimi
    K2. When `photos` are provided the vision model is used for photo-grounded copy. Persists into the
    listing by default.

    Args:
        id (int):
        body (ListingGenerateContentRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | ListingGenerateContentResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
