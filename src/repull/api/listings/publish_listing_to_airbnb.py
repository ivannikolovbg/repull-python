from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.listing_publish_airbnb_request import ListingPublishAirbnbRequest
from ...models.listing_publish_airbnb_response import ListingPublishAirbnbResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ListingPublishAirbnbRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/{id}/publish/airbnb".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListingPublishAirbnbResponse | None:
    if response.status_code == 200:
        response_200 = ListingPublishAirbnbResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListingPublishAirbnbResponse]:
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
    body: ListingPublishAirbnbRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | ListingPublishAirbnbResponse]:
    """ Publish a listing to Airbnb

     Push a Repull listing's canonical content to Airbnb. Pass `airbnbConnectionId` to update an already-
    mapped Airbnb listing, or `hostId` to create a brand-new Airbnb listing under that host.

    **A publish is not one call to Airbnb.** It is up to eight independent ones — details, description,
    amenities, rooms, policies, photos, pricing, checkout_tasks — and each can fail on its own.
    `result.published` is true only when every attempted section landed; `result.sections` lists the
    ones that did and `result.errors[]` carries Airbnb's own reason, per section, for the ones that did
    not. **A partial publish is normal and is not rolled back**: what succeeded stays applied. Publish
    again once you have fixed the failing sections — a re-publish of an unchanged section is harmless.

    `result.lockedFields` names the fields Airbnb will not let this listing change at all. They are not
    retryable by anyone: Airbnb answers 200 and applies nothing. `GET /v1/channels/airbnb/listings/{id}`
    reports the same list up front.

    **Which fields this pushes** — title, description sections and house rules (English/primary locale),
    amenities, rooms and beds, photos, nightly price and fees, cancellation policy and guest controls,
    check-in/out times, quiet hours, property and room type, checkout tasks. **Not pushed by this
    endpoint:** non-primary locales (`PUT /v1/channels/airbnb/listings/{id}/descriptions`), guest-safety
    disclosures (`PUT …/safety-disclosures`), check-in method (`PUT …/details`), permits (`PUT
    …/permits`), and the calendar (`PUT …/availability`).

    `force: true` re-pushes every section, ignoring dirty-field tracking. Without it only the sections
    changed since the last successful publish are sent.

    Send `Idempotency-Key` to make a retry safe: a timeout on a publish otherwise leaves you unable to
    tell whether it ran.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ListingPublishAirbnbRequest | Unset): Pass either `airbnbConnectionId` (update an
            already-mapped listing) or `hostId` (create a brand-new Airbnb listing under that host).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingPublishAirbnbResponse]
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
    body: ListingPublishAirbnbRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Error | ListingPublishAirbnbResponse | None:
    """ Publish a listing to Airbnb

     Push a Repull listing's canonical content to Airbnb. Pass `airbnbConnectionId` to update an already-
    mapped Airbnb listing, or `hostId` to create a brand-new Airbnb listing under that host.

    **A publish is not one call to Airbnb.** It is up to eight independent ones — details, description,
    amenities, rooms, policies, photos, pricing, checkout_tasks — and each can fail on its own.
    `result.published` is true only when every attempted section landed; `result.sections` lists the
    ones that did and `result.errors[]` carries Airbnb's own reason, per section, for the ones that did
    not. **A partial publish is normal and is not rolled back**: what succeeded stays applied. Publish
    again once you have fixed the failing sections — a re-publish of an unchanged section is harmless.

    `result.lockedFields` names the fields Airbnb will not let this listing change at all. They are not
    retryable by anyone: Airbnb answers 200 and applies nothing. `GET /v1/channels/airbnb/listings/{id}`
    reports the same list up front.

    **Which fields this pushes** — title, description sections and house rules (English/primary locale),
    amenities, rooms and beds, photos, nightly price and fees, cancellation policy and guest controls,
    check-in/out times, quiet hours, property and room type, checkout tasks. **Not pushed by this
    endpoint:** non-primary locales (`PUT /v1/channels/airbnb/listings/{id}/descriptions`), guest-safety
    disclosures (`PUT …/safety-disclosures`), check-in method (`PUT …/details`), permits (`PUT
    …/permits`), and the calendar (`PUT …/availability`).

    `force: true` re-pushes every section, ignoring dirty-field tracking. Without it only the sections
    changed since the last successful publish are sent.

    Send `Idempotency-Key` to make a retry safe: a timeout on a publish otherwise leaves you unable to
    tell whether it ran.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ListingPublishAirbnbRequest | Unset): Pass either `airbnbConnectionId` (update an
            already-mapped listing) or `hostId` (create a brand-new Airbnb listing under that host).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingPublishAirbnbResponse
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
    body: ListingPublishAirbnbRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | ListingPublishAirbnbResponse]:
    """ Publish a listing to Airbnb

     Push a Repull listing's canonical content to Airbnb. Pass `airbnbConnectionId` to update an already-
    mapped Airbnb listing, or `hostId` to create a brand-new Airbnb listing under that host.

    **A publish is not one call to Airbnb.** It is up to eight independent ones — details, description,
    amenities, rooms, policies, photos, pricing, checkout_tasks — and each can fail on its own.
    `result.published` is true only when every attempted section landed; `result.sections` lists the
    ones that did and `result.errors[]` carries Airbnb's own reason, per section, for the ones that did
    not. **A partial publish is normal and is not rolled back**: what succeeded stays applied. Publish
    again once you have fixed the failing sections — a re-publish of an unchanged section is harmless.

    `result.lockedFields` names the fields Airbnb will not let this listing change at all. They are not
    retryable by anyone: Airbnb answers 200 and applies nothing. `GET /v1/channels/airbnb/listings/{id}`
    reports the same list up front.

    **Which fields this pushes** — title, description sections and house rules (English/primary locale),
    amenities, rooms and beds, photos, nightly price and fees, cancellation policy and guest controls,
    check-in/out times, quiet hours, property and room type, checkout tasks. **Not pushed by this
    endpoint:** non-primary locales (`PUT /v1/channels/airbnb/listings/{id}/descriptions`), guest-safety
    disclosures (`PUT …/safety-disclosures`), check-in method (`PUT …/details`), permits (`PUT
    …/permits`), and the calendar (`PUT …/availability`).

    `force: true` re-pushes every section, ignoring dirty-field tracking. Without it only the sections
    changed since the last successful publish are sent.

    Send `Idempotency-Key` to make a retry safe: a timeout on a publish otherwise leaves you unable to
    tell whether it ran.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ListingPublishAirbnbRequest | Unset): Pass either `airbnbConnectionId` (update an
            already-mapped listing) or `hostId` (create a brand-new Airbnb listing under that host).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingPublishAirbnbResponse]
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
    body: ListingPublishAirbnbRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Error | ListingPublishAirbnbResponse | None:
    """ Publish a listing to Airbnb

     Push a Repull listing's canonical content to Airbnb. Pass `airbnbConnectionId` to update an already-
    mapped Airbnb listing, or `hostId` to create a brand-new Airbnb listing under that host.

    **A publish is not one call to Airbnb.** It is up to eight independent ones — details, description,
    amenities, rooms, policies, photos, pricing, checkout_tasks — and each can fail on its own.
    `result.published` is true only when every attempted section landed; `result.sections` lists the
    ones that did and `result.errors[]` carries Airbnb's own reason, per section, for the ones that did
    not. **A partial publish is normal and is not rolled back**: what succeeded stays applied. Publish
    again once you have fixed the failing sections — a re-publish of an unchanged section is harmless.

    `result.lockedFields` names the fields Airbnb will not let this listing change at all. They are not
    retryable by anyone: Airbnb answers 200 and applies nothing. `GET /v1/channels/airbnb/listings/{id}`
    reports the same list up front.

    **Which fields this pushes** — title, description sections and house rules (English/primary locale),
    amenities, rooms and beds, photos, nightly price and fees, cancellation policy and guest controls,
    check-in/out times, quiet hours, property and room type, checkout tasks. **Not pushed by this
    endpoint:** non-primary locales (`PUT /v1/channels/airbnb/listings/{id}/descriptions`), guest-safety
    disclosures (`PUT …/safety-disclosures`), check-in method (`PUT …/details`), permits (`PUT
    …/permits`), and the calendar (`PUT …/availability`).

    `force: true` re-pushes every section, ignoring dirty-field tracking. Without it only the sections
    changed since the last successful publish are sent.

    Send `Idempotency-Key` to make a retry safe: a timeout on a publish otherwise leaves you unable to
    tell whether it ran.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (ListingPublishAirbnbRequest | Unset): Pass either `airbnbConnectionId` (update an
            already-mapped listing) or `hostId` (create a brand-new Airbnb listing under that host).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingPublishAirbnbResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
