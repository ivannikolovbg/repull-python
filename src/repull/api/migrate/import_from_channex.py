from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.import_from_channex_body import ImportFromChannexBody
from ...models.import_from_channex_response_200 import ImportFromChannexResponse200
from ...models.import_from_channex_response_201 import ImportFromChannexResponse201
from typing import cast



def _get_kwargs(
    *,
    body: ImportFromChannexBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/migrations/channex",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ImportFromChannexResponse200 | ImportFromChannexResponse201 | None:
    if response.status_code == 200:
        response_200 = ImportFromChannexResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 201:
        response_201 = ImportFromChannexResponse201.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ImportFromChannexResponse200 | ImportFromChannexResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ImportFromChannexBody,

) -> Response[Error | ImportFromChannexResponse200 | ImportFromChannexResponse201]:
    """ Import from Channex

     Move a workspace off Channex without changing a single id on your side. Pass your Channex API key:
    Repull reads your Channex properties, room types, rate plans, webhooks, signing keys, channels and
    upcoming bookings through Channex's own API (read-only — nothing is written to Channex, and the key
    is not stored). Each Channex property is matched to your Repull listing or hotel (by Booking.com
    hotel/room and Airbnb/Vrbo listing ids, then by title and address) or created; every Channex id then
    resolves, and is returned, unchanged on the Channex-compatible API at `/channex/api/v1`. Webhooks
    are recreated inactive; activate them with `POST /channex/api/v1/migration/cutover`. Safe to re-run:
    a run that hits its time budget returns `complete: false` and the next run continues.

    Args:
        body (ImportFromChannexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ImportFromChannexResponse200 | ImportFromChannexResponse201]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ImportFromChannexBody,

) -> Error | ImportFromChannexResponse200 | ImportFromChannexResponse201 | None:
    """ Import from Channex

     Move a workspace off Channex without changing a single id on your side. Pass your Channex API key:
    Repull reads your Channex properties, room types, rate plans, webhooks, signing keys, channels and
    upcoming bookings through Channex's own API (read-only — nothing is written to Channex, and the key
    is not stored). Each Channex property is matched to your Repull listing or hotel (by Booking.com
    hotel/room and Airbnb/Vrbo listing ids, then by title and address) or created; every Channex id then
    resolves, and is returned, unchanged on the Channex-compatible API at `/channex/api/v1`. Webhooks
    are recreated inactive; activate them with `POST /channex/api/v1/migration/cutover`. Safe to re-run:
    a run that hits its time budget returns `complete: false` and the next run continues.

    Args:
        body (ImportFromChannexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ImportFromChannexResponse200 | ImportFromChannexResponse201
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ImportFromChannexBody,

) -> Response[Error | ImportFromChannexResponse200 | ImportFromChannexResponse201]:
    """ Import from Channex

     Move a workspace off Channex without changing a single id on your side. Pass your Channex API key:
    Repull reads your Channex properties, room types, rate plans, webhooks, signing keys, channels and
    upcoming bookings through Channex's own API (read-only — nothing is written to Channex, and the key
    is not stored). Each Channex property is matched to your Repull listing or hotel (by Booking.com
    hotel/room and Airbnb/Vrbo listing ids, then by title and address) or created; every Channex id then
    resolves, and is returned, unchanged on the Channex-compatible API at `/channex/api/v1`. Webhooks
    are recreated inactive; activate them with `POST /channex/api/v1/migration/cutover`. Safe to re-run:
    a run that hits its time budget returns `complete: false` and the next run continues.

    Args:
        body (ImportFromChannexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ImportFromChannexResponse200 | ImportFromChannexResponse201]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ImportFromChannexBody,

) -> Error | ImportFromChannexResponse200 | ImportFromChannexResponse201 | None:
    """ Import from Channex

     Move a workspace off Channex without changing a single id on your side. Pass your Channex API key:
    Repull reads your Channex properties, room types, rate plans, webhooks, signing keys, channels and
    upcoming bookings through Channex's own API (read-only — nothing is written to Channex, and the key
    is not stored). Each Channex property is matched to your Repull listing or hotel (by Booking.com
    hotel/room and Airbnb/Vrbo listing ids, then by title and address) or created; every Channex id then
    resolves, and is returned, unchanged on the Channex-compatible API at `/channex/api/v1`. Webhooks
    are recreated inactive; activate them with `POST /channex/api/v1/migration/cutover`. Safe to re-run:
    a run that hits its time budget returns `complete: false` and the next run continues.

    Args:
        body (ImportFromChannexBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ImportFromChannexResponse200 | ImportFromChannexResponse201
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
