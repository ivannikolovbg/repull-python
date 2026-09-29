from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.withdraw_conversation_preapproval_response_200 import WithdrawConversationPreapprovalResponse200
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/conversations/{id}/pre-approval".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | WithdrawConversationPreapprovalResponse200 | None:
    if response.status_code == 200:
        response_200 = WithdrawConversationPreapprovalResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | WithdrawConversationPreapprovalResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | WithdrawConversationPreapprovalResponse200]:
    """ Withdraw a pre-approval

     Withdraw the live pre-approval (or offer) on this conversation: the guest can no longer book on it,
    and the inquiry is open again. **VRBO**. On Airbnb a pre-approval is a special offer — withdraw it
    with `DELETE /v1/conversations/{id}/special-offers/{offerId}`; here it is `422
    channel_not_supported`.

    `GET /v1/conversations/{id}` → `capabilities.canWithdraw` says whether there is something to
    withdraw.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WithdrawConversationPreapprovalResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Error | WithdrawConversationPreapprovalResponse200 | None:
    """ Withdraw a pre-approval

     Withdraw the live pre-approval (or offer) on this conversation: the guest can no longer book on it,
    and the inquiry is open again. **VRBO**. On Airbnb a pre-approval is a special offer — withdraw it
    with `DELETE /v1/conversations/{id}/special-offers/{offerId}`; here it is `422
    channel_not_supported`.

    `GET /v1/conversations/{id}` → `capabilities.canWithdraw` says whether there is something to
    withdraw.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WithdrawConversationPreapprovalResponse200
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error | WithdrawConversationPreapprovalResponse200]:
    """ Withdraw a pre-approval

     Withdraw the live pre-approval (or offer) on this conversation: the guest can no longer book on it,
    and the inquiry is open again. **VRBO**. On Airbnb a pre-approval is a special offer — withdraw it
    with `DELETE /v1/conversations/{id}/special-offers/{offerId}`; here it is `422
    channel_not_supported`.

    `GET /v1/conversations/{id}` → `capabilities.canWithdraw` says whether there is something to
    withdraw.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WithdrawConversationPreapprovalResponse200]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Error | WithdrawConversationPreapprovalResponse200 | None:
    """ Withdraw a pre-approval

     Withdraw the live pre-approval (or offer) on this conversation: the guest can no longer book on it,
    and the inquiry is open again. **VRBO**. On Airbnb a pre-approval is a special offer — withdraw it
    with `DELETE /v1/conversations/{id}/special-offers/{offerId}`; here it is `422
    channel_not_supported`.

    `GET /v1/conversations/{id}` → `capabilities.canWithdraw` says whether there is something to
    withdraw.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WithdrawConversationPreapprovalResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
