from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.update_airbnb_booking_settings_body import UpdateAirbnbBookingSettingsBody
from ...models.update_airbnb_booking_settings_response_200 import UpdateAirbnbBookingSettingsResponse200
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: UpdateAirbnbBookingSettingsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/airbnb/listings/{id}/booking-settings".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | UpdateAirbnbBookingSettingsResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateAirbnbBookingSettingsResponse200.from_dict(response.json())



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

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | UpdateAirbnbBookingSettingsResponse200]:
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
    body: UpdateAirbnbBookingSettingsBody,

) -> Response[Error | UpdateAirbnbBookingSettingsResponse200]:
    """ Update Airbnb booking settings

     Set any subset of a listing's booking settings on Airbnb. Partial — a field you do not send is left
    as it is.

    `{id}` is the **Repull listing id** (from `GET /v1/properties` or `GET
    /v1/channels/airbnb/listings`), not the Airbnb listing id; Repull translates it before calling
    Airbnb.

    The body is validated before anything reaches Airbnb, so a bad value is a `422` naming the field
    rather than a failed upstream call. Unknown fields are refused rather than dropped.

    **Two groups, applied in order.** Instant Book, check-in/out and the cancellation fields go to
    Airbnb's booking-settings resource. Advance notice, preparation time and booking window go to
    Airbnb's availability rules — Airbnb replaces that whole document, so Repull reads the current rules
    first and merges your change onto them, which is why setting a preparation time does not blank the
    listing's min/max nights. The response's `applied` array names the groups that were written.

    **Non-refundable is a percentage here, a factor on Airbnb.** Airbnb stores
    `non_refundable_price_factor` between 0.7 and 1.0; send `cancellation.nonRefundable.discountPercent`
    (0-30) and Repull converts — 10% becomes 0.9. `enabled: false` sets the factor to 1.0.

    **Not exposed by Airbnb:** `preReservationMessage` and `automaticStayExtension`. Sending either
    returns a `422` explaining where to set it instead.

    **Errors:** `403 connection_reauth_required` — Airbnb no longer accepts the connection for this
    listing (reconnect; retrying won't help). `403 listing_inactive` — the listing is inactive. `404
    not_found` — no Airbnb-connected listing with this id in the workspace. `422 invalid_params` — the
    body is wrong; `field` names it. `422 airbnb_rejected` — Airbnb refused the change; `message`
    carries its reason. `429 airbnb_rate_limited` — back off. `502 airbnb_error` — Airbnb outage or
    timeout; retry.

    Args:
        id (str):
        body (UpdateAirbnbBookingSettingsBody): Partial update — a field you do not send is left
            as it is. Unknown fields are refused with `422`, so a typo can never be silently dropped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbBookingSettingsResponse200]
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
    body: UpdateAirbnbBookingSettingsBody,

) -> Error | UpdateAirbnbBookingSettingsResponse200 | None:
    """ Update Airbnb booking settings

     Set any subset of a listing's booking settings on Airbnb. Partial — a field you do not send is left
    as it is.

    `{id}` is the **Repull listing id** (from `GET /v1/properties` or `GET
    /v1/channels/airbnb/listings`), not the Airbnb listing id; Repull translates it before calling
    Airbnb.

    The body is validated before anything reaches Airbnb, so a bad value is a `422` naming the field
    rather than a failed upstream call. Unknown fields are refused rather than dropped.

    **Two groups, applied in order.** Instant Book, check-in/out and the cancellation fields go to
    Airbnb's booking-settings resource. Advance notice, preparation time and booking window go to
    Airbnb's availability rules — Airbnb replaces that whole document, so Repull reads the current rules
    first and merges your change onto them, which is why setting a preparation time does not blank the
    listing's min/max nights. The response's `applied` array names the groups that were written.

    **Non-refundable is a percentage here, a factor on Airbnb.** Airbnb stores
    `non_refundable_price_factor` between 0.7 and 1.0; send `cancellation.nonRefundable.discountPercent`
    (0-30) and Repull converts — 10% becomes 0.9. `enabled: false` sets the factor to 1.0.

    **Not exposed by Airbnb:** `preReservationMessage` and `automaticStayExtension`. Sending either
    returns a `422` explaining where to set it instead.

    **Errors:** `403 connection_reauth_required` — Airbnb no longer accepts the connection for this
    listing (reconnect; retrying won't help). `403 listing_inactive` — the listing is inactive. `404
    not_found` — no Airbnb-connected listing with this id in the workspace. `422 invalid_params` — the
    body is wrong; `field` names it. `422 airbnb_rejected` — Airbnb refused the change; `message`
    carries its reason. `429 airbnb_rate_limited` — back off. `502 airbnb_error` — Airbnb outage or
    timeout; retry.

    Args:
        id (str):
        body (UpdateAirbnbBookingSettingsBody): Partial update — a field you do not send is left
            as it is. Unknown fields are refused with `422`, so a typo can never be silently dropped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbBookingSettingsResponse200
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
    body: UpdateAirbnbBookingSettingsBody,

) -> Response[Error | UpdateAirbnbBookingSettingsResponse200]:
    """ Update Airbnb booking settings

     Set any subset of a listing's booking settings on Airbnb. Partial — a field you do not send is left
    as it is.

    `{id}` is the **Repull listing id** (from `GET /v1/properties` or `GET
    /v1/channels/airbnb/listings`), not the Airbnb listing id; Repull translates it before calling
    Airbnb.

    The body is validated before anything reaches Airbnb, so a bad value is a `422` naming the field
    rather than a failed upstream call. Unknown fields are refused rather than dropped.

    **Two groups, applied in order.** Instant Book, check-in/out and the cancellation fields go to
    Airbnb's booking-settings resource. Advance notice, preparation time and booking window go to
    Airbnb's availability rules — Airbnb replaces that whole document, so Repull reads the current rules
    first and merges your change onto them, which is why setting a preparation time does not blank the
    listing's min/max nights. The response's `applied` array names the groups that were written.

    **Non-refundable is a percentage here, a factor on Airbnb.** Airbnb stores
    `non_refundable_price_factor` between 0.7 and 1.0; send `cancellation.nonRefundable.discountPercent`
    (0-30) and Repull converts — 10% becomes 0.9. `enabled: false` sets the factor to 1.0.

    **Not exposed by Airbnb:** `preReservationMessage` and `automaticStayExtension`. Sending either
    returns a `422` explaining where to set it instead.

    **Errors:** `403 connection_reauth_required` — Airbnb no longer accepts the connection for this
    listing (reconnect; retrying won't help). `403 listing_inactive` — the listing is inactive. `404
    not_found` — no Airbnb-connected listing with this id in the workspace. `422 invalid_params` — the
    body is wrong; `field` names it. `422 airbnb_rejected` — Airbnb refused the change; `message`
    carries its reason. `429 airbnb_rate_limited` — back off. `502 airbnb_error` — Airbnb outage or
    timeout; retry.

    Args:
        id (str):
        body (UpdateAirbnbBookingSettingsBody): Partial update — a field you do not send is left
            as it is. Unknown fields are refused with `422`, so a typo can never be silently dropped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbBookingSettingsResponse200]
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
    body: UpdateAirbnbBookingSettingsBody,

) -> Error | UpdateAirbnbBookingSettingsResponse200 | None:
    """ Update Airbnb booking settings

     Set any subset of a listing's booking settings on Airbnb. Partial — a field you do not send is left
    as it is.

    `{id}` is the **Repull listing id** (from `GET /v1/properties` or `GET
    /v1/channels/airbnb/listings`), not the Airbnb listing id; Repull translates it before calling
    Airbnb.

    The body is validated before anything reaches Airbnb, so a bad value is a `422` naming the field
    rather than a failed upstream call. Unknown fields are refused rather than dropped.

    **Two groups, applied in order.** Instant Book, check-in/out and the cancellation fields go to
    Airbnb's booking-settings resource. Advance notice, preparation time and booking window go to
    Airbnb's availability rules — Airbnb replaces that whole document, so Repull reads the current rules
    first and merges your change onto them, which is why setting a preparation time does not blank the
    listing's min/max nights. The response's `applied` array names the groups that were written.

    **Non-refundable is a percentage here, a factor on Airbnb.** Airbnb stores
    `non_refundable_price_factor` between 0.7 and 1.0; send `cancellation.nonRefundable.discountPercent`
    (0-30) and Repull converts — 10% becomes 0.9. `enabled: false` sets the factor to 1.0.

    **Not exposed by Airbnb:** `preReservationMessage` and `automaticStayExtension`. Sending either
    returns a `422` explaining where to set it instead.

    **Errors:** `403 connection_reauth_required` — Airbnb no longer accepts the connection for this
    listing (reconnect; retrying won't help). `403 listing_inactive` — the listing is inactive. `404
    not_found` — no Airbnb-connected listing with this id in the workspace. `422 invalid_params` — the
    body is wrong; `field` names it. `422 airbnb_rejected` — Airbnb refused the change; `message`
    carries its reason. `429 airbnb_rate_limited` — back off. `502 airbnb_error` — Airbnb outage or
    timeout; retry.

    Args:
        id (str):
        body (UpdateAirbnbBookingSettingsBody): Partial update — a field you do not send is left
            as it is. Unknown fields are refused with `422`, so a typo can never be silently dropped.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbBookingSettingsResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
