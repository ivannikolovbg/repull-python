from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.listing_publish_booking_request import ListingPublishBookingRequest
from ...models.listing_publish_booking_response import ListingPublishBookingResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ListingPublishBookingRequest | Unset = UNSET,
    hotel_id: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["hotel_id"] = hotel_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/{id}/publish/booking".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | ListingPublishBookingResponse | None:
    if response.status_code == 200:
        response_200 = ListingPublishBookingResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())



        return response_400

    if response.status_code == 402:
        response_402 = Error.from_dict(response.json())



        return response_402

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())



        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | ListingPublishBookingResponse]:
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
    body: ListingPublishBookingRequest | Unset = UNSET,
    hotel_id: str | Unset = UNSET,

) -> Response[Error | ListingPublishBookingResponse]:
    """ Publish a listing to Booking.com

     Push a Repull listing's content to Booking.com. The listing must already be mapped to a Booking.com
    property + room — claim the hotel through the Connect Booking flow, then map its rooms with `POST
    /v1/connect/booking/map-rooms`.

    **Which property the content lands in.** A listing can be mapped to more than one Booking.com
    property; the same unit re-listed under a new property keeps its old mapping, and workspaces
    routinely sit on five or six. When the listing has exactly one property you need send nothing. When
    it has several, name one with `hotelId` in the body (or `?hotel_id=` — the same value, accepted
    either way, body wins if you send both). Omit it on such a listing and the push is refused with
    **`409 ambiguous_booking_mapping`**, listing the candidate ids: content pushed into a property
    chosen for you lands on the wrong listing and reports success, which is worse than a refusal. `GET
    /v1/channels/booking/properties` lists every property with the listings mapped under it. Naming a
    property this listing is not mapped to is a `404` that names the ones it is.

    The property that actually received the content comes back as `result.hotelId`.

    **A publish is not one call to Booking.com.** It is several independent Content API calls — details,
    description, amenities, rooms, photos, pricing — and each can fail on its own. `result.published` is
    true only when every attempted section landed; `result.sections` lists the ones that did and
    `result.errors[]` carries Booking.com's own reason, per section, for the ones that did not. A
    property whose Content API credentials do not cover a section answers 403 for that section alone.
    **A partial publish is normal and is not rolled back**: what succeeded stays applied. Fix the
    failing sections and publish again — re-publishing an unchanged section is harmless.

    A listing with no Booking.com property mapped at all is not an error: the call returns
    `result.published: false` with `result.reason` and `result.hotelId: null`, and nothing is pushed.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        body (ListingPublishBookingRequest | Unset): Optional. Omit the body entirely when the
            listing is mapped to exactly one Booking.com property.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingPublishBookingResponse]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
hotel_id=hotel_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingPublishBookingRequest | Unset = UNSET,
    hotel_id: str | Unset = UNSET,

) -> Error | ListingPublishBookingResponse | None:
    """ Publish a listing to Booking.com

     Push a Repull listing's content to Booking.com. The listing must already be mapped to a Booking.com
    property + room — claim the hotel through the Connect Booking flow, then map its rooms with `POST
    /v1/connect/booking/map-rooms`.

    **Which property the content lands in.** A listing can be mapped to more than one Booking.com
    property; the same unit re-listed under a new property keeps its old mapping, and workspaces
    routinely sit on five or six. When the listing has exactly one property you need send nothing. When
    it has several, name one with `hotelId` in the body (or `?hotel_id=` — the same value, accepted
    either way, body wins if you send both). Omit it on such a listing and the push is refused with
    **`409 ambiguous_booking_mapping`**, listing the candidate ids: content pushed into a property
    chosen for you lands on the wrong listing and reports success, which is worse than a refusal. `GET
    /v1/channels/booking/properties` lists every property with the listings mapped under it. Naming a
    property this listing is not mapped to is a `404` that names the ones it is.

    The property that actually received the content comes back as `result.hotelId`.

    **A publish is not one call to Booking.com.** It is several independent Content API calls — details,
    description, amenities, rooms, photos, pricing — and each can fail on its own. `result.published` is
    true only when every attempted section landed; `result.sections` lists the ones that did and
    `result.errors[]` carries Booking.com's own reason, per section, for the ones that did not. A
    property whose Content API credentials do not cover a section answers 403 for that section alone.
    **A partial publish is normal and is not rolled back**: what succeeded stays applied. Fix the
    failing sections and publish again — re-publishing an unchanged section is harmless.

    A listing with no Booking.com property mapped at all is not an error: the call returns
    `result.published: false` with `result.reason` and `result.hotelId: null`, and nothing is pushed.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        body (ListingPublishBookingRequest | Unset): Optional. Omit the body entirely when the
            listing is mapped to exactly one Booking.com property.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingPublishBookingResponse
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
hotel_id=hotel_id,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingPublishBookingRequest | Unset = UNSET,
    hotel_id: str | Unset = UNSET,

) -> Response[Error | ListingPublishBookingResponse]:
    """ Publish a listing to Booking.com

     Push a Repull listing's content to Booking.com. The listing must already be mapped to a Booking.com
    property + room — claim the hotel through the Connect Booking flow, then map its rooms with `POST
    /v1/connect/booking/map-rooms`.

    **Which property the content lands in.** A listing can be mapped to more than one Booking.com
    property; the same unit re-listed under a new property keeps its old mapping, and workspaces
    routinely sit on five or six. When the listing has exactly one property you need send nothing. When
    it has several, name one with `hotelId` in the body (or `?hotel_id=` — the same value, accepted
    either way, body wins if you send both). Omit it on such a listing and the push is refused with
    **`409 ambiguous_booking_mapping`**, listing the candidate ids: content pushed into a property
    chosen for you lands on the wrong listing and reports success, which is worse than a refusal. `GET
    /v1/channels/booking/properties` lists every property with the listings mapped under it. Naming a
    property this listing is not mapped to is a `404` that names the ones it is.

    The property that actually received the content comes back as `result.hotelId`.

    **A publish is not one call to Booking.com.** It is several independent Content API calls — details,
    description, amenities, rooms, photos, pricing — and each can fail on its own. `result.published` is
    true only when every attempted section landed; `result.sections` lists the ones that did and
    `result.errors[]` carries Booking.com's own reason, per section, for the ones that did not. A
    property whose Content API credentials do not cover a section answers 403 for that section alone.
    **A partial publish is normal and is not rolled back**: what succeeded stays applied. Fix the
    failing sections and publish again — re-publishing an unchanged section is harmless.

    A listing with no Booking.com property mapped at all is not an error: the call returns
    `result.published: false` with `result.reason` and `result.hotelId: null`, and nothing is pushed.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        body (ListingPublishBookingRequest | Unset): Optional. Omit the body entirely when the
            listing is mapped to exactly one Booking.com property.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListingPublishBookingResponse]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
hotel_id=hotel_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingPublishBookingRequest | Unset = UNSET,
    hotel_id: str | Unset = UNSET,

) -> Error | ListingPublishBookingResponse | None:
    """ Publish a listing to Booking.com

     Push a Repull listing's content to Booking.com. The listing must already be mapped to a Booking.com
    property + room — claim the hotel through the Connect Booking flow, then map its rooms with `POST
    /v1/connect/booking/map-rooms`.

    **Which property the content lands in.** A listing can be mapped to more than one Booking.com
    property; the same unit re-listed under a new property keeps its old mapping, and workspaces
    routinely sit on five or six. When the listing has exactly one property you need send nothing. When
    it has several, name one with `hotelId` in the body (or `?hotel_id=` — the same value, accepted
    either way, body wins if you send both). Omit it on such a listing and the push is refused with
    **`409 ambiguous_booking_mapping`**, listing the candidate ids: content pushed into a property
    chosen for you lands on the wrong listing and reports success, which is worse than a refusal. `GET
    /v1/channels/booking/properties` lists every property with the listings mapped under it. Naming a
    property this listing is not mapped to is a `404` that names the ones it is.

    The property that actually received the content comes back as `result.hotelId`.

    **A publish is not one call to Booking.com.** It is several independent Content API calls — details,
    description, amenities, rooms, photos, pricing — and each can fail on its own. `result.published` is
    true only when every attempted section landed; `result.sections` lists the ones that did and
    `result.errors[]` carries Booking.com's own reason, per section, for the ones that did not. A
    property whose Content API credentials do not cover a section answers 403 for that section alone.
    **A partial publish is normal and is not rolled back**: what succeeded stays applied. Fix the
    failing sections and publish again — re-publishing an unchanged section is harmless.

    A listing with no Booking.com property mapped at all is not an error: the call returns
    `result.published: false` with `result.reason` and `result.hotelId: null`, and nothing is pushed.

    Returns `403 listing_inactive` when the listing is inactive. An inactive listing keeps syncing, but
    cannot be read or changed through the API until it is activated.

    Args:
        id (int):
        hotel_id (str | Unset):
        body (ListingPublishBookingRequest | Unset): Optional. Omit the body entirely when the
            listing is mapped to exactly one Booking.com property.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListingPublishBookingResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
hotel_id=hotel_id,

    )).parsed
