from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_vrbo_listing_rates_response_200 import GetVrboListingRatesResponse200
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    id: str,
    *,
    vrbo_listing_number: str | Unset = UNSET,
    start: datetime.date | Unset = UNSET,
    end: datetime.date | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["vrboListingNumber"] = vrbo_listing_number

    json_start: str | Unset = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    json_end: str | Unset = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/vrbo/listings/{id}/rates".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetVrboListingRatesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetVrboListingRatesResponse200.from_dict(response.json())



        return response_200

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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

    if response.status_code == 504:
        response_504 = Error.from_dict(response.json())



        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetVrboListingRatesResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    vrbo_listing_number: str | Unset = UNSET,
    start: datetime.date | Unset = UNSET,
    end: datetime.date | Unset = UNSET,

) -> Response[Error | GetVrboListingRatesResponse200]:
    """ Get the Vrbo rates and stay discounts

     Per night over a date range: the nightly rate, its weekday, the weekly (7–27 nights) and monthly
    (28+ nights) discounts and the minimum stay. Vrbo offers only these two stay discounts, saved per
    night with the weekday prices.

    Read live from Vrbo on every request (a date range). **Cost:** 1 Vrbo calendar call (`?start=&end=`,
    default today + 13 days) on Vrbo, spaced ~3 s apart per account.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        start (datetime.date | Unset):
        end (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboListingRatesResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
vrbo_listing_number=vrbo_listing_number,
start=start,
end=end,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    vrbo_listing_number: str | Unset = UNSET,
    start: datetime.date | Unset = UNSET,
    end: datetime.date | Unset = UNSET,

) -> Error | GetVrboListingRatesResponse200 | None:
    """ Get the Vrbo rates and stay discounts

     Per night over a date range: the nightly rate, its weekday, the weekly (7–27 nights) and monthly
    (28+ nights) discounts and the minimum stay. Vrbo offers only these two stay discounts, saved per
    night with the weekday prices.

    Read live from Vrbo on every request (a date range). **Cost:** 1 Vrbo calendar call (`?start=&end=`,
    default today + 13 days) on Vrbo, spaced ~3 s apart per account.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        start (datetime.date | Unset):
        end (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboListingRatesResponse200
     """


    return sync_detailed(
        id=id,
client=client,
vrbo_listing_number=vrbo_listing_number,
start=start,
end=end,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    vrbo_listing_number: str | Unset = UNSET,
    start: datetime.date | Unset = UNSET,
    end: datetime.date | Unset = UNSET,

) -> Response[Error | GetVrboListingRatesResponse200]:
    """ Get the Vrbo rates and stay discounts

     Per night over a date range: the nightly rate, its weekday, the weekly (7–27 nights) and monthly
    (28+ nights) discounts and the minimum stay. Vrbo offers only these two stay discounts, saved per
    night with the weekday prices.

    Read live from Vrbo on every request (a date range). **Cost:** 1 Vrbo calendar call (`?start=&end=`,
    default today + 13 days) on Vrbo, spaced ~3 s apart per account.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        start (datetime.date | Unset):
        end (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboListingRatesResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
vrbo_listing_number=vrbo_listing_number,
start=start,
end=end,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    vrbo_listing_number: str | Unset = UNSET,
    start: datetime.date | Unset = UNSET,
    end: datetime.date | Unset = UNSET,

) -> Error | GetVrboListingRatesResponse200 | None:
    """ Get the Vrbo rates and stay discounts

     Per night over a date range: the nightly rate, its weekday, the weekly (7–27 nights) and monthly
    (28+ nights) discounts and the minimum stay. Vrbo offers only these two stay discounts, saved per
    night with the weekday prices.

    Read live from Vrbo on every request (a date range). **Cost:** 1 Vrbo calendar call (`?start=&end=`,
    default today + 13 days) on Vrbo, spaced ~3 s apart per account.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        start (datetime.date | Unset):
        end (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboListingRatesResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
vrbo_listing_number=vrbo_listing_number,
start=start,
end=end,

    )).parsed
