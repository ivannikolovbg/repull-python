from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_review import AirbnbReview
from ...models.error import Error
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: AirbnbReview,

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

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

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
    body: AirbnbReview,

) -> Response[AirbnbReview | Error]:
    """ Edit Airbnb host review

     Edit a host-side review for an Airbnb stay. Airbnb collapses POST + PUT into the same upstream call
    (`PUT /v2/listing_reviews/{id}`), so this endpoint covers both initial submit and subsequent edits
    while the review window is open.

    Body is a partial `AirbnbReview` — pass the fields you want to change (rating, public review,
    private feedback, category ratings).

    Args:
        id (str):
        body (AirbnbReview): An Airbnb review (guest → host or host → guest).

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
    body: AirbnbReview,

) -> AirbnbReview | Error | None:
    """ Edit Airbnb host review

     Edit a host-side review for an Airbnb stay. Airbnb collapses POST + PUT into the same upstream call
    (`PUT /v2/listing_reviews/{id}`), so this endpoint covers both initial submit and subsequent edits
    while the review window is open.

    Body is a partial `AirbnbReview` — pass the fields you want to change (rating, public review,
    private feedback, category ratings).

    Args:
        id (str):
        body (AirbnbReview): An Airbnb review (guest → host or host → guest).

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
    body: AirbnbReview,

) -> Response[AirbnbReview | Error]:
    """ Edit Airbnb host review

     Edit a host-side review for an Airbnb stay. Airbnb collapses POST + PUT into the same upstream call
    (`PUT /v2/listing_reviews/{id}`), so this endpoint covers both initial submit and subsequent edits
    while the review window is open.

    Body is a partial `AirbnbReview` — pass the fields you want to change (rating, public review,
    private feedback, category ratings).

    Args:
        id (str):
        body (AirbnbReview): An Airbnb review (guest → host or host → guest).

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
    body: AirbnbReview,

) -> AirbnbReview | Error | None:
    """ Edit Airbnb host review

     Edit a host-side review for an Airbnb stay. Airbnb collapses POST + PUT into the same upstream call
    (`PUT /v2/listing_reviews/{id}`), so this endpoint covers both initial submit and subsequent edits
    while the review window is open.

    Body is a partial `AirbnbReview` — pass the fields you want to change (rating, public review,
    private feedback, category ratings).

    Args:
        id (str):
        body (AirbnbReview): An Airbnb review (guest → host or host → guest).

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
