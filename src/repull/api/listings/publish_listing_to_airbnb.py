from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.listing_publish_airbnb_request import ListingPublishAirbnbRequest
from ...models.listing_publish_response import ListingPublishResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: int,
    *,
    body: ListingPublishAirbnbRequest | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/listings/{id}/publish/airbnb".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ListingPublishResponse | None:
    if response.status_code == 200:
        response_200 = ListingPublishResponse.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ListingPublishResponse]:
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
    body: ListingPublishAirbnbRequest | Unset = UNSET,

) -> Response[Any | ListingPublishResponse]:
    """ Publish a listing to Airbnb

     Push a Repull listing to Airbnb. Pass `airbnbConnectionId` to update an already-mapped Airbnb
    listing, or `hostId` to create a brand-new Airbnb listing under that host.

    Args:
        id (int):
        body (ListingPublishAirbnbRequest | Unset): Pass either `airbnbConnectionId` (update an
            already-mapped listing) or `hostId` (create a brand-new Airbnb listing under that host).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListingPublishResponse]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingPublishAirbnbRequest | Unset = UNSET,

) -> Any | ListingPublishResponse | None:
    """ Publish a listing to Airbnb

     Push a Repull listing to Airbnb. Pass `airbnbConnectionId` to update an already-mapped Airbnb
    listing, or `hostId` to create a brand-new Airbnb listing under that host.

    Args:
        id (int):
        body (ListingPublishAirbnbRequest | Unset): Pass either `airbnbConnectionId` (update an
            already-mapped listing) or `hostId` (create a brand-new Airbnb listing under that host).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListingPublishResponse
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingPublishAirbnbRequest | Unset = UNSET,

) -> Response[Any | ListingPublishResponse]:
    """ Publish a listing to Airbnb

     Push a Repull listing to Airbnb. Pass `airbnbConnectionId` to update an already-mapped Airbnb
    listing, or `hostId` to create a brand-new Airbnb listing under that host.

    Args:
        id (int):
        body (ListingPublishAirbnbRequest | Unset): Pass either `airbnbConnectionId` (update an
            already-mapped listing) or `hostId` (create a brand-new Airbnb listing under that host).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ListingPublishResponse]
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
    id: int,
    *,
    client: AuthenticatedClient | Client,
    body: ListingPublishAirbnbRequest | Unset = UNSET,

) -> Any | ListingPublishResponse | None:
    """ Publish a listing to Airbnb

     Push a Repull listing to Airbnb. Pass `airbnbConnectionId` to update an already-mapped Airbnb
    listing, or `hostId` to create a brand-new Airbnb listing under that host.

    Args:
        id (int):
        body (ListingPublishAirbnbRequest | Unset): Pass either `airbnbConnectionId` (update an
            already-mapped listing) or `hostId` (create a brand-new Airbnb listing under that host).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ListingPublishResponse
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
