from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.promotion_bulk_request import PromotionBulkRequest
from ...models.promotion_bulk_response import PromotionBulkResponse
from typing import cast



def _get_kwargs(
    *,
    body: PromotionBulkRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/promotions/bulk",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PromotionBulkResponse | None:
    if response.status_code == 200:
        response_200 = PromotionBulkResponse.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PromotionBulkResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PromotionBulkRequest,

) -> Response[Error | PromotionBulkResponse]:
    """ Add or remove a promotion on many listings

     Applies one promotion to up to 100 listings — `add` it, or `remove` the listing's running promotion
    of that channel and type. Each listing gets its own result with the channel's reason when refused,
    so one refusal doesn't stop the rest. Returns `403 listing_inactive` before doing anything when any
    listing is inactive.

    Args:
        body (PromotionBulkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PromotionBulkResponse]
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
    body: PromotionBulkRequest,

) -> Error | PromotionBulkResponse | None:
    """ Add or remove a promotion on many listings

     Applies one promotion to up to 100 listings — `add` it, or `remove` the listing's running promotion
    of that channel and type. Each listing gets its own result with the channel's reason when refused,
    so one refusal doesn't stop the rest. Returns `403 listing_inactive` before doing anything when any
    listing is inactive.

    Args:
        body (PromotionBulkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PromotionBulkResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PromotionBulkRequest,

) -> Response[Error | PromotionBulkResponse]:
    """ Add or remove a promotion on many listings

     Applies one promotion to up to 100 listings — `add` it, or `remove` the listing's running promotion
    of that channel and type. Each listing gets its own result with the channel's reason when refused,
    so one refusal doesn't stop the rest. Returns `403 listing_inactive` before doing anything when any
    listing is inactive.

    Args:
        body (PromotionBulkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PromotionBulkResponse]
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
    body: PromotionBulkRequest,

) -> Error | PromotionBulkResponse | None:
    """ Add or remove a promotion on many listings

     Applies one promotion to up to 100 listings — `add` it, or `remove` the listing's running promotion
    of that channel and type. Each listing gets its own result with the channel's reason when refused,
    so one refusal doesn't stop the rest. Returns `403 listing_inactive` before doing anything when any
    listing is inactive.

    Args:
        body (PromotionBulkRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PromotionBulkResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
