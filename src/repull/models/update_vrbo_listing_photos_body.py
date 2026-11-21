from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_photos_body_add_item import UpdateVrboListingPhotosBodyAddItem
  from ..models.update_vrbo_listing_photos_body_captions import UpdateVrboListingPhotosBodyCaptions





T = TypeVar("T", bound="UpdateVrboListingPhotosBody")



@_attrs_define
class UpdateVrboListingPhotosBody:
    """ 
        Attributes:
            add (list[UpdateVrboListingPhotosBodyAddItem] | Unset):
            delete (list[str] | Unset):
            captions (UpdateVrboListingPhotosBodyCaptions | Unset): `{photoId: caption}`
            order (list[str] | Unset):
            cover (str | Unset):
     """

    add: list[UpdateVrboListingPhotosBodyAddItem] | Unset = UNSET
    delete: list[str] | Unset = UNSET
    captions: UpdateVrboListingPhotosBodyCaptions | Unset = UNSET
    order: list[str] | Unset = UNSET
    cover: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_photos_body_add_item import UpdateVrboListingPhotosBodyAddItem
        from ..models.update_vrbo_listing_photos_body_captions import UpdateVrboListingPhotosBodyCaptions
        add: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.add, Unset):
            add = []
            for add_item_data in self.add:
                add_item = add_item_data.to_dict()
                add.append(add_item)



        delete: list[str] | Unset = UNSET
        if not isinstance(self.delete, Unset):
            delete = self.delete



        captions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.captions, Unset):
            captions = self.captions.to_dict()

        order: list[str] | Unset = UNSET
        if not isinstance(self.order, Unset):
            order = self.order



        cover = self.cover


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if add is not UNSET:
            field_dict["add"] = add
        if delete is not UNSET:
            field_dict["delete"] = delete
        if captions is not UNSET:
            field_dict["captions"] = captions
        if order is not UNSET:
            field_dict["order"] = order
        if cover is not UNSET:
            field_dict["cover"] = cover

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_photos_body_add_item import UpdateVrboListingPhotosBodyAddItem
        from ..models.update_vrbo_listing_photos_body_captions import UpdateVrboListingPhotosBodyCaptions
        d = dict(src_dict)
        _add = d.pop("add", UNSET)
        add: list[UpdateVrboListingPhotosBodyAddItem] | Unset = UNSET
        if _add is not UNSET:
            add = []
            for add_item_data in _add:
                add_item = UpdateVrboListingPhotosBodyAddItem.from_dict(add_item_data)



                add.append(add_item)


        delete = cast(list[str], d.pop("delete", UNSET))


        _captions = d.pop("captions", UNSET)
        captions: UpdateVrboListingPhotosBodyCaptions | Unset
        if isinstance(_captions,  Unset):
            captions = UNSET
        else:
            captions = UpdateVrboListingPhotosBodyCaptions.from_dict(_captions)




        order = cast(list[str], d.pop("order", UNSET))


        cover = d.pop("cover", UNSET)

        update_vrbo_listing_photos_body = cls(
            add=add,
            delete=delete,
            captions=captions,
            order=order,
            cover=cover,
        )

        return update_vrbo_listing_photos_body

