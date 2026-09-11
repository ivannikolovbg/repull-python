from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.availability_write_request import AvailabilityWriteRequest
from ...models.availability_write_result import AvailabilityWriteResult
from ...models.error import Error
from typing import cast



def _get_kwargs(
    property_id: int,
    *,
    body: AvailabilityWriteRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/availability/{property_id}".format(property_id=quote(str(property_id), safe=""),),
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

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

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
    property_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AvailabilityWriteRequest,

) -> Response[AvailabilityWriteResult | Error]:
    """ Set prices, block or unblock dates

     Writes the calendar for one property AND pushes to every connected channel in the same step. A write
    that only changed our copy would leave the OTA calendars stale and eventually double-book a guest.

    Args:
        property_id (int):
        body (AvailabilityWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailabilityWriteResult | Error]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    property_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AvailabilityWriteRequest,

) -> AvailabilityWriteResult | Error | None:
    """ Set prices, block or unblock dates

     Writes the calendar for one property AND pushes to every connected channel in the same step. A write
    that only changed our copy would leave the OTA calendars stale and eventually double-book a guest.

    Args:
        property_id (int):
        body (AvailabilityWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailabilityWriteResult | Error
     """


    return sync_detailed(
        property_id=property_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    property_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AvailabilityWriteRequest,

) -> Response[AvailabilityWriteResult | Error]:
    """ Set prices, block or unblock dates

     Writes the calendar for one property AND pushes to every connected channel in the same step. A write
    that only changed our copy would leave the OTA calendars stale and eventually double-book a guest.

    Args:
        property_id (int):
        body (AvailabilityWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AvailabilityWriteResult | Error]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    property_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: AvailabilityWriteRequest,

) -> AvailabilityWriteResult | Error | None:
    """ Set prices, block or unblock dates

     Writes the calendar for one property AND pushes to every connected channel in the same step. A write
    that only changed our copy would leave the OTA calendars stale and eventually double-book a guest.

    Args:
        property_id (int):
        body (AvailabilityWriteRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AvailabilityWriteResult | Error
     """


    return (await asyncio_detailed(
        property_id=property_id,
client=client,
body=body,

    )).parsed
