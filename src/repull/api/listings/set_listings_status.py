from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.listing_status_batch_request import ListingStatusBatchRequest
from ...models.listing_status_batch_response import ListingStatusBatchResponse
from typing import cast



def _get_kwargs(
    *,
    body: ListingStatusBatchRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/status",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListingStatusBatchResponse | None:
    if response.status_code == 200:
        response_200 = ListingStatusBatchResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 402:
        response_402 = Error.from_dict(response.json())



        return response_402

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListingStatusBatchResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListingStatusBatchRequest,

) -> Response[Error | ListingStatusBatchResponse]:
    r""" Activate or deactivate listings in bulk

     Sets up to 500 listings active or inactive in one call. Send `{ \"listingIds\": [\"4118\",
    \"4119\"], \"active\": false }` to deactivate them, or `\"active\": true` to activate them.

    An inactive listing is not counted toward your plan's listing limit or billed. It is NOT deleted and
    the upstream channel (Airbnb / Booking.com / your PMS) is never touched — its data keeps syncing, so
    it is complete the moment you activate it again. Until then it cannot be read, changed, or receive
    webhooks.

    **All or nothing.** Nothing changes unless the whole request can be applied:
    - If any id is not one of your listings, the call returns `404` naming those ids.
    - If activating would take you over your plan's listing limit, the call returns `402
    listings_limit_exceeded`. Only listings that are currently inactive count toward the new total, so
    re-sending ids that are already active never trips the limit.

    Deactivating is always allowed, including when your account is already over its limit — it is how
    you get back under it.

    **Idempotent.** Ids already in the requested state are returned in `unchanged`; ids this call
    changed are returned in `updated`.

    For a single listing, `PATCH /v1/listings/{id}` does the same.

    Args:
        body (ListingStatusBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingStatusBatchResponse]
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
    body: ListingStatusBatchRequest,

) -> Error | ListingStatusBatchResponse | None:
    r""" Activate or deactivate listings in bulk

     Sets up to 500 listings active or inactive in one call. Send `{ \"listingIds\": [\"4118\",
    \"4119\"], \"active\": false }` to deactivate them, or `\"active\": true` to activate them.

    An inactive listing is not counted toward your plan's listing limit or billed. It is NOT deleted and
    the upstream channel (Airbnb / Booking.com / your PMS) is never touched — its data keeps syncing, so
    it is complete the moment you activate it again. Until then it cannot be read, changed, or receive
    webhooks.

    **All or nothing.** Nothing changes unless the whole request can be applied:
    - If any id is not one of your listings, the call returns `404` naming those ids.
    - If activating would take you over your plan's listing limit, the call returns `402
    listings_limit_exceeded`. Only listings that are currently inactive count toward the new total, so
    re-sending ids that are already active never trips the limit.

    Deactivating is always allowed, including when your account is already over its limit — it is how
    you get back under it.

    **Idempotent.** Ids already in the requested state are returned in `unchanged`; ids this call
    changed are returned in `updated`.

    For a single listing, `PATCH /v1/listings/{id}` does the same.

    Args:
        body (ListingStatusBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingStatusBatchResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ListingStatusBatchRequest,

) -> Response[Error | ListingStatusBatchResponse]:
    r""" Activate or deactivate listings in bulk

     Sets up to 500 listings active or inactive in one call. Send `{ \"listingIds\": [\"4118\",
    \"4119\"], \"active\": false }` to deactivate them, or `\"active\": true` to activate them.

    An inactive listing is not counted toward your plan's listing limit or billed. It is NOT deleted and
    the upstream channel (Airbnb / Booking.com / your PMS) is never touched — its data keeps syncing, so
    it is complete the moment you activate it again. Until then it cannot be read, changed, or receive
    webhooks.

    **All or nothing.** Nothing changes unless the whole request can be applied:
    - If any id is not one of your listings, the call returns `404` naming those ids.
    - If activating would take you over your plan's listing limit, the call returns `402
    listings_limit_exceeded`. Only listings that are currently inactive count toward the new total, so
    re-sending ids that are already active never trips the limit.

    Deactivating is always allowed, including when your account is already over its limit — it is how
    you get back under it.

    **Idempotent.** Ids already in the requested state are returned in `unchanged`; ids this call
    changed are returned in `updated`.

    For a single listing, `PATCH /v1/listings/{id}` does the same.

    Args:
        body (ListingStatusBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingStatusBatchResponse]
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
    body: ListingStatusBatchRequest,

) -> Error | ListingStatusBatchResponse | None:
    r""" Activate or deactivate listings in bulk

     Sets up to 500 listings active or inactive in one call. Send `{ \"listingIds\": [\"4118\",
    \"4119\"], \"active\": false }` to deactivate them, or `\"active\": true` to activate them.

    An inactive listing is not counted toward your plan's listing limit or billed. It is NOT deleted and
    the upstream channel (Airbnb / Booking.com / your PMS) is never touched — its data keeps syncing, so
    it is complete the moment you activate it again. Until then it cannot be read, changed, or receive
    webhooks.

    **All or nothing.** Nothing changes unless the whole request can be applied:
    - If any id is not one of your listings, the call returns `404` naming those ids.
    - If activating would take you over your plan's listing limit, the call returns `402
    listings_limit_exceeded`. Only listings that are currently inactive count toward the new total, so
    re-sending ids that are already active never trips the limit.

    Deactivating is always allowed, including when your account is already over its limit — it is how
    you get back under it.

    **Idempotent.** Ids already in the requested state are returned in `unchanged`; ids this call
    changed are returned in `updated`.

    For a single listing, `PATCH /v1/listings/{id}` does the same.

    Args:
        body (ListingStatusBatchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingStatusBatchResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
