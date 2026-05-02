from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.market_calendar_response import MarketCalendarResponse
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    city: str,
    *,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    listing_id: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    params["listingId"] = listing_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/markets/{city}/calendar".format(city=quote(str(city), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | MarketCalendarResponse | None:
    if response.status_code == 200:
        response_200 = MarketCalendarResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 502:
        response_502 = cast(Any, None)
        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | MarketCalendarResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    city: str,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    listing_id: int | Unset = UNSET,

) -> Response[Any | MarketCalendarResponse]:
    """ Calendar-level market view

     Date-by-date market view for a city — market avg / min / max nightly rate, occupancy %, Wheelhouse
    demand, events touching the date, and (when `listingId` is supplied) an overlay of the customer's
    own pricing + availability.

    Args:
        city (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        listing_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MarketCalendarResponse]
     """


    kwargs = _get_kwargs(
        city=city,
start_date=start_date,
end_date=end_date,
listing_id=listing_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    city: str,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    listing_id: int | Unset = UNSET,

) -> Any | MarketCalendarResponse | None:
    """ Calendar-level market view

     Date-by-date market view for a city — market avg / min / max nightly rate, occupancy %, Wheelhouse
    demand, events touching the date, and (when `listingId` is supplied) an overlay of the customer's
    own pricing + availability.

    Args:
        city (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        listing_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MarketCalendarResponse
     """


    return sync_detailed(
        city=city,
client=client,
start_date=start_date,
end_date=end_date,
listing_id=listing_id,

    ).parsed

async def asyncio_detailed(
    city: str,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    listing_id: int | Unset = UNSET,

) -> Response[Any | MarketCalendarResponse]:
    """ Calendar-level market view

     Date-by-date market view for a city — market avg / min / max nightly rate, occupancy %, Wheelhouse
    demand, events touching the date, and (when `listingId` is supplied) an overlay of the customer's
    own pricing + availability.

    Args:
        city (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        listing_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | MarketCalendarResponse]
     """


    kwargs = _get_kwargs(
        city=city,
start_date=start_date,
end_date=end_date,
listing_id=listing_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    city: str,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    listing_id: int | Unset = UNSET,

) -> Any | MarketCalendarResponse | None:
    """ Calendar-level market view

     Date-by-date market view for a city — market avg / min / max nightly rate, occupancy %, Wheelhouse
    demand, events touching the date, and (when `listingId` is supplied) an overlay of the customer's
    own pricing + availability.

    Args:
        city (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        listing_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | MarketCalendarResponse
     """


    return (await asyncio_detailed(
        city=city,
client=client,
start_date=start_date,
end_date=end_date,
listing_id=listing_id,

    )).parsed
