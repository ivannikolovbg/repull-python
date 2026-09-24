from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_content_update_request_checkout_tasks_type_0_item_task_type import ListingContentUpdateRequestCheckoutTasksType0ItemTaskType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingContentUpdateRequestCheckoutTasksType0Item")



@_attrs_define
class ListingContentUpdateRequestCheckoutTasksType0Item:
    """ 
        Attributes:
            task_type (ListingContentUpdateRequestCheckoutTasksType0ItemTaskType): Any casing is accepted; stored lowercase.
            instructions (None | str | Unset): Detail shown to the guest with the task, e.g. "Leave the keys on the kitchen
                counter".
            required (bool | None | Unset):
     """

    task_type: ListingContentUpdateRequestCheckoutTasksType0ItemTaskType
    instructions: None | str | Unset = UNSET
    required: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        task_type = self.task_type.value

        instructions: None | str | Unset
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        else:
            instructions = self.instructions

        required: bool | None | Unset
        if isinstance(self.required, Unset):
            required = UNSET
        else:
            required = self.required


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "taskType": task_type,
        })
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_type = ListingContentUpdateRequestCheckoutTasksType0ItemTaskType(d.pop("taskType"))




        def _parse_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))


        def _parse_required(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        required = _parse_required(d.pop("required", UNSET))


        listing_content_update_request_checkout_tasks_type_0_item = cls(
            task_type=task_type,
            instructions=instructions,
            required=required,
        )


        listing_content_update_request_checkout_tasks_type_0_item.additional_properties = d
        return listing_content_update_request_checkout_tasks_type_0_item

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
