from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.booking_setup_body import BookingSetupBody
from ...models.error import Error
from typing import cast



def _get_kwargs(
    *,
    body: BookingSetupBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/booking/setup",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 201:
        response_201 = cast(Any, None)
        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BookingSetupBody,

) -> Response[Any | Error]:
    """ Booking.com property setup actions

     Action-router for onboarding a property onto Booking.com. Select the step with `action`:

    - `create-legal-entity` — register the legal entity (returns 201).
    - `check-legal-status` — poll legal-entity status by `leid`.
    - `check-readiness` — check whether a property is ready to open (`property_id`).
    - `open-property` — open the property for sale (`property_id`).
    - `set-contacts` — set property contacts (`property_id`, `contacts`).
    - `set-policies` — set property policies (`property_id`, plus policy fields).

    Missing required fields per action return a validation error; upstream failures surface as
    `booking_error`.

    Args:
        body (BookingSetupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    body: BookingSetupBody,

) -> Any | Error | None:
    """ Booking.com property setup actions

     Action-router for onboarding a property onto Booking.com. Select the step with `action`:

    - `create-legal-entity` — register the legal entity (returns 201).
    - `check-legal-status` — poll legal-entity status by `leid`.
    - `check-readiness` — check whether a property is ready to open (`property_id`).
    - `open-property` — open the property for sale (`property_id`).
    - `set-contacts` — set property contacts (`property_id`, `contacts`).
    - `set-policies` — set property policies (`property_id`, plus policy fields).

    Missing required fields per action return a validation error; upstream failures surface as
    `booking_error`.

    Args:
        body (BookingSetupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: BookingSetupBody,

) -> Response[Any | Error]:
    """ Booking.com property setup actions

     Action-router for onboarding a property onto Booking.com. Select the step with `action`:

    - `create-legal-entity` — register the legal entity (returns 201).
    - `check-legal-status` — poll legal-entity status by `leid`.
    - `check-readiness` — check whether a property is ready to open (`property_id`).
    - `open-property` — open the property for sale (`property_id`).
    - `set-contacts` — set property contacts (`property_id`, `contacts`).
    - `set-policies` — set property policies (`property_id`, plus policy fields).

    Missing required fields per action return a validation error; upstream failures surface as
    `booking_error`.

    Args:
        body (BookingSetupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    body: BookingSetupBody,

) -> Any | Error | None:
    """ Booking.com property setup actions

     Action-router for onboarding a property onto Booking.com. Select the step with `action`:

    - `create-legal-entity` — register the legal entity (returns 201).
    - `check-legal-status` — poll legal-entity status by `leid`.
    - `check-readiness` — check whether a property is ready to open (`property_id`).
    - `open-property` — open the property for sale (`property_id`).
    - `set-contacts` — set property contacts (`property_id`, `contacts`).
    - `set-policies` — set property policies (`property_id`, plus policy fields).

    Missing required fields per action return a validation error; upstream failures surface as
    `booking_error`.

    Args:
        body (BookingSetupBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
