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
  from ..models.ai_operation_completed_payload_output import AiOperationCompletedPayloadOutput





T = TypeVar("T", bound="AiOperationCompletedPayload")



@_attrs_define
class AiOperationCompletedPayload:
    """ Payload for `ai.operation.completed`. An async AI run (review response, message draft, pricing suggestion) finished.

        Attributes:
            operation_id (str | Unset):  Example: aiop_01HX5XPQ2K.
            type_ (str | Unset): AI operation kind — e.g. respond-to-guest, price-suggestion, review-response. Example:
                respond-to-guest.
            input_summary (str | Unset):  Example: Guest asked about parking.
            output (AiOperationCompletedPayloadOutput | Unset): Operation-specific output object. Example: {'message': 'Free
                underground parking is included with your stay.'}.
            tokens_used (int | Unset):  Example: 184.
            completed_at (datetime.datetime | Unset):  Example: 2026-05-01T18:00:00.000Z.
     """

    operation_id: str | Unset = UNSET
    type_: str | Unset = UNSET
    input_summary: str | Unset = UNSET
    output: AiOperationCompletedPayloadOutput | Unset = UNSET
    tokens_used: int | Unset = UNSET
    completed_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ai_operation_completed_payload_output import AiOperationCompletedPayloadOutput
        operation_id = self.operation_id

        type_ = self.type_

        input_summary = self.input_summary

        output: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.to_dict()

        tokens_used = self.tokens_used

        completed_at: str | Unset = UNSET
        if not isinstance(self.completed_at, Unset):
            completed_at = self.completed_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if input_summary is not UNSET:
            field_dict["inputSummary"] = input_summary
        if output is not UNSET:
            field_dict["output"] = output
        if tokens_used is not UNSET:
            field_dict["tokensUsed"] = tokens_used
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ai_operation_completed_payload_output import AiOperationCompletedPayloadOutput
        d = dict(src_dict)
        operation_id = d.pop("operationId", UNSET)

        type_ = d.pop("type", UNSET)

        input_summary = d.pop("inputSummary", UNSET)

        _output = d.pop("output", UNSET)
        output: AiOperationCompletedPayloadOutput | Unset
        if isinstance(_output,  Unset):
            output = UNSET
        else:
            output = AiOperationCompletedPayloadOutput.from_dict(_output)




        tokens_used = d.pop("tokensUsed", UNSET)

        _completed_at = d.pop("completedAt", UNSET)
        completed_at: datetime.datetime | Unset
        if isinstance(_completed_at,  Unset):
            completed_at = UNSET
        else:
            completed_at = isoparse(_completed_at)




        ai_operation_completed_payload = cls(
            operation_id=operation_id,
            type_=type_,
            input_summary=input_summary,
            output=output,
            tokens_used=tokens_used,
            completed_at=completed_at,
        )


        ai_operation_completed_payload.additional_properties = d
        return ai_operation_completed_payload

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
