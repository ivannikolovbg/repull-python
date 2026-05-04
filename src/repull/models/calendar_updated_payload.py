from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.calendar_updated_payload_range import CalendarUpdatedPayloadRange





T = TypeVar("T", bound="CalendarUpdatedPayload")



@_attrs_define
class CalendarUpdatedPayload:
    """ Payload for `calendar.updated`. Availability or pricing for a listing was updated.

        Attributes:
            listing_id (int | Unset):  Example: 6250.
            range_ (CalendarUpdatedPayloadRange | Unset):
            affected_dates (int | Unset):  Example: 14.
            pricing_changed (bool | Unset):  Example: True.
            availability_changed (bool | Unset):
     """

    listing_id: int | Unset = UNSET
    range_: CalendarUpdatedPayloadRange | Unset = UNSET
    affected_dates: int | Unset = UNSET
    pricing_changed: bool | Unset = UNSET
    availability_changed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.calendar_updated_payload_range import CalendarUpdatedPayloadRange
        listing_id = self.listing_id

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        affected_dates = self.affected_dates

        pricing_changed = self.pricing_changed

        availability_changed = self.availability_changed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if range_ is not UNSET:
            field_dict["range"] = range_
        if affected_dates is not UNSET:
            field_dict["affectedDates"] = affected_dates
        if pricing_changed is not UNSET:
            field_dict["pricingChanged"] = pricing_changed
        if availability_changed is not UNSET:
            field_dict["availabilityChanged"] = availability_changed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.calendar_updated_payload_range import CalendarUpdatedPayloadRange
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        _range_ = d.pop("range", UNSET)
        range_: CalendarUpdatedPayloadRange | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = CalendarUpdatedPayloadRange.from_dict(_range_)




        affected_dates = d.pop("affectedDates", UNSET)

        pricing_changed = d.pop("pricingChanged", UNSET)

        availability_changed = d.pop("availabilityChanged", UNSET)

        calendar_updated_payload = cls(
            listing_id=listing_id,
            range_=range_,
            affected_dates=affected_dates,
            pricing_changed=pricing_changed,
            availability_changed=availability_changed,
        )


        calendar_updated_payload.additional_properties = d
        return calendar_updated_payload

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
