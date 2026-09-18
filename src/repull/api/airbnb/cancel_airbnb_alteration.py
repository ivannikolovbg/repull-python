from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.cancel_airbnb_alteration_body import CancelAirbnbAlterationBody
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: CancelAirbnbAlterationBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/airbnb/alterations/{id}/cancel".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
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
    body: CancelAirbnbAlterationBody | Unset = UNSET,

) -> Response[Any | Error]:
    """ Cancel Airbnb alteration

     Withdraw an alteration you proposed, before the other side has answered it. **Write-side** — calls
    Airbnb upstream (`respondToAlteration` with status `canceled`). Use this when you sent the wrong
    dates, guest count, price or listing: the alteration stops being pending instead of sitting there
    until the guest acts on it.

    This is the third of Airbnb's three answers to a pending alteration, alongside `accept` and
    `decline`, and behaves identically to them: requires a connected Airbnb host for the workspace (else
    `404 no_connection`) and that the alteration id belongs to a reservation in your workspace (else
    `404 not_found`). No request body is required.

    Airbnb decides whether an alteration can still be withdrawn — one that has already been accepted or
    declined is refused upstream, and Airbnb's own reason comes back in `message`.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (CancelAirbnbAlterationBody | Unset): No fields required. An empty body is accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    body: CancelAirbnbAlterationBody | Unset = UNSET,

) -> Any | Error | None:
    """ Cancel Airbnb alteration

     Withdraw an alteration you proposed, before the other side has answered it. **Write-side** — calls
    Airbnb upstream (`respondToAlteration` with status `canceled`). Use this when you sent the wrong
    dates, guest count, price or listing: the alteration stops being pending instead of sitting there
    until the guest acts on it.

    This is the third of Airbnb's three answers to a pending alteration, alongside `accept` and
    `decline`, and behaves identically to them: requires a connected Airbnb host for the workspace (else
    `404 no_connection`) and that the alteration id belongs to a reservation in your workspace (else
    `404 not_found`). No request body is required.

    Airbnb decides whether an alteration can still be withdrawn — one that has already been accepted or
    declined is refused upstream, and Airbnb's own reason comes back in `message`.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (CancelAirbnbAlterationBody | Unset): No fields required. An empty body is accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
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
    body: CancelAirbnbAlterationBody | Unset = UNSET,

) -> Response[Any | Error]:
    """ Cancel Airbnb alteration

     Withdraw an alteration you proposed, before the other side has answered it. **Write-side** — calls
    Airbnb upstream (`respondToAlteration` with status `canceled`). Use this when you sent the wrong
    dates, guest count, price or listing: the alteration stops being pending instead of sitting there
    until the guest acts on it.

    This is the third of Airbnb's three answers to a pending alteration, alongside `accept` and
    `decline`, and behaves identically to them: requires a connected Airbnb host for the workspace (else
    `404 no_connection`) and that the alteration id belongs to a reservation in your workspace (else
    `404 not_found`). No request body is required.

    Airbnb decides whether an alteration can still be withdrawn — one that has already been accepted or
    declined is refused upstream, and Airbnb's own reason comes back in `message`.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (CancelAirbnbAlterationBody | Unset): No fields required. An empty body is accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    body: CancelAirbnbAlterationBody | Unset = UNSET,

) -> Any | Error | None:
    """ Cancel Airbnb alteration

     Withdraw an alteration you proposed, before the other side has answered it. **Write-side** — calls
    Airbnb upstream (`respondToAlteration` with status `canceled`). Use this when you sent the wrong
    dates, guest count, price or listing: the alteration stops being pending instead of sitting there
    until the guest acts on it.

    This is the third of Airbnb's three answers to a pending alteration, alongside `accept` and
    `decline`, and behaves identically to them: requires a connected Airbnb host for the workspace (else
    `404 no_connection`) and that the alteration id belongs to a reservation in your workspace (else
    `404 not_found`). No request body is required.

    Airbnb decides whether an alteration can still be withdrawn — one that has already been accepted or
    declined is refused upstream, and Airbnb's own reason comes back in `message`.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (CancelAirbnbAlterationBody | Unset): No fields required. An empty body is accepted.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
