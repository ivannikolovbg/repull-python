from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.vrbo_listing import VrboListing
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/channels/vrbo/listings",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[VrboListing] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_vrbo_listing_list_response_item_data in (_response_200):
            componentsschemas_vrbo_listing_list_response_item = VrboListing.from_dict(componentsschemas_vrbo_listing_list_response_item_data)



            response_200.append(componentsschemas_vrbo_listing_list_response_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[VrboListing]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[VrboListing]]:
    """ List VRBO listings

     List VRBO listings this workspace owns. VRBO is agency-model — Repull reads listings via the public
    iCal/HTTP feeds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[VrboListing]]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,

) -> list[VrboListing] | None:
    """ List VRBO listings

     List VRBO listings this workspace owns. VRBO is agency-model — Repull reads listings via the public
    iCal/HTTP feeds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[VrboListing]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,

) -> Response[list[VrboListing]]:
    """ List VRBO listings

     List VRBO listings this workspace owns. VRBO is agency-model — Repull reads listings via the public
    iCal/HTTP feeds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[VrboListing]]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,

) -> list[VrboListing] | None:
    """ List VRBO listings

     List VRBO listings this workspace owns. VRBO is agency-model — Repull reads listings via the public
    iCal/HTTP feeds.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[VrboListing]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
