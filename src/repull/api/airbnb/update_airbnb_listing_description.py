from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_content_write_response import AirbnbContentWriteResponse
from ...models.airbnb_description_write_request import AirbnbDescriptionWriteRequest
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: AirbnbDescriptionWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/airbnb/listings/{id}/descriptions".format(id=quote(str(id), safe=""),),
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
    body: AirbnbDescriptionWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[AirbnbContentWriteResponse | Error]:
    r""" Update an Airbnb description for one locale

     Write one locale's copy to the live Airbnb listing.

    Airbnb keeps a SEPARATE description per locale (`PUT
    /v2/listing_descriptions/{listingId}/{locale}`), which is why `locale` is part of the request and
    not a guess: a listing can carry twelve of them, and writing Italian copy into the English row is
    how a translation gets lost. Only the fields you send are written; Airbnb keeps the rest. `GET
    /v1/channels/airbnb/listings/{id}/settings?type=locales` lists the locales already synced for the
    listing.

    `description` is not an accepted field: Airbnb composes the public description from the sections
    (`summary`, `space`, `access`, …) and ignores a directly-supplied one.

    **A 200 does not by itself mean the change was applied.** On an established listing Airbnb LOCKS
    host-managed description fields — the write returns 200, reports them as locked, and applies nothing
    for them. The response reports `blockedFields`: the fields YOU sent that Airbnb dropped.
    `blockedFields: []` is what a landed write looks like; a non-empty list is still a 200 (the other
    fields really were written) with a `message` naming what was not. Reporting that as a clean success
    is the bug behind \"the description does not push to Airbnb\".

    This writes to AIRBNB. To write Repull's own canonical copy — the content a later publish
    distributes — use `PUT /v1/listings/{id}/content` with `locale`.

    Send `Idempotency-Key` to make a retry safe.

    Returns `403 listing_inactive` when the listing is inactive.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbDescriptionWriteRequest): Write one locale's copy. Airbnb keeps a separate
            description per locale, which is why the locale is explicit: writing Italian copy into the
            English row is how a translation gets lost. Only the fields you send are written.

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
    body: AirbnbDescriptionWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> AirbnbContentWriteResponse | Error | None:
    r""" Update an Airbnb description for one locale

     Write one locale's copy to the live Airbnb listing.

    Airbnb keeps a SEPARATE description per locale (`PUT
    /v2/listing_descriptions/{listingId}/{locale}`), which is why `locale` is part of the request and
    not a guess: a listing can carry twelve of them, and writing Italian copy into the English row is
    how a translation gets lost. Only the fields you send are written; Airbnb keeps the rest. `GET
    /v1/channels/airbnb/listings/{id}/settings?type=locales` lists the locales already synced for the
    listing.

    `description` is not an accepted field: Airbnb composes the public description from the sections
    (`summary`, `space`, `access`, …) and ignores a directly-supplied one.

    **A 200 does not by itself mean the change was applied.** On an established listing Airbnb LOCKS
    host-managed description fields — the write returns 200, reports them as locked, and applies nothing
    for them. The response reports `blockedFields`: the fields YOU sent that Airbnb dropped.
    `blockedFields: []` is what a landed write looks like; a non-empty list is still a 200 (the other
    fields really were written) with a `message` naming what was not. Reporting that as a clean success
    is the bug behind \"the description does not push to Airbnb\".

    This writes to AIRBNB. To write Repull's own canonical copy — the content a later publish
    distributes — use `PUT /v1/listings/{id}/content` with `locale`.

    Send `Idempotency-Key` to make a retry safe.

    Returns `403 listing_inactive` when the listing is inactive.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbDescriptionWriteRequest): Write one locale's copy. Airbnb keeps a separate
            description per locale, which is why the locale is explicit: writing Italian copy into the
            English row is how a translation gets lost. Only the fields you send are written.

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
    body: AirbnbDescriptionWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[AirbnbContentWriteResponse | Error]:
    r""" Update an Airbnb description for one locale

     Write one locale's copy to the live Airbnb listing.

    Airbnb keeps a SEPARATE description per locale (`PUT
    /v2/listing_descriptions/{listingId}/{locale}`), which is why `locale` is part of the request and
    not a guess: a listing can carry twelve of them, and writing Italian copy into the English row is
    how a translation gets lost. Only the fields you send are written; Airbnb keeps the rest. `GET
    /v1/channels/airbnb/listings/{id}/settings?type=locales` lists the locales already synced for the
    listing.

    `description` is not an accepted field: Airbnb composes the public description from the sections
    (`summary`, `space`, `access`, …) and ignores a directly-supplied one.

    **A 200 does not by itself mean the change was applied.** On an established listing Airbnb LOCKS
    host-managed description fields — the write returns 200, reports them as locked, and applies nothing
    for them. The response reports `blockedFields`: the fields YOU sent that Airbnb dropped.
    `blockedFields: []` is what a landed write looks like; a non-empty list is still a 200 (the other
    fields really were written) with a `message` naming what was not. Reporting that as a clean success
    is the bug behind \"the description does not push to Airbnb\".

    This writes to AIRBNB. To write Repull's own canonical copy — the content a later publish
    distributes — use `PUT /v1/listings/{id}/content` with `locale`.

    Send `Idempotency-Key` to make a retry safe.

    Returns `403 listing_inactive` when the listing is inactive.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbDescriptionWriteRequest): Write one locale's copy. Airbnb keeps a separate
            description per locale, which is why the locale is explicit: writing Italian copy into the
            English row is how a translation gets lost. Only the fields you send are written.

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
    body: AirbnbDescriptionWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> AirbnbContentWriteResponse | Error | None:
    r""" Update an Airbnb description for one locale

     Write one locale's copy to the live Airbnb listing.

    Airbnb keeps a SEPARATE description per locale (`PUT
    /v2/listing_descriptions/{listingId}/{locale}`), which is why `locale` is part of the request and
    not a guess: a listing can carry twelve of them, and writing Italian copy into the English row is
    how a translation gets lost. Only the fields you send are written; Airbnb keeps the rest. `GET
    /v1/channels/airbnb/listings/{id}/settings?type=locales` lists the locales already synced for the
    listing.

    `description` is not an accepted field: Airbnb composes the public description from the sections
    (`summary`, `space`, `access`, …) and ignores a directly-supplied one.

    **A 200 does not by itself mean the change was applied.** On an established listing Airbnb LOCKS
    host-managed description fields — the write returns 200, reports them as locked, and applies nothing
    for them. The response reports `blockedFields`: the fields YOU sent that Airbnb dropped.
    `blockedFields: []` is what a landed write looks like; a non-empty list is still a 200 (the other
    fields really were written) with a `message` naming what was not. Reporting that as a clean success
    is the bug behind \"the description does not push to Airbnb\".

    This writes to AIRBNB. To write Repull's own canonical copy — the content a later publish
    distributes — use `PUT /v1/listings/{id}/content` with `locale`.

    Send `Idempotency-Key` to make a retry safe.

    Returns `403 listing_inactive` when the listing is inactive.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbDescriptionWriteRequest): Write one locale's copy. Airbnb keeps a separate
            description per locale, which is why the locale is explicit: writing Italian copy into the
            English row is how a translation gets lost. Only the fields you send are written.

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
