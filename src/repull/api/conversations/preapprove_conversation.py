from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.preapprove_conversation_body import PreapproveConversationBody
from ...models.preapprove_conversation_response_201 import PreapproveConversationResponse201
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: PreapproveConversationBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/conversations/{id}/pre-approval".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PreapproveConversationResponse201 | None:
    if response.status_code == 201:
        response_201 = PreapproveConversationResponse201.from_dict(response.json())



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

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PreapproveConversationResponse201]:
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
    body: PreapproveConversationBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | PreapproveConversationResponse201]:
    """ Pre-approve an inquiry

     Pre-approve the Airbnb inquiry on this conversation: the guest who asked about dates may now book
    them at the listed price, without waiting on you. To change the dates, guests or price, send a
    special offer instead (`POST /v1/conversations/{id}/special-offers`).

    Find inquiries that need an answer with `GET /v1/inquiries` (default `status=open`); each carries
    the `conversationId` to use here.

    **Airbnb only**, and only for listings connected to Airbnb directly. A Booking.com, VRBO or direct-
    booking conversation, or an Airbnb one relayed through a PMS (Hostaway, Guesty), returns `422
    channel_not_supported` and nothing is sent.

    Runs the same action as the Vanio dashboard’s Pre-approve button, so the inquiry is marked
    `pre_approved` everywhere.

    An Airbnb refusal is never reported as a success: an inquiry that already moved on is `409
    inquiry_no_longer_open`, an expired one `409 inquiry_expired`, a conversation that already has a
    booking `409 conversation_already_booked`.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (PreapproveConversationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PreapproveConversationResponse201]
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
    body: PreapproveConversationBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Error | PreapproveConversationResponse201 | None:
    """ Pre-approve an inquiry

     Pre-approve the Airbnb inquiry on this conversation: the guest who asked about dates may now book
    them at the listed price, without waiting on you. To change the dates, guests or price, send a
    special offer instead (`POST /v1/conversations/{id}/special-offers`).

    Find inquiries that need an answer with `GET /v1/inquiries` (default `status=open`); each carries
    the `conversationId` to use here.

    **Airbnb only**, and only for listings connected to Airbnb directly. A Booking.com, VRBO or direct-
    booking conversation, or an Airbnb one relayed through a PMS (Hostaway, Guesty), returns `422
    channel_not_supported` and nothing is sent.

    Runs the same action as the Vanio dashboard’s Pre-approve button, so the inquiry is marked
    `pre_approved` everywhere.

    An Airbnb refusal is never reported as a success: an inquiry that already moved on is `409
    inquiry_no_longer_open`, an expired one `409 inquiry_expired`, a conversation that already has a
    booking `409 conversation_already_booked`.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (PreapproveConversationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PreapproveConversationResponse201
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
    body: PreapproveConversationBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | PreapproveConversationResponse201]:
    """ Pre-approve an inquiry

     Pre-approve the Airbnb inquiry on this conversation: the guest who asked about dates may now book
    them at the listed price, without waiting on you. To change the dates, guests or price, send a
    special offer instead (`POST /v1/conversations/{id}/special-offers`).

    Find inquiries that need an answer with `GET /v1/inquiries` (default `status=open`); each carries
    the `conversationId` to use here.

    **Airbnb only**, and only for listings connected to Airbnb directly. A Booking.com, VRBO or direct-
    booking conversation, or an Airbnb one relayed through a PMS (Hostaway, Guesty), returns `422
    channel_not_supported` and nothing is sent.

    Runs the same action as the Vanio dashboard’s Pre-approve button, so the inquiry is marked
    `pre_approved` everywhere.

    An Airbnb refusal is never reported as a success: an inquiry that already moved on is `409
    inquiry_no_longer_open`, an expired one `409 inquiry_expired`, a conversation that already has a
    booking `409 conversation_already_booked`.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (PreapproveConversationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PreapproveConversationResponse201]
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
    body: PreapproveConversationBody | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Error | PreapproveConversationResponse201 | None:
    """ Pre-approve an inquiry

     Pre-approve the Airbnb inquiry on this conversation: the guest who asked about dates may now book
    them at the listed price, without waiting on you. To change the dates, guests or price, send a
    special offer instead (`POST /v1/conversations/{id}/special-offers`).

    Find inquiries that need an answer with `GET /v1/inquiries` (default `status=open`); each carries
    the `conversationId` to use here.

    **Airbnb only**, and only for listings connected to Airbnb directly. A Booking.com, VRBO or direct-
    booking conversation, or an Airbnb one relayed through a PMS (Hostaway, Guesty), returns `422
    channel_not_supported` and nothing is sent.

    Runs the same action as the Vanio dashboard’s Pre-approve button, so the inquiry is marked
    `pre_approved` everywhere.

    An Airbnb refusal is never reported as a success: an inquiry that already moved on is `409
    inquiry_no_longer_open`, an expired one `409 inquiry_expired`, a conversation that already has a
    booking `409 conversation_already_booked`.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (PreapproveConversationBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PreapproveConversationResponse201
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
