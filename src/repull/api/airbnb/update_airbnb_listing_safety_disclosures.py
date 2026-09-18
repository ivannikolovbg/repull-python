from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_safety_disclosures_write_request import AirbnbSafetyDisclosuresWriteRequest
from ...models.error import Error
from ...models.update_airbnb_listing_safety_disclosures_response_200 import UpdateAirbnbListingSafetyDisclosuresResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: AirbnbSafetyDisclosuresWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/airbnb/listings/{id}/safety-disclosures".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | UpdateAirbnbListingSafetyDisclosuresResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateAirbnbListingSafetyDisclosuresResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | UpdateAirbnbListingSafetyDisclosuresResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AirbnbSafetyDisclosuresWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | UpdateAirbnbListingSafetyDisclosuresResponse200]:
    """ Update guest-safety disclosures

     Declare or retract the guest-safety disclosures on the live Airbnb listing.

    **This is a MERGE, not a replacement.** Airbnb keeps one value per disclosure type: a type you leave
    out keeps the value it has, and to retract one you send it with `value: false`. A full replacement
    would let a partial request silently un-declare a security camera — a guest-safety statement, not a
    preference.

    Only the disclosures are sent upstream. The same Airbnb endpoint carries the cancellation policy and
    instant-book settings, and this endpoint never touches them.

    Send `Idempotency-Key` to make a retry safe.

    Airbnb refusing the change is `422 airbnb_rejected` with Airbnb's own reason; an expired or revoked
    connection is `403 connection_reauth_required`.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbSafetyDisclosuresWriteRequest): A MERGE, not a replacement: Airbnb keeps one
            value per disclosure type, a type you leave out keeps the value it has, and to retract a
            disclosure you send it with `value: false`. A full replacement would let a partial request
            silently un-declare a security camera — which is a guest-safety statement, not a
            preference.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbListingSafetyDisclosuresResponse200]
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AirbnbSafetyDisclosuresWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> Error | UpdateAirbnbListingSafetyDisclosuresResponse200 | None:
    """ Update guest-safety disclosures

     Declare or retract the guest-safety disclosures on the live Airbnb listing.

    **This is a MERGE, not a replacement.** Airbnb keeps one value per disclosure type: a type you leave
    out keeps the value it has, and to retract one you send it with `value: false`. A full replacement
    would let a partial request silently un-declare a security camera — a guest-safety statement, not a
    preference.

    Only the disclosures are sent upstream. The same Airbnb endpoint carries the cancellation policy and
    instant-book settings, and this endpoint never touches them.

    Send `Idempotency-Key` to make a retry safe.

    Airbnb refusing the change is `422 airbnb_rejected` with Airbnb's own reason; an expired or revoked
    connection is `403 connection_reauth_required`.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbSafetyDisclosuresWriteRequest): A MERGE, not a replacement: Airbnb keeps one
            value per disclosure type, a type you leave out keeps the value it has, and to retract a
            disclosure you send it with `value: false`. A full replacement would let a partial request
            silently un-declare a security camera — which is a guest-safety statement, not a
            preference.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbListingSafetyDisclosuresResponse200
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AirbnbSafetyDisclosuresWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | UpdateAirbnbListingSafetyDisclosuresResponse200]:
    """ Update guest-safety disclosures

     Declare or retract the guest-safety disclosures on the live Airbnb listing.

    **This is a MERGE, not a replacement.** Airbnb keeps one value per disclosure type: a type you leave
    out keeps the value it has, and to retract one you send it with `value: false`. A full replacement
    would let a partial request silently un-declare a security camera — a guest-safety statement, not a
    preference.

    Only the disclosures are sent upstream. The same Airbnb endpoint carries the cancellation policy and
    instant-book settings, and this endpoint never touches them.

    Send `Idempotency-Key` to make a retry safe.

    Airbnb refusing the change is `422 airbnb_rejected` with Airbnb's own reason; an expired or revoked
    connection is `403 connection_reauth_required`.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbSafetyDisclosuresWriteRequest): A MERGE, not a replacement: Airbnb keeps one
            value per disclosure type, a type you leave out keeps the value it has, and to retract a
            disclosure you send it with `value: false`. A full replacement would let a partial request
            silently un-declare a security camera — which is a guest-safety statement, not a
            preference.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbListingSafetyDisclosuresResponse200]
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AirbnbSafetyDisclosuresWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> Error | UpdateAirbnbListingSafetyDisclosuresResponse200 | None:
    """ Update guest-safety disclosures

     Declare or retract the guest-safety disclosures on the live Airbnb listing.

    **This is a MERGE, not a replacement.** Airbnb keeps one value per disclosure type: a type you leave
    out keeps the value it has, and to retract one you send it with `value: false`. A full replacement
    would let a partial request silently un-declare a security camera — a guest-safety statement, not a
    preference.

    Only the disclosures are sent upstream. The same Airbnb endpoint carries the cancellation policy and
    instant-book settings, and this endpoint never touches them.

    Send `Idempotency-Key` to make a retry safe.

    Airbnb refusing the change is `422 airbnb_rejected` with Airbnb's own reason; an expired or revoked
    connection is `403 connection_reauth_required`.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbSafetyDisclosuresWriteRequest): A MERGE, not a replacement: Airbnb keeps one
            value per disclosure type, a type you leave out keeps the value it has, and to retract a
            disclosure you send it with `value: false`. A full replacement would let a partial request
            silently un-declare a security camera — which is a guest-safety statement, not a
            preference.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbListingSafetyDisclosuresResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
