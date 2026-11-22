from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_vrbo_offer_body import CreateVrboOfferBody
from ...models.create_vrbo_offer_response_201_type_0 import CreateVrboOfferResponse201Type0
from ...models.create_vrbo_offer_response_201_type_1 import CreateVrboOfferResponse201Type1
from ...models.error import Error
from typing import cast



def _get_kwargs(
    *,
    body: CreateVrboOfferBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/vrbo/offers",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CreateVrboOfferResponse201Type0 | CreateVrboOfferResponse201Type1 | Error | None:
    if response.status_code == 201:
        def _parse_response_201(data: object) -> CreateVrboOfferResponse201Type0 | CreateVrboOfferResponse201Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0 = CreateVrboOfferResponse201Type0.from_dict(data)



                return response_201_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_201_type_1 = CreateVrboOfferResponse201Type1.from_dict(data)



            return response_201_type_1

        response_201 = _parse_response_201(response.json())

        return response_201

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

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CreateVrboOfferResponse201Type0 | CreateVrboOfferResponse201Type1 | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateVrboOfferBody,

) -> Response[CreateVrboOfferResponse201Type0 | CreateVrboOfferResponse201Type1 | Error]:
    r""" Pre-approve or quote a Vrbo inquiry

     Answer a Vrbo inquiry — the counterpart of `POST /v1/channels/airbnb/offers`, the same body
    addressed by the Vrbo conversation. `type: \"preapproval\"` invites the guest to book their dates at
    the listed price; `type: \"offer\"` sends Vrbo's edited quote.

    **Priced by its parts, not a total.** Vrbo adds its taxes and service fee itself, so a quote takes
    `rental_amount`, `fees` (`[{ type, value }]`, Vrbo fee types such as `CLEANING`, `PET`) and
    `damage_deposit`; `total_price` is refused. The stay is `start_date` + `nights` and `guest_details`,
    as on Airbnb; leave them out to keep the guest's own. Both types may carry a `message` to the guest.
    Vrbo has no instant-book switch on a pre-approval (`block_instant_booking` is refused) and a quote
    is always for the conversation's property (`listing_id` is refused).

    The same as `POST /v1/conversations/{id}/pre-approval` and `/special-offers` on a Vrbo conversation,
    which take the Repull conversation id. Send `Idempotency-Key`: a retry without it can send the guest
    two quotes. Returns `403 listing_inactive` when the conversation's listing is inactive.

    Args:
        body (CreateVrboOfferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateVrboOfferResponse201Type0 | CreateVrboOfferResponse201Type1 | Error]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: CreateVrboOfferBody,

) -> CreateVrboOfferResponse201Type0 | CreateVrboOfferResponse201Type1 | Error | None:
    r""" Pre-approve or quote a Vrbo inquiry

     Answer a Vrbo inquiry — the counterpart of `POST /v1/channels/airbnb/offers`, the same body
    addressed by the Vrbo conversation. `type: \"preapproval\"` invites the guest to book their dates at
    the listed price; `type: \"offer\"` sends Vrbo's edited quote.

    **Priced by its parts, not a total.** Vrbo adds its taxes and service fee itself, so a quote takes
    `rental_amount`, `fees` (`[{ type, value }]`, Vrbo fee types such as `CLEANING`, `PET`) and
    `damage_deposit`; `total_price` is refused. The stay is `start_date` + `nights` and `guest_details`,
    as on Airbnb; leave them out to keep the guest's own. Both types may carry a `message` to the guest.
    Vrbo has no instant-book switch on a pre-approval (`block_instant_booking` is refused) and a quote
    is always for the conversation's property (`listing_id` is refused).

    The same as `POST /v1/conversations/{id}/pre-approval` and `/special-offers` on a Vrbo conversation,
    which take the Repull conversation id. Send `Idempotency-Key`: a retry without it can send the guest
    two quotes. Returns `403 listing_inactive` when the conversation's listing is inactive.

    Args:
        body (CreateVrboOfferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateVrboOfferResponse201Type0 | CreateVrboOfferResponse201Type1 | Error
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: CreateVrboOfferBody,

) -> Response[CreateVrboOfferResponse201Type0 | CreateVrboOfferResponse201Type1 | Error]:
    r""" Pre-approve or quote a Vrbo inquiry

     Answer a Vrbo inquiry — the counterpart of `POST /v1/channels/airbnb/offers`, the same body
    addressed by the Vrbo conversation. `type: \"preapproval\"` invites the guest to book their dates at
    the listed price; `type: \"offer\"` sends Vrbo's edited quote.

    **Priced by its parts, not a total.** Vrbo adds its taxes and service fee itself, so a quote takes
    `rental_amount`, `fees` (`[{ type, value }]`, Vrbo fee types such as `CLEANING`, `PET`) and
    `damage_deposit`; `total_price` is refused. The stay is `start_date` + `nights` and `guest_details`,
    as on Airbnb; leave them out to keep the guest's own. Both types may carry a `message` to the guest.
    Vrbo has no instant-book switch on a pre-approval (`block_instant_booking` is refused) and a quote
    is always for the conversation's property (`listing_id` is refused).

    The same as `POST /v1/conversations/{id}/pre-approval` and `/special-offers` on a Vrbo conversation,
    which take the Repull conversation id. Send `Idempotency-Key`: a retry without it can send the guest
    two quotes. Returns `403 listing_inactive` when the conversation's listing is inactive.

    Args:
        body (CreateVrboOfferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateVrboOfferResponse201Type0 | CreateVrboOfferResponse201Type1 | Error]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: CreateVrboOfferBody,

) -> CreateVrboOfferResponse201Type0 | CreateVrboOfferResponse201Type1 | Error | None:
    r""" Pre-approve or quote a Vrbo inquiry

     Answer a Vrbo inquiry — the counterpart of `POST /v1/channels/airbnb/offers`, the same body
    addressed by the Vrbo conversation. `type: \"preapproval\"` invites the guest to book their dates at
    the listed price; `type: \"offer\"` sends Vrbo's edited quote.

    **Priced by its parts, not a total.** Vrbo adds its taxes and service fee itself, so a quote takes
    `rental_amount`, `fees` (`[{ type, value }]`, Vrbo fee types such as `CLEANING`, `PET`) and
    `damage_deposit`; `total_price` is refused. The stay is `start_date` + `nights` and `guest_details`,
    as on Airbnb; leave them out to keep the guest's own. Both types may carry a `message` to the guest.
    Vrbo has no instant-book switch on a pre-approval (`block_instant_booking` is refused) and a quote
    is always for the conversation's property (`listing_id` is refused).

    The same as `POST /v1/conversations/{id}/pre-approval` and `/special-offers` on a Vrbo conversation,
    which take the Repull conversation id. Send `Idempotency-Key`: a retry without it can send the guest
    two quotes. Returns `403 listing_inactive` when the conversation's listing is inactive.

    Args:
        body (CreateVrboOfferBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateVrboOfferResponse201Type0 | CreateVrboOfferResponse201Type1 | Error
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
