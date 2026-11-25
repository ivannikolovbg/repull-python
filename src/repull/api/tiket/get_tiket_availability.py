from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.tiket_availability_response import TiketAvailabilityResponse
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    *,
    property_id: str,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = 31,
    room_type_code: str | Unset = UNSET,
    rate_plan_code: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["property_id"] = property_id

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    params["number_of_days"] = number_of_days

    params["room_type_code"] = room_type_code

    params["rate_plan_code"] = rate_plan_code


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/tiket/availability",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TiketAvailabilityResponse | None:
    if response.status_code == 200:
        response_200 = TiketAvailabilityResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | TiketAvailabilityResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    property_id: str,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = 31,
    room_type_code: str | Unset = UNSET,
    rate_plan_code: str | Unset = UNSET,

) -> Response[Error | TiketAvailabilityResponse]:
    """ Read tiket.com rates, availability and restrictions

     What tiket.com holds for a property over a date window, read live from tiket.com: rooms to sell and
    booked per room type, prices (Room Based, or per number of guests on an Occupancy Based property,
    and children prices) and restrictions per rate plan. One row per night, room type and rate plan.

    `property_id` must be a tiket.com property connected to this workspace (`GET
    /v1/channels/tiket/properties`).

    Args:
        property_id (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        number_of_days (int | Unset):  Default: 31.
        room_type_code (str | Unset):
        rate_plan_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketAvailabilityResponse]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
start_date=start_date,
end_date=end_date,
number_of_days=number_of_days,
room_type_code=room_type_code,
rate_plan_code=rate_plan_code,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    property_id: str,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = 31,
    room_type_code: str | Unset = UNSET,
    rate_plan_code: str | Unset = UNSET,

) -> Error | TiketAvailabilityResponse | None:
    """ Read tiket.com rates, availability and restrictions

     What tiket.com holds for a property over a date window, read live from tiket.com: rooms to sell and
    booked per room type, prices (Room Based, or per number of guests on an Occupancy Based property,
    and children prices) and restrictions per rate plan. One row per night, room type and rate plan.

    `property_id` must be a tiket.com property connected to this workspace (`GET
    /v1/channels/tiket/properties`).

    Args:
        property_id (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        number_of_days (int | Unset):  Default: 31.
        room_type_code (str | Unset):
        rate_plan_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketAvailabilityResponse
     """


    return sync_detailed(
        client=client,
property_id=property_id,
start_date=start_date,
end_date=end_date,
number_of_days=number_of_days,
room_type_code=room_type_code,
rate_plan_code=rate_plan_code,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    property_id: str,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = 31,
    room_type_code: str | Unset = UNSET,
    rate_plan_code: str | Unset = UNSET,

) -> Response[Error | TiketAvailabilityResponse]:
    """ Read tiket.com rates, availability and restrictions

     What tiket.com holds for a property over a date window, read live from tiket.com: rooms to sell and
    booked per room type, prices (Room Based, or per number of guests on an Occupancy Based property,
    and children prices) and restrictions per rate plan. One row per night, room type and rate plan.

    `property_id` must be a tiket.com property connected to this workspace (`GET
    /v1/channels/tiket/properties`).

    Args:
        property_id (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        number_of_days (int | Unset):  Default: 31.
        room_type_code (str | Unset):
        rate_plan_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketAvailabilityResponse]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
start_date=start_date,
end_date=end_date,
number_of_days=number_of_days,
room_type_code=room_type_code,
rate_plan_code=rate_plan_code,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    property_id: str,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    number_of_days: int | Unset = 31,
    room_type_code: str | Unset = UNSET,
    rate_plan_code: str | Unset = UNSET,

) -> Error | TiketAvailabilityResponse | None:
    """ Read tiket.com rates, availability and restrictions

     What tiket.com holds for a property over a date window, read live from tiket.com: rooms to sell and
    booked per room type, prices (Room Based, or per number of guests on an Occupancy Based property,
    and children prices) and restrictions per rate plan. One row per night, room type and rate plan.

    `property_id` must be a tiket.com property connected to this workspace (`GET
    /v1/channels/tiket/properties`).

    Args:
        property_id (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        number_of_days (int | Unset):  Default: 31.
        room_type_code (str | Unset):
        rate_plan_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketAvailabilityResponse
     """


    return (await asyncio_detailed(
        client=client,
property_id=property_id,
start_date=start_date,
end_date=end_date,
number_of_days=number_of_days,
room_type_code=room_type_code,
rate_plan_code=rate_plan_code,

    )).parsed
