from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_billing_checkout_body import CreateBillingCheckoutBody
from ...models.create_billing_checkout_response_200 import CreateBillingCheckoutResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: CreateBillingCheckoutBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/billing",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CreateBillingCheckoutResponse200 | None:
    if response.status_code == 200:
        response_200 = CreateBillingCheckoutResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | CreateBillingCheckoutResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateBillingCheckoutBody | Unset = UNSET,

) -> Response[Any | CreateBillingCheckoutResponse200]:
    """ Start an upgrade

     Returns the URL where the workspace owner upgrades to Starter. Plans above Starter are set up with
    the Repull team and return `422 billing_error` with the next step.

    Args:
        body (CreateBillingCheckoutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateBillingCheckoutResponse200]
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
    body: CreateBillingCheckoutBody | Unset = UNSET,

) -> Any | CreateBillingCheckoutResponse200 | None:
    """ Start an upgrade

     Returns the URL where the workspace owner upgrades to Starter. Plans above Starter are set up with
    the Repull team and return `422 billing_error` with the next step.

    Args:
        body (CreateBillingCheckoutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateBillingCheckoutResponse200
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateBillingCheckoutBody | Unset = UNSET,

) -> Response[Any | CreateBillingCheckoutResponse200]:
    """ Start an upgrade

     Returns the URL where the workspace owner upgrades to Starter. Plans above Starter are set up with
    the Repull team and return `422 billing_error` with the next step.

    Args:
        body (CreateBillingCheckoutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CreateBillingCheckoutResponse200]
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
    body: CreateBillingCheckoutBody | Unset = UNSET,

) -> Any | CreateBillingCheckoutResponse200 | None:
    """ Start an upgrade

     Returns the URL where the workspace owner upgrades to Starter. Plans above Starter are set up with
    the Repull team and return `422 billing_error` with the next step.

    Args:
        body (CreateBillingCheckoutBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CreateBillingCheckoutResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
