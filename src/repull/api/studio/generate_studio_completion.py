from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.generate_studio_completion_body import GenerateStudioCompletionBody
from ...models.generate_studio_completion_response_200 import GenerateStudioCompletionResponse200
from ...models.studio_error import StudioError
from typing import cast



def _get_kwargs(
    *,
    body: GenerateStudioCompletionBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/studio/generate",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GenerateStudioCompletionResponse200 | StudioError | None:
    if response.status_code == 200:
        response_200 = GenerateStudioCompletionResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = StudioError.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = StudioError.from_dict(response.json())



        return response_401

    if response.status_code == 429:
        response_429 = StudioError.from_dict(response.json())



        return response_429

    if response.status_code == 500:
        response_500 = StudioError.from_dict(response.json())



        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GenerateStudioCompletionResponse200 | StudioError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GenerateStudioCompletionBody,

) -> Response[GenerateStudioCompletionResponse200 | StudioError]:
    """ Generate text with Repull AI

     Sends a prompt to Repull AI and returns the completion synchronously. This is the single LLM
    endpoint used by the Studio UI; programmatic clients can use it to drive their own vibe-coding
    flows. Responses include token accounting, cost-in-micros, and cache/fallback flags. 429s include a
    `Retry-After` header.

    Args:
        body (GenerateStudioCompletionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateStudioCompletionResponse200 | StudioError]
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
    body: GenerateStudioCompletionBody,

) -> GenerateStudioCompletionResponse200 | StudioError | None:
    """ Generate text with Repull AI

     Sends a prompt to Repull AI and returns the completion synchronously. This is the single LLM
    endpoint used by the Studio UI; programmatic clients can use it to drive their own vibe-coding
    flows. Responses include token accounting, cost-in-micros, and cache/fallback flags. 429s include a
    `Retry-After` header.

    Args:
        body (GenerateStudioCompletionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateStudioCompletionResponse200 | StudioError
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: GenerateStudioCompletionBody,

) -> Response[GenerateStudioCompletionResponse200 | StudioError]:
    """ Generate text with Repull AI

     Sends a prompt to Repull AI and returns the completion synchronously. This is the single LLM
    endpoint used by the Studio UI; programmatic clients can use it to drive their own vibe-coding
    flows. Responses include token accounting, cost-in-micros, and cache/fallback flags. 429s include a
    `Retry-After` header.

    Args:
        body (GenerateStudioCompletionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateStudioCompletionResponse200 | StudioError]
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
    body: GenerateStudioCompletionBody,

) -> GenerateStudioCompletionResponse200 | StudioError | None:
    """ Generate text with Repull AI

     Sends a prompt to Repull AI and returns the completion synchronously. This is the single LLM
    endpoint used by the Studio UI; programmatic clients can use it to drive their own vibe-coding
    flows. Responses include token accounting, cost-in-micros, and cache/fallback flags. 429s include a
    `Retry-After` header.

    Args:
        body (GenerateStudioCompletionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateStudioCompletionResponse200 | StudioError
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
