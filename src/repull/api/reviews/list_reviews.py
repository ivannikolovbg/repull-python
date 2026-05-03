from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_reviews_platform import ListReviewsPlatform
from ...models.list_reviews_reviewer_role import ListReviewsReviewerRole
from ...models.list_reviews_status import ListReviewsStatus
from ...models.review_list_response import ReviewListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    platform: ListReviewsPlatform | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    rating_min: float | Unset = UNSET,
    rating_max: float | Unset = UNSET,
    status: ListReviewsStatus | Unset = UNSET,
    reviewer_role: ListReviewsReviewerRole | Unset = ListReviewsReviewerRole.GUEST,
    x_schema: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_schema, Unset):
        headers["X-Schema"] = x_schema



    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    json_platform: str | Unset = UNSET
    if not isinstance(platform, Unset):
        json_platform = platform.value

    params["platform"] = json_platform

    params["listingId"] = listing_id

    params["rating_min"] = rating_min

    params["rating_max"] = rating_max

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_reviewer_role: str | Unset = UNSET
    if not isinstance(reviewer_role, Unset):
        json_reviewer_role = reviewer_role.value

    params["reviewerRole"] = json_reviewer_role


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/reviews",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ReviewListResponse | None:
    if response.status_code == 200:
        response_200 = ReviewListResponse.from_dict(response.json())



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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ReviewListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    platform: ListReviewsPlatform | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    rating_min: float | Unset = UNSET,
    rating_max: float | Unset = UNSET,
    status: ListReviewsStatus | Unset = UNSET,
    reviewer_role: ListReviewsReviewerRole | Unset = ListReviewsReviewerRole.GUEST,
    x_schema: str | Unset = UNSET,

) -> Response[Error | ReviewListResponse]:
    """ List reviews

     Cursor-paginated guest + host review stream for the workspace. Backed by main vanio's unified
    `reviews` table (populated by per-channel backfill crons), so this surface returns the complete
    cross-channel history — separate from `/v1/channels/airbnb/reviews` which hits Airbnb live.

    Filters: `platform` (`airbnb`|`booking`|`vrbo`), `listing_id` (internal Repull listing id),
    `rating_min` / `rating_max` (inclusive bounds, 0..5), `status` (`responded`|`unanswered`|`all`),
    `reviewer_role` (`guest` (default) | `host` | `all`).

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        platform (ListReviewsPlatform | Unset):
        listing_id (int | Unset):
        rating_min (float | Unset):
        rating_max (float | Unset):
        status (ListReviewsStatus | Unset):
        reviewer_role (ListReviewsReviewerRole | Unset):  Default: ListReviewsReviewerRole.GUEST.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReviewListResponse]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
limit=limit,
platform=platform,
listing_id=listing_id,
rating_min=rating_min,
rating_max=rating_max,
status=status,
reviewer_role=reviewer_role,
x_schema=x_schema,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    platform: ListReviewsPlatform | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    rating_min: float | Unset = UNSET,
    rating_max: float | Unset = UNSET,
    status: ListReviewsStatus | Unset = UNSET,
    reviewer_role: ListReviewsReviewerRole | Unset = ListReviewsReviewerRole.GUEST,
    x_schema: str | Unset = UNSET,

) -> Error | ReviewListResponse | None:
    """ List reviews

     Cursor-paginated guest + host review stream for the workspace. Backed by main vanio's unified
    `reviews` table (populated by per-channel backfill crons), so this surface returns the complete
    cross-channel history — separate from `/v1/channels/airbnb/reviews` which hits Airbnb live.

    Filters: `platform` (`airbnb`|`booking`|`vrbo`), `listing_id` (internal Repull listing id),
    `rating_min` / `rating_max` (inclusive bounds, 0..5), `status` (`responded`|`unanswered`|`all`),
    `reviewer_role` (`guest` (default) | `host` | `all`).

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        platform (ListReviewsPlatform | Unset):
        listing_id (int | Unset):
        rating_min (float | Unset):
        rating_max (float | Unset):
        status (ListReviewsStatus | Unset):
        reviewer_role (ListReviewsReviewerRole | Unset):  Default: ListReviewsReviewerRole.GUEST.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReviewListResponse
     """


    return sync_detailed(
        client=client,
cursor=cursor,
limit=limit,
platform=platform,
listing_id=listing_id,
rating_min=rating_min,
rating_max=rating_max,
status=status,
reviewer_role=reviewer_role,
x_schema=x_schema,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    platform: ListReviewsPlatform | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    rating_min: float | Unset = UNSET,
    rating_max: float | Unset = UNSET,
    status: ListReviewsStatus | Unset = UNSET,
    reviewer_role: ListReviewsReviewerRole | Unset = ListReviewsReviewerRole.GUEST,
    x_schema: str | Unset = UNSET,

) -> Response[Error | ReviewListResponse]:
    """ List reviews

     Cursor-paginated guest + host review stream for the workspace. Backed by main vanio's unified
    `reviews` table (populated by per-channel backfill crons), so this surface returns the complete
    cross-channel history — separate from `/v1/channels/airbnb/reviews` which hits Airbnb live.

    Filters: `platform` (`airbnb`|`booking`|`vrbo`), `listing_id` (internal Repull listing id),
    `rating_min` / `rating_max` (inclusive bounds, 0..5), `status` (`responded`|`unanswered`|`all`),
    `reviewer_role` (`guest` (default) | `host` | `all`).

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        platform (ListReviewsPlatform | Unset):
        listing_id (int | Unset):
        rating_min (float | Unset):
        rating_max (float | Unset):
        status (ListReviewsStatus | Unset):
        reviewer_role (ListReviewsReviewerRole | Unset):  Default: ListReviewsReviewerRole.GUEST.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReviewListResponse]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
limit=limit,
platform=platform,
listing_id=listing_id,
rating_min=rating_min,
rating_max=rating_max,
status=status,
reviewer_role=reviewer_role,
x_schema=x_schema,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    platform: ListReviewsPlatform | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    rating_min: float | Unset = UNSET,
    rating_max: float | Unset = UNSET,
    status: ListReviewsStatus | Unset = UNSET,
    reviewer_role: ListReviewsReviewerRole | Unset = ListReviewsReviewerRole.GUEST,
    x_schema: str | Unset = UNSET,

) -> Error | ReviewListResponse | None:
    """ List reviews

     Cursor-paginated guest + host review stream for the workspace. Backed by main vanio's unified
    `reviews` table (populated by per-channel backfill crons), so this surface returns the complete
    cross-channel history — separate from `/v1/channels/airbnb/reviews` which hits Airbnb live.

    Filters: `platform` (`airbnb`|`booking`|`vrbo`), `listing_id` (internal Repull listing id),
    `rating_min` / `rating_max` (inclusive bounds, 0..5), `status` (`responded`|`unanswered`|`all`),
    `reviewer_role` (`guest` (default) | `host` | `all`).

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        platform (ListReviewsPlatform | Unset):
        listing_id (int | Unset):
        rating_min (float | Unset):
        rating_max (float | Unset):
        status (ListReviewsStatus | Unset):
        reviewer_role (ListReviewsReviewerRole | Unset):  Default: ListReviewsReviewerRole.GUEST.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReviewListResponse
     """


    return (await asyncio_detailed(
        client=client,
cursor=cursor,
limit=limit,
platform=platform,
listing_id=listing_id,
rating_min=rating_min,
rating_max=rating_max,
status=status,
reviewer_role=reviewer_role,
x_schema=x_schema,

    )).parsed
