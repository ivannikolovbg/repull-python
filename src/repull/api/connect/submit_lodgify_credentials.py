from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.submit_lodgify_credentials_body import SubmitLodgifyCredentialsBody
from ...models.submit_lodgify_credentials_response_200 import SubmitLodgifyCredentialsResponse200
from typing import cast



def _get_kwargs(
    *,
    body: SubmitLodgifyCredentialsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/lodgify/credentials",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SubmitLodgifyCredentialsResponse200 | None:
    if response.status_code == 200:
        response_200 = SubmitLodgifyCredentialsResponse200.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SubmitLodgifyCredentialsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SubmitLodgifyCredentialsBody,

) -> Response[Error | SubmitLodgifyCredentialsResponse200]:
    """ Submit Lodgify credentials for a Connect session

     Completes a credentials-pattern connection for Lodgify. API key from Lodgify → Settings → Public
    API.

    The credentials are validated against Lodgify before anything is persisted, so an invalid pair
    returns `invalid_credentials` rather than creating a dead connection. On success the
    `pms_connections` row is written and the Connect session moves to its terminal state.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitLodgifyCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SubmitLodgifyCredentialsResponse200]
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
    body: SubmitLodgifyCredentialsBody,

) -> Error | SubmitLodgifyCredentialsResponse200 | None:
    """ Submit Lodgify credentials for a Connect session

     Completes a credentials-pattern connection for Lodgify. API key from Lodgify → Settings → Public
    API.

    The credentials are validated against Lodgify before anything is persisted, so an invalid pair
    returns `invalid_credentials` rather than creating a dead connection. On success the
    `pms_connections` row is written and the Connect session moves to its terminal state.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitLodgifyCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SubmitLodgifyCredentialsResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SubmitLodgifyCredentialsBody,

) -> Response[Error | SubmitLodgifyCredentialsResponse200]:
    """ Submit Lodgify credentials for a Connect session

     Completes a credentials-pattern connection for Lodgify. API key from Lodgify → Settings → Public
    API.

    The credentials are validated against Lodgify before anything is persisted, so an invalid pair
    returns `invalid_credentials` rather than creating a dead connection. On success the
    `pms_connections` row is written and the Connect session moves to its terminal state.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitLodgifyCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SubmitLodgifyCredentialsResponse200]
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
    body: SubmitLodgifyCredentialsBody,

) -> Error | SubmitLodgifyCredentialsResponse200 | None:
    """ Submit Lodgify credentials for a Connect session

     Completes a credentials-pattern connection for Lodgify. API key from Lodgify → Settings → Public
    API.

    The credentials are validated against Lodgify before anything is persisted, so an invalid pair
    returns `invalid_credentials` rather than creating a dead connection. On success the
    `pms_connections` row is written and the Connect session moves to its terminal state.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitLodgifyCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SubmitLodgifyCredentialsResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
