from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.airbnb_availability_write_request import AirbnbAvailabilityWriteRequest
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: AirbnbAvailabilityWriteRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/v1/channels/airbnb/listings/{id}/availability".format(id=quote(str(id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
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
    body: AirbnbAvailabilityWriteRequest,

) -> Response[Any]:
    r""" Update Airbnb availability

     Push availability + restrictions to Airbnb. `type: \"calendar\"` writes per-date restrictions —
    min/max nights, closed-to-arrival, closed-to-departure, and stop-sell (`availability:
    \"unavailable\"`) — via a batch of operations that each target either a date range or an explicit
    date list. `type: \"rules\"` writes listing-level availability rules (default min/max nights,
    booking lead time, turnover days, seasonal/day-of-week min nights). Restrictions never leak across
    channels — this endpoint writes only to Airbnb.

    Args:
        id (str):
        body (AirbnbAvailabilityWriteRequest): Body for `PUT
            /v1/channels/airbnb/listings/{id}/availability`. `type: "calendar"` carries per-date
            restrictions (min/max nights, closed-to-arrival/departure, stop-sell); `type: "rules"`
            carries listing-level availability rules (default min/max nights, booking lead time,
            turnover days).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AirbnbAvailabilityWriteRequest,

) -> Response[Any]:
    r""" Update Airbnb availability

     Push availability + restrictions to Airbnb. `type: \"calendar\"` writes per-date restrictions —
    min/max nights, closed-to-arrival, closed-to-departure, and stop-sell (`availability:
    \"unavailable\"`) — via a batch of operations that each target either a date range or an explicit
    date list. `type: \"rules\"` writes listing-level availability rules (default min/max nights,
    booking lead time, turnover days, seasonal/day-of-week min nights). Restrictions never leak across
    channels — this endpoint writes only to Airbnb.

    Args:
        id (str):
        body (AirbnbAvailabilityWriteRequest): Body for `PUT
            /v1/channels/airbnb/listings/{id}/availability`. `type: "calendar"` carries per-date
            restrictions (min/max nights, closed-to-arrival/departure, stop-sell); `type: "rules"`
            carries listing-level availability rules (default min/max nights, booking lead time,
            turnover days).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

