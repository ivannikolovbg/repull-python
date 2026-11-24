from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.tiket_listing_pricing_response import TiketListingPricingResponse
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    id: int,
    *,
    hotel_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = 31,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["hotel_id"] = hotel_id

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    params["number_of_days"] = number_of_days


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/tiket/listings/{id}/pricing".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TiketListingPricingResponse | None:
    if response.status_code == 200:
        response_200 = TiketListingPricingResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | TiketListingPricingResponse]:
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
    hotel_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = 31,

) -> Response[Error | TiketListingPricingResponse]:
    """ Read tiket.com rates, availability and restrictions for a listing

     Same as `GET /v1/channels/tiket/availability`, addressed by listing: the listing's tiket.com room
    type and every active rate plan of that room, read live from tiket.com.

    A listing mapped on more than one tiket.com property needs `hotel_id`; without it the call returns
    `409 ambiguous_tiket_mapping` listing the ids.

    Args:
        id (int):
        hotel_id (str | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        number_of_days (int | Unset):  Default: 31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketListingPricingResponse]
     """


    kwargs = _get_kwargs(
        id=id,
hotel_id=hotel_id,
start_date=start_date,
end_date=end_date,
number_of_days=number_of_days,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    hotel_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = 31,

) -> Error | TiketListingPricingResponse | None:
    """ Read tiket.com rates, availability and restrictions for a listing

     Same as `GET /v1/channels/tiket/availability`, addressed by listing: the listing's tiket.com room
    type and every active rate plan of that room, read live from tiket.com.

    A listing mapped on more than one tiket.com property needs `hotel_id`; without it the call returns
    `409 ambiguous_tiket_mapping` listing the ids.

    Args:
        id (int):
        hotel_id (str | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        number_of_days (int | Unset):  Default: 31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketListingPricingResponse
     """


    return sync_detailed(
        id=id,
client=client,
hotel_id=hotel_id,
start_date=start_date,
end_date=end_date,
number_of_days=number_of_days,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    hotel_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = 31,

) -> Response[Error | TiketListingPricingResponse]:
    """ Read tiket.com rates, availability and restrictions for a listing

     Same as `GET /v1/channels/tiket/availability`, addressed by listing: the listing's tiket.com room
    type and every active rate plan of that room, read live from tiket.com.

    A listing mapped on more than one tiket.com property needs `hotel_id`; without it the call returns
    `409 ambiguous_tiket_mapping` listing the ids.

    Args:
        id (int):
        hotel_id (str | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        number_of_days (int | Unset):  Default: 31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketListingPricingResponse]
     """


    kwargs = _get_kwargs(
        id=id,
hotel_id=hotel_id,
start_date=start_date,
end_date=end_date,
number_of_days=number_of_days,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    hotel_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = 31,

) -> Error | TiketListingPricingResponse | None:
    """ Read tiket.com rates, availability and restrictions for a listing

     Same as `GET /v1/channels/tiket/availability`, addressed by listing: the listing's tiket.com room
    type and every active rate plan of that room, read live from tiket.com.

    A listing mapped on more than one tiket.com property needs `hotel_id`; without it the call returns
    `409 ambiguous_tiket_mapping` listing the ids.

    Args:
        id (int):
        hotel_id (str | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        number_of_days (int | Unset):  Default: 31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketListingPricingResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
hotel_id=hotel_id,
start_date=start_date,
end_date=end_date,
number_of_days=number_of_days,

    )).parsed
