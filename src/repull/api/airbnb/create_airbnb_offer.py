from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_airbnb_offer_body import CreateAirbnbOfferBody
from ...models.create_airbnb_offer_response_201 import CreateAirbnbOfferResponse201
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: CreateAirbnbOfferBody,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/airbnb/offers",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateAirbnbOfferResponse201 | Error | None:
    if response.status_code == 201:
        response_201 = CreateAirbnbOfferResponse201.from_dict(response.json())



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

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateAirbnbOfferResponse201 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAirbnbOfferBody,
    idempotency_key: str | Unset = UNSET,

) -> Response[CreateAirbnbOfferResponse201 | Error]:
    r""" Create Airbnb special offer or pre-approval

     Create a pre-approval or a special offer on an Airbnb thread, addressed by **Airbnb** ids. **Write-
    side** — calls Airbnb upstream. The Repull-id equivalents, which also update the inquiry in Vanio,
    are `POST /v1/conversations/{id}/pre-approval` and `POST /v1/conversations/{id}/special-offers` —
    prefer those unless you only hold Airbnb ids.

    - `type: \"preapproval\"` — let the guest book the dates and price they asked about. Requires
    `thread_id`; optional `block_instant_booking`.
    - `type: \"offer\"` — your own terms. Requires `thread_id`, `listing_id` (the **Airbnb** listing id,
    as a string), `start_date`, `nights`, `total_price` (whole stay, listing currency) and
    `guest_details` with `number_of_guests` (or `number_of_adults`; Airbnb counts adults + children).

    The body is validated before anything reaches Airbnb (a `422 invalid_params` names the field), and
    unknown fields are refused. The legacy spellings `threadId` and `blockInstantBooking` still work.
    The request is sent as the Airbnb account that owns the thread or listing.

    Airbnb refusals are mapped rather than returned as a 500: `409 inquiry_no_longer_open` /
    `inquiry_expired` when the inquiry moved on, `422 airbnb_rejected` with Airbnb’s reason otherwise,
    `403 connection_reauth_required` when the grant does not allow it.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again.

    Args:
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (CreateAirbnbOfferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAirbnbOfferResponse201 | Error]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAirbnbOfferBody,
    idempotency_key: str | Unset = UNSET,

) -> CreateAirbnbOfferResponse201 | Error | None:
    r""" Create Airbnb special offer or pre-approval

     Create a pre-approval or a special offer on an Airbnb thread, addressed by **Airbnb** ids. **Write-
    side** — calls Airbnb upstream. The Repull-id equivalents, which also update the inquiry in Vanio,
    are `POST /v1/conversations/{id}/pre-approval` and `POST /v1/conversations/{id}/special-offers` —
    prefer those unless you only hold Airbnb ids.

    - `type: \"preapproval\"` — let the guest book the dates and price they asked about. Requires
    `thread_id`; optional `block_instant_booking`.
    - `type: \"offer\"` — your own terms. Requires `thread_id`, `listing_id` (the **Airbnb** listing id,
    as a string), `start_date`, `nights`, `total_price` (whole stay, listing currency) and
    `guest_details` with `number_of_guests` (or `number_of_adults`; Airbnb counts adults + children).

    The body is validated before anything reaches Airbnb (a `422 invalid_params` names the field), and
    unknown fields are refused. The legacy spellings `threadId` and `blockInstantBooking` still work.
    The request is sent as the Airbnb account that owns the thread or listing.

    Airbnb refusals are mapped rather than returned as a 500: `409 inquiry_no_longer_open` /
    `inquiry_expired` when the inquiry moved on, `422 airbnb_rejected` with Airbnb’s reason otherwise,
    `403 connection_reauth_required` when the grant does not allow it.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again.

    Args:
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (CreateAirbnbOfferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAirbnbOfferResponse201 | Error
     """


    return sync_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAirbnbOfferBody,
    idempotency_key: str | Unset = UNSET,

) -> Response[CreateAirbnbOfferResponse201 | Error]:
    r""" Create Airbnb special offer or pre-approval

     Create a pre-approval or a special offer on an Airbnb thread, addressed by **Airbnb** ids. **Write-
    side** — calls Airbnb upstream. The Repull-id equivalents, which also update the inquiry in Vanio,
    are `POST /v1/conversations/{id}/pre-approval` and `POST /v1/conversations/{id}/special-offers` —
    prefer those unless you only hold Airbnb ids.

    - `type: \"preapproval\"` — let the guest book the dates and price they asked about. Requires
    `thread_id`; optional `block_instant_booking`.
    - `type: \"offer\"` — your own terms. Requires `thread_id`, `listing_id` (the **Airbnb** listing id,
    as a string), `start_date`, `nights`, `total_price` (whole stay, listing currency) and
    `guest_details` with `number_of_guests` (or `number_of_adults`; Airbnb counts adults + children).

    The body is validated before anything reaches Airbnb (a `422 invalid_params` names the field), and
    unknown fields are refused. The legacy spellings `threadId` and `blockInstantBooking` still work.
    The request is sent as the Airbnb account that owns the thread or listing.

    Airbnb refusals are mapped rather than returned as a 500: `409 inquiry_no_longer_open` /
    `inquiry_expired` when the inquiry moved on, `422 airbnb_rejected` with Airbnb’s reason otherwise,
    `403 connection_reauth_required` when the grant does not allow it.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again.

    Args:
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (CreateAirbnbOfferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateAirbnbOfferResponse201 | Error]
     """


    kwargs = _get_kwargs(
        body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateAirbnbOfferBody,
    idempotency_key: str | Unset = UNSET,

) -> CreateAirbnbOfferResponse201 | Error | None:
    r""" Create Airbnb special offer or pre-approval

     Create a pre-approval or a special offer on an Airbnb thread, addressed by **Airbnb** ids. **Write-
    side** — calls Airbnb upstream. The Repull-id equivalents, which also update the inquiry in Vanio,
    are `POST /v1/conversations/{id}/pre-approval` and `POST /v1/conversations/{id}/special-offers` —
    prefer those unless you only hold Airbnb ids.

    - `type: \"preapproval\"` — let the guest book the dates and price they asked about. Requires
    `thread_id`; optional `block_instant_booking`.
    - `type: \"offer\"` — your own terms. Requires `thread_id`, `listing_id` (the **Airbnb** listing id,
    as a string), `start_date`, `nights`, `total_price` (whole stay, listing currency) and
    `guest_details` with `number_of_guests` (or `number_of_adults`; Airbnb counts adults + children).

    The body is validated before anything reaches Airbnb (a `422 invalid_params` names the field), and
    unknown fields are refused. The legacy spellings `threadId` and `blockInstantBooking` still work.
    The request is sent as the Airbnb account that owns the thread or listing.

    Airbnb refusals are mapped rather than returned as a 500: `409 inquiry_no_longer_open` /
    `inquiry_expired` when the inquiry moved on, `422 airbnb_rejected` with Airbnb’s reason otherwise,
    `403 connection_reauth_required` when the grant does not allow it.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again.

    Args:
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (CreateAirbnbOfferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateAirbnbOfferResponse201 | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
