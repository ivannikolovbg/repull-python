from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.tiket_connect_claim_response import TiketConnectClaimResponse
from ...models.verify_tiket_claim_body import VerifyTiketClaimBody
from typing import cast



def _get_kwargs(
    *,
    body: VerifyTiketClaimBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connect/tiket/verify",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | TiketConnectClaimResponse | None:
    if response.status_code == 200:
        response_200 = TiketConnectClaimResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 410:
        response_410 = Error.from_dict(response.json())



        return response_410

    if response.status_code == 412:
        response_412 = Error.from_dict(response.json())



        return response_412

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | TiketConnectClaimResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VerifyTiketClaimBody,

) -> Response[Error | TiketConnectClaimResponse]:
    r""" Claim a tiket.com property in a Connect session

     Called by the hosted Connect page and authorized by the Connect session id, not an API key. Start
    the session with `POST /v1/connect` (`allowedProviders: [\"tiket\"]`) and send the host to its
    `url`.

    The host activates Repull as their channel manager in the tiket.com extranet, then enters their
    tiket.com Hotel ID (a number). Repull checks with tiket.com, then imports the property's room types
    and rate plans and maps rooms to listings with the same name (`autoMapped`).

    `412 awaiting_activation` means tiket.com has not activated Repull for that Hotel ID yet, or the id
    is wrong. tiket.com does not announce activations, so the hosted page offers to try again and Repull
    keeps checking in the background. A property already connected to another workspace returns `409
    property_already_connected`.

    Args:
        body (VerifyTiketClaimBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketConnectClaimResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: VerifyTiketClaimBody,

) -> Error | TiketConnectClaimResponse | None:
    r""" Claim a tiket.com property in a Connect session

     Called by the hosted Connect page and authorized by the Connect session id, not an API key. Start
    the session with `POST /v1/connect` (`allowedProviders: [\"tiket\"]`) and send the host to its
    `url`.

    The host activates Repull as their channel manager in the tiket.com extranet, then enters their
    tiket.com Hotel ID (a number). Repull checks with tiket.com, then imports the property's room types
    and rate plans and maps rooms to listings with the same name (`autoMapped`).

    `412 awaiting_activation` means tiket.com has not activated Repull for that Hotel ID yet, or the id
    is wrong. tiket.com does not announce activations, so the hosted page offers to try again and Repull
    keeps checking in the background. A property already connected to another workspace returns `409
    property_already_connected`.

    Args:
        body (VerifyTiketClaimBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketConnectClaimResponse
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: VerifyTiketClaimBody,

) -> Response[Error | TiketConnectClaimResponse]:
    r""" Claim a tiket.com property in a Connect session

     Called by the hosted Connect page and authorized by the Connect session id, not an API key. Start
    the session with `POST /v1/connect` (`allowedProviders: [\"tiket\"]`) and send the host to its
    `url`.

    The host activates Repull as their channel manager in the tiket.com extranet, then enters their
    tiket.com Hotel ID (a number). Repull checks with tiket.com, then imports the property's room types
    and rate plans and maps rooms to listings with the same name (`autoMapped`).

    `412 awaiting_activation` means tiket.com has not activated Repull for that Hotel ID yet, or the id
    is wrong. tiket.com does not announce activations, so the hosted page offers to try again and Repull
    keeps checking in the background. A property already connected to another workspace returns `409
    property_already_connected`.

    Args:
        body (VerifyTiketClaimBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | TiketConnectClaimResponse]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: VerifyTiketClaimBody,

) -> Error | TiketConnectClaimResponse | None:
    r""" Claim a tiket.com property in a Connect session

     Called by the hosted Connect page and authorized by the Connect session id, not an API key. Start
    the session with `POST /v1/connect` (`allowedProviders: [\"tiket\"]`) and send the host to its
    `url`.

    The host activates Repull as their channel manager in the tiket.com extranet, then enters their
    tiket.com Hotel ID (a number). Repull checks with tiket.com, then imports the property's room types
    and rate plans and maps rooms to listings with the same name (`autoMapped`).

    `412 awaiting_activation` means tiket.com has not activated Repull for that Hotel ID yet, or the id
    is wrong. tiket.com does not announce activations, so the hosted page offers to try again and Repull
    keeps checking in the background. A property already connected to another workspace returns `409
    property_already_connected`.

    Args:
        body (VerifyTiketClaimBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | TiketConnectClaimResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
