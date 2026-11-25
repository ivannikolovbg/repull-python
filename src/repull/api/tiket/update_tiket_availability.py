from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.tiket_ari_write_response import TiketAriWriteResponse
from ...models.tiket_availability_update_request import TiketAvailabilityUpdateRequest
from typing import cast



def _get_kwargs(
    *,
    body: TiketAvailabilityUpdateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/tiket/availability",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TiketAriWriteResponse | None:
    if response.status_code == 200:
        response_200 = TiketAriWriteResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | TiketAriWriteResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiketAvailabilityUpdateRequest,

) -> Response[Error | TiketAriWriteResponse]:
    """ Write tiket.com rates, availability or restrictions

     `type` selects the write:

    - `availability` — rooms to sell per room type (`availableRooms`). `stopSell` with a `ratePlanCode`
    also closes that rate plan.
    - `rates` — `price` on a Room Based property or `occupancyPrices` on an Occupancy Based one, per
    room type and rate plan. `currency` defaults to the property currency.
    - `restrictions` — `minStay`, `maxStay`, `stopSell`, `closedToArrival`, `closedToDeparture`,
    `minAdvanceDays`, `maxAdvanceDays`.

    Dates are inclusive and must fall between today and 500 days ahead. Every update is checked before
    anything is sent; a problem returns `422 invalid_params` naming each field, and nothing is written.

    **Children rates are paused.** tiket.com has asked every channel manager not to send children rates
    until it fixes an issue on its side, so a write that includes `childPrices` is refused with `422
    invalid_params` and nothing is sent. Children rates set in the tiket.com extranet still apply. Send
    `price` or `occupancyPrices` without `childPrices`.

    **Every write is read back.** `applied` is `verified` when tiket.com holds what was sent, `mismatch`
    when it holds something else (see `mismatches`), or `unverified` with `verify: false`. tiket.com's
    own warnings come back verbatim in `warnings`. A write tiket.com refuses returns `tiket_rejected`
    with tiket.com's reason and its reference (`echoToken`) in `value_received`.

    To write by listing instead of by room type, use `PUT /v1/channels/tiket/listings/{id}/pricing`.

    Args:
        body (TiketAvailabilityUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketAriWriteResponse]
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
    body: TiketAvailabilityUpdateRequest,

) -> Error | TiketAriWriteResponse | None:
    """ Write tiket.com rates, availability or restrictions

     `type` selects the write:

    - `availability` — rooms to sell per room type (`availableRooms`). `stopSell` with a `ratePlanCode`
    also closes that rate plan.
    - `rates` — `price` on a Room Based property or `occupancyPrices` on an Occupancy Based one, per
    room type and rate plan. `currency` defaults to the property currency.
    - `restrictions` — `minStay`, `maxStay`, `stopSell`, `closedToArrival`, `closedToDeparture`,
    `minAdvanceDays`, `maxAdvanceDays`.

    Dates are inclusive and must fall between today and 500 days ahead. Every update is checked before
    anything is sent; a problem returns `422 invalid_params` naming each field, and nothing is written.

    **Children rates are paused.** tiket.com has asked every channel manager not to send children rates
    until it fixes an issue on its side, so a write that includes `childPrices` is refused with `422
    invalid_params` and nothing is sent. Children rates set in the tiket.com extranet still apply. Send
    `price` or `occupancyPrices` without `childPrices`.

    **Every write is read back.** `applied` is `verified` when tiket.com holds what was sent, `mismatch`
    when it holds something else (see `mismatches`), or `unverified` with `verify: false`. tiket.com's
    own warnings come back verbatim in `warnings`. A write tiket.com refuses returns `tiket_rejected`
    with tiket.com's reason and its reference (`echoToken`) in `value_received`.

    To write by listing instead of by room type, use `PUT /v1/channels/tiket/listings/{id}/pricing`.

    Args:
        body (TiketAvailabilityUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketAriWriteResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiketAvailabilityUpdateRequest,

) -> Response[Error | TiketAriWriteResponse]:
    """ Write tiket.com rates, availability or restrictions

     `type` selects the write:

    - `availability` — rooms to sell per room type (`availableRooms`). `stopSell` with a `ratePlanCode`
    also closes that rate plan.
    - `rates` — `price` on a Room Based property or `occupancyPrices` on an Occupancy Based one, per
    room type and rate plan. `currency` defaults to the property currency.
    - `restrictions` — `minStay`, `maxStay`, `stopSell`, `closedToArrival`, `closedToDeparture`,
    `minAdvanceDays`, `maxAdvanceDays`.

    Dates are inclusive and must fall between today and 500 days ahead. Every update is checked before
    anything is sent; a problem returns `422 invalid_params` naming each field, and nothing is written.

    **Children rates are paused.** tiket.com has asked every channel manager not to send children rates
    until it fixes an issue on its side, so a write that includes `childPrices` is refused with `422
    invalid_params` and nothing is sent. Children rates set in the tiket.com extranet still apply. Send
    `price` or `occupancyPrices` without `childPrices`.

    **Every write is read back.** `applied` is `verified` when tiket.com holds what was sent, `mismatch`
    when it holds something else (see `mismatches`), or `unverified` with `verify: false`. tiket.com's
    own warnings come back verbatim in `warnings`. A write tiket.com refuses returns `tiket_rejected`
    with tiket.com's reason and its reference (`echoToken`) in `value_received`.

    To write by listing instead of by room type, use `PUT /v1/channels/tiket/listings/{id}/pricing`.

    Args:
        body (TiketAvailabilityUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketAriWriteResponse]
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
    body: TiketAvailabilityUpdateRequest,

) -> Error | TiketAriWriteResponse | None:
    """ Write tiket.com rates, availability or restrictions

     `type` selects the write:

    - `availability` — rooms to sell per room type (`availableRooms`). `stopSell` with a `ratePlanCode`
    also closes that rate plan.
    - `rates` — `price` on a Room Based property or `occupancyPrices` on an Occupancy Based one, per
    room type and rate plan. `currency` defaults to the property currency.
    - `restrictions` — `minStay`, `maxStay`, `stopSell`, `closedToArrival`, `closedToDeparture`,
    `minAdvanceDays`, `maxAdvanceDays`.

    Dates are inclusive and must fall between today and 500 days ahead. Every update is checked before
    anything is sent; a problem returns `422 invalid_params` naming each field, and nothing is written.

    **Children rates are paused.** tiket.com has asked every channel manager not to send children rates
    until it fixes an issue on its side, so a write that includes `childPrices` is refused with `422
    invalid_params` and nothing is sent. Children rates set in the tiket.com extranet still apply. Send
    `price` or `occupancyPrices` without `childPrices`.

    **Every write is read back.** `applied` is `verified` when tiket.com holds what was sent, `mismatch`
    when it holds something else (see `mismatches`), or `unverified` with `verify: false`. tiket.com's
    own warnings come back verbatim in `warnings`. A write tiket.com refuses returns `tiket_rejected`
    with tiket.com's reason and its reference (`echoToken`) in `value_received`.

    To write by listing instead of by room type, use `PUT /v1/channels/tiket/listings/{id}/pricing`.

    Args:
        body (TiketAvailabilityUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketAriWriteResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
