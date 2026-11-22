from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.update_airbnb_house_rules_body import UpdateAirbnbHouseRulesBody
from ...models.update_airbnb_house_rules_response_200 import UpdateAirbnbHouseRulesResponse200
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: UpdateAirbnbHouseRulesBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/airbnb/listings/{id}/house-rules".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | UpdateAirbnbHouseRulesResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateAirbnbHouseRulesResponse200.from_dict(response.json())



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

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | UpdateAirbnbHouseRulesResponse200]:
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
    body: UpdateAirbnbHouseRulesBody,

) -> Response[Error | UpdateAirbnbHouseRulesResponse200]:
    """ Update Airbnb house rules

     Write the house rules text for one language — the same write as `PUT …/descriptions` `{ locale,
    description: { house_rules } }`, with the same answer (`written`, `blockedFields`). On Airbnb the
    check-in and check-out times are booking settings: set them with `PUT …/booking-settings`. Whether
    pets, smoking, events or children are allowed is set in the Airbnb app.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        body (UpdateAirbnbHouseRulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbHouseRulesResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAirbnbHouseRulesBody,

) -> Error | UpdateAirbnbHouseRulesResponse200 | None:
    """ Update Airbnb house rules

     Write the house rules text for one language — the same write as `PUT …/descriptions` `{ locale,
    description: { house_rules } }`, with the same answer (`written`, `blockedFields`). On Airbnb the
    check-in and check-out times are booking settings: set them with `PUT …/booking-settings`. Whether
    pets, smoking, events or children are allowed is set in the Airbnb app.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        body (UpdateAirbnbHouseRulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbHouseRulesResponse200
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAirbnbHouseRulesBody,

) -> Response[Error | UpdateAirbnbHouseRulesResponse200]:
    """ Update Airbnb house rules

     Write the house rules text for one language — the same write as `PUT …/descriptions` `{ locale,
    description: { house_rules } }`, with the same answer (`written`, `blockedFields`). On Airbnb the
    check-in and check-out times are booking settings: set them with `PUT …/booking-settings`. Whether
    pets, smoking, events or children are allowed is set in the Airbnb app.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        body (UpdateAirbnbHouseRulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbHouseRulesResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateAirbnbHouseRulesBody,

) -> Error | UpdateAirbnbHouseRulesResponse200 | None:
    """ Update Airbnb house rules

     Write the house rules text for one language — the same write as `PUT …/descriptions` `{ locale,
    description: { house_rules } }`, with the same answer (`written`, `blockedFields`). On Airbnb the
    check-in and check-out times are booking settings: set them with `PUT …/booking-settings`. Whether
    pets, smoking, events or children are allowed is set in the Airbnb app.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        body (UpdateAirbnbHouseRulesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbHouseRulesResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
