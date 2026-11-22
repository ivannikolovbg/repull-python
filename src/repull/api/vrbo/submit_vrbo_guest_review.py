from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.submit_vrbo_guest_review_body import SubmitVrboGuestReviewBody
from ...models.submit_vrbo_guest_review_response_200 import SubmitVrboGuestReviewResponse200
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: SubmitVrboGuestReviewBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/vrbo/reviews/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SubmitVrboGuestReviewResponse200 | None:
    if response.status_code == 200:
        response_200 = SubmitVrboGuestReviewResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SubmitVrboGuestReviewResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitVrboGuestReviewBody,

) -> Response[Error | SubmitVrboGuestReviewResponse200]:
    r""" Rate a Vrbo guest

     Rate the guest of a Vrbo stay — Vrbo's \"Rate guest\", the counterpart of `PUT
    /v1/channels/airbnb/reviews/{id}`, and the same as `POST /v1/reviews/{id}/guest-review` on a Vrbo
    review. `rating` (overall, 1–5), `categoryRatings` (`cleanliness`, `communication`,
    `respect_house_rules`) and `isRevieweeRecommended` (would host again). Vrbo's rating has no text:
    `publicReview` / `privateFeedback` are refused when not empty. Publishing is final.

    `{id}` is the review `id` from `GET /v1/channels/vrbo/reviews?reviewerRole=host`; a review from
    another channel is `404`.

    Args:
        id (str):  Example: 181567.
        body (SubmitVrboGuestReviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SubmitVrboGuestReviewResponse200]
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitVrboGuestReviewBody,

) -> Error | SubmitVrboGuestReviewResponse200 | None:
    r""" Rate a Vrbo guest

     Rate the guest of a Vrbo stay — Vrbo's \"Rate guest\", the counterpart of `PUT
    /v1/channels/airbnb/reviews/{id}`, and the same as `POST /v1/reviews/{id}/guest-review` on a Vrbo
    review. `rating` (overall, 1–5), `categoryRatings` (`cleanliness`, `communication`,
    `respect_house_rules`) and `isRevieweeRecommended` (would host again). Vrbo's rating has no text:
    `publicReview` / `privateFeedback` are refused when not empty. Publishing is final.

    `{id}` is the review `id` from `GET /v1/channels/vrbo/reviews?reviewerRole=host`; a review from
    another channel is `404`.

    Args:
        id (str):  Example: 181567.
        body (SubmitVrboGuestReviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SubmitVrboGuestReviewResponse200
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitVrboGuestReviewBody,

) -> Response[Error | SubmitVrboGuestReviewResponse200]:
    r""" Rate a Vrbo guest

     Rate the guest of a Vrbo stay — Vrbo's \"Rate guest\", the counterpart of `PUT
    /v1/channels/airbnb/reviews/{id}`, and the same as `POST /v1/reviews/{id}/guest-review` on a Vrbo
    review. `rating` (overall, 1–5), `categoryRatings` (`cleanliness`, `communication`,
    `respect_house_rules`) and `isRevieweeRecommended` (would host again). Vrbo's rating has no text:
    `publicReview` / `privateFeedback` are refused when not empty. Publishing is final.

    `{id}` is the review `id` from `GET /v1/channels/vrbo/reviews?reviewerRole=host`; a review from
    another channel is `404`.

    Args:
        id (str):  Example: 181567.
        body (SubmitVrboGuestReviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SubmitVrboGuestReviewResponse200]
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SubmitVrboGuestReviewBody,

) -> Error | SubmitVrboGuestReviewResponse200 | None:
    r""" Rate a Vrbo guest

     Rate the guest of a Vrbo stay — Vrbo's \"Rate guest\", the counterpart of `PUT
    /v1/channels/airbnb/reviews/{id}`, and the same as `POST /v1/reviews/{id}/guest-review` on a Vrbo
    review. `rating` (overall, 1–5), `categoryRatings` (`cleanliness`, `communication`,
    `respect_house_rules`) and `isRevieweeRecommended` (would host again). Vrbo's rating has no text:
    `publicReview` / `privateFeedback` are refused when not empty. Publishing is final.

    `{id}` is the review `id` from `GET /v1/channels/vrbo/reviews?reviewerRole=host`; a review from
    another channel is `404`.

    Args:
        id (str):  Example: 181567.
        body (SubmitVrboGuestReviewBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SubmitVrboGuestReviewResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
