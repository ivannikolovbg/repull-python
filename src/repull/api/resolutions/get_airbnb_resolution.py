from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.resolution import Resolution
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    x_schema: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_schema, Unset):
        headers["X-Schema"] = x_schema



    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/resolutions/{id}".format(id=quote(str(id), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | Resolution | None:
    if response.status_code == 200:
        response_200 = Resolution.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | Resolution]:
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
    x_schema: str | Unset = UNSET,

) -> Response[Error | Resolution]:
    """ Get an Airbnb Resolution Center case

     One Airbnb Resolution Center case. `{id}` is the Airbnb resolution id (the `resolutionId` from the
    list, also a transaction's `reference`). Read-only (see the list endpoint). The amounts moved are in
    the transactions ledger — join `resolutionId` to a transaction's `reference`. 404 when it isn't in
    this workspace (POST the list endpoint to refresh first).

    Args:
        id (str):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Resolution]
     """


    kwargs = _get_kwargs(
        id=id,
x_schema=x_schema,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    x_schema: str | Unset = UNSET,

) -> Error | Resolution | None:
    """ Get an Airbnb Resolution Center case

     One Airbnb Resolution Center case. `{id}` is the Airbnb resolution id (the `resolutionId` from the
    list, also a transaction's `reference`). Read-only (see the list endpoint). The amounts moved are in
    the transactions ledger — join `resolutionId` to a transaction's `reference`. 404 when it isn't in
    this workspace (POST the list endpoint to refresh first).

    Args:
        id (str):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Resolution
     """


    return sync_detailed(
        id=id,
client=client,
x_schema=x_schema,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    x_schema: str | Unset = UNSET,

) -> Response[Error | Resolution]:
    """ Get an Airbnb Resolution Center case

     One Airbnb Resolution Center case. `{id}` is the Airbnb resolution id (the `resolutionId` from the
    list, also a transaction's `reference`). Read-only (see the list endpoint). The amounts moved are in
    the transactions ledger — join `resolutionId` to a transaction's `reference`. 404 when it isn't in
    this workspace (POST the list endpoint to refresh first).

    Args:
        id (str):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | Resolution]
     """


    kwargs = _get_kwargs(
        id=id,
x_schema=x_schema,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    x_schema: str | Unset = UNSET,

) -> Error | Resolution | None:
    """ Get an Airbnb Resolution Center case

     One Airbnb Resolution Center case. `{id}` is the Airbnb resolution id (the `resolutionId` from the
    list, also a transaction's `reference`). Read-only (see the list endpoint). The amounts moved are in
    the transactions ledger — join `resolutionId` to a transaction's `reference`. 404 when it isn't in
    this workspace (POST the list endpoint to refresh first).

    Args:
        id (str):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | Resolution
     """


    return (await asyncio_detailed(
        id=id,
client=client,
x_schema=x_schema,

    )).parsed
