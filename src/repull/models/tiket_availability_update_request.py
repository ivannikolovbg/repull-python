from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tiket_availability_update_request_type import TiketAvailabilityUpdateRequestType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tiket_ari_update import TiketAriUpdate





T = TypeVar("T", bound="TiketAvailabilityUpdateRequest")



@_attrs_define
class TiketAvailabilityUpdateRequest:
    """ 
        Attributes:
            property_id (str): tiket.com Hotel ID.
            type_ (TiketAvailabilityUpdateRequestType): `availability` — rooms to sell per room type. `rates` — prices per
                room type and rate plan. `restrictions` — stay and arrival rules per room type and rate plan.
            updates (list[TiketAriUpdate]):
            verify (bool | Unset): Read the nights back from tiket.com after the write and report `applied`. `false` skips
                the read-back (`applied: unverified`). Default: True.
     """

    property_id: str
    type_: TiketAvailabilityUpdateRequestType
    updates: list[TiketAriUpdate]
    verify: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tiket_ari_update import TiketAriUpdate
        property_id = self.property_id

        type_ = self.type_.value

        updates = []
        for updates_item_data in self.updates:
            updates_item = updates_item_data.to_dict()
            updates.append(updates_item)



        verify = self.verify


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "property_id": property_id,
            "type": type_,
            "updates": updates,
        })
        if verify is not UNSET:
            field_dict["verify"] = verify

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiket_ari_update import TiketAriUpdate
        d = dict(src_dict)
        property_id = d.pop("property_id")

        type_ = TiketAvailabilityUpdateRequestType(d.pop("type"))




        updates = []
        _updates = d.pop("updates")
        for updates_item_data in (_updates):
            updates_item = TiketAriUpdate.from_dict(updates_item_data)



            updates.append(updates_item)


        verify = d.pop("verify", UNSET)

        tiket_availability_update_request = cls(
            property_id=property_id,
            type_=type_,
            updates=updates,
            verify=verify,
        )


        tiket_availability_update_request.additional_properties = d
        return tiket_availability_update_request

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
