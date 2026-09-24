from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_setup_body import BookingSetupBody
from ...models.error import Error
from typing import cast



def _get_kwargs(
    *,
    body: BookingSetupBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/booking/setup",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BookingSetupBody,

) -> Response[Any | Error]:
    r""" Booking.com property setup actions

     Action-router for putting a property onto Booking.com — including building one from nothing. Select
    the step with `action`.

    ## Opening a property

    - `create-property` — create a NEW Booking.com property for a Repull listing (`listing_id`). Creates
    the property, its first room with the listing's beds, a rate plan and the room-rate product that
    makes the room sellable (under the listing's cancellation policy), sets the contact and invoice
    details and the facilities, seeds availability and rates, syncs the calendar, then runs
    Booking.com's readiness check and reports what still blocks opening in `warnings`. Send `contact`
    (`name`, `email`, `phone` in international form); without it the workspace owner is used, and a
    workspace with no usable contact is refused before anything is created. Returns 201.
    - `add-room` — add another room type (and its sellable product) to a property (`listing_id`,
    `property_id`). Returns 201.
    - `add-unit` — raise the number of identical units on an existing room (`listing_id`, `property_id`,
    `room_id`).
    - `advance` — run Booking.com's readiness check for a property (`property_id`) and, when it passes,
    open it. Returns `checked`, `opened`, `sellable` and `blockers` — Booking.com's own reasons it
    cannot open yet.

    ## Account and policy steps

    - `create-legal-entity` — register a legal entity directly (returns 201). Not normally needed: see
    the legal-entity rules below.
    - `check-legal-status` — always `404`. A legal entity's details are readable for any id on the
    connectivity-provider credentials every workspace shares, and nothing records which workspace
    registered which entity, so no entity can be shown to be yours. `create-property` resolves it for
    you.
    - `check-readiness` — whether a property is ready to open (`property_id`): `ready` and `blockers`,
    without trying to open it.
    - `open-property` — open the property for sale (`property_id`). Refused with `422 booking_rejected`
    naming the blockers when it is not ready.
    - `set-contacts` — set property contacts (`property_id`, `contacts` in Booking.com's Contacts API
    shape; at most one carries the `general` profile).
    - `set-policies` — add a cancellation policy (`property_id`, `policyCode`, optional
    `prepaymentRequired`). House rules, pets, children and the damage deposit are `POST
    /v1/channels/booking/content` with `type: \"settings\"`.

    ## Three things about Booking.com that cost real money

    **A newly created property is NOT sellable.** Booking.com opens it only when its readiness check
    passes, and the check names what is missing — a main photo still processing, no availability, a
    licence the region requires. The response always reports `status: \"being_built\"` and `sellable:
    false`, never a guess, with the reasons in `warnings`. Resolve them, then `advance`.

    **A room with no ACTIVE rate plan is invisible.** Booking only renders rooms that have at least one
    active product linkage (room × rate plan). A room can be created successfully, return a `roomId`,
    and never appear on the property page. If `rateId` comes back `null` from `create-property` or `add-
    room`, that is exactly what happened: activate a rate plan on the property in the Extranet, then add
    the room again.

    **Room names are Booking.com's.** Travellers see one of Booking.com's standard names (\"Two-Bedroom
    Apartment\"), chosen from the listing's bedrooms. The listing's own name is kept as the operator-
    side reference, never shown to guests.

    ## The legal entity is resolved, not asked for

    A property is created against the legal entity Booking.com contracts with, invoices and pays. You do
    not normally send one:

    1. If this workspace already creates properties under a legal entity, that one is reused. A second
    is never registered.
    2. If it has none and the request carries `legal_entity` (`company_name`, `legal_contact_name`,
    `legal_contact_email`), one is registered and used. Booking.com emails the legal contact a contract;
    creation only succeeds once it is signed.
    3. If it has none and no `legal_entity`, the request is refused with `422 legal_entity_required`
    naming the fields — a contracted company is never invented.

    `legal_entity_id` overrides all of that. An id that already carries another workspace's properties
    is refused with `403 legal_entity_not_yours` before anything is created.

    ## What you do not control

    Properties are created against Booking's **production** target only. A test-target property cannot
    be sold through and there is no route back from one, so `target` is not a parameter — sending it
    changes nothing.

    The property category comes from the listing's property type (Apartment when it has none; Holiday
    home, Villa or Chalet when it says so). The initial room count is 1. Latitude and longitude come
    from the listing and are adjusted slightly to clear Booking.com's duplicate detection — send the
    property's true position on the listing and do not pre-adjust it yourself.

    The listing's name, check-in/check-out times, currency, capacity and price come from the listing.
    Its postal code is taken from the listing's own `postalCode`; when the listing has none, it falls
    back to a connected Airbnb listing. A listing with neither is created without a postal code, so set
    `postalCode` on the listing first.

    ## Guards

    Every action that takes a `property_id` requires a property connected to this workspace; any other
    id returns `404 not_found`. Every action that takes a `listing_id` requires a listing in this
    workspace; any other id returns `404 not_found`.

    `create-property` refuses a listing with no coordinates (`422 missing_coordinates`) before anything
    is created — creating a Booking.com property cannot be undone.

    `create-property` is subject to the same published-listing gate as the dashboard: no plan, or the
    plan's listing limit reached, returns `403 billing_error` with `used` and `limit`, and nothing is
    created.

    Returns `403 listing_inactive` when the listing — or any listing mapped to the Booking.com property
    — is inactive. An inactive listing keeps syncing, but cannot be read or changed through the API
    until it is activated.

    If a property is created and a later step fails, the response is `422 booking_create_partial`
    carrying `property_id`. The property EXISTS. Do not retry `create-property`, which would open a
    second one — continue with `add-room` and `advance`.

    Args:
        body (BookingSetupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    body: BookingSetupBody,

) -> Any | Error | None:
    r""" Booking.com property setup actions

     Action-router for putting a property onto Booking.com — including building one from nothing. Select
    the step with `action`.

    ## Opening a property

    - `create-property` — create a NEW Booking.com property for a Repull listing (`listing_id`). Creates
    the property, its first room with the listing's beds, a rate plan and the room-rate product that
    makes the room sellable (under the listing's cancellation policy), sets the contact and invoice
    details and the facilities, seeds availability and rates, syncs the calendar, then runs
    Booking.com's readiness check and reports what still blocks opening in `warnings`. Send `contact`
    (`name`, `email`, `phone` in international form); without it the workspace owner is used, and a
    workspace with no usable contact is refused before anything is created. Returns 201.
    - `add-room` — add another room type (and its sellable product) to a property (`listing_id`,
    `property_id`). Returns 201.
    - `add-unit` — raise the number of identical units on an existing room (`listing_id`, `property_id`,
    `room_id`).
    - `advance` — run Booking.com's readiness check for a property (`property_id`) and, when it passes,
    open it. Returns `checked`, `opened`, `sellable` and `blockers` — Booking.com's own reasons it
    cannot open yet.

    ## Account and policy steps

    - `create-legal-entity` — register a legal entity directly (returns 201). Not normally needed: see
    the legal-entity rules below.
    - `check-legal-status` — always `404`. A legal entity's details are readable for any id on the
    connectivity-provider credentials every workspace shares, and nothing records which workspace
    registered which entity, so no entity can be shown to be yours. `create-property` resolves it for
    you.
    - `check-readiness` — whether a property is ready to open (`property_id`): `ready` and `blockers`,
    without trying to open it.
    - `open-property` — open the property for sale (`property_id`). Refused with `422 booking_rejected`
    naming the blockers when it is not ready.
    - `set-contacts` — set property contacts (`property_id`, `contacts` in Booking.com's Contacts API
    shape; at most one carries the `general` profile).
    - `set-policies` — add a cancellation policy (`property_id`, `policyCode`, optional
    `prepaymentRequired`). House rules, pets, children and the damage deposit are `POST
    /v1/channels/booking/content` with `type: \"settings\"`.

    ## Three things about Booking.com that cost real money

    **A newly created property is NOT sellable.** Booking.com opens it only when its readiness check
    passes, and the check names what is missing — a main photo still processing, no availability, a
    licence the region requires. The response always reports `status: \"being_built\"` and `sellable:
    false`, never a guess, with the reasons in `warnings`. Resolve them, then `advance`.

    **A room with no ACTIVE rate plan is invisible.** Booking only renders rooms that have at least one
    active product linkage (room × rate plan). A room can be created successfully, return a `roomId`,
    and never appear on the property page. If `rateId` comes back `null` from `create-property` or `add-
    room`, that is exactly what happened: activate a rate plan on the property in the Extranet, then add
    the room again.

    **Room names are Booking.com's.** Travellers see one of Booking.com's standard names (\"Two-Bedroom
    Apartment\"), chosen from the listing's bedrooms. The listing's own name is kept as the operator-
    side reference, never shown to guests.

    ## The legal entity is resolved, not asked for

    A property is created against the legal entity Booking.com contracts with, invoices and pays. You do
    not normally send one:

    1. If this workspace already creates properties under a legal entity, that one is reused. A second
    is never registered.
    2. If it has none and the request carries `legal_entity` (`company_name`, `legal_contact_name`,
    `legal_contact_email`), one is registered and used. Booking.com emails the legal contact a contract;
    creation only succeeds once it is signed.
    3. If it has none and no `legal_entity`, the request is refused with `422 legal_entity_required`
    naming the fields — a contracted company is never invented.

    `legal_entity_id` overrides all of that. An id that already carries another workspace's properties
    is refused with `403 legal_entity_not_yours` before anything is created.

    ## What you do not control

    Properties are created against Booking's **production** target only. A test-target property cannot
    be sold through and there is no route back from one, so `target` is not a parameter — sending it
    changes nothing.

    The property category comes from the listing's property type (Apartment when it has none; Holiday
    home, Villa or Chalet when it says so). The initial room count is 1. Latitude and longitude come
    from the listing and are adjusted slightly to clear Booking.com's duplicate detection — send the
    property's true position on the listing and do not pre-adjust it yourself.

    The listing's name, check-in/check-out times, currency, capacity and price come from the listing.
    Its postal code is taken from the listing's own `postalCode`; when the listing has none, it falls
    back to a connected Airbnb listing. A listing with neither is created without a postal code, so set
    `postalCode` on the listing first.

    ## Guards

    Every action that takes a `property_id` requires a property connected to this workspace; any other
    id returns `404 not_found`. Every action that takes a `listing_id` requires a listing in this
    workspace; any other id returns `404 not_found`.

    `create-property` refuses a listing with no coordinates (`422 missing_coordinates`) before anything
    is created — creating a Booking.com property cannot be undone.

    `create-property` is subject to the same published-listing gate as the dashboard: no plan, or the
    plan's listing limit reached, returns `403 billing_error` with `used` and `limit`, and nothing is
    created.

    Returns `403 listing_inactive` when the listing — or any listing mapped to the Booking.com property
    — is inactive. An inactive listing keeps syncing, but cannot be read or changed through the API
    until it is activated.

    If a property is created and a later step fails, the response is `422 booking_create_partial`
    carrying `property_id`. The property EXISTS. Do not retry `create-property`, which would open a
    second one — continue with `add-room` and `advance`.

    Args:
        body (BookingSetupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BookingSetupBody,

) -> Response[Any | Error]:
    r""" Booking.com property setup actions

     Action-router for putting a property onto Booking.com — including building one from nothing. Select
    the step with `action`.

    ## Opening a property

    - `create-property` — create a NEW Booking.com property for a Repull listing (`listing_id`). Creates
    the property, its first room with the listing's beds, a rate plan and the room-rate product that
    makes the room sellable (under the listing's cancellation policy), sets the contact and invoice
    details and the facilities, seeds availability and rates, syncs the calendar, then runs
    Booking.com's readiness check and reports what still blocks opening in `warnings`. Send `contact`
    (`name`, `email`, `phone` in international form); without it the workspace owner is used, and a
    workspace with no usable contact is refused before anything is created. Returns 201.
    - `add-room` — add another room type (and its sellable product) to a property (`listing_id`,
    `property_id`). Returns 201.
    - `add-unit` — raise the number of identical units on an existing room (`listing_id`, `property_id`,
    `room_id`).
    - `advance` — run Booking.com's readiness check for a property (`property_id`) and, when it passes,
    open it. Returns `checked`, `opened`, `sellable` and `blockers` — Booking.com's own reasons it
    cannot open yet.

    ## Account and policy steps

    - `create-legal-entity` — register a legal entity directly (returns 201). Not normally needed: see
    the legal-entity rules below.
    - `check-legal-status` — always `404`. A legal entity's details are readable for any id on the
    connectivity-provider credentials every workspace shares, and nothing records which workspace
    registered which entity, so no entity can be shown to be yours. `create-property` resolves it for
    you.
    - `check-readiness` — whether a property is ready to open (`property_id`): `ready` and `blockers`,
    without trying to open it.
    - `open-property` — open the property for sale (`property_id`). Refused with `422 booking_rejected`
    naming the blockers when it is not ready.
    - `set-contacts` — set property contacts (`property_id`, `contacts` in Booking.com's Contacts API
    shape; at most one carries the `general` profile).
    - `set-policies` — add a cancellation policy (`property_id`, `policyCode`, optional
    `prepaymentRequired`). House rules, pets, children and the damage deposit are `POST
    /v1/channels/booking/content` with `type: \"settings\"`.

    ## Three things about Booking.com that cost real money

    **A newly created property is NOT sellable.** Booking.com opens it only when its readiness check
    passes, and the check names what is missing — a main photo still processing, no availability, a
    licence the region requires. The response always reports `status: \"being_built\"` and `sellable:
    false`, never a guess, with the reasons in `warnings`. Resolve them, then `advance`.

    **A room with no ACTIVE rate plan is invisible.** Booking only renders rooms that have at least one
    active product linkage (room × rate plan). A room can be created successfully, return a `roomId`,
    and never appear on the property page. If `rateId` comes back `null` from `create-property` or `add-
    room`, that is exactly what happened: activate a rate plan on the property in the Extranet, then add
    the room again.

    **Room names are Booking.com's.** Travellers see one of Booking.com's standard names (\"Two-Bedroom
    Apartment\"), chosen from the listing's bedrooms. The listing's own name is kept as the operator-
    side reference, never shown to guests.

    ## The legal entity is resolved, not asked for

    A property is created against the legal entity Booking.com contracts with, invoices and pays. You do
    not normally send one:

    1. If this workspace already creates properties under a legal entity, that one is reused. A second
    is never registered.
    2. If it has none and the request carries `legal_entity` (`company_name`, `legal_contact_name`,
    `legal_contact_email`), one is registered and used. Booking.com emails the legal contact a contract;
    creation only succeeds once it is signed.
    3. If it has none and no `legal_entity`, the request is refused with `422 legal_entity_required`
    naming the fields — a contracted company is never invented.

    `legal_entity_id` overrides all of that. An id that already carries another workspace's properties
    is refused with `403 legal_entity_not_yours` before anything is created.

    ## What you do not control

    Properties are created against Booking's **production** target only. A test-target property cannot
    be sold through and there is no route back from one, so `target` is not a parameter — sending it
    changes nothing.

    The property category comes from the listing's property type (Apartment when it has none; Holiday
    home, Villa or Chalet when it says so). The initial room count is 1. Latitude and longitude come
    from the listing and are adjusted slightly to clear Booking.com's duplicate detection — send the
    property's true position on the listing and do not pre-adjust it yourself.

    The listing's name, check-in/check-out times, currency, capacity and price come from the listing.
    Its postal code is taken from the listing's own `postalCode`; when the listing has none, it falls
    back to a connected Airbnb listing. A listing with neither is created without a postal code, so set
    `postalCode` on the listing first.

    ## Guards

    Every action that takes a `property_id` requires a property connected to this workspace; any other
    id returns `404 not_found`. Every action that takes a `listing_id` requires a listing in this
    workspace; any other id returns `404 not_found`.

    `create-property` refuses a listing with no coordinates (`422 missing_coordinates`) before anything
    is created — creating a Booking.com property cannot be undone.

    `create-property` is subject to the same published-listing gate as the dashboard: no plan, or the
    plan's listing limit reached, returns `403 billing_error` with `used` and `limit`, and nothing is
    created.

    Returns `403 listing_inactive` when the listing — or any listing mapped to the Booking.com property
    — is inactive. An inactive listing keeps syncing, but cannot be read or changed through the API
    until it is activated.

    If a property is created and a later step fails, the response is `422 booking_create_partial`
    carrying `property_id`. The property EXISTS. Do not retry `create-property`, which would open a
    second one — continue with `add-room` and `advance`.

    Args:
        body (BookingSetupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    body: BookingSetupBody,

) -> Any | Error | None:
    r""" Booking.com property setup actions

     Action-router for putting a property onto Booking.com — including building one from nothing. Select
    the step with `action`.

    ## Opening a property

    - `create-property` — create a NEW Booking.com property for a Repull listing (`listing_id`). Creates
    the property, its first room with the listing's beds, a rate plan and the room-rate product that
    makes the room sellable (under the listing's cancellation policy), sets the contact and invoice
    details and the facilities, seeds availability and rates, syncs the calendar, then runs
    Booking.com's readiness check and reports what still blocks opening in `warnings`. Send `contact`
    (`name`, `email`, `phone` in international form); without it the workspace owner is used, and a
    workspace with no usable contact is refused before anything is created. Returns 201.
    - `add-room` — add another room type (and its sellable product) to a property (`listing_id`,
    `property_id`). Returns 201.
    - `add-unit` — raise the number of identical units on an existing room (`listing_id`, `property_id`,
    `room_id`).
    - `advance` — run Booking.com's readiness check for a property (`property_id`) and, when it passes,
    open it. Returns `checked`, `opened`, `sellable` and `blockers` — Booking.com's own reasons it
    cannot open yet.

    ## Account and policy steps

    - `create-legal-entity` — register a legal entity directly (returns 201). Not normally needed: see
    the legal-entity rules below.
    - `check-legal-status` — always `404`. A legal entity's details are readable for any id on the
    connectivity-provider credentials every workspace shares, and nothing records which workspace
    registered which entity, so no entity can be shown to be yours. `create-property` resolves it for
    you.
    - `check-readiness` — whether a property is ready to open (`property_id`): `ready` and `blockers`,
    without trying to open it.
    - `open-property` — open the property for sale (`property_id`). Refused with `422 booking_rejected`
    naming the blockers when it is not ready.
    - `set-contacts` — set property contacts (`property_id`, `contacts` in Booking.com's Contacts API
    shape; at most one carries the `general` profile).
    - `set-policies` — add a cancellation policy (`property_id`, `policyCode`, optional
    `prepaymentRequired`). House rules, pets, children and the damage deposit are `POST
    /v1/channels/booking/content` with `type: \"settings\"`.

    ## Three things about Booking.com that cost real money

    **A newly created property is NOT sellable.** Booking.com opens it only when its readiness check
    passes, and the check names what is missing — a main photo still processing, no availability, a
    licence the region requires. The response always reports `status: \"being_built\"` and `sellable:
    false`, never a guess, with the reasons in `warnings`. Resolve them, then `advance`.

    **A room with no ACTIVE rate plan is invisible.** Booking only renders rooms that have at least one
    active product linkage (room × rate plan). A room can be created successfully, return a `roomId`,
    and never appear on the property page. If `rateId` comes back `null` from `create-property` or `add-
    room`, that is exactly what happened: activate a rate plan on the property in the Extranet, then add
    the room again.

    **Room names are Booking.com's.** Travellers see one of Booking.com's standard names (\"Two-Bedroom
    Apartment\"), chosen from the listing's bedrooms. The listing's own name is kept as the operator-
    side reference, never shown to guests.

    ## The legal entity is resolved, not asked for

    A property is created against the legal entity Booking.com contracts with, invoices and pays. You do
    not normally send one:

    1. If this workspace already creates properties under a legal entity, that one is reused. A second
    is never registered.
    2. If it has none and the request carries `legal_entity` (`company_name`, `legal_contact_name`,
    `legal_contact_email`), one is registered and used. Booking.com emails the legal contact a contract;
    creation only succeeds once it is signed.
    3. If it has none and no `legal_entity`, the request is refused with `422 legal_entity_required`
    naming the fields — a contracted company is never invented.

    `legal_entity_id` overrides all of that. An id that already carries another workspace's properties
    is refused with `403 legal_entity_not_yours` before anything is created.

    ## What you do not control

    Properties are created against Booking's **production** target only. A test-target property cannot
    be sold through and there is no route back from one, so `target` is not a parameter — sending it
    changes nothing.

    The property category comes from the listing's property type (Apartment when it has none; Holiday
    home, Villa or Chalet when it says so). The initial room count is 1. Latitude and longitude come
    from the listing and are adjusted slightly to clear Booking.com's duplicate detection — send the
    property's true position on the listing and do not pre-adjust it yourself.

    The listing's name, check-in/check-out times, currency, capacity and price come from the listing.
    Its postal code is taken from the listing's own `postalCode`; when the listing has none, it falls
    back to a connected Airbnb listing. A listing with neither is created without a postal code, so set
    `postalCode` on the listing first.

    ## Guards

    Every action that takes a `property_id` requires a property connected to this workspace; any other
    id returns `404 not_found`. Every action that takes a `listing_id` requires a listing in this
    workspace; any other id returns `404 not_found`.

    `create-property` refuses a listing with no coordinates (`422 missing_coordinates`) before anything
    is created — creating a Booking.com property cannot be undone.

    `create-property` is subject to the same published-listing gate as the dashboard: no plan, or the
    plan's listing limit reached, returns `403 billing_error` with `used` and `limit`, and nothing is
    created.

    Returns `403 listing_inactive` when the listing — or any listing mapped to the Booking.com property
    — is inactive. An inactive listing keeps syncing, but cannot be read or changed through the API
    until it is activated.

    If a property is created and a later step fails, the response is `422 booking_create_partial`
    carrying `property_id`. The property EXISTS. Do not retry `create-property`, which would open a
    second one — continue with `add-room` and `advance`.

    Args:
        body (BookingSetupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
