from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.reply_booking_review_body import ReplyBookingReviewBody
from ...models.reply_booking_review_response_200 import ReplyBookingReviewResponse200
from typing import cast



def _get_kwargs(
    *,
    body: ReplyBookingReviewBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/booking/reviews",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ReplyBookingReviewResponse200 | None:
    if response.status_code == 200:
        response_200 = ReplyBookingReviewResponse200.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ReplyBookingReviewResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReplyBookingReviewBody,

) -> Response[Error | ReplyBookingReviewResponse200]:
    """ Reply to Booking.com review

     Post a public host reply to a guest review on Booking.com. Booking allows one host reply per review
    — repeated POSTs are rejected by upstream.

    Booking.com does NOT support host-authored reviews of guests via the API (platform-level
    limitation), so this endpoint is reply-only.

    Args:
        body (ReplyBookingReviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReplyBookingReviewResponse200]
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
    body: ReplyBookingReviewBody,

) -> Error | ReplyBookingReviewResponse200 | None:
    """ Reply to Booking.com review

     Post a public host reply to a guest review on Booking.com. Booking allows one host reply per review
    — repeated POSTs are rejected by upstream.

    Booking.com does NOT support host-authored reviews of guests via the API (platform-level
    limitation), so this endpoint is reply-only.

    Args:
        body (ReplyBookingReviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReplyBookingReviewResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ReplyBookingReviewBody,

) -> Response[Error | ReplyBookingReviewResponse200]:
    """ Reply to Booking.com review

     Post a public host reply to a guest review on Booking.com. Booking allows one host reply per review
    — repeated POSTs are rejected by upstream.

    Booking.com does NOT support host-authored reviews of guests via the API (platform-level
    limitation), so this endpoint is reply-only.

    Args:
        body (ReplyBookingReviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReplyBookingReviewResponse200]
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
    body: ReplyBookingReviewBody,

) -> Error | ReplyBookingReviewResponse200 | None:
    """ Reply to Booking.com review

     Post a public host reply to a guest review on Booking.com. Booking allows one host reply per review
    — repeated POSTs are rejected by upstream.

    Booking.com does NOT support host-authored reviews of guests via the API (platform-level
    limitation), so this endpoint is reply-only.

    Args:
        body (ReplyBookingReviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReplyBookingReviewResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
