from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetListingMarkupsResponse200BookingItem")



@_attrs_define
class GetListingMarkupsResponse200BookingItem:
    """ 
        Attributes:
            hotel_id (str | Unset): Booking.com property id.
            markup_percent (float | None | Unset): Percent added on Booking.com, for every listing on this property.
                Example: 18.
            listing_ids (list[str] | Unset): Listings in this workspace priced through this property — all share this
                markup.
     """

    hotel_id: str | Unset = UNSET
    markup_percent: float | None | Unset = UNSET
    listing_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        hotel_id = self.hotel_id

        markup_percent: float | None | Unset
        if isinstance(self.markup_percent, Unset):
            markup_percent = UNSET
        else:
            markup_percent = self.markup_percent

        listing_ids: list[str] | Unset = UNSET
        if not isinstance(self.listing_ids, Unset):
            listing_ids = self.listing_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hotel_id is not UNSET:
            field_dict["hotelId"] = hotel_id
        if markup_percent is not UNSET:
            field_dict["markupPercent"] = markup_percent
        if listing_ids is not UNSET:
            field_dict["listingIds"] = listing_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hotel_id = d.pop("hotelId", UNSET)

        def _parse_markup_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        markup_percent = _parse_markup_percent(d.pop("markupPercent", UNSET))


        listing_ids = cast(list[str], d.pop("listingIds", UNSET))


        get_listing_markups_response_200_booking_item = cls(
            hotel_id=hotel_id,
            markup_percent=markup_percent,
            listing_ids=listing_ids,
        )


        get_listing_markups_response_200_booking_item.additional_properties = d
        return get_listing_markups_response_200_booking_item

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
