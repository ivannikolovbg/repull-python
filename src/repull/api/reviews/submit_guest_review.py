from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_host_review_submit import AirbnbHostReviewSubmit
from ...models.error import Error
from ...models.submit_guest_review_response_200 import SubmitGuestReviewResponse200
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: AirbnbHostReviewSubmit,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/reviews/{id}/guest-review".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SubmitGuestReviewResponse200 | None:
    if response.status_code == 200:
        response_200 = SubmitGuestReviewResponse200.from_dict(response.json())



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

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SubmitGuestReviewResponse200]:
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
    body: AirbnbHostReviewSubmit,

) -> Response[Error | SubmitGuestReviewResponse200]:
    r""" Review a guest (publishes, final)

     Submit your review of a guest — a review with `reviewerRole: \"host\"` from `GET
    /v1/reviews?reviewerRole=host`. Only Airbnb lets hosts review guests; a review from another channel
    returns `422 unsupported_channel`.

    **Submitting publishes it and is final:** Airbnb has no draft and does not allow edits; a second
    submission is `409 review_already_submitted`. Airbnb accepts it up to 14 days after checkout
    (`expiresAt`); after that, `409 review_window_closed`.

    Required: `publicReview`, `isRevieweeRecommended` (whether you would host the guest again), and a
    1–5 rating for **each** of `cleanliness`, `communication` and `respect_house_rules` — send `rating`
    to use one score for all three, `categoryRatings` to score them individually, or both (`rating`
    fills any category you did not rate). Optional: `privateFeedback`, a note to the guest that is not
    published. A request missing a required piece is refused with `422 invalid_params` naming it, before
    anything is sent to Airbnb.

    ```json
    {
      \"publicReview\": \"Joanne was a great guest.\",
      \"rating\": 5,
      \"privateFeedback\": \"Thanks for leaving the place so tidy!\",
      \"isRevieweeRecommended\": true
    }
    ```

    A guest's review of you (`reviewerRole: \"guest\"`) cannot be written here — `409 not_host_review`;
    answer it with `POST /v1/reviews/{id}/reply`. Same behaviour as `PUT
    /v1/channels/airbnb/reviews/{id}`. Guide: https://repull.dev/docs/reviews#review-a-guest

    Args:
        id (int):
        body (AirbnbHostReviewSubmit): Your review of a guest. Airbnb requires `publicReview`,
            `isRevieweeRecommended`, and a rating for each of cleanliness, communication and
            respect_house_rules — through `rating`, `categoryRatings`, or both. Submitting publishes
            it and is final. Example: {'publicReview': 'Joanne was a great guest. The space was kept
            clean and communication was clear.', 'rating': 5, 'categoryRatings': [{'category':
            'cleanliness', 'rating': 5, 'comment': 'Left it spotless'}], 'privateFeedback': 'Thanks
            for being such a considerate guest!', 'isRevieweeRecommended': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SubmitGuestReviewResponse200]
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
    body: AirbnbHostReviewSubmit,

) -> Error | SubmitGuestReviewResponse200 | None:
    r""" Review a guest (publishes, final)

     Submit your review of a guest — a review with `reviewerRole: \"host\"` from `GET
    /v1/reviews?reviewerRole=host`. Only Airbnb lets hosts review guests; a review from another channel
    returns `422 unsupported_channel`.

    **Submitting publishes it and is final:** Airbnb has no draft and does not allow edits; a second
    submission is `409 review_already_submitted`. Airbnb accepts it up to 14 days after checkout
    (`expiresAt`); after that, `409 review_window_closed`.

    Required: `publicReview`, `isRevieweeRecommended` (whether you would host the guest again), and a
    1–5 rating for **each** of `cleanliness`, `communication` and `respect_house_rules` — send `rating`
    to use one score for all three, `categoryRatings` to score them individually, or both (`rating`
    fills any category you did not rate). Optional: `privateFeedback`, a note to the guest that is not
    published. A request missing a required piece is refused with `422 invalid_params` naming it, before
    anything is sent to Airbnb.

    ```json
    {
      \"publicReview\": \"Joanne was a great guest.\",
      \"rating\": 5,
      \"privateFeedback\": \"Thanks for leaving the place so tidy!\",
      \"isRevieweeRecommended\": true
    }
    ```

    A guest's review of you (`reviewerRole: \"guest\"`) cannot be written here — `409 not_host_review`;
    answer it with `POST /v1/reviews/{id}/reply`. Same behaviour as `PUT
    /v1/channels/airbnb/reviews/{id}`. Guide: https://repull.dev/docs/reviews#review-a-guest

    Args:
        id (int):
        body (AirbnbHostReviewSubmit): Your review of a guest. Airbnb requires `publicReview`,
            `isRevieweeRecommended`, and a rating for each of cleanliness, communication and
            respect_house_rules — through `rating`, `categoryRatings`, or both. Submitting publishes
            it and is final. Example: {'publicReview': 'Joanne was a great guest. The space was kept
            clean and communication was clear.', 'rating': 5, 'categoryRatings': [{'category':
            'cleanliness', 'rating': 5, 'comment': 'Left it spotless'}], 'privateFeedback': 'Thanks
            for being such a considerate guest!', 'isRevieweeRecommended': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SubmitGuestReviewResponse200
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
    body: AirbnbHostReviewSubmit,

) -> Response[Error | SubmitGuestReviewResponse200]:
    r""" Review a guest (publishes, final)

     Submit your review of a guest — a review with `reviewerRole: \"host\"` from `GET
    /v1/reviews?reviewerRole=host`. Only Airbnb lets hosts review guests; a review from another channel
    returns `422 unsupported_channel`.

    **Submitting publishes it and is final:** Airbnb has no draft and does not allow edits; a second
    submission is `409 review_already_submitted`. Airbnb accepts it up to 14 days after checkout
    (`expiresAt`); after that, `409 review_window_closed`.

    Required: `publicReview`, `isRevieweeRecommended` (whether you would host the guest again), and a
    1–5 rating for **each** of `cleanliness`, `communication` and `respect_house_rules` — send `rating`
    to use one score for all three, `categoryRatings` to score them individually, or both (`rating`
    fills any category you did not rate). Optional: `privateFeedback`, a note to the guest that is not
    published. A request missing a required piece is refused with `422 invalid_params` naming it, before
    anything is sent to Airbnb.

    ```json
    {
      \"publicReview\": \"Joanne was a great guest.\",
      \"rating\": 5,
      \"privateFeedback\": \"Thanks for leaving the place so tidy!\",
      \"isRevieweeRecommended\": true
    }
    ```

    A guest's review of you (`reviewerRole: \"guest\"`) cannot be written here — `409 not_host_review`;
    answer it with `POST /v1/reviews/{id}/reply`. Same behaviour as `PUT
    /v1/channels/airbnb/reviews/{id}`. Guide: https://repull.dev/docs/reviews#review-a-guest

    Args:
        id (int):
        body (AirbnbHostReviewSubmit): Your review of a guest. Airbnb requires `publicReview`,
            `isRevieweeRecommended`, and a rating for each of cleanliness, communication and
            respect_house_rules — through `rating`, `categoryRatings`, or both. Submitting publishes
            it and is final. Example: {'publicReview': 'Joanne was a great guest. The space was kept
            clean and communication was clear.', 'rating': 5, 'categoryRatings': [{'category':
            'cleanliness', 'rating': 5, 'comment': 'Left it spotless'}], 'privateFeedback': 'Thanks
            for being such a considerate guest!', 'isRevieweeRecommended': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SubmitGuestReviewResponse200]
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
    body: AirbnbHostReviewSubmit,

) -> Error | SubmitGuestReviewResponse200 | None:
    r""" Review a guest (publishes, final)

     Submit your review of a guest — a review with `reviewerRole: \"host\"` from `GET
    /v1/reviews?reviewerRole=host`. Only Airbnb lets hosts review guests; a review from another channel
    returns `422 unsupported_channel`.

    **Submitting publishes it and is final:** Airbnb has no draft and does not allow edits; a second
    submission is `409 review_already_submitted`. Airbnb accepts it up to 14 days after checkout
    (`expiresAt`); after that, `409 review_window_closed`.

    Required: `publicReview`, `isRevieweeRecommended` (whether you would host the guest again), and a
    1–5 rating for **each** of `cleanliness`, `communication` and `respect_house_rules` — send `rating`
    to use one score for all three, `categoryRatings` to score them individually, or both (`rating`
    fills any category you did not rate). Optional: `privateFeedback`, a note to the guest that is not
    published. A request missing a required piece is refused with `422 invalid_params` naming it, before
    anything is sent to Airbnb.

    ```json
    {
      \"publicReview\": \"Joanne was a great guest.\",
      \"rating\": 5,
      \"privateFeedback\": \"Thanks for leaving the place so tidy!\",
      \"isRevieweeRecommended\": true
    }
    ```

    A guest's review of you (`reviewerRole: \"guest\"`) cannot be written here — `409 not_host_review`;
    answer it with `POST /v1/reviews/{id}/reply`. Same behaviour as `PUT
    /v1/channels/airbnb/reviews/{id}`. Guide: https://repull.dev/docs/reviews#review-a-guest

    Args:
        id (int):
        body (AirbnbHostReviewSubmit): Your review of a guest. Airbnb requires `publicReview`,
            `isRevieweeRecommended`, and a rating for each of cleanliness, communication and
            respect_house_rules — through `rating`, `categoryRatings`, or both. Submitting publishes
            it and is final. Example: {'publicReview': 'Joanne was a great guest. The space was kept
            clean and communication was clear.', 'rating': 5, 'categoryRatings': [{'category':
            'cleanliness', 'rating': 5, 'comment': 'Left it spotless'}], 'privateFeedback': 'Thanks
            for being such a considerate guest!', 'isRevieweeRecommended': True}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SubmitGuestReviewResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
