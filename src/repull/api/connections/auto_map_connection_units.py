from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.auto_map_connection_units_body import AutoMapConnectionUnitsBody
from ...models.auto_map_connection_units_response_200 import AutoMapConnectionUnitsResponse200
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: AutoMapConnectionUnitsBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/connections/{id}/mappings/automap".format(id=quote(str(id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AutoMapConnectionUnitsResponse200 | None:
    if response.status_code == 200:
        response_200 = AutoMapConnectionUnitsResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AutoMapConnectionUnitsResponse200]:
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
    body: AutoMapConnectionUnitsBody | Unset = UNSET,

) -> Response[AutoMapConnectionUnitsResponse200]:
    """ Auto-map units by exact name

     Proposes (or with `apply: true` applies) mappings where a unit's name exactly matches one listing.
    Never guesses on ambiguity.

    Auth: a Repull API key, or a Connect session token (`sessionId`) while the hosted flow is mapping.

    Args:
        id (str):
        body (AutoMapConnectionUnitsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutoMapConnectionUnitsResponse200]
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AutoMapConnectionUnitsBody | Unset = UNSET,

) -> AutoMapConnectionUnitsResponse200 | None:
    """ Auto-map units by exact name

     Proposes (or with `apply: true` applies) mappings where a unit's name exactly matches one listing.
    Never guesses on ambiguity.

    Auth: a Repull API key, or a Connect session token (`sessionId`) while the hosted flow is mapping.

    Args:
        id (str):
        body (AutoMapConnectionUnitsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutoMapConnectionUnitsResponse200
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AutoMapConnectionUnitsBody | Unset = UNSET,

) -> Response[AutoMapConnectionUnitsResponse200]:
    """ Auto-map units by exact name

     Proposes (or with `apply: true` applies) mappings where a unit's name exactly matches one listing.
    Never guesses on ambiguity.

    Auth: a Repull API key, or a Connect session token (`sessionId`) while the hosted flow is mapping.

    Args:
        id (str):
        body (AutoMapConnectionUnitsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AutoMapConnectionUnitsResponse200]
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
    id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AutoMapConnectionUnitsBody | Unset = UNSET,

) -> AutoMapConnectionUnitsResponse200 | None:
    """ Auto-map units by exact name

     Proposes (or with `apply: true` applies) mappings where a unit's name exactly matches one listing.
    Never guesses on ambiguity.

    Auth: a Repull API key, or a Connect session token (`sessionId`) while the hosted flow is mapping.

    Args:
        id (str):
        body (AutoMapConnectionUnitsBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AutoMapConnectionUnitsResponse200
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
