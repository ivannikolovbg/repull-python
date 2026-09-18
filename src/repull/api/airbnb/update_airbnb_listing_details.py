from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_content_write_response import AirbnbContentWriteResponse
from ...models.airbnb_listing_details_write_request import AirbnbListingDetailsWriteRequest
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: AirbnbListingDetailsWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/airbnb/listings/{id}/details".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AirbnbContentWriteResponse | Error | None:
    if response.status_code == 200:
        response_200 = AirbnbContentWriteResponse.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AirbnbContentWriteResponse | Error]:
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
    body: AirbnbListingDetailsWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[AirbnbContentWriteResponse | Error]:
    """ Update property type, room type, quiet hours or check-in method

     Change what kind of property the Airbnb listing is, when its quiet hours are, or how the guest gets
    in. Partial: only the fields you send are written. At least one required; an unknown field is
    refused by name rather than dropped.

    This is the UPDATE path for fields that previously had none. `POST /v1/listings` accepts a
    `propertyType` when a listing is CREATED and nothing could change it afterwards, so a listing mis-
    typed at import stayed mis-typed; the check-in method was mirrored and never exposed at all.

    **A 200 does not by itself mean the change was applied.** `property_type_category`,
    `property_type_group` and `check_in_option` are among the attributes Airbnb locks on established
    listings: the write returns 200, and Airbnb applies nothing for the locked ones. The response
    reports `blockedFields` — the fields YOU sent that Airbnb dropped — and `blockedFields: []` is what
    a landed write looks like. `GET …/details` reports the same list as `lockedFields` so you can check
    first.

    Canonical property type (the value Repull keeps and republishes) is set with `PUT
    /v1/listings/{id}/content` under `details`; this endpoint writes straight to Airbnb.

    Send `Idempotency-Key` to make a retry safe.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbListingDetailsWriteRequest): Update what kind of property this is, when the
            quiet hours are, or how the guest gets in. At least one field required. These are among
            the attributes Airbnb locks on established listings — see `blockedFields` on the response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbContentWriteResponse | Error]
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
    body: AirbnbListingDetailsWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> AirbnbContentWriteResponse | Error | None:
    """ Update property type, room type, quiet hours or check-in method

     Change what kind of property the Airbnb listing is, when its quiet hours are, or how the guest gets
    in. Partial: only the fields you send are written. At least one required; an unknown field is
    refused by name rather than dropped.

    This is the UPDATE path for fields that previously had none. `POST /v1/listings` accepts a
    `propertyType` when a listing is CREATED and nothing could change it afterwards, so a listing mis-
    typed at import stayed mis-typed; the check-in method was mirrored and never exposed at all.

    **A 200 does not by itself mean the change was applied.** `property_type_category`,
    `property_type_group` and `check_in_option` are among the attributes Airbnb locks on established
    listings: the write returns 200, and Airbnb applies nothing for the locked ones. The response
    reports `blockedFields` — the fields YOU sent that Airbnb dropped — and `blockedFields: []` is what
    a landed write looks like. `GET …/details` reports the same list as `lockedFields` so you can check
    first.

    Canonical property type (the value Repull keeps and republishes) is set with `PUT
    /v1/listings/{id}/content` under `details`; this endpoint writes straight to Airbnb.

    Send `Idempotency-Key` to make a retry safe.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbListingDetailsWriteRequest): Update what kind of property this is, when the
            quiet hours are, or how the guest gets in. At least one field required. These are among
            the attributes Airbnb locks on established listings — see `blockedFields` on the response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbContentWriteResponse | Error
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
    body: AirbnbListingDetailsWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[AirbnbContentWriteResponse | Error]:
    """ Update property type, room type, quiet hours or check-in method

     Change what kind of property the Airbnb listing is, when its quiet hours are, or how the guest gets
    in. Partial: only the fields you send are written. At least one required; an unknown field is
    refused by name rather than dropped.

    This is the UPDATE path for fields that previously had none. `POST /v1/listings` accepts a
    `propertyType` when a listing is CREATED and nothing could change it afterwards, so a listing mis-
    typed at import stayed mis-typed; the check-in method was mirrored and never exposed at all.

    **A 200 does not by itself mean the change was applied.** `property_type_category`,
    `property_type_group` and `check_in_option` are among the attributes Airbnb locks on established
    listings: the write returns 200, and Airbnb applies nothing for the locked ones. The response
    reports `blockedFields` — the fields YOU sent that Airbnb dropped — and `blockedFields: []` is what
    a landed write looks like. `GET …/details` reports the same list as `lockedFields` so you can check
    first.

    Canonical property type (the value Repull keeps and republishes) is set with `PUT
    /v1/listings/{id}/content` under `details`; this endpoint writes straight to Airbnb.

    Send `Idempotency-Key` to make a retry safe.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbListingDetailsWriteRequest): Update what kind of property this is, when the
            quiet hours are, or how the guest gets in. At least one field required. These are among
            the attributes Airbnb locks on established listings — see `blockedFields` on the response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbContentWriteResponse | Error]
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
    body: AirbnbListingDetailsWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> AirbnbContentWriteResponse | Error | None:
    """ Update property type, room type, quiet hours or check-in method

     Change what kind of property the Airbnb listing is, when its quiet hours are, or how the guest gets
    in. Partial: only the fields you send are written. At least one required; an unknown field is
    refused by name rather than dropped.

    This is the UPDATE path for fields that previously had none. `POST /v1/listings` accepts a
    `propertyType` when a listing is CREATED and nothing could change it afterwards, so a listing mis-
    typed at import stayed mis-typed; the check-in method was mirrored and never exposed at all.

    **A 200 does not by itself mean the change was applied.** `property_type_category`,
    `property_type_group` and `check_in_option` are among the attributes Airbnb locks on established
    listings: the write returns 200, and Airbnb applies nothing for the locked ones. The response
    reports `blockedFields` — the fields YOU sent that Airbnb dropped — and `blockedFields: []` is what
    a landed write looks like. `GET …/details` reports the same list as `lockedFields` so you can check
    first.

    Canonical property type (the value Repull keeps and republishes) is set with `PUT
    /v1/listings/{id}/content` under `details`; this endpoint writes straight to Airbnb.

    Send `Idempotency-Key` to make a retry safe.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbListingDetailsWriteRequest): Update what kind of property this is, when the
            quiet hours are, or how the guest gets in. At least one field required. These are among
            the attributes Airbnb locks on established listings — see `blockedFields` on the response.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbContentWriteResponse | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
