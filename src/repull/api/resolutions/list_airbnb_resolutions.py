from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.list_airbnb_resolutions_response_200 import ListAirbnbResolutionsResponse200
from ...models.list_airbnb_resolutions_status import ListAirbnbResolutionsStatus
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    status: ListAirbnbResolutionsStatus | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_schema, Unset):
        headers["X-Schema"] = x_schema



    

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/resolutions",
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListAirbnbResolutionsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAirbnbResolutionsResponse200.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListAirbnbResolutionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: ListAirbnbResolutionsStatus | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Response[Error | ListAirbnbResolutionsResponse200]:
    """ List Airbnb Resolution Center cases

     The host's Airbnb Resolution Center cases (AirCover / damage, extra-guest, refund and change
    requests), open and closed. Served from the database; `POST` this path to refresh from Airbnb. READ-
    ONLY upstream — Airbnb's Resolutions API is read-only; a claim is created, evidence added and status
    changed only in Airbnb's Resolution Center UI, not via API. Use this for visibility and action
    tracking (`suggestedActionText`). The money a resolution moved is in the transactions ledger as
    `Resolution Payout` / `Resolution Adjustment` rows sharing the same reference — join on
    `resolutionId`. Cursor-paginated, newest first.

    Args:
        status (ListAirbnbResolutionsStatus | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbResolutionsResponse200]
     """


    kwargs = _get_kwargs(
        status=status,
limit=limit,
cursor=cursor,
x_schema=x_schema,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    status: ListAirbnbResolutionsStatus | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Error | ListAirbnbResolutionsResponse200 | None:
    """ List Airbnb Resolution Center cases

     The host's Airbnb Resolution Center cases (AirCover / damage, extra-guest, refund and change
    requests), open and closed. Served from the database; `POST` this path to refresh from Airbnb. READ-
    ONLY upstream — Airbnb's Resolutions API is read-only; a claim is created, evidence added and status
    changed only in Airbnb's Resolution Center UI, not via API. Use this for visibility and action
    tracking (`suggestedActionText`). The money a resolution moved is in the transactions ledger as
    `Resolution Payout` / `Resolution Adjustment` rows sharing the same reference — join on
    `resolutionId`. Cursor-paginated, newest first.

    Args:
        status (ListAirbnbResolutionsStatus | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbResolutionsResponse200
     """


    return sync_detailed(
        client=client,
status=status,
limit=limit,
cursor=cursor,
x_schema=x_schema,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: ListAirbnbResolutionsStatus | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Response[Error | ListAirbnbResolutionsResponse200]:
    """ List Airbnb Resolution Center cases

     The host's Airbnb Resolution Center cases (AirCover / damage, extra-guest, refund and change
    requests), open and closed. Served from the database; `POST` this path to refresh from Airbnb. READ-
    ONLY upstream — Airbnb's Resolutions API is read-only; a claim is created, evidence added and status
    changed only in Airbnb's Resolution Center UI, not via API. Use this for visibility and action
    tracking (`suggestedActionText`). The money a resolution moved is in the transactions ledger as
    `Resolution Payout` / `Resolution Adjustment` rows sharing the same reference — join on
    `resolutionId`. Cursor-paginated, newest first.

    Args:
        status (ListAirbnbResolutionsStatus | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListAirbnbResolutionsResponse200]
     """


    kwargs = _get_kwargs(
        status=status,
limit=limit,
cursor=cursor,
x_schema=x_schema,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: ListAirbnbResolutionsStatus | Unset = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Error | ListAirbnbResolutionsResponse200 | None:
    """ List Airbnb Resolution Center cases

     The host's Airbnb Resolution Center cases (AirCover / damage, extra-guest, refund and change
    requests), open and closed. Served from the database; `POST` this path to refresh from Airbnb. READ-
    ONLY upstream — Airbnb's Resolutions API is read-only; a claim is created, evidence added and status
    changed only in Airbnb's Resolution Center UI, not via API. Use this for visibility and action
    tracking (`suggestedActionText`). The money a resolution moved is in the transactions ledger as
    `Resolution Payout` / `Resolution Adjustment` rows sharing the same reference — join on
    `resolutionId`. Cursor-paginated, newest first.

    Args:
        status (ListAirbnbResolutionsStatus | Unset):
        limit (int | Unset):
        cursor (str | Unset):
        x_schema (str | Unset):  Example: my-app-schema.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListAirbnbResolutionsResponse200
     """


    return (await asyncio_detailed(
        client=client,
status=status,
limit=limit,
cursor=cursor,
x_schema=x_schema,

    )).parsed
