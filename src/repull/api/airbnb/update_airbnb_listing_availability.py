from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_availability_write_request import AirbnbAvailabilityWriteRequest
from ...models.error import Error
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: AirbnbAvailabilityWriteRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/airbnb/listings/{id}/availability".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
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
    body: AirbnbAvailabilityWriteRequest,

) -> Response[Any | Error]:
    r""" Update Airbnb availability

     Push availability + restrictions to Airbnb. `type: \"calendar\"` writes per-date restrictions —
    min/max nights, closed-to-arrival, closed-to-departure, and stop-sell (`availability:
    \"unavailable\"`) — via a batch of operations that each target either a date range or an explicit
    date list. `type: \"rules\"` writes listing-level availability rules (default min/max nights,
    booking lead time, turnover days, seasonal/day-of-week min nights). Restrictions never leak across
    channels — this endpoint writes only to Airbnb.

    `{id}` is the **Repull listing id** (from `GET /v1/properties` or `GET
    /v1/channels/airbnb/listings`), not the Airbnb listing id — Repull translates it before calling
    Airbnb.

    The body is validated before anything reaches Airbnb: a malformed body is `422 invalid_params`
    naming the `field`. Calendar operations accept only the documented fields.

    **Blocking dates:** Airbnb requires a `busy_subtype` whenever `availability` is `\"unavailable\"`.
    If an operation leaves it out, Repull sends `busy_subtype: \"BLOCKED_BY_HOST\"`; send
    `\"OUTSIDE_RESERVATION\"` for dates held by a booking made on another channel.

    **Errors:** `403 listing_not_api_connected` — Airbnb was never told to sync this listing (its
    `syncCategory` is `none`); the host must switch API sync on for it in Airbnb, reconnecting the
    account will not help. `403 connection_reauth_required` — Airbnb no longer accepts the connection at
    all (reconnect; retrying won't help). `403 listing_inactive` — the listing is inactive. `404
    not_found` — no Airbnb-connected listing with this id in the workspace. `422 airbnb_rejected` —
    Airbnb refused the change; `message` carries its reason. `429 airbnb_rate_limited` — back off. `502
    airbnb_error` — Airbnb outage or timeout; retry.

    Args:
        id (str):
        body (AirbnbAvailabilityWriteRequest): Body for `PUT
            /v1/channels/airbnb/listings/{id}/availability`. `type: "calendar"` carries per-date
            restrictions (min/max nights, closed-to-arrival/departure, stop-sell); `type: "rules"`
            carries listing-level availability rules (default min/max nights, booking lead time,
            turnover days).

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
    body: AirbnbAvailabilityWriteRequest,

) -> Any | Error | None:
    r""" Update Airbnb availability

     Push availability + restrictions to Airbnb. `type: \"calendar\"` writes per-date restrictions —
    min/max nights, closed-to-arrival, closed-to-departure, and stop-sell (`availability:
    \"unavailable\"`) — via a batch of operations that each target either a date range or an explicit
    date list. `type: \"rules\"` writes listing-level availability rules (default min/max nights,
    booking lead time, turnover days, seasonal/day-of-week min nights). Restrictions never leak across
    channels — this endpoint writes only to Airbnb.

    `{id}` is the **Repull listing id** (from `GET /v1/properties` or `GET
    /v1/channels/airbnb/listings`), not the Airbnb listing id — Repull translates it before calling
    Airbnb.

    The body is validated before anything reaches Airbnb: a malformed body is `422 invalid_params`
    naming the `field`. Calendar operations accept only the documented fields.

    **Blocking dates:** Airbnb requires a `busy_subtype` whenever `availability` is `\"unavailable\"`.
    If an operation leaves it out, Repull sends `busy_subtype: \"BLOCKED_BY_HOST\"`; send
    `\"OUTSIDE_RESERVATION\"` for dates held by a booking made on another channel.

    **Errors:** `403 listing_not_api_connected` — Airbnb was never told to sync this listing (its
    `syncCategory` is `none`); the host must switch API sync on for it in Airbnb, reconnecting the
    account will not help. `403 connection_reauth_required` — Airbnb no longer accepts the connection at
    all (reconnect; retrying won't help). `403 listing_inactive` — the listing is inactive. `404
    not_found` — no Airbnb-connected listing with this id in the workspace. `422 airbnb_rejected` —
    Airbnb refused the change; `message` carries its reason. `429 airbnb_rate_limited` — back off. `502
    airbnb_error` — Airbnb outage or timeout; retry.

    Args:
        id (str):
        body (AirbnbAvailabilityWriteRequest): Body for `PUT
            /v1/channels/airbnb/listings/{id}/availability`. `type: "calendar"` carries per-date
            restrictions (min/max nights, closed-to-arrival/departure, stop-sell); `type: "rules"`
            carries listing-level availability rules (default min/max nights, booking lead time,
            turnover days).

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
    body: AirbnbAvailabilityWriteRequest,

) -> Response[Any | Error]:
    r""" Update Airbnb availability

     Push availability + restrictions to Airbnb. `type: \"calendar\"` writes per-date restrictions —
    min/max nights, closed-to-arrival, closed-to-departure, and stop-sell (`availability:
    \"unavailable\"`) — via a batch of operations that each target either a date range or an explicit
    date list. `type: \"rules\"` writes listing-level availability rules (default min/max nights,
    booking lead time, turnover days, seasonal/day-of-week min nights). Restrictions never leak across
    channels — this endpoint writes only to Airbnb.

    `{id}` is the **Repull listing id** (from `GET /v1/properties` or `GET
    /v1/channels/airbnb/listings`), not the Airbnb listing id — Repull translates it before calling
    Airbnb.

    The body is validated before anything reaches Airbnb: a malformed body is `422 invalid_params`
    naming the `field`. Calendar operations accept only the documented fields.

    **Blocking dates:** Airbnb requires a `busy_subtype` whenever `availability` is `\"unavailable\"`.
    If an operation leaves it out, Repull sends `busy_subtype: \"BLOCKED_BY_HOST\"`; send
    `\"OUTSIDE_RESERVATION\"` for dates held by a booking made on another channel.

    **Errors:** `403 listing_not_api_connected` — Airbnb was never told to sync this listing (its
    `syncCategory` is `none`); the host must switch API sync on for it in Airbnb, reconnecting the
    account will not help. `403 connection_reauth_required` — Airbnb no longer accepts the connection at
    all (reconnect; retrying won't help). `403 listing_inactive` — the listing is inactive. `404
    not_found` — no Airbnb-connected listing with this id in the workspace. `422 airbnb_rejected` —
    Airbnb refused the change; `message` carries its reason. `429 airbnb_rate_limited` — back off. `502
    airbnb_error` — Airbnb outage or timeout; retry.

    Args:
        id (str):
        body (AirbnbAvailabilityWriteRequest): Body for `PUT
            /v1/channels/airbnb/listings/{id}/availability`. `type: "calendar"` carries per-date
            restrictions (min/max nights, closed-to-arrival/departure, stop-sell); `type: "rules"`
            carries listing-level availability rules (default min/max nights, booking lead time,
            turnover days).

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
    body: AirbnbAvailabilityWriteRequest,

) -> Any | Error | None:
    r""" Update Airbnb availability

     Push availability + restrictions to Airbnb. `type: \"calendar\"` writes per-date restrictions —
    min/max nights, closed-to-arrival, closed-to-departure, and stop-sell (`availability:
    \"unavailable\"`) — via a batch of operations that each target either a date range or an explicit
    date list. `type: \"rules\"` writes listing-level availability rules (default min/max nights,
    booking lead time, turnover days, seasonal/day-of-week min nights). Restrictions never leak across
    channels — this endpoint writes only to Airbnb.

    `{id}` is the **Repull listing id** (from `GET /v1/properties` or `GET
    /v1/channels/airbnb/listings`), not the Airbnb listing id — Repull translates it before calling
    Airbnb.

    The body is validated before anything reaches Airbnb: a malformed body is `422 invalid_params`
    naming the `field`. Calendar operations accept only the documented fields.

    **Blocking dates:** Airbnb requires a `busy_subtype` whenever `availability` is `\"unavailable\"`.
    If an operation leaves it out, Repull sends `busy_subtype: \"BLOCKED_BY_HOST\"`; send
    `\"OUTSIDE_RESERVATION\"` for dates held by a booking made on another channel.

    **Errors:** `403 listing_not_api_connected` — Airbnb was never told to sync this listing (its
    `syncCategory` is `none`); the host must switch API sync on for it in Airbnb, reconnecting the
    account will not help. `403 connection_reauth_required` — Airbnb no longer accepts the connection at
    all (reconnect; retrying won't help). `403 listing_inactive` — the listing is inactive. `404
    not_found` — no Airbnb-connected listing with this id in the workspace. `422 airbnb_rejected` —
    Airbnb refused the change; `message` carries its reason. `429 airbnb_rate_limited` — back off. `502
    airbnb_error` — Airbnb outage or timeout; retry.

    Args:
        id (str):
        body (AirbnbAvailabilityWriteRequest): Body for `PUT
            /v1/channels/airbnb/listings/{id}/availability`. `type: "calendar"` carries per-date
            restrictions (min/max nights, closed-to-arrival/departure, stop-sell); `type: "rules"`
            carries listing-level availability rules (default min/max nights, booking lead time,
            turnover days).

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
