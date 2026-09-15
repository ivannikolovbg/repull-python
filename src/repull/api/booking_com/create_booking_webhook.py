from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_booking_webhook_body import CreateBookingWebhookBody
from ...models.error import Error
from typing import cast



def _get_kwargs(
    *,
    body: CreateBookingWebhookBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/booking/webhooks",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | None:
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateBookingWebhookBody,

) -> Response[Error]:
    """ Subscribe to a Booking.com notification

     **Not available through the API — always returns `403 forbidden`.** Booking.com notification
    subscriptions belong to the Repull platform account that every workspace shares: they are per
    notification type, not per property, so reading or changing them would affect every workspace.
    Booking.com events for your own properties are delivered through Repull webhooks — subscribe with
    `POST /v1/webhooks`.

    Args:
        body (CreateBookingWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
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
    body: CreateBookingWebhookBody,

) -> Error | None:
    """ Subscribe to a Booking.com notification

     **Not available through the API — always returns `403 forbidden`.** Booking.com notification
    subscriptions belong to the Repull platform account that every workspace shares: they are per
    notification type, not per property, so reading or changing them would affect every workspace.
    Booking.com events for your own properties are delivered through Repull webhooks — subscribe with
    `POST /v1/webhooks`.

    Args:
        body (CreateBookingWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateBookingWebhookBody,

) -> Response[Error]:
    """ Subscribe to a Booking.com notification

     **Not available through the API — always returns `403 forbidden`.** Booking.com notification
    subscriptions belong to the Repull platform account that every workspace shares: they are per
    notification type, not per property, so reading or changing them would affect every workspace.
    Booking.com events for your own properties are delivered through Repull webhooks — subscribe with
    `POST /v1/webhooks`.

    Args:
        body (CreateBookingWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
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
    body: CreateBookingWebhookBody,

) -> Error | None:
    """ Subscribe to a Booking.com notification

     **Not available through the API — always returns `403 forbidden`.** Booking.com notification
    subscriptions belong to the Repull platform account that every workspace shares: they are per
    notification type, not per property, so reading or changing them would affect every workspace.
    Booking.com events for your own properties are delivered through Repull webhooks — subscribe with
    `POST /v1/webhooks`.

    Args:
        body (CreateBookingWebhookBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
