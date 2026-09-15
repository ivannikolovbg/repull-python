from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.quote import Quote
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    *,
    property_id: int,
    check_in: datetime.date,
    check_out: datetime.date,
    guests: int | Unset = 1,
    pets: int | Unset = 0,
    website_id: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["property_id"] = property_id

    json_check_in = check_in.isoformat()
    params["check_in"] = json_check_in

    json_check_out = check_out.isoformat()
    params["check_out"] = json_check_out

    params["guests"] = guests

    params["pets"] = pets

    params["website_id"] = website_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/quotes",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Quote | None:
    if response.status_code == 200:
        response_200 = Quote.from_dict(response.json())



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

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Quote]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    property_id: int,
    check_in: datetime.date,
    check_out: datetime.date,
    guests: int | Unset = 1,
    pets: int | Unset = 0,
    website_id: int | Unset = UNSET,

) -> Response[Error | Quote]:
    """ Price a stay

     Returns the full price breakdown for a stay — nightly total, length-of-stay discount, cleaning fee,
    pet and other fees, taxes, and the total.

    A quote is priced against a booking website, because the markup, custom fees and tax overrides that
    decide what a guest is actually charged live there. A workspace with no booking site receives `422
    quote_unavailable` rather than a number computed from different rules than the ones applied at
    checkout.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        property_id (int):
        check_in (datetime.date):
        check_out (datetime.date):
        guests (int | Unset):  Default: 1.
        pets (int | Unset):  Default: 0.
        website_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Quote]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
check_in=check_in,
check_out=check_out,
guests=guests,
pets=pets,
website_id=website_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    property_id: int,
    check_in: datetime.date,
    check_out: datetime.date,
    guests: int | Unset = 1,
    pets: int | Unset = 0,
    website_id: int | Unset = UNSET,

) -> Error | Quote | None:
    """ Price a stay

     Returns the full price breakdown for a stay — nightly total, length-of-stay discount, cleaning fee,
    pet and other fees, taxes, and the total.

    A quote is priced against a booking website, because the markup, custom fees and tax overrides that
    decide what a guest is actually charged live there. A workspace with no booking site receives `422
    quote_unavailable` rather than a number computed from different rules than the ones applied at
    checkout.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        property_id (int):
        check_in (datetime.date):
        check_out (datetime.date):
        guests (int | Unset):  Default: 1.
        pets (int | Unset):  Default: 0.
        website_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Quote
     """


    return sync_detailed(
        client=client,
property_id=property_id,
check_in=check_in,
check_out=check_out,
guests=guests,
pets=pets,
website_id=website_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    property_id: int,
    check_in: datetime.date,
    check_out: datetime.date,
    guests: int | Unset = 1,
    pets: int | Unset = 0,
    website_id: int | Unset = UNSET,

) -> Response[Error | Quote]:
    """ Price a stay

     Returns the full price breakdown for a stay — nightly total, length-of-stay discount, cleaning fee,
    pet and other fees, taxes, and the total.

    A quote is priced against a booking website, because the markup, custom fees and tax overrides that
    decide what a guest is actually charged live there. A workspace with no booking site receives `422
    quote_unavailable` rather than a number computed from different rules than the ones applied at
    checkout.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        property_id (int):
        check_in (datetime.date):
        check_out (datetime.date):
        guests (int | Unset):  Default: 1.
        pets (int | Unset):  Default: 0.
        website_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Quote]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
check_in=check_in,
check_out=check_out,
guests=guests,
pets=pets,
website_id=website_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    property_id: int,
    check_in: datetime.date,
    check_out: datetime.date,
    guests: int | Unset = 1,
    pets: int | Unset = 0,
    website_id: int | Unset = UNSET,

) -> Error | Quote | None:
    """ Price a stay

     Returns the full price breakdown for a stay — nightly total, length-of-stay discount, cleaning fee,
    pet and other fees, taxes, and the total.

    A quote is priced against a booking website, because the markup, custom fees and tax overrides that
    decide what a guest is actually charged live there. A workspace with no booking site receives `422
    quote_unavailable` rather than a number computed from different rules than the ones applied at
    checkout.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        property_id (int):
        check_in (datetime.date):
        check_out (datetime.date):
        guests (int | Unset):  Default: 1.
        pets (int | Unset):  Default: 0.
        website_id (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Quote
     """


    return (await asyncio_detailed(
        client=client,
property_id=property_id,
check_in=check_in,
check_out=check_out,
guests=guests,
pets=pets,
website_id=website_id,

    )).parsed
