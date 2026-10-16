from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_connection_imports_response_200 import ListConnectionImportsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    limit: int | Unset = 20,
    session_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["sessionId"] = session_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connections/{id}/imports".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListConnectionImportsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListConnectionImportsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListConnectionImportsResponse200]:
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
    limit: int | Unset = 20,
    session_id: str | Unset = UNSET,

) -> Response[Error | ListConnectionImportsResponse200]:
    """ List a connection's imports

     The import runs of one connected account, newest first: the first sync after connecting, a room or
    unit mapped later, a reconnect, a re-sync. Each run says where it stands (`running`, `completed`,
    `failed`), its stages and what it imported.

    To know when an account's first sync is done, wait for the `account.import.completed` webhook, or
    poll this endpoint (or `GET /v1/connect`, whose connections carry their latest `import`) until the
    newest run is no longer `running`.

    Auth: a Repull API key, or a Connect session token (`sessionId`).

    Args:
        id (str):
        limit (int | Unset):  Default: 20.
        session_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListConnectionImportsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
limit=limit,
session_id=session_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    session_id: str | Unset = UNSET,

) -> Error | ListConnectionImportsResponse200 | None:
    """ List a connection's imports

     The import runs of one connected account, newest first: the first sync after connecting, a room or
    unit mapped later, a reconnect, a re-sync. Each run says where it stands (`running`, `completed`,
    `failed`), its stages and what it imported.

    To know when an account's first sync is done, wait for the `account.import.completed` webhook, or
    poll this endpoint (or `GET /v1/connect`, whose connections carry their latest `import`) until the
    newest run is no longer `running`.

    Auth: a Repull API key, or a Connect session token (`sessionId`).

    Args:
        id (str):
        limit (int | Unset):  Default: 20.
        session_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListConnectionImportsResponse200
     """


    return sync_detailed(
        id=id,
client=client,
limit=limit,
session_id=session_id,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    session_id: str | Unset = UNSET,

) -> Response[Error | ListConnectionImportsResponse200]:
    """ List a connection's imports

     The import runs of one connected account, newest first: the first sync after connecting, a room or
    unit mapped later, a reconnect, a re-sync. Each run says where it stands (`running`, `completed`,
    `failed`), its stages and what it imported.

    To know when an account's first sync is done, wait for the `account.import.completed` webhook, or
    poll this endpoint (or `GET /v1/connect`, whose connections carry their latest `import`) until the
    newest run is no longer `running`.

    Auth: a Repull API key, or a Connect session token (`sessionId`).

    Args:
        id (str):
        limit (int | Unset):  Default: 20.
        session_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListConnectionImportsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
limit=limit,
session_id=session_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    session_id: str | Unset = UNSET,

) -> Error | ListConnectionImportsResponse200 | None:
    """ List a connection's imports

     The import runs of one connected account, newest first: the first sync after connecting, a room or
    unit mapped later, a reconnect, a re-sync. Each run says where it stands (`running`, `completed`,
    `failed`), its stages and what it imported.

    To know when an account's first sync is done, wait for the `account.import.completed` webhook, or
    poll this endpoint (or `GET /v1/connect`, whose connections carry their latest `import`) until the
    newest run is no longer `running`.

    Auth: a Repull API key, or a Connect session token (`sessionId`).

    Args:
        id (str):
        limit (int | Unset):  Default: 20.
        session_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListConnectionImportsResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
limit=limit,
session_id=session_id,

    )).parsed
