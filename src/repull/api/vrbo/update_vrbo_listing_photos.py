from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.update_vrbo_listing_photos_body import UpdateVrboListingPhotosBody
from ...models.update_vrbo_listing_photos_response_200 import UpdateVrboListingPhotosResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: UpdateVrboListingPhotosBody,
    vrbo_listing_number: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["vrboListingNumber"] = vrbo_listing_number


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/vrbo/listings/{id}/photos".format(id=quote(str(id), safe=""),),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | UpdateVrboListingPhotosResponse200 | None:
    if response.status_code == 200:
        response_200 = UpdateVrboListingPhotosResponse200.from_dict(response.json())



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

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if response.status_code == 502:
        response_502 = Error.from_dict(response.json())



        return response_502

    if response.status_code == 503:
        response_503 = Error.from_dict(response.json())



        return response_503

    if response.status_code == 504:
        response_504 = Error.from_dict(response.json())



        return response_504

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | UpdateVrboListingPhotosResponse200]:
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
    body: UpdateVrboListingPhotosBody,
    vrbo_listing_number: str | Unset = UNSET,

) -> Response[Error | UpdateVrboListingPhotosResponse200]:
    r""" Update the Vrbo photos

     Change the photos of the listing's existing Vrbo listing. **Partial:** send only the fields to
    change; a field you leave out is never changed on Vrbo, and a field sent as `null` means \"none\"
    (where the field can be cleared). Fields Vrbo can change but never empty once set are refused with
    `422 invalid_params` when sent empty or `null`, rather than answering OK while Vrbo keeps the old
    value. `add: [{url, caption?}]` (https URLs Vrbo downloads), `delete: [id]`, `captions: {id:
    caption}`, `order: [id…]`, `cover: id`. Applied in that order. `order` may list only the first
    photos; the rest keep their order, and every photo is sent with its new position (as Vrbo's own page
    does). **Captions are one-way:** Vrbo has not been shown to clear a caption once set, so an empty
    caption is refused. Each `add` uploads a photo again — it is the one write that is not idempotent.

    **Cost:** about 2 calls per photo added, 1 per delete/caption/reorder, plus reads on Vrbo, spaced ~3
    s apart per account. The answer comes once Vrbo has saved and the section has been read back.

    **When Vrbo refuses** a value the answer is `422 vrbo_rejected` with Vrbo's own message, the refused
    fields in `errors` and what Vrbo has now in `data` (fields Vrbo accepted in the same request are
    saved). A malformed body is `422 invalid_params` naming the field, and nothing is sent to Vrbo.

    Needs a Vrbo account connected with full access: one connected with messaging access answers `403
    vrbo_messaging_access`. Returns `403 listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        body (UpdateVrboListingPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateVrboListingPhotosResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
vrbo_listing_number=vrbo_listing_number,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateVrboListingPhotosBody,
    vrbo_listing_number: str | Unset = UNSET,

) -> Error | UpdateVrboListingPhotosResponse200 | None:
    r""" Update the Vrbo photos

     Change the photos of the listing's existing Vrbo listing. **Partial:** send only the fields to
    change; a field you leave out is never changed on Vrbo, and a field sent as `null` means \"none\"
    (where the field can be cleared). Fields Vrbo can change but never empty once set are refused with
    `422 invalid_params` when sent empty or `null`, rather than answering OK while Vrbo keeps the old
    value. `add: [{url, caption?}]` (https URLs Vrbo downloads), `delete: [id]`, `captions: {id:
    caption}`, `order: [id…]`, `cover: id`. Applied in that order. `order` may list only the first
    photos; the rest keep their order, and every photo is sent with its new position (as Vrbo's own page
    does). **Captions are one-way:** Vrbo has not been shown to clear a caption once set, so an empty
    caption is refused. Each `add` uploads a photo again — it is the one write that is not idempotent.

    **Cost:** about 2 calls per photo added, 1 per delete/caption/reorder, plus reads on Vrbo, spaced ~3
    s apart per account. The answer comes once Vrbo has saved and the section has been read back.

    **When Vrbo refuses** a value the answer is `422 vrbo_rejected` with Vrbo's own message, the refused
    fields in `errors` and what Vrbo has now in `data` (fields Vrbo accepted in the same request are
    saved). A malformed body is `422 invalid_params` naming the field, and nothing is sent to Vrbo.

    Needs a Vrbo account connected with full access: one connected with messaging access answers `403
    vrbo_messaging_access`. Returns `403 listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        body (UpdateVrboListingPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateVrboListingPhotosResponse200
     """


    return sync_detailed(
        id=id,
client=client,
body=body,
vrbo_listing_number=vrbo_listing_number,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateVrboListingPhotosBody,
    vrbo_listing_number: str | Unset = UNSET,

) -> Response[Error | UpdateVrboListingPhotosResponse200]:
    r""" Update the Vrbo photos

     Change the photos of the listing's existing Vrbo listing. **Partial:** send only the fields to
    change; a field you leave out is never changed on Vrbo, and a field sent as `null` means \"none\"
    (where the field can be cleared). Fields Vrbo can change but never empty once set are refused with
    `422 invalid_params` when sent empty or `null`, rather than answering OK while Vrbo keeps the old
    value. `add: [{url, caption?}]` (https URLs Vrbo downloads), `delete: [id]`, `captions: {id:
    caption}`, `order: [id…]`, `cover: id`. Applied in that order. `order` may list only the first
    photos; the rest keep their order, and every photo is sent with its new position (as Vrbo's own page
    does). **Captions are one-way:** Vrbo has not been shown to clear a caption once set, so an empty
    caption is refused. Each `add` uploads a photo again — it is the one write that is not idempotent.

    **Cost:** about 2 calls per photo added, 1 per delete/caption/reorder, plus reads on Vrbo, spaced ~3
    s apart per account. The answer comes once Vrbo has saved and the section has been read back.

    **When Vrbo refuses** a value the answer is `422 vrbo_rejected` with Vrbo's own message, the refused
    fields in `errors` and what Vrbo has now in `data` (fields Vrbo accepted in the same request are
    saved). A malformed body is `422 invalid_params` naming the field, and nothing is sent to Vrbo.

    Needs a Vrbo account connected with full access: one connected with messaging access answers `403
    vrbo_messaging_access`. Returns `403 listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        body (UpdateVrboListingPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | UpdateVrboListingPhotosResponse200]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,
vrbo_listing_number=vrbo_listing_number,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateVrboListingPhotosBody,
    vrbo_listing_number: str | Unset = UNSET,

) -> Error | UpdateVrboListingPhotosResponse200 | None:
    r""" Update the Vrbo photos

     Change the photos of the listing's existing Vrbo listing. **Partial:** send only the fields to
    change; a field you leave out is never changed on Vrbo, and a field sent as `null` means \"none\"
    (where the field can be cleared). Fields Vrbo can change but never empty once set are refused with
    `422 invalid_params` when sent empty or `null`, rather than answering OK while Vrbo keeps the old
    value. `add: [{url, caption?}]` (https URLs Vrbo downloads), `delete: [id]`, `captions: {id:
    caption}`, `order: [id…]`, `cover: id`. Applied in that order. `order` may list only the first
    photos; the rest keep their order, and every photo is sent with its new position (as Vrbo's own page
    does). **Captions are one-way:** Vrbo has not been shown to clear a caption once set, so an empty
    caption is refused. Each `add` uploads a photo again — it is the one write that is not idempotent.

    **Cost:** about 2 calls per photo added, 1 per delete/caption/reorder, plus reads on Vrbo, spaced ~3
    s apart per account. The answer comes once Vrbo has saved and the section has been read back.

    **When Vrbo refuses** a value the answer is `422 vrbo_rejected` with Vrbo's own message, the refused
    fields in `errors` and what Vrbo has now in `data` (fields Vrbo accepted in the same request are
    saved). A malformed body is `422 invalid_params` naming the field, and nothing is sent to Vrbo.

    Needs a Vrbo account connected with full access: one connected with messaging access answers `403
    vrbo_messaging_access`. Returns `403 listing_inactive` when the listing is inactive.

    Args:
        id (str):
        vrbo_listing_number (str | Unset):
        body (UpdateVrboListingPhotosBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | UpdateVrboListingPhotosResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,
vrbo_listing_number=vrbo_listing_number,

    )).parsed
