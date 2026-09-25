from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.set_listing_markup_body_channel import SetListingMarkupBodyChannel
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SetListingMarkupBody")



@_attrs_define
class SetListingMarkupBody:
    """ 
        Attributes:
            channel (SetListingMarkupBodyChannel):
            markup_percent (float | None): 15 = +15%. `null` removes the markup.
            hotel_id (str | Unset): Booking.com property — required when the listing is on more than one.
     """

    channel: SetListingMarkupBodyChannel
    markup_percent: float | None
    hotel_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        channel = self.channel.value

        markup_percent: float | None
        markup_percent = self.markup_percent

        hotel_id = self.hotel_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "channel": channel,
            "markupPercent": markup_percent,
        })
        if hotel_id is not UNSET:
            field_dict["hotelId"] = hotel_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = SetListingMarkupBodyChannel(d.pop("channel"))




        def _parse_markup_percent(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        markup_percent = _parse_markup_percent(d.pop("markupPercent"))


        hotel_id = d.pop("hotelId", UNSET)

        set_listing_markup_body = cls(
            channel=channel,
            markup_percent=markup_percent,
            hotel_id=hotel_id,
        )


        set_listing_markup_body.additional_properties = d
        return set_listing_markup_body

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
