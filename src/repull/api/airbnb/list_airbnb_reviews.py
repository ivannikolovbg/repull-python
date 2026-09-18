from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_review_list_response import AirbnbReviewListResponse
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    account_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["account_id"] = account_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/airbnb/reviews",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AirbnbReviewListResponse | Error | None:
    if response.status_code == 200:
        response_200 = AirbnbReviewListResponse.from_dict(response.json())



        return response_200

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AirbnbReviewListResponse | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,

) -> Response[AirbnbReviewListResponse | Error]:
    """ List Airbnb reviews

     List reviews left by guests on Airbnb listings in this workspace. Includes both reviews of the host
    and reviews of the guest (where the host has not yet submitted theirs).

    Reviews of inactive listings are left out; they keep syncing and reappear once the listing is
    activated. Filtering by an inactive listing (`listing_id`) returns `403 listing_inactive`.

    **Several Airbnb accounts?** A workspace can connect more than one. By default this returns every
    connected account's rows; pass `?account_id=<airbnb host id>` to scope to one. Every row carries
    `accountId` + `accountName` either way, and `dataFreshness.accounts[]` reports each account's
    freshness separately, so one disconnected host no longer marks the whole response stale.

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbReviewListResponse | Error]
     """


    kwargs = _get_kwargs(
        account_id=account_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,

) -> AirbnbReviewListResponse | Error | None:
    """ List Airbnb reviews

     List reviews left by guests on Airbnb listings in this workspace. Includes both reviews of the host
    and reviews of the guest (where the host has not yet submitted theirs).

    Reviews of inactive listings are left out; they keep syncing and reappear once the listing is
    activated. Filtering by an inactive listing (`listing_id`) returns `403 listing_inactive`.

    **Several Airbnb accounts?** A workspace can connect more than one. By default this returns every
    connected account's rows; pass `?account_id=<airbnb host id>` to scope to one. Every row carries
    `accountId` + `accountName` either way, and `dataFreshness.accounts[]` reports each account's
    freshness separately, so one disconnected host no longer marks the whole response stale.

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbReviewListResponse | Error
     """


    return sync_detailed(
        client=client,
account_id=account_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,

) -> Response[AirbnbReviewListResponse | Error]:
    """ List Airbnb reviews

     List reviews left by guests on Airbnb listings in this workspace. Includes both reviews of the host
    and reviews of the guest (where the host has not yet submitted theirs).

    Reviews of inactive listings are left out; they keep syncing and reappear once the listing is
    activated. Filtering by an inactive listing (`listing_id`) returns `403 listing_inactive`.

    **Several Airbnb accounts?** A workspace can connect more than one. By default this returns every
    connected account's rows; pass `?account_id=<airbnb host id>` to scope to one. Every row carries
    `accountId` + `accountName` either way, and `dataFreshness.accounts[]` reports each account's
    freshness separately, so one disconnected host no longer marks the whole response stale.

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbReviewListResponse | Error]
     """


    kwargs = _get_kwargs(
        account_id=account_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,

) -> AirbnbReviewListResponse | Error | None:
    """ List Airbnb reviews

     List reviews left by guests on Airbnb listings in this workspace. Includes both reviews of the host
    and reviews of the guest (where the host has not yet submitted theirs).

    Reviews of inactive listings are left out; they keep syncing and reappear once the listing is
    activated. Filtering by an inactive listing (`listing_id`) returns `403 listing_inactive`.

    **Several Airbnb accounts?** A workspace can connect more than one. By default this returns every
    connected account's rows; pass `?account_id=<airbnb host id>` to scope to one. Every row carries
    `accountId` + `accountName` either way, and `dataFreshness.accounts[]` reports each account's
    freshness separately, so one disconnected host no longer marks the whole response stale.

    Args:
        account_id (str | Unset):  Example: 1772489413932732258.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbReviewListResponse | Error
     """


    return (await asyncio_detailed(
        client=client,
account_id=account_id,

    )).parsed
