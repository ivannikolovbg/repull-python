from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.update_booking_charges_body_charges_item import UpdateBookingChargesBodyChargesItem





T = TypeVar("T", bound="UpdateBookingChargesBody")



@_attrs_define
class UpdateBookingChargesBody:
    """ 
        Attributes:
            property_id (str): Booking.com hotel/property id.
            charges (list[UpdateBookingChargesBodyChargesItem]): Full charge set to apply.
     """

    property_id: str
    charges: list[UpdateBookingChargesBodyChargesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_booking_charges_body_charges_item import UpdateBookingChargesBodyChargesItem
        property_id = self.property_id

        charges = []
        for charges_item_data in self.charges:
            charges_item = charges_item_data.to_dict()
            charges.append(charges_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "property_id": property_id,
            "charges": charges,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_booking_charges_body_charges_item import UpdateBookingChargesBodyChargesItem
        d = dict(src_dict)
        property_id = d.pop("property_id")

        charges = []
        _charges = d.pop("charges")
        for charges_item_data in (_charges):
            charges_item = UpdateBookingChargesBodyChargesItem.from_dict(charges_item_data)



            charges.append(charges_item)


        update_booking_charges_body = cls(
            property_id=property_id,
            charges=charges,
        )


        update_booking_charges_body.additional_properties = d
        return update_booking_charges_body

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
