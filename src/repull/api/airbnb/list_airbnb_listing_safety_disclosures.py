from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_airbnb_listing_safety_disclosures_response_200 import ListAirbnbListingSafetyDisclosuresResponse200
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/listings/{id}/safety-disclosures".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListAirbnbListingSafetyDisclosuresResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAirbnbListingSafetyDisclosuresResponse200.from_dict(response.json())



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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListAirbnbListingSafetyDisclosuresResponse200]:
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

) -> Response[Error | ListAirbnbListingSafetyDisclosuresResponse200]:
    r""" List guest-safety disclosures

     What a guest is told about the property before they book — exterior security cameras, a decibel
    noise monitor, pets on the property, stairs, a pool with no fence, weapons, shared spaces, limited
    parking. Airbnb calls them `listing_expectations_for_guests` and shows them at booking time.

    **Pure DB read** from the local mirror. EVERY supported disclosure type is returned, including the
    ones this listing has not declared (`value: false`), so \"does this property have cameras?\" has an
    answer rather than a missing key — `declared` tells you whether Airbnb holds an explicit answer.
    Types Airbnb returns that are not in the documented set are passed through rather than dropped.

    Where a listing is connected to several Airbnb listings, a disclosure declared on any of them is
    reported as true of the property.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbListingSafetyDisclosuresResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | ListAirbnbListingSafetyDisclosuresResponse200 | None:
    r""" List guest-safety disclosures

     What a guest is told about the property before they book — exterior security cameras, a decibel
    noise monitor, pets on the property, stairs, a pool with no fence, weapons, shared spaces, limited
    parking. Airbnb calls them `listing_expectations_for_guests` and shows them at booking time.

    **Pure DB read** from the local mirror. EVERY supported disclosure type is returned, including the
    ones this listing has not declared (`value: false`), so \"does this property have cameras?\" has an
    answer rather than a missing key — `declared` tells you whether Airbnb holds an explicit answer.
    Types Airbnb returns that are not in the documented set are passed through rather than dropped.

    Where a listing is connected to several Airbnb listings, a disclosure declared on any of them is
    reported as true of the property.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbListingSafetyDisclosuresResponse200
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | ListAirbnbListingSafetyDisclosuresResponse200]:
    r""" List guest-safety disclosures

     What a guest is told about the property before they book — exterior security cameras, a decibel
    noise monitor, pets on the property, stairs, a pool with no fence, weapons, shared spaces, limited
    parking. Airbnb calls them `listing_expectations_for_guests` and shows them at booking time.

    **Pure DB read** from the local mirror. EVERY supported disclosure type is returned, including the
    ones this listing has not declared (`value: false`), so \"does this property have cameras?\" has an
    answer rather than a missing key — `declared` tells you whether Airbnb holds an explicit answer.
    Types Airbnb returns that are not in the documented set are passed through rather than dropped.

    Where a listing is connected to several Airbnb listings, a disclosure declared on any of them is
    reported as true of the property.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbListingSafetyDisclosuresResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | ListAirbnbListingSafetyDisclosuresResponse200 | None:
    r""" List guest-safety disclosures

     What a guest is told about the property before they book — exterior security cameras, a decibel
    noise monitor, pets on the property, stairs, a pool with no fence, weapons, shared spaces, limited
    parking. Airbnb calls them `listing_expectations_for_guests` and shows them at booking time.

    **Pure DB read** from the local mirror. EVERY supported disclosure type is returned, including the
    ones this listing has not declared (`value: false`), so \"does this property have cameras?\" has an
    answer rather than a missing key — `declared` tells you whether Airbnb holds an explicit answer.
    Types Airbnb returns that are not in the documented set are passed through rather than dropped.

    Where a listing is connected to several Airbnb listings, a disclosure declared on any of them is
    reported as true of the property.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbListingSafetyDisclosuresResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
