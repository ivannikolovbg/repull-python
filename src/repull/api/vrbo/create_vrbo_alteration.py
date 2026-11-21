from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_vrbo_alteration_body import CreateVrboAlterationBody
from ...models.create_vrbo_alteration_response_200 import CreateVrboAlterationResponse200
from ...models.create_vrbo_alteration_response_201 import CreateVrboAlterationResponse201
from ...models.error import Error
from typing import cast



def _get_kwargs(
    *,
    body: CreateVrboAlterationBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/vrbo/alterations",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateVrboAlterationResponse200 | CreateVrboAlterationResponse201 | Error | None:
    if response.status_code == 200:
        response_200 = CreateVrboAlterationResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 201:
        response_201 = CreateVrboAlterationResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateVrboAlterationResponse200 | CreateVrboAlterationResponse201 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateVrboAlterationBody,

) -> Response[CreateVrboAlterationResponse200 | CreateVrboAlterationResponse201 | Error]:
    """ Change a Vrbo reservation

     Change an existing Vrbo booking — the counterpart of `POST /v1/channels/airbnb/alterations`. Send
    `confirmation_code` and what changes: `check_in`, `check_out`, `check_in_time` / `check_out_time`
    (`HH:MM` on the hour or half hour), `number_of_adults`, `number_of_children`, `pets`; for the price,
    `rent_amount` (the new rent — Vrbo adds its fees and taxes) or `keep_original_price: true`. Fields
    you leave out keep the booking's values.

    Unlike Airbnb, the change is made at once (the guest does not accept it); when the guest owes more,
    Vrbo requests it by `payment_due_date`. **`preview: true`** returns Vrbo's dry run — `before`,
    `after`, the price difference (`payment`, or `priceUnchanged`) and the due-date range — and changes
    nothing.

    Vrbo's rules are checked first and refused by field: e.g. a pay-later booking's check-in cannot
    move, guests are capped by the listing. `GET /v1/channels/vrbo/reservations/{code}?options=change`
    shows the booking's values and limits. Airbnb fields with no Vrbo equivalent are refused by name:
    `number_of_guests` (send adults and children), `total_price` (send `rent_amount`), `listing_id`
    (Vrbo cannot move a booking to another unit).

    Args:
        body (CreateVrboAlterationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateVrboAlterationResponse200 | CreateVrboAlterationResponse201 | Error]
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
    body: CreateVrboAlterationBody,

) -> CreateVrboAlterationResponse200 | CreateVrboAlterationResponse201 | Error | None:
    """ Change a Vrbo reservation

     Change an existing Vrbo booking — the counterpart of `POST /v1/channels/airbnb/alterations`. Send
    `confirmation_code` and what changes: `check_in`, `check_out`, `check_in_time` / `check_out_time`
    (`HH:MM` on the hour or half hour), `number_of_adults`, `number_of_children`, `pets`; for the price,
    `rent_amount` (the new rent — Vrbo adds its fees and taxes) or `keep_original_price: true`. Fields
    you leave out keep the booking's values.

    Unlike Airbnb, the change is made at once (the guest does not accept it); when the guest owes more,
    Vrbo requests it by `payment_due_date`. **`preview: true`** returns Vrbo's dry run — `before`,
    `after`, the price difference (`payment`, or `priceUnchanged`) and the due-date range — and changes
    nothing.

    Vrbo's rules are checked first and refused by field: e.g. a pay-later booking's check-in cannot
    move, guests are capped by the listing. `GET /v1/channels/vrbo/reservations/{code}?options=change`
    shows the booking's values and limits. Airbnb fields with no Vrbo equivalent are refused by name:
    `number_of_guests` (send adults and children), `total_price` (send `rent_amount`), `listing_id`
    (Vrbo cannot move a booking to another unit).

    Args:
        body (CreateVrboAlterationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateVrboAlterationResponse200 | CreateVrboAlterationResponse201 | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateVrboAlterationBody,

) -> Response[CreateVrboAlterationResponse200 | CreateVrboAlterationResponse201 | Error]:
    """ Change a Vrbo reservation

     Change an existing Vrbo booking — the counterpart of `POST /v1/channels/airbnb/alterations`. Send
    `confirmation_code` and what changes: `check_in`, `check_out`, `check_in_time` / `check_out_time`
    (`HH:MM` on the hour or half hour), `number_of_adults`, `number_of_children`, `pets`; for the price,
    `rent_amount` (the new rent — Vrbo adds its fees and taxes) or `keep_original_price: true`. Fields
    you leave out keep the booking's values.

    Unlike Airbnb, the change is made at once (the guest does not accept it); when the guest owes more,
    Vrbo requests it by `payment_due_date`. **`preview: true`** returns Vrbo's dry run — `before`,
    `after`, the price difference (`payment`, or `priceUnchanged`) and the due-date range — and changes
    nothing.

    Vrbo's rules are checked first and refused by field: e.g. a pay-later booking's check-in cannot
    move, guests are capped by the listing. `GET /v1/channels/vrbo/reservations/{code}?options=change`
    shows the booking's values and limits. Airbnb fields with no Vrbo equivalent are refused by name:
    `number_of_guests` (send adults and children), `total_price` (send `rent_amount`), `listing_id`
    (Vrbo cannot move a booking to another unit).

    Args:
        body (CreateVrboAlterationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateVrboAlterationResponse200 | CreateVrboAlterationResponse201 | Error]
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
    body: CreateVrboAlterationBody,

) -> CreateVrboAlterationResponse200 | CreateVrboAlterationResponse201 | Error | None:
    """ Change a Vrbo reservation

     Change an existing Vrbo booking — the counterpart of `POST /v1/channels/airbnb/alterations`. Send
    `confirmation_code` and what changes: `check_in`, `check_out`, `check_in_time` / `check_out_time`
    (`HH:MM` on the hour or half hour), `number_of_adults`, `number_of_children`, `pets`; for the price,
    `rent_amount` (the new rent — Vrbo adds its fees and taxes) or `keep_original_price: true`. Fields
    you leave out keep the booking's values.

    Unlike Airbnb, the change is made at once (the guest does not accept it); when the guest owes more,
    Vrbo requests it by `payment_due_date`. **`preview: true`** returns Vrbo's dry run — `before`,
    `after`, the price difference (`payment`, or `priceUnchanged`) and the due-date range — and changes
    nothing.

    Vrbo's rules are checked first and refused by field: e.g. a pay-later booking's check-in cannot
    move, guests are capped by the listing. `GET /v1/channels/vrbo/reservations/{code}?options=change`
    shows the booking's values and limits. Airbnb fields with no Vrbo equivalent are refused by name:
    `number_of_guests` (send adults and children), `total_price` (send `rent_amount`), `listing_id`
    (Vrbo cannot move a booking to another unit).

    Args:
        body (CreateVrboAlterationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateVrboAlterationResponse200 | CreateVrboAlterationResponse201 | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
