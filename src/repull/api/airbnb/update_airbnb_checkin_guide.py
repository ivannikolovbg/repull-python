from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    locale: str | Unset = 'en',

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["locale"] = locale


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/airbnb/listings/{id}/checkin-guide".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

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
    locale: str | Unset = 'en',

) -> Response[Any | Error]:
    """ Upsert Airbnb check-in guide

     Upsert the check-in guide for one locale on an Airbnb listing. **Write-side** — calls Airbnb
    upstream; the DB mirror is reconciled by the sync worker once the upstream call returns. Target the
    locale with `?locale=en` (defaults to `en`). Requires a connected Airbnb host, else `404
    no_connection`.

    Args:
        id (str):
        locale (str | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    locale: str | Unset = 'en',

) -> Any | Error | None:
    """ Upsert Airbnb check-in guide

     Upsert the check-in guide for one locale on an Airbnb listing. **Write-side** — calls Airbnb
    upstream; the DB mirror is reconciled by the sync worker once the upstream call returns. Target the
    locale with `?locale=en` (defaults to `en`). Requires a connected Airbnb host, else `404
    no_connection`.

    Args:
        id (str):
        locale (str | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
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
    locale: str | Unset = 'en',

) -> Response[Any | Error]:
    """ Upsert Airbnb check-in guide

     Upsert the check-in guide for one locale on an Airbnb listing. **Write-side** — calls Airbnb
    upstream; the DB mirror is reconciled by the sync worker once the upstream call returns. Target the
    locale with `?locale=en` (defaults to `en`). Requires a connected Airbnb host, else `404
    no_connection`.

    Args:
        id (str):
        locale (str | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
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
    locale: str | Unset = 'en',

) -> Any | Error | None:
    """ Upsert Airbnb check-in guide

     Upsert the check-in guide for one locale on an Airbnb listing. **Write-side** — calls Airbnb
    upstream; the DB mirror is reconciled by the sync worker once the upstream call returns. Target the
    locale with `?locale=en` (defaults to `en`). Requires a connected Airbnb host, else `404
    no_connection`.

    Args:
        id (str):
        locale (str | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
locale=locale,

    )).parsed
