from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetVrboPublishJobResponse200JobRejectedPhotosItem")



@_attrs_define
class GetVrboPublishJobResponse200JobRejectedPhotosItem:
    """ 
        Attributes:
            photo (int | None | Unset):
            reason (str | Unset):
     """

    photo: int | None | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        photo: int | None | Unset
        if isinstance(self.photo, Unset):
            photo = UNSET
        else:
            photo = self.photo

        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if photo is not UNSET:
            field_dict["photo"] = photo
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_photo(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        photo = _parse_photo(d.pop("photo", UNSET))


        reason = d.pop("reason", UNSET)

        get_vrbo_publish_job_response_200_job_rejected_photos_item = cls(
            photo=photo,
            reason=reason,
        )


        get_vrbo_publish_job_response_200_job_rejected_photos_item.additional_properties = d
        return get_vrbo_publish_job_response_200_job_rejected_photos_item

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
