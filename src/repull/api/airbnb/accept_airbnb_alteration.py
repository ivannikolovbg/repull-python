from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.accept_airbnb_alteration_body import AcceptAirbnbAlterationBody
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: AcceptAirbnbAlterationBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/airbnb/alterations/{id}/accept".format(id=quote(str(id), safe=""),),
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
    body: AcceptAirbnbAlterationBody | Unset = UNSET,

) -> Response[Any | Error]:
    """ Accept Airbnb alteration

     Accept a pending Airbnb reservation alteration. **Write-side** — calls Airbnb upstream
    (`respondToAlteration`) to approve the proposed date / guest-count / price change. Requires a
    connected Airbnb host for the workspace (else `404 no_connection`) and that the alteration id
    belongs to a reservation in your workspace (else `404 not_found`). No request body is required.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (AcceptAirbnbAlterationBody | Unset): No fields required. An empty body is accepted.

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
    body: AcceptAirbnbAlterationBody | Unset = UNSET,

) -> Any | Error | None:
    """ Accept Airbnb alteration

     Accept a pending Airbnb reservation alteration. **Write-side** — calls Airbnb upstream
    (`respondToAlteration`) to approve the proposed date / guest-count / price change. Requires a
    connected Airbnb host for the workspace (else `404 no_connection`) and that the alteration id
    belongs to a reservation in your workspace (else `404 not_found`). No request body is required.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (AcceptAirbnbAlterationBody | Unset): No fields required. An empty body is accepted.

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
    body: AcceptAirbnbAlterationBody | Unset = UNSET,

) -> Response[Any | Error]:
    """ Accept Airbnb alteration

     Accept a pending Airbnb reservation alteration. **Write-side** — calls Airbnb upstream
    (`respondToAlteration`) to approve the proposed date / guest-count / price change. Requires a
    connected Airbnb host for the workspace (else `404 no_connection`) and that the alteration id
    belongs to a reservation in your workspace (else `404 not_found`). No request body is required.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (AcceptAirbnbAlterationBody | Unset): No fields required. An empty body is accepted.

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
    body: AcceptAirbnbAlterationBody | Unset = UNSET,

) -> Any | Error | None:
    """ Accept Airbnb alteration

     Accept a pending Airbnb reservation alteration. **Write-side** — calls Airbnb upstream
    (`respondToAlteration`) to approve the proposed date / guest-count / price change. Requires a
    connected Airbnb host for the workspace (else `404 no_connection`) and that the alteration id
    belongs to a reservation in your workspace (else `404 not_found`). No request body is required.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Args:
        id (str):
        body (AcceptAirbnbAlterationBody | Unset): No fields required. An empty body is accepted.

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
