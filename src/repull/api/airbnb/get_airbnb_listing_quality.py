from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_airbnb_listing_quality_response_200 import GetAirbnbListingQualityResponse200
from ...models.get_airbnb_listing_quality_type import GetAirbnbListingQualityType
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    type_: GetAirbnbListingQualityType | Unset = GetAirbnbListingQualityType.ALL,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/listings/{id}/quality".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetAirbnbListingQualityResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAirbnbListingQualityResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetAirbnbListingQualityResponse200]:
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
    type_: GetAirbnbListingQualityType | Unset = GetAirbnbListingQualityType.ALL,

) -> Response[Error | GetAirbnbListingQualityResponse200]:
    """ Get Airbnb listing quality

     Return an Airbnb listing's quality signals — standards, reservation issues, and monthly quality
    stats. **Pure DB read** from the local quality mirrors. Scope the response with
    `?type=all|standards|issues|stats` (default `all`, which returns `{ standards, issues }`). Returns
    `404` when the listing has no Airbnb connection in this workspace.

    Args:
        id (str):
        type_ (GetAirbnbListingQualityType | Unset):  Default: GetAirbnbListingQualityType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetAirbnbListingQualityResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
type_=type_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: GetAirbnbListingQualityType | Unset = GetAirbnbListingQualityType.ALL,

) -> Error | GetAirbnbListingQualityResponse200 | None:
    """ Get Airbnb listing quality

     Return an Airbnb listing's quality signals — standards, reservation issues, and monthly quality
    stats. **Pure DB read** from the local quality mirrors. Scope the response with
    `?type=all|standards|issues|stats` (default `all`, which returns `{ standards, issues }`). Returns
    `404` when the listing has no Airbnb connection in this workspace.

    Args:
        id (str):
        type_ (GetAirbnbListingQualityType | Unset):  Default: GetAirbnbListingQualityType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetAirbnbListingQualityResponse200
     """


    return sync_detailed(
        id=id,
client=client,
type_=type_,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: GetAirbnbListingQualityType | Unset = GetAirbnbListingQualityType.ALL,

) -> Response[Error | GetAirbnbListingQualityResponse200]:
    """ Get Airbnb listing quality

     Return an Airbnb listing's quality signals — standards, reservation issues, and monthly quality
    stats. **Pure DB read** from the local quality mirrors. Scope the response with
    `?type=all|standards|issues|stats` (default `all`, which returns `{ standards, issues }`). Returns
    `404` when the listing has no Airbnb connection in this workspace.

    Args:
        id (str):
        type_ (GetAirbnbListingQualityType | Unset):  Default: GetAirbnbListingQualityType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetAirbnbListingQualityResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
type_=type_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    type_: GetAirbnbListingQualityType | Unset = GetAirbnbListingQualityType.ALL,

) -> Error | GetAirbnbListingQualityResponse200 | None:
    """ Get Airbnb listing quality

     Return an Airbnb listing's quality signals — standards, reservation issues, and monthly quality
    stats. **Pure DB read** from the local quality mirrors. Scope the response with
    `?type=all|standards|issues|stats` (default `all`, which returns `{ standards, issues }`). Returns
    `404` when the listing has no Airbnb connection in this workspace.

    Args:
        id (str):
        type_ (GetAirbnbListingQualityType | Unset):  Default: GetAirbnbListingQualityType.ALL.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetAirbnbListingQualityResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
type_=type_,

    )).parsed
