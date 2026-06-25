from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_properties_channel import ListPropertiesChannel
from ...models.list_properties_status import ListPropertiesStatus
from ...models.property_list_response import PropertyListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    q: str | Unset = UNSET,
    status: ListPropertiesStatus | Unset = ListPropertiesStatus.ACTIVE,
    lifecycle_status: str | Unset = UNSET,
    channel: ListPropertiesChannel | Unset = UNSET,
    include_total: bool | Unset = True,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["offset"] = offset

    params["q"] = q

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["lifecycle_status"] = lifecycle_status

    json_channel: str | Unset = UNSET
    if not isinstance(channel, Unset):
        json_channel = channel.value

    params["channel"] = json_channel

    params["include_total"] = include_total


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/properties",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PropertyListResponse | None:
    if response.status_code == 200:
        response_200 = PropertyListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PropertyListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    q: str | Unset = UNSET,
    status: ListPropertiesStatus | Unset = ListPropertiesStatus.ACTIVE,
    lifecycle_status: str | Unset = UNSET,
    channel: ListPropertiesChannel | Unset = UNSET,
    include_total: bool | Unset = True,

) -> Response[Error | PropertyListResponse]:
    """ List properties

     Cursor-paginated list of properties for the authenticated workspace. Walk pages with
    `?cursor=<pagination.nextCursor>`; stop when `pagination.hasMore` is `false`. Cursor is opaque
    base64 — do not parse it.

    `?offset=` is also accepted as a first-class alias for shallow paging (0..10000) — see the `offset`
    parameter below. Mutually exclusive with `cursor`.

    Filters: `q` (substring on name/street/city), `status` (active|inactive|all), `lifecycle_status`
    (exact match on the listing's lifecycle state). Other unknown params (e.g. `?search=` or
    `?propertyId=`) are rejected with 422 — no silent unfiltered results.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        q (str | Unset):
        status (ListPropertiesStatus | Unset):  Default: ListPropertiesStatus.ACTIVE.
        lifecycle_status (str | Unset):  Example: live.
        channel (ListPropertiesChannel | Unset):  Example: airbnb.
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PropertyListResponse]
     """


    kwargs = _get_kwargs(
        limit=limit,
cursor=cursor,
offset=offset,
q=q,
status=status,
lifecycle_status=lifecycle_status,
channel=channel,
include_total=include_total,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    q: str | Unset = UNSET,
    status: ListPropertiesStatus | Unset = ListPropertiesStatus.ACTIVE,
    lifecycle_status: str | Unset = UNSET,
    channel: ListPropertiesChannel | Unset = UNSET,
    include_total: bool | Unset = True,

) -> Error | PropertyListResponse | None:
    """ List properties

     Cursor-paginated list of properties for the authenticated workspace. Walk pages with
    `?cursor=<pagination.nextCursor>`; stop when `pagination.hasMore` is `false`. Cursor is opaque
    base64 — do not parse it.

    `?offset=` is also accepted as a first-class alias for shallow paging (0..10000) — see the `offset`
    parameter below. Mutually exclusive with `cursor`.

    Filters: `q` (substring on name/street/city), `status` (active|inactive|all), `lifecycle_status`
    (exact match on the listing's lifecycle state). Other unknown params (e.g. `?search=` or
    `?propertyId=`) are rejected with 422 — no silent unfiltered results.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        q (str | Unset):
        status (ListPropertiesStatus | Unset):  Default: ListPropertiesStatus.ACTIVE.
        lifecycle_status (str | Unset):  Example: live.
        channel (ListPropertiesChannel | Unset):  Example: airbnb.
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PropertyListResponse
     """


    return sync_detailed(
        client=client,
limit=limit,
cursor=cursor,
offset=offset,
q=q,
status=status,
lifecycle_status=lifecycle_status,
channel=channel,
include_total=include_total,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    q: str | Unset = UNSET,
    status: ListPropertiesStatus | Unset = ListPropertiesStatus.ACTIVE,
    lifecycle_status: str | Unset = UNSET,
    channel: ListPropertiesChannel | Unset = UNSET,
    include_total: bool | Unset = True,

) -> Response[Error | PropertyListResponse]:
    """ List properties

     Cursor-paginated list of properties for the authenticated workspace. Walk pages with
    `?cursor=<pagination.nextCursor>`; stop when `pagination.hasMore` is `false`. Cursor is opaque
    base64 — do not parse it.

    `?offset=` is also accepted as a first-class alias for shallow paging (0..10000) — see the `offset`
    parameter below. Mutually exclusive with `cursor`.

    Filters: `q` (substring on name/street/city), `status` (active|inactive|all), `lifecycle_status`
    (exact match on the listing's lifecycle state). Other unknown params (e.g. `?search=` or
    `?propertyId=`) are rejected with 422 — no silent unfiltered results.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        q (str | Unset):
        status (ListPropertiesStatus | Unset):  Default: ListPropertiesStatus.ACTIVE.
        lifecycle_status (str | Unset):  Example: live.
        channel (ListPropertiesChannel | Unset):  Example: airbnb.
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PropertyListResponse]
     """


    kwargs = _get_kwargs(
        limit=limit,
cursor=cursor,
offset=offset,
q=q,
status=status,
lifecycle_status=lifecycle_status,
channel=channel,
include_total=include_total,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 50,
    cursor: str | Unset = UNSET,
    offset: int | Unset = 0,
    q: str | Unset = UNSET,
    status: ListPropertiesStatus | Unset = ListPropertiesStatus.ACTIVE,
    lifecycle_status: str | Unset = UNSET,
    channel: ListPropertiesChannel | Unset = UNSET,
    include_total: bool | Unset = True,

) -> Error | PropertyListResponse | None:
    """ List properties

     Cursor-paginated list of properties for the authenticated workspace. Walk pages with
    `?cursor=<pagination.nextCursor>`; stop when `pagination.hasMore` is `false`. Cursor is opaque
    base64 — do not parse it.

    `?offset=` is also accepted as a first-class alias for shallow paging (0..10000) — see the `offset`
    parameter below. Mutually exclusive with `cursor`.

    Filters: `q` (substring on name/street/city), `status` (active|inactive|all), `lifecycle_status`
    (exact match on the listing's lifecycle state). Other unknown params (e.g. `?search=` or
    `?propertyId=`) are rejected with 422 — no silent unfiltered results.

    Args:
        limit (int | Unset):  Default: 50.
        cursor (str | Unset):
        offset (int | Unset):  Default: 0.
        q (str | Unset):
        status (ListPropertiesStatus | Unset):  Default: ListPropertiesStatus.ACTIVE.
        lifecycle_status (str | Unset):  Example: live.
        channel (ListPropertiesChannel | Unset):  Example: airbnb.
        include_total (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PropertyListResponse
     """


    return (await asyncio_detailed(
        client=client,
limit=limit,
cursor=cursor,
offset=offset,
q=q,
status=status,
lifecycle_status=lifecycle_status,
channel=channel,
include_total=include_total,

    )).parsed
