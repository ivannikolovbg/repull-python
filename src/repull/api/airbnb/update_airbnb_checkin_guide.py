from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.update_airbnb_checkin_guide_body import UpdateAirbnbCheckinGuideBody
from ...models.update_airbnb_checkin_guide_response_200 import UpdateAirbnbCheckinGuideResponse200
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: UpdateAirbnbCheckinGuideBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/airbnb/listings/{id}/checkin-guide".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | UpdateAirbnbCheckinGuideResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateAirbnbCheckinGuideResponse200.from_dict(response.json())



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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | UpdateAirbnbCheckinGuideResponse200]:
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
    body: UpdateAirbnbCheckinGuideBody,

) -> Response[Error | UpdateAirbnbCheckinGuideResponse200]:
    r""" Replace the steps of an Airbnb check-in guide

     Write the check-in guide guests see before arrival: an ordered list of text steps. **Replaces**
    every existing step, so send the whole guide; `{\"steps\": []}` removes them all. The response is
    the guide re-read from Airbnb after the write.

    If the listing has no guide yet, one is created in `locale` (default: the existing guide's, else
    `en`).

    Safe on failure: the new steps are created before the old ones are removed, and if a create fails
    the steps this call added are removed again, so the guide is never left emptier than it was.

    Text steps only. Steps with photos need Airbnb's media upload and are not supported here yet. For
    the other arrival details use `PUT /v1/channels/airbnb/listings/{id}/details`:
    `check_in_option.instruction` (arrival instructions), `house_manual`, `directions`, `wifi_network`,
    `wifi_password`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UpdateAirbnbCheckinGuideBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbCheckinGuideResponse200]
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
    body: UpdateAirbnbCheckinGuideBody,

) -> Error | UpdateAirbnbCheckinGuideResponse200 | None:
    r""" Replace the steps of an Airbnb check-in guide

     Write the check-in guide guests see before arrival: an ordered list of text steps. **Replaces**
    every existing step, so send the whole guide; `{\"steps\": []}` removes them all. The response is
    the guide re-read from Airbnb after the write.

    If the listing has no guide yet, one is created in `locale` (default: the existing guide's, else
    `en`).

    Safe on failure: the new steps are created before the old ones are removed, and if a create fails
    the steps this call added are removed again, so the guide is never left emptier than it was.

    Text steps only. Steps with photos need Airbnb's media upload and are not supported here yet. For
    the other arrival details use `PUT /v1/channels/airbnb/listings/{id}/details`:
    `check_in_option.instruction` (arrival instructions), `house_manual`, `directions`, `wifi_network`,
    `wifi_password`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UpdateAirbnbCheckinGuideBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbCheckinGuideResponse200
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
    body: UpdateAirbnbCheckinGuideBody,

) -> Response[Error | UpdateAirbnbCheckinGuideResponse200]:
    r""" Replace the steps of an Airbnb check-in guide

     Write the check-in guide guests see before arrival: an ordered list of text steps. **Replaces**
    every existing step, so send the whole guide; `{\"steps\": []}` removes them all. The response is
    the guide re-read from Airbnb after the write.

    If the listing has no guide yet, one is created in `locale` (default: the existing guide's, else
    `en`).

    Safe on failure: the new steps are created before the old ones are removed, and if a create fails
    the steps this call added are removed again, so the guide is never left emptier than it was.

    Text steps only. Steps with photos need Airbnb's media upload and are not supported here yet. For
    the other arrival details use `PUT /v1/channels/airbnb/listings/{id}/details`:
    `check_in_option.instruction` (arrival instructions), `house_manual`, `directions`, `wifi_network`,
    `wifi_password`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UpdateAirbnbCheckinGuideBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbCheckinGuideResponse200]
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
    body: UpdateAirbnbCheckinGuideBody,

) -> Error | UpdateAirbnbCheckinGuideResponse200 | None:
    r""" Replace the steps of an Airbnb check-in guide

     Write the check-in guide guests see before arrival: an ordered list of text steps. **Replaces**
    every existing step, so send the whole guide; `{\"steps\": []}` removes them all. The response is
    the guide re-read from Airbnb after the write.

    If the listing has no guide yet, one is created in `locale` (default: the existing guide's, else
    `en`).

    Safe on failure: the new steps are created before the old ones are removed, and if a create fails
    the steps this call added are removed again, so the guide is never left emptier than it was.

    Text steps only. Steps with photos need Airbnb's media upload and are not supported here yet. For
    the other arrival details use `PUT /v1/channels/airbnb/listings/{id}/details`:
    `check_in_option.instruction` (arrival instructions), `house_manual`, `directions`, `wifi_network`,
    `wifi_password`.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (UpdateAirbnbCheckinGuideBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbCheckinGuideResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
