from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_usage_tier_response_200 import GetUsageTierResponse200
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/usage/tier",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetUsageTierResponse200 | None:
    if response.status_code == 200:
        response_200 = GetUsageTierResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetUsageTierResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetUsageTierResponse200]:
    """ Get tier and quota

     Lightweight current-tier snapshot for status badges and quota meters — plan limits (monthly
    requests, daily AI requests, dynamic-pricing listings), the amount used, the amount remaining, and
    the next reset. `null` limits mean unlimited on that dimension.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetUsageTierResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetUsageTierResponse200 | None:
    """ Get tier and quota

     Lightweight current-tier snapshot for status badges and quota meters — plan limits (monthly
    requests, daily AI requests, dynamic-pricing listings), the amount used, the amount remaining, and
    the next reset. `null` limits mean unlimited on that dimension.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetUsageTierResponse200
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetUsageTierResponse200]:
    """ Get tier and quota

     Lightweight current-tier snapshot for status badges and quota meters — plan limits (monthly
    requests, daily AI requests, dynamic-pricing listings), the amount used, the amount remaining, and
    the next reset. `null` limits mean unlimited on that dimension.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetUsageTierResponse200]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetUsageTierResponse200 | None:
    """ Get tier and quota

     Lightweight current-tier snapshot for status badges and quota meters — plan limits (monthly
    requests, daily AI requests, dynamic-pricing listings), the amount used, the amount remaining, and
    the next reset. `null` limits mean unlimited on that dimension.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetUsageTierResponse200
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
