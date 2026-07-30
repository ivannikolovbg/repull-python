from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_airbnb_checkin_guide_response_200 import GetAirbnbCheckinGuideResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    locale: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["locale"] = locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/listings/{id}/checkin-guide".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetAirbnbCheckinGuideResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAirbnbCheckinGuideResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetAirbnbCheckinGuideResponse200]:
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
    locale: str | Unset = UNSET,

) -> Response[Error | GetAirbnbCheckinGuideResponse200]:
    """ Get Airbnb check-in guide

     Return every published locale variant of an Airbnb listing's check-in guide. **Pure DB read** from
    `listings_airbnb_check_in_guides`. Pass `?locale=en` to filter to one locale (prefix match). Returns
    `404` when the listing has no Airbnb connection in this workspace.

    Args:
        id (str):
        locale (str | Unset):  Example: en.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetAirbnbCheckinGuideResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
locale=locale,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> Error | GetAirbnbCheckinGuideResponse200 | None:
    """ Get Airbnb check-in guide

     Return every published locale variant of an Airbnb listing's check-in guide. **Pure DB read** from
    `listings_airbnb_check_in_guides`. Pass `?locale=en` to filter to one locale (prefix match). Returns
    `404` when the listing has no Airbnb connection in this workspace.

    Args:
        id (str):
        locale (str | Unset):  Example: en.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetAirbnbCheckinGuideResponse200
     """


    return sync_detailed(
        id=id,
client=client,
locale=locale,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> Response[Error | GetAirbnbCheckinGuideResponse200]:
    """ Get Airbnb check-in guide

     Return every published locale variant of an Airbnb listing's check-in guide. **Pure DB read** from
    `listings_airbnb_check_in_guides`. Pass `?locale=en` to filter to one locale (prefix match). Returns
    `404` when the listing has no Airbnb connection in this workspace.

    Args:
        id (str):
        locale (str | Unset):  Example: en.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetAirbnbCheckinGuideResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
locale=locale,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    locale: str | Unset = UNSET,

) -> Error | GetAirbnbCheckinGuideResponse200 | None:
    """ Get Airbnb check-in guide

     Return every published locale variant of an Airbnb listing's check-in guide. **Pure DB read** from
    `listings_airbnb_check_in_guides`. Pass `?locale=en` to filter to one locale (prefix match). Returns
    `404` when the listing has no Airbnb connection in this workspace.

    Args:
        id (str):
        locale (str | Unset):  Example: en.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetAirbnbCheckinGuideResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
locale=locale,

    )).parsed
