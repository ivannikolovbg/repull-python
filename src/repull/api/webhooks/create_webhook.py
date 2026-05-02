from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_webhook_body import CreateWebhookBody
from ...models.webhook_subscription import WebhookSubscription
from typing import cast



def _get_kwargs(
    *,
    body: CreateWebhookBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/webhooks",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WebhookSubscription | None:
    if response.status_code == 201:
        response_201 = WebhookSubscription.from_dict(response.json())



        return response_201

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
    *,
    client: AuthenticatedClient | Client,
    body: CreateWebhookBody,

) -> Response[WebhookSubscription]:
    """ Create webhook subscription

     Register a new endpoint. Returns the plaintext signing secret ONCE — capture it from the response
    and store it securely. After this call the secret is masked everywhere; mint a new one with `POST
    /v1/webhooks/{id}/rotate-secret` if you lose it. See `GET /v1/webhooks/event-types` for the full
    list of subscribable events.

    Args:
        body (CreateWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookSubscription]
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
    body: CreateWebhookBody,

) -> WebhookSubscription | None:
    """ Create webhook subscription

     Register a new endpoint. Returns the plaintext signing secret ONCE — capture it from the response
    and store it securely. After this call the secret is masked everywhere; mint a new one with `POST
    /v1/webhooks/{id}/rotate-secret` if you lose it. See `GET /v1/webhooks/event-types` for the full
    list of subscribable events.

    Args:
        body (CreateWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookSubscription
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateWebhookBody,

) -> Response[WebhookSubscription]:
    """ Create webhook subscription

     Register a new endpoint. Returns the plaintext signing secret ONCE — capture it from the response
    and store it securely. After this call the secret is masked everywhere; mint a new one with `POST
    /v1/webhooks/{id}/rotate-secret` if you lose it. See `GET /v1/webhooks/event-types` for the full
    list of subscribable events.

    Args:
        body (CreateWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookSubscription]
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
    body: CreateWebhookBody,

) -> WebhookSubscription | None:
    """ Create webhook subscription

     Register a new endpoint. Returns the plaintext signing secret ONCE — capture it from the response
    and store it securely. After this call the secret is masked everywhere; mint a new one with `POST
    /v1/webhooks/{id}/rotate-secret` if you lose it. See `GET /v1/webhooks/event-types` for the full
    list of subscribable events.

    Args:
        body (CreateWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookSubscription
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
