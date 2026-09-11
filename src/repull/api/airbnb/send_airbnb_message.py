from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.send_airbnb_message_body import SendAirbnbMessageBody
from typing import cast



def _get_kwargs(
    thread_id: str,
    *,
    body: SendAirbnbMessageBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/airbnb/messaging/{thread_id}/messages".format(thread_id=quote(str(thread_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendAirbnbMessageBody,

) -> Response[Any | Error]:
    """ Send Airbnb message

     Send a message in an Airbnb thread as the host. Airbnb enforces content rules (no off-platform
    contact info, no external URLs) — violating messages are rejected upstream and surface as
    `airbnb_error`.

    The `{threadId}` is the Airbnb thread id — the `externalThreadId` field on a unified `Conversation`
    (`GET /v1/conversations`).

    Args:
        thread_id (str):
        body (SendAirbnbMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        thread_id=thread_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendAirbnbMessageBody,

) -> Any | Error | None:
    """ Send Airbnb message

     Send a message in an Airbnb thread as the host. Airbnb enforces content rules (no off-platform
    contact info, no external URLs) — violating messages are rejected upstream and surface as
    `airbnb_error`.

    The `{threadId}` is the Airbnb thread id — the `externalThreadId` field on a unified `Conversation`
    (`GET /v1/conversations`).

    Args:
        thread_id (str):
        body (SendAirbnbMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        thread_id=thread_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendAirbnbMessageBody,

) -> Response[Any | Error]:
    """ Send Airbnb message

     Send a message in an Airbnb thread as the host. Airbnb enforces content rules (no off-platform
    contact info, no external URLs) — violating messages are rejected upstream and surface as
    `airbnb_error`.

    The `{threadId}` is the Airbnb thread id — the `externalThreadId` field on a unified `Conversation`
    (`GET /v1/conversations`).

    Args:
        thread_id (str):
        body (SendAirbnbMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        thread_id=thread_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    thread_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SendAirbnbMessageBody,

) -> Any | Error | None:
    """ Send Airbnb message

     Send a message in an Airbnb thread as the host. Airbnb enforces content rules (no off-platform
    contact info, no external URLs) — violating messages are rejected upstream and surface as
    `airbnb_error`.

    The `{threadId}` is the Airbnb thread id — the `externalThreadId` field on a unified `Conversation`
    (`GET /v1/conversations`).

    Args:
        thread_id (str):
        body (SendAirbnbMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        thread_id=thread_id,
client=client,
body=body,

    )).parsed
