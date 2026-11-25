from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.tiket_ari_write_response import TiketAriWriteResponse
from ...models.tiket_listing_pricing_update_request import TiketListingPricingUpdateRequest
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: TiketListingPricingUpdateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/tiket/listings/{id}/pricing".format(id=quote(str(id), safe=""),),
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | TiketAriWriteResponse]:
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
    body: TiketListingPricingUpdateRequest,

) -> Response[Error | TiketAriWriteResponse]:
    """ Write tiket.com rates, availability or restrictions for a listing

     Same contract as `PUT /v1/channels/tiket/availability`, addressed by listing. `roomTypeCode` is
    always the listing's room; `ratePlanCode` defaults to every rate plan of the room selected for
    pushes (`pushTarget`), so one update row is sent to each. `type` defaults to `rates`.

    **Children rates are paused.** tiket.com has asked every channel manager not to send children rates
    until it fixes an issue on its side, so a write that includes `childPrices` is refused with `422
    invalid_params` and nothing is sent. Children rates set in the tiket.com extranet still apply. Send
    `price` or `occupancyPrices` without `childPrices`.

    Args:
        id (int):
        body (TiketListingPricingUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketAriWriteResponse]
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
    body: TiketListingPricingUpdateRequest,

) -> Error | TiketAriWriteResponse | None:
    """ Write tiket.com rates, availability or restrictions for a listing

     Same contract as `PUT /v1/channels/tiket/availability`, addressed by listing. `roomTypeCode` is
    always the listing's room; `ratePlanCode` defaults to every rate plan of the room selected for
    pushes (`pushTarget`), so one update row is sent to each. `type` defaults to `rates`.

    **Children rates are paused.** tiket.com has asked every channel manager not to send children rates
    until it fixes an issue on its side, so a write that includes `childPrices` is refused with `422
    invalid_params` and nothing is sent. Children rates set in the tiket.com extranet still apply. Send
    `price` or `occupancyPrices` without `childPrices`.

    Args:
        id (int):
        body (TiketListingPricingUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketAriWriteResponse
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
    body: TiketListingPricingUpdateRequest,

) -> Response[Error | TiketAriWriteResponse]:
    """ Write tiket.com rates, availability or restrictions for a listing

     Same contract as `PUT /v1/channels/tiket/availability`, addressed by listing. `roomTypeCode` is
    always the listing's room; `ratePlanCode` defaults to every rate plan of the room selected for
    pushes (`pushTarget`), so one update row is sent to each. `type` defaults to `rates`.

    **Children rates are paused.** tiket.com has asked every channel manager not to send children rates
    until it fixes an issue on its side, so a write that includes `childPrices` is refused with `422
    invalid_params` and nothing is sent. Children rates set in the tiket.com extranet still apply. Send
    `price` or `occupancyPrices` without `childPrices`.

    Args:
        id (int):
        body (TiketListingPricingUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketAriWriteResponse]
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
    body: TiketListingPricingUpdateRequest,

) -> Error | TiketAriWriteResponse | None:
    """ Write tiket.com rates, availability or restrictions for a listing

     Same contract as `PUT /v1/channels/tiket/availability`, addressed by listing. `roomTypeCode` is
    always the listing's room; `ratePlanCode` defaults to every rate plan of the room selected for
    pushes (`pushTarget`), so one update row is sent to each. `type` defaults to `rates`.

    **Children rates are paused.** tiket.com has asked every channel manager not to send children rates
    until it fixes an issue on its side, so a write that includes `childPrices` is refused with `422
    invalid_params` and nothing is sent. Children rates set in the tiket.com extranet still apply. Send
    `price` or `occupancyPrices` without `childPrices`.

    Args:
        id (int):
        body (TiketListingPricingUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketAriWriteResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
