from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.send_message_request import SendMessageRequest
from ...models.send_message_response import SendMessageResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: SendMessageRequest,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/conversations/{id}/messages".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SendMessageResponse | None:
    if response.status_code == 200:
        response_200 = SendMessageResponse.from_dict(response.json())



        return response_200

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

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: SendMessageRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | SendMessageResponse]:
    """ Send a message to the guest

     Sends a message to the guest on this conversation and records it in the thread.

    Omit `channel` and the message goes out on whichever channel the conversation already uses (Airbnb,
    Booking.com, SMS, email or the direct-booking site) — that is the right default. Pass `channel` only
    to force a specific one.

    The message is attributed to the API: it is recorded with `aiGenerated` false so an API send is
    never counted as an automated reply.

    ### Airbnb rewrites links — check `contentRewritten`

    Airbnb rejects guest messages containing a link, an email address or a phone number, and names the
    offending text. When that happens the offending fragment is stripped and the remainder is re-sent
    once, which means **the guest receives a message that is not the one you wrote**. Reporting that as
    a plain success would be a lie, so every response carries `contentRewritten`; when it is `true`,
    `deliveredContent` is the text that actually reached the guest. Check it before assuming your
    message went out verbatim.

    When the text cannot be salvaged (the link is most of the message) nothing is delivered and the call
    returns `422 message_not_sent` with the channel's verbatim refusal in `statusReason`.

    Send `Idempotency-Key` — without it, retrying after a network timeout sends the guest the same
    message twice.

    ### Attachments

    Send files with `attachments: [{ url, contentType?, filename? }]` — public `https://` URLs, up to 5
    per request, 10 MB each. `message` may be omitted when there are attachments (except on
    Booking.com). Repull downloads each file, reads its real type from the bytes, keeps a durable copy
    and delivers it through the channel's own file flow. **Every file is checked before anything is
    sent**: if one is unreachable, too large or of a type the channel refuses, the call returns 422
    naming the file (`index`) and the guest receives nothing.

    | Channel | Accepted types | Text | How it arrives |
    |---|---|---|---|
    | Airbnb | JPEG, PNG, GIF, WebP (converted to JPEG), MP4, QuickTime | optional | each file as its
    own message, then the text as a separate message |
    | Booking.com | JPEG, PNG | **required** | one message carrying the text and every file |
    | SMS, email, direct-booking site chat | — | — | `422 attachments_not_supported`, nothing sent |

    Airbnb does not allow files in pre-booking (inquiry) conversations; that refusal comes back as `422
    message_not_sent`. Because Airbnb delivers files one message at a time, a later file can be refused
    after earlier ones arrived — that returns `422 message_partially_sent` with `parts` saying exactly
    which messages reached the guest; resend only the rest.

    The response's `attachments` lists each file's durable `url`, and `parts` lists every channel
    message the send produced. Read-back (`GET /v1/conversations/{id}/messages`) shows the same files in
    each message's `attachments`.

    **Inactive listings:** a conversation that belongs to an inactive listing returns `403
    listing_inactive` and no message is sent. Activate the listing first.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (SendMessageRequest): `message`, `attachments`, or both. Per-channel limits for
            `attachments`:

            | Channel | Accepted types | Per file | Per request | Text |
            |---|---|---|---|---|
            | Airbnb | JPEG, PNG, GIF, WebP (sent as JPEG), MP4, QuickTime | 10 MB | 5 | optional —
            each file is sent as its own message, then the text |
            | Booking.com | JPEG, PNG | 10 MB | 5 | **required** — all files ride on the one text
            message |
            | SMS, email, direct-booking site chat | — | — | — | `422 attachments_not_supported`;
            nothing is sent |

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SendMessageResponse]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: SendMessageRequest,
    idempotency_key: str | Unset = UNSET,

) -> Error | SendMessageResponse | None:
    """ Send a message to the guest

     Sends a message to the guest on this conversation and records it in the thread.

    Omit `channel` and the message goes out on whichever channel the conversation already uses (Airbnb,
    Booking.com, SMS, email or the direct-booking site) — that is the right default. Pass `channel` only
    to force a specific one.

    The message is attributed to the API: it is recorded with `aiGenerated` false so an API send is
    never counted as an automated reply.

    ### Airbnb rewrites links — check `contentRewritten`

    Airbnb rejects guest messages containing a link, an email address or a phone number, and names the
    offending text. When that happens the offending fragment is stripped and the remainder is re-sent
    once, which means **the guest receives a message that is not the one you wrote**. Reporting that as
    a plain success would be a lie, so every response carries `contentRewritten`; when it is `true`,
    `deliveredContent` is the text that actually reached the guest. Check it before assuming your
    message went out verbatim.

    When the text cannot be salvaged (the link is most of the message) nothing is delivered and the call
    returns `422 message_not_sent` with the channel's verbatim refusal in `statusReason`.

    Send `Idempotency-Key` — without it, retrying after a network timeout sends the guest the same
    message twice.

    ### Attachments

    Send files with `attachments: [{ url, contentType?, filename? }]` — public `https://` URLs, up to 5
    per request, 10 MB each. `message` may be omitted when there are attachments (except on
    Booking.com). Repull downloads each file, reads its real type from the bytes, keeps a durable copy
    and delivers it through the channel's own file flow. **Every file is checked before anything is
    sent**: if one is unreachable, too large or of a type the channel refuses, the call returns 422
    naming the file (`index`) and the guest receives nothing.

    | Channel | Accepted types | Text | How it arrives |
    |---|---|---|---|
    | Airbnb | JPEG, PNG, GIF, WebP (converted to JPEG), MP4, QuickTime | optional | each file as its
    own message, then the text as a separate message |
    | Booking.com | JPEG, PNG | **required** | one message carrying the text and every file |
    | SMS, email, direct-booking site chat | — | — | `422 attachments_not_supported`, nothing sent |

    Airbnb does not allow files in pre-booking (inquiry) conversations; that refusal comes back as `422
    message_not_sent`. Because Airbnb delivers files one message at a time, a later file can be refused
    after earlier ones arrived — that returns `422 message_partially_sent` with `parts` saying exactly
    which messages reached the guest; resend only the rest.

    The response's `attachments` lists each file's durable `url`, and `parts` lists every channel
    message the send produced. Read-back (`GET /v1/conversations/{id}/messages`) shows the same files in
    each message's `attachments`.

    **Inactive listings:** a conversation that belongs to an inactive listing returns `403
    listing_inactive` and no message is sent. Activate the listing first.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (SendMessageRequest): `message`, `attachments`, or both. Per-channel limits for
            `attachments`:

            | Channel | Accepted types | Per file | Per request | Text |
            |---|---|---|---|---|
            | Airbnb | JPEG, PNG, GIF, WebP (sent as JPEG), MP4, QuickTime | 10 MB | 5 | optional —
            each file is sent as its own message, then the text |
            | Booking.com | JPEG, PNG | 10 MB | 5 | **required** — all files ride on the one text
            message |
            | SMS, email, direct-booking site chat | — | — | — | `422 attachments_not_supported`;
            nothing is sent |

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SendMessageResponse
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: SendMessageRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | SendMessageResponse]:
    """ Send a message to the guest

     Sends a message to the guest on this conversation and records it in the thread.

    Omit `channel` and the message goes out on whichever channel the conversation already uses (Airbnb,
    Booking.com, SMS, email or the direct-booking site) — that is the right default. Pass `channel` only
    to force a specific one.

    The message is attributed to the API: it is recorded with `aiGenerated` false so an API send is
    never counted as an automated reply.

    ### Airbnb rewrites links — check `contentRewritten`

    Airbnb rejects guest messages containing a link, an email address or a phone number, and names the
    offending text. When that happens the offending fragment is stripped and the remainder is re-sent
    once, which means **the guest receives a message that is not the one you wrote**. Reporting that as
    a plain success would be a lie, so every response carries `contentRewritten`; when it is `true`,
    `deliveredContent` is the text that actually reached the guest. Check it before assuming your
    message went out verbatim.

    When the text cannot be salvaged (the link is most of the message) nothing is delivered and the call
    returns `422 message_not_sent` with the channel's verbatim refusal in `statusReason`.

    Send `Idempotency-Key` — without it, retrying after a network timeout sends the guest the same
    message twice.

    ### Attachments

    Send files with `attachments: [{ url, contentType?, filename? }]` — public `https://` URLs, up to 5
    per request, 10 MB each. `message` may be omitted when there are attachments (except on
    Booking.com). Repull downloads each file, reads its real type from the bytes, keeps a durable copy
    and delivers it through the channel's own file flow. **Every file is checked before anything is
    sent**: if one is unreachable, too large or of a type the channel refuses, the call returns 422
    naming the file (`index`) and the guest receives nothing.

    | Channel | Accepted types | Text | How it arrives |
    |---|---|---|---|
    | Airbnb | JPEG, PNG, GIF, WebP (converted to JPEG), MP4, QuickTime | optional | each file as its
    own message, then the text as a separate message |
    | Booking.com | JPEG, PNG | **required** | one message carrying the text and every file |
    | SMS, email, direct-booking site chat | — | — | `422 attachments_not_supported`, nothing sent |

    Airbnb does not allow files in pre-booking (inquiry) conversations; that refusal comes back as `422
    message_not_sent`. Because Airbnb delivers files one message at a time, a later file can be refused
    after earlier ones arrived — that returns `422 message_partially_sent` with `parts` saying exactly
    which messages reached the guest; resend only the rest.

    The response's `attachments` lists each file's durable `url`, and `parts` lists every channel
    message the send produced. Read-back (`GET /v1/conversations/{id}/messages`) shows the same files in
    each message's `attachments`.

    **Inactive listings:** a conversation that belongs to an inactive listing returns `403
    listing_inactive` and no message is sent. Activate the listing first.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (SendMessageRequest): `message`, `attachments`, or both. Per-channel limits for
            `attachments`:

            | Channel | Accepted types | Per file | Per request | Text |
            |---|---|---|---|---|
            | Airbnb | JPEG, PNG, GIF, WebP (sent as JPEG), MP4, QuickTime | 10 MB | 5 | optional —
            each file is sent as its own message, then the text |
            | Booking.com | JPEG, PNG | 10 MB | 5 | **required** — all files ride on the one text
            message |
            | SMS, email, direct-booking site chat | — | — | — | `422 attachments_not_supported`;
            nothing is sent |

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SendMessageResponse]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: SendMessageRequest,
    idempotency_key: str | Unset = UNSET,

) -> Error | SendMessageResponse | None:
    """ Send a message to the guest

     Sends a message to the guest on this conversation and records it in the thread.

    Omit `channel` and the message goes out on whichever channel the conversation already uses (Airbnb,
    Booking.com, SMS, email or the direct-booking site) — that is the right default. Pass `channel` only
    to force a specific one.

    The message is attributed to the API: it is recorded with `aiGenerated` false so an API send is
    never counted as an automated reply.

    ### Airbnb rewrites links — check `contentRewritten`

    Airbnb rejects guest messages containing a link, an email address or a phone number, and names the
    offending text. When that happens the offending fragment is stripped and the remainder is re-sent
    once, which means **the guest receives a message that is not the one you wrote**. Reporting that as
    a plain success would be a lie, so every response carries `contentRewritten`; when it is `true`,
    `deliveredContent` is the text that actually reached the guest. Check it before assuming your
    message went out verbatim.

    When the text cannot be salvaged (the link is most of the message) nothing is delivered and the call
    returns `422 message_not_sent` with the channel's verbatim refusal in `statusReason`.

    Send `Idempotency-Key` — without it, retrying after a network timeout sends the guest the same
    message twice.

    ### Attachments

    Send files with `attachments: [{ url, contentType?, filename? }]` — public `https://` URLs, up to 5
    per request, 10 MB each. `message` may be omitted when there are attachments (except on
    Booking.com). Repull downloads each file, reads its real type from the bytes, keeps a durable copy
    and delivers it through the channel's own file flow. **Every file is checked before anything is
    sent**: if one is unreachable, too large or of a type the channel refuses, the call returns 422
    naming the file (`index`) and the guest receives nothing.

    | Channel | Accepted types | Text | How it arrives |
    |---|---|---|---|
    | Airbnb | JPEG, PNG, GIF, WebP (converted to JPEG), MP4, QuickTime | optional | each file as its
    own message, then the text as a separate message |
    | Booking.com | JPEG, PNG | **required** | one message carrying the text and every file |
    | SMS, email, direct-booking site chat | — | — | `422 attachments_not_supported`, nothing sent |

    Airbnb does not allow files in pre-booking (inquiry) conversations; that refusal comes back as `422
    message_not_sent`. Because Airbnb delivers files one message at a time, a later file can be refused
    after earlier ones arrived — that returns `422 message_partially_sent` with `parts` saying exactly
    which messages reached the guest; resend only the rest.

    The response's `attachments` lists each file's durable `url`, and `parts` lists every channel
    message the send produced. Read-back (`GET /v1/conversations/{id}/messages`) shows the same files in
    each message's `attachments`.

    **Inactive listings:** a conversation that belongs to an inactive listing returns `403
    listing_inactive` and no message is sent. Activate the listing first.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (SendMessageRequest): `message`, `attachments`, or both. Per-channel limits for
            `attachments`:

            | Channel | Accepted types | Per file | Per request | Text |
            |---|---|---|---|---|
            | Airbnb | JPEG, PNG, GIF, WebP (sent as JPEG), MP4, QuickTime | 10 MB | 5 | optional —
            each file is sent as its own message, then the text |
            | Booking.com | JPEG, PNG | 10 MB | 5 | **required** — all files ride on the one text
            message |
            | SMS, email, direct-booking site chat | — | — | — | `422 attachments_not_supported`;
            nothing is sent |

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SendMessageResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
