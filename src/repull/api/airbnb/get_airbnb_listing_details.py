from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_airbnb_listing_details_response_200 import GetAirbnbListingDetailsResponse200
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/listings/{id}/details".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetAirbnbListingDetailsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAirbnbListingDetailsResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetAirbnbListingDetailsResponse200]:
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

) -> Response[Error | GetAirbnbListingDetailsResponse200]:
    """ Get Airbnb listing details

     What kind of property Airbnb thinks this is — property type group and category, room type, capacity
    — plus the check-in method (`checkInOption`), whether the listing is live (`hasAvailability`), and
    **`lockedFields`: the attributes Airbnb refuses to change on this listing**.

    **Pure DB read** from the local mirror, one entry per Airbnb connection.

    Read `lockedFields` before a content write. Airbnb does not refuse a write to a locked attribute: it
    returns 200, reports the attribute as locked, and applies nothing — which is why a write can look
    successful and change nothing. 1,180 of 5,917 synced listings carry at least one locked attribute.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetAirbnbListingDetailsResponse200]
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

) -> Error | GetAirbnbListingDetailsResponse200 | None:
    """ Get Airbnb listing details

     What kind of property Airbnb thinks this is — property type group and category, room type, capacity
    — plus the check-in method (`checkInOption`), whether the listing is live (`hasAvailability`), and
    **`lockedFields`: the attributes Airbnb refuses to change on this listing**.

    **Pure DB read** from the local mirror, one entry per Airbnb connection.

    Read `lockedFields` before a content write. Airbnb does not refuse a write to a locked attribute: it
    returns 200, reports the attribute as locked, and applies nothing — which is why a write can look
    successful and change nothing. 1,180 of 5,917 synced listings carry at least one locked attribute.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetAirbnbListingDetailsResponse200
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetAirbnbListingDetailsResponse200]:
    """ Get Airbnb listing details

     What kind of property Airbnb thinks this is — property type group and category, room type, capacity
    — plus the check-in method (`checkInOption`), whether the listing is live (`hasAvailability`), and
    **`lockedFields`: the attributes Airbnb refuses to change on this listing**.

    **Pure DB read** from the local mirror, one entry per Airbnb connection.

    Read `lockedFields` before a content write. Airbnb does not refuse a write to a locked attribute: it
    returns 200, reports the attribute as locked, and applies nothing — which is why a write can look
    successful and change nothing. 1,180 of 5,917 synced listings carry at least one locked attribute.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetAirbnbListingDetailsResponse200]
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

) -> Error | GetAirbnbListingDetailsResponse200 | None:
    """ Get Airbnb listing details

     What kind of property Airbnb thinks this is — property type group and category, room type, capacity
    — plus the check-in method (`checkInOption`), whether the listing is live (`hasAvailability`), and
    **`lockedFields`: the attributes Airbnb refuses to change on this listing**.

    **Pure DB read** from the local mirror, one entry per Airbnb connection.

    Read `lockedFields` before a content write. Airbnb does not refuse a write to a locked attribute: it
    returns 200, reports the attribute as locked, and applies nothing — which is why a write can look
    successful and change nothing. 1,180 of 5,917 synced listings carry at least one locked attribute.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetAirbnbListingDetailsResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
