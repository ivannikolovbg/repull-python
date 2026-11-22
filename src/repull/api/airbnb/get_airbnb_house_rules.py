from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_airbnb_house_rules_response_200 import GetAirbnbHouseRulesResponse200
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/listings/{id}/house-rules".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetAirbnbHouseRulesResponse200 | None:
    if response.status_code == 200:
        response_200 = GetAirbnbHouseRulesResponse200.from_dict(response.json())



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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetAirbnbHouseRulesResponse200]:
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

) -> Response[Error | GetAirbnbHouseRulesResponse200]:
    r""" Get Airbnb house rules

     The listing's house rules under the names Vrbo's `GET /v1/channels/vrbo/listings/{id}/house-rules`
    uses: check-in and check-out times, guest capacity, whether children, infants, pets, smoking and
    events are allowed, Airbnb's \"things to know\" (`expectations`), and the written rules per
    language. **Repull's stored copy**, like every Airbnb read: check `dataFreshness` before treating a
    value as current. `POST /v1/listings/{id}/pull/airbnb` refreshes it from Airbnb.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetAirbnbHouseRulesResponse200]
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

) -> Error | GetAirbnbHouseRulesResponse200 | None:
    r""" Get Airbnb house rules

     The listing's house rules under the names Vrbo's `GET /v1/channels/vrbo/listings/{id}/house-rules`
    uses: check-in and check-out times, guest capacity, whether children, infants, pets, smoking and
    events are allowed, Airbnb's \"things to know\" (`expectations`), and the written rules per
    language. **Repull's stored copy**, like every Airbnb read: check `dataFreshness` before treating a
    value as current. `POST /v1/listings/{id}/pull/airbnb` refreshes it from Airbnb.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetAirbnbHouseRulesResponse200
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetAirbnbHouseRulesResponse200]:
    r""" Get Airbnb house rules

     The listing's house rules under the names Vrbo's `GET /v1/channels/vrbo/listings/{id}/house-rules`
    uses: check-in and check-out times, guest capacity, whether children, infants, pets, smoking and
    events are allowed, Airbnb's \"things to know\" (`expectations`), and the written rules per
    language. **Repull's stored copy**, like every Airbnb read: check `dataFreshness` before treating a
    value as current. `POST /v1/listings/{id}/pull/airbnb` refreshes it from Airbnb.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetAirbnbHouseRulesResponse200]
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

) -> Error | GetAirbnbHouseRulesResponse200 | None:
    r""" Get Airbnb house rules

     The listing's house rules under the names Vrbo's `GET /v1/channels/vrbo/listings/{id}/house-rules`
    uses: check-in and check-out times, guest capacity, whether children, infants, pets, smoking and
    events are allowed, Airbnb's \"things to know\" (`expectations`), and the written rules per
    language. **Repull's stored copy**, like every Airbnb read: check `dataFreshness` before treating a
    value as current. `POST /v1/listings/{id}/pull/airbnb` refreshes it from Airbnb.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetAirbnbHouseRulesResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
