from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_airbnb_listing_photo_response_200 import DeleteAirbnbListingPhotoResponse200
from ...models.error import Error
from typing import cast



def _get_kwargs(
    id: str,
    *,
    photo_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["photoId"] = photo_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/channels/airbnb/listings/{id}/photos".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteAirbnbListingPhotoResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = DeleteAirbnbListingPhotoResponse200.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteAirbnbListingPhotoResponse200 | Error]:
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
    photo_id: str,

) -> Response[DeleteAirbnbListingPhotoResponse200 | Error]:
    """ Delete an Airbnb photo

     Remove a single photo from an Airbnb listing. Pass the Airbnb-side photo id as `?photoId=`. Write-
    side — calls Airbnb upstream; the local photo cache is reconciled by the sync worker afterwards.

    Args:
        id (str):
        photo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAirbnbListingPhotoResponse200 | Error]
     """


    kwargs = _get_kwargs(
        id=id,
photo_id=photo_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    photo_id: str,

) -> DeleteAirbnbListingPhotoResponse200 | Error | None:
    """ Delete an Airbnb photo

     Remove a single photo from an Airbnb listing. Pass the Airbnb-side photo id as `?photoId=`. Write-
    side — calls Airbnb upstream; the local photo cache is reconciled by the sync worker afterwards.

    Args:
        id (str):
        photo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAirbnbListingPhotoResponse200 | Error
     """


    return sync_detailed(
        id=id,
client=client,
photo_id=photo_id,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    photo_id: str,

) -> Response[DeleteAirbnbListingPhotoResponse200 | Error]:
    """ Delete an Airbnb photo

     Remove a single photo from an Airbnb listing. Pass the Airbnb-side photo id as `?photoId=`. Write-
    side — calls Airbnb upstream; the local photo cache is reconciled by the sync worker afterwards.

    Args:
        id (str):
        photo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAirbnbListingPhotoResponse200 | Error]
     """


    kwargs = _get_kwargs(
        id=id,
photo_id=photo_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    photo_id: str,

) -> DeleteAirbnbListingPhotoResponse200 | Error | None:
    """ Delete an Airbnb photo

     Remove a single photo from an Airbnb listing. Pass the Airbnb-side photo id as `?photoId=`. Write-
    side — calls Airbnb upstream; the local photo cache is reconciled by the sync worker afterwards.

    Args:
        id (str):
        photo_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAirbnbListingPhotoResponse200 | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
photo_id=photo_id,

    )).parsed
