from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PmsCapabilitiesReservations")



@_attrs_define
class PmsCapabilitiesReservations:
    """ 
        Attributes:
            respond (bool | Unset): `POST /v1/reservations/{id}/accept|decline` on requests this PMS relays.
            preapprove (bool | Unset): `POST /v1/conversations/{id}/pre-approval` on inquiries this PMS relays.
     """

    respond: bool | Unset = UNSET
    preapprove: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        respond = self.respond

        preapprove = self.preapprove


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if respond is not UNSET:
            field_dict["respond"] = respond
        if preapprove is not UNSET:
            field_dict["preapprove"] = preapprove

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        respond = d.pop("respond", UNSET)

        preapprove = d.pop("preapprove", UNSET)

        pms_capabilities_reservations = cls(
            respond=respond,
            preapprove=preapprove,
        )


        pms_capabilities_reservations.additional_properties = d
        return pms_capabilities_reservations

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
