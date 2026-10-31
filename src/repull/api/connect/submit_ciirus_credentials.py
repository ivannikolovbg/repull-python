from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.submit_ciirus_credentials_body import SubmitCiirusCredentialsBody
from ...models.submit_ciirus_credentials_response_200 import SubmitCiirusCredentialsResponse200
from typing import cast



def _get_kwargs(
    *,
    body: SubmitCiirusCredentialsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/ciirus/credentials",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SubmitCiirusCredentialsResponse200 | None:
    if response.status_code == 200:
        response_200 = SubmitCiirusCredentialsResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SubmitCiirusCredentialsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SubmitCiirusCredentialsBody,

) -> Response[Error | SubmitCiirusCredentialsResponse200]:
    """ Submit CiiRUS credentials for a Connect session

     Completes a credentials-pattern connection for CiiRUS with the property manager's CiiRUS API
    username and password.

    **What syncs.** Units become listings (with descriptions, photos, amenities, rooms and house rules);
    reservations (with their charge and tax breakdown and payments) and reviews are imported, then
    polled for changes. Bookings can be created, quoted, changed and cancelled in CiiRUS — see
    `capabilities.reservations` on `GET /v1/connect/ciirus`. Guest messages are not available through
    CiiRUS's API.

    **Where the credentials come from.** The CiiRUS API Explorer gives the API username and password
    after signing in with the CiiRUS MC username and company password; CiiRUS support can also issue
    them. Credentials that see several suppliers (management companies) also need
    `managementCompanyUserId`.

    **IP whitelist.** CiiRUS only accepts calls from whitelisted IP addresses, and answers a wrong
    password and a non-whitelisted address the same way. When this returns `invalid_credentials` with
    correct credentials, ask CiiRUS support to whitelist Repull for the API user.

    The credentials are validated against CiiRUS before anything is stored, so invalid ones return
    `invalid_credentials` rather than creating a dead connection. On success only the credential fields
    below are stored, and the first sync of listings and reservations is queued.

    CiiRUS has no webhooks: after the first sync, reservation changes are picked up by polling about
    once a minute.

    Reconnecting replaces the stored credentials on the workspace's existing CiiRUS connection — the
    `pmsConnectionId` stays the same.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitCiirusCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SubmitCiirusCredentialsResponse200]
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
    body: SubmitCiirusCredentialsBody,

) -> Error | SubmitCiirusCredentialsResponse200 | None:
    """ Submit CiiRUS credentials for a Connect session

     Completes a credentials-pattern connection for CiiRUS with the property manager's CiiRUS API
    username and password.

    **What syncs.** Units become listings (with descriptions, photos, amenities, rooms and house rules);
    reservations (with their charge and tax breakdown and payments) and reviews are imported, then
    polled for changes. Bookings can be created, quoted, changed and cancelled in CiiRUS — see
    `capabilities.reservations` on `GET /v1/connect/ciirus`. Guest messages are not available through
    CiiRUS's API.

    **Where the credentials come from.** The CiiRUS API Explorer gives the API username and password
    after signing in with the CiiRUS MC username and company password; CiiRUS support can also issue
    them. Credentials that see several suppliers (management companies) also need
    `managementCompanyUserId`.

    **IP whitelist.** CiiRUS only accepts calls from whitelisted IP addresses, and answers a wrong
    password and a non-whitelisted address the same way. When this returns `invalid_credentials` with
    correct credentials, ask CiiRUS support to whitelist Repull for the API user.

    The credentials are validated against CiiRUS before anything is stored, so invalid ones return
    `invalid_credentials` rather than creating a dead connection. On success only the credential fields
    below are stored, and the first sync of listings and reservations is queued.

    CiiRUS has no webhooks: after the first sync, reservation changes are picked up by polling about
    once a minute.

    Reconnecting replaces the stored credentials on the workspace's existing CiiRUS connection — the
    `pmsConnectionId` stays the same.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitCiirusCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SubmitCiirusCredentialsResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SubmitCiirusCredentialsBody,

) -> Response[Error | SubmitCiirusCredentialsResponse200]:
    """ Submit CiiRUS credentials for a Connect session

     Completes a credentials-pattern connection for CiiRUS with the property manager's CiiRUS API
    username and password.

    **What syncs.** Units become listings (with descriptions, photos, amenities, rooms and house rules);
    reservations (with their charge and tax breakdown and payments) and reviews are imported, then
    polled for changes. Bookings can be created, quoted, changed and cancelled in CiiRUS — see
    `capabilities.reservations` on `GET /v1/connect/ciirus`. Guest messages are not available through
    CiiRUS's API.

    **Where the credentials come from.** The CiiRUS API Explorer gives the API username and password
    after signing in with the CiiRUS MC username and company password; CiiRUS support can also issue
    them. Credentials that see several suppliers (management companies) also need
    `managementCompanyUserId`.

    **IP whitelist.** CiiRUS only accepts calls from whitelisted IP addresses, and answers a wrong
    password and a non-whitelisted address the same way. When this returns `invalid_credentials` with
    correct credentials, ask CiiRUS support to whitelist Repull for the API user.

    The credentials are validated against CiiRUS before anything is stored, so invalid ones return
    `invalid_credentials` rather than creating a dead connection. On success only the credential fields
    below are stored, and the first sync of listings and reservations is queued.

    CiiRUS has no webhooks: after the first sync, reservation changes are picked up by polling about
    once a minute.

    Reconnecting replaces the stored credentials on the workspace's existing CiiRUS connection — the
    `pmsConnectionId` stays the same.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitCiirusCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SubmitCiirusCredentialsResponse200]
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
    body: SubmitCiirusCredentialsBody,

) -> Error | SubmitCiirusCredentialsResponse200 | None:
    """ Submit CiiRUS credentials for a Connect session

     Completes a credentials-pattern connection for CiiRUS with the property manager's CiiRUS API
    username and password.

    **What syncs.** Units become listings (with descriptions, photos, amenities, rooms and house rules);
    reservations (with their charge and tax breakdown and payments) and reviews are imported, then
    polled for changes. Bookings can be created, quoted, changed and cancelled in CiiRUS — see
    `capabilities.reservations` on `GET /v1/connect/ciirus`. Guest messages are not available through
    CiiRUS's API.

    **Where the credentials come from.** The CiiRUS API Explorer gives the API username and password
    after signing in with the CiiRUS MC username and company password; CiiRUS support can also issue
    them. Credentials that see several suppliers (management companies) also need
    `managementCompanyUserId`.

    **IP whitelist.** CiiRUS only accepts calls from whitelisted IP addresses, and answers a wrong
    password and a non-whitelisted address the same way. When this returns `invalid_credentials` with
    correct credentials, ask CiiRUS support to whitelist Repull for the API user.

    The credentials are validated against CiiRUS before anything is stored, so invalid ones return
    `invalid_credentials` rather than creating a dead connection. On success only the credential fields
    below are stored, and the first sync of listings and reservations is queued.

    CiiRUS has no webhooks: after the first sync, reservation changes are picked up by polling about
    once a minute.

    Reconnecting replaces the stored credentials on the workspace's existing CiiRUS connection — the
    `pmsConnectionId` stays the same.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitCiirusCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SubmitCiirusCredentialsResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
