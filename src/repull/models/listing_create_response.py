from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="ListingCreateResponse")



@_attrs_define
class ListingCreateResponse:
    """ 
        Attributes:
            id (str | Unset): New listing ID — use for follow-up generate-content / publish calls
            calendar_days_seeded (int | Unset): Nights of calendar written from the price you stated. `0` means the listing
                has no calendar and a publish will send no availability — state `defaultDailyPrice` on the create, or set it
                later with `PUT /v1/listings/{id}/content` under `pricing`.
     """

    id: str | Unset = UNSET
    calendar_days_seeded: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        calendar_days_seeded = self.calendar_days_seeded


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if calendar_days_seeded is not UNSET:
            field_dict["calendarDaysSeeded"] = calendar_days_seeded

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        calendar_days_seeded = d.pop("calendarDaysSeeded", UNSET)

        listing_create_response = cls(
            id=id,
            calendar_days_seeded=calendar_days_seeded,
        )


        listing_create_response.additional_properties = d
        return listing_create_response

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
