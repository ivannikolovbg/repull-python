from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.ai_operation_operation import AIOperationOperation
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ai_operation_input import AIOperationInput





T = TypeVar("T", bound="AIOperation")



@_attrs_define
class AIOperation:
    """ 
        Attributes:
            operation (AIOperationOperation | Unset): AI operation to perform
            input_ (AIOperationInput | Unset): Operation-specific input data
     """

    operation: AIOperationOperation | Unset = UNSET
    input_: AIOperationInput | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ai_operation_input import AIOperationInput
        operation: str | Unset = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value


        input_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_, Unset):
            input_ = self.input_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if operation is not UNSET:
            field_dict["operation"] = operation
        if input_ is not UNSET:
            field_dict["input"] = input_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ai_operation_input import AIOperationInput
        d = dict(src_dict)
        _operation = d.pop("operation", UNSET)
        operation: AIOperationOperation | Unset
        if isinstance(_operation,  Unset):
            operation = UNSET
        else:
            operation = AIOperationOperation(_operation)




        _input_ = d.pop("input", UNSET)
        input_: AIOperationInput | Unset
        if isinstance(_input_,  Unset):
            input_ = UNSET
        else:
            input_ = AIOperationInput.from_dict(_input_)




        ai_operation = cls(
            operation=operation,
            input_=input_,
        )


        ai_operation.additional_properties = d
        return ai_operation

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
