from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_vrbo_reviews_reviewer_role import ListVrboReviewsReviewerRole
from ...models.list_vrbo_reviews_status import ListVrboReviewsStatus
from ...models.review_list_response import ReviewListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    listing_id: str | Unset = UNSET,
    status: ListVrboReviewsStatus | Unset = UNSET,
    reviewer_role: ListVrboReviewsReviewerRole | Unset = ListVrboReviewsReviewerRole.GUEST,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params["listingId"] = listing_id

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
        "url": "/v1/channels/vrbo/reviews",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ReviewListResponse | None:
    if response.status_code == 200:
        response_200 = ReviewListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

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
    listing_id: str | Unset = UNSET,
    status: ListVrboReviewsStatus | Unset = UNSET,
    reviewer_role: ListVrboReviewsReviewerRole | Unset = ListVrboReviewsReviewerRole.GUEST,

) -> Response[Error | ReviewListResponse]:
    """ List Vrbo reviews

     The workspace's Vrbo reviews — the counterpart of `GET /v1/channels/airbnb/reviews`. The same list,
    filters, paging and review shape as `GET /v1/reviews?platform=vrbo`, with the channel fixed:
    `reviewerRole=guest` (default) is what guests wrote, `reviewerRole=host` your ratings of guests.
    Reply to a review with `POST /v1/reviews/{id}/reply`; rate a guest with `PUT
    /v1/channels/vrbo/reviews/{id}`.

    Reviews of inactive listings are left out; `listingId` naming an inactive listing returns `403
    listing_inactive`. `platform` other than `vrbo` is refused.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        listing_id (str | Unset):
        status (ListVrboReviewsStatus | Unset):
        reviewer_role (ListVrboReviewsReviewerRole | Unset):  Default:
            ListVrboReviewsReviewerRole.GUEST.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReviewListResponse]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
limit=limit,
listing_id=listing_id,
status=status,
reviewer_role=reviewer_role,

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
    listing_id: str | Unset = UNSET,
    status: ListVrboReviewsStatus | Unset = UNSET,
    reviewer_role: ListVrboReviewsReviewerRole | Unset = ListVrboReviewsReviewerRole.GUEST,

) -> Error | ReviewListResponse | None:
    """ List Vrbo reviews

     The workspace's Vrbo reviews — the counterpart of `GET /v1/channels/airbnb/reviews`. The same list,
    filters, paging and review shape as `GET /v1/reviews?platform=vrbo`, with the channel fixed:
    `reviewerRole=guest` (default) is what guests wrote, `reviewerRole=host` your ratings of guests.
    Reply to a review with `POST /v1/reviews/{id}/reply`; rate a guest with `PUT
    /v1/channels/vrbo/reviews/{id}`.

    Reviews of inactive listings are left out; `listingId` naming an inactive listing returns `403
    listing_inactive`. `platform` other than `vrbo` is refused.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        listing_id (str | Unset):
        status (ListVrboReviewsStatus | Unset):
        reviewer_role (ListVrboReviewsReviewerRole | Unset):  Default:
            ListVrboReviewsReviewerRole.GUEST.

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
listing_id=listing_id,
status=status,
reviewer_role=reviewer_role,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    listing_id: str | Unset = UNSET,
    status: ListVrboReviewsStatus | Unset = UNSET,
    reviewer_role: ListVrboReviewsReviewerRole | Unset = ListVrboReviewsReviewerRole.GUEST,

) -> Response[Error | ReviewListResponse]:
    """ List Vrbo reviews

     The workspace's Vrbo reviews — the counterpart of `GET /v1/channels/airbnb/reviews`. The same list,
    filters, paging and review shape as `GET /v1/reviews?platform=vrbo`, with the channel fixed:
    `reviewerRole=guest` (default) is what guests wrote, `reviewerRole=host` your ratings of guests.
    Reply to a review with `POST /v1/reviews/{id}/reply`; rate a guest with `PUT
    /v1/channels/vrbo/reviews/{id}`.

    Reviews of inactive listings are left out; `listingId` naming an inactive listing returns `403
    listing_inactive`. `platform` other than `vrbo` is refused.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        listing_id (str | Unset):
        status (ListVrboReviewsStatus | Unset):
        reviewer_role (ListVrboReviewsReviewerRole | Unset):  Default:
            ListVrboReviewsReviewerRole.GUEST.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReviewListResponse]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
limit=limit,
listing_id=listing_id,
status=status,
reviewer_role=reviewer_role,

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
    listing_id: str | Unset = UNSET,
    status: ListVrboReviewsStatus | Unset = UNSET,
    reviewer_role: ListVrboReviewsReviewerRole | Unset = ListVrboReviewsReviewerRole.GUEST,

) -> Error | ReviewListResponse | None:
    """ List Vrbo reviews

     The workspace's Vrbo reviews — the counterpart of `GET /v1/channels/airbnb/reviews`. The same list,
    filters, paging and review shape as `GET /v1/reviews?platform=vrbo`, with the channel fixed:
    `reviewerRole=guest` (default) is what guests wrote, `reviewerRole=host` your ratings of guests.
    Reply to a review with `POST /v1/reviews/{id}/reply`; rate a guest with `PUT
    /v1/channels/vrbo/reviews/{id}`.

    Reviews of inactive listings are left out; `listingId` naming an inactive listing returns `403
    listing_inactive`. `platform` other than `vrbo` is refused.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        listing_id (str | Unset):
        status (ListVrboReviewsStatus | Unset):
        reviewer_role (ListVrboReviewsReviewerRole | Unset):  Default:
            ListVrboReviewsReviewerRole.GUEST.

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
listing_id=listing_id,
status=status,
reviewer_role=reviewer_role,

    )).parsed
