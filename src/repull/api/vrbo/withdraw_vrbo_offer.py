from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.withdraw_vrbo_offer_response_200 import WithdrawVrboOfferResponse200
from typing import cast



def _get_kwargs(
    *,
    thread_id: str,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["thread_id"] = thread_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/channels/vrbo/offers",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | WithdrawVrboOfferResponse200 | None:
    if response.status_code == 200:
        response_200 = WithdrawVrboOfferResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | WithdrawVrboOfferResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    thread_id: str,

) -> Response[Error | WithdrawVrboOfferResponse200]:
    """ Withdraw the Vrbo pre-approval or quote

     Withdraw the conversation's pre-approval or quote: the guest can no longer book on it. The
    counterpart of `DELETE /v1/channels/airbnb/offers`, by `thread_id`.

    Args:
        thread_id (str):  Example: vrbo:3f2a9c1e-5b7d-4e2a-9c1f-0a1b2c3d4e5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WithdrawVrboOfferResponse200]
     """


    kwargs = _get_kwargs(
        thread_id=thread_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    thread_id: str,

) -> Error | WithdrawVrboOfferResponse200 | None:
    """ Withdraw the Vrbo pre-approval or quote

     Withdraw the conversation's pre-approval or quote: the guest can no longer book on it. The
    counterpart of `DELETE /v1/channels/airbnb/offers`, by `thread_id`.

    Args:
        thread_id (str):  Example: vrbo:3f2a9c1e-5b7d-4e2a-9c1f-0a1b2c3d4e5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WithdrawVrboOfferResponse200
     """


    return sync_detailed(
        client=client,
thread_id=thread_id,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    thread_id: str,

) -> Response[Error | WithdrawVrboOfferResponse200]:
    """ Withdraw the Vrbo pre-approval or quote

     Withdraw the conversation's pre-approval or quote: the guest can no longer book on it. The
    counterpart of `DELETE /v1/channels/airbnb/offers`, by `thread_id`.

    Args:
        thread_id (str):  Example: vrbo:3f2a9c1e-5b7d-4e2a-9c1f-0a1b2c3d4e5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WithdrawVrboOfferResponse200]
     """


    kwargs = _get_kwargs(
        thread_id=thread_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    thread_id: str,

) -> Error | WithdrawVrboOfferResponse200 | None:
    """ Withdraw the Vrbo pre-approval or quote

     Withdraw the conversation's pre-approval or quote: the guest can no longer book on it. The
    counterpart of `DELETE /v1/channels/airbnb/offers`, by `thread_id`.

    Args:
        thread_id (str):  Example: vrbo:3f2a9c1e-5b7d-4e2a-9c1f-0a1b2c3d4e5f.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WithdrawVrboOfferResponse200
     """


    return (await asyncio_detailed(
        client=client,
thread_id=thread_id,

    )).parsed
