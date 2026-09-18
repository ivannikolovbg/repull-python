from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_alteration import AirbnbAlteration
from ...models.airbnb_alteration_create_request import AirbnbAlterationCreateRequest
from ...models.error import Error
from typing import cast



def _get_kwargs(
    *,
    body: AirbnbAlterationCreateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/airbnb/alterations",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AirbnbAlteration | Error | None:
    if response.status_code == 201:
        response_201 = AirbnbAlteration.from_dict(response.json())



        return response_201

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

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AirbnbAlteration | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AirbnbAlterationCreateRequest,

) -> Response[AirbnbAlteration | Error]:
    """ Create Airbnb alteration

     Propose a change to an existing Airbnb reservation: new dates, a new guest count, a new total price,
    or a move to a different listing. **Write-side** — calls Airbnb upstream. Requires a connected
    Airbnb host for the workspace, else `404 no_connection`.

    The body is validated before anything reaches Airbnb. `confirmation_code` is required and **at least
    one** of `check_in`, `check_out`, `number_of_guests`, `total_price` or `listing_id` must be sent
    with it — an alteration that changes nothing is `422 invalid_params`, not a request Airbnb is asked
    to act on. Unknown fields are refused rather than ignored, so a misspelling can never look like a
    successful write.

    **Listing transfer.** `listing_id` moves the reservation to another listing in your workspace. Send
    the **Repull** listing id (the `id` from `GET /v1/properties`); Repull checks you own it, that it is
    active and connected to Airbnb, translates it to the Airbnb listing id and sends it upstream.
    Callers who hold the Airbnb-side id instead may send `airbnb_listing_id`. **Airbnb decides** whether
    to honour a listing change on an alteration — Repull sends it and reports Airbnb’s answer; a refusal
    comes back as `422 airbnb_rejected` carrying Airbnb’s own message.

    Returns `403 listing_inactive` when the reservation’s listing, or the listing it is being moved to,
    is inactive. An inactive listing keeps syncing, but cannot be read or changed through the API until
    it is activated.

    Args:
        body (AirbnbAlterationCreateRequest): A proposed change to an existing Airbnb reservation.
            `confirmation_code` names the reservation; at least one of `check_in`, `check_out`,
            `number_of_guests`, `total_price` or `listing_id` must be sent with it, because an
            alteration that changes nothing is not something Airbnb can act on (it is refused with
            `422 invalid_params`).

            Unknown fields are refused rather than silently dropped. The older connector-native
            spellings (`start_date`, `end_date`, `total_price_override`, and an Airbnb guest-details
            object in place of `number_of_guests`) are still accepted for existing integrations; send
            the canonical names above in new code, and never a canonical field and its older spelling
            with different values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbAlteration | Error]
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
    body: AirbnbAlterationCreateRequest,

) -> AirbnbAlteration | Error | None:
    """ Create Airbnb alteration

     Propose a change to an existing Airbnb reservation: new dates, a new guest count, a new total price,
    or a move to a different listing. **Write-side** — calls Airbnb upstream. Requires a connected
    Airbnb host for the workspace, else `404 no_connection`.

    The body is validated before anything reaches Airbnb. `confirmation_code` is required and **at least
    one** of `check_in`, `check_out`, `number_of_guests`, `total_price` or `listing_id` must be sent
    with it — an alteration that changes nothing is `422 invalid_params`, not a request Airbnb is asked
    to act on. Unknown fields are refused rather than ignored, so a misspelling can never look like a
    successful write.

    **Listing transfer.** `listing_id` moves the reservation to another listing in your workspace. Send
    the **Repull** listing id (the `id` from `GET /v1/properties`); Repull checks you own it, that it is
    active and connected to Airbnb, translates it to the Airbnb listing id and sends it upstream.
    Callers who hold the Airbnb-side id instead may send `airbnb_listing_id`. **Airbnb decides** whether
    to honour a listing change on an alteration — Repull sends it and reports Airbnb’s answer; a refusal
    comes back as `422 airbnb_rejected` carrying Airbnb’s own message.

    Returns `403 listing_inactive` when the reservation’s listing, or the listing it is being moved to,
    is inactive. An inactive listing keeps syncing, but cannot be read or changed through the API until
    it is activated.

    Args:
        body (AirbnbAlterationCreateRequest): A proposed change to an existing Airbnb reservation.
            `confirmation_code` names the reservation; at least one of `check_in`, `check_out`,
            `number_of_guests`, `total_price` or `listing_id` must be sent with it, because an
            alteration that changes nothing is not something Airbnb can act on (it is refused with
            `422 invalid_params`).

            Unknown fields are refused rather than silently dropped. The older connector-native
            spellings (`start_date`, `end_date`, `total_price_override`, and an Airbnb guest-details
            object in place of `number_of_guests`) are still accepted for existing integrations; send
            the canonical names above in new code, and never a canonical field and its older spelling
            with different values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbAlteration | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: AirbnbAlterationCreateRequest,

) -> Response[AirbnbAlteration | Error]:
    """ Create Airbnb alteration

     Propose a change to an existing Airbnb reservation: new dates, a new guest count, a new total price,
    or a move to a different listing. **Write-side** — calls Airbnb upstream. Requires a connected
    Airbnb host for the workspace, else `404 no_connection`.

    The body is validated before anything reaches Airbnb. `confirmation_code` is required and **at least
    one** of `check_in`, `check_out`, `number_of_guests`, `total_price` or `listing_id` must be sent
    with it — an alteration that changes nothing is `422 invalid_params`, not a request Airbnb is asked
    to act on. Unknown fields are refused rather than ignored, so a misspelling can never look like a
    successful write.

    **Listing transfer.** `listing_id` moves the reservation to another listing in your workspace. Send
    the **Repull** listing id (the `id` from `GET /v1/properties`); Repull checks you own it, that it is
    active and connected to Airbnb, translates it to the Airbnb listing id and sends it upstream.
    Callers who hold the Airbnb-side id instead may send `airbnb_listing_id`. **Airbnb decides** whether
    to honour a listing change on an alteration — Repull sends it and reports Airbnb’s answer; a refusal
    comes back as `422 airbnb_rejected` carrying Airbnb’s own message.

    Returns `403 listing_inactive` when the reservation’s listing, or the listing it is being moved to,
    is inactive. An inactive listing keeps syncing, but cannot be read or changed through the API until
    it is activated.

    Args:
        body (AirbnbAlterationCreateRequest): A proposed change to an existing Airbnb reservation.
            `confirmation_code` names the reservation; at least one of `check_in`, `check_out`,
            `number_of_guests`, `total_price` or `listing_id` must be sent with it, because an
            alteration that changes nothing is not something Airbnb can act on (it is refused with
            `422 invalid_params`).

            Unknown fields are refused rather than silently dropped. The older connector-native
            spellings (`start_date`, `end_date`, `total_price_override`, and an Airbnb guest-details
            object in place of `number_of_guests`) are still accepted for existing integrations; send
            the canonical names above in new code, and never a canonical field and its older spelling
            with different values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbAlteration | Error]
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
    body: AirbnbAlterationCreateRequest,

) -> AirbnbAlteration | Error | None:
    """ Create Airbnb alteration

     Propose a change to an existing Airbnb reservation: new dates, a new guest count, a new total price,
    or a move to a different listing. **Write-side** — calls Airbnb upstream. Requires a connected
    Airbnb host for the workspace, else `404 no_connection`.

    The body is validated before anything reaches Airbnb. `confirmation_code` is required and **at least
    one** of `check_in`, `check_out`, `number_of_guests`, `total_price` or `listing_id` must be sent
    with it — an alteration that changes nothing is `422 invalid_params`, not a request Airbnb is asked
    to act on. Unknown fields are refused rather than ignored, so a misspelling can never look like a
    successful write.

    **Listing transfer.** `listing_id` moves the reservation to another listing in your workspace. Send
    the **Repull** listing id (the `id` from `GET /v1/properties`); Repull checks you own it, that it is
    active and connected to Airbnb, translates it to the Airbnb listing id and sends it upstream.
    Callers who hold the Airbnb-side id instead may send `airbnb_listing_id`. **Airbnb decides** whether
    to honour a listing change on an alteration — Repull sends it and reports Airbnb’s answer; a refusal
    comes back as `422 airbnb_rejected` carrying Airbnb’s own message.

    Returns `403 listing_inactive` when the reservation’s listing, or the listing it is being moved to,
    is inactive. An inactive listing keeps syncing, but cannot be read or changed through the API until
    it is activated.

    Args:
        body (AirbnbAlterationCreateRequest): A proposed change to an existing Airbnb reservation.
            `confirmation_code` names the reservation; at least one of `check_in`, `check_out`,
            `number_of_guests`, `total_price` or `listing_id` must be sent with it, because an
            alteration that changes nothing is not something Airbnb can act on (it is refused with
            `422 invalid_params`).

            Unknown fields are refused rather than silently dropped. The older connector-native
            spellings (`start_date`, `end_date`, `total_price_override`, and an Airbnb guest-details
            object in place of `number_of_guests`) are still accepted for existing integrations; send
            the canonical names above in new code, and never a canonical field and its older spelling
            with different values.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbAlteration | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
