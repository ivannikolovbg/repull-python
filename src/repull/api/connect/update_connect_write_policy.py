from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.update_connect_write_policy_body import UpdateConnectWritePolicyBody
from ...models.update_connect_write_policy_response_200 import UpdateConnectWritePolicyResponse200
from typing import cast



def _get_kwargs(
    provider: str,
    *,
    body: UpdateConnectWritePolicyBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/connect/{provider}/write-policy".format(provider=quote(str(provider), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | UpdateConnectWritePolicyResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateConnectWritePolicyResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | UpdateConnectWritePolicyResponse200]:
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
    body: UpdateConnectWritePolicyBody,

) -> Response[Error | UpdateConnectWritePolicyResponse200]:
    """ Change what the app may change in a PMS

     Turns individual write switches on or off for the connection. Only the switches you send change.
    Takes effect on the next write — nothing already sent to the PMS is undone. The policy is kept when
    the PMS is reconnected.

    With `reservations.api` off, the reservations API returns `409 pms_writes_off` for bookings on this
    PMS. With `reservations.website` off, booking sites stop taking bookings for it before the guest is
    charged.

    Args:
        provider (str):
        body (UpdateConnectWritePolicyBody): Only the switches you send change. Every value must
            be a boolean. Example: {'calendar': {'availability': False, 'rates': True}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateConnectWritePolicyResponse200]
     """


    kwargs = _get_kwargs(
        provider=provider,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateConnectWritePolicyBody,

) -> Error | UpdateConnectWritePolicyResponse200 | None:
    """ Change what the app may change in a PMS

     Turns individual write switches on or off for the connection. Only the switches you send change.
    Takes effect on the next write — nothing already sent to the PMS is undone. The policy is kept when
    the PMS is reconnected.

    With `reservations.api` off, the reservations API returns `409 pms_writes_off` for bookings on this
    PMS. With `reservations.website` off, booking sites stop taking bookings for it before the guest is
    charged.

    Args:
        provider (str):
        body (UpdateConnectWritePolicyBody): Only the switches you send change. Every value must
            be a boolean. Example: {'calendar': {'availability': False, 'rates': True}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateConnectWritePolicyResponse200
     """


    return sync_detailed(
        provider=provider,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateConnectWritePolicyBody,

) -> Response[Error | UpdateConnectWritePolicyResponse200]:
    """ Change what the app may change in a PMS

     Turns individual write switches on or off for the connection. Only the switches you send change.
    Takes effect on the next write — nothing already sent to the PMS is undone. The policy is kept when
    the PMS is reconnected.

    With `reservations.api` off, the reservations API returns `409 pms_writes_off` for bookings on this
    PMS. With `reservations.website` off, booking sites stop taking bookings for it before the guest is
    charged.

    Args:
        provider (str):
        body (UpdateConnectWritePolicyBody): Only the switches you send change. Every value must
            be a boolean. Example: {'calendar': {'availability': False, 'rates': True}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateConnectWritePolicyResponse200]
     """


    kwargs = _get_kwargs(
        provider=provider,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    provider: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateConnectWritePolicyBody,

) -> Error | UpdateConnectWritePolicyResponse200 | None:
    """ Change what the app may change in a PMS

     Turns individual write switches on or off for the connection. Only the switches you send change.
    Takes effect on the next write — nothing already sent to the PMS is undone. The policy is kept when
    the PMS is reconnected.

    With `reservations.api` off, the reservations API returns `409 pms_writes_off` for bookings on this
    PMS. With `reservations.website` off, booking sites stop taking bookings for it before the guest is
    charged.

    Args:
        provider (str):
        body (UpdateConnectWritePolicyBody): Only the switches you send change. Every value must
            be a boolean. Example: {'calendar': {'availability': False, 'rates': True}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateConnectWritePolicyResponse200
     """


    return (await asyncio_detailed(
        provider=provider,
client=client,
body=body,

    )).parsed
