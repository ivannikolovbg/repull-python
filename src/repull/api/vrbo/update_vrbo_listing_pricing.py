from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from typing import cast



def _get_kwargs(
    id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/vrbo/listings/{id}/pricing".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | None:
    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 501:
        response_501 = Error.from_dict(response.json())



        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error]:
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

) -> Response[Error]:
    """ Update VRBO pricing (501 — no push API exists)

     VRBO has no rate-push API. To change what VRBO sees, update the underlying Vanio calendar/pricing-
    settings (e.g. `PUT /v1/listings/{id}/calendar` once wired) — VRBO will pick up the change on its
    next pull. This endpoint always returns **501** rather than fake-stubbing a successful push the SDK
    would silently swallow.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
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

) -> Error | None:
    """ Update VRBO pricing (501 — no push API exists)

     VRBO has no rate-push API. To change what VRBO sees, update the underlying Vanio calendar/pricing-
    settings (e.g. `PUT /v1/listings/{id}/calendar` once wired) — VRBO will pick up the change on its
    next pull. This endpoint always returns **501** rather than fake-stubbing a successful push the SDK
    would silently swallow.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Error]:
    """ Update VRBO pricing (501 — no push API exists)

     VRBO has no rate-push API. To change what VRBO sees, update the underlying Vanio calendar/pricing-
    settings (e.g. `PUT /v1/listings/{id}/calendar` once wired) — VRBO will pick up the change on its
    next pull. This endpoint always returns **501** rather than fake-stubbing a successful push the SDK
    would silently swallow.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
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

) -> Error | None:
    """ Update VRBO pricing (501 — no push API exists)

     VRBO has no rate-push API. To change what VRBO sees, update the underlying Vanio calendar/pricing-
    settings (e.g. `PUT /v1/listings/{id}/calendar` once wired) — VRBO will pick up the change on its
    next pull. This endpoint always returns **501** rather than fake-stubbing a successful push the SDK
    would silently swallow.

    Args:
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
