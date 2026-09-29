from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_connect_write_policy_response_200 import GetConnectWritePolicyResponse200
from typing import cast



def _get_kwargs(
    provider: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/connect/{provider}/write-policy".format(provider=quote(str(provider), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetConnectWritePolicyResponse200 | None:
    if response.status_code == 200:
        response_200 = GetConnectWritePolicyResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetConnectWritePolicyResponse200]:
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

) -> Response[Error | GetConnectWritePolicyResponse200]:
    """ Get what the app may change in a PMS

     Returns the connection's write policy: whether the app may open and close nights, change prices and
    minimum stay in the PMS, and whether bookings may be created or changed there from the booking
    website, the dashboard or the reservations API.

    Hotel PMSs (Cloudbeds, Mews) start with every calendar switch off — the PMS owns its room inventory.
    Every other PMS starts with everything on. PMS connections only.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetConnectWritePolicyResponse200]
     """


    kwargs = _get_kwargs(
        provider=provider,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    provider: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetConnectWritePolicyResponse200 | None:
    """ Get what the app may change in a PMS

     Returns the connection's write policy: whether the app may open and close nights, change prices and
    minimum stay in the PMS, and whether bookings may be created or changed there from the booking
    website, the dashboard or the reservations API.

    Hotel PMSs (Cloudbeds, Mews) start with every calendar switch off — the PMS owns its room inventory.
    Every other PMS starts with everything on. PMS connections only.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetConnectWritePolicyResponse200
     """


    return sync_detailed(
        provider=provider,
client=client,

    ).parsed

async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | GetConnectWritePolicyResponse200]:
    """ Get what the app may change in a PMS

     Returns the connection's write policy: whether the app may open and close nights, change prices and
    minimum stay in the PMS, and whether bookings may be created or changed there from the booking
    website, the dashboard or the reservations API.

    Hotel PMSs (Cloudbeds, Mews) start with every calendar switch off — the PMS owns its room inventory.
    Every other PMS starts with everything on. PMS connections only.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetConnectWritePolicyResponse200]
     """


    kwargs = _get_kwargs(
        provider=provider,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    provider: str,
    *,
    client: AuthenticatedClient | Client,

) -> Error | GetConnectWritePolicyResponse200 | None:
    """ Get what the app may change in a PMS

     Returns the connection's write policy: whether the app may open and close nights, change prices and
    minimum stay in the PMS, and whether bookings may be created or changed there from the booking
    website, the dashboard or the reservations API.

    Hotel PMSs (Cloudbeds, Mews) start with every calendar switch off — the PMS owns its room inventory.
    Every other PMS starts with everything on. PMS connections only.

    Args:
        provider (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetConnectWritePolicyResponse200
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,

    )).parsed
