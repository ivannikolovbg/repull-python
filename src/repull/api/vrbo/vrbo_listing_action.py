from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.vrbo_listing_action_body import VrboListingActionBody
from ...models.vrbo_listing_action_response_200 import VrboListingActionResponse200
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: VrboListingActionBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/vrbo/listings/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | VrboListingActionResponse200 | None:
    if response.status_code == 200:
        response_200 = VrboListingActionResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 202:
        response_202 = cast(Any, None)
        return response_202

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error | VrboListingActionResponse200]:
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
    body: VrboListingActionBody,

) -> Response[Any | Error | VrboListingActionResponse200]:
    r""" Act on the Vrbo listing

     Airbnb's listing actions, on Vrbo:

    - `push` / `publish` — push the listing's content onto its Vrbo listing: the same job as `POST
    /v1/listings/{id}/publish/vrbo` (`202`, poll `GET /v1/listings/{id}/publish/vrbo?jobId=`). Optional
    `sections` and `vrboListingNumber`.
    - `unlist` — Vrbo's \"Hide listing\": out of Vrbo search, no new bookings. Read back from Vrbo
    before answering.
    - `relist` — Vrbo's \"Reactivate\".
    - `delete` — deactivate the Repull record (local; the Vrbo listing is not touched — use `unlist` for
    that).

    `unlist` / `relist` act on every Vrbo unit of the listing, or the one named with
    `vrboListingNumber`. Needs full access. See https://repull.dev/docs/channels/vrbo/listing-content.

    Args:
        id (str):
        body (VrboListingActionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | VrboListingActionResponse200]
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
    body: VrboListingActionBody,

) -> Any | Error | VrboListingActionResponse200 | None:
    r""" Act on the Vrbo listing

     Airbnb's listing actions, on Vrbo:

    - `push` / `publish` — push the listing's content onto its Vrbo listing: the same job as `POST
    /v1/listings/{id}/publish/vrbo` (`202`, poll `GET /v1/listings/{id}/publish/vrbo?jobId=`). Optional
    `sections` and `vrboListingNumber`.
    - `unlist` — Vrbo's \"Hide listing\": out of Vrbo search, no new bookings. Read back from Vrbo
    before answering.
    - `relist` — Vrbo's \"Reactivate\".
    - `delete` — deactivate the Repull record (local; the Vrbo listing is not touched — use `unlist` for
    that).

    `unlist` / `relist` act on every Vrbo unit of the listing, or the one named with
    `vrboListingNumber`. Needs full access. See https://repull.dev/docs/channels/vrbo/listing-content.

    Args:
        id (str):
        body (VrboListingActionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | VrboListingActionResponse200
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
    body: VrboListingActionBody,

) -> Response[Any | Error | VrboListingActionResponse200]:
    r""" Act on the Vrbo listing

     Airbnb's listing actions, on Vrbo:

    - `push` / `publish` — push the listing's content onto its Vrbo listing: the same job as `POST
    /v1/listings/{id}/publish/vrbo` (`202`, poll `GET /v1/listings/{id}/publish/vrbo?jobId=`). Optional
    `sections` and `vrboListingNumber`.
    - `unlist` — Vrbo's \"Hide listing\": out of Vrbo search, no new bookings. Read back from Vrbo
    before answering.
    - `relist` — Vrbo's \"Reactivate\".
    - `delete` — deactivate the Repull record (local; the Vrbo listing is not touched — use `unlist` for
    that).

    `unlist` / `relist` act on every Vrbo unit of the listing, or the one named with
    `vrboListingNumber`. Needs full access. See https://repull.dev/docs/channels/vrbo/listing-content.

    Args:
        id (str):
        body (VrboListingActionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | VrboListingActionResponse200]
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
    body: VrboListingActionBody,

) -> Any | Error | VrboListingActionResponse200 | None:
    r""" Act on the Vrbo listing

     Airbnb's listing actions, on Vrbo:

    - `push` / `publish` — push the listing's content onto its Vrbo listing: the same job as `POST
    /v1/listings/{id}/publish/vrbo` (`202`, poll `GET /v1/listings/{id}/publish/vrbo?jobId=`). Optional
    `sections` and `vrboListingNumber`.
    - `unlist` — Vrbo's \"Hide listing\": out of Vrbo search, no new bookings. Read back from Vrbo
    before answering.
    - `relist` — Vrbo's \"Reactivate\".
    - `delete` — deactivate the Repull record (local; the Vrbo listing is not touched — use `unlist` for
    that).

    `unlist` / `relist` act on every Vrbo unit of the listing, or the one named with
    `vrboListingNumber`. Needs full access. See https://repull.dev/docs/channels/vrbo/listing-content.

    Args:
        id (str):
        body (VrboListingActionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | VrboListingActionResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
