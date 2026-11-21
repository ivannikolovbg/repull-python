from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.publish_listing_to_vrbo_body import PublishListingToVrboBody
from ...models.publish_listing_to_vrbo_response_202 import PublishListingToVrboResponse202
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: PublishListingToVrboBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/{id}/publish/vrbo".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PublishListingToVrboResponse202 | None:
    if response.status_code == 202:
        response_202 = PublishListingToVrboResponse202.from_dict(response.json())



        return response_202

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PublishListingToVrboResponse202]:
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
    body: PublishListingToVrboBody | Unset = UNSET,

) -> Response[Error | PublishListingToVrboResponse202]:
    r""" Create or update a listing on Vrbo

     **A listing not yet on Vrbo** is created there; **a listing already linked to a Vrbo listing** gets
    its content pushed onto that listing (`mode: update`, below).

    Creates the listing on Vrbo in the host's connected Vrbo account, from the listing's content: title
    and description, property type, rooms and beds, amenities, photos, house rules (guests, minimum age,
    children, pets, smoking, events), check-in and check-out times, minimum stay, advance notice and
    booking window, the nightly price, cleaning, pet and extra-guest fees, the cancellation policy and
    the licence number. Vrbo's automatic new-listing discount is turned off so the listing sells at your
    prices.

    **It is a job.** Vrbo's onboarding takes 5–15 minutes (photos go up one at a time), so this answers
    `202` with `job.jobId`. Poll `GET /v1/listings/{id}/publish/vrbo?jobId=` for each finished step.
    When Vrbo has published the listing, that read links the new Vrbo unit to the listing with calendar
    sync on and queues the whole calendar (prices, availability, minimum stay) to Vrbo: **keep polling
    until `linked` is true.**

    **Which account.** A workspace with one Vrbo account needs nothing. With several, name it with
    `accountId` (`\"vrbo:13\"`, as the connection id). An account connected with messaging access is
    refused with `403 vrbo_messaging_access`.

    **Missing content** (street address, city, photos, nightly price, description) is refused with `422
    listing_incomplete` naming what is missing. A run that failed part-way leaves an unpublished Vrbo
    property: publishing again completes it instead of creating a second one.

    **Update (listing already on Vrbo).** Write the content with `PUT /v1/listings/{id}/content`, then
    publish: the listing's content is pushed onto its existing Vrbo listing, section by section —
    headline and description, property type, amenities, house rules (check-in/out, guests, children,
    pets, smoking, events), booking settings (instant book, minimum stay, notice, booking window),
    cancellation policy, cleaning/pet/extra-guest fees, the base rate (with the unit's markup) and the
    weekly and monthly stay discounts over the booking window (`rates`; the nights keep the prices Vrbo
    has). Rates and the base rate share Vrbo's calendar quota with the listing's calendar push: when it
    is writing, those steps wait for it (up to 3 minutes) and try once more, else they end `failed` with
    `vrbo_calendar_busy` — publish again later. Each write is partial (a field the content has no value
    for is left alone) and is read back from Vrbo. Rooms, photos and registration are not replaced on an
    existing listing (`skipped` says so): edit them with `PUT
    /v1/channels/vrbo/listings/{id}/{section}`. It is a job too (a few minutes: Vrbo calls are spaced ~3
    s apart per account): poll `GET ?jobId=` — each entry of `job.sections` has its `status`, Vrbo's
    refusals and what Vrbo stored. Limit it with `sections` (e.g. `[\"description\", \"fees\"]`); name
    the Vrbo listing with `vrboListingNumber` when the listing is linked to several. One push per
    listing at a time (`409 vrbo_push_running`). Needs full access (`403 vrbo_messaging_access`
    otherwise).

    Prices, availability and minimum stay per night always go through the calendar: `PUT
    /v1/availability/{propertyId}`.

    Args:
        id (int):
        body (PublishListingToVrboBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PublishListingToVrboResponse202]
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
    body: PublishListingToVrboBody | Unset = UNSET,

) -> Error | PublishListingToVrboResponse202 | None:
    r""" Create or update a listing on Vrbo

     **A listing not yet on Vrbo** is created there; **a listing already linked to a Vrbo listing** gets
    its content pushed onto that listing (`mode: update`, below).

    Creates the listing on Vrbo in the host's connected Vrbo account, from the listing's content: title
    and description, property type, rooms and beds, amenities, photos, house rules (guests, minimum age,
    children, pets, smoking, events), check-in and check-out times, minimum stay, advance notice and
    booking window, the nightly price, cleaning, pet and extra-guest fees, the cancellation policy and
    the licence number. Vrbo's automatic new-listing discount is turned off so the listing sells at your
    prices.

    **It is a job.** Vrbo's onboarding takes 5–15 minutes (photos go up one at a time), so this answers
    `202` with `job.jobId`. Poll `GET /v1/listings/{id}/publish/vrbo?jobId=` for each finished step.
    When Vrbo has published the listing, that read links the new Vrbo unit to the listing with calendar
    sync on and queues the whole calendar (prices, availability, minimum stay) to Vrbo: **keep polling
    until `linked` is true.**

    **Which account.** A workspace with one Vrbo account needs nothing. With several, name it with
    `accountId` (`\"vrbo:13\"`, as the connection id). An account connected with messaging access is
    refused with `403 vrbo_messaging_access`.

    **Missing content** (street address, city, photos, nightly price, description) is refused with `422
    listing_incomplete` naming what is missing. A run that failed part-way leaves an unpublished Vrbo
    property: publishing again completes it instead of creating a second one.

    **Update (listing already on Vrbo).** Write the content with `PUT /v1/listings/{id}/content`, then
    publish: the listing's content is pushed onto its existing Vrbo listing, section by section —
    headline and description, property type, amenities, house rules (check-in/out, guests, children,
    pets, smoking, events), booking settings (instant book, minimum stay, notice, booking window),
    cancellation policy, cleaning/pet/extra-guest fees, the base rate (with the unit's markup) and the
    weekly and monthly stay discounts over the booking window (`rates`; the nights keep the prices Vrbo
    has). Rates and the base rate share Vrbo's calendar quota with the listing's calendar push: when it
    is writing, those steps wait for it (up to 3 minutes) and try once more, else they end `failed` with
    `vrbo_calendar_busy` — publish again later. Each write is partial (a field the content has no value
    for is left alone) and is read back from Vrbo. Rooms, photos and registration are not replaced on an
    existing listing (`skipped` says so): edit them with `PUT
    /v1/channels/vrbo/listings/{id}/{section}`. It is a job too (a few minutes: Vrbo calls are spaced ~3
    s apart per account): poll `GET ?jobId=` — each entry of `job.sections` has its `status`, Vrbo's
    refusals and what Vrbo stored. Limit it with `sections` (e.g. `[\"description\", \"fees\"]`); name
    the Vrbo listing with `vrboListingNumber` when the listing is linked to several. One push per
    listing at a time (`409 vrbo_push_running`). Needs full access (`403 vrbo_messaging_access`
    otherwise).

    Prices, availability and minimum stay per night always go through the calendar: `PUT
    /v1/availability/{propertyId}`.

    Args:
        id (int):
        body (PublishListingToVrboBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PublishListingToVrboResponse202
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
    body: PublishListingToVrboBody | Unset = UNSET,

) -> Response[Error | PublishListingToVrboResponse202]:
    r""" Create or update a listing on Vrbo

     **A listing not yet on Vrbo** is created there; **a listing already linked to a Vrbo listing** gets
    its content pushed onto that listing (`mode: update`, below).

    Creates the listing on Vrbo in the host's connected Vrbo account, from the listing's content: title
    and description, property type, rooms and beds, amenities, photos, house rules (guests, minimum age,
    children, pets, smoking, events), check-in and check-out times, minimum stay, advance notice and
    booking window, the nightly price, cleaning, pet and extra-guest fees, the cancellation policy and
    the licence number. Vrbo's automatic new-listing discount is turned off so the listing sells at your
    prices.

    **It is a job.** Vrbo's onboarding takes 5–15 minutes (photos go up one at a time), so this answers
    `202` with `job.jobId`. Poll `GET /v1/listings/{id}/publish/vrbo?jobId=` for each finished step.
    When Vrbo has published the listing, that read links the new Vrbo unit to the listing with calendar
    sync on and queues the whole calendar (prices, availability, minimum stay) to Vrbo: **keep polling
    until `linked` is true.**

    **Which account.** A workspace with one Vrbo account needs nothing. With several, name it with
    `accountId` (`\"vrbo:13\"`, as the connection id). An account connected with messaging access is
    refused with `403 vrbo_messaging_access`.

    **Missing content** (street address, city, photos, nightly price, description) is refused with `422
    listing_incomplete` naming what is missing. A run that failed part-way leaves an unpublished Vrbo
    property: publishing again completes it instead of creating a second one.

    **Update (listing already on Vrbo).** Write the content with `PUT /v1/listings/{id}/content`, then
    publish: the listing's content is pushed onto its existing Vrbo listing, section by section —
    headline and description, property type, amenities, house rules (check-in/out, guests, children,
    pets, smoking, events), booking settings (instant book, minimum stay, notice, booking window),
    cancellation policy, cleaning/pet/extra-guest fees, the base rate (with the unit's markup) and the
    weekly and monthly stay discounts over the booking window (`rates`; the nights keep the prices Vrbo
    has). Rates and the base rate share Vrbo's calendar quota with the listing's calendar push: when it
    is writing, those steps wait for it (up to 3 minutes) and try once more, else they end `failed` with
    `vrbo_calendar_busy` — publish again later. Each write is partial (a field the content has no value
    for is left alone) and is read back from Vrbo. Rooms, photos and registration are not replaced on an
    existing listing (`skipped` says so): edit them with `PUT
    /v1/channels/vrbo/listings/{id}/{section}`. It is a job too (a few minutes: Vrbo calls are spaced ~3
    s apart per account): poll `GET ?jobId=` — each entry of `job.sections` has its `status`, Vrbo's
    refusals and what Vrbo stored. Limit it with `sections` (e.g. `[\"description\", \"fees\"]`); name
    the Vrbo listing with `vrboListingNumber` when the listing is linked to several. One push per
    listing at a time (`409 vrbo_push_running`). Needs full access (`403 vrbo_messaging_access`
    otherwise).

    Prices, availability and minimum stay per night always go through the calendar: `PUT
    /v1/availability/{propertyId}`.

    Args:
        id (int):
        body (PublishListingToVrboBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PublishListingToVrboResponse202]
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
    body: PublishListingToVrboBody | Unset = UNSET,

) -> Error | PublishListingToVrboResponse202 | None:
    r""" Create or update a listing on Vrbo

     **A listing not yet on Vrbo** is created there; **a listing already linked to a Vrbo listing** gets
    its content pushed onto that listing (`mode: update`, below).

    Creates the listing on Vrbo in the host's connected Vrbo account, from the listing's content: title
    and description, property type, rooms and beds, amenities, photos, house rules (guests, minimum age,
    children, pets, smoking, events), check-in and check-out times, minimum stay, advance notice and
    booking window, the nightly price, cleaning, pet and extra-guest fees, the cancellation policy and
    the licence number. Vrbo's automatic new-listing discount is turned off so the listing sells at your
    prices.

    **It is a job.** Vrbo's onboarding takes 5–15 minutes (photos go up one at a time), so this answers
    `202` with `job.jobId`. Poll `GET /v1/listings/{id}/publish/vrbo?jobId=` for each finished step.
    When Vrbo has published the listing, that read links the new Vrbo unit to the listing with calendar
    sync on and queues the whole calendar (prices, availability, minimum stay) to Vrbo: **keep polling
    until `linked` is true.**

    **Which account.** A workspace with one Vrbo account needs nothing. With several, name it with
    `accountId` (`\"vrbo:13\"`, as the connection id). An account connected with messaging access is
    refused with `403 vrbo_messaging_access`.

    **Missing content** (street address, city, photos, nightly price, description) is refused with `422
    listing_incomplete` naming what is missing. A run that failed part-way leaves an unpublished Vrbo
    property: publishing again completes it instead of creating a second one.

    **Update (listing already on Vrbo).** Write the content with `PUT /v1/listings/{id}/content`, then
    publish: the listing's content is pushed onto its existing Vrbo listing, section by section —
    headline and description, property type, amenities, house rules (check-in/out, guests, children,
    pets, smoking, events), booking settings (instant book, minimum stay, notice, booking window),
    cancellation policy, cleaning/pet/extra-guest fees, the base rate (with the unit's markup) and the
    weekly and monthly stay discounts over the booking window (`rates`; the nights keep the prices Vrbo
    has). Rates and the base rate share Vrbo's calendar quota with the listing's calendar push: when it
    is writing, those steps wait for it (up to 3 minutes) and try once more, else they end `failed` with
    `vrbo_calendar_busy` — publish again later. Each write is partial (a field the content has no value
    for is left alone) and is read back from Vrbo. Rooms, photos and registration are not replaced on an
    existing listing (`skipped` says so): edit them with `PUT
    /v1/channels/vrbo/listings/{id}/{section}`. It is a job too (a few minutes: Vrbo calls are spaced ~3
    s apart per account): poll `GET ?jobId=` — each entry of `job.sections` has its `status`, Vrbo's
    refusals and what Vrbo stored. Limit it with `sections` (e.g. `[\"description\", \"fees\"]`); name
    the Vrbo listing with `vrboListingNumber` when the listing is linked to several. One push per
    listing at a time (`409 vrbo_push_running`). Needs full access (`403 vrbo_messaging_access`
    otherwise).

    Prices, availability and minimum stay per night always go through the calendar: `PUT
    /v1/availability/{propertyId}`.

    Args:
        id (int):
        body (PublishListingToVrboBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PublishListingToVrboResponse202
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
