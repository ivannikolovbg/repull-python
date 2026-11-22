from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_vrbo_threads_response_200 import ListVrboThreadsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    account_id: str | Unset = UNSET,
    listing_id: str | Unset = UNSET,
    reservation_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["account_id"] = account_id

    params["listing_id"] = listing_id

    params["reservation_id"] = reservation_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/vrbo/messaging",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListVrboThreadsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListVrboThreadsResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListVrboThreadsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
    listing_id: str | Unset = UNSET,
    reservation_id: str | Unset = UNSET,

) -> Response[Error | ListVrboThreadsResponse200]:
    """ List Vrbo message threads

     The workspace's Vrbo conversations, newest activity first (up to 200) — the counterpart of `GET
    /v1/channels/airbnb/messaging`, read from Repull's copy of the Vrbo inbox. Each thread carries the
    Vrbo account it belongs to (`accountId`, `accountName`). `externalThreadId` (`vrbo:<uuid>`)
    addresses the thread on these routes; `id` is the Repull conversation id of
    `/v1/conversations/{id}`.

    Only conversations Vrbo itself holds are listed: a Vrbo booking that reached Repull another way (a
    PMS, iCal) has no Vrbo conversation to message.

    Threads on inactive listings are left out. Filtering by an inactive listing (`listing_id`) returns
    `403 listing_inactive`.

    Args:
        account_id (str | Unset):  Example: vrbo:7001234.
        listing_id (str | Unset):
        reservation_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListVrboThreadsResponse200]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
listing_id=listing_id,
reservation_id=reservation_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
    listing_id: str | Unset = UNSET,
    reservation_id: str | Unset = UNSET,

) -> Error | ListVrboThreadsResponse200 | None:
    """ List Vrbo message threads

     The workspace's Vrbo conversations, newest activity first (up to 200) — the counterpart of `GET
    /v1/channels/airbnb/messaging`, read from Repull's copy of the Vrbo inbox. Each thread carries the
    Vrbo account it belongs to (`accountId`, `accountName`). `externalThreadId` (`vrbo:<uuid>`)
    addresses the thread on these routes; `id` is the Repull conversation id of
    `/v1/conversations/{id}`.

    Only conversations Vrbo itself holds are listed: a Vrbo booking that reached Repull another way (a
    PMS, iCal) has no Vrbo conversation to message.

    Threads on inactive listings are left out. Filtering by an inactive listing (`listing_id`) returns
    `403 listing_inactive`.

    Args:
        account_id (str | Unset):  Example: vrbo:7001234.
        listing_id (str | Unset):
        reservation_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListVrboThreadsResponse200
     """


    return sync_detailed(
        client=client,
account_id=account_id,
listing_id=listing_id,
reservation_id=reservation_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
    listing_id: str | Unset = UNSET,
    reservation_id: str | Unset = UNSET,

) -> Response[Error | ListVrboThreadsResponse200]:
    """ List Vrbo message threads

     The workspace's Vrbo conversations, newest activity first (up to 200) — the counterpart of `GET
    /v1/channels/airbnb/messaging`, read from Repull's copy of the Vrbo inbox. Each thread carries the
    Vrbo account it belongs to (`accountId`, `accountName`). `externalThreadId` (`vrbo:<uuid>`)
    addresses the thread on these routes; `id` is the Repull conversation id of
    `/v1/conversations/{id}`.

    Only conversations Vrbo itself holds are listed: a Vrbo booking that reached Repull another way (a
    PMS, iCal) has no Vrbo conversation to message.

    Threads on inactive listings are left out. Filtering by an inactive listing (`listing_id`) returns
    `403 listing_inactive`.

    Args:
        account_id (str | Unset):  Example: vrbo:7001234.
        listing_id (str | Unset):
        reservation_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListVrboThreadsResponse200]
     """


    kwargs = _get_kwargs(
        account_id=account_id,
listing_id=listing_id,
reservation_id=reservation_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,
    listing_id: str | Unset = UNSET,
    reservation_id: str | Unset = UNSET,

) -> Error | ListVrboThreadsResponse200 | None:
    """ List Vrbo message threads

     The workspace's Vrbo conversations, newest activity first (up to 200) — the counterpart of `GET
    /v1/channels/airbnb/messaging`, read from Repull's copy of the Vrbo inbox. Each thread carries the
    Vrbo account it belongs to (`accountId`, `accountName`). `externalThreadId` (`vrbo:<uuid>`)
    addresses the thread on these routes; `id` is the Repull conversation id of
    `/v1/conversations/{id}`.

    Only conversations Vrbo itself holds are listed: a Vrbo booking that reached Repull another way (a
    PMS, iCal) has no Vrbo conversation to message.

    Threads on inactive listings are left out. Filtering by an inactive listing (`listing_id`) returns
    `403 listing_inactive`.

    Args:
        account_id (str | Unset):  Example: vrbo:7001234.
        listing_id (str | Unset):
        reservation_id (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListVrboThreadsResponse200
     """


    return (await asyncio_detailed(
        client=client,
account_id=account_id,
listing_id=listing_id,
reservation_id=reservation_id,

    )).parsed
