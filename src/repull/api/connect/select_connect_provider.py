from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.select_connect_provider_body import SelectConnectProviderBody
from ...models.select_provider_response import SelectProviderResponse
from typing import cast



def _get_kwargs(
    session_id: str,
    *,
    body: SelectConnectProviderBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/sessions/{session_id}/select-provider".format(session_id=quote(str(session_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> SelectProviderResponse | None:
    if response.status_code == 200:
        response_200 = SelectProviderResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[SelectProviderResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SelectConnectProviderBody,

) -> Response[SelectProviderResponse]:
    """ Bind a picker session to a provider

     Called by the hosted picker page once the user clicks a channel card. Validates the provider exists
    and is permitted by the session's `allowed_providers` whitelist (if any), then returns the next-step
    URL the picker should navigate to.

    No API key required — the session ID is the capability token. The session must still be pending and
    unexpired.

    Args:
        session_id (str):
        body (SelectConnectProviderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SelectProviderResponse]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SelectConnectProviderBody,

) -> SelectProviderResponse | None:
    """ Bind a picker session to a provider

     Called by the hosted picker page once the user clicks a channel card. Validates the provider exists
    and is permitted by the session's `allowed_providers` whitelist (if any), then returns the next-step
    URL the picker should navigate to.

    No API key required — the session ID is the capability token. The session must still be pending and
    unexpired.

    Args:
        session_id (str):
        body (SelectConnectProviderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SelectProviderResponse
     """


    return sync_detailed(
        session_id=session_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SelectConnectProviderBody,

) -> Response[SelectProviderResponse]:
    """ Bind a picker session to a provider

     Called by the hosted picker page once the user clicks a channel card. Validates the provider exists
    and is permitted by the session's `allowed_providers` whitelist (if any), then returns the next-step
    URL the picker should navigate to.

    No API key required — the session ID is the capability token. The session must still be pending and
    unexpired.

    Args:
        session_id (str):
        body (SelectConnectProviderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SelectProviderResponse]
     """


    kwargs = _get_kwargs(
        session_id=session_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    session_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SelectConnectProviderBody,

) -> SelectProviderResponse | None:
    """ Bind a picker session to a provider

     Called by the hosted picker page once the user clicks a channel card. Validates the provider exists
    and is permitted by the session's `allowed_providers` whitelist (if any), then returns the next-step
    URL the picker should navigate to.

    No API key required — the session ID is the capability token. The session must still be pending and
    unexpired.

    Args:
        session_id (str):
        body (SelectConnectProviderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SelectProviderResponse
     """


    return (await asyncio_detailed(
        session_id=session_id,
client=client,
body=body,

    )).parsed
