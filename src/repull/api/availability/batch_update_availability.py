from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.availability_batch_write_request import AvailabilityBatchWriteRequest
from ...models.availability_write_result import AvailabilityWriteResult
from ...models.error import Error
from typing import cast



def _get_kwargs(
    *,
    body: AvailabilityBatchWriteRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/availability/batch",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AvailabilityWriteResult | Error | None:
    if response.status_code == 200:
        response_200 = AvailabilityWriteResult.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AvailabilityWriteResult | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AvailabilityBatchWriteRequest,

) -> Response[AvailabilityWriteResult | Error]:
    """ Update availability across many properties

     Applies ONE settings object across up to 500 properties and pushes the result to every connected
    channel.

    Ownership is checked before anything is written: a batch containing a property from another
    workspace is refused as a whole and names the offending ids, rather than being partially applied.

    Per-property *different* values are separate calls — presenting them as one request would be a false
    claim about atomicity.

    Args:
        body (AvailabilityBatchWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailabilityWriteResult | Error]
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
    body: AvailabilityBatchWriteRequest,

) -> AvailabilityWriteResult | Error | None:
    """ Update availability across many properties

     Applies ONE settings object across up to 500 properties and pushes the result to every connected
    channel.

    Ownership is checked before anything is written: a batch containing a property from another
    workspace is refused as a whole and names the offending ids, rather than being partially applied.

    Per-property *different* values are separate calls — presenting them as one request would be a false
    claim about atomicity.

    Args:
        body (AvailabilityBatchWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailabilityWriteResult | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AvailabilityBatchWriteRequest,

) -> Response[AvailabilityWriteResult | Error]:
    """ Update availability across many properties

     Applies ONE settings object across up to 500 properties and pushes the result to every connected
    channel.

    Ownership is checked before anything is written: a batch containing a property from another
    workspace is refused as a whole and names the offending ids, rather than being partially applied.

    Per-property *different* values are separate calls — presenting them as one request would be a false
    claim about atomicity.

    Args:
        body (AvailabilityBatchWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailabilityWriteResult | Error]
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
    body: AvailabilityBatchWriteRequest,

) -> AvailabilityWriteResult | Error | None:
    """ Update availability across many properties

     Applies ONE settings object across up to 500 properties and pushes the result to every connected
    channel.

    Ownership is checked before anything is written: a batch containing a property from another
    workspace is refused as a whole and names the offending ids, rather than being partially applied.

    Per-property *different* values are separate calls — presenting them as one request would be a false
    claim about atomicity.

    Args:
        body (AvailabilityBatchWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailabilityWriteResult | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
