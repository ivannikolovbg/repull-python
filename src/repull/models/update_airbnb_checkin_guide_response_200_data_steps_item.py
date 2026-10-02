from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateAirbnbCheckinGuideResponse200DataStepsItem")



@_attrs_define
class UpdateAirbnbCheckinGuideResponse200DataStepsItem:
    """ 
        Attributes:
            id (int | Unset):
            notes (None | str | Unset):
            media_url (None | str | Unset):
     """

    id: int | Unset = UNSET
    notes: None | str | Unset = UNSET
    media_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        media_url: None | str | Unset
        if isinstance(self.media_url, Unset):
            media_url = UNSET
        else:
            media_url = self.media_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if media_url is not UNSET:
            field_dict["mediaUrl"] = media_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_media_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        media_url = _parse_media_url(d.pop("mediaUrl", UNSET))


        update_airbnb_checkin_guide_response_200_data_steps_item = cls(
            id=id,
            notes=notes,
            media_url=media_url,
        )


        update_airbnb_checkin_guide_response_200_data_steps_item.additional_properties = d
        return update_airbnb_checkin_guide_response_200_data_steps_item

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
