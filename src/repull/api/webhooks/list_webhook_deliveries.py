from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.list_webhook_deliveries_status import ListWebhookDeliveriesStatus
from ...models.webhook_delivery_list_response import WebhookDeliveryListResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    id: UUID,
    *,
    limit: int | Unset = 25,
    cursor: str | Unset = UNSET,
    status: ListWebhookDeliveriesStatus | Unset = ListWebhookDeliveriesStatus.ALL,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/webhooks/{id}/deliveries".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> WebhookDeliveryListResponse | None:
    if response.status_code == 200:
        response_200 = WebhookDeliveryListResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[WebhookDeliveryListResponse]:
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
    limit: int | Unset = 25,
    cursor: str | Unset = UNSET,
    status: ListWebhookDeliveriesStatus | Unset = ListWebhookDeliveriesStatus.ALL,

) -> Response[WebhookDeliveryListResponse]:
    """ List webhook deliveries

     Paginated history of every delivery attempt for this subscription.

    Args:
        id (UUID):
        limit (int | Unset):  Default: 25.
        cursor (str | Unset): ISO timestamp from `pagination.nextCursor`
        status (ListWebhookDeliveriesStatus | Unset):  Default: ListWebhookDeliveriesStatus.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookDeliveryListResponse]
     """


    kwargs = _get_kwargs(
        id=id,
limit=limit,
cursor=cursor,
status=status,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 25,
    cursor: str | Unset = UNSET,
    status: ListWebhookDeliveriesStatus | Unset = ListWebhookDeliveriesStatus.ALL,

) -> WebhookDeliveryListResponse | None:
    """ List webhook deliveries

     Paginated history of every delivery attempt for this subscription.

    Args:
        id (UUID):
        limit (int | Unset):  Default: 25.
        cursor (str | Unset): ISO timestamp from `pagination.nextCursor`
        status (ListWebhookDeliveriesStatus | Unset):  Default: ListWebhookDeliveriesStatus.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookDeliveryListResponse
     """


    return sync_detailed(
        id=id,
client=client,
limit=limit,
cursor=cursor,
status=status,

    ).parsed

async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 25,
    cursor: str | Unset = UNSET,
    status: ListWebhookDeliveriesStatus | Unset = ListWebhookDeliveriesStatus.ALL,

) -> Response[WebhookDeliveryListResponse]:
    """ List webhook deliveries

     Paginated history of every delivery attempt for this subscription.

    Args:
        id (UUID):
        limit (int | Unset):  Default: 25.
        cursor (str | Unset): ISO timestamp from `pagination.nextCursor`
        status (ListWebhookDeliveriesStatus | Unset):  Default: ListWebhookDeliveriesStatus.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WebhookDeliveryListResponse]
     """


    kwargs = _get_kwargs(
        id=id,
limit=limit,
cursor=cursor,
status=status,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 25,
    cursor: str | Unset = UNSET,
    status: ListWebhookDeliveriesStatus | Unset = ListWebhookDeliveriesStatus.ALL,

) -> WebhookDeliveryListResponse | None:
    """ List webhook deliveries

     Paginated history of every delivery attempt for this subscription.

    Args:
        id (UUID):
        limit (int | Unset):  Default: 25.
        cursor (str | Unset): ISO timestamp from `pagination.nextCursor`
        status (ListWebhookDeliveriesStatus | Unset):  Default: ListWebhookDeliveriesStatus.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WebhookDeliveryListResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
limit=limit,
cursor=cursor,
status=status,

    )).parsed
