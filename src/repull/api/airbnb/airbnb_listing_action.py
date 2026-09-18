from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_listing_action_request import AirbnbListingActionRequest
from ...models.airbnb_listing_action_response_200_type_0 import AirbnbListingActionResponse200Type0
from ...models.airbnb_listing_action_response_200_type_1 import AirbnbListingActionResponse200Type1
from ...models.airbnb_listing_lifecycle_response import AirbnbListingLifecycleResponse
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: AirbnbListingActionRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/airbnb/listings/{id}".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AirbnbListingActionResponse200Type0 | AirbnbListingActionResponse200Type1 | AirbnbListingLifecycleResponse | Error | None:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> AirbnbListingActionResponse200Type0 | AirbnbListingActionResponse200Type1 | AirbnbListingLifecycleResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = AirbnbListingActionResponse200Type0.from_dict(data)



                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = AirbnbListingActionResponse200Type1.from_dict(data)



                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = AirbnbListingLifecycleResponse.from_dict(data)



            return response_200_type_2

        response_200 = _parse_response_200(response.json())

        return response_200

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

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AirbnbListingActionResponse200Type0 | AirbnbListingActionResponse200Type1 | AirbnbListingLifecycleResponse | Error]:
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
    body: AirbnbListingActionRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[AirbnbListingActionResponse200Type0 | AirbnbListingActionResponse200Type1 | AirbnbListingLifecycleResponse | Error]:
    r""" Listing action (delete/push/publish/unlist/relist)

     Apply a state action to a listing by id. The path `id` is the canonical Repull listing id.

    **Deactivating in Repull and unlisting on Airbnb are different operations.**

    `delete` is a **deactivate of the Repull record only** — it sets the listing inactive and KEEPS the
    row; it does NOT touch the Airbnb listing, which stays live and keeps taking bookings. Use it to
    exclude a listing from the API / trim back under the plan-listings cap; reactivate via `PATCH
    /v1/listings/{id}` with `{ \"active\": true }`. Idempotent.

    `unlist` calls Airbnb and **takes the live listing down**: it is deactivated with a valid
    deactivation reason and then READ BACK, so \"Airbnb accepted the call but the listing is still
    live\" is reported as a failure rather than a success. Requires `airbnbConnectionId` — a listing can
    be connected to more than one Airbnb listing, and taking down the wrong one is not undoable through
    this API. `relist` puts it back up (re-enables sync and makes the listing available again); it does
    not push content.

    `push` / `publish` push the listing's content to Airbnb via the same host-side sync orchestrator as
    `POST /v1/listings/{id}/publish/airbnb` — pass `airbnbConnectionId` to update an already-mapped
    Airbnb listing, or `hostId` to create + publish a new one under that host. `force` re-pushes every
    field, ignoring dirty-field tracking. The result is per-section: see `AirbnbPublishResult`.

    Any other action (e.g. `pull`) returns a structured 422 naming the supported actions.

    Returns `403 listing_inactive` for `push`/`publish`/`unlist`/`relist` when the listing is inactive.
    `delete` (deactivation) is always accepted.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbListingActionRequest | Unset): Body for `POST
            /v1/channels/airbnb/listings/{id}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbListingActionResponse200Type0 | AirbnbListingActionResponse200Type1 | AirbnbListingLifecycleResponse | Error]
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
    body: AirbnbListingActionRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> AirbnbListingActionResponse200Type0 | AirbnbListingActionResponse200Type1 | AirbnbListingLifecycleResponse | Error | None:
    r""" Listing action (delete/push/publish/unlist/relist)

     Apply a state action to a listing by id. The path `id` is the canonical Repull listing id.

    **Deactivating in Repull and unlisting on Airbnb are different operations.**

    `delete` is a **deactivate of the Repull record only** — it sets the listing inactive and KEEPS the
    row; it does NOT touch the Airbnb listing, which stays live and keeps taking bookings. Use it to
    exclude a listing from the API / trim back under the plan-listings cap; reactivate via `PATCH
    /v1/listings/{id}` with `{ \"active\": true }`. Idempotent.

    `unlist` calls Airbnb and **takes the live listing down**: it is deactivated with a valid
    deactivation reason and then READ BACK, so \"Airbnb accepted the call but the listing is still
    live\" is reported as a failure rather than a success. Requires `airbnbConnectionId` — a listing can
    be connected to more than one Airbnb listing, and taking down the wrong one is not undoable through
    this API. `relist` puts it back up (re-enables sync and makes the listing available again); it does
    not push content.

    `push` / `publish` push the listing's content to Airbnb via the same host-side sync orchestrator as
    `POST /v1/listings/{id}/publish/airbnb` — pass `airbnbConnectionId` to update an already-mapped
    Airbnb listing, or `hostId` to create + publish a new one under that host. `force` re-pushes every
    field, ignoring dirty-field tracking. The result is per-section: see `AirbnbPublishResult`.

    Any other action (e.g. `pull`) returns a structured 422 naming the supported actions.

    Returns `403 listing_inactive` for `push`/`publish`/`unlist`/`relist` when the listing is inactive.
    `delete` (deactivation) is always accepted.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbListingActionRequest | Unset): Body for `POST
            /v1/channels/airbnb/listings/{id}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbListingActionResponse200Type0 | AirbnbListingActionResponse200Type1 | AirbnbListingLifecycleResponse | Error
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
    body: AirbnbListingActionRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> Response[AirbnbListingActionResponse200Type0 | AirbnbListingActionResponse200Type1 | AirbnbListingLifecycleResponse | Error]:
    r""" Listing action (delete/push/publish/unlist/relist)

     Apply a state action to a listing by id. The path `id` is the canonical Repull listing id.

    **Deactivating in Repull and unlisting on Airbnb are different operations.**

    `delete` is a **deactivate of the Repull record only** — it sets the listing inactive and KEEPS the
    row; it does NOT touch the Airbnb listing, which stays live and keeps taking bookings. Use it to
    exclude a listing from the API / trim back under the plan-listings cap; reactivate via `PATCH
    /v1/listings/{id}` with `{ \"active\": true }`. Idempotent.

    `unlist` calls Airbnb and **takes the live listing down**: it is deactivated with a valid
    deactivation reason and then READ BACK, so \"Airbnb accepted the call but the listing is still
    live\" is reported as a failure rather than a success. Requires `airbnbConnectionId` — a listing can
    be connected to more than one Airbnb listing, and taking down the wrong one is not undoable through
    this API. `relist` puts it back up (re-enables sync and makes the listing available again); it does
    not push content.

    `push` / `publish` push the listing's content to Airbnb via the same host-side sync orchestrator as
    `POST /v1/listings/{id}/publish/airbnb` — pass `airbnbConnectionId` to update an already-mapped
    Airbnb listing, or `hostId` to create + publish a new one under that host. `force` re-pushes every
    field, ignoring dirty-field tracking. The result is per-section: see `AirbnbPublishResult`.

    Any other action (e.g. `pull`) returns a structured 422 naming the supported actions.

    Returns `403 listing_inactive` for `push`/`publish`/`unlist`/`relist` when the listing is inactive.
    `delete` (deactivation) is always accepted.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbListingActionRequest | Unset): Body for `POST
            /v1/channels/airbnb/listings/{id}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbListingActionResponse200Type0 | AirbnbListingActionResponse200Type1 | AirbnbListingLifecycleResponse | Error]
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
    body: AirbnbListingActionRequest | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,

) -> AirbnbListingActionResponse200Type0 | AirbnbListingActionResponse200Type1 | AirbnbListingLifecycleResponse | Error | None:
    r""" Listing action (delete/push/publish/unlist/relist)

     Apply a state action to a listing by id. The path `id` is the canonical Repull listing id.

    **Deactivating in Repull and unlisting on Airbnb are different operations.**

    `delete` is a **deactivate of the Repull record only** — it sets the listing inactive and KEEPS the
    row; it does NOT touch the Airbnb listing, which stays live and keeps taking bookings. Use it to
    exclude a listing from the API / trim back under the plan-listings cap; reactivate via `PATCH
    /v1/listings/{id}` with `{ \"active\": true }`. Idempotent.

    `unlist` calls Airbnb and **takes the live listing down**: it is deactivated with a valid
    deactivation reason and then READ BACK, so \"Airbnb accepted the call but the listing is still
    live\" is reported as a failure rather than a success. Requires `airbnbConnectionId` — a listing can
    be connected to more than one Airbnb listing, and taking down the wrong one is not undoable through
    this API. `relist` puts it back up (re-enables sync and makes the listing available again); it does
    not push content.

    `push` / `publish` push the listing's content to Airbnb via the same host-side sync orchestrator as
    `POST /v1/listings/{id}/publish/airbnb` — pass `airbnbConnectionId` to update an already-mapped
    Airbnb listing, or `hostId` to create + publish a new one under that host. `force` re-pushes every
    field, ignoring dirty-field tracking. The result is per-section: see `AirbnbPublishResult`.

    Any other action (e.g. `pull`) returns a structured 422 naming the supported actions.

    Returns `403 listing_inactive` for `push`/`publish`/`unlist`/`relist` when the listing is inactive.
    `delete` (deactivation) is always accepted.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbListingActionRequest | Unset): Body for `POST
            /v1/channels/airbnb/listings/{id}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbListingActionResponse200Type0 | AirbnbListingActionResponse200Type1 | AirbnbListingLifecycleResponse | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
