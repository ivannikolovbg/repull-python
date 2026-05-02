from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.update_webhook_body import UpdateWebhookBody
from ...models.webhook_subscription import WebhookSubscription
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    body: UpdateWebhookBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/webhooks/{id}".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WebhookSubscription | None:
    if response.status_code == 200:
        response_200 = WebhookSubscription.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WebhookSubscription]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWebhookBody | Unset = UNSET,

) -> Response[WebhookSubscription]:
    """ Update webhook subscription

     Update url, description, events, or status (active|paused). Re-enabling clears
    `consecutive_failures` and `disabled_at`.

    Args:
        id (UUID):
        body (UpdateWebhookBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookSubscription]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWebhookBody | Unset = UNSET,

) -> WebhookSubscription | None:
    """ Update webhook subscription

     Update url, description, events, or status (active|paused). Re-enabling clears
    `consecutive_failures` and `disabled_at`.

    Args:
        id (UUID):
        body (UpdateWebhookBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookSubscription
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWebhookBody | Unset = UNSET,

) -> Response[WebhookSubscription]:
    """ Update webhook subscription

     Update url, description, events, or status (active|paused). Re-enabling clears
    `consecutive_failures` and `disabled_at`.

    Args:
        id (UUID):
        body (UpdateWebhookBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookSubscription]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateWebhookBody | Unset = UNSET,

) -> WebhookSubscription | None:
    """ Update webhook subscription

     Update url, description, events, or status (active|paused). Re-enabling clears
    `consecutive_failures` and `disabled_at`.

    Args:
        id (UUID):
        body (UpdateWebhookBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookSubscription
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
