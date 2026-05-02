from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_listings_status import ListListingsStatus
from ...models.listing_list_response import ListingListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    q: str | Unset = UNSET,
    status: ListListingsStatus | Unset = UNSET,
    channel: str | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_schema, Unset):
        headers["X-Schema"] = x_schema



    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params["q"] = q

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["channel"] = channel


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/listings",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListingListResponse | None:
    if response.status_code == 200:
        response_200 = ListingListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListingListResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    q: str | Unset = UNSET,
    status: ListListingsStatus | Unset = UNSET,
    channel: str | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Response[Error | ListingListResponse]:
    """ List listings

     Cursor-paginated list of listings owned by the authenticated workspace. Use `pagination.next_cursor`
    from one response as the `cursor` query param of the next request to walk the full set. Filters: `q`
    (substring on name/street/city), `status`, `channel`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        q (str | Unset):
        status (ListListingsStatus | Unset):
        channel (str | Unset):  Example: airbnb.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingListResponse]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
limit=limit,
q=q,
status=status,
channel=channel,
x_schema=x_schema,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    q: str | Unset = UNSET,
    status: ListListingsStatus | Unset = UNSET,
    channel: str | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Error | ListingListResponse | None:
    """ List listings

     Cursor-paginated list of listings owned by the authenticated workspace. Use `pagination.next_cursor`
    from one response as the `cursor` query param of the next request to walk the full set. Filters: `q`
    (substring on name/street/city), `status`, `channel`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        q (str | Unset):
        status (ListListingsStatus | Unset):
        channel (str | Unset):  Example: airbnb.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingListResponse
     """


    return sync_detailed(
        client=client,
cursor=cursor,
limit=limit,
q=q,
status=status,
channel=channel,
x_schema=x_schema,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    q: str | Unset = UNSET,
    status: ListListingsStatus | Unset = UNSET,
    channel: str | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Response[Error | ListingListResponse]:
    """ List listings

     Cursor-paginated list of listings owned by the authenticated workspace. Use `pagination.next_cursor`
    from one response as the `cursor` query param of the next request to walk the full set. Filters: `q`
    (substring on name/street/city), `status`, `channel`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        q (str | Unset):
        status (ListListingsStatus | Unset):
        channel (str | Unset):  Example: airbnb.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingListResponse]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
limit=limit,
q=q,
status=status,
channel=channel,
x_schema=x_schema,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    q: str | Unset = UNSET,
    status: ListListingsStatus | Unset = UNSET,
    channel: str | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Error | ListingListResponse | None:
    """ List listings

     Cursor-paginated list of listings owned by the authenticated workspace. Use `pagination.next_cursor`
    from one response as the `cursor` query param of the next request to walk the full set. Filters: `q`
    (substring on name/street/city), `status`, `channel`.

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        q (str | Unset):
        status (ListListingsStatus | Unset):
        channel (str | Unset):  Example: airbnb.
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingListResponse
     """


    return (await asyncio_detailed(
        client=client,
cursor=cursor,
limit=limit,
q=q,
status=status,
channel=channel,
x_schema=x_schema,

    )).parsed
