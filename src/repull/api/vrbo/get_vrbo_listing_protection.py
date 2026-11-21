from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_vrbo_listing_protection_response_200 import GetVrboListingProtectionResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    vrbo_listing_number: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["vrboListingNumber"] = vrbo_listing_number


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/vrbo/listings/{id}/protection".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetVrboListingProtectionResponse200 | None:
    if response.status_code == 200:
        response_200 = GetVrboListingProtectionResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetVrboListingProtectionResponse200]:
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

) -> Response[Error | GetVrboListingProtectionResponse200]:
    """ Get the Vrbo damage protection

     Refundable damage deposit and damage protection.

    Read live from the listing's Vrbo listing in the host's connected Vrbo account. **Cost:** 1 Vrbo
    call on Vrbo, spaced ~3 s apart per account — a few seconds. Vrbo is read live on every request
    (nothing is cached), so read the section you need rather than polling.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboListingProtectionResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
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
    vrbo_listing_number: str | Unset = UNSET,

) -> Error | GetVrboListingProtectionResponse200 | None:
    """ Get the Vrbo damage protection

     Refundable damage deposit and damage protection.

    Read live from the listing's Vrbo listing in the host's connected Vrbo account. **Cost:** 1 Vrbo
    call on Vrbo, spaced ~3 s apart per account — a few seconds. Vrbo is read live on every request
    (nothing is cached), so read the section you need rather than polling.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboListingProtectionResponse200
     """


    return sync_detailed(
        id=id,
client=client,
vrbo_listing_number=vrbo_listing_number,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    vrbo_listing_number: str | Unset = UNSET,

) -> Response[Error | GetVrboListingProtectionResponse200]:
    """ Get the Vrbo damage protection

     Refundable damage deposit and damage protection.

    Read live from the listing's Vrbo listing in the host's connected Vrbo account. **Cost:** 1 Vrbo
    call on Vrbo, spaced ~3 s apart per account — a few seconds. Vrbo is read live on every request
    (nothing is cached), so read the section you need rather than polling.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboListingProtectionResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
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
    vrbo_listing_number: str | Unset = UNSET,

) -> Error | GetVrboListingProtectionResponse200 | None:
    """ Get the Vrbo damage protection

     Refundable damage deposit and damage protection.

    Read live from the listing's Vrbo listing in the host's connected Vrbo account. **Cost:** 1 Vrbo
    call on Vrbo, spaced ~3 s apart per account — a few seconds. Vrbo is read live on every request
    (nothing is cached), so read the section you need rather than polling.

    Works with messaging or full access. Returns `404` when the listing is not linked to Vrbo, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboListingProtectionResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
vrbo_listing_number=vrbo_listing_number,

    )).parsed
