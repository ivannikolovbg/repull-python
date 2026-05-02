from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.listing_pricing_strategy_input import ListingPricingStrategyInput
from ...models.update_listing_pricing_strategy_response_200 import UpdateListingPricingStrategyResponse200
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ListingPricingStrategyInput,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/listings/{id}/pricing/strategy".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UpdateListingPricingStrategyResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateListingPricingStrategyResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UpdateListingPricingStrategyResponse200]:
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
    body: ListingPricingStrategyInput,

) -> Response[UpdateListingPricingStrategyResponse200]:
    """ Update pricing strategy

     Upserts the strategy on `(listing_id, customer_id)` — repeated PUTs are idempotent. Send only the
    fields you want to change; omitted fields take server-side defaults.

    Args:
        id (int):
        body (ListingPricingStrategyInput): Same shape as `ListingPricingStrategy` minus the read-
            only fields. Send only fields you want to change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateListingPricingStrategyResponse200]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingPricingStrategyInput,

) -> UpdateListingPricingStrategyResponse200 | None:
    """ Update pricing strategy

     Upserts the strategy on `(listing_id, customer_id)` — repeated PUTs are idempotent. Send only the
    fields you want to change; omitted fields take server-side defaults.

    Args:
        id (int):
        body (ListingPricingStrategyInput): Same shape as `ListingPricingStrategy` minus the read-
            only fields. Send only fields you want to change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateListingPricingStrategyResponse200
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingPricingStrategyInput,

) -> Response[UpdateListingPricingStrategyResponse200]:
    """ Update pricing strategy

     Upserts the strategy on `(listing_id, customer_id)` — repeated PUTs are idempotent. Send only the
    fields you want to change; omitted fields take server-side defaults.

    Args:
        id (int):
        body (ListingPricingStrategyInput): Same shape as `ListingPricingStrategy` minus the read-
            only fields. Send only fields you want to change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateListingPricingStrategyResponse200]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingPricingStrategyInput,

) -> UpdateListingPricingStrategyResponse200 | None:
    """ Update pricing strategy

     Upserts the strategy on `(listing_id, customer_id)` — repeated PUTs are idempotent. Send only the
    fields you want to change; omitted fields take server-side defaults.

    Args:
        id (int):
        body (ListingPricingStrategyInput): Same shape as `ListingPricingStrategy` minus the read-
            only fields. Send only fields you want to change.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateListingPricingStrategyResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
