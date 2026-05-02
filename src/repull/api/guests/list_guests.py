from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.guest_list_response import GuestListResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    q: str | Unset = UNSET,
    has_reservation: bool | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_schema, Unset):
        headers["X-Schema"] = x_schema



    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    params["q"] = q

    params["has_reservation"] = has_reservation

    params["listing_id"] = listing_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/guests",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GuestListResponse | None:
    if response.status_code == 200:
        response_200 = GuestListResponse.from_dict(response.json())



        return response_200

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GuestListResponse]:
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
    has_reservation: bool | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Response[Error | GuestListResponse]:
    """ List guests

     Cursor-paginated list of guests in the workspace. Walks `guests.id ASC` keyset for constant per-page
    cost regardless of how many guests the customer has. Use `pagination.next_cursor` from one response
    as the `cursor` query param of the next request.

    Filters: `q` (substring on name/email/phone), `has_reservation` (`true`|`false`), `listing_id`
    (restrict to guests with at least one reservation on that listing).

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        q (str | Unset):
        has_reservation (bool | Unset):
        listing_id (int | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GuestListResponse]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
limit=limit,
q=q,
has_reservation=has_reservation,
listing_id=listing_id,
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
    has_reservation: bool | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Error | GuestListResponse | None:
    """ List guests

     Cursor-paginated list of guests in the workspace. Walks `guests.id ASC` keyset for constant per-page
    cost regardless of how many guests the customer has. Use `pagination.next_cursor` from one response
    as the `cursor` query param of the next request.

    Filters: `q` (substring on name/email/phone), `has_reservation` (`true`|`false`), `listing_id`
    (restrict to guests with at least one reservation on that listing).

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        q (str | Unset):
        has_reservation (bool | Unset):
        listing_id (int | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GuestListResponse
     """


    return sync_detailed(
        client=client,
cursor=cursor,
limit=limit,
q=q,
has_reservation=has_reservation,
listing_id=listing_id,
x_schema=x_schema,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 20,
    q: str | Unset = UNSET,
    has_reservation: bool | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Response[Error | GuestListResponse]:
    """ List guests

     Cursor-paginated list of guests in the workspace. Walks `guests.id ASC` keyset for constant per-page
    cost regardless of how many guests the customer has. Use `pagination.next_cursor` from one response
    as the `cursor` query param of the next request.

    Filters: `q` (substring on name/email/phone), `has_reservation` (`true`|`false`), `listing_id`
    (restrict to guests with at least one reservation on that listing).

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        q (str | Unset):
        has_reservation (bool | Unset):
        listing_id (int | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GuestListResponse]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
limit=limit,
q=q,
has_reservation=has_reservation,
listing_id=listing_id,
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
    has_reservation: bool | Unset = UNSET,
    listing_id: int | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Error | GuestListResponse | None:
    """ List guests

     Cursor-paginated list of guests in the workspace. Walks `guests.id ASC` keyset for constant per-page
    cost regardless of how many guests the customer has. Use `pagination.next_cursor` from one response
    as the `cursor` query param of the next request.

    Filters: `q` (substring on name/email/phone), `has_reservation` (`true`|`false`), `listing_id`
    (restrict to guests with at least one reservation on that listing).

    Args:
        cursor (str | Unset):
        limit (int | Unset):  Default: 20.
        q (str | Unset):
        has_reservation (bool | Unset):
        listing_id (int | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GuestListResponse
     """


    return (await asyncio_detailed(
        client=client,
cursor=cursor,
limit=limit,
q=q,
has_reservation=has_reservation,
listing_id=listing_id,
x_schema=x_schema,

    )).parsed
