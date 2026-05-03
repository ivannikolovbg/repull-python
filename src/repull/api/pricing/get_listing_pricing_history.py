from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.listing_pricing_history_response import ListingPricingHistoryResponse
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    id: int,
    *,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,

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

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/{id}/pricing/history".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListingPricingHistoryResponse | None:
    if response.status_code == 200:
        response_200 = ListingPricingHistoryResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListingPricingHistoryResponse]:
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
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,

) -> Response[Error | ListingPricingHistoryResponse]:
    """ Pricing recommendation audit trail

     Cursor-paginated audit trail of pricing recommendations vs applied prices for a listing across a
    date window. Use `pagination.nextCursor` from one response as the `cursor` query param of the next
    request.

    Defaults to ±90 days from today. Cursor is a keyset on `date ASC` — stable even if rows are added
    during a partner's pagination walk. `limit` is capped at 500 — exceeding returns 422.

    Args:
        id (int):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingPricingHistoryResponse]
     """


    kwargs = _get_kwargs(
        id=id,
start_date=start_date,
end_date=end_date,
limit=limit,
cursor=cursor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,

) -> Error | ListingPricingHistoryResponse | None:
    """ Pricing recommendation audit trail

     Cursor-paginated audit trail of pricing recommendations vs applied prices for a listing across a
    date window. Use `pagination.nextCursor` from one response as the `cursor` query param of the next
    request.

    Defaults to ±90 days from today. Cursor is a keyset on `date ASC` — stable even if rows are added
    during a partner's pagination walk. `limit` is capped at 500 — exceeding returns 422.

    Args:
        id (int):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingPricingHistoryResponse
     """


    return sync_detailed(
        id=id,
client=client,
start_date=start_date,
end_date=end_date,
limit=limit,
cursor=cursor,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,

) -> Response[Error | ListingPricingHistoryResponse]:
    """ Pricing recommendation audit trail

     Cursor-paginated audit trail of pricing recommendations vs applied prices for a listing across a
    date window. Use `pagination.nextCursor` from one response as the `cursor` query param of the next
    request.

    Defaults to ±90 days from today. Cursor is a keyset on `date ASC` — stable even if rows are added
    during a partner's pagination walk. `limit` is capped at 500 — exceeding returns 422.

    Args:
        id (int):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingPricingHistoryResponse]
     """


    kwargs = _get_kwargs(
        id=id,
start_date=start_date,
end_date=end_date,
limit=limit,
cursor=cursor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    limit: int | Unset = 100,
    cursor: str | Unset = UNSET,

) -> Error | ListingPricingHistoryResponse | None:
    """ Pricing recommendation audit trail

     Cursor-paginated audit trail of pricing recommendations vs applied prices for a listing across a
    date window. Use `pagination.nextCursor` from one response as the `cursor` query param of the next
    request.

    Defaults to ±90 days from today. Cursor is a keyset on `date ASC` — stable even if rows are added
    during a partner's pagination walk. `limit` is capped at 500 — exceeding returns 422.

    Args:
        id (int):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        limit (int | Unset):  Default: 100.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingPricingHistoryResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
start_date=start_date,
end_date=end_date,
limit=limit,
cursor=cursor,

    )).parsed
