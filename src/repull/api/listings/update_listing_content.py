from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.listing_content_update_request import ListingContentUpdateRequest
from ...models.listing_content_update_response import ListingContentUpdateResponse
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ListingContentUpdateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/listings/{id}/content".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListingContentUpdateResponse | None:
    if response.status_code == 200:
        response_200 = ListingContentUpdateResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListingContentUpdateResponse]:
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
    body: ListingContentUpdateRequest,

) -> Response[Error | ListingContentUpdateResponse]:
    r""" Update canonical listing content

     Write your PMS's canonical listing content — title, description, amenities, address, occupancy, and
    policies — into a Repull listing, making it the source of truth. This is the flagship \"the PMS owns
    listing content, Repull distributes it\" enabler.

    **Partial update:** every field is optional. Only the fields you send are written; absent fields are
    left untouched. `amenities` is a FULL replacement of the amenity set (omit to leave untouched, send
    `[]` to clear).

    **Local write only — NOT a channel publish.** This mutates Repull's own copy of the content. It does
    NOT push to Airbnb / Booking.com; it marks the channels dirty so a later publish knows what changed.
    Distribution stays a separate explicit step.

    **Photos are deferred:** a provided `photos` array is echoed back in the `deferred` field and NOT
    persisted (media ingestion is a follow-up).

    Cross-tenant access (a listing that belongs to a different workspace) returns 404 — never 403. This
    endpoint is served even when the account is over the plan-listings cap, since editing content on a
    listing you already own never grows the portfolio.

    Args:
        id (int):
        body (ListingContentUpdateRequest): Canonical PMS-owned listing content. Every field is
            optional — this is a partial update, only the fields you send are written; absent fields
            are left untouched. This is a LOCAL write only: it does NOT push to Airbnb/Booking.com.
            Distribution is a separate explicit publish step. `photos` are ingested by URL and
            attached to the listing in order (full-replace by default, or append via `photosMode`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingContentUpdateResponse]
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
    body: ListingContentUpdateRequest,

) -> Error | ListingContentUpdateResponse | None:
    r""" Update canonical listing content

     Write your PMS's canonical listing content — title, description, amenities, address, occupancy, and
    policies — into a Repull listing, making it the source of truth. This is the flagship \"the PMS owns
    listing content, Repull distributes it\" enabler.

    **Partial update:** every field is optional. Only the fields you send are written; absent fields are
    left untouched. `amenities` is a FULL replacement of the amenity set (omit to leave untouched, send
    `[]` to clear).

    **Local write only — NOT a channel publish.** This mutates Repull's own copy of the content. It does
    NOT push to Airbnb / Booking.com; it marks the channels dirty so a later publish knows what changed.
    Distribution stays a separate explicit step.

    **Photos are deferred:** a provided `photos` array is echoed back in the `deferred` field and NOT
    persisted (media ingestion is a follow-up).

    Cross-tenant access (a listing that belongs to a different workspace) returns 404 — never 403. This
    endpoint is served even when the account is over the plan-listings cap, since editing content on a
    listing you already own never grows the portfolio.

    Args:
        id (int):
        body (ListingContentUpdateRequest): Canonical PMS-owned listing content. Every field is
            optional — this is a partial update, only the fields you send are written; absent fields
            are left untouched. This is a LOCAL write only: it does NOT push to Airbnb/Booking.com.
            Distribution is a separate explicit publish step. `photos` are ingested by URL and
            attached to the listing in order (full-replace by default, or append via `photosMode`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingContentUpdateResponse
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
    body: ListingContentUpdateRequest,

) -> Response[Error | ListingContentUpdateResponse]:
    r""" Update canonical listing content

     Write your PMS's canonical listing content — title, description, amenities, address, occupancy, and
    policies — into a Repull listing, making it the source of truth. This is the flagship \"the PMS owns
    listing content, Repull distributes it\" enabler.

    **Partial update:** every field is optional. Only the fields you send are written; absent fields are
    left untouched. `amenities` is a FULL replacement of the amenity set (omit to leave untouched, send
    `[]` to clear).

    **Local write only — NOT a channel publish.** This mutates Repull's own copy of the content. It does
    NOT push to Airbnb / Booking.com; it marks the channels dirty so a later publish knows what changed.
    Distribution stays a separate explicit step.

    **Photos are deferred:** a provided `photos` array is echoed back in the `deferred` field and NOT
    persisted (media ingestion is a follow-up).

    Cross-tenant access (a listing that belongs to a different workspace) returns 404 — never 403. This
    endpoint is served even when the account is over the plan-listings cap, since editing content on a
    listing you already own never grows the portfolio.

    Args:
        id (int):
        body (ListingContentUpdateRequest): Canonical PMS-owned listing content. Every field is
            optional — this is a partial update, only the fields you send are written; absent fields
            are left untouched. This is a LOCAL write only: it does NOT push to Airbnb/Booking.com.
            Distribution is a separate explicit publish step. `photos` are ingested by URL and
            attached to the listing in order (full-replace by default, or append via `photosMode`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingContentUpdateResponse]
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
    body: ListingContentUpdateRequest,

) -> Error | ListingContentUpdateResponse | None:
    r""" Update canonical listing content

     Write your PMS's canonical listing content — title, description, amenities, address, occupancy, and
    policies — into a Repull listing, making it the source of truth. This is the flagship \"the PMS owns
    listing content, Repull distributes it\" enabler.

    **Partial update:** every field is optional. Only the fields you send are written; absent fields are
    left untouched. `amenities` is a FULL replacement of the amenity set (omit to leave untouched, send
    `[]` to clear).

    **Local write only — NOT a channel publish.** This mutates Repull's own copy of the content. It does
    NOT push to Airbnb / Booking.com; it marks the channels dirty so a later publish knows what changed.
    Distribution stays a separate explicit step.

    **Photos are deferred:** a provided `photos` array is echoed back in the `deferred` field and NOT
    persisted (media ingestion is a follow-up).

    Cross-tenant access (a listing that belongs to a different workspace) returns 404 — never 403. This
    endpoint is served even when the account is over the plan-listings cap, since editing content on a
    listing you already own never grows the portfolio.

    Args:
        id (int):
        body (ListingContentUpdateRequest): Canonical PMS-owned listing content. Every field is
            optional — this is a partial update, only the fields you send are written; absent fields
            are left untouched. This is a LOCAL write only: it does NOT push to Airbnb/Booking.com.
            Distribution is a separate explicit publish step. `photos` are ingested by URL and
            attached to the listing in order (full-replace by default, or append via `photosMode`).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingContentUpdateResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
