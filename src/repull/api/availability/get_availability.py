from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.property_availability import PropertyAvailability
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    property_id: int,
    *,
    from_: datetime.date,
    to: datetime.date,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/availability/{property_id}".format(property_id=quote(str(property_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | PropertyAvailability | None:
    if response.status_code == 200:
        response_200 = PropertyAvailability.from_dict(response.json())



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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | PropertyAvailability]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    property_id: int,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date,
    to: datetime.date,

) -> Response[Error | PropertyAvailability]:
    """ Get property availability

     Channel-agnostic day-by-day availability calendar for a property over a date window. Returns a thin
    per-date shape — `{ date, available, price, minNights }` — projected from the property calendar.

    The `from` and `to` query params are **required** (ISO `YYYY-MM-DD`, inclusive) — omitting or
    malforming either returns 422. The window is capped at 366 days; longer ranges are truncated to the
    first 366 days.

    **`days` contains only the dates we actually hold calendar data for.** Requested dates with no
    calendar row are listed in `coverage.missingDates` — their availability is unknown. Never treat a
    missing date as bookable: this endpoint deliberately does not synthesise availability, because a
    fabricated open date can be double-booked. A property with no calendar still returns a real 200
    (`days: []`, every date in `coverage.missingDates`), never a 404 — 404 means the property id does
    not exist or belongs to a different workspace.

    This endpoint is read-only, and the projected per-date shape carries **availability, price, and min-
    nights only** — it does NOT expose max-stay, closed-to-arrival (CTA), closed-to-departure (CTD), or
    the dedicated stop-sell flag. To read or write that full restriction set on Booking.com use the
    channel routes: `GET`/`PUT /v1/channels/booking/availability` (with the room + rate ids from `GET
    /v1/channels/booking/properties/{id}/rooms`). To **write** calendar values use `PUT
    /v1/availability/{propertyId}` (or `PATCH /v1/availability/batch`), which updates the property
    calendar and pushes to its connected channels; channel-only settings stay on the channel routes.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        property_id (int):
        from_ (datetime.date):
        to (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PropertyAvailability]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
from_=from_,
to=to,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    property_id: int,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date,
    to: datetime.date,

) -> Error | PropertyAvailability | None:
    """ Get property availability

     Channel-agnostic day-by-day availability calendar for a property over a date window. Returns a thin
    per-date shape — `{ date, available, price, minNights }` — projected from the property calendar.

    The `from` and `to` query params are **required** (ISO `YYYY-MM-DD`, inclusive) — omitting or
    malforming either returns 422. The window is capped at 366 days; longer ranges are truncated to the
    first 366 days.

    **`days` contains only the dates we actually hold calendar data for.** Requested dates with no
    calendar row are listed in `coverage.missingDates` — their availability is unknown. Never treat a
    missing date as bookable: this endpoint deliberately does not synthesise availability, because a
    fabricated open date can be double-booked. A property with no calendar still returns a real 200
    (`days: []`, every date in `coverage.missingDates`), never a 404 — 404 means the property id does
    not exist or belongs to a different workspace.

    This endpoint is read-only, and the projected per-date shape carries **availability, price, and min-
    nights only** — it does NOT expose max-stay, closed-to-arrival (CTA), closed-to-departure (CTD), or
    the dedicated stop-sell flag. To read or write that full restriction set on Booking.com use the
    channel routes: `GET`/`PUT /v1/channels/booking/availability` (with the room + rate ids from `GET
    /v1/channels/booking/properties/{id}/rooms`). To **write** calendar values use `PUT
    /v1/availability/{propertyId}` (or `PATCH /v1/availability/batch`), which updates the property
    calendar and pushes to its connected channels; channel-only settings stay on the channel routes.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        property_id (int):
        from_ (datetime.date):
        to (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PropertyAvailability
     """


    return sync_detailed(
        property_id=property_id,
client=client,
from_=from_,
to=to,

    ).parsed

async def asyncio_detailed(
    property_id: int,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date,
    to: datetime.date,

) -> Response[Error | PropertyAvailability]:
    """ Get property availability

     Channel-agnostic day-by-day availability calendar for a property over a date window. Returns a thin
    per-date shape — `{ date, available, price, minNights }` — projected from the property calendar.

    The `from` and `to` query params are **required** (ISO `YYYY-MM-DD`, inclusive) — omitting or
    malforming either returns 422. The window is capped at 366 days; longer ranges are truncated to the
    first 366 days.

    **`days` contains only the dates we actually hold calendar data for.** Requested dates with no
    calendar row are listed in `coverage.missingDates` — their availability is unknown. Never treat a
    missing date as bookable: this endpoint deliberately does not synthesise availability, because a
    fabricated open date can be double-booked. A property with no calendar still returns a real 200
    (`days: []`, every date in `coverage.missingDates`), never a 404 — 404 means the property id does
    not exist or belongs to a different workspace.

    This endpoint is read-only, and the projected per-date shape carries **availability, price, and min-
    nights only** — it does NOT expose max-stay, closed-to-arrival (CTA), closed-to-departure (CTD), or
    the dedicated stop-sell flag. To read or write that full restriction set on Booking.com use the
    channel routes: `GET`/`PUT /v1/channels/booking/availability` (with the room + rate ids from `GET
    /v1/channels/booking/properties/{id}/rooms`). To **write** calendar values use `PUT
    /v1/availability/{propertyId}` (or `PATCH /v1/availability/batch`), which updates the property
    calendar and pushes to its connected channels; channel-only settings stay on the channel routes.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        property_id (int):
        from_ (datetime.date):
        to (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PropertyAvailability]
     """


    kwargs = _get_kwargs(
        property_id=property_id,
from_=from_,
to=to,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    property_id: int,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.date,
    to: datetime.date,

) -> Error | PropertyAvailability | None:
    """ Get property availability

     Channel-agnostic day-by-day availability calendar for a property over a date window. Returns a thin
    per-date shape — `{ date, available, price, minNights }` — projected from the property calendar.

    The `from` and `to` query params are **required** (ISO `YYYY-MM-DD`, inclusive) — omitting or
    malforming either returns 422. The window is capped at 366 days; longer ranges are truncated to the
    first 366 days.

    **`days` contains only the dates we actually hold calendar data for.** Requested dates with no
    calendar row are listed in `coverage.missingDates` — their availability is unknown. Never treat a
    missing date as bookable: this endpoint deliberately does not synthesise availability, because a
    fabricated open date can be double-booked. A property with no calendar still returns a real 200
    (`days: []`, every date in `coverage.missingDates`), never a 404 — 404 means the property id does
    not exist or belongs to a different workspace.

    This endpoint is read-only, and the projected per-date shape carries **availability, price, and min-
    nights only** — it does NOT expose max-stay, closed-to-arrival (CTA), closed-to-departure (CTD), or
    the dedicated stop-sell flag. To read or write that full restriction set on Booking.com use the
    channel routes: `GET`/`PUT /v1/channels/booking/availability` (with the room + rate ids from `GET
    /v1/channels/booking/properties/{id}/rooms`). To **write** calendar values use `PUT
    /v1/availability/{propertyId}` (or `PATCH /v1/availability/batch`), which updates the property
    calendar and pushes to its connected channels; channel-only settings stay on the channel routes.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        property_id (int):
        from_ (datetime.date):
        to (datetime.date):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PropertyAvailability
     """


    return (await asyncio_detailed(
        property_id=property_id,
client=client,
from_=from_,
to=to,

    )).parsed
