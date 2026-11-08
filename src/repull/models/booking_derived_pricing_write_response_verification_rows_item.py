from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_occupancy_rule import BookingOccupancyRule





T = TypeVar("T", bound="BookingDerivedPricingWriteResponseVerificationRowsItem")



@_attrs_define
class BookingDerivedPricingWriteResponseVerificationRowsItem:
    """ 
        Attributes:
            room_id (str | Unset):
            rate_id (str | Unset):
            expected (list[BookingOccupancyRule] | Unset):
            booking (list[BookingOccupancyRule] | None | Unset):
            match (bool | Unset):
     """

    room_id: str | Unset = UNSET
    rate_id: str | Unset = UNSET
    expected: list[BookingOccupancyRule] | Unset = UNSET
    booking: list[BookingOccupancyRule] | None | Unset = UNSET
    match: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_occupancy_rule import BookingOccupancyRule
        room_id = self.room_id

        rate_id = self.rate_id

        expected: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.expected, Unset):
            expected = []
            for expected_item_data in self.expected:
                expected_item = expected_item_data.to_dict()
                expected.append(expected_item)



        booking: list[dict[str, Any]] | None | Unset
        if isinstance(self.booking, Unset):
            booking = UNSET
        elif isinstance(self.booking, list):
            booking = []
            for booking_type_0_item_data in self.booking:
                booking_type_0_item = booking_type_0_item_data.to_dict()
                booking.append(booking_type_0_item)


        else:
            booking = self.booking

        match = self.match


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if rate_id is not UNSET:
            field_dict["rateId"] = rate_id
        if expected is not UNSET:
            field_dict["expected"] = expected
        if booking is not UNSET:
            field_dict["booking"] = booking
        if match is not UNSET:
            field_dict["match"] = match

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_occupancy_rule import BookingOccupancyRule
        d = dict(src_dict)
        room_id = d.pop("roomId", UNSET)

        rate_id = d.pop("rateId", UNSET)

        _expected = d.pop("expected", UNSET)
        expected: list[BookingOccupancyRule] | Unset = UNSET
        if _expected is not UNSET:
            expected = []
            for expected_item_data in _expected:
                expected_item = BookingOccupancyRule.from_dict(expected_item_data)



                expected.append(expected_item)


        def _parse_booking(data: object) -> list[BookingOccupancyRule] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                booking_type_0 = []
                _booking_type_0 = data
                for booking_type_0_item_data in (_booking_type_0):
                    booking_type_0_item = BookingOccupancyRule.from_dict(booking_type_0_item_data)



                    booking_type_0.append(booking_type_0_item)

                return booking_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[BookingOccupancyRule] | None | Unset, data)

        booking = _parse_booking(d.pop("booking", UNSET))


        match = d.pop("match", UNSET)

        booking_derived_pricing_write_response_verification_rows_item = cls(
            room_id=room_id,
            rate_id=rate_id,
            expected=expected,
            booking=booking,
            match=match,
        )


        booking_derived_pricing_write_response_verification_rows_item.additional_properties = d
        return booking_derived_pricing_write_response_verification_rows_item

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
