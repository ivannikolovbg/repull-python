from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.calendar_response import CalendarResponse
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    property_id: int,
    *,
    start_date: datetime.date,
    end_date: datetime.date,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/availability/{property_id}".format(property_id=quote(str(property_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CalendarResponse | None:
    if response.status_code == 200:
        response_200 = CalendarResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CalendarResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    property_id: int,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date,
    end_date: datetime.date,

) -> Response[CalendarResponse]:
    """ Get availability calendar

     Returns day-by-day availability, pricing, and minimum stay for a property.

    Args:
        property_id (int):
        start_date (datetime.date):
        end_date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarResponse]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
start_date=start_date,
end_date=end_date,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    property_id: int,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date,
    end_date: datetime.date,

) -> CalendarResponse | None:
    """ Get availability calendar

     Returns day-by-day availability, pricing, and minimum stay for a property.

    Args:
        property_id (int):
        start_date (datetime.date):
        end_date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarResponse
     """


    return sync_detailed(
        property_id=property_id,
client=client,
start_date=start_date,
end_date=end_date,

    ).parsed

async def asyncio_detailed(
    property_id: int,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date,
    end_date: datetime.date,

) -> Response[CalendarResponse]:
    """ Get availability calendar

     Returns day-by-day availability, pricing, and minimum stay for a property.

    Args:
        property_id (int):
        start_date (datetime.date):
        end_date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CalendarResponse]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
start_date=start_date,
end_date=end_date,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    property_id: int,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date,
    end_date: datetime.date,

) -> CalendarResponse | None:
    """ Get availability calendar

     Returns day-by-day availability, pricing, and minimum stay for a property.

    Args:
        property_id (int):
        start_date (datetime.date):
        end_date (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CalendarResponse
     """


    return (await asyncio_detailed(
        property_id=property_id,
client=client,
start_date=start_date,
end_date=end_date,

    )).parsed
