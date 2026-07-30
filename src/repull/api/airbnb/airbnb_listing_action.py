from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_listing_action_request import AirbnbListingActionRequest
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: AirbnbListingActionRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/airbnb/listings/{id}".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error]:
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

) -> Response[Any | Error]:
    r""" Listing action (delete/push/publish)

     Apply a state action to a listing by id. The path `id` is the canonical Repull listing id.

    `delete` is a **deactivate of the Repull record only** — it sets the listing inactive and KEEPS the
    row; it does NOT touch the upstream Airbnb listing (Repull never deletes or deactivates on Airbnb's
    side). Use it to exclude a listing / trim back under the plan-listings cap; reactivate via `PATCH
    /v1/listings/{id}` with `{ \"active\": true }`. Idempotent.

    `push` / `publish` push the listing's content to Airbnb via the same host-side sync orchestrator as
    `POST /v1/listings/{id}/publish/airbnb` — pass `airbnbConnectionId` to update an already-mapped
    Airbnb listing, or `hostId` to create + publish a new one under that host. `force` re-pushes every
    field, ignoring dirty-field tracking.

    Any other action (e.g. `pull`, `unlist`) returns a structured 422 naming the supported actions.

    Args:
        id (str):
        body (AirbnbListingActionRequest | Unset): Body for `POST
            /v1/channels/airbnb/listings/{id}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

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

) -> Any | Error | None:
    r""" Listing action (delete/push/publish)

     Apply a state action to a listing by id. The path `id` is the canonical Repull listing id.

    `delete` is a **deactivate of the Repull record only** — it sets the listing inactive and KEEPS the
    row; it does NOT touch the upstream Airbnb listing (Repull never deletes or deactivates on Airbnb's
    side). Use it to exclude a listing / trim back under the plan-listings cap; reactivate via `PATCH
    /v1/listings/{id}` with `{ \"active\": true }`. Idempotent.

    `push` / `publish` push the listing's content to Airbnb via the same host-side sync orchestrator as
    `POST /v1/listings/{id}/publish/airbnb` — pass `airbnbConnectionId` to update an already-mapped
    Airbnb listing, or `hostId` to create + publish a new one under that host. `force` re-pushes every
    field, ignoring dirty-field tracking.

    Any other action (e.g. `pull`, `unlist`) returns a structured 422 naming the supported actions.

    Args:
        id (str):
        body (AirbnbListingActionRequest | Unset): Body for `POST
            /v1/channels/airbnb/listings/{id}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AirbnbListingActionRequest | Unset = UNSET,

) -> Response[Any | Error]:
    r""" Listing action (delete/push/publish)

     Apply a state action to a listing by id. The path `id` is the canonical Repull listing id.

    `delete` is a **deactivate of the Repull record only** — it sets the listing inactive and KEEPS the
    row; it does NOT touch the upstream Airbnb listing (Repull never deletes or deactivates on Airbnb's
    side). Use it to exclude a listing / trim back under the plan-listings cap; reactivate via `PATCH
    /v1/listings/{id}` with `{ \"active\": true }`. Idempotent.

    `push` / `publish` push the listing's content to Airbnb via the same host-side sync orchestrator as
    `POST /v1/listings/{id}/publish/airbnb` — pass `airbnbConnectionId` to update an already-mapped
    Airbnb listing, or `hostId` to create + publish a new one under that host. `force` re-pushes every
    field, ignoring dirty-field tracking.

    Any other action (e.g. `pull`, `unlist`) returns a structured 422 naming the supported actions.

    Args:
        id (str):
        body (AirbnbListingActionRequest | Unset): Body for `POST
            /v1/channels/airbnb/listings/{id}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

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

) -> Any | Error | None:
    r""" Listing action (delete/push/publish)

     Apply a state action to a listing by id. The path `id` is the canonical Repull listing id.

    `delete` is a **deactivate of the Repull record only** — it sets the listing inactive and KEEPS the
    row; it does NOT touch the upstream Airbnb listing (Repull never deletes or deactivates on Airbnb's
    side). Use it to exclude a listing / trim back under the plan-listings cap; reactivate via `PATCH
    /v1/listings/{id}` with `{ \"active\": true }`. Idempotent.

    `push` / `publish` push the listing's content to Airbnb via the same host-side sync orchestrator as
    `POST /v1/listings/{id}/publish/airbnb` — pass `airbnbConnectionId` to update an already-mapped
    Airbnb listing, or `hostId` to create + publish a new one under that host. `force` re-pushes every
    field, ignoring dirty-field tracking.

    Any other action (e.g. `pull`, `unlist`) returns a structured 422 naming the supported actions.

    Args:
        id (str):
        body (AirbnbListingActionRequest | Unset): Body for `POST
            /v1/channels/airbnb/listings/{id}`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
