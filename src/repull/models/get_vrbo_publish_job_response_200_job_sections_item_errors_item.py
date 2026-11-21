from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetVrboPublishJobResponse200JobSectionsItemErrorsItem")



@_attrs_define
class GetVrboPublishJobResponse200JobSectionsItemErrorsItem:
    """ 
        Attributes:
            field (None | str | Unset):
            message (str | Unset):
            code (None | str | Unset):
     """

    field: None | str | Unset = UNSET
    message: str | Unset = UNSET
    code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        field: None | str | Unset
        if isinstance(self.field, Unset):
            field = UNSET
        else:
            field = self.field

        message = self.message

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if field is not UNSET:
            field_dict["field"] = field
        if message is not UNSET:
            field_dict["message"] = message
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field = _parse_field(d.pop("field", UNSET))


        message = d.pop("message", UNSET)

        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        get_vrbo_publish_job_response_200_job_sections_item_errors_item = cls(
            field=field,
            message=message,
            code=code,
        )


        get_vrbo_publish_job_response_200_job_sections_item_errors_item.additional_properties = d
        return get_vrbo_publish_job_response_200_job_sections_item_errors_item

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
