from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetVrboListingVideosResponse200DataItemsItem")



@_attrs_define
class GetVrboListingVideosResponse200DataItemsItem:
    """ 
        Attributes:
            id (str | Unset):
            file_name (None | str | Unset):
            status (None | str | Unset): Vrbo's processing / review status.
            url (None | str | Unset):
            thumbnail (None | str | Unset):
            uploaded_time (None | str | Unset):
            rejected_reasons (Any | Unset): Why Vrbo's review refused the video.
     """

    id: str | Unset = UNSET
    file_name: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    thumbnail: None | str | Unset = UNSET
    uploaded_time: None | str | Unset = UNSET
    rejected_reasons: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        file_name: None | str | Unset
        if isinstance(self.file_name, Unset):
            file_name = UNSET
        else:
            file_name = self.file_name

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        thumbnail: None | str | Unset
        if isinstance(self.thumbnail, Unset):
            thumbnail = UNSET
        else:
            thumbnail = self.thumbnail

        uploaded_time: None | str | Unset
        if isinstance(self.uploaded_time, Unset):
            uploaded_time = UNSET
        else:
            uploaded_time = self.uploaded_time

        rejected_reasons = self.rejected_reasons


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if file_name is not UNSET:
            field_dict["fileName"] = file_name
        if status is not UNSET:
            field_dict["status"] = status
        if url is not UNSET:
            field_dict["url"] = url
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if uploaded_time is not UNSET:
            field_dict["uploadedTime"] = uploaded_time
        if rejected_reasons is not UNSET:
            field_dict["rejectedReasons"] = rejected_reasons

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_file_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file_name = _parse_file_name(d.pop("fileName", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        def _parse_thumbnail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail = _parse_thumbnail(d.pop("thumbnail", UNSET))


        def _parse_uploaded_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uploaded_time = _parse_uploaded_time(d.pop("uploadedTime", UNSET))


        rejected_reasons = d.pop("rejectedReasons", UNSET)

        get_vrbo_listing_videos_response_200_data_items_item = cls(
            id=id,
            file_name=file_name,
            status=status,
            url=url,
            thumbnail=thumbnail,
            uploaded_time=uploaded_time,
            rejected_reasons=rejected_reasons,
        )


        get_vrbo_listing_videos_response_200_data_items_item.additional_properties = d
        return get_vrbo_listing_videos_response_200_data_items_item

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
