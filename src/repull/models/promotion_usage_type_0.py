from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.promotion_usage_type_0_last_applied_amount import PromotionUsageType0LastAppliedAmount
  from ..models.promotion_usage_type_0_revenue import PromotionUsageType0Revenue





T = TypeVar("T", bound="PromotionUsageType0")



@_attrs_define
class PromotionUsageType0:
    """ 
        Attributes:
            bookings (int | Unset):
            room_nights (int | Unset):
            cancellations (int | Unset):
            revenue (PromotionUsageType0Revenue | Unset):
            last_applied_at (datetime.datetime | Unset): Airbnb Custom promotion: when it was last applied to a booking.
            last_applied_amount (PromotionUsageType0LastAppliedAmount | Unset):
     """

    bookings: int | Unset = UNSET
    room_nights: int | Unset = UNSET
    cancellations: int | Unset = UNSET
    revenue: PromotionUsageType0Revenue | Unset = UNSET
    last_applied_at: datetime.datetime | Unset = UNSET
    last_applied_amount: PromotionUsageType0LastAppliedAmount | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.promotion_usage_type_0_last_applied_amount import PromotionUsageType0LastAppliedAmount
        from ..models.promotion_usage_type_0_revenue import PromotionUsageType0Revenue
        bookings = self.bookings

        room_nights = self.room_nights

        cancellations = self.cancellations

        revenue: dict[str, Any] | Unset = UNSET
        if not isinstance(self.revenue, Unset):
            revenue = self.revenue.to_dict()

        last_applied_at: str | Unset = UNSET
        if not isinstance(self.last_applied_at, Unset):
            last_applied_at = self.last_applied_at.isoformat()

        last_applied_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_applied_amount, Unset):
            last_applied_amount = self.last_applied_amount.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bookings is not UNSET:
            field_dict["bookings"] = bookings
        if room_nights is not UNSET:
            field_dict["roomNights"] = room_nights
        if cancellations is not UNSET:
            field_dict["cancellations"] = cancellations
        if revenue is not UNSET:
            field_dict["revenue"] = revenue
        if last_applied_at is not UNSET:
            field_dict["lastAppliedAt"] = last_applied_at
        if last_applied_amount is not UNSET:
            field_dict["lastAppliedAmount"] = last_applied_amount

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promotion_usage_type_0_last_applied_amount import PromotionUsageType0LastAppliedAmount
        from ..models.promotion_usage_type_0_revenue import PromotionUsageType0Revenue
        d = dict(src_dict)
        bookings = d.pop("bookings", UNSET)

        room_nights = d.pop("roomNights", UNSET)

        cancellations = d.pop("cancellations", UNSET)

        _revenue = d.pop("revenue", UNSET)
        revenue: PromotionUsageType0Revenue | Unset
        if isinstance(_revenue,  Unset):
            revenue = UNSET
        else:
            revenue = PromotionUsageType0Revenue.from_dict(_revenue)




        _last_applied_at = d.pop("lastAppliedAt", UNSET)
        last_applied_at: datetime.datetime | Unset
        if isinstance(_last_applied_at,  Unset):
            last_applied_at = UNSET
        else:
            last_applied_at = isoparse(_last_applied_at)




        _last_applied_amount = d.pop("lastAppliedAmount", UNSET)
        last_applied_amount: PromotionUsageType0LastAppliedAmount | Unset
        if isinstance(_last_applied_amount,  Unset):
            last_applied_amount = UNSET
        else:
            last_applied_amount = PromotionUsageType0LastAppliedAmount.from_dict(_last_applied_amount)




        promotion_usage_type_0 = cls(
            bookings=bookings,
            room_nights=room_nights,
            cancellations=cancellations,
            revenue=revenue,
            last_applied_at=last_applied_at,
            last_applied_amount=last_applied_amount,
        )


        promotion_usage_type_0.additional_properties = d
        return promotion_usage_type_0

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
