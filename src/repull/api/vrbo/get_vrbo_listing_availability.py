from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_vrbo_listing_availability_response_200 import GetVrboListingAvailabilityResponse200
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    id: str,
    *,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    job_id: str | Unset = UNSET,
    vrbo_listing_number: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    params["jobId"] = job_id

    params["vrboListingNumber"] = vrbo_listing_number


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/vrbo/listings/{id}/availability".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetVrboListingAvailabilityResponse200 | None:
    if response.status_code == 200:
        response_200 = GetVrboListingAvailabilityResponse200.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetVrboListingAvailabilityResponse200]:
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
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    job_id: str | Unset = UNSET,
    vrbo_listing_number: str | Unset = UNSET,

) -> Response[Error | GetVrboListingAvailabilityResponse200]:
    """ Get the Vrbo calendar

     The listing's calendar as Vrbo shows it, night by night — the counterpart of `GET
    /v1/channels/airbnb/listings/{id}/availability`: whether each night is `available`, what holds it
    (`blockedBy`: a `reservation`, a `block` or an imported `ical` calendar, with the booking's
    `reservationRef`), the nightly price, minimum stay and whether guests can arrive or leave that day.

    Read from Vrbo for each request (one Vrbo read for the range): `start_date`..`end_date`, at most 366
    nights, default the next 30. `?jobId=` reads the status of a write instead.

    Args:
        id (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        job_id (str | Unset):
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboListingAvailabilityResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
start_date=start_date,
end_date=end_date,
job_id=job_id,
vrbo_listing_number=vrbo_listing_number,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    job_id: str | Unset = UNSET,
    vrbo_listing_number: str | Unset = UNSET,

) -> Error | GetVrboListingAvailabilityResponse200 | None:
    """ Get the Vrbo calendar

     The listing's calendar as Vrbo shows it, night by night — the counterpart of `GET
    /v1/channels/airbnb/listings/{id}/availability`: whether each night is `available`, what holds it
    (`blockedBy`: a `reservation`, a `block` or an imported `ical` calendar, with the booking's
    `reservationRef`), the nightly price, minimum stay and whether guests can arrive or leave that day.

    Read from Vrbo for each request (one Vrbo read for the range): `start_date`..`end_date`, at most 366
    nights, default the next 30. `?jobId=` reads the status of a write instead.

    Args:
        id (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        job_id (str | Unset):
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboListingAvailabilityResponse200
     """


    return sync_detailed(
        id=id,
client=client,
start_date=start_date,
end_date=end_date,
job_id=job_id,
vrbo_listing_number=vrbo_listing_number,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    job_id: str | Unset = UNSET,
    vrbo_listing_number: str | Unset = UNSET,

) -> Response[Error | GetVrboListingAvailabilityResponse200]:
    """ Get the Vrbo calendar

     The listing's calendar as Vrbo shows it, night by night — the counterpart of `GET
    /v1/channels/airbnb/listings/{id}/availability`: whether each night is `available`, what holds it
    (`blockedBy`: a `reservation`, a `block` or an imported `ical` calendar, with the booking's
    `reservationRef`), the nightly price, minimum stay and whether guests can arrive or leave that day.

    Read from Vrbo for each request (one Vrbo read for the range): `start_date`..`end_date`, at most 366
    nights, default the next 30. `?jobId=` reads the status of a write instead.

    Args:
        id (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        job_id (str | Unset):
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboListingAvailabilityResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
start_date=start_date,
end_date=end_date,
job_id=job_id,
vrbo_listing_number=vrbo_listing_number,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    job_id: str | Unset = UNSET,
    vrbo_listing_number: str | Unset = UNSET,

) -> Error | GetVrboListingAvailabilityResponse200 | None:
    """ Get the Vrbo calendar

     The listing's calendar as Vrbo shows it, night by night — the counterpart of `GET
    /v1/channels/airbnb/listings/{id}/availability`: whether each night is `available`, what holds it
    (`blockedBy`: a `reservation`, a `block` or an imported `ical` calendar, with the booking's
    `reservationRef`), the nightly price, minimum stay and whether guests can arrive or leave that day.

    Read from Vrbo for each request (one Vrbo read for the range): `start_date`..`end_date`, at most 366
    nights, default the next 30. `?jobId=` reads the status of a write instead.

    Args:
        id (str):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        job_id (str | Unset):
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboListingAvailabilityResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
start_date=start_date,
end_date=end_date,
job_id=job_id,
vrbo_listing_number=vrbo_listing_number,

    )).parsed
