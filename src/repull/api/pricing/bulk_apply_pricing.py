from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulk_pricing_request import BulkPricingRequest
from ...models.bulk_pricing_response import BulkPricingResponse
from ...models.error import Error
from typing import cast



def _get_kwargs(
    *,
    body: BulkPricingRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/pricing/bulk",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BulkPricingResponse | Error | None:
    if response.status_code == 200:
        response_200 = BulkPricingResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BulkPricingResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkPricingRequest,

) -> Response[BulkPricingResponse | Error]:
    """ Bulk apply or decline pricing recommendations

     Apply or decline pending Atlas pricing recommendations across many listings in one call. Built for
    power users with hundreds of listings who would otherwise need 500 sequential single-listing POSTs.

    - `items` is capped at 500 entries per request — exceeding returns 422.
    - Per-item failures (stale listing IDs, no pending recs, channel auth blips) DO NOT fail the whole
    batch — partial success is the norm at this scale and the granular `failed[]` array lets the SDK
    retry just the bad entries.
    - Tier-limit accounting: this endpoint counts as **1 API call** regardless of how many items the
    body contains.

    Apply path writes the recommended price to each listing's calendar via the calendar service (which
    fans out to Airbnb/Booking/VRBO) then marks the Atlas recommendation `applied`. Decline path is
    Atlas-only — fast.

    Args:
        body (BulkPricingRequest): Body for `POST /v1/listings/pricing/bulk`. Apply or decline
            pending Atlas pricing recommendations across many listings in one call. Capped at 500
            items per request — exceeding returns 422.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkPricingResponse | Error]
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
    body: BulkPricingRequest,

) -> BulkPricingResponse | Error | None:
    """ Bulk apply or decline pricing recommendations

     Apply or decline pending Atlas pricing recommendations across many listings in one call. Built for
    power users with hundreds of listings who would otherwise need 500 sequential single-listing POSTs.

    - `items` is capped at 500 entries per request — exceeding returns 422.
    - Per-item failures (stale listing IDs, no pending recs, channel auth blips) DO NOT fail the whole
    batch — partial success is the norm at this scale and the granular `failed[]` array lets the SDK
    retry just the bad entries.
    - Tier-limit accounting: this endpoint counts as **1 API call** regardless of how many items the
    body contains.

    Apply path writes the recommended price to each listing's calendar via the calendar service (which
    fans out to Airbnb/Booking/VRBO) then marks the Atlas recommendation `applied`. Decline path is
    Atlas-only — fast.

    Args:
        body (BulkPricingRequest): Body for `POST /v1/listings/pricing/bulk`. Apply or decline
            pending Atlas pricing recommendations across many listings in one call. Capped at 500
            items per request — exceeding returns 422.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkPricingResponse | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BulkPricingRequest,

) -> Response[BulkPricingResponse | Error]:
    """ Bulk apply or decline pricing recommendations

     Apply or decline pending Atlas pricing recommendations across many listings in one call. Built for
    power users with hundreds of listings who would otherwise need 500 sequential single-listing POSTs.

    - `items` is capped at 500 entries per request — exceeding returns 422.
    - Per-item failures (stale listing IDs, no pending recs, channel auth blips) DO NOT fail the whole
    batch — partial success is the norm at this scale and the granular `failed[]` array lets the SDK
    retry just the bad entries.
    - Tier-limit accounting: this endpoint counts as **1 API call** regardless of how many items the
    body contains.

    Apply path writes the recommended price to each listing's calendar via the calendar service (which
    fans out to Airbnb/Booking/VRBO) then marks the Atlas recommendation `applied`. Decline path is
    Atlas-only — fast.

    Args:
        body (BulkPricingRequest): Body for `POST /v1/listings/pricing/bulk`. Apply or decline
            pending Atlas pricing recommendations across many listings in one call. Capped at 500
            items per request — exceeding returns 422.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BulkPricingResponse | Error]
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
    body: BulkPricingRequest,

) -> BulkPricingResponse | Error | None:
    """ Bulk apply or decline pricing recommendations

     Apply or decline pending Atlas pricing recommendations across many listings in one call. Built for
    power users with hundreds of listings who would otherwise need 500 sequential single-listing POSTs.

    - `items` is capped at 500 entries per request — exceeding returns 422.
    - Per-item failures (stale listing IDs, no pending recs, channel auth blips) DO NOT fail the whole
    batch — partial success is the norm at this scale and the granular `failed[]` array lets the SDK
    retry just the bad entries.
    - Tier-limit accounting: this endpoint counts as **1 API call** regardless of how many items the
    body contains.

    Apply path writes the recommended price to each listing's calendar via the calendar service (which
    fans out to Airbnb/Booking/VRBO) then marks the Atlas recommendation `applied`. Decline path is
    Atlas-only — fast.

    Args:
        body (BulkPricingRequest): Body for `POST /v1/listings/pricing/bulk`. Apply or decline
            pending Atlas pricing recommendations across many listings in one call. Capped at 500
            items per request — exceeding returns 422.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BulkPricingResponse | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
