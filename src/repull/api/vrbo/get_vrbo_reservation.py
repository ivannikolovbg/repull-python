from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.get_vrbo_reservation_options import GetVrboReservationOptions
from ...models.get_vrbo_reservation_response_200 import GetVrboReservationResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    code: str,
    *,
    options: GetVrboReservationOptions | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_options: str | Unset = UNSET
    if not isinstance(options, Unset):
        json_options = options.value

    params["options"] = json_options


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/vrbo/reservations/{code}".format(code=quote(str(code), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | GetVrboReservationResponse200 | None:
    if response.status_code == 200:
        response_200 = GetVrboReservationResponse200.from_dict(response.json())



        return response_200

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

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | GetVrboReservationResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    code: str,
    *,
    client: AuthenticatedClient | Client,
    options: GetVrboReservationOptions | Unset = UNSET,

) -> Response[Error | GetVrboReservationResponse200]:
    r""" Get a Vrbo reservation

     A Vrbo booking by its confirmation code, as Vrbo shows it now — the counterpart of `GET
    /v1/channels/airbnb/reservations/{code}`: its state (`Booked`, a request, …), dates, party, the
    guest's charges (`guestLines`), your deductions and payout (`hostLines`, `payout`), the cancellation
    policy and the damage deposit, plus `availableActions` — what Vrbo's \"Change or cancel the
    booking\" menu offers right now.

    `?options=cancel|change|decline` returns Vrbo's choices for that action instead: the cancel reasons
    and message limits; the booking's current dates, times and party with Vrbo's limits (e.g. a pay-
    later booking's check-in is locked); or the decline reasons of a booking request. Read live from
    Vrbo (a few seconds).

    Args:
        code (str):  Example: HA-8K2P3Q.
        options (GetVrboReservationOptions | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboReservationResponse200]
     """


    kwargs = _get_kwargs(
        code=code,
options=options,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    code: str,
    *,
    client: AuthenticatedClient | Client,
    options: GetVrboReservationOptions | Unset = UNSET,

) -> Error | GetVrboReservationResponse200 | None:
    r""" Get a Vrbo reservation

     A Vrbo booking by its confirmation code, as Vrbo shows it now — the counterpart of `GET
    /v1/channels/airbnb/reservations/{code}`: its state (`Booked`, a request, …), dates, party, the
    guest's charges (`guestLines`), your deductions and payout (`hostLines`, `payout`), the cancellation
    policy and the damage deposit, plus `availableActions` — what Vrbo's \"Change or cancel the
    booking\" menu offers right now.

    `?options=cancel|change|decline` returns Vrbo's choices for that action instead: the cancel reasons
    and message limits; the booking's current dates, times and party with Vrbo's limits (e.g. a pay-
    later booking's check-in is locked); or the decline reasons of a booking request. Read live from
    Vrbo (a few seconds).

    Args:
        code (str):  Example: HA-8K2P3Q.
        options (GetVrboReservationOptions | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboReservationResponse200
     """


    return sync_detailed(
        code=code,
client=client,
options=options,

    ).parsed

async def asyncio_detailed(
    code: str,
    *,
    client: AuthenticatedClient | Client,
    options: GetVrboReservationOptions | Unset = UNSET,

) -> Response[Error | GetVrboReservationResponse200]:
    r""" Get a Vrbo reservation

     A Vrbo booking by its confirmation code, as Vrbo shows it now — the counterpart of `GET
    /v1/channels/airbnb/reservations/{code}`: its state (`Booked`, a request, …), dates, party, the
    guest's charges (`guestLines`), your deductions and payout (`hostLines`, `payout`), the cancellation
    policy and the damage deposit, plus `availableActions` — what Vrbo's \"Change or cancel the
    booking\" menu offers right now.

    `?options=cancel|change|decline` returns Vrbo's choices for that action instead: the cancel reasons
    and message limits; the booking's current dates, times and party with Vrbo's limits (e.g. a pay-
    later booking's check-in is locked); or the decline reasons of a booking request. Read live from
    Vrbo (a few seconds).

    Args:
        code (str):  Example: HA-8K2P3Q.
        options (GetVrboReservationOptions | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | GetVrboReservationResponse200]
     """


    kwargs = _get_kwargs(
        code=code,
options=options,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    code: str,
    *,
    client: AuthenticatedClient | Client,
    options: GetVrboReservationOptions | Unset = UNSET,

) -> Error | GetVrboReservationResponse200 | None:
    r""" Get a Vrbo reservation

     A Vrbo booking by its confirmation code, as Vrbo shows it now — the counterpart of `GET
    /v1/channels/airbnb/reservations/{code}`: its state (`Booked`, a request, …), dates, party, the
    guest's charges (`guestLines`), your deductions and payout (`hostLines`, `payout`), the cancellation
    policy and the damage deposit, plus `availableActions` — what Vrbo's \"Change or cancel the
    booking\" menu offers right now.

    `?options=cancel|change|decline` returns Vrbo's choices for that action instead: the cancel reasons
    and message limits; the booking's current dates, times and party with Vrbo's limits (e.g. a pay-
    later booking's check-in is locked); or the decline reasons of a booking request. Read live from
    Vrbo (a few seconds).

    Args:
        code (str):  Example: HA-8K2P3Q.
        options (GetVrboReservationOptions | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | GetVrboReservationResponse200
     """


    return (await asyncio_detailed(
        code=code,
client=client,
options=options,

    )).parsed
