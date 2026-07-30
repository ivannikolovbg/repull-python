from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.sandbox_reset_result import SandboxResetResult
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/sandbox/reset",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SandboxResetResult | None:
    if response.status_code == 200:
        response_200 = SandboxResetResult.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SandboxResetResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | SandboxResetResult]:
    """ Reset sandbox fixtures

     Clear the authenticated test customer's sandbox fixtures. **Requires a test key (`sk_test_*`)** —
    live or legacy keys are rejected with 403.

    Deletes ONLY the customer's rows in the isolated sandbox data space — it can never touch real
    inventory (`listings`, `reservations`, connections). Idempotent: resetting an empty sandbox returns
    zero counts (still 200). Returns per-resource deletion counts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SandboxResetResult]
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

) -> Error | SandboxResetResult | None:
    """ Reset sandbox fixtures

     Clear the authenticated test customer's sandbox fixtures. **Requires a test key (`sk_test_*`)** —
    live or legacy keys are rejected with 403.

    Deletes ONLY the customer's rows in the isolated sandbox data space — it can never touch real
    inventory (`listings`, `reservations`, connections). Idempotent: resetting an empty sandbox returns
    zero counts (still 200). Returns per-resource deletion counts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SandboxResetResult
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | SandboxResetResult]:
    """ Reset sandbox fixtures

     Clear the authenticated test customer's sandbox fixtures. **Requires a test key (`sk_test_*`)** —
    live or legacy keys are rejected with 403.

    Deletes ONLY the customer's rows in the isolated sandbox data space — it can never touch real
    inventory (`listings`, `reservations`, connections). Idempotent: resetting an empty sandbox returns
    zero counts (still 200). Returns per-resource deletion counts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SandboxResetResult]
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

) -> Error | SandboxResetResult | None:
    """ Reset sandbox fixtures

     Clear the authenticated test customer's sandbox fixtures. **Requires a test key (`sk_test_*`)** —
    live or legacy keys are rejected with 403.

    Deletes ONLY the customer's rows in the isolated sandbox data space — it can never touch real
    inventory (`listings`, `reservations`, connections). Idempotent: resetting an empty sandbox returns
    zero counts (still 200). Returns per-resource deletion counts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SandboxResetResult
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
