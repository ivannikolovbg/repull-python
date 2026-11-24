from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connect_provider_session import ConnectProviderSession
from ...models.create_connection_body import CreateConnectionBody
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    provider: str,
    *,
    body: CreateConnectionBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/{provider}".format(provider=quote(str(provider), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConnectProviderSession | None:
    if response.status_code == 200:
        response_200 = ConnectProviderSession.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConnectProviderSession]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateConnectionBody | Unset = UNSET,

) -> Response[ConnectProviderSession]:
    r""" Connect to PMS/OTA provider

     Establish a connection to a PMS or OTA platform. Credentials vary by provider — see docs for each
    provider.

    Airbnb-specific: pass `redirectUrl` (where to send the user after consent) and optionally
    `accessType`. Three tiers: `read_only` grants read-only scopes; `messaging` (shown to hosts as
    \"Messaging & reviews\") grants read scopes plus message read/send and review writes (reply to guest
    reviews, submit host reviews — Airbnb's `reviews_write`) but NOT property management, so it can
    coexist with another app (e.g. an existing PMS) that already holds property management on the same
    Airbnb account; `full_access` — the default — grants full host scopes including the exclusive
    property management (only one app per Airbnb account can hold it). The response returns a hosted
    `url` to redirect the user to.

    Booking.com: pass `redirectUrl` (no `accessType`). The response returns a hosted `url` — send the
    user there to select our connectivity provider in their Booking.com Extranet and paste their Hotel
    ID. Same response shape as Airbnb (`url`, `sessionId`, `expiresAt`, `state`).

    **Returning to your app.** Every return to `redirectUrl` carries `status`, `sessionId` and your
    `state`, whether the host connected, cancelled, hit an error or let the session expire, so you can
    always tie it back to the call that started it.

    PMS providers are not connected by this call: send their credentials to `POST
    /v1/connect/{provider}/credentials`, or start a hosted session with `POST /v1/connect`.

    **PriceLabs (an app).** Pass `redirectUrl` (and optionally `state`, `locale`, `workspace`). The
    response returns a hosted `url` for the session's workspace: yours, the one `X-Workspace-Id` names,
    or a new sub-workspace when you send `workspace.name` (its id comes back as `workspaceId`). The page
    shows the host a key for **every listing of that workspace, including listings added later**, with
    the steps to paste it into PriceLabs, then waits for PriceLabs' first call and completes like every
    provider: redirect to `redirectUrl` (`status=connected&connectionId=…`) or the
    `repull:connect:completed` popup message, and `connect.session.completed`. When PriceLabs first uses
    the key, `account.created` is sent. To keep PriceLabs away from the rest of an account, put the
    listings it should price in a sub-workspace and connect PriceLabs there. To issue the key yourself
    (no hosted page, or only some listings) use `POST /v1/connect/pricelabs/key`.

    Args:
        provider (str):
        body (CreateConnectionBody | Unset): Provider-specific credentials (apiKey,
            clientId/clientSecret, etc.) or OAuth init params for Airbnb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectProviderSession]
     """


    kwargs = _get_kwargs(
        provider=provider,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateConnectionBody | Unset = UNSET,

) -> ConnectProviderSession | None:
    r""" Connect to PMS/OTA provider

     Establish a connection to a PMS or OTA platform. Credentials vary by provider — see docs for each
    provider.

    Airbnb-specific: pass `redirectUrl` (where to send the user after consent) and optionally
    `accessType`. Three tiers: `read_only` grants read-only scopes; `messaging` (shown to hosts as
    \"Messaging & reviews\") grants read scopes plus message read/send and review writes (reply to guest
    reviews, submit host reviews — Airbnb's `reviews_write`) but NOT property management, so it can
    coexist with another app (e.g. an existing PMS) that already holds property management on the same
    Airbnb account; `full_access` — the default — grants full host scopes including the exclusive
    property management (only one app per Airbnb account can hold it). The response returns a hosted
    `url` to redirect the user to.

    Booking.com: pass `redirectUrl` (no `accessType`). The response returns a hosted `url` — send the
    user there to select our connectivity provider in their Booking.com Extranet and paste their Hotel
    ID. Same response shape as Airbnb (`url`, `sessionId`, `expiresAt`, `state`).

    **Returning to your app.** Every return to `redirectUrl` carries `status`, `sessionId` and your
    `state`, whether the host connected, cancelled, hit an error or let the session expire, so you can
    always tie it back to the call that started it.

    PMS providers are not connected by this call: send their credentials to `POST
    /v1/connect/{provider}/credentials`, or start a hosted session with `POST /v1/connect`.

    **PriceLabs (an app).** Pass `redirectUrl` (and optionally `state`, `locale`, `workspace`). The
    response returns a hosted `url` for the session's workspace: yours, the one `X-Workspace-Id` names,
    or a new sub-workspace when you send `workspace.name` (its id comes back as `workspaceId`). The page
    shows the host a key for **every listing of that workspace, including listings added later**, with
    the steps to paste it into PriceLabs, then waits for PriceLabs' first call and completes like every
    provider: redirect to `redirectUrl` (`status=connected&connectionId=…`) or the
    `repull:connect:completed` popup message, and `connect.session.completed`. When PriceLabs first uses
    the key, `account.created` is sent. To keep PriceLabs away from the rest of an account, put the
    listings it should price in a sub-workspace and connect PriceLabs there. To issue the key yourself
    (no hosted page, or only some listings) use `POST /v1/connect/pricelabs/key`.

    Args:
        provider (str):
        body (CreateConnectionBody | Unset): Provider-specific credentials (apiKey,
            clientId/clientSecret, etc.) or OAuth init params for Airbnb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectProviderSession
     """


    return sync_detailed(
        provider=provider,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateConnectionBody | Unset = UNSET,

) -> Response[ConnectProviderSession]:
    r""" Connect to PMS/OTA provider

     Establish a connection to a PMS or OTA platform. Credentials vary by provider — see docs for each
    provider.

    Airbnb-specific: pass `redirectUrl` (where to send the user after consent) and optionally
    `accessType`. Three tiers: `read_only` grants read-only scopes; `messaging` (shown to hosts as
    \"Messaging & reviews\") grants read scopes plus message read/send and review writes (reply to guest
    reviews, submit host reviews — Airbnb's `reviews_write`) but NOT property management, so it can
    coexist with another app (e.g. an existing PMS) that already holds property management on the same
    Airbnb account; `full_access` — the default — grants full host scopes including the exclusive
    property management (only one app per Airbnb account can hold it). The response returns a hosted
    `url` to redirect the user to.

    Booking.com: pass `redirectUrl` (no `accessType`). The response returns a hosted `url` — send the
    user there to select our connectivity provider in their Booking.com Extranet and paste their Hotel
    ID. Same response shape as Airbnb (`url`, `sessionId`, `expiresAt`, `state`).

    **Returning to your app.** Every return to `redirectUrl` carries `status`, `sessionId` and your
    `state`, whether the host connected, cancelled, hit an error or let the session expire, so you can
    always tie it back to the call that started it.

    PMS providers are not connected by this call: send their credentials to `POST
    /v1/connect/{provider}/credentials`, or start a hosted session with `POST /v1/connect`.

    **PriceLabs (an app).** Pass `redirectUrl` (and optionally `state`, `locale`, `workspace`). The
    response returns a hosted `url` for the session's workspace: yours, the one `X-Workspace-Id` names,
    or a new sub-workspace when you send `workspace.name` (its id comes back as `workspaceId`). The page
    shows the host a key for **every listing of that workspace, including listings added later**, with
    the steps to paste it into PriceLabs, then waits for PriceLabs' first call and completes like every
    provider: redirect to `redirectUrl` (`status=connected&connectionId=…`) or the
    `repull:connect:completed` popup message, and `connect.session.completed`. When PriceLabs first uses
    the key, `account.created` is sent. To keep PriceLabs away from the rest of an account, put the
    listings it should price in a sub-workspace and connect PriceLabs there. To issue the key yourself
    (no hosted page, or only some listings) use `POST /v1/connect/pricelabs/key`.

    Args:
        provider (str):
        body (CreateConnectionBody | Unset): Provider-specific credentials (apiKey,
            clientId/clientSecret, etc.) or OAuth init params for Airbnb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectProviderSession]
     """


    kwargs = _get_kwargs(
        provider=provider,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreateConnectionBody | Unset = UNSET,

) -> ConnectProviderSession | None:
    r""" Connect to PMS/OTA provider

     Establish a connection to a PMS or OTA platform. Credentials vary by provider — see docs for each
    provider.

    Airbnb-specific: pass `redirectUrl` (where to send the user after consent) and optionally
    `accessType`. Three tiers: `read_only` grants read-only scopes; `messaging` (shown to hosts as
    \"Messaging & reviews\") grants read scopes plus message read/send and review writes (reply to guest
    reviews, submit host reviews — Airbnb's `reviews_write`) but NOT property management, so it can
    coexist with another app (e.g. an existing PMS) that already holds property management on the same
    Airbnb account; `full_access` — the default — grants full host scopes including the exclusive
    property management (only one app per Airbnb account can hold it). The response returns a hosted
    `url` to redirect the user to.

    Booking.com: pass `redirectUrl` (no `accessType`). The response returns a hosted `url` — send the
    user there to select our connectivity provider in their Booking.com Extranet and paste their Hotel
    ID. Same response shape as Airbnb (`url`, `sessionId`, `expiresAt`, `state`).

    **Returning to your app.** Every return to `redirectUrl` carries `status`, `sessionId` and your
    `state`, whether the host connected, cancelled, hit an error or let the session expire, so you can
    always tie it back to the call that started it.

    PMS providers are not connected by this call: send their credentials to `POST
    /v1/connect/{provider}/credentials`, or start a hosted session with `POST /v1/connect`.

    **PriceLabs (an app).** Pass `redirectUrl` (and optionally `state`, `locale`, `workspace`). The
    response returns a hosted `url` for the session's workspace: yours, the one `X-Workspace-Id` names,
    or a new sub-workspace when you send `workspace.name` (its id comes back as `workspaceId`). The page
    shows the host a key for **every listing of that workspace, including listings added later**, with
    the steps to paste it into PriceLabs, then waits for PriceLabs' first call and completes like every
    provider: redirect to `redirectUrl` (`status=connected&connectionId=…`) or the
    `repull:connect:completed` popup message, and `connect.session.completed`. When PriceLabs first uses
    the key, `account.created` is sent. To keep PriceLabs away from the rest of an account, put the
    listings it should price in a sub-workspace and connect PriceLabs there. To issue the key yourself
    (no hosted page, or only some listings) use `POST /v1/connect/pricelabs/key`.

    Args:
        provider (str):
        body (CreateConnectionBody | Unset): Provider-specific credentials (apiKey,
            clientId/clientSecret, etc.) or OAuth init params for Airbnb.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectProviderSession
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,
body=body,

    )).parsed
