from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_conversation_special_offer_body import CreateConversationSpecialOfferBody
from ...models.create_conversation_special_offer_response_201 import CreateConversationSpecialOfferResponse201
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: CreateConversationSpecialOfferBody,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/conversations/{id}/special-offers".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateConversationSpecialOfferResponse201 | Error | None:
    if response.status_code == 201:
        response_201 = CreateConversationSpecialOfferResponse201.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateConversationSpecialOfferResponse201 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CreateConversationSpecialOfferBody,
    idempotency_key: str | Unset = UNSET,

) -> Response[CreateConversationSpecialOfferResponse201 | Error]:
    """ Send a special offer (Airbnb, VRBO)

     Send the guest on this conversation a special offer: your own dates, guest count and price. One
    endpoint for every channel that has offers — **Airbnb** (connected directly) and **VRBO** (its “Edit
    quote”). Use it to answer an inquiry with different terms. To accept the guest’s own dates and price
    as they asked, pre-approve instead (`POST /v1/conversations/{id}/pre-approval`).

    **How the price is set depends on the channel** — `GET /v1/conversations/{id}` →
    `capabilities.offerPrice` says which:
    - `total` (Airbnb): send `totalPrice`, the whole stay in the listing’s Airbnb currency, with
    `checkIn`, `checkOut` and `guests`.
    - `breakdown` (VRBO): send the price’s parts — `rentalAmount` (rent, excluding fees), `fees` by VRBO
    fee type, `damageDeposit` — and VRBO computes the guest total, adding its taxes and service fee.
    Dates and party are optional (omitted → the inquiry’s own). Only what you send is changed. Preview
    the result first with `POST /v1/conversations/{id}/special-offers/preview`.

    Sending the other kind is `422 offer_price_total_required` / `offer_price_breakdown_required` naming
    the field; nothing is sent. A channel without offers (Booking.com, direct, an Airbnb inquiry relayed
    by a PMS) is `422 channel_not_supported`.

    `listingId` (Airbnb) is optional: omit it to offer the listing the guest asked about. It is a
    **Repull** listing id. `message` (VRBO) is sent to the guest with the offer.

    An offer the channel refuses is never a `201`: dates that are taken, a price below the channel’s
    minimum and the like are `422` with the channel’s own reason in `message`.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again. Without it, a retry after a timeout can send the
    guest two offers.

    Read or withdraw the offer with `GET` / `DELETE /v1/conversations/{id}/special-offers/{offerId}`
    (VRBO: `offerId` = `current`).

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (CreateConversationSpecialOfferBody): Priced by `totalPrice` (Airbnb) OR by its parts
            — `rentalAmount`, `fees`, `damageDeposit` (VRBO) — never both. With `totalPrice`,
            `checkIn`, `checkOut` and `guests` are required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateConversationSpecialOfferResponse201 | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CreateConversationSpecialOfferBody,
    idempotency_key: str | Unset = UNSET,

) -> CreateConversationSpecialOfferResponse201 | Error | None:
    """ Send a special offer (Airbnb, VRBO)

     Send the guest on this conversation a special offer: your own dates, guest count and price. One
    endpoint for every channel that has offers — **Airbnb** (connected directly) and **VRBO** (its “Edit
    quote”). Use it to answer an inquiry with different terms. To accept the guest’s own dates and price
    as they asked, pre-approve instead (`POST /v1/conversations/{id}/pre-approval`).

    **How the price is set depends on the channel** — `GET /v1/conversations/{id}` →
    `capabilities.offerPrice` says which:
    - `total` (Airbnb): send `totalPrice`, the whole stay in the listing’s Airbnb currency, with
    `checkIn`, `checkOut` and `guests`.
    - `breakdown` (VRBO): send the price’s parts — `rentalAmount` (rent, excluding fees), `fees` by VRBO
    fee type, `damageDeposit` — and VRBO computes the guest total, adding its taxes and service fee.
    Dates and party are optional (omitted → the inquiry’s own). Only what you send is changed. Preview
    the result first with `POST /v1/conversations/{id}/special-offers/preview`.

    Sending the other kind is `422 offer_price_total_required` / `offer_price_breakdown_required` naming
    the field; nothing is sent. A channel without offers (Booking.com, direct, an Airbnb inquiry relayed
    by a PMS) is `422 channel_not_supported`.

    `listingId` (Airbnb) is optional: omit it to offer the listing the guest asked about. It is a
    **Repull** listing id. `message` (VRBO) is sent to the guest with the offer.

    An offer the channel refuses is never a `201`: dates that are taken, a price below the channel’s
    minimum and the like are `422` with the channel’s own reason in `message`.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again. Without it, a retry after a timeout can send the
    guest two offers.

    Read or withdraw the offer with `GET` / `DELETE /v1/conversations/{id}/special-offers/{offerId}`
    (VRBO: `offerId` = `current`).

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (CreateConversationSpecialOfferBody): Priced by `totalPrice` (Airbnb) OR by its parts
            — `rentalAmount`, `fees`, `damageDeposit` (VRBO) — never both. With `totalPrice`,
            `checkIn`, `checkOut` and `guests` are required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateConversationSpecialOfferResponse201 | Error
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CreateConversationSpecialOfferBody,
    idempotency_key: str | Unset = UNSET,

) -> Response[CreateConversationSpecialOfferResponse201 | Error]:
    """ Send a special offer (Airbnb, VRBO)

     Send the guest on this conversation a special offer: your own dates, guest count and price. One
    endpoint for every channel that has offers — **Airbnb** (connected directly) and **VRBO** (its “Edit
    quote”). Use it to answer an inquiry with different terms. To accept the guest’s own dates and price
    as they asked, pre-approve instead (`POST /v1/conversations/{id}/pre-approval`).

    **How the price is set depends on the channel** — `GET /v1/conversations/{id}` →
    `capabilities.offerPrice` says which:
    - `total` (Airbnb): send `totalPrice`, the whole stay in the listing’s Airbnb currency, with
    `checkIn`, `checkOut` and `guests`.
    - `breakdown` (VRBO): send the price’s parts — `rentalAmount` (rent, excluding fees), `fees` by VRBO
    fee type, `damageDeposit` — and VRBO computes the guest total, adding its taxes and service fee.
    Dates and party are optional (omitted → the inquiry’s own). Only what you send is changed. Preview
    the result first with `POST /v1/conversations/{id}/special-offers/preview`.

    Sending the other kind is `422 offer_price_total_required` / `offer_price_breakdown_required` naming
    the field; nothing is sent. A channel without offers (Booking.com, direct, an Airbnb inquiry relayed
    by a PMS) is `422 channel_not_supported`.

    `listingId` (Airbnb) is optional: omit it to offer the listing the guest asked about. It is a
    **Repull** listing id. `message` (VRBO) is sent to the guest with the offer.

    An offer the channel refuses is never a `201`: dates that are taken, a price below the channel’s
    minimum and the like are `422` with the channel’s own reason in `message`.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again. Without it, a retry after a timeout can send the
    guest two offers.

    Read or withdraw the offer with `GET` / `DELETE /v1/conversations/{id}/special-offers/{offerId}`
    (VRBO: `offerId` = `current`).

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (CreateConversationSpecialOfferBody): Priced by `totalPrice` (Airbnb) OR by its parts
            — `rentalAmount`, `fees`, `damageDeposit` (VRBO) — never both. With `totalPrice`,
            `checkIn`, `checkOut` and `guests` are required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateConversationSpecialOfferResponse201 | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: CreateConversationSpecialOfferBody,
    idempotency_key: str | Unset = UNSET,

) -> CreateConversationSpecialOfferResponse201 | Error | None:
    """ Send a special offer (Airbnb, VRBO)

     Send the guest on this conversation a special offer: your own dates, guest count and price. One
    endpoint for every channel that has offers — **Airbnb** (connected directly) and **VRBO** (its “Edit
    quote”). Use it to answer an inquiry with different terms. To accept the guest’s own dates and price
    as they asked, pre-approve instead (`POST /v1/conversations/{id}/pre-approval`).

    **How the price is set depends on the channel** — `GET /v1/conversations/{id}` →
    `capabilities.offerPrice` says which:
    - `total` (Airbnb): send `totalPrice`, the whole stay in the listing’s Airbnb currency, with
    `checkIn`, `checkOut` and `guests`.
    - `breakdown` (VRBO): send the price’s parts — `rentalAmount` (rent, excluding fees), `fees` by VRBO
    fee type, `damageDeposit` — and VRBO computes the guest total, adding its taxes and service fee.
    Dates and party are optional (omitted → the inquiry’s own). Only what you send is changed. Preview
    the result first with `POST /v1/conversations/{id}/special-offers/preview`.

    Sending the other kind is `422 offer_price_total_required` / `offer_price_breakdown_required` naming
    the field; nothing is sent. A channel without offers (Booking.com, direct, an Airbnb inquiry relayed
    by a PMS) is `422 channel_not_supported`.

    `listingId` (Airbnb) is optional: omit it to offer the listing the guest asked about. It is a
    **Repull** listing id. `message` (VRBO) is sent to the guest with the offer.

    An offer the channel refuses is never a `201`: dates that are taken, a price below the channel’s
    minimum and the like are `422` with the channel’s own reason in `message`.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again. Without it, a retry after a timeout can send the
    guest two offers.

    Read or withdraw the offer with `GET` / `DELETE /v1/conversations/{id}/special-offers/{offerId}`
    (VRBO: `offerId` = `current`).

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (CreateConversationSpecialOfferBody): Priced by `totalPrice` (Airbnb) OR by its parts
            — `rentalAmount`, `fees`, `damageDeposit` (VRBO) — never both. With `totalPrice`,
            `checkIn`, `checkOut` and `guests` are required.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateConversationSpecialOfferResponse201 | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
