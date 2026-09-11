from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.alteration_change import AlterationChange





T = TypeVar("T", bound="ReservationAlterationCreatedPayloadChanges")



@_attrs_define
class ReservationAlterationCreatedPayloadChanges:
    """ Requested deltas keyed by field name (`checkIn`, `checkOut`, `guestCount`, `totalPrice`). Only changed fields
    appear.

        Example:
            {'checkOut': {'from': '2026-06-16', 'to': '2026-06-18'}, 'totalPrice': {'from': '1320.00', 'to': '1760.00'}}

     """

    additional_properties: dict[str, AlterationChange] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.alteration_change import AlterationChange
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.alteration_change import AlterationChange
        d = dict(src_dict)
        reservation_alteration_created_payload_changes = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AlterationChange.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        reservation_alteration_created_payload_changes.additional_properties = additional_properties
        return reservation_alteration_created_payload_changes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> AlterationChange:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: AlterationChange) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
