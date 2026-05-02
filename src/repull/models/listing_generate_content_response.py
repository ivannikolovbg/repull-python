from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_content import ListingContent





T = TypeVar("T", bound="ListingGenerateContentResponse")



@_attrs_define
class ListingGenerateContentResponse:
    """ 
        Attributes:
            listing_id (int | Unset):
            persisted (bool | Unset):
            content (ListingContent | Unset):
     """

    listing_id: int | Unset = UNSET
    persisted: bool | Unset = UNSET
    content: ListingContent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_content import ListingContent
        listing_id = self.listing_id

        persisted = self.persisted

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if persisted is not UNSET:
            field_dict["persisted"] = persisted
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_content import ListingContent
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        persisted = d.pop("persisted", UNSET)

        _content = d.pop("content", UNSET)
        content: ListingContent | Unset
        if isinstance(_content,  Unset):
            content = UNSET
        else:
            content = ListingContent.from_dict(_content)




        listing_generate_content_response = cls(
            listing_id=listing_id,
            persisted=persisted,
            content=content,
        )


        listing_generate_content_response.additional_properties = d
        return listing_generate_content_response

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
