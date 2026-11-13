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
    """ Refresh a connection's listings

     Refresh listings: picks up listings you've added on Airbnb since you connected. Re-reads the
    connected account's listings and their calendars (pricing and availability) now; a new property
    comes in as a new listing and existing listings are refreshed. Nothing else is re-imported: no
    reservations, conversations, reviews or payouts.

    The same import runs on its own once a day for every connected Airbnb account, and when the host
    reconnects. Call this when you know a property was just added and do not want to wait.

    New listings obey your plan's active-listing limit: past it, and when the property is unlisted on
    Airbnb, they arrive inactive. Existing listings keep their status.

    The import runs in the background (`202`). It is recorded like any other import (trigger `resync`,
    one `listings` stage): follow it on `GET /v1/connections/{id}/imports` or wait for
    `account.import.completed`, then read the new listings with `GET /v1/listings`.

    Airbnb connections only for now. Returns `409 conflict` while a listings import of the account is
    already running, and `409 connection_reauth_required` when the account is disconnected.

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
    """ Refresh a connection's listings

     Refresh listings: picks up listings you've added on Airbnb since you connected. Re-reads the
    connected account's listings and their calendars (pricing and availability) now; a new property
    comes in as a new listing and existing listings are refreshed. Nothing else is re-imported: no
    reservations, conversations, reviews or payouts.

    The same import runs on its own once a day for every connected Airbnb account, and when the host
    reconnects. Call this when you know a property was just added and do not want to wait.

    New listings obey your plan's active-listing limit: past it, and when the property is unlisted on
    Airbnb, they arrive inactive. Existing listings keep their status.

    The import runs in the background (`202`). It is recorded like any other import (trigger `resync`,
    one `listings` stage): follow it on `GET /v1/connections/{id}/imports` or wait for
    `account.import.completed`, then read the new listings with `GET /v1/listings`.

    Airbnb connections only for now. Returns `409 conflict` while a listings import of the account is
    already running, and `409 connection_reauth_required` when the account is disconnected.

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
    """ Refresh a connection's listings

     Refresh listings: picks up listings you've added on Airbnb since you connected. Re-reads the
    connected account's listings and their calendars (pricing and availability) now; a new property
    comes in as a new listing and existing listings are refreshed. Nothing else is re-imported: no
    reservations, conversations, reviews or payouts.

    The same import runs on its own once a day for every connected Airbnb account, and when the host
    reconnects. Call this when you know a property was just added and do not want to wait.

    New listings obey your plan's active-listing limit: past it, and when the property is unlisted on
    Airbnb, they arrive inactive. Existing listings keep their status.

    The import runs in the background (`202`). It is recorded like any other import (trigger `resync`,
    one `listings` stage): follow it on `GET /v1/connections/{id}/imports` or wait for
    `account.import.completed`, then read the new listings with `GET /v1/listings`.

    Airbnb connections only for now. Returns `409 conflict` while a listings import of the account is
    already running, and `409 connection_reauth_required` when the account is disconnected.

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
    """ Refresh a connection's listings

     Refresh listings: picks up listings you've added on Airbnb since you connected. Re-reads the
    connected account's listings and their calendars (pricing and availability) now; a new property
    comes in as a new listing and existing listings are refreshed. Nothing else is re-imported: no
    reservations, conversations, reviews or payouts.

    The same import runs on its own once a day for every connected Airbnb account, and when the host
    reconnects. Call this when you know a property was just added and do not want to wait.

    New listings obey your plan's active-listing limit: past it, and when the property is unlisted on
    Airbnb, they arrive inactive. Existing listings keep their status.

    The import runs in the background (`202`). It is recorded like any other import (trigger `resync`,
    one `listings` stage): follow it on `GET /v1/connections/{id}/imports` or wait for
    `account.import.completed`, then read the new listings with `GET /v1/listings`.

    Airbnb connections only for now. Returns `409 conflict` while a listings import of the account is
    already running, and `409 connection_reauth_required` when the account is disconnected.

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
