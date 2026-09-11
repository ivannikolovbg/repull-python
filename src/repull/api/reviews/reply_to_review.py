from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.reply_to_review_body import ReplyToReviewBody
from ...models.reply_to_review_response_201 import ReplyToReviewResponse201
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ReplyToReviewBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/reviews/{id}/reply".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ReplyToReviewResponse201 | None:
    if response.status_code == 201:
        response_201 = ReplyToReviewResponse201.from_dict(response.json())



        return response_201

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ReplyToReviewResponse201]:
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
    body: ReplyToReviewBody,

) -> Response[Error | ReplyToReviewResponse201]:
    """ Reply to a review on any channel

     Resolves the review, reads its channel and dispatches the reply. Channel-neutral: you do not need to
    know where the review came from.

    Replies are available on Airbnb today; a review from a channel without a reply API returns `422
    unsupported_channel` naming the channels that do work.

    Args:
        id (int):
        body (ReplyToReviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReplyToReviewResponse201]
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
    body: ReplyToReviewBody,

) -> Error | ReplyToReviewResponse201 | None:
    """ Reply to a review on any channel

     Resolves the review, reads its channel and dispatches the reply. Channel-neutral: you do not need to
    know where the review came from.

    Replies are available on Airbnb today; a review from a channel without a reply API returns `422
    unsupported_channel` naming the channels that do work.

    Args:
        id (int):
        body (ReplyToReviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReplyToReviewResponse201
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
    body: ReplyToReviewBody,

) -> Response[Error | ReplyToReviewResponse201]:
    """ Reply to a review on any channel

     Resolves the review, reads its channel and dispatches the reply. Channel-neutral: you do not need to
    know where the review came from.

    Replies are available on Airbnb today; a review from a channel without a reply API returns `422
    unsupported_channel` naming the channels that do work.

    Args:
        id (int):
        body (ReplyToReviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReplyToReviewResponse201]
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
    body: ReplyToReviewBody,

) -> Error | ReplyToReviewResponse201 | None:
    """ Reply to a review on any channel

     Resolves the review, reads its channel and dispatches the reply. Channel-neutral: you do not need to
    know where the review came from.

    Replies are available on Airbnb today; a review from a channel without a reply API returns `422
    unsupported_channel` naming the channels that do work.

    Args:
        id (int):
        body (ReplyToReviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReplyToReviewResponse201
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
