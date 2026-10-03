from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.guest_update_request import GuestUpdateRequest
from ...models.guest_update_response import GuestUpdateResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: GuestUpdateRequest,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/guests/{id}".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GuestUpdateResponse | None:
    if response.status_code == 200:
        response_200 = GuestUpdateResponse.from_dict(response.json())



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

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GuestUpdateResponse]:
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
    body: GuestUpdateRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | GuestUpdateResponse]:
    """ Update a guest

     Change a guest's name, email, phone or language. Email and phone are added as the guest's newest
    contact; earlier ones are kept.

    **Guests linked to a connected PMS** (created with `provider`, or imported from one) are changed in
    that PMS first. A PMS whose API cannot change guest profiles returns `422 pms_write_unsupported`
    naming it (Hostaway today) and nothing is written; `GET /v1/connect/{provider}` →
    `capabilities.pms.guests.update` says so beforehand. A revoked PMS connection is `403
    connection_reauth_required`.

    Send `Idempotency-Key` to make a retry safe.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (GuestUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GuestUpdateResponse]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: GuestUpdateRequest,
    idempotency_key: str | Unset = UNSET,

) -> Error | GuestUpdateResponse | None:
    """ Update a guest

     Change a guest's name, email, phone or language. Email and phone are added as the guest's newest
    contact; earlier ones are kept.

    **Guests linked to a connected PMS** (created with `provider`, or imported from one) are changed in
    that PMS first. A PMS whose API cannot change guest profiles returns `422 pms_write_unsupported`
    naming it (Hostaway today) and nothing is written; `GET /v1/connect/{provider}` →
    `capabilities.pms.guests.update` says so beforehand. A revoked PMS connection is `403
    connection_reauth_required`.

    Send `Idempotency-Key` to make a retry safe.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (GuestUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GuestUpdateResponse
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: GuestUpdateRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | GuestUpdateResponse]:
    """ Update a guest

     Change a guest's name, email, phone or language. Email and phone are added as the guest's newest
    contact; earlier ones are kept.

    **Guests linked to a connected PMS** (created with `provider`, or imported from one) are changed in
    that PMS first. A PMS whose API cannot change guest profiles returns `422 pms_write_unsupported`
    naming it (Hostaway today) and nothing is written; `GET /v1/connect/{provider}` →
    `capabilities.pms.guests.update` says so beforehand. A revoked PMS connection is `403
    connection_reauth_required`.

    Send `Idempotency-Key` to make a retry safe.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (GuestUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GuestUpdateResponse]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: GuestUpdateRequest,
    idempotency_key: str | Unset = UNSET,

) -> Error | GuestUpdateResponse | None:
    """ Update a guest

     Change a guest's name, email, phone or language. Email and phone are added as the guest's newest
    contact; earlier ones are kept.

    **Guests linked to a connected PMS** (created with `provider`, or imported from one) are changed in
    that PMS first. A PMS whose API cannot change guest profiles returns `422 pms_write_unsupported`
    naming it (Hostaway today) and nothing is written; `GET /v1/connect/{provider}` →
    `capabilities.pms.guests.update` says so beforehand. A revoked PMS connection is `403
    connection_reauth_required`.

    Send `Idempotency-Key` to make a retry safe.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (GuestUpdateRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GuestUpdateResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
