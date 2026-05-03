from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.error_error_support import ErrorErrorSupport





T = TypeVar("T", bound="ErrorError")



@_attrs_define
class ErrorError:
    """ 
        Attributes:
            code (str): Stable machine-parseable error identifier. Match on this for retry logic. Codes are namespaced and
                never change meaning. Example: invalid_params.
            message (str): Human-readable cause. Echoes the offending value when relevant. Example: The check_in_after
                parameter must be an ISO 8601 date (YYYY-MM-DD or YYYY-MM-DDTHH:mm:ssZ). You sent: 'garbage'..
            fix (str): Exact recovery steps. Surface this verbatim in your UI / agent reasoning trace — it is written to be
                actionable without further reading. Example: Pass check_in_after as a string in ISO 8601 format. Example:
                ?check_in_after=2026-01-15.
            docs_url (str): Canonical write-up for this error code. URL pattern: `https://repull.dev/docs/errors/{code}`.
                Example: https://repull.dev/docs/errors/invalid_params.
            request_id (str): Opaque per-request id. Mirrors the `x-request-id` response header. Capture it before retrying
                so logs can be correlated. Example: req_01J5X7Y8Z9ABCDEF12345678.
            field (str | Unset): Body field, query param, or path segment the error is about. Present when the error is
                parameter-specific. Example: check_in_after.
            value_received (Any | Unset): Echo of the offending value (truncated to 200 chars). Useful for debugging — helps
                callers see what the server actually parsed. Example: garbage.
            valid_values (list[str] | Unset): Allowed values when the error is enum-related (e.g. unknown `provider`,
                unknown `status`). Example: ['airbnb', 'booking', 'vrbo', 'plumguide'].
            valid_params (list[str] | Unset): Sorted list of every query param this endpoint accepts. Present on `code:
                "unknown_params"` (HTTP 422) so SDK consumers can self-correct without reading docs. Example: ['cursor',
                'has_reservation', 'include_total', 'limit', 'listingId', 'q'].
            endpoint (str | Unset): The endpoint path that produced the error. Present on `code: "unknown_params"` so
                consumers can match validation failures to the operation they invoked. Example: /v1/guests.
            did_you_mean (str | Unset): Suggestion for typos and near-matches. Present when the server can guess the intent.
                Example: check_in_after.
            retry_after (int | Unset): Seconds the client should wait before retrying. Mirrors the `Retry-After` HTTP
                header. Present on rate-limit responses and on transient upstream failures that are safe to retry. Example: 60.
            support (ErrorErrorSupport | Unset): LAST-RESORT contact handle. Only set on errors that genuinely cannot be
                self-fixed (billing dispute, account-state corruption, OAuth partner intervention). Never fall back to support
                before trying `fix` and `docs_url`.
     """

    code: str
    message: str
    fix: str
    docs_url: str
    request_id: str
    field: str | Unset = UNSET
    value_received: Any | Unset = UNSET
    valid_values: list[str] | Unset = UNSET
    valid_params: list[str] | Unset = UNSET
    endpoint: str | Unset = UNSET
    did_you_mean: str | Unset = UNSET
    retry_after: int | Unset = UNSET
    support: ErrorErrorSupport | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.error_error_support import ErrorErrorSupport
        code = self.code

        message = self.message

        fix = self.fix

        docs_url = self.docs_url

        request_id = self.request_id

        field = self.field

        value_received = self.value_received

        valid_values: list[str] | Unset = UNSET
        if not isinstance(self.valid_values, Unset):
            valid_values = self.valid_values



        valid_params: list[str] | Unset = UNSET
        if not isinstance(self.valid_params, Unset):
            valid_params = self.valid_params



        endpoint = self.endpoint

        did_you_mean = self.did_you_mean

        retry_after = self.retry_after

        support: dict[str, Any] | Unset = UNSET
        if not isinstance(self.support, Unset):
            support = self.support.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "message": message,
            "fix": fix,
            "docs_url": docs_url,
            "request_id": request_id,
        })
        if field is not UNSET:
            field_dict["field"] = field
        if value_received is not UNSET:
            field_dict["value_received"] = value_received
        if valid_values is not UNSET:
            field_dict["valid_values"] = valid_values
        if valid_params is not UNSET:
            field_dict["validParams"] = valid_params
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if did_you_mean is not UNSET:
            field_dict["did_you_mean"] = did_you_mean
        if retry_after is not UNSET:
            field_dict["retry_after"] = retry_after
        if support is not UNSET:
            field_dict["support"] = support

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_error_support import ErrorErrorSupport
        d = dict(src_dict)
        code = d.pop("code")

        message = d.pop("message")

        fix = d.pop("fix")

        docs_url = d.pop("docs_url")

        request_id = d.pop("request_id")

        field = d.pop("field", UNSET)

        value_received = d.pop("value_received", UNSET)

        valid_values = cast(list[str], d.pop("valid_values", UNSET))


        valid_params = cast(list[str], d.pop("validParams", UNSET))


        endpoint = d.pop("endpoint", UNSET)

        did_you_mean = d.pop("did_you_mean", UNSET)

        retry_after = d.pop("retry_after", UNSET)

        _support = d.pop("support", UNSET)
        support: ErrorErrorSupport | Unset
        if isinstance(_support,  Unset):
            support = UNSET
        else:
            support = ErrorErrorSupport.from_dict(_support)




        error_error = cls(
            code=code,
            message=message,
            fix=fix,
            docs_url=docs_url,
            request_id=request_id,
            field=field,
            value_received=value_received,
            valid_values=valid_values,
            valid_params=valid_params,
            endpoint=endpoint,
            did_you_mean=did_you_mean,
            retry_after=retry_after,
            support=support,
        )


        error_error.additional_properties = d
        return error_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
