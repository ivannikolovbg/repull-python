from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.submit_track_credentials_body import SubmitTrackCredentialsBody
from ...models.submit_track_credentials_response_200 import SubmitTrackCredentialsResponse200
from typing import cast



def _get_kwargs(
    *,
    body: SubmitTrackCredentialsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/track/credentials",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SubmitTrackCredentialsResponse200 | None:
    if response.status_code == 200:
        response_200 = SubmitTrackCredentialsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SubmitTrackCredentialsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SubmitTrackCredentialsBody,

) -> Response[Error | SubmitTrackCredentialsResponse200]:
    """ Submit Track credentials for a Connect session

     Completes a credentials-pattern connection for Track (TRACK Hospitality Software) with the property
    manager's Track domain and an API key + secret.

    **What syncs.** Units become listings; reservations (with their fee and tax breakdown) and guest
    message threads are imported, then polled for changes. Bookings can be created, quoted, changed and
    cancelled in Track — see `capabilities.reservations` on `GET /v1/connect/track`.

    **Which key.** A **Server Key** — created in Track under Configuration → Company Setup → API Keys —
    has full access and is recommended. A **Channel Key** — under Configuration → PMS Setup →
    Distribution Channels — only allows booking. `keyType` defaults to `server`.

    The key is validated against Track before anything is stored, so an invalid key returns
    `invalid_credentials` rather than creating a dead connection. On success only the credential fields
    below are stored, and the first sync of listings and reservations is queued.

    Track has no webhooks: after the first sync, reservation and message changes are picked up by
    polling about once a minute.

    Reconnecting replaces the stored credentials on the workspace's existing Track connection — the
    `pmsConnectionId` stays the same.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitTrackCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SubmitTrackCredentialsResponse200]
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
    body: SubmitTrackCredentialsBody,

) -> Error | SubmitTrackCredentialsResponse200 | None:
    """ Submit Track credentials for a Connect session

     Completes a credentials-pattern connection for Track (TRACK Hospitality Software) with the property
    manager's Track domain and an API key + secret.

    **What syncs.** Units become listings; reservations (with their fee and tax breakdown) and guest
    message threads are imported, then polled for changes. Bookings can be created, quoted, changed and
    cancelled in Track — see `capabilities.reservations` on `GET /v1/connect/track`.

    **Which key.** A **Server Key** — created in Track under Configuration → Company Setup → API Keys —
    has full access and is recommended. A **Channel Key** — under Configuration → PMS Setup →
    Distribution Channels — only allows booking. `keyType` defaults to `server`.

    The key is validated against Track before anything is stored, so an invalid key returns
    `invalid_credentials` rather than creating a dead connection. On success only the credential fields
    below are stored, and the first sync of listings and reservations is queued.

    Track has no webhooks: after the first sync, reservation and message changes are picked up by
    polling about once a minute.

    Reconnecting replaces the stored credentials on the workspace's existing Track connection — the
    `pmsConnectionId` stays the same.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitTrackCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SubmitTrackCredentialsResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SubmitTrackCredentialsBody,

) -> Response[Error | SubmitTrackCredentialsResponse200]:
    """ Submit Track credentials for a Connect session

     Completes a credentials-pattern connection for Track (TRACK Hospitality Software) with the property
    manager's Track domain and an API key + secret.

    **What syncs.** Units become listings; reservations (with their fee and tax breakdown) and guest
    message threads are imported, then polled for changes. Bookings can be created, quoted, changed and
    cancelled in Track — see `capabilities.reservations` on `GET /v1/connect/track`.

    **Which key.** A **Server Key** — created in Track under Configuration → Company Setup → API Keys —
    has full access and is recommended. A **Channel Key** — under Configuration → PMS Setup →
    Distribution Channels — only allows booking. `keyType` defaults to `server`.

    The key is validated against Track before anything is stored, so an invalid key returns
    `invalid_credentials` rather than creating a dead connection. On success only the credential fields
    below are stored, and the first sync of listings and reservations is queued.

    Track has no webhooks: after the first sync, reservation and message changes are picked up by
    polling about once a minute.

    Reconnecting replaces the stored credentials on the workspace's existing Track connection — the
    `pmsConnectionId` stays the same.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitTrackCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SubmitTrackCredentialsResponse200]
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
    body: SubmitTrackCredentialsBody,

) -> Error | SubmitTrackCredentialsResponse200 | None:
    """ Submit Track credentials for a Connect session

     Completes a credentials-pattern connection for Track (TRACK Hospitality Software) with the property
    manager's Track domain and an API key + secret.

    **What syncs.** Units become listings; reservations (with their fee and tax breakdown) and guest
    message threads are imported, then polled for changes. Bookings can be created, quoted, changed and
    cancelled in Track — see `capabilities.reservations` on `GET /v1/connect/track`.

    **Which key.** A **Server Key** — created in Track under Configuration → Company Setup → API Keys —
    has full access and is recommended. A **Channel Key** — under Configuration → PMS Setup →
    Distribution Channels — only allows booking. `keyType` defaults to `server`.

    The key is validated against Track before anything is stored, so an invalid key returns
    `invalid_credentials` rather than creating a dead connection. On success only the credential fields
    below are stored, and the first sync of listings and reservations is queued.

    Track has no webhooks: after the first sync, reservation and message changes are picked up by
    polling about once a minute.

    Reconnecting replaces the stored credentials on the workspace's existing Track connection — the
    `pmsConnectionId` stays the same.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitTrackCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SubmitTrackCredentialsResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
