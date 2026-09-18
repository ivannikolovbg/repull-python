from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_connection_response_200 import DeleteConnectionResponse200
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    provider: str,
    *,
    account_id: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["accountId"] = account_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/connect/{provider}".format(provider=quote(str(provider), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteConnectionResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = DeleteConnectionResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 501:
        response_501 = Error.from_dict(response.json())



        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteConnectionResponse200 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,

) -> Response[DeleteConnectionResponse200 | Error]:
    """ Disconnect provider

     Disconnect ONE connected account of a provider from this workspace. Supported for `airbnb` and
    `booking`.

    **Which account.** Pass `accountId` — for Airbnb the host id (`accounts[].externalAccountId` from
    `GET /v1/connect/airbnb`), for Booking.com the hotel id. It is optional only when the workspace has
    exactly one account for the provider. With several and no `accountId`, the call returns `422` with
    the account ids in `valid_values` instead of guessing. An `accountId` that is not connected to this
    workspace returns `404`. Disconnecting one account leaves the others connected.

    **What happens.** The account's stored authorization is removed and it stops syncing. Its listings
    are **deactivated**, not deleted: they stop counting toward your plan's listing limit, their data is
    kept, and they are returned in `listingsDeactivated`. A listing that is still connected through
    another account or channel stays active. Reconnect the account, then activate the listings with
    `POST /v1/listings/status`.

    The change is all or nothing. For Airbnb, the host can also revoke access on Airbnb's side (Account
    → Privacy & sharing → Connected apps); that alone does not update this workspace, so call this
    endpoint as well.

    Other providers return `501 not_implemented` with instructions for disconnecting on the provider's
    side. That answer depends only on the provider, not on your workspace: an unsupported provider
    returns `501` whether or not you have a connection to it. `404 not_found` on a supported provider
    means this workspace has no connection to it (or, with `accountId`, that the account is not
    connected here).

    Args:
        provider (str):
        account_id (str | Unset):  Example: 143778955.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteConnectionResponse200 | Error]
     """


    kwargs = _get_kwargs(
        provider=provider,
account_id=account_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,

) -> DeleteConnectionResponse200 | Error | None:
    """ Disconnect provider

     Disconnect ONE connected account of a provider from this workspace. Supported for `airbnb` and
    `booking`.

    **Which account.** Pass `accountId` — for Airbnb the host id (`accounts[].externalAccountId` from
    `GET /v1/connect/airbnb`), for Booking.com the hotel id. It is optional only when the workspace has
    exactly one account for the provider. With several and no `accountId`, the call returns `422` with
    the account ids in `valid_values` instead of guessing. An `accountId` that is not connected to this
    workspace returns `404`. Disconnecting one account leaves the others connected.

    **What happens.** The account's stored authorization is removed and it stops syncing. Its listings
    are **deactivated**, not deleted: they stop counting toward your plan's listing limit, their data is
    kept, and they are returned in `listingsDeactivated`. A listing that is still connected through
    another account or channel stays active. Reconnect the account, then activate the listings with
    `POST /v1/listings/status`.

    The change is all or nothing. For Airbnb, the host can also revoke access on Airbnb's side (Account
    → Privacy & sharing → Connected apps); that alone does not update this workspace, so call this
    endpoint as well.

    Other providers return `501 not_implemented` with instructions for disconnecting on the provider's
    side. That answer depends only on the provider, not on your workspace: an unsupported provider
    returns `501` whether or not you have a connection to it. `404 not_found` on a supported provider
    means this workspace has no connection to it (or, with `accountId`, that the account is not
    connected here).

    Args:
        provider (str):
        account_id (str | Unset):  Example: 143778955.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteConnectionResponse200 | Error
     """


    return sync_detailed(
        provider=provider,
client=client,
account_id=account_id,

    ).parsed

async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,

) -> Response[DeleteConnectionResponse200 | Error]:
    """ Disconnect provider

     Disconnect ONE connected account of a provider from this workspace. Supported for `airbnb` and
    `booking`.

    **Which account.** Pass `accountId` — for Airbnb the host id (`accounts[].externalAccountId` from
    `GET /v1/connect/airbnb`), for Booking.com the hotel id. It is optional only when the workspace has
    exactly one account for the provider. With several and no `accountId`, the call returns `422` with
    the account ids in `valid_values` instead of guessing. An `accountId` that is not connected to this
    workspace returns `404`. Disconnecting one account leaves the others connected.

    **What happens.** The account's stored authorization is removed and it stops syncing. Its listings
    are **deactivated**, not deleted: they stop counting toward your plan's listing limit, their data is
    kept, and they are returned in `listingsDeactivated`. A listing that is still connected through
    another account or channel stays active. Reconnect the account, then activate the listings with
    `POST /v1/listings/status`.

    The change is all or nothing. For Airbnb, the host can also revoke access on Airbnb's side (Account
    → Privacy & sharing → Connected apps); that alone does not update this workspace, so call this
    endpoint as well.

    Other providers return `501 not_implemented` with instructions for disconnecting on the provider's
    side. That answer depends only on the provider, not on your workspace: an unsupported provider
    returns `501` whether or not you have a connection to it. `404 not_found` on a supported provider
    means this workspace has no connection to it (or, with `accountId`, that the account is not
    connected here).

    Args:
        provider (str):
        account_id (str | Unset):  Example: 143778955.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteConnectionResponse200 | Error]
     """


    kwargs = _get_kwargs(
        provider=provider,
account_id=account_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    account_id: str | Unset = UNSET,

) -> DeleteConnectionResponse200 | Error | None:
    """ Disconnect provider

     Disconnect ONE connected account of a provider from this workspace. Supported for `airbnb` and
    `booking`.

    **Which account.** Pass `accountId` — for Airbnb the host id (`accounts[].externalAccountId` from
    `GET /v1/connect/airbnb`), for Booking.com the hotel id. It is optional only when the workspace has
    exactly one account for the provider. With several and no `accountId`, the call returns `422` with
    the account ids in `valid_values` instead of guessing. An `accountId` that is not connected to this
    workspace returns `404`. Disconnecting one account leaves the others connected.

    **What happens.** The account's stored authorization is removed and it stops syncing. Its listings
    are **deactivated**, not deleted: they stop counting toward your plan's listing limit, their data is
    kept, and they are returned in `listingsDeactivated`. A listing that is still connected through
    another account or channel stays active. Reconnect the account, then activate the listings with
    `POST /v1/listings/status`.

    The change is all or nothing. For Airbnb, the host can also revoke access on Airbnb's side (Account
    → Privacy & sharing → Connected apps); that alone does not update this workspace, so call this
    endpoint as well.

    Other providers return `501 not_implemented` with instructions for disconnecting on the provider's
    side. That answer depends only on the provider, not on your workspace: an unsupported provider
    returns `501` whether or not you have a connection to it. `404 not_found` on a supported provider
    means this workspace has no connection to it (or, with `accountId`, that the account is not
    connected here).

    Args:
        provider (str):
        account_id (str | Unset):  Example: 143778955.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteConnectionResponse200 | Error
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,
account_id=account_id,

    )).parsed
