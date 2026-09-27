from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.submit_cloudbeds_credentials_body import SubmitCloudbedsCredentialsBody
from ...models.submit_cloudbeds_credentials_response_200 import SubmitCloudbedsCredentialsResponse200
from typing import cast



def _get_kwargs(
    *,
    body: SubmitCloudbedsCredentialsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/cloudbeds/credentials",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SubmitCloudbedsCredentialsResponse200 | None:
    if response.status_code == 200:
        response_200 = SubmitCloudbedsCredentialsResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SubmitCloudbedsCredentialsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SubmitCloudbedsCredentialsBody,

) -> Response[Error | SubmitCloudbedsCredentialsResponse200]:
    """ Submit Cloudbeds credentials for a Connect session

     Completes a credentials-pattern connection for Cloudbeds with a property (or organization) API key,
    created in Cloudbeds under Apps & Marketplace → API Credentials.

    In Cloudbeds a listing is a room type and its rooms are units. A booking with several rooms becomes
    one reservation per room.

    The key is validated and the properties it can see are read before anything is stored. On success
    Repull subscribes to the property's Cloudbeds webhooks (reservations, guests, room blocks) and
    queues the first sync.

    Cloudbeds keys expire if unused for 30 days; the connection's regular sync keeps them alive.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitCloudbedsCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SubmitCloudbedsCredentialsResponse200]
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
    body: SubmitCloudbedsCredentialsBody,

) -> Error | SubmitCloudbedsCredentialsResponse200 | None:
    """ Submit Cloudbeds credentials for a Connect session

     Completes a credentials-pattern connection for Cloudbeds with a property (or organization) API key,
    created in Cloudbeds under Apps & Marketplace → API Credentials.

    In Cloudbeds a listing is a room type and its rooms are units. A booking with several rooms becomes
    one reservation per room.

    The key is validated and the properties it can see are read before anything is stored. On success
    Repull subscribes to the property's Cloudbeds webhooks (reservations, guests, room blocks) and
    queues the first sync.

    Cloudbeds keys expire if unused for 30 days; the connection's regular sync keeps them alive.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitCloudbedsCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SubmitCloudbedsCredentialsResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SubmitCloudbedsCredentialsBody,

) -> Response[Error | SubmitCloudbedsCredentialsResponse200]:
    """ Submit Cloudbeds credentials for a Connect session

     Completes a credentials-pattern connection for Cloudbeds with a property (or organization) API key,
    created in Cloudbeds under Apps & Marketplace → API Credentials.

    In Cloudbeds a listing is a room type and its rooms are units. A booking with several rooms becomes
    one reservation per room.

    The key is validated and the properties it can see are read before anything is stored. On success
    Repull subscribes to the property's Cloudbeds webhooks (reservations, guests, room blocks) and
    queues the first sync.

    Cloudbeds keys expire if unused for 30 days; the connection's regular sync keeps them alive.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitCloudbedsCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SubmitCloudbedsCredentialsResponse200]
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
    body: SubmitCloudbedsCredentialsBody,

) -> Error | SubmitCloudbedsCredentialsResponse200 | None:
    """ Submit Cloudbeds credentials for a Connect session

     Completes a credentials-pattern connection for Cloudbeds with a property (or organization) API key,
    created in Cloudbeds under Apps & Marketplace → API Credentials.

    In Cloudbeds a listing is a room type and its rooms are units. A booking with several rooms becomes
    one reservation per room.

    The key is validated and the properties it can see are read before anything is stored. On success
    Repull subscribes to the property's Cloudbeds webhooks (reservations, guests, room blocks) and
    queues the first sync.

    Cloudbeds keys expire if unused for 30 days; the connection's regular sync keeps them alive.

    No API key required when called with a `sessionId` — the session is the capability token.

    Args:
        body (SubmitCloudbedsCredentialsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SubmitCloudbedsCredentialsResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
