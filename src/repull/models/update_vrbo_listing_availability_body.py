from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_vrbo_listing_availability_body_type import UpdateVrboListingAvailabilityBodyType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_availability_body_operations_item import UpdateVrboListingAvailabilityBodyOperationsItem





T = TypeVar("T", bound="UpdateVrboListingAvailabilityBody")



@_attrs_define
class UpdateVrboListingAvailabilityBody:
    """ 
        Attributes:
            operations (list[UpdateVrboListingAvailabilityBodyOperationsItem]):
            type_ (UpdateVrboListingAvailabilityBodyType | Unset):  Default: UpdateVrboListingAvailabilityBodyType.CALENDAR.
     """

    operations: list[UpdateVrboListingAvailabilityBodyOperationsItem]
    type_: UpdateVrboListingAvailabilityBodyType | Unset = UpdateVrboListingAvailabilityBodyType.CALENDAR





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_availability_body_operations_item import UpdateVrboListingAvailabilityBodyOperationsItem
        operations = []
        for operations_item_data in self.operations:
            operations_item = operations_item_data.to_dict()
            operations.append(operations_item)



        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "operations": operations,
        })
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_availability_body_operations_item import UpdateVrboListingAvailabilityBodyOperationsItem
        d = dict(src_dict)
        operations = []
        _operations = d.pop("operations")
        for operations_item_data in (_operations):
            operations_item = UpdateVrboListingAvailabilityBodyOperationsItem.from_dict(operations_item_data)



            operations.append(operations_item)


        _type_ = d.pop("type", UNSET)
        type_: UpdateVrboListingAvailabilityBodyType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = UpdateVrboListingAvailabilityBodyType(_type_)




        update_vrbo_listing_availability_body = cls(
            operations=operations,
            type_=type_,
        )

        return update_vrbo_listing_availability_body

