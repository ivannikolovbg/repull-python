from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_translations_body_set_item import UpdateVrboListingTranslationsBodySetItem





T = TypeVar("T", bound="UpdateVrboListingTranslationsBody")



@_attrs_define
class UpdateVrboListingTranslationsBody:
    """ 
        Attributes:
            set_ (list[UpdateVrboListingTranslationsBodySetItem] | Unset):
            delete (list[str] | Unset):
     """

    set_: list[UpdateVrboListingTranslationsBodySetItem] | Unset = UNSET
    delete: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_translations_body_set_item import UpdateVrboListingTranslationsBodySetItem
        set_: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.set_, Unset):
            set_ = []
            for set_item_data in self.set_:
                set_item = set_item_data.to_dict()
                set_.append(set_item)



        delete: list[str] | Unset = UNSET
        if not isinstance(self.delete, Unset):
            delete = self.delete




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if set_ is not UNSET:
            field_dict["set"] = set_
        if delete is not UNSET:
            field_dict["delete"] = delete

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_translations_body_set_item import UpdateVrboListingTranslationsBodySetItem
        d = dict(src_dict)
        _set_ = d.pop("set", UNSET)
        set_: list[UpdateVrboListingTranslationsBodySetItem] | Unset = UNSET
        if _set_ is not UNSET:
            set_ = []
            for set_item_data in _set_:
                set_item = UpdateVrboListingTranslationsBodySetItem.from_dict(set_item_data)



                set_.append(set_item)


        delete = cast(list[str], d.pop("delete", UNSET))


        update_vrbo_listing_translations_body = cls(
            set_=set_,
            delete=delete,
        )

        return update_vrbo_listing_translations_body

