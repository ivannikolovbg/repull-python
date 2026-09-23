from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.listing_pull_airbnb_request import ListingPullAirbnbRequest
from ...models.listing_pull_response import ListingPullResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ListingPullAirbnbRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/{id}/pull/airbnb".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListingPullResponse | None:
    if response.status_code == 200:
        response_200 = ListingPullResponse.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListingPullResponse]:
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
    body: ListingPullAirbnbRequest | Unset = UNSET,

) -> Response[Error | ListingPullResponse]:
    """ Refresh a listing from Airbnb

     Re-read this listing from Airbnb and update your stored copy, then report what was refreshed and
    when. The mirror image of `POST /v1/listings/{id}/publish/airbnb`.

    Every other Airbnb read on this API is served from our database. This endpoint is the one that goes
    and asks Airbnb — use it after a push, to see the values Airbnb actually kept, or when a host has
    changed something in the Airbnb app.

    **What it refreshes:** basic listing facts (property type, bedrooms, beds, bathrooms, capacity),
    descriptions, photos, rooms and beds, amenities, booking settings (check-in/check-out windows, guest
    controls, cancellation policy), stay rules (min/max nights, advance-booking window, turnover
    buffer), pricing settings and standard fees, permits, checkout tasks and the check-in guide. After
    it returns, those values are what `GET /v1/listings/{id}?include=content,details` and the
    `/v1/channels/airbnb/**` routes serve.

    **What it does NOT refresh:** the calendar (nightly rates and availability — see `GET
    /v1/channels/airbnb/listings/{id}/availability`), reservations, messages, reviews or payouts. Those
    arrive continuously through the channel's own sync and never need a manual pull.

    **Runs synchronously** — the response is the result, not a job id. Expect several seconds.

    **One pull per listing per 15 minutes.** A pull is roughly a dozen Airbnb calls; a second call
    inside the window returns `429 rate_limit_exceeded` with `Retry-After` and `nextPullAvailableAt`,
    and makes no Airbnb calls. Two simultaneous calls cannot both run.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        body (ListingPullAirbnbRequest | Unset): Optional. Omit the body entirely to pull through
            the listing's primary Airbnb connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingPullResponse]
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
    body: ListingPullAirbnbRequest | Unset = UNSET,

) -> Error | ListingPullResponse | None:
    """ Refresh a listing from Airbnb

     Re-read this listing from Airbnb and update your stored copy, then report what was refreshed and
    when. The mirror image of `POST /v1/listings/{id}/publish/airbnb`.

    Every other Airbnb read on this API is served from our database. This endpoint is the one that goes
    and asks Airbnb — use it after a push, to see the values Airbnb actually kept, or when a host has
    changed something in the Airbnb app.

    **What it refreshes:** basic listing facts (property type, bedrooms, beds, bathrooms, capacity),
    descriptions, photos, rooms and beds, amenities, booking settings (check-in/check-out windows, guest
    controls, cancellation policy), stay rules (min/max nights, advance-booking window, turnover
    buffer), pricing settings and standard fees, permits, checkout tasks and the check-in guide. After
    it returns, those values are what `GET /v1/listings/{id}?include=content,details` and the
    `/v1/channels/airbnb/**` routes serve.

    **What it does NOT refresh:** the calendar (nightly rates and availability — see `GET
    /v1/channels/airbnb/listings/{id}/availability`), reservations, messages, reviews or payouts. Those
    arrive continuously through the channel's own sync and never need a manual pull.

    **Runs synchronously** — the response is the result, not a job id. Expect several seconds.

    **One pull per listing per 15 minutes.** A pull is roughly a dozen Airbnb calls; a second call
    inside the window returns `429 rate_limit_exceeded` with `Retry-After` and `nextPullAvailableAt`,
    and makes no Airbnb calls. Two simultaneous calls cannot both run.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        body (ListingPullAirbnbRequest | Unset): Optional. Omit the body entirely to pull through
            the listing's primary Airbnb connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingPullResponse
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
    body: ListingPullAirbnbRequest | Unset = UNSET,

) -> Response[Error | ListingPullResponse]:
    """ Refresh a listing from Airbnb

     Re-read this listing from Airbnb and update your stored copy, then report what was refreshed and
    when. The mirror image of `POST /v1/listings/{id}/publish/airbnb`.

    Every other Airbnb read on this API is served from our database. This endpoint is the one that goes
    and asks Airbnb — use it after a push, to see the values Airbnb actually kept, or when a host has
    changed something in the Airbnb app.

    **What it refreshes:** basic listing facts (property type, bedrooms, beds, bathrooms, capacity),
    descriptions, photos, rooms and beds, amenities, booking settings (check-in/check-out windows, guest
    controls, cancellation policy), stay rules (min/max nights, advance-booking window, turnover
    buffer), pricing settings and standard fees, permits, checkout tasks and the check-in guide. After
    it returns, those values are what `GET /v1/listings/{id}?include=content,details` and the
    `/v1/channels/airbnb/**` routes serve.

    **What it does NOT refresh:** the calendar (nightly rates and availability — see `GET
    /v1/channels/airbnb/listings/{id}/availability`), reservations, messages, reviews or payouts. Those
    arrive continuously through the channel's own sync and never need a manual pull.

    **Runs synchronously** — the response is the result, not a job id. Expect several seconds.

    **One pull per listing per 15 minutes.** A pull is roughly a dozen Airbnb calls; a second call
    inside the window returns `429 rate_limit_exceeded` with `Retry-After` and `nextPullAvailableAt`,
    and makes no Airbnb calls. Two simultaneous calls cannot both run.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        body (ListingPullAirbnbRequest | Unset): Optional. Omit the body entirely to pull through
            the listing's primary Airbnb connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingPullResponse]
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
    body: ListingPullAirbnbRequest | Unset = UNSET,

) -> Error | ListingPullResponse | None:
    """ Refresh a listing from Airbnb

     Re-read this listing from Airbnb and update your stored copy, then report what was refreshed and
    when. The mirror image of `POST /v1/listings/{id}/publish/airbnb`.

    Every other Airbnb read on this API is served from our database. This endpoint is the one that goes
    and asks Airbnb — use it after a push, to see the values Airbnb actually kept, or when a host has
    changed something in the Airbnb app.

    **What it refreshes:** basic listing facts (property type, bedrooms, beds, bathrooms, capacity),
    descriptions, photos, rooms and beds, amenities, booking settings (check-in/check-out windows, guest
    controls, cancellation policy), stay rules (min/max nights, advance-booking window, turnover
    buffer), pricing settings and standard fees, permits, checkout tasks and the check-in guide. After
    it returns, those values are what `GET /v1/listings/{id}?include=content,details` and the
    `/v1/channels/airbnb/**` routes serve.

    **What it does NOT refresh:** the calendar (nightly rates and availability — see `GET
    /v1/channels/airbnb/listings/{id}/availability`), reservations, messages, reviews or payouts. Those
    arrive continuously through the channel's own sync and never need a manual pull.

    **Runs synchronously** — the response is the result, not a job id. Expect several seconds.

    **One pull per listing per 15 minutes.** A pull is roughly a dozen Airbnb calls; a second call
    inside the window returns `429 rate_limit_exceeded` with `Retry-After` and `nextPullAvailableAt`,
    and makes no Airbnb calls. Two simultaneous calls cannot both run.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        body (ListingPullAirbnbRequest | Unset): Optional. Omit the body entirely to pull through
            the listing's primary Airbnb connection.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingPullResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
