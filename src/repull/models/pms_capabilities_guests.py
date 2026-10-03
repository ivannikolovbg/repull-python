from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PmsCapabilitiesGuests")



@_attrs_define
class PmsCapabilitiesGuests:
    """ 
        Attributes:
            create (bool | Unset): `POST /v1/guests` with `provider`.
            update (bool | Unset): `PATCH /v1/guests/{id}` on a guest linked to this PMS.
     """

    create: bool | Unset = UNSET
    update: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        create = self.create

        update = self.update


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if create is not UNSET:
            field_dict["create"] = create
        if update is not UNSET:
            field_dict["update"] = update

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create = d.pop("create", UNSET)

        update = d.pop("update", UNSET)

        pms_capabilities_guests = cls(
            create=create,
            update=update,
        )


        pms_capabilities_guests.additional_properties = d
        return pms_capabilities_guests

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
