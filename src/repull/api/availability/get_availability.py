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
    per-date shape — `{ date, available, price, minNights }` — projected from the connected channel
    calendar (currently Airbnb).

    The `from` and `to` query params are **required** (ISO `YYYY-MM-DD`, inclusive) — omitting or
    malforming either returns 422. The window is capped at 366 days; longer ranges are truncated to the
    first 366 days.

    Every date in the window is present in `days`: dates with no explicit calendar row fall back to
    `available: true` at the property's default nightly price. A property with no channel calendar still
    returns a real 200 (a fully-default calendar), never a 404 — 404 means the property id does not
    exist or belongs to a different workspace.

    This endpoint is read-only. Availability **writes** stay per-channel: `PUT
    /v1/channels/airbnb/listings/{id}/availability` (Airbnb) or `PUT /v1/channels/booking/availability`
    (Booking.com).

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
    per-date shape — `{ date, available, price, minNights }` — projected from the connected channel
    calendar (currently Airbnb).

    The `from` and `to` query params are **required** (ISO `YYYY-MM-DD`, inclusive) — omitting or
    malforming either returns 422. The window is capped at 366 days; longer ranges are truncated to the
    first 366 days.

    Every date in the window is present in `days`: dates with no explicit calendar row fall back to
    `available: true` at the property's default nightly price. A property with no channel calendar still
    returns a real 200 (a fully-default calendar), never a 404 — 404 means the property id does not
    exist or belongs to a different workspace.

    This endpoint is read-only. Availability **writes** stay per-channel: `PUT
    /v1/channels/airbnb/listings/{id}/availability` (Airbnb) or `PUT /v1/channels/booking/availability`
    (Booking.com).

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
    per-date shape — `{ date, available, price, minNights }` — projected from the connected channel
    calendar (currently Airbnb).

    The `from` and `to` query params are **required** (ISO `YYYY-MM-DD`, inclusive) — omitting or
    malforming either returns 422. The window is capped at 366 days; longer ranges are truncated to the
    first 366 days.

    Every date in the window is present in `days`: dates with no explicit calendar row fall back to
    `available: true` at the property's default nightly price. A property with no channel calendar still
    returns a real 200 (a fully-default calendar), never a 404 — 404 means the property id does not
    exist or belongs to a different workspace.

    This endpoint is read-only. Availability **writes** stay per-channel: `PUT
    /v1/channels/airbnb/listings/{id}/availability` (Airbnb) or `PUT /v1/channels/booking/availability`
    (Booking.com).

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
    per-date shape — `{ date, available, price, minNights }` — projected from the connected channel
    calendar (currently Airbnb).

    The `from` and `to` query params are **required** (ISO `YYYY-MM-DD`, inclusive) — omitting or
    malforming either returns 422. The window is capped at 366 days; longer ranges are truncated to the
    first 366 days.

    Every date in the window is present in `days`: dates with no explicit calendar row fall back to
    `available: true` at the property's default nightly price. A property with no channel calendar still
    returns a real 200 (a fully-default calendar), never a 404 — 404 means the property id does not
    exist or belongs to a different workspace.

    This endpoint is read-only. Availability **writes** stay per-channel: `PUT
    /v1/channels/airbnb/listings/{id}/availability` (Airbnb) or `PUT /v1/channels/booking/availability`
    (Booking.com).

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
