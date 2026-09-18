from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_airbnb_listing_permits_response_200 import ListAirbnbListingPermitsResponse200
from ...models.list_airbnb_listing_permits_source import ListAirbnbListingPermitsSource
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    source: ListAirbnbListingPermitsSource | Unset = ListAirbnbListingPermitsSource.CACHE,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_source: str | Unset = UNSET
    if not isinstance(source, Unset):
        json_source = source.value

    params["source"] = json_source


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/listings/{id}/permits".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListAirbnbListingPermitsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAirbnbListingPermitsResponse200.from_dict(response.json())



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

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListAirbnbListingPermitsResponse200]:
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
    source: ListAirbnbListingPermitsSource | Unset = ListAirbnbListingPermitsSource.CACHE,

) -> Response[Error | ListAirbnbListingPermitsResponse200]:
    """ List Airbnb permits and licences

     The regulatory permits, licences and registration numbers attached to an Airbnb listing.

    **DB-only by default.** `?source=cache` (the default) returns the permits as last mirrored by the
    sync worker — regulatory body, regulation type, status, permit number — with no upstream call.

    **`?source=live` also returns the QUESTIONS.** The mirror stores the RESULT of a permit, not what
    Airbnb asks for it, so a caller that is about to write needs `?source=live` once: it returns each
    permit flow with the `question_key`, `answer_type` and `options` of every question, and the answers
    already on file. Airbnb refuses a `question_key` it did not ask for on this listing, so this is not
    optional guesswork you can skip.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        source (ListAirbnbListingPermitsSource | Unset):  Default:
            ListAirbnbListingPermitsSource.CACHE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbListingPermitsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
source=source,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    source: ListAirbnbListingPermitsSource | Unset = ListAirbnbListingPermitsSource.CACHE,

) -> Error | ListAirbnbListingPermitsResponse200 | None:
    """ List Airbnb permits and licences

     The regulatory permits, licences and registration numbers attached to an Airbnb listing.

    **DB-only by default.** `?source=cache` (the default) returns the permits as last mirrored by the
    sync worker — regulatory body, regulation type, status, permit number — with no upstream call.

    **`?source=live` also returns the QUESTIONS.** The mirror stores the RESULT of a permit, not what
    Airbnb asks for it, so a caller that is about to write needs `?source=live` once: it returns each
    permit flow with the `question_key`, `answer_type` and `options` of every question, and the answers
    already on file. Airbnb refuses a `question_key` it did not ask for on this listing, so this is not
    optional guesswork you can skip.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        source (ListAirbnbListingPermitsSource | Unset):  Default:
            ListAirbnbListingPermitsSource.CACHE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbListingPermitsResponse200
     """


    return sync_detailed(
        id=id,
client=client,
source=source,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    source: ListAirbnbListingPermitsSource | Unset = ListAirbnbListingPermitsSource.CACHE,

) -> Response[Error | ListAirbnbListingPermitsResponse200]:
    """ List Airbnb permits and licences

     The regulatory permits, licences and registration numbers attached to an Airbnb listing.

    **DB-only by default.** `?source=cache` (the default) returns the permits as last mirrored by the
    sync worker — regulatory body, regulation type, status, permit number — with no upstream call.

    **`?source=live` also returns the QUESTIONS.** The mirror stores the RESULT of a permit, not what
    Airbnb asks for it, so a caller that is about to write needs `?source=live` once: it returns each
    permit flow with the `question_key`, `answer_type` and `options` of every question, and the answers
    already on file. Airbnb refuses a `question_key` it did not ask for on this listing, so this is not
    optional guesswork you can skip.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        source (ListAirbnbListingPermitsSource | Unset):  Default:
            ListAirbnbListingPermitsSource.CACHE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbListingPermitsResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
source=source,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    source: ListAirbnbListingPermitsSource | Unset = ListAirbnbListingPermitsSource.CACHE,

) -> Error | ListAirbnbListingPermitsResponse200 | None:
    """ List Airbnb permits and licences

     The regulatory permits, licences and registration numbers attached to an Airbnb listing.

    **DB-only by default.** `?source=cache` (the default) returns the permits as last mirrored by the
    sync worker — regulatory body, regulation type, status, permit number — with no upstream call.

    **`?source=live` also returns the QUESTIONS.** The mirror stores the RESULT of a permit, not what
    Airbnb asks for it, so a caller that is about to write needs `?source=live` once: it returns each
    permit flow with the `question_key`, `answer_type` and `options` of every question, and the answers
    already on file. Airbnb refuses a `question_key` it did not ask for on this listing, so this is not
    optional guesswork you can skip.

    Returns `404` when the listing has no Airbnb connection in this workspace, and `403
    listing_inactive` when the listing is inactive.

    Args:
        id (str):
        source (ListAirbnbListingPermitsSource | Unset):  Default:
            ListAirbnbListingPermitsSource.CACHE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbListingPermitsResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
source=source,

    )).parsed
