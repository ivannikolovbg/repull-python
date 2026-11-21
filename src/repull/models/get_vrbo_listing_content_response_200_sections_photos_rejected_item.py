from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetVrboListingContentResponse200SectionsPhotosRejectedItem")



@_attrs_define
class GetVrboListingContentResponse200SectionsPhotosRejectedItem:
    """ 
        Attributes:
            id (str | Unset):
            url (None | str | Unset):
            reason (str | Unset):
     """

    id: str | Unset = UNSET
    url: None | str | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        reason = d.pop("reason", UNSET)

        get_vrbo_listing_content_response_200_sections_photos_rejected_item = cls(
            id=id,
            url=url,
            reason=reason,
        )


        get_vrbo_listing_content_response_200_sections_photos_rejected_item.additional_properties = d
        return get_vrbo_listing_content_response_200_sections_photos_rejected_item

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
