from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.refresh_airbnb_resolutions_body import RefreshAirbnbResolutionsBody
from ...models.refresh_airbnb_resolutions_response_200 import RefreshAirbnbResolutionsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: RefreshAirbnbResolutionsBody | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_schema, Unset):
        headers["X-Schema"] = x_schema



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channels/airbnb/resolutions",
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | RefreshAirbnbResolutionsResponse200 | None:
    if response.status_code == 200:
        response_200 = RefreshAirbnbResolutionsResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 500:
        response_500 = Error.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | RefreshAirbnbResolutionsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RefreshAirbnbResolutionsBody | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Response[Error | RefreshAirbnbResolutionsResponse200]:
    """ Refresh Airbnb resolutions from Airbnb

     Pulls the latest Resolution Center cases from Airbnb (read-only) and stores them, then read with
    GET. Optionally scope to one `account_id` and/or `status`.

    Args:
        x_schema (str | Unset):  Example: my-app-schema.
        body (RefreshAirbnbResolutionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RefreshAirbnbResolutionsResponse200]
     """


    kwargs = _get_kwargs(
        body=body,
x_schema=x_schema,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: RefreshAirbnbResolutionsBody | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Error | RefreshAirbnbResolutionsResponse200 | None:
    """ Refresh Airbnb resolutions from Airbnb

     Pulls the latest Resolution Center cases from Airbnb (read-only) and stores them, then read with
    GET. Optionally scope to one `account_id` and/or `status`.

    Args:
        x_schema (str | Unset):  Example: my-app-schema.
        body (RefreshAirbnbResolutionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RefreshAirbnbResolutionsResponse200
     """


    return sync_detailed(
        client=client,
body=body,
x_schema=x_schema,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: RefreshAirbnbResolutionsBody | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Response[Error | RefreshAirbnbResolutionsResponse200]:
    """ Refresh Airbnb resolutions from Airbnb

     Pulls the latest Resolution Center cases from Airbnb (read-only) and stores them, then read with
    GET. Optionally scope to one `account_id` and/or `status`.

    Args:
        x_schema (str | Unset):  Example: my-app-schema.
        body (RefreshAirbnbResolutionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | RefreshAirbnbResolutionsResponse200]
     """


    kwargs = _get_kwargs(
        body=body,
x_schema=x_schema,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: RefreshAirbnbResolutionsBody | Unset = UNSET,
    x_schema: str | Unset = UNSET,

) -> Error | RefreshAirbnbResolutionsResponse200 | None:
    """ Refresh Airbnb resolutions from Airbnb

     Pulls the latest Resolution Center cases from Airbnb (read-only) and stores them, then read with
    GET. Optionally scope to one `account_id` and/or `status`.

    Args:
        x_schema (str | Unset):  Example: my-app-schema.
        body (RefreshAirbnbResolutionsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | RefreshAirbnbResolutionsResponse200
     """


    return (await asyncio_detailed(
        client=client,
body=body,
x_schema=x_schema,

    )).parsed
