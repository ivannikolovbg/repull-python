from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.update_booking_content_body import UpdateBookingContentBody
from typing import cast



def _get_kwargs(
    *,
    body: UpdateBookingContentBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/booking/content",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
    body: UpdateBookingContentBody,

) -> Response[Any | Error]:
    r""" Update Booking.com content

     Write one kind of content to a Booking.com property only. Nothing on the canonical listing or on
    Airbnb changes. To send the listing's own content to every channel instead, use `PUT
    /v1/listings/{id}/content` and publish.

    | `type` | What it is |
    |---|---|
    | `photos` | The property's photos. Add `room_id` to read one room's gallery. |
    | `facilities` | Property facilities, or a room's with `room_id` (Booking.com's ids — `GET` returns
    them). |
    | `description` | The property description. Booking.com rewrites what you send into its own
    multilingual copy; allow about 3 hours to appear. |
    | `settings` | House rules, pets, children, damage deposit, invoice recipient, booking model. |
    | `policies` | Cancellation and prepayment policies. |
    | `licences` | The region's licence rules and the licence on file. |
    | `checkin_methods` | How guests get in (holiday homes). |
    | `contacts` | Who Booking.com contacts about the property. |

    `amenities` is accepted as another name for `facilities`, and `descriptions` for `description`.

    What each `type` takes:

    - `description`: `text`, optional `language` (default `en`).
    - `facilities`: `facilities: [{ facility_id | room_facility_id, state: \"PRESENT\" | \"MISSING\",
    instances? }]`. Facilities you do not send stay as they are.
    - `photos`: `photos: [{ url }]`, uploaded in the background. With `room_id`, send `photo_ids`
    instead to add photos that have finished processing to that room.
    - `settings`: `settings: { <block>: {…} }`, for example `{ \"pets\": { \"pets_allowed\":
    \"PETS_ALLOWED\" } }`. Each block is written separately and reported in `results`.
    - `policies`: `policyCode` (152 = free cancellation at any time, 1 = non-refundable, …), optional
    `prepaymentRequired`; add `policyId` to change an existing policy. A property holds at most 7
    policies and none can be deleted.
    - `licences`: `variantId` and `contentData: [{ name, value }]`, from the rules `GET ?type=licences`
    returns; optional `room_id`.
    - `checkin_methods`: `methods: [{ checkin_method }]`, using a name from `GET ?type=checkin_methods`
    `available`.
    - `contacts`: `contacts: [...]` in Booking.com's contact shape.

    If Booking.com refuses the write, the response is `422 booking_rejected` with Booking.com's reason,
    even when Booking.com answered HTTP 200. Resending the same body will be refused again.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        body (UpdateBookingContentBody):

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
    body: UpdateBookingContentBody,

) -> Any | Error | None:
    r""" Update Booking.com content

     Write one kind of content to a Booking.com property only. Nothing on the canonical listing or on
    Airbnb changes. To send the listing's own content to every channel instead, use `PUT
    /v1/listings/{id}/content` and publish.

    | `type` | What it is |
    |---|---|
    | `photos` | The property's photos. Add `room_id` to read one room's gallery. |
    | `facilities` | Property facilities, or a room's with `room_id` (Booking.com's ids — `GET` returns
    them). |
    | `description` | The property description. Booking.com rewrites what you send into its own
    multilingual copy; allow about 3 hours to appear. |
    | `settings` | House rules, pets, children, damage deposit, invoice recipient, booking model. |
    | `policies` | Cancellation and prepayment policies. |
    | `licences` | The region's licence rules and the licence on file. |
    | `checkin_methods` | How guests get in (holiday homes). |
    | `contacts` | Who Booking.com contacts about the property. |

    `amenities` is accepted as another name for `facilities`, and `descriptions` for `description`.

    What each `type` takes:

    - `description`: `text`, optional `language` (default `en`).
    - `facilities`: `facilities: [{ facility_id | room_facility_id, state: \"PRESENT\" | \"MISSING\",
    instances? }]`. Facilities you do not send stay as they are.
    - `photos`: `photos: [{ url }]`, uploaded in the background. With `room_id`, send `photo_ids`
    instead to add photos that have finished processing to that room.
    - `settings`: `settings: { <block>: {…} }`, for example `{ \"pets\": { \"pets_allowed\":
    \"PETS_ALLOWED\" } }`. Each block is written separately and reported in `results`.
    - `policies`: `policyCode` (152 = free cancellation at any time, 1 = non-refundable, …), optional
    `prepaymentRequired`; add `policyId` to change an existing policy. A property holds at most 7
    policies and none can be deleted.
    - `licences`: `variantId` and `contentData: [{ name, value }]`, from the rules `GET ?type=licences`
    returns; optional `room_id`.
    - `checkin_methods`: `methods: [{ checkin_method }]`, using a name from `GET ?type=checkin_methods`
    `available`.
    - `contacts`: `contacts: [...]` in Booking.com's contact shape.

    If Booking.com refuses the write, the response is `422 booking_rejected` with Booking.com's reason,
    even when Booking.com answered HTTP 200. Resending the same body will be refused again.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        body (UpdateBookingContentBody):

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
    body: UpdateBookingContentBody,

) -> Response[Any | Error]:
    r""" Update Booking.com content

     Write one kind of content to a Booking.com property only. Nothing on the canonical listing or on
    Airbnb changes. To send the listing's own content to every channel instead, use `PUT
    /v1/listings/{id}/content` and publish.

    | `type` | What it is |
    |---|---|
    | `photos` | The property's photos. Add `room_id` to read one room's gallery. |
    | `facilities` | Property facilities, or a room's with `room_id` (Booking.com's ids — `GET` returns
    them). |
    | `description` | The property description. Booking.com rewrites what you send into its own
    multilingual copy; allow about 3 hours to appear. |
    | `settings` | House rules, pets, children, damage deposit, invoice recipient, booking model. |
    | `policies` | Cancellation and prepayment policies. |
    | `licences` | The region's licence rules and the licence on file. |
    | `checkin_methods` | How guests get in (holiday homes). |
    | `contacts` | Who Booking.com contacts about the property. |

    `amenities` is accepted as another name for `facilities`, and `descriptions` for `description`.

    What each `type` takes:

    - `description`: `text`, optional `language` (default `en`).
    - `facilities`: `facilities: [{ facility_id | room_facility_id, state: \"PRESENT\" | \"MISSING\",
    instances? }]`. Facilities you do not send stay as they are.
    - `photos`: `photos: [{ url }]`, uploaded in the background. With `room_id`, send `photo_ids`
    instead to add photos that have finished processing to that room.
    - `settings`: `settings: { <block>: {…} }`, for example `{ \"pets\": { \"pets_allowed\":
    \"PETS_ALLOWED\" } }`. Each block is written separately and reported in `results`.
    - `policies`: `policyCode` (152 = free cancellation at any time, 1 = non-refundable, …), optional
    `prepaymentRequired`; add `policyId` to change an existing policy. A property holds at most 7
    policies and none can be deleted.
    - `licences`: `variantId` and `contentData: [{ name, value }]`, from the rules `GET ?type=licences`
    returns; optional `room_id`.
    - `checkin_methods`: `methods: [{ checkin_method }]`, using a name from `GET ?type=checkin_methods`
    `available`.
    - `contacts`: `contacts: [...]` in Booking.com's contact shape.

    If Booking.com refuses the write, the response is `422 booking_rejected` with Booking.com's reason,
    even when Booking.com answered HTTP 200. Resending the same body will be refused again.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        body (UpdateBookingContentBody):

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
    body: UpdateBookingContentBody,

) -> Any | Error | None:
    r""" Update Booking.com content

     Write one kind of content to a Booking.com property only. Nothing on the canonical listing or on
    Airbnb changes. To send the listing's own content to every channel instead, use `PUT
    /v1/listings/{id}/content` and publish.

    | `type` | What it is |
    |---|---|
    | `photos` | The property's photos. Add `room_id` to read one room's gallery. |
    | `facilities` | Property facilities, or a room's with `room_id` (Booking.com's ids — `GET` returns
    them). |
    | `description` | The property description. Booking.com rewrites what you send into its own
    multilingual copy; allow about 3 hours to appear. |
    | `settings` | House rules, pets, children, damage deposit, invoice recipient, booking model. |
    | `policies` | Cancellation and prepayment policies. |
    | `licences` | The region's licence rules and the licence on file. |
    | `checkin_methods` | How guests get in (holiday homes). |
    | `contacts` | Who Booking.com contacts about the property. |

    `amenities` is accepted as another name for `facilities`, and `descriptions` for `description`.

    What each `type` takes:

    - `description`: `text`, optional `language` (default `en`).
    - `facilities`: `facilities: [{ facility_id | room_facility_id, state: \"PRESENT\" | \"MISSING\",
    instances? }]`. Facilities you do not send stay as they are.
    - `photos`: `photos: [{ url }]`, uploaded in the background. With `room_id`, send `photo_ids`
    instead to add photos that have finished processing to that room.
    - `settings`: `settings: { <block>: {…} }`, for example `{ \"pets\": { \"pets_allowed\":
    \"PETS_ALLOWED\" } }`. Each block is written separately and reported in `results`.
    - `policies`: `policyCode` (152 = free cancellation at any time, 1 = non-refundable, …), optional
    `prepaymentRequired`; add `policyId` to change an existing policy. A property holds at most 7
    policies and none can be deleted.
    - `licences`: `variantId` and `contentData: [{ name, value }]`, from the rules `GET ?type=licences`
    returns; optional `room_id`.
    - `checkin_methods`: `methods: [{ checkin_method }]`, using a name from `GET ?type=checkin_methods`
    `available`.
    - `contacts`: `contacts: [...]` in Booking.com's contact shape.

    If Booking.com refuses the write, the response is `422 booking_rejected` with Booking.com's reason,
    even when Booking.com answered HTTP 200. Resending the same body will be refused again.

    `property_id` must be a Booking.com property connected to this workspace (`GET
    /v1/channels/booking/properties` lists them). Any other id — including one connected to a different
    workspace — returns `404 not_found`, the same answer as an id that does not exist.

    Returns `403 listing_inactive` when any listing mapped to the Booking.com property is inactive. An
    inactive listing keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        body (UpdateBookingContentBody):

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
