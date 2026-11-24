from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.start_connection_import_body import StartConnectionImportBody
from ...models.start_connection_import_response_202 import StartConnectionImportResponse202
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: StartConnectionImportBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connections/{id}/imports".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | StartConnectionImportResponse202 | None:
    if response.status_code == 202:
        response_202 = StartConnectionImportResponse202.from_dict(response.json())



        return response_202

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | StartConnectionImportResponse202]:
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
    body: StartConnectionImportBody | Unset = UNSET,

) -> Response[Error | StartConnectionImportResponse202]:
    """ Start an import of a connection

     Start an import of a connected Airbnb account now. Two scopes:

    **`full`** — the import that runs when an account is first connected, again: listings with their
    calendars (pricing and availability), reservations, then payouts, reviews and conversations. For an
    account that has never fully imported, e.g. a first import that never started or stalled. Returns
    `409 conflict` once the account has been fully imported (everything keeps syncing on its own after
    that).

    **`listings`** — picks up listings you've added on Airbnb since you connected. Re-reads the
    connected account's listings now: a new property comes in as a new listing, together with its
    calendar (pricing and availability), and existing listings are refreshed. On a full-access
    connection Repull is the source of your calendars, so the calendars of listings already in Repull
    are not re-read from Airbnb; on read-only and messaging connections they are. Nothing else is re-
    imported. The same import runs on its own once a day for every connected Airbnb account, and when
    the host reconnects.

    With no body, Repull chooses: `full` for an account that has never fully imported, `listings`
    otherwise.

    New listings obey your plan's active-listing limit: past it, and when the property is unlisted on
    Airbnb, they arrive inactive. Existing listings keep their status.

    Every scope runs in the background (`202`) and is recorded like any other import: follow it on `GET
    /v1/connections/{id}/imports` (`importId`, when returned, is its id there) or wait for
    `account.import.completed`. An import no worker picks up within 10 minutes ends `failed` with reason
    `did_not_start` (and `account.import.failed`); call this again. A `full` request also replaces such
    an import itself (`replacedImportId`).

    Airbnb connections only for now. Returns `409 conflict` while an import of the account is already
    running, and `409 connection_reauth_required` when the account is disconnected.

    Args:
        id (str):
        body (StartConnectionImportBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StartConnectionImportResponse202]
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
    body: StartConnectionImportBody | Unset = UNSET,

) -> Error | StartConnectionImportResponse202 | None:
    """ Start an import of a connection

     Start an import of a connected Airbnb account now. Two scopes:

    **`full`** — the import that runs when an account is first connected, again: listings with their
    calendars (pricing and availability), reservations, then payouts, reviews and conversations. For an
    account that has never fully imported, e.g. a first import that never started or stalled. Returns
    `409 conflict` once the account has been fully imported (everything keeps syncing on its own after
    that).

    **`listings`** — picks up listings you've added on Airbnb since you connected. Re-reads the
    connected account's listings now: a new property comes in as a new listing, together with its
    calendar (pricing and availability), and existing listings are refreshed. On a full-access
    connection Repull is the source of your calendars, so the calendars of listings already in Repull
    are not re-read from Airbnb; on read-only and messaging connections they are. Nothing else is re-
    imported. The same import runs on its own once a day for every connected Airbnb account, and when
    the host reconnects.

    With no body, Repull chooses: `full` for an account that has never fully imported, `listings`
    otherwise.

    New listings obey your plan's active-listing limit: past it, and when the property is unlisted on
    Airbnb, they arrive inactive. Existing listings keep their status.

    Every scope runs in the background (`202`) and is recorded like any other import: follow it on `GET
    /v1/connections/{id}/imports` (`importId`, when returned, is its id there) or wait for
    `account.import.completed`. An import no worker picks up within 10 minutes ends `failed` with reason
    `did_not_start` (and `account.import.failed`); call this again. A `full` request also replaces such
    an import itself (`replacedImportId`).

    Airbnb connections only for now. Returns `409 conflict` while an import of the account is already
    running, and `409 connection_reauth_required` when the account is disconnected.

    Args:
        id (str):
        body (StartConnectionImportBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StartConnectionImportResponse202
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
    body: StartConnectionImportBody | Unset = UNSET,

) -> Response[Error | StartConnectionImportResponse202]:
    """ Start an import of a connection

     Start an import of a connected Airbnb account now. Two scopes:

    **`full`** — the import that runs when an account is first connected, again: listings with their
    calendars (pricing and availability), reservations, then payouts, reviews and conversations. For an
    account that has never fully imported, e.g. a first import that never started or stalled. Returns
    `409 conflict` once the account has been fully imported (everything keeps syncing on its own after
    that).

    **`listings`** — picks up listings you've added on Airbnb since you connected. Re-reads the
    connected account's listings now: a new property comes in as a new listing, together with its
    calendar (pricing and availability), and existing listings are refreshed. On a full-access
    connection Repull is the source of your calendars, so the calendars of listings already in Repull
    are not re-read from Airbnb; on read-only and messaging connections they are. Nothing else is re-
    imported. The same import runs on its own once a day for every connected Airbnb account, and when
    the host reconnects.

    With no body, Repull chooses: `full` for an account that has never fully imported, `listings`
    otherwise.

    New listings obey your plan's active-listing limit: past it, and when the property is unlisted on
    Airbnb, they arrive inactive. Existing listings keep their status.

    Every scope runs in the background (`202`) and is recorded like any other import: follow it on `GET
    /v1/connections/{id}/imports` (`importId`, when returned, is its id there) or wait for
    `account.import.completed`. An import no worker picks up within 10 minutes ends `failed` with reason
    `did_not_start` (and `account.import.failed`); call this again. A `full` request also replaces such
    an import itself (`replacedImportId`).

    Airbnb connections only for now. Returns `409 conflict` while an import of the account is already
    running, and `409 connection_reauth_required` when the account is disconnected.

    Args:
        id (str):
        body (StartConnectionImportBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | StartConnectionImportResponse202]
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
    body: StartConnectionImportBody | Unset = UNSET,

) -> Error | StartConnectionImportResponse202 | None:
    """ Start an import of a connection

     Start an import of a connected Airbnb account now. Two scopes:

    **`full`** — the import that runs when an account is first connected, again: listings with their
    calendars (pricing and availability), reservations, then payouts, reviews and conversations. For an
    account that has never fully imported, e.g. a first import that never started or stalled. Returns
    `409 conflict` once the account has been fully imported (everything keeps syncing on its own after
    that).

    **`listings`** — picks up listings you've added on Airbnb since you connected. Re-reads the
    connected account's listings now: a new property comes in as a new listing, together with its
    calendar (pricing and availability), and existing listings are refreshed. On a full-access
    connection Repull is the source of your calendars, so the calendars of listings already in Repull
    are not re-read from Airbnb; on read-only and messaging connections they are. Nothing else is re-
    imported. The same import runs on its own once a day for every connected Airbnb account, and when
    the host reconnects.

    With no body, Repull chooses: `full` for an account that has never fully imported, `listings`
    otherwise.

    New listings obey your plan's active-listing limit: past it, and when the property is unlisted on
    Airbnb, they arrive inactive. Existing listings keep their status.

    Every scope runs in the background (`202`) and is recorded like any other import: follow it on `GET
    /v1/connections/{id}/imports` (`importId`, when returned, is its id there) or wait for
    `account.import.completed`. An import no worker picks up within 10 minutes ends `failed` with reason
    `did_not_start` (and `account.import.failed`); call this again. A `full` request also replaces such
    an import itself (`replacedImportId`).

    Airbnb connections only for now. Returns `409 conflict` while an import of the account is already
    running, and `409 connection_reauth_required` when the account is disconnected.

    Args:
        id (str):
        body (StartConnectionImportBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | StartConnectionImportResponse202
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
