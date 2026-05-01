from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_v1_reservations_response_200 import GetV1ReservationsResponse200
from ...models.get_v1_reservations_status import GetV1ReservationsStatus
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    *,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    platform: str | Unset = UNSET,
    status: GetV1ReservationsStatus | Unset = UNSET,
    check_in_from: datetime.date | Unset = UNSET,
    check_in_to: datetime.date | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["platform"] = platform

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_check_in_from: str | Unset = UNSET
    if not isinstance(check_in_from, Unset):
        json_check_in_from = check_in_from.isoformat()
    params["checkInFrom"] = json_check_in_from

    json_check_in_to: str | Unset = UNSET
    if not isinstance(check_in_to, Unset):
        json_check_in_to = check_in_to.isoformat()
    params["checkInTo"] = json_check_in_to


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/reservations",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetV1ReservationsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetV1ReservationsResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GetV1ReservationsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    platform: str | Unset = UNSET,
    status: GetV1ReservationsStatus | Unset = UNSET,
    check_in_from: datetime.date | Unset = UNSET,
    check_in_to: datetime.date | Unset = UNSET,

) -> Response[GetV1ReservationsResponse200]:
    """ List reservations

     Returns reservations across all connected PMS platforms. Filter by platform, status, date range.

    Args:
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.
        platform (str | Unset):
        status (GetV1ReservationsStatus | Unset):
        check_in_from (datetime.date | Unset):
        check_in_to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV1ReservationsResponse200]
     """


    kwargs = _get_kwargs(
        limit=limit,
offset=offset,
platform=platform,
status=status,
check_in_from=check_in_from,
check_in_to=check_in_to,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    platform: str | Unset = UNSET,
    status: GetV1ReservationsStatus | Unset = UNSET,
    check_in_from: datetime.date | Unset = UNSET,
    check_in_to: datetime.date | Unset = UNSET,

) -> GetV1ReservationsResponse200 | None:
    """ List reservations

     Returns reservations across all connected PMS platforms. Filter by platform, status, date range.

    Args:
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.
        platform (str | Unset):
        status (GetV1ReservationsStatus | Unset):
        check_in_from (datetime.date | Unset):
        check_in_to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV1ReservationsResponse200
     """


    return sync_detailed(
        client=client,
limit=limit,
offset=offset,
platform=platform,
status=status,
check_in_from=check_in_from,
check_in_to=check_in_to,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    platform: str | Unset = UNSET,
    status: GetV1ReservationsStatus | Unset = UNSET,
    check_in_from: datetime.date | Unset = UNSET,
    check_in_to: datetime.date | Unset = UNSET,

) -> Response[GetV1ReservationsResponse200]:
    """ List reservations

     Returns reservations across all connected PMS platforms. Filter by platform, status, date range.

    Args:
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.
        platform (str | Unset):
        status (GetV1ReservationsStatus | Unset):
        check_in_from (datetime.date | Unset):
        check_in_to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetV1ReservationsResponse200]
     """


    kwargs = _get_kwargs(
        limit=limit,
offset=offset,
platform=platform,
status=status,
check_in_from=check_in_from,
check_in_to=check_in_to,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    platform: str | Unset = UNSET,
    status: GetV1ReservationsStatus | Unset = UNSET,
    check_in_from: datetime.date | Unset = UNSET,
    check_in_to: datetime.date | Unset = UNSET,

) -> GetV1ReservationsResponse200 | None:
    """ List reservations

     Returns reservations across all connected PMS platforms. Filter by platform, status, date range.

    Args:
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.
        platform (str | Unset):
        status (GetV1ReservationsStatus | Unset):
        check_in_from (datetime.date | Unset):
        check_in_to (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetV1ReservationsResponse200
     """


    return (await asyncio_detailed(
        client=client,
limit=limit,
offset=offset,
platform=platform,
status=status,
check_in_from=check_in_from,
check_in_to=check_in_to,

    )).parsed
