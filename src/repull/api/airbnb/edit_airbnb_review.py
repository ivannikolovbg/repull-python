from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_host_review_submit import AirbnbHostReviewSubmit
from ...models.airbnb_review import AirbnbReview
from ...models.error import Error
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: AirbnbHostReviewSubmit,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/airbnb/reviews/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AirbnbReview | Error | None:
    if response.status_code == 200:
        response_200 = AirbnbReview.from_dict(response.json())



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

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AirbnbReview | Error]:
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
    body: AirbnbHostReviewSubmit,

) -> Response[AirbnbReview | Error]:
    r""" Submit your review of a guest (publishes, final)

     Submit your review of a guest — the review with `reviewerRole: \"host\"`. **Submitting publishes it
    and is final:** Airbnb has no draft and does not allow edits; a second submission is `409
    review_already_submitted`. Airbnb accepts it up to 14 days after checkout (`expiresAt`).

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
    reply to it with `POST /v1/channels/airbnb/reviews/{id}/respond`. After the window closes: `409
    review_window_closed`. Full guide: https://repull.dev/docs/channels/airbnb/reviews

    Args:
        id (str):
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
        Response[AirbnbReview | Error]
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
    body: AirbnbHostReviewSubmit,

) -> AirbnbReview | Error | None:
    r""" Submit your review of a guest (publishes, final)

     Submit your review of a guest — the review with `reviewerRole: \"host\"`. **Submitting publishes it
    and is final:** Airbnb has no draft and does not allow edits; a second submission is `409
    review_already_submitted`. Airbnb accepts it up to 14 days after checkout (`expiresAt`).

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
    reply to it with `POST /v1/channels/airbnb/reviews/{id}/respond`. After the window closes: `409
    review_window_closed`. Full guide: https://repull.dev/docs/channels/airbnb/reviews

    Args:
        id (str):
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
        AirbnbReview | Error
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
    body: AirbnbHostReviewSubmit,

) -> Response[AirbnbReview | Error]:
    r""" Submit your review of a guest (publishes, final)

     Submit your review of a guest — the review with `reviewerRole: \"host\"`. **Submitting publishes it
    and is final:** Airbnb has no draft and does not allow edits; a second submission is `409
    review_already_submitted`. Airbnb accepts it up to 14 days after checkout (`expiresAt`).

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
    reply to it with `POST /v1/channels/airbnb/reviews/{id}/respond`. After the window closes: `409
    review_window_closed`. Full guide: https://repull.dev/docs/channels/airbnb/reviews

    Args:
        id (str):
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
        Response[AirbnbReview | Error]
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
    body: AirbnbHostReviewSubmit,

) -> AirbnbReview | Error | None:
    r""" Submit your review of a guest (publishes, final)

     Submit your review of a guest — the review with `reviewerRole: \"host\"`. **Submitting publishes it
    and is final:** Airbnb has no draft and does not allow edits; a second submission is `409
    review_already_submitted`. Airbnb accepts it up to 14 days after checkout (`expiresAt`).

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
    reply to it with `POST /v1/channels/airbnb/reviews/{id}/respond`. After the window closes: `409
    review_window_closed`. Full guide: https://repull.dev/docs/channels/airbnb/reviews

    Args:
        id (str):
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
        AirbnbReview | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
