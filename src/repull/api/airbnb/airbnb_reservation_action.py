from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_reservation_action_body import AirbnbReservationActionBody
from ...models.airbnb_reservation_action_response_200 import AirbnbReservationActionResponse200
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    code: str,
    *,
    body: AirbnbReservationActionBody,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/airbnb/reservations/{code}".format(code=quote(str(code), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AirbnbReservationActionResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = AirbnbReservationActionResponse200.from_dict(response.json())



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

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AirbnbReservationActionResponse200 | Error]:
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
    body: AirbnbReservationActionBody,
    idempotency_key: str | Unset = UNSET,

) -> Response[AirbnbReservationActionResponse200 | Error]:
    """ Accept, decline or cancel an Airbnb reservation

     Act on an Airbnb reservation by its Airbnb confirmation code. **Write-side** — calls Airbnb
    upstream, as the Airbnb account that owns the booking.

    - `accept` — accept a pending booking request.
    - `decline` — decline a pending booking request. Requires `reason` (one of Airbnb's decline reasons)
    and `message` (sent to the guest, at most 500 characters).
    - `cancel` — cancel a confirmed booking as the host. Requires `reason` (one of Airbnb's host-
    cancellation reasons). **Host cancellations carry Airbnb penalties.**

    The body is validated before anything reaches Airbnb; unknown fields are refused. There is no `pre-
    approve` action: a pre-approval answers an inquiry, which has no confirmation code — use `POST
    /v1/conversations/{id}/pre-approval`. For accept/decline, `POST /v1/reservations/{id}/accept` and
    `/decline` do the same by Repull id and also update Vanio.

    Airbnb refusals are mapped rather than returned as a 500: a request that already moved on is `409
    request_no_longer_pending` (do not retry), an expired one `409 request_expired`, any other refusal
    `422 airbnb_rejected` with Airbnb's reason.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Send `Idempotency-Key` to make a retry safe.

    Args:
        code (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbReservationActionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbReservationActionResponse200 | Error]
     """


    kwargs = _get_kwargs(
        code=code,
body=body,
idempotency_key=idempotency_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    code: str,
    *,
    client: AuthenticatedClient | Client,
    body: AirbnbReservationActionBody,
    idempotency_key: str | Unset = UNSET,

) -> AirbnbReservationActionResponse200 | Error | None:
    """ Accept, decline or cancel an Airbnb reservation

     Act on an Airbnb reservation by its Airbnb confirmation code. **Write-side** — calls Airbnb
    upstream, as the Airbnb account that owns the booking.

    - `accept` — accept a pending booking request.
    - `decline` — decline a pending booking request. Requires `reason` (one of Airbnb's decline reasons)
    and `message` (sent to the guest, at most 500 characters).
    - `cancel` — cancel a confirmed booking as the host. Requires `reason` (one of Airbnb's host-
    cancellation reasons). **Host cancellations carry Airbnb penalties.**

    The body is validated before anything reaches Airbnb; unknown fields are refused. There is no `pre-
    approve` action: a pre-approval answers an inquiry, which has no confirmation code — use `POST
    /v1/conversations/{id}/pre-approval`. For accept/decline, `POST /v1/reservations/{id}/accept` and
    `/decline` do the same by Repull id and also update Vanio.

    Airbnb refusals are mapped rather than returned as a 500: a request that already moved on is `409
    request_no_longer_pending` (do not retry), an expired one `409 request_expired`, any other refusal
    `422 airbnb_rejected` with Airbnb's reason.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Send `Idempotency-Key` to make a retry safe.

    Args:
        code (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbReservationActionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbReservationActionResponse200 | Error
     """


    return sync_detailed(
        code=code,
client=client,
body=body,
idempotency_key=idempotency_key,

    ).parsed

async def asyncio_detailed(
    code: str,
    *,
    client: AuthenticatedClient | Client,
    body: AirbnbReservationActionBody,
    idempotency_key: str | Unset = UNSET,

) -> Response[AirbnbReservationActionResponse200 | Error]:
    """ Accept, decline or cancel an Airbnb reservation

     Act on an Airbnb reservation by its Airbnb confirmation code. **Write-side** — calls Airbnb
    upstream, as the Airbnb account that owns the booking.

    - `accept` — accept a pending booking request.
    - `decline` — decline a pending booking request. Requires `reason` (one of Airbnb's decline reasons)
    and `message` (sent to the guest, at most 500 characters).
    - `cancel` — cancel a confirmed booking as the host. Requires `reason` (one of Airbnb's host-
    cancellation reasons). **Host cancellations carry Airbnb penalties.**

    The body is validated before anything reaches Airbnb; unknown fields are refused. There is no `pre-
    approve` action: a pre-approval answers an inquiry, which has no confirmation code — use `POST
    /v1/conversations/{id}/pre-approval`. For accept/decline, `POST /v1/reservations/{id}/accept` and
    `/decline` do the same by Repull id and also update Vanio.

    Airbnb refusals are mapped rather than returned as a 500: a request that already moved on is `409
    request_no_longer_pending` (do not retry), an expired one `409 request_expired`, any other refusal
    `422 airbnb_rejected` with Airbnb's reason.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Send `Idempotency-Key` to make a retry safe.

    Args:
        code (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbReservationActionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AirbnbReservationActionResponse200 | Error]
     """


    kwargs = _get_kwargs(
        code=code,
body=body,
idempotency_key=idempotency_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    code: str,
    *,
    client: AuthenticatedClient | Client,
    body: AirbnbReservationActionBody,
    idempotency_key: str | Unset = UNSET,

) -> AirbnbReservationActionResponse200 | Error | None:
    """ Accept, decline or cancel an Airbnb reservation

     Act on an Airbnb reservation by its Airbnb confirmation code. **Write-side** — calls Airbnb
    upstream, as the Airbnb account that owns the booking.

    - `accept` — accept a pending booking request.
    - `decline` — decline a pending booking request. Requires `reason` (one of Airbnb's decline reasons)
    and `message` (sent to the guest, at most 500 characters).
    - `cancel` — cancel a confirmed booking as the host. Requires `reason` (one of Airbnb's host-
    cancellation reasons). **Host cancellations carry Airbnb penalties.**

    The body is validated before anything reaches Airbnb; unknown fields are refused. There is no `pre-
    approve` action: a pre-approval answers an inquiry, which has no confirmation code — use `POST
    /v1/conversations/{id}/pre-approval`. For accept/decline, `POST /v1/reservations/{id}/accept` and
    `/decline` do the same by Repull id and also update Vanio.

    Airbnb refusals are mapped rather than returned as a 500: a request that already moved on is `409
    request_no_longer_pending` (do not retry), an expired one `409 request_expired`, any other refusal
    `422 airbnb_rejected` with Airbnb's reason.

    Returns `403 listing_inactive` when the listing this resolves to is inactive. An inactive listing
    keeps syncing, but cannot be read or changed through the API until it is activated.

    Send `Idempotency-Key` to make a retry safe.

    Args:
        code (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbReservationActionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AirbnbReservationActionResponse200 | Error
     """


    return (await asyncio_detailed(
        code=code,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
