from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.webhook_delivery_detail import WebhookDeliveryDetail
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    delivery_id: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/webhooks/{id}/deliveries/{delivery_id}".format(id=quote(str(id), safe=""),delivery_id=quote(str(delivery_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WebhookDeliveryDetail | None:
    if response.status_code == 200:
        response_200 = WebhookDeliveryDetail.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WebhookDeliveryDetail]:
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

) -> Response[WebhookDeliveryDetail]:
    """ Get webhook delivery

     Full request + response capture for one delivery attempt.

    Args:
        id (UUID):
        delivery_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookDeliveryDetail]
     """


    kwargs = _get_kwargs(
        id=id,
delivery_id=delivery_id,

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

) -> WebhookDeliveryDetail | None:
    """ Get webhook delivery

     Full request + response capture for one delivery attempt.

    Args:
        id (UUID):
        delivery_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookDeliveryDetail
     """


    return sync_detailed(
        id=id,
delivery_id=delivery_id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    delivery_id: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[WebhookDeliveryDetail]:
    """ Get webhook delivery

     Full request + response capture for one delivery attempt.

    Args:
        id (UUID):
        delivery_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookDeliveryDetail]
     """


    kwargs = _get_kwargs(
        id=id,
delivery_id=delivery_id,

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

) -> WebhookDeliveryDetail | None:
    """ Get webhook delivery

     Full request + response capture for one delivery attempt.

    Args:
        id (UUID):
        delivery_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookDeliveryDetail
     """


    return (await asyncio_detailed(
        id=id,
delivery_id=delivery_id,
client=client,

    )).parsed
