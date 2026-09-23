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
    """ Send a special offer

     Send the guest on this conversation an Airbnb special offer: your own dates, guest count and total
    price. The guest has 24 hours to book it. Use it to answer an inquiry with different terms, or to
    make a returning guest a custom price. To accept the guest’s own dates and price as they asked, pre-
    approve instead (`POST /v1/conversations/{id}/pre-approval`).

    `listingId` is optional: omit it to offer the listing the guest asked about. It is a **Repull**
    listing id; Repull sends Airbnb its own listing id, using the link that belongs to this
    conversation’s Airbnb account.

    `totalPrice` is the whole stay, in the listing’s Airbnb currency — Airbnb does not take a currency
    on an offer.

    **Airbnb only**, and only for listings connected to Airbnb directly; anything else is `422
    channel_not_supported` and nothing is sent. The inquiry is marked `special_offer_sent`.

    An offer Airbnb refuses is never a `201`: dates that are taken, a price below Airbnb’s minimum, too
    many guests and the like are `422 airbnb_rejected` with Airbnb’s own reason in `message`.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again. Without it, a retry after a timeout can send the
    guest two offers.

    Read or withdraw the offer with `GET` / `DELETE /v1/conversations/{id}/special-offers/{offerId}`.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (CreateConversationSpecialOfferBody):

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
    """ Send a special offer

     Send the guest on this conversation an Airbnb special offer: your own dates, guest count and total
    price. The guest has 24 hours to book it. Use it to answer an inquiry with different terms, or to
    make a returning guest a custom price. To accept the guest’s own dates and price as they asked, pre-
    approve instead (`POST /v1/conversations/{id}/pre-approval`).

    `listingId` is optional: omit it to offer the listing the guest asked about. It is a **Repull**
    listing id; Repull sends Airbnb its own listing id, using the link that belongs to this
    conversation’s Airbnb account.

    `totalPrice` is the whole stay, in the listing’s Airbnb currency — Airbnb does not take a currency
    on an offer.

    **Airbnb only**, and only for listings connected to Airbnb directly; anything else is `422
    channel_not_supported` and nothing is sent. The inquiry is marked `special_offer_sent`.

    An offer Airbnb refuses is never a `201`: dates that are taken, a price below Airbnb’s minimum, too
    many guests and the like are `422 airbnb_rejected` with Airbnb’s own reason in `message`.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again. Without it, a retry after a timeout can send the
    guest two offers.

    Read or withdraw the offer with `GET` / `DELETE /v1/conversations/{id}/special-offers/{offerId}`.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (CreateConversationSpecialOfferBody):

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
    """ Send a special offer

     Send the guest on this conversation an Airbnb special offer: your own dates, guest count and total
    price. The guest has 24 hours to book it. Use it to answer an inquiry with different terms, or to
    make a returning guest a custom price. To accept the guest’s own dates and price as they asked, pre-
    approve instead (`POST /v1/conversations/{id}/pre-approval`).

    `listingId` is optional: omit it to offer the listing the guest asked about. It is a **Repull**
    listing id; Repull sends Airbnb its own listing id, using the link that belongs to this
    conversation’s Airbnb account.

    `totalPrice` is the whole stay, in the listing’s Airbnb currency — Airbnb does not take a currency
    on an offer.

    **Airbnb only**, and only for listings connected to Airbnb directly; anything else is `422
    channel_not_supported` and nothing is sent. The inquiry is marked `special_offer_sent`.

    An offer Airbnb refuses is never a `201`: dates that are taken, a price below Airbnb’s minimum, too
    many guests and the like are `422 airbnb_rejected` with Airbnb’s own reason in `message`.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again. Without it, a retry after a timeout can send the
    guest two offers.

    Read or withdraw the offer with `GET` / `DELETE /v1/conversations/{id}/special-offers/{offerId}`.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (CreateConversationSpecialOfferBody):

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
    """ Send a special offer

     Send the guest on this conversation an Airbnb special offer: your own dates, guest count and total
    price. The guest has 24 hours to book it. Use it to answer an inquiry with different terms, or to
    make a returning guest a custom price. To accept the guest’s own dates and price as they asked, pre-
    approve instead (`POST /v1/conversations/{id}/pre-approval`).

    `listingId` is optional: omit it to offer the listing the guest asked about. It is a **Repull**
    listing id; Repull sends Airbnb its own listing id, using the link that belongs to this
    conversation’s Airbnb account.

    `totalPrice` is the whole stay, in the listing’s Airbnb currency — Airbnb does not take a currency
    on an offer.

    **Airbnb only**, and only for listings connected to Airbnb directly; anything else is `422
    channel_not_supported` and nothing is sent. The inquiry is marked `special_offer_sent`.

    An offer Airbnb refuses is never a `201`: dates that are taken, a price below Airbnb’s minimum, too
    many guests and the like are `422 airbnb_rejected` with Airbnb’s own reason in `message`.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again. Without it, a retry after a timeout can send the
    guest two offers.

    Read or withdraw the offer with `GET` / `DELETE /v1/conversations/{id}/special-offers/{offerId}`.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (CreateConversationSpecialOfferBody):

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
