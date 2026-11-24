from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="VerifyTiketClaimBody")



@_attrs_define
class VerifyTiketClaimBody:
    """ 
        Attributes:
            session_id (str):
            hotel_id (str): tiket.com Hotel ID.
            name (str | Unset): Optional property name to show until tiket.com's is read.
     """

    session_id: str
    hotel_id: str
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        session_id = self.session_id

        hotel_id = self.hotel_id

        name = self.name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sessionId": session_id,
            "hotelId": hotel_id,
        })
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        session_id = d.pop("sessionId")

        hotel_id = d.pop("hotelId")

        name = d.pop("name", UNSET)

        verify_tiket_claim_body = cls(
            session_id=session_id,
            hotel_id=hotel_id,
            name=name,
        )


        verify_tiket_claim_body.additional_properties = d
        return verify_tiket_claim_body

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
