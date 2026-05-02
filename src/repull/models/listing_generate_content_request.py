from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_generate_content_request_style import ListingGenerateContentRequestStyle
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingGenerateContentRequest")



@_attrs_define
class ListingGenerateContentRequest:
    """ 
        Attributes:
            photos (list[str] | Unset): Up to 8 reference photos. When present, Kimi K2 vision is used for grounded copy.
            style (ListingGenerateContentRequestStyle | Unset):  Default: ListingGenerateContentRequestStyle.WARM.
            persist (bool | Unset): Save the generated content to the listing (so subsequent publishes pick it up). Default:
                True.
     """

    photos: list[str] | Unset = UNSET
    style: ListingGenerateContentRequestStyle | Unset = ListingGenerateContentRequestStyle.WARM
    persist: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        photos: list[str] | Unset = UNSET
        if not isinstance(self.photos, Unset):
            photos = self.photos



        style: str | Unset = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.value


        persist = self.persist


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if photos is not UNSET:
            field_dict["photos"] = photos
        if style is not UNSET:
            field_dict["style"] = style
        if persist is not UNSET:
            field_dict["persist"] = persist

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        photos = cast(list[str], d.pop("photos", UNSET))


        _style = d.pop("style", UNSET)
        style: ListingGenerateContentRequestStyle | Unset
        if isinstance(_style,  Unset):
            style = UNSET
        else:
            style = ListingGenerateContentRequestStyle(_style)




        persist = d.pop("persist", UNSET)

        listing_generate_content_request = cls(
            photos=photos,
            style=style,
            persist=persist,
        )


        listing_generate_content_request.additional_properties = d
        return listing_generate_content_request

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
