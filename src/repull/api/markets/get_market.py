from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.market_detail_response import MarketDetailResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    city: str,
    *,
    comps_page: int | Unset = 1,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["compsPage"] = comps_page


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/markets/{city}".format(city=quote(str(city), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | MarketDetailResponse | None:
    if response.status_code == 200:
        response_200 = MarketDetailResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 502:
        response_502 = cast(Any, None)
        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error | MarketDetailResponse]:
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
    comps_page: int | Unset = 1,

) -> Response[Any | Error | MarketDetailResponse]:
    """ Deep-dive on a single market

     Detailed market view for one city — price distribution, bedroom mix, property types, upcoming
    events, Wheelhouse demand, monthly benchmarks, customer health rollup, top comps (proximity-sorted,
    paginated), customer's percentile position, capacity-mix gap, and a 6-month supply trend.

    Args:
        city (str):
        comps_page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | MarketDetailResponse]
     """


    kwargs = _get_kwargs(
        city=city,
comps_page=comps_page,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    city: str,
    *,
    client: AuthenticatedClient | Client,
    comps_page: int | Unset = 1,

) -> Any | Error | MarketDetailResponse | None:
    """ Deep-dive on a single market

     Detailed market view for one city — price distribution, bedroom mix, property types, upcoming
    events, Wheelhouse demand, monthly benchmarks, customer health rollup, top comps (proximity-sorted,
    paginated), customer's percentile position, capacity-mix gap, and a 6-month supply trend.

    Args:
        city (str):
        comps_page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | MarketDetailResponse
     """


    return sync_detailed(
        city=city,
client=client,
comps_page=comps_page,

    ).parsed

async def asyncio_detailed(
    city: str,
    *,
    client: AuthenticatedClient | Client,
    comps_page: int | Unset = 1,

) -> Response[Any | Error | MarketDetailResponse]:
    """ Deep-dive on a single market

     Detailed market view for one city — price distribution, bedroom mix, property types, upcoming
    events, Wheelhouse demand, monthly benchmarks, customer health rollup, top comps (proximity-sorted,
    paginated), customer's percentile position, capacity-mix gap, and a 6-month supply trend.

    Args:
        city (str):
        comps_page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | MarketDetailResponse]
     """


    kwargs = _get_kwargs(
        city=city,
comps_page=comps_page,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    city: str,
    *,
    client: AuthenticatedClient | Client,
    comps_page: int | Unset = 1,

) -> Any | Error | MarketDetailResponse | None:
    """ Deep-dive on a single market

     Detailed market view for one city — price distribution, bedroom mix, property types, upcoming
    events, Wheelhouse demand, monthly benchmarks, customer health rollup, top comps (proximity-sorted,
    paginated), customer's percentile position, capacity-mix gap, and a 6-month supply trend.

    Args:
        city (str):
        comps_page (int | Unset):  Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | MarketDetailResponse
     """


    return (await asyncio_detailed(
        city=city,
client=client,
comps_page=comps_page,

    )).parsed
