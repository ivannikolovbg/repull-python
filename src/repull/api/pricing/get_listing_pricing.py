from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.listing_pricing_response import ListingPricingResponse
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    id: int,
    *,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,

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


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings/{id}/pricing".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ListingPricingResponse | None:
    if response.status_code == 200:
        response_200 = ListingPricingResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ListingPricingResponse]:
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

) -> Response[Any | ListingPricingResponse]:
    """ Get pricing recommendations

     Returns date-by-date pricing recommendations for a listing's upcoming calendar window, plus the
    listing's base-price context and a 5km comp summary. Recommendations come from the Atlas pricing
    model — pre-computed nightly and stored in `pricing_recommendations`. Use POST to apply or decline
    pending recommendations.

    Args:
        id (int):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListingPricingResponse]
     """


    kwargs = _get_kwargs(
        id=id,
start_date=start_date,
end_date=end_date,

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

) -> Any | ListingPricingResponse | None:
    """ Get pricing recommendations

     Returns date-by-date pricing recommendations for a listing's upcoming calendar window, plus the
    listing's base-price context and a 5km comp summary. Recommendations come from the Atlas pricing
    model — pre-computed nightly and stored in `pricing_recommendations`. Use POST to apply or decline
    pending recommendations.

    Args:
        id (int):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListingPricingResponse
     """


    return sync_detailed(
        id=id,
client=client,
start_date=start_date,
end_date=end_date,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,

) -> Response[Any | ListingPricingResponse]:
    """ Get pricing recommendations

     Returns date-by-date pricing recommendations for a listing's upcoming calendar window, plus the
    listing's base-price context and a 5km comp summary. Recommendations come from the Atlas pricing
    model — pre-computed nightly and stored in `pricing_recommendations`. Use POST to apply or decline
    pending recommendations.

    Args:
        id (int):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListingPricingResponse]
     """


    kwargs = _get_kwargs(
        id=id,
start_date=start_date,
end_date=end_date,

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

) -> Any | ListingPricingResponse | None:
    """ Get pricing recommendations

     Returns date-by-date pricing recommendations for a listing's upcoming calendar window, plus the
    listing's base-price context and a 5km comp summary. Recommendations come from the Atlas pricing
    model — pre-computed nightly and stored in `pricing_recommendations`. Use POST to apply or decline
    pending recommendations.

    Args:
        id (int):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListingPricingResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
start_date=start_date,
end_date=end_date,

    )).parsed
