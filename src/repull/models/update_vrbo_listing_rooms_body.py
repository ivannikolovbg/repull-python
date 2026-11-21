from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_rooms_body_add_item import UpdateVrboListingRoomsBodyAddItem
  from ..models.update_vrbo_listing_rooms_body_update_item import UpdateVrboListingRoomsBodyUpdateItem





T = TypeVar("T", bound="UpdateVrboListingRoomsBody")



@_attrs_define
class UpdateVrboListingRoomsBody:
    """ 
        Attributes:
            add (list[UpdateVrboListingRoomsBodyAddItem] | Unset):
            update (list[UpdateVrboListingRoomsBodyUpdateItem] | Unset):
            delete (list[str] | Unset):
     """

    add: list[UpdateVrboListingRoomsBodyAddItem] | Unset = UNSET
    update: list[UpdateVrboListingRoomsBodyUpdateItem] | Unset = UNSET
    delete: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_rooms_body_add_item import UpdateVrboListingRoomsBodyAddItem
        from ..models.update_vrbo_listing_rooms_body_update_item import UpdateVrboListingRoomsBodyUpdateItem
        add: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.add, Unset):
            add = []
            for add_item_data in self.add:
                add_item = add_item_data.to_dict()
                add.append(add_item)



        update: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.update, Unset):
            update = []
            for update_item_data in self.update:
                update_item = update_item_data.to_dict()
                update.append(update_item)



        delete: list[str] | Unset = UNSET
        if not isinstance(self.delete, Unset):
            delete = self.delete




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if add is not UNSET:
            field_dict["add"] = add
        if update is not UNSET:
            field_dict["update"] = update
        if delete is not UNSET:
            field_dict["delete"] = delete

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_rooms_body_add_item import UpdateVrboListingRoomsBodyAddItem
        from ..models.update_vrbo_listing_rooms_body_update_item import UpdateVrboListingRoomsBodyUpdateItem
        d = dict(src_dict)
        _add = d.pop("add", UNSET)
        add: list[UpdateVrboListingRoomsBodyAddItem] | Unset = UNSET
        if _add is not UNSET:
            add = []
            for add_item_data in _add:
                add_item = UpdateVrboListingRoomsBodyAddItem.from_dict(add_item_data)



                add.append(add_item)


        _update = d.pop("update", UNSET)
        update: list[UpdateVrboListingRoomsBodyUpdateItem] | Unset = UNSET
        if _update is not UNSET:
            update = []
            for update_item_data in _update:
                update_item = UpdateVrboListingRoomsBodyUpdateItem.from_dict(update_item_data)



                update.append(update_item)


        delete = cast(list[str], d.pop("delete", UNSET))


        update_vrbo_listing_rooms_body = cls(
            add=add,
            update=update,
            delete=delete,
        )

        return update_vrbo_listing_rooms_body

