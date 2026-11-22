from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.send_message_response import SendMessageResponse
from ...models.send_vrbo_message_body import SendVrboMessageBody
from typing import cast



def _get_kwargs(
    thread_id: str,
    *,
    body: SendVrboMessageBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/vrbo/messaging/{thread_id}/messages".format(thread_id=quote(str(thread_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SendMessageResponse | None:
    if response.status_code == 201:
        response_201 = SendMessageResponse.from_dict(response.json())



        return response_201

    if response.status_code == 202:
        response_202 = SendMessageResponse.from_dict(response.json())



        return response_202

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SendMessageResponse]:
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
    body: SendVrboMessageBody,

) -> Response[Error | SendMessageResponse]:
    r""" Send a Vrbo message

     Send a message in a Vrbo conversation through the host's connected Vrbo account — the counterpart of
    `POST /v1/channels/airbnb/messaging/{threadId}/messages`, with the same body. It is sent the way the
    dashboard sends it and recorded in the conversation, so it also appears on `GET
    /v1/conversations/{id}/messages`.

    `201` with `status: \"sent\"` when Vrbo took it; `202` with `status: \"queued\"` when Vrbo was slow
    and the send finishes in the background — do not send it again, watch
    `conversation.message.status_changed`. Vrbo messages are text: a `mediaUrl` is refused with `422
    attachments_not_supported`. Send `Idempotency-Key` to make a retry safe.

    Vrbo has no edit, unsend or reaction on a sent message (Airbnb's `PATCH …/messages/{messageId}`).

    Returns `403 listing_inactive` when the conversation's listing is inactive.

    Args:
        thread_id (str):  Example: vrbo:3f2a9c1e-5b7d-4e2a-9c1f-0a1b2c3d4e5f.
        body (SendVrboMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SendMessageResponse]
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
    body: SendVrboMessageBody,

) -> Error | SendMessageResponse | None:
    r""" Send a Vrbo message

     Send a message in a Vrbo conversation through the host's connected Vrbo account — the counterpart of
    `POST /v1/channels/airbnb/messaging/{threadId}/messages`, with the same body. It is sent the way the
    dashboard sends it and recorded in the conversation, so it also appears on `GET
    /v1/conversations/{id}/messages`.

    `201` with `status: \"sent\"` when Vrbo took it; `202` with `status: \"queued\"` when Vrbo was slow
    and the send finishes in the background — do not send it again, watch
    `conversation.message.status_changed`. Vrbo messages are text: a `mediaUrl` is refused with `422
    attachments_not_supported`. Send `Idempotency-Key` to make a retry safe.

    Vrbo has no edit, unsend or reaction on a sent message (Airbnb's `PATCH …/messages/{messageId}`).

    Returns `403 listing_inactive` when the conversation's listing is inactive.

    Args:
        thread_id (str):  Example: vrbo:3f2a9c1e-5b7d-4e2a-9c1f-0a1b2c3d4e5f.
        body (SendVrboMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SendMessageResponse
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
    body: SendVrboMessageBody,

) -> Response[Error | SendMessageResponse]:
    r""" Send a Vrbo message

     Send a message in a Vrbo conversation through the host's connected Vrbo account — the counterpart of
    `POST /v1/channels/airbnb/messaging/{threadId}/messages`, with the same body. It is sent the way the
    dashboard sends it and recorded in the conversation, so it also appears on `GET
    /v1/conversations/{id}/messages`.

    `201` with `status: \"sent\"` when Vrbo took it; `202` with `status: \"queued\"` when Vrbo was slow
    and the send finishes in the background — do not send it again, watch
    `conversation.message.status_changed`. Vrbo messages are text: a `mediaUrl` is refused with `422
    attachments_not_supported`. Send `Idempotency-Key` to make a retry safe.

    Vrbo has no edit, unsend or reaction on a sent message (Airbnb's `PATCH …/messages/{messageId}`).

    Returns `403 listing_inactive` when the conversation's listing is inactive.

    Args:
        thread_id (str):  Example: vrbo:3f2a9c1e-5b7d-4e2a-9c1f-0a1b2c3d4e5f.
        body (SendVrboMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SendMessageResponse]
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
    body: SendVrboMessageBody,

) -> Error | SendMessageResponse | None:
    r""" Send a Vrbo message

     Send a message in a Vrbo conversation through the host's connected Vrbo account — the counterpart of
    `POST /v1/channels/airbnb/messaging/{threadId}/messages`, with the same body. It is sent the way the
    dashboard sends it and recorded in the conversation, so it also appears on `GET
    /v1/conversations/{id}/messages`.

    `201` with `status: \"sent\"` when Vrbo took it; `202` with `status: \"queued\"` when Vrbo was slow
    and the send finishes in the background — do not send it again, watch
    `conversation.message.status_changed`. Vrbo messages are text: a `mediaUrl` is refused with `422
    attachments_not_supported`. Send `Idempotency-Key` to make a retry safe.

    Vrbo has no edit, unsend or reaction on a sent message (Airbnb's `PATCH …/messages/{messageId}`).

    Returns `403 listing_inactive` when the conversation's listing is inactive.

    Args:
        thread_id (str):  Example: vrbo:3f2a9c1e-5b7d-4e2a-9c1f-0a1b2c3d4e5f.
        body (SendVrboMessageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SendMessageResponse
     """


    return (await asyncio_detailed(
        thread_id=thread_id,
client=client,
body=body,

    )).parsed
