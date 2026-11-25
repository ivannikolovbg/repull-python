from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.tiket_setup_request import TiketSetupRequest
from ...models.tiket_setup_response import TiketSetupResponse
from typing import cast



def _get_kwargs(
    *,
    body: TiketSetupRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/tiket/setup",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TiketSetupResponse | None:
    if response.status_code == 200:
        response_200 = TiketSetupResponse.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | TiketSetupResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiketSetupRequest,

) -> Response[Error | TiketSetupResponse]:
    """ Set up a tiket.com property

     Onboarding and maintenance actions for tiket.com properties (counterpart of `POST
    /v1/channels/booking/setup`). `action`:

    - `request-activation` — ask tiket.com to activate Repull as channel manager for one or more
    existing properties (`properties[]`). The usual path for a group; a single host activates Repull in
    the tiket.com extranet and connects through Connect instead.
    - `check-activation` — whether tiket.com has activated Repull for `hotel_id` yet.
    - `create-property` — create a new property on tiket.com from a listing (`listing_id` plus the
    property and company details). Then `request-registration` asks tiket.com for its ids and `set-
    tiket-hotel-id` records the Hotel ID tiket.com replies with.
    - `add-room`, `add-rate-plan` — add a room type or rate plan to a property Repull created.
    - `request-content-mapping` / `confirm-content-mapping` — for an existing property, ask tiket.com to
    link Repull's codes to it so `POST /v1/listings/{id}/publish/tiket` can send content.
    - `refresh` — re-read room types and rate plans from tiket.com.
    - `set-push-rate-plans` — choose the rate plans (`rate_plan_ids`) that receive prices and
    restrictions.
    - `set-sync` — turn automatic calendar sending on or off (`enabled`).
    - `disconnect` — stop syncing the property. Always available, even when its listings are inactive.

    tiket.com accepts incomplete content and rejects it later, so content is checked against tiket.com's
    requirements before it is sent; problems come back as `422 invalid_params` with each field in
    `value_received`.

    Args:
        body (TiketSetupRequest): Fields depend on `action`. Every action except `create-
            property`, `request-activation` and `check-activation` names a property with `property_id`
            or, for a property Repull created that tiket.com has not assigned an id to yet,
            `partner_hotel_code`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketSetupResponse]
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
    body: TiketSetupRequest,

) -> Error | TiketSetupResponse | None:
    """ Set up a tiket.com property

     Onboarding and maintenance actions for tiket.com properties (counterpart of `POST
    /v1/channels/booking/setup`). `action`:

    - `request-activation` — ask tiket.com to activate Repull as channel manager for one or more
    existing properties (`properties[]`). The usual path for a group; a single host activates Repull in
    the tiket.com extranet and connects through Connect instead.
    - `check-activation` — whether tiket.com has activated Repull for `hotel_id` yet.
    - `create-property` — create a new property on tiket.com from a listing (`listing_id` plus the
    property and company details). Then `request-registration` asks tiket.com for its ids and `set-
    tiket-hotel-id` records the Hotel ID tiket.com replies with.
    - `add-room`, `add-rate-plan` — add a room type or rate plan to a property Repull created.
    - `request-content-mapping` / `confirm-content-mapping` — for an existing property, ask tiket.com to
    link Repull's codes to it so `POST /v1/listings/{id}/publish/tiket` can send content.
    - `refresh` — re-read room types and rate plans from tiket.com.
    - `set-push-rate-plans` — choose the rate plans (`rate_plan_ids`) that receive prices and
    restrictions.
    - `set-sync` — turn automatic calendar sending on or off (`enabled`).
    - `disconnect` — stop syncing the property. Always available, even when its listings are inactive.

    tiket.com accepts incomplete content and rejects it later, so content is checked against tiket.com's
    requirements before it is sent; problems come back as `422 invalid_params` with each field in
    `value_received`.

    Args:
        body (TiketSetupRequest): Fields depend on `action`. Every action except `create-
            property`, `request-activation` and `check-activation` names a property with `property_id`
            or, for a property Repull created that tiket.com has not assigned an id to yet,
            `partner_hotel_code`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketSetupResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: TiketSetupRequest,

) -> Response[Error | TiketSetupResponse]:
    """ Set up a tiket.com property

     Onboarding and maintenance actions for tiket.com properties (counterpart of `POST
    /v1/channels/booking/setup`). `action`:

    - `request-activation` — ask tiket.com to activate Repull as channel manager for one or more
    existing properties (`properties[]`). The usual path for a group; a single host activates Repull in
    the tiket.com extranet and connects through Connect instead.
    - `check-activation` — whether tiket.com has activated Repull for `hotel_id` yet.
    - `create-property` — create a new property on tiket.com from a listing (`listing_id` plus the
    property and company details). Then `request-registration` asks tiket.com for its ids and `set-
    tiket-hotel-id` records the Hotel ID tiket.com replies with.
    - `add-room`, `add-rate-plan` — add a room type or rate plan to a property Repull created.
    - `request-content-mapping` / `confirm-content-mapping` — for an existing property, ask tiket.com to
    link Repull's codes to it so `POST /v1/listings/{id}/publish/tiket` can send content.
    - `refresh` — re-read room types and rate plans from tiket.com.
    - `set-push-rate-plans` — choose the rate plans (`rate_plan_ids`) that receive prices and
    restrictions.
    - `set-sync` — turn automatic calendar sending on or off (`enabled`).
    - `disconnect` — stop syncing the property. Always available, even when its listings are inactive.

    tiket.com accepts incomplete content and rejects it later, so content is checked against tiket.com's
    requirements before it is sent; problems come back as `422 invalid_params` with each field in
    `value_received`.

    Args:
        body (TiketSetupRequest): Fields depend on `action`. Every action except `create-
            property`, `request-activation` and `check-activation` names a property with `property_id`
            or, for a property Repull created that tiket.com has not assigned an id to yet,
            `partner_hotel_code`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketSetupResponse]
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
    body: TiketSetupRequest,

) -> Error | TiketSetupResponse | None:
    """ Set up a tiket.com property

     Onboarding and maintenance actions for tiket.com properties (counterpart of `POST
    /v1/channels/booking/setup`). `action`:

    - `request-activation` — ask tiket.com to activate Repull as channel manager for one or more
    existing properties (`properties[]`). The usual path for a group; a single host activates Repull in
    the tiket.com extranet and connects through Connect instead.
    - `check-activation` — whether tiket.com has activated Repull for `hotel_id` yet.
    - `create-property` — create a new property on tiket.com from a listing (`listing_id` plus the
    property and company details). Then `request-registration` asks tiket.com for its ids and `set-
    tiket-hotel-id` records the Hotel ID tiket.com replies with.
    - `add-room`, `add-rate-plan` — add a room type or rate plan to a property Repull created.
    - `request-content-mapping` / `confirm-content-mapping` — for an existing property, ask tiket.com to
    link Repull's codes to it so `POST /v1/listings/{id}/publish/tiket` can send content.
    - `refresh` — re-read room types and rate plans from tiket.com.
    - `set-push-rate-plans` — choose the rate plans (`rate_plan_ids`) that receive prices and
    restrictions.
    - `set-sync` — turn automatic calendar sending on or off (`enabled`).
    - `disconnect` — stop syncing the property. Always available, even when its listings are inactive.

    tiket.com accepts incomplete content and rejects it later, so content is checked against tiket.com's
    requirements before it is sent; problems come back as `422 invalid_params` with each field in
    `value_received`.

    Args:
        body (TiketSetupRequest): Fields depend on `action`. Every action except `create-
            property`, `request-activation` and `check-activation` names a property with `property_id`
            or, for a property Repull created that tiket.com has not assigned an id to yet,
            `partner_hotel_code`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketSetupResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
