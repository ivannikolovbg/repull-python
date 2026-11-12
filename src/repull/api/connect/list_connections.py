from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connection_list_response import ConnectionListResponse
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connect",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConnectionListResponse | None:
    if response.status_code == 200:
        response_200 = ConnectionListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConnectionListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[ConnectionListResponse]:
    r""" List PMS/OTA connections

     Returns every PMS and OTA connection in the workspace, each with its `status`.

    **Account ids.** `externalAccountId` is the platform's own account id (Airbnb host id, Booking.com
    hotel id, the Booking.com account id behind an Extranet login, the PMS account id; `null` when the
    platform does not give us one) and `id` is our connection record, the `X-Account-Id`.

    **Access level.** Every connection carries `accessType`: `read_only`, `messaging` or `full_access`,
    or `null` when unknown. Airbnb: the tier the host's token was granted with. Vrbo: bookings and
    messages only (`messaging`) or with the calendar push (`full_access`). Booking.com: always
    `full_access`. Booking.com Extranet: always `messaging` (reads reservations, messages and reviews
    and replies; never writes rates or availability). PMS: `read_only` when every write-policy switch is
    off, else `full_access`. See the `ConnectionAccessType` schema.

    **One entry per Booking.com Extranet login.** Each Booking.com account that invites the Repull user
    connects as its own login, with its own `externalAccountId` — the Booking.com account id (handle
    `booking_extranet:{externalAccountId}`). A new login adds an entry next to the existing ones and
    never replaces them; the entries share the workspace's Extranet `id`, and each login's listings,
    reservations, conversations and reviews stay under its own account (filter them with
    `?account=booking_extranet:{externalAccountId}`).

    **Spot connections that need attention.** A connection whose `status` is not `active` may need the
    host to do something before it works — most commonly a Booking.com Extranet connection where the
    invited user was granted only partial access (`status: \"needs_permissions\"`). A Smoobu connection
    still on a legacy single API key carries `action.reason: \"reauth_required\"` while its `status` is
    `active`: Smoobu stops accepting those keys on October 31, 2026, and `fixUrl` opens the form for a
    new API key + secret (the connection id stays the same). These connections carry two extra fields:

    - `action` — `{ required: true, reason, message }`. `reason` is a stable machine code (e.g.
    `needs_permissions`); `message` is a host-facing one-liner describing what to do.
    - `fixUrl` — a durable link that reopens the hosted Connect flow **bound to that account, on the fix
    screen** (e.g. \"grant full access\" + a Re-check button). It is safe to store and show in your own
    dashboard.

    **Self-serve repair:** when `action.required` is true, surface a \"Fix\" button that opens `fixUrl`
    in a new tab (or embed it). The host resolves the issue (e.g. grants the user full access in
    Booking.com) and clicks Re-check; the import finishes on its own and the connection flips back to
    `active` — no re-invite, no support ticket. Poll this endpoint (or read it after the host returns)
    to confirm `action` has cleared.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionListResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> ConnectionListResponse | None:
    r""" List PMS/OTA connections

     Returns every PMS and OTA connection in the workspace, each with its `status`.

    **Account ids.** `externalAccountId` is the platform's own account id (Airbnb host id, Booking.com
    hotel id, the Booking.com account id behind an Extranet login, the PMS account id; `null` when the
    platform does not give us one) and `id` is our connection record, the `X-Account-Id`.

    **Access level.** Every connection carries `accessType`: `read_only`, `messaging` or `full_access`,
    or `null` when unknown. Airbnb: the tier the host's token was granted with. Vrbo: bookings and
    messages only (`messaging`) or with the calendar push (`full_access`). Booking.com: always
    `full_access`. Booking.com Extranet: always `messaging` (reads reservations, messages and reviews
    and replies; never writes rates or availability). PMS: `read_only` when every write-policy switch is
    off, else `full_access`. See the `ConnectionAccessType` schema.

    **One entry per Booking.com Extranet login.** Each Booking.com account that invites the Repull user
    connects as its own login, with its own `externalAccountId` — the Booking.com account id (handle
    `booking_extranet:{externalAccountId}`). A new login adds an entry next to the existing ones and
    never replaces them; the entries share the workspace's Extranet `id`, and each login's listings,
    reservations, conversations and reviews stay under its own account (filter them with
    `?account=booking_extranet:{externalAccountId}`).

    **Spot connections that need attention.** A connection whose `status` is not `active` may need the
    host to do something before it works — most commonly a Booking.com Extranet connection where the
    invited user was granted only partial access (`status: \"needs_permissions\"`). A Smoobu connection
    still on a legacy single API key carries `action.reason: \"reauth_required\"` while its `status` is
    `active`: Smoobu stops accepting those keys on October 31, 2026, and `fixUrl` opens the form for a
    new API key + secret (the connection id stays the same). These connections carry two extra fields:

    - `action` — `{ required: true, reason, message }`. `reason` is a stable machine code (e.g.
    `needs_permissions`); `message` is a host-facing one-liner describing what to do.
    - `fixUrl` — a durable link that reopens the hosted Connect flow **bound to that account, on the fix
    screen** (e.g. \"grant full access\" + a Re-check button). It is safe to store and show in your own
    dashboard.

    **Self-serve repair:** when `action.required` is true, surface a \"Fix\" button that opens `fixUrl`
    in a new tab (or embed it). The host resolves the issue (e.g. grants the user full access in
    Booking.com) and clicks Re-check; the import finishes on its own and the connection flips back to
    `active` — no re-invite, no support ticket. Poll this endpoint (or read it after the host returns)
    to confirm `action` has cleared.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionListResponse
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[ConnectionListResponse]:
    r""" List PMS/OTA connections

     Returns every PMS and OTA connection in the workspace, each with its `status`.

    **Account ids.** `externalAccountId` is the platform's own account id (Airbnb host id, Booking.com
    hotel id, the Booking.com account id behind an Extranet login, the PMS account id; `null` when the
    platform does not give us one) and `id` is our connection record, the `X-Account-Id`.

    **Access level.** Every connection carries `accessType`: `read_only`, `messaging` or `full_access`,
    or `null` when unknown. Airbnb: the tier the host's token was granted with. Vrbo: bookings and
    messages only (`messaging`) or with the calendar push (`full_access`). Booking.com: always
    `full_access`. Booking.com Extranet: always `messaging` (reads reservations, messages and reviews
    and replies; never writes rates or availability). PMS: `read_only` when every write-policy switch is
    off, else `full_access`. See the `ConnectionAccessType` schema.

    **One entry per Booking.com Extranet login.** Each Booking.com account that invites the Repull user
    connects as its own login, with its own `externalAccountId` — the Booking.com account id (handle
    `booking_extranet:{externalAccountId}`). A new login adds an entry next to the existing ones and
    never replaces them; the entries share the workspace's Extranet `id`, and each login's listings,
    reservations, conversations and reviews stay under its own account (filter them with
    `?account=booking_extranet:{externalAccountId}`).

    **Spot connections that need attention.** A connection whose `status` is not `active` may need the
    host to do something before it works — most commonly a Booking.com Extranet connection where the
    invited user was granted only partial access (`status: \"needs_permissions\"`). A Smoobu connection
    still on a legacy single API key carries `action.reason: \"reauth_required\"` while its `status` is
    `active`: Smoobu stops accepting those keys on October 31, 2026, and `fixUrl` opens the form for a
    new API key + secret (the connection id stays the same). These connections carry two extra fields:

    - `action` — `{ required: true, reason, message }`. `reason` is a stable machine code (e.g.
    `needs_permissions`); `message` is a host-facing one-liner describing what to do.
    - `fixUrl` — a durable link that reopens the hosted Connect flow **bound to that account, on the fix
    screen** (e.g. \"grant full access\" + a Re-check button). It is safe to store and show in your own
    dashboard.

    **Self-serve repair:** when `action.required` is true, surface a \"Fix\" button that opens `fixUrl`
    in a new tab (or embed it). The host resolves the issue (e.g. grants the user full access in
    Booking.com) and clicks Re-check; the import finishes on its own and the connection flips back to
    `active` — no re-invite, no support ticket. Poll this endpoint (or read it after the host returns)
    to confirm `action` has cleared.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectionListResponse]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> ConnectionListResponse | None:
    r""" List PMS/OTA connections

     Returns every PMS and OTA connection in the workspace, each with its `status`.

    **Account ids.** `externalAccountId` is the platform's own account id (Airbnb host id, Booking.com
    hotel id, the Booking.com account id behind an Extranet login, the PMS account id; `null` when the
    platform does not give us one) and `id` is our connection record, the `X-Account-Id`.

    **Access level.** Every connection carries `accessType`: `read_only`, `messaging` or `full_access`,
    or `null` when unknown. Airbnb: the tier the host's token was granted with. Vrbo: bookings and
    messages only (`messaging`) or with the calendar push (`full_access`). Booking.com: always
    `full_access`. Booking.com Extranet: always `messaging` (reads reservations, messages and reviews
    and replies; never writes rates or availability). PMS: `read_only` when every write-policy switch is
    off, else `full_access`. See the `ConnectionAccessType` schema.

    **One entry per Booking.com Extranet login.** Each Booking.com account that invites the Repull user
    connects as its own login, with its own `externalAccountId` — the Booking.com account id (handle
    `booking_extranet:{externalAccountId}`). A new login adds an entry next to the existing ones and
    never replaces them; the entries share the workspace's Extranet `id`, and each login's listings,
    reservations, conversations and reviews stay under its own account (filter them with
    `?account=booking_extranet:{externalAccountId}`).

    **Spot connections that need attention.** A connection whose `status` is not `active` may need the
    host to do something before it works — most commonly a Booking.com Extranet connection where the
    invited user was granted only partial access (`status: \"needs_permissions\"`). A Smoobu connection
    still on a legacy single API key carries `action.reason: \"reauth_required\"` while its `status` is
    `active`: Smoobu stops accepting those keys on October 31, 2026, and `fixUrl` opens the form for a
    new API key + secret (the connection id stays the same). These connections carry two extra fields:

    - `action` — `{ required: true, reason, message }`. `reason` is a stable machine code (e.g.
    `needs_permissions`); `message` is a host-facing one-liner describing what to do.
    - `fixUrl` — a durable link that reopens the hosted Connect flow **bound to that account, on the fix
    screen** (e.g. \"grant full access\" + a Re-check button). It is safe to store and show in your own
    dashboard.

    **Self-serve repair:** when `action.required` is true, surface a \"Fix\" button that opens `fixUrl`
    in a new tab (or embed it). The host resolves the issue (e.g. grants the user full access in
    Booking.com) and clicks Re-check; the import finishes on its own and the connection flips back to
    `active` — no re-invite, no support ticket. Poll this endpoint (or read it after the host returns)
    to confirm `action` has cleared.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectionListResponse
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
