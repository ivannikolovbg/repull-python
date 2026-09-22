from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.replay_webhook_delivery_body import ReplayWebhookDeliveryBody
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    delivery_id: UUID,
    *,
    body: ReplayWebhookDeliveryBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/webhooks/{id}/deliveries/{delivery_id}/replay".format(id=quote(str(id), safe=""),delivery_id=quote(str(delivery_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

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
    id: UUID,
    delivery_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ReplayWebhookDeliveryBody | Unset = UNSET,

) -> Response[Any | Error]:
    r""" Replay webhook delivery

     Re-sends the original payload (same eventId, fresh deliveryId, attempt + 1).

    A delivery may be replayed at most **3 times per rolling 60 minutes**; the 4th inside that window
    answers `409 replay_limit_reached` and names the time the next one is allowed. The limit is charged
    to the original delivery, so replaying the delivery a replay produced draws on the same budget. It
    is not a lifetime cap — a delivery that has not been replayed for an hour starts fresh.

    A delivery your endpoint already accepted is not re-sent (it would be a duplicate) and answers `409
    delivery_already_succeeded`; send `{\"force\": true}` to replay it anyway, which still counts
    against the limit.

    A delivery about a listing that is inactive now is not re-sent and answers `403 listing_inactive`;
    activate the listing first.

    Args:
        id (UUID):
        delivery_id (UUID):
        body (ReplayWebhookDeliveryBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        id=id,
delivery_id=delivery_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    delivery_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ReplayWebhookDeliveryBody | Unset = UNSET,

) -> Any | Error | None:
    r""" Replay webhook delivery

     Re-sends the original payload (same eventId, fresh deliveryId, attempt + 1).

    A delivery may be replayed at most **3 times per rolling 60 minutes**; the 4th inside that window
    answers `409 replay_limit_reached` and names the time the next one is allowed. The limit is charged
    to the original delivery, so replaying the delivery a replay produced draws on the same budget. It
    is not a lifetime cap — a delivery that has not been replayed for an hour starts fresh.

    A delivery your endpoint already accepted is not re-sent (it would be a duplicate) and answers `409
    delivery_already_succeeded`; send `{\"force\": true}` to replay it anyway, which still counts
    against the limit.

    A delivery about a listing that is inactive now is not re-sent and answers `403 listing_inactive`;
    activate the listing first.

    Args:
        id (UUID):
        delivery_id (UUID):
        body (ReplayWebhookDeliveryBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        id=id,
delivery_id=delivery_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    delivery_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ReplayWebhookDeliveryBody | Unset = UNSET,

) -> Response[Any | Error]:
    r""" Replay webhook delivery

     Re-sends the original payload (same eventId, fresh deliveryId, attempt + 1).

    A delivery may be replayed at most **3 times per rolling 60 minutes**; the 4th inside that window
    answers `409 replay_limit_reached` and names the time the next one is allowed. The limit is charged
    to the original delivery, so replaying the delivery a replay produced draws on the same budget. It
    is not a lifetime cap — a delivery that has not been replayed for an hour starts fresh.

    A delivery your endpoint already accepted is not re-sent (it would be a duplicate) and answers `409
    delivery_already_succeeded`; send `{\"force\": true}` to replay it anyway, which still counts
    against the limit.

    A delivery about a listing that is inactive now is not re-sent and answers `403 listing_inactive`;
    activate the listing first.

    Args:
        id (UUID):
        delivery_id (UUID):
        body (ReplayWebhookDeliveryBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        id=id,
delivery_id=delivery_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    delivery_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: ReplayWebhookDeliveryBody | Unset = UNSET,

) -> Any | Error | None:
    r""" Replay webhook delivery

     Re-sends the original payload (same eventId, fresh deliveryId, attempt + 1).

    A delivery may be replayed at most **3 times per rolling 60 minutes**; the 4th inside that window
    answers `409 replay_limit_reached` and names the time the next one is allowed. The limit is charged
    to the original delivery, so replaying the delivery a replay produced draws on the same budget. It
    is not a lifetime cap — a delivery that has not been replayed for an hour starts fresh.

    A delivery your endpoint already accepted is not re-sent (it would be a duplicate) and answers `409
    delivery_already_succeeded`; send `{\"force\": true}` to replay it anyway, which still counts
    against the limit.

    A delivery about a listing that is inactive now is not re-sent and answers `403 listing_inactive`;
    activate the listing first.

    Args:
        id (UUID):
        delivery_id (UUID):
        body (ReplayWebhookDeliveryBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        id=id,
delivery_id=delivery_id,
client=client,
body=body,

    )).parsed
