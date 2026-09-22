from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.send_airbnb_message_body import SendAirbnbMessageBody
from ...models.send_airbnb_message_response_201_type_1 import SendAirbnbMessageResponse201Type1
from ...models.send_message_response import SendMessageResponse
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



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SendAirbnbMessageResponse201Type1 | SendMessageResponse | None:
    if response.status_code == 201:
        def _parse_response_201(data: object) -> SendAirbnbMessageResponse201Type1 | SendMessageResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0 = SendMessageResponse.from_dict(data)



                return response_201_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_201_type_1 = SendAirbnbMessageResponse201Type1.from_dict(data)



            return response_201_type_1

        response_201 = _parse_response_201(response.json())

        return response_201

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SendAirbnbMessageResponse201Type1 | SendMessageResponse]:
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

) -> Response[Error | SendAirbnbMessageResponse201Type1 | SendMessageResponse]:
    """ Send Airbnb message

     Send a message in an Airbnb thread as the host. Airbnb enforces content rules (no off-platform
    contact info, no external URLs) — violating messages are rejected upstream and surface as
    `airbnb_error`.

    ### Sending a photo or video (`mediaUrl`)

    Airbnb only accepts media uploaded to a signed URL it issues, one file per message and no text on
    the same message. With `mediaUrl`, Repull downloads the file (public `https://` only, 10 MB max),
    reads its real type from the bytes (JPEG, PNG, GIF, WebP — converted to JPEG — or MP4/QuickTime),
    uploads it to Airbnb and sends it; `message`, if given, follows as a separate message. This is the
    same flow as `POST /v1/conversations/{id}/messages` with `attachments` — prefer that endpoint, which
    also takes several files per request. The response is a `SendMessageResponse`, the send is recorded
    in the conversation, and failures are the 422 codes documented there
    (`attachment_type_not_supported`, `attachment_too_large`, `message_not_sent` for a pre-booking
    thread, …). The thread must already be synced to Repull (`GET /v1/conversations` lists them),
    otherwise `404`.

    Text-only sends (no `mediaUrl`) go straight to Airbnb and return Airbnb's message object.

    The `{threadId}` is the Airbnb thread id — the `externalThreadId` field on a unified `Conversation`
    (`GET /v1/conversations`).

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        thread_id (str):
        body (SendAirbnbMessageBody): `message`, `mediaUrl`, or both.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SendAirbnbMessageResponse201Type1 | SendMessageResponse]
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

) -> Error | SendAirbnbMessageResponse201Type1 | SendMessageResponse | None:
    """ Send Airbnb message

     Send a message in an Airbnb thread as the host. Airbnb enforces content rules (no off-platform
    contact info, no external URLs) — violating messages are rejected upstream and surface as
    `airbnb_error`.

    ### Sending a photo or video (`mediaUrl`)

    Airbnb only accepts media uploaded to a signed URL it issues, one file per message and no text on
    the same message. With `mediaUrl`, Repull downloads the file (public `https://` only, 10 MB max),
    reads its real type from the bytes (JPEG, PNG, GIF, WebP — converted to JPEG — or MP4/QuickTime),
    uploads it to Airbnb and sends it; `message`, if given, follows as a separate message. This is the
    same flow as `POST /v1/conversations/{id}/messages` with `attachments` — prefer that endpoint, which
    also takes several files per request. The response is a `SendMessageResponse`, the send is recorded
    in the conversation, and failures are the 422 codes documented there
    (`attachment_type_not_supported`, `attachment_too_large`, `message_not_sent` for a pre-booking
    thread, …). The thread must already be synced to Repull (`GET /v1/conversations` lists them),
    otherwise `404`.

    Text-only sends (no `mediaUrl`) go straight to Airbnb and return Airbnb's message object.

    The `{threadId}` is the Airbnb thread id — the `externalThreadId` field on a unified `Conversation`
    (`GET /v1/conversations`).

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        thread_id (str):
        body (SendAirbnbMessageBody): `message`, `mediaUrl`, or both.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SendAirbnbMessageResponse201Type1 | SendMessageResponse
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

) -> Response[Error | SendAirbnbMessageResponse201Type1 | SendMessageResponse]:
    """ Send Airbnb message

     Send a message in an Airbnb thread as the host. Airbnb enforces content rules (no off-platform
    contact info, no external URLs) — violating messages are rejected upstream and surface as
    `airbnb_error`.

    ### Sending a photo or video (`mediaUrl`)

    Airbnb only accepts media uploaded to a signed URL it issues, one file per message and no text on
    the same message. With `mediaUrl`, Repull downloads the file (public `https://` only, 10 MB max),
    reads its real type from the bytes (JPEG, PNG, GIF, WebP — converted to JPEG — or MP4/QuickTime),
    uploads it to Airbnb and sends it; `message`, if given, follows as a separate message. This is the
    same flow as `POST /v1/conversations/{id}/messages` with `attachments` — prefer that endpoint, which
    also takes several files per request. The response is a `SendMessageResponse`, the send is recorded
    in the conversation, and failures are the 422 codes documented there
    (`attachment_type_not_supported`, `attachment_too_large`, `message_not_sent` for a pre-booking
    thread, …). The thread must already be synced to Repull (`GET /v1/conversations` lists them),
    otherwise `404`.

    Text-only sends (no `mediaUrl`) go straight to Airbnb and return Airbnb's message object.

    The `{threadId}` is the Airbnb thread id — the `externalThreadId` field on a unified `Conversation`
    (`GET /v1/conversations`).

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        thread_id (str):
        body (SendAirbnbMessageBody): `message`, `mediaUrl`, or both.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SendAirbnbMessageResponse201Type1 | SendMessageResponse]
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

) -> Error | SendAirbnbMessageResponse201Type1 | SendMessageResponse | None:
    """ Send Airbnb message

     Send a message in an Airbnb thread as the host. Airbnb enforces content rules (no off-platform
    contact info, no external URLs) — violating messages are rejected upstream and surface as
    `airbnb_error`.

    ### Sending a photo or video (`mediaUrl`)

    Airbnb only accepts media uploaded to a signed URL it issues, one file per message and no text on
    the same message. With `mediaUrl`, Repull downloads the file (public `https://` only, 10 MB max),
    reads its real type from the bytes (JPEG, PNG, GIF, WebP — converted to JPEG — or MP4/QuickTime),
    uploads it to Airbnb and sends it; `message`, if given, follows as a separate message. This is the
    same flow as `POST /v1/conversations/{id}/messages` with `attachments` — prefer that endpoint, which
    also takes several files per request. The response is a `SendMessageResponse`, the send is recorded
    in the conversation, and failures are the 422 codes documented there
    (`attachment_type_not_supported`, `attachment_too_large`, `message_not_sent` for a pre-booking
    thread, …). The thread must already be synced to Repull (`GET /v1/conversations` lists them),
    otherwise `404`.

    Text-only sends (no `mediaUrl`) go straight to Airbnb and return Airbnb's message object.

    The `{threadId}` is the Airbnb thread id — the `externalThreadId` field on a unified `Conversation`
    (`GET /v1/conversations`).

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        thread_id (str):
        body (SendAirbnbMessageBody): `message`, `mediaUrl`, or both.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SendAirbnbMessageResponse201Type1 | SendMessageResponse
     """


    return (await asyncio_detailed(
        thread_id=thread_id,
client=client,
body=body,

    )).parsed
