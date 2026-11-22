from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.pull_listing_from_vrbo_body import PullListingFromVrboBody
from ...models.pull_listing_from_vrbo_response_200 import PullListingFromVrboResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: PullListingFromVrboBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/{id}/pull/vrbo".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PullListingFromVrboResponse200 | None:
    if response.status_code == 200:
        response_200 = PullListingFromVrboResponse200.from_dict(response.json())



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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

    if response.status_code == 504:
        response_504 = Error.from_dict(response.json())



        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PullListingFromVrboResponse200]:
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
    body: PullListingFromVrboBody | Unset = UNSET,

) -> Response[Error | PullListingFromVrboResponse200]:
    """ Refresh a listing from Vrbo

     Re-read every content section of the listing's Vrbo listing from Vrbo and keep it as Repull's copy,
    then report what was refreshed and when — the counterpart of `POST /v1/listings/{id}/pull/airbnb`.
    Use it after the host changed something on Vrbo, so the `/v1/channels/vrbo/listings/{id}/…` reads
    answer with what Vrbo holds now.

    **What it refreshes:** descriptions, details, story, additional-info, photos, amenities, rooms,
    location, house-rules, booking-settings, cancellation, fees, pricing, payment-terms, protection,
    taxes, permits, checkin-guide, videos. **Not** the calendar, rates per night, bookings, messages,
    reviews or payouts — those arrive through the channel's own sync.

    **Runs synchronously:** about 45 Vrbo calls spaced ~3 s apart per account, **around 2.5 minutes**. A
    section Vrbo fails to return is listed in `failedSections`; the others are refreshed.

    **One pull per listing per 15 minutes**, as on Airbnb: a second call inside the window returns `429
    rate_limit_exceeded` with `Retry-After` and `nextPullAvailableAt`, and makes no Vrbo calls.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        body (PullListingFromVrboBody | Unset): Optional. Omit the body to pull the listing's Vrbo
            listing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PullListingFromVrboResponse200]
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
    body: PullListingFromVrboBody | Unset = UNSET,

) -> Error | PullListingFromVrboResponse200 | None:
    """ Refresh a listing from Vrbo

     Re-read every content section of the listing's Vrbo listing from Vrbo and keep it as Repull's copy,
    then report what was refreshed and when — the counterpart of `POST /v1/listings/{id}/pull/airbnb`.
    Use it after the host changed something on Vrbo, so the `/v1/channels/vrbo/listings/{id}/…` reads
    answer with what Vrbo holds now.

    **What it refreshes:** descriptions, details, story, additional-info, photos, amenities, rooms,
    location, house-rules, booking-settings, cancellation, fees, pricing, payment-terms, protection,
    taxes, permits, checkin-guide, videos. **Not** the calendar, rates per night, bookings, messages,
    reviews or payouts — those arrive through the channel's own sync.

    **Runs synchronously:** about 45 Vrbo calls spaced ~3 s apart per account, **around 2.5 minutes**. A
    section Vrbo fails to return is listed in `failedSections`; the others are refreshed.

    **One pull per listing per 15 minutes**, as on Airbnb: a second call inside the window returns `429
    rate_limit_exceeded` with `Retry-After` and `nextPullAvailableAt`, and makes no Vrbo calls.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        body (PullListingFromVrboBody | Unset): Optional. Omit the body to pull the listing's Vrbo
            listing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PullListingFromVrboResponse200
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
    body: PullListingFromVrboBody | Unset = UNSET,

) -> Response[Error | PullListingFromVrboResponse200]:
    """ Refresh a listing from Vrbo

     Re-read every content section of the listing's Vrbo listing from Vrbo and keep it as Repull's copy,
    then report what was refreshed and when — the counterpart of `POST /v1/listings/{id}/pull/airbnb`.
    Use it after the host changed something on Vrbo, so the `/v1/channels/vrbo/listings/{id}/…` reads
    answer with what Vrbo holds now.

    **What it refreshes:** descriptions, details, story, additional-info, photos, amenities, rooms,
    location, house-rules, booking-settings, cancellation, fees, pricing, payment-terms, protection,
    taxes, permits, checkin-guide, videos. **Not** the calendar, rates per night, bookings, messages,
    reviews or payouts — those arrive through the channel's own sync.

    **Runs synchronously:** about 45 Vrbo calls spaced ~3 s apart per account, **around 2.5 minutes**. A
    section Vrbo fails to return is listed in `failedSections`; the others are refreshed.

    **One pull per listing per 15 minutes**, as on Airbnb: a second call inside the window returns `429
    rate_limit_exceeded` with `Retry-After` and `nextPullAvailableAt`, and makes no Vrbo calls.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        body (PullListingFromVrboBody | Unset): Optional. Omit the body to pull the listing's Vrbo
            listing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PullListingFromVrboResponse200]
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
    body: PullListingFromVrboBody | Unset = UNSET,

) -> Error | PullListingFromVrboResponse200 | None:
    """ Refresh a listing from Vrbo

     Re-read every content section of the listing's Vrbo listing from Vrbo and keep it as Repull's copy,
    then report what was refreshed and when — the counterpart of `POST /v1/listings/{id}/pull/airbnb`.
    Use it after the host changed something on Vrbo, so the `/v1/channels/vrbo/listings/{id}/…` reads
    answer with what Vrbo holds now.

    **What it refreshes:** descriptions, details, story, additional-info, photos, amenities, rooms,
    location, house-rules, booking-settings, cancellation, fees, pricing, payment-terms, protection,
    taxes, permits, checkin-guide, videos. **Not** the calendar, rates per night, bookings, messages,
    reviews or payouts — those arrive through the channel's own sync.

    **Runs synchronously:** about 45 Vrbo calls spaced ~3 s apart per account, **around 2.5 minutes**. A
    section Vrbo fails to return is listed in `failedSections`; the others are refreshed.

    **One pull per listing per 15 minutes**, as on Airbnb: a second call inside the window returns `429
    rate_limit_exceeded` with `Retry-After` and `nextPullAvailableAt`, and makes no Vrbo calls.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        body (PullListingFromVrboBody | Unset): Optional. Omit the body to pull the listing's Vrbo
            listing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PullListingFromVrboResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
