from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.accept_reservation_request_response_200 import AcceptReservationRequestResponse200
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/reservations/{id}/accept".format(id=quote(str(id), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AcceptReservationRequestResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = AcceptReservationRequestResponse200.from_dict(response.json())



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

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AcceptReservationRequestResponse200 | Error]:
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
    idempotency_key: str | Unset = UNSET,

) -> Response[AcceptReservationRequestResponse200 | Error]:
    """ Accept a booking request

     Accept a pending Airbnb booking request — a reservation with status `pending`, made on a listing
    without Instant Book. Find them with `GET /v1/reservations?status=pending`. Airbnb expires a request
    the host has not answered within 24 hours.

    Runs the same action as the Vanio dashboard’s Accept button. Airbnb confirms asynchronously: the
    reservation’s status moves to confirmed, and a `reservation.updated` webhook fires, when Airbnb’s
    notification lands (usually within seconds). The response reports what Airbnb was asked to do.

    **Airbnb only**, and only for listings connected to Airbnb directly: other channels have no request
    step (`422 channel_not_supported`). A reservation that is not pending is refused before Airbnb is
    contacted (`409 reservation_not_pending`); one Airbnb says already moved on is `409
    request_no_longer_pending`. Neither is worth retrying.

    Takes no body.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcceptReservationRequestResponse200 | Error]
     """


    kwargs = _get_kwargs(
        id=id,
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
    idempotency_key: str | Unset = UNSET,

) -> AcceptReservationRequestResponse200 | Error | None:
    """ Accept a booking request

     Accept a pending Airbnb booking request — a reservation with status `pending`, made on a listing
    without Instant Book. Find them with `GET /v1/reservations?status=pending`. Airbnb expires a request
    the host has not answered within 24 hours.

    Runs the same action as the Vanio dashboard’s Accept button. Airbnb confirms asynchronously: the
    reservation’s status moves to confirmed, and a `reservation.updated` webhook fires, when Airbnb’s
    notification lands (usually within seconds). The response reports what Airbnb was asked to do.

    **Airbnb only**, and only for listings connected to Airbnb directly: other channels have no request
    step (`422 channel_not_supported`). A reservation that is not pending is refused before Airbnb is
    contacted (`409 reservation_not_pending`); one Airbnb says already moved on is `409
    request_no_longer_pending`. Neither is worth retrying.

    Takes no body.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcceptReservationRequestResponse200 | Error
     """


    return sync_detailed(
        id=id,
client=client,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    idempotency_key: str | Unset = UNSET,

) -> Response[AcceptReservationRequestResponse200 | Error]:
    """ Accept a booking request

     Accept a pending Airbnb booking request — a reservation with status `pending`, made on a listing
    without Instant Book. Find them with `GET /v1/reservations?status=pending`. Airbnb expires a request
    the host has not answered within 24 hours.

    Runs the same action as the Vanio dashboard’s Accept button. Airbnb confirms asynchronously: the
    reservation’s status moves to confirmed, and a `reservation.updated` webhook fires, when Airbnb’s
    notification lands (usually within seconds). The response reports what Airbnb was asked to do.

    **Airbnb only**, and only for listings connected to Airbnb directly: other channels have no request
    step (`422 channel_not_supported`). A reservation that is not pending is refused before Airbnb is
    contacted (`409 reservation_not_pending`); one Airbnb says already moved on is `409
    request_no_longer_pending`. Neither is worth retrying.

    Takes no body.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AcceptReservationRequestResponse200 | Error]
     """


    kwargs = _get_kwargs(
        id=id,
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
    idempotency_key: str | Unset = UNSET,

) -> AcceptReservationRequestResponse200 | Error | None:
    """ Accept a booking request

     Accept a pending Airbnb booking request — a reservation with status `pending`, made on a listing
    without Instant Book. Find them with `GET /v1/reservations?status=pending`. Airbnb expires a request
    the host has not answered within 24 hours.

    Runs the same action as the Vanio dashboard’s Accept button. Airbnb confirms asynchronously: the
    reservation’s status moves to confirmed, and a `reservation.updated` webhook fires, when Airbnb’s
    notification lands (usually within seconds). The response reports what Airbnb was asked to do.

    **Airbnb only**, and only for listings connected to Airbnb directly: other channels have no request
    step (`422 channel_not_supported`). A reservation that is not pending is refused before Airbnb is
    contacted (`409 reservation_not_pending`); one Airbnb says already moved on is `409
    request_no_longer_pending`. Neither is worth retrying.

    Takes no body.

    Send `Idempotency-Key`: a repeat with the same key replays the first response instead of acting
    twice (a `409 idempotency_key_in_use` while the first is still running). A 5xx, a `429
    airbnb_rate_limited` or a `403 connection_reauth_required` is not stored — nothing was done — so
    retrying with the same key reaches Airbnb again.

    Args:
        id (int):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AcceptReservationRequestResponse200 | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
idempotency_key=idempotency_key,

    )).parsed
