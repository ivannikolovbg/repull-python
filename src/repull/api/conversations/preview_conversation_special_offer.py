from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.preview_conversation_special_offer_body import PreviewConversationSpecialOfferBody
from ...models.preview_conversation_special_offer_response_200 import PreviewConversationSpecialOfferResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: PreviewConversationSpecialOfferBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/conversations/{id}/special-offers/preview".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PreviewConversationSpecialOfferResponse200 | None:
    if response.status_code == 200:
        response_200 = PreviewConversationSpecialOfferResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PreviewConversationSpecialOfferResponse200]:
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
    body: PreviewConversationSpecialOfferBody | Unset = UNSET,

) -> Response[Error | PreviewConversationSpecialOfferResponse200]:
    """ Preview a special offer

     See what a special offer would be — as the channel itself recalculates it, with its taxes, service
    fee and guest total — **without sending anything** to the guest. Same body as `POST
    /v1/conversations/{id}/special-offers`; the price may be omitted to see only a date or party change,
    and `{}` shows the current offer recalculated.

    **VRBO** (its “Edit quote” recalculation). A channel without a preview — Airbnb takes your total as
    it is — returns `422 preview_not_supported`; `GET /v1/conversations/{id}` →
    `capabilities.canPreviewOffer` says which.

    Read-only: safe to call as often as you need while a user edits an offer.

    Args:
        id (int):
        body (PreviewConversationSpecialOfferBody | Unset): Any of the offer fields; only what is
            sent is changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PreviewConversationSpecialOfferResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PreviewConversationSpecialOfferBody | Unset = UNSET,

) -> Error | PreviewConversationSpecialOfferResponse200 | None:
    """ Preview a special offer

     See what a special offer would be — as the channel itself recalculates it, with its taxes, service
    fee and guest total — **without sending anything** to the guest. Same body as `POST
    /v1/conversations/{id}/special-offers`; the price may be omitted to see only a date or party change,
    and `{}` shows the current offer recalculated.

    **VRBO** (its “Edit quote” recalculation). A channel without a preview — Airbnb takes your total as
    it is — returns `422 preview_not_supported`; `GET /v1/conversations/{id}` →
    `capabilities.canPreviewOffer` says which.

    Read-only: safe to call as often as you need while a user edits an offer.

    Args:
        id (int):
        body (PreviewConversationSpecialOfferBody | Unset): Any of the offer fields; only what is
            sent is changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PreviewConversationSpecialOfferResponse200
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PreviewConversationSpecialOfferBody | Unset = UNSET,

) -> Response[Error | PreviewConversationSpecialOfferResponse200]:
    """ Preview a special offer

     See what a special offer would be — as the channel itself recalculates it, with its taxes, service
    fee and guest total — **without sending anything** to the guest. Same body as `POST
    /v1/conversations/{id}/special-offers`; the price may be omitted to see only a date or party change,
    and `{}` shows the current offer recalculated.

    **VRBO** (its “Edit quote” recalculation). A channel without a preview — Airbnb takes your total as
    it is — returns `422 preview_not_supported`; `GET /v1/conversations/{id}` →
    `capabilities.canPreviewOffer` says which.

    Read-only: safe to call as often as you need while a user edits an offer.

    Args:
        id (int):
        body (PreviewConversationSpecialOfferBody | Unset): Any of the offer fields; only what is
            sent is changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PreviewConversationSpecialOfferResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PreviewConversationSpecialOfferBody | Unset = UNSET,

) -> Error | PreviewConversationSpecialOfferResponse200 | None:
    """ Preview a special offer

     See what a special offer would be — as the channel itself recalculates it, with its taxes, service
    fee and guest total — **without sending anything** to the guest. Same body as `POST
    /v1/conversations/{id}/special-offers`; the price may be omitted to see only a date or party change,
    and `{}` shows the current offer recalculated.

    **VRBO** (its “Edit quote” recalculation). A channel without a preview — Airbnb takes your total as
    it is — returns `422 preview_not_supported`; `GET /v1/conversations/{id}` →
    `capabilities.canPreviewOffer` says which.

    Read-only: safe to call as often as you need while a user edits an offer.

    Args:
        id (int):
        body (PreviewConversationSpecialOfferBody | Unset): Any of the offer fields; only what is
            sent is changed.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PreviewConversationSpecialOfferResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
