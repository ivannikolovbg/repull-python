from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.ai_operation_failed_payload_error import AiOperationFailedPayloadError





T = TypeVar("T", bound="AiOperationFailedPayload")



@_attrs_define
class AiOperationFailedPayload:
    """ Payload for `ai.operation.failed`. An async AI run terminated with an error and will not be retried.

        Attributes:
            operation_id (str | Unset):  Example: aiop_01HX5XPQ2L.
            type_ (str | Unset):  Example: price-suggestion.
            error (AiOperationFailedPayloadError | Unset):
            failed_at (datetime.datetime | Unset):  Example: 2026-05-01T18:01:00.000Z.
     """

    operation_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    error: AiOperationFailedPayloadError | Unset = UNSET
    failed_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ai_operation_failed_payload_error import AiOperationFailedPayloadError
        operation_id = self.operation_id

        type_ = self.type_

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        failed_at: str | Unset = UNSET
        if not isinstance(self.failed_at, Unset):
            failed_at = self.failed_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if error is not UNSET:
            field_dict["error"] = error
        if failed_at is not UNSET:
            field_dict["failedAt"] = failed_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ai_operation_failed_payload_error import AiOperationFailedPayloadError
        d = dict(src_dict)
        operation_id = d.pop("operationId", UNSET)

        type_ = d.pop("type", UNSET)

        _error = d.pop("error", UNSET)
        error: AiOperationFailedPayloadError | Unset
        if isinstance(_error,  Unset):
            error = UNSET
        else:
            error = AiOperationFailedPayloadError.from_dict(_error)




        _failed_at = d.pop("failedAt", UNSET)
        failed_at: datetime.datetime | Unset
        if isinstance(_failed_at,  Unset):
            failed_at = UNSET
        else:
            failed_at = isoparse(_failed_at)




        ai_operation_failed_payload = cls(
            operation_id=operation_id,
            type_=type_,
            error=error,
            failed_at=failed_at,
        )


        ai_operation_failed_payload.additional_properties = d
        return ai_operation_failed_payload

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
