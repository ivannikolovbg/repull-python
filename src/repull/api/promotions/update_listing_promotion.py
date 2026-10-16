from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.promotion_response import PromotionResponse
from ...models.promotion_update_request import PromotionUpdateRequest
from typing import cast



def _get_kwargs(
    id: int,
    promotion_id: int,
    *,
    body: PromotionUpdateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/listings/{id}/promotions/{promotion_id}".format(id=quote(str(id), safe=""),promotion_id=quote(str(promotion_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | PromotionResponse | None:
    if response.status_code == 200:
        response_200 = PromotionResponse.from_dict(response.json())



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

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 502:
        response_502 = cast(Any, None)
        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error | PromotionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    promotion_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PromotionUpdateRequest,

) -> Response[Any | Error | PromotionResponse]:
    """ Change a promotion

     Booking.com promotions only — Airbnb's have nothing to change. `rules`, when sent, replaces the
    promotion's rules whole. A promotion that also covers other listings' rooms changes for them too, so
    it needs `confirmShared: true` (otherwise `409 promotion_shared_promotion`). Promotions that come
    from the listing's weekly or monthly discount are changed in its pricing settings.

    A request a channel can't take is refused with `422` and a `promotion_*` code; the message names the
    channel and the field and says what to do, and `channel` / `field` are set. Booking.com writes
    return once Booking.com shows the change (it lags its own writes by a few seconds).

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        promotion_id (int):
        body (PromotionUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | PromotionResponse]
     """


    kwargs = _get_kwargs(
        id=id,
promotion_id=promotion_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    promotion_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PromotionUpdateRequest,

) -> Any | Error | PromotionResponse | None:
    """ Change a promotion

     Booking.com promotions only — Airbnb's have nothing to change. `rules`, when sent, replaces the
    promotion's rules whole. A promotion that also covers other listings' rooms changes for them too, so
    it needs `confirmShared: true` (otherwise `409 promotion_shared_promotion`). Promotions that come
    from the listing's weekly or monthly discount are changed in its pricing settings.

    A request a channel can't take is refused with `422` and a `promotion_*` code; the message names the
    channel and the field and says what to do, and `channel` / `field` are set. Booking.com writes
    return once Booking.com shows the change (it lags its own writes by a few seconds).

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        promotion_id (int):
        body (PromotionUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | PromotionResponse
     """


    return sync_detailed(
        id=id,
promotion_id=promotion_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    promotion_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PromotionUpdateRequest,

) -> Response[Any | Error | PromotionResponse]:
    """ Change a promotion

     Booking.com promotions only — Airbnb's have nothing to change. `rules`, when sent, replaces the
    promotion's rules whole. A promotion that also covers other listings' rooms changes for them too, so
    it needs `confirmShared: true` (otherwise `409 promotion_shared_promotion`). Promotions that come
    from the listing's weekly or monthly discount are changed in its pricing settings.

    A request a channel can't take is refused with `422` and a `promotion_*` code; the message names the
    channel and the field and says what to do, and `channel` / `field` are set. Booking.com writes
    return once Booking.com shows the change (it lags its own writes by a few seconds).

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        promotion_id (int):
        body (PromotionUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | PromotionResponse]
     """


    kwargs = _get_kwargs(
        id=id,
promotion_id=promotion_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    promotion_id: int,
    *,
    client: AuthenticatedClient | Client,
    body: PromotionUpdateRequest,

) -> Any | Error | PromotionResponse | None:
    """ Change a promotion

     Booking.com promotions only — Airbnb's have nothing to change. `rules`, when sent, replaces the
    promotion's rules whole. A promotion that also covers other listings' rooms changes for them too, so
    it needs `confirmShared: true` (otherwise `409 promotion_shared_promotion`). Promotions that come
    from the listing's weekly or monthly discount are changed in its pricing settings.

    A request a channel can't take is refused with `422` and a `promotion_*` code; the message names the
    channel and the field and says what to do, and `channel` / `field` are set. Booking.com writes
    return once Booking.com shows the change (it lags its own writes by a few seconds).

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        promotion_id (int):
        body (PromotionUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | PromotionResponse
     """


    return (await asyncio_detailed(
        id=id,
promotion_id=promotion_id,
client=client,
body=body,

    )).parsed
