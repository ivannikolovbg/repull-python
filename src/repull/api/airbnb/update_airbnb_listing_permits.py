from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_permits_write_request import AirbnbPermitsWriteRequest
from ...models.error import Error
from ...models.update_airbnb_listing_permits_response_200 import UpdateAirbnbListingPermitsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: AirbnbPermitsWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key



    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/airbnb/listings/{id}/permits".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | UpdateAirbnbListingPermitsResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateAirbnbListingPermitsResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | UpdateAirbnbListingPermitsResponse200]:
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
    body: AirbnbPermitsWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | UpdateAirbnbListingPermitsResponse200]:
    r""" Answer Airbnb permit questions

     Answer the regulatory permit questions for a listing — the licence or registration number a city
    requires to keep the listing up.

    Read the questions first with `GET …/permits?source=live`: every answer is keyed by a `question_key`
    Airbnb asks for THIS listing, and the question's `answer_type` decides which value field applies
    (`text_value`, `date_value`, or `selected_options_value`). Answers are forwarded verbatim — nothing
    is defaulted or inferred, because a wrong licence number can take a listing down in a regulated
    city.

    Send `Idempotency-Key`: a timeout here leaves you unable to tell \"never arrived\" from \"arrived,
    response lost\", and this is a compliance filing.

    Airbnb refusing the answers (an unknown question key, a malformed licence number) is `422
    airbnb_rejected` carrying Airbnb's own reason. An expired or revoked Airbnb connection is `403
    connection_reauth_required`.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbPermitsWriteRequest): Answer the regulatory permit questions Airbnb asks for
            this listing. Read them first with `?source=live` on the GET — Airbnb refuses a
            `question_key` it did not ask for on this listing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbListingPermitsResponse200]
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
    body: AirbnbPermitsWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> Error | UpdateAirbnbListingPermitsResponse200 | None:
    r""" Answer Airbnb permit questions

     Answer the regulatory permit questions for a listing — the licence or registration number a city
    requires to keep the listing up.

    Read the questions first with `GET …/permits?source=live`: every answer is keyed by a `question_key`
    Airbnb asks for THIS listing, and the question's `answer_type` decides which value field applies
    (`text_value`, `date_value`, or `selected_options_value`). Answers are forwarded verbatim — nothing
    is defaulted or inferred, because a wrong licence number can take a listing down in a regulated
    city.

    Send `Idempotency-Key`: a timeout here leaves you unable to tell \"never arrived\" from \"arrived,
    response lost\", and this is a compliance filing.

    Airbnb refusing the answers (an unknown question key, a malformed licence number) is `422
    airbnb_rejected` carrying Airbnb's own reason. An expired or revoked Airbnb connection is `403
    connection_reauth_required`.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbPermitsWriteRequest): Answer the regulatory permit questions Airbnb asks for
            this listing. Read them first with `?source=live` on the GET — Airbnb refuses a
            `question_key` it did not ask for on this listing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbListingPermitsResponse200
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
    body: AirbnbPermitsWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> Response[Error | UpdateAirbnbListingPermitsResponse200]:
    r""" Answer Airbnb permit questions

     Answer the regulatory permit questions for a listing — the licence or registration number a city
    requires to keep the listing up.

    Read the questions first with `GET …/permits?source=live`: every answer is keyed by a `question_key`
    Airbnb asks for THIS listing, and the question's `answer_type` decides which value field applies
    (`text_value`, `date_value`, or `selected_options_value`). Answers are forwarded verbatim — nothing
    is defaulted or inferred, because a wrong licence number can take a listing down in a regulated
    city.

    Send `Idempotency-Key`: a timeout here leaves you unable to tell \"never arrived\" from \"arrived,
    response lost\", and this is a compliance filing.

    Airbnb refusing the answers (an unknown question key, a malformed licence number) is `422
    airbnb_rejected` carrying Airbnb's own reason. An expired or revoked Airbnb connection is `403
    connection_reauth_required`.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbPermitsWriteRequest): Answer the regulatory permit questions Airbnb asks for
            this listing. Read them first with `?source=live` on the GET — Airbnb refuses a
            `question_key` it did not ask for on this listing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateAirbnbListingPermitsResponse200]
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
    body: AirbnbPermitsWriteRequest,
    idempotency_key: str | Unset = UNSET,

) -> Error | UpdateAirbnbListingPermitsResponse200 | None:
    r""" Answer Airbnb permit questions

     Answer the regulatory permit questions for a listing — the licence or registration number a city
    requires to keep the listing up.

    Read the questions first with `GET …/permits?source=live`: every answer is keyed by a `question_key`
    Airbnb asks for THIS listing, and the question's `answer_type` decides which value field applies
    (`text_value`, `date_value`, or `selected_options_value`). Answers are forwarded verbatim — nothing
    is defaulted or inferred, because a wrong licence number can take a listing down in a regulated
    city.

    Send `Idempotency-Key`: a timeout here leaves you unable to tell \"never arrived\" from \"arrived,
    response lost\", and this is a compliance filing.

    Airbnb refusing the answers (an unknown question key, a malformed licence number) is `422
    airbnb_rejected` carrying Airbnb's own reason. An expired or revoked Airbnb connection is `403
    connection_reauth_required`.

    Args:
        id (str):
        idempotency_key (str | Unset):  Example: 9f1c2f7e-4a3b-4f2e-9c8d-1b6a0e5d7c31.
        body (AirbnbPermitsWriteRequest): Answer the regulatory permit questions Airbnb asks for
            this listing. Read them first with `?source=live` on the GET — Airbnb refuses a
            `question_key` it did not ask for on this listing.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateAirbnbListingPermitsResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
idempotency_key=idempotency_key,

    )).parsed
