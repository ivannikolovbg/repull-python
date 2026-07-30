from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_airbnb_alterations_response_200 import ListAirbnbAlterationsResponse200
from ...models.list_airbnb_alterations_type import ListAirbnbAlterationsType
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    type_: ListAirbnbAlterationsType | Unset = ListAirbnbAlterationsType.PENDING,
    reservation_code: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["reservation_code"] = reservation_code


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/alterations",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListAirbnbAlterationsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAirbnbAlterationsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListAirbnbAlterationsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: ListAirbnbAlterationsType | Unset = ListAirbnbAlterationsType.PENDING,
    reservation_code: str | Unset = UNSET,

) -> Response[Error | ListAirbnbAlterationsResponse200]:
    """ List Airbnb alterations

     List reservation alteration requests for Airbnb reservations in this workspace. **Pure DB read**
    from the local `reservation_alterations` mirror — never calls Airbnb upstream — scoped to your
    workspace via the reservations join.

    Default returns only pending alterations; pass `?type=all` for the full history. Filter to a single
    reservation with `?reservation_code=<confirmation code>`. Every response carries the
    `data_freshness` envelope.

    Args:
        type_ (ListAirbnbAlterationsType | Unset):  Default: ListAirbnbAlterationsType.PENDING.
        reservation_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbAlterationsResponse200]
     """


    kwargs = _get_kwargs(
        type_=type_,
reservation_code=reservation_code,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    type_: ListAirbnbAlterationsType | Unset = ListAirbnbAlterationsType.PENDING,
    reservation_code: str | Unset = UNSET,

) -> Error | ListAirbnbAlterationsResponse200 | None:
    """ List Airbnb alterations

     List reservation alteration requests for Airbnb reservations in this workspace. **Pure DB read**
    from the local `reservation_alterations` mirror — never calls Airbnb upstream — scoped to your
    workspace via the reservations join.

    Default returns only pending alterations; pass `?type=all` for the full history. Filter to a single
    reservation with `?reservation_code=<confirmation code>`. Every response carries the
    `data_freshness` envelope.

    Args:
        type_ (ListAirbnbAlterationsType | Unset):  Default: ListAirbnbAlterationsType.PENDING.
        reservation_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbAlterationsResponse200
     """


    return sync_detailed(
        client=client,
type_=type_,
reservation_code=reservation_code,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    type_: ListAirbnbAlterationsType | Unset = ListAirbnbAlterationsType.PENDING,
    reservation_code: str | Unset = UNSET,

) -> Response[Error | ListAirbnbAlterationsResponse200]:
    """ List Airbnb alterations

     List reservation alteration requests for Airbnb reservations in this workspace. **Pure DB read**
    from the local `reservation_alterations` mirror — never calls Airbnb upstream — scoped to your
    workspace via the reservations join.

    Default returns only pending alterations; pass `?type=all` for the full history. Filter to a single
    reservation with `?reservation_code=<confirmation code>`. Every response carries the
    `data_freshness` envelope.

    Args:
        type_ (ListAirbnbAlterationsType | Unset):  Default: ListAirbnbAlterationsType.PENDING.
        reservation_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbAlterationsResponse200]
     """


    kwargs = _get_kwargs(
        type_=type_,
reservation_code=reservation_code,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    type_: ListAirbnbAlterationsType | Unset = ListAirbnbAlterationsType.PENDING,
    reservation_code: str | Unset = UNSET,

) -> Error | ListAirbnbAlterationsResponse200 | None:
    """ List Airbnb alterations

     List reservation alteration requests for Airbnb reservations in this workspace. **Pure DB read**
    from the local `reservation_alterations` mirror — never calls Airbnb upstream — scoped to your
    workspace via the reservations join.

    Default returns only pending alterations; pass `?type=all` for the full history. Filter to a single
    reservation with `?reservation_code=<confirmation code>`. Every response carries the
    `data_freshness` envelope.

    Args:
        type_ (ListAirbnbAlterationsType | Unset):  Default: ListAirbnbAlterationsType.PENDING.
        reservation_code (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbAlterationsResponse200
     """


    return (await asyncio_detailed(
        client=client,
type_=type_,
reservation_code=reservation_code,

    )).parsed
