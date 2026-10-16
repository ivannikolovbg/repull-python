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
  from ..models.promotion_rules_blackout_dates_quota import PromotionRulesBlackoutDatesQuota
  from ..models.promotion_rules_booking_window import PromotionRulesBookingWindow
  from ..models.promotion_rules_last_minute import PromotionRulesLastMinute
  from ..models.promotion_rules_stay_window import PromotionRulesStayWindow





T = TypeVar("T", bound="PromotionRules")



@_attrs_define
class PromotionRules:
    """ Which rules a type supports depends on the channel — see the catalog.

        Attributes:
            campaign (str | Unset): Booking.com campaigns: `black_friday`, `getaway`, `late_escape`, `early_year`.
            audience (str | Unset): `public`, `subscribers` (members only, at least 10%), `app`, `all` (app and mobile web),
                or a country id from the catalog (e.g. `united_kingdom_pos`).
            stay_window (PromotionRulesStayWindow | Unset):
            booking_window (PromotionRulesBookingWindow | Unset):
            last_minute (PromotionRulesLastMinute | Unset):
            early_booker_days (int | Unset):
            min_nights (int | Unset):
            non_refundable (bool | Unset):
            blackout_dates (list[datetime.date] | Unset): Airbnb — not yet available.
            blackout_dates_quota (PromotionRulesBlackoutDatesQuota | Unset):
     """

    campaign: str | Unset = UNSET
    audience: str | Unset = UNSET
    stay_window: PromotionRulesStayWindow | Unset = UNSET
    booking_window: PromotionRulesBookingWindow | Unset = UNSET
    last_minute: PromotionRulesLastMinute | Unset = UNSET
    early_booker_days: int | Unset = UNSET
    min_nights: int | Unset = UNSET
    non_refundable: bool | Unset = UNSET
    blackout_dates: list[datetime.date] | Unset = UNSET
    blackout_dates_quota: PromotionRulesBlackoutDatesQuota | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.promotion_rules_blackout_dates_quota import PromotionRulesBlackoutDatesQuota
        from ..models.promotion_rules_booking_window import PromotionRulesBookingWindow
        from ..models.promotion_rules_last_minute import PromotionRulesLastMinute
        from ..models.promotion_rules_stay_window import PromotionRulesStayWindow
        campaign = self.campaign

        audience = self.audience

        stay_window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stay_window, Unset):
            stay_window = self.stay_window.to_dict()

        booking_window: dict[str, Any] | Unset = UNSET
        if not isinstance(self.booking_window, Unset):
            booking_window = self.booking_window.to_dict()

        last_minute: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_minute, Unset):
            last_minute = self.last_minute.to_dict()

        early_booker_days = self.early_booker_days

        min_nights = self.min_nights

        non_refundable = self.non_refundable

        blackout_dates: list[str] | Unset = UNSET
        if not isinstance(self.blackout_dates, Unset):
            blackout_dates = []
            for blackout_dates_item_data in self.blackout_dates:
                blackout_dates_item = blackout_dates_item_data.isoformat()
                blackout_dates.append(blackout_dates_item)



        blackout_dates_quota: dict[str, Any] | Unset = UNSET
        if not isinstance(self.blackout_dates_quota, Unset):
            blackout_dates_quota = self.blackout_dates_quota.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if audience is not UNSET:
            field_dict["audience"] = audience
        if stay_window is not UNSET:
            field_dict["stayWindow"] = stay_window
        if booking_window is not UNSET:
            field_dict["bookingWindow"] = booking_window
        if last_minute is not UNSET:
            field_dict["lastMinute"] = last_minute
        if early_booker_days is not UNSET:
            field_dict["earlyBookerDays"] = early_booker_days
        if min_nights is not UNSET:
            field_dict["minNights"] = min_nights
        if non_refundable is not UNSET:
            field_dict["nonRefundable"] = non_refundable
        if blackout_dates is not UNSET:
            field_dict["blackoutDates"] = blackout_dates
        if blackout_dates_quota is not UNSET:
            field_dict["blackoutDatesQuota"] = blackout_dates_quota

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promotion_rules_blackout_dates_quota import PromotionRulesBlackoutDatesQuota
        from ..models.promotion_rules_booking_window import PromotionRulesBookingWindow
        from ..models.promotion_rules_last_minute import PromotionRulesLastMinute
        from ..models.promotion_rules_stay_window import PromotionRulesStayWindow
        d = dict(src_dict)
        campaign = d.pop("campaign", UNSET)

        audience = d.pop("audience", UNSET)

        _stay_window = d.pop("stayWindow", UNSET)
        stay_window: PromotionRulesStayWindow | Unset
        if isinstance(_stay_window,  Unset):
            stay_window = UNSET
        else:
            stay_window = PromotionRulesStayWindow.from_dict(_stay_window)




        _booking_window = d.pop("bookingWindow", UNSET)
        booking_window: PromotionRulesBookingWindow | Unset
        if isinstance(_booking_window,  Unset):
            booking_window = UNSET
        else:
            booking_window = PromotionRulesBookingWindow.from_dict(_booking_window)




        _last_minute = d.pop("lastMinute", UNSET)
        last_minute: PromotionRulesLastMinute | Unset
        if isinstance(_last_minute,  Unset):
            last_minute = UNSET
        else:
            last_minute = PromotionRulesLastMinute.from_dict(_last_minute)




        early_booker_days = d.pop("earlyBookerDays", UNSET)

        min_nights = d.pop("minNights", UNSET)

        non_refundable = d.pop("nonRefundable", UNSET)

        _blackout_dates = d.pop("blackoutDates", UNSET)
        blackout_dates: list[datetime.date] | Unset = UNSET
        if _blackout_dates is not UNSET:
            blackout_dates = []
            for blackout_dates_item_data in _blackout_dates:
                blackout_dates_item = isoparse(blackout_dates_item_data).date()



                blackout_dates.append(blackout_dates_item)


        _blackout_dates_quota = d.pop("blackoutDatesQuota", UNSET)
        blackout_dates_quota: PromotionRulesBlackoutDatesQuota | Unset
        if isinstance(_blackout_dates_quota,  Unset):
            blackout_dates_quota = UNSET
        else:
            blackout_dates_quota = PromotionRulesBlackoutDatesQuota.from_dict(_blackout_dates_quota)




        promotion_rules = cls(
            campaign=campaign,
            audience=audience,
            stay_window=stay_window,
            booking_window=booking_window,
            last_minute=last_minute,
            early_booker_days=early_booker_days,
            min_nights=min_nights,
            non_refundable=non_refundable,
            blackout_dates=blackout_dates,
            blackout_dates_quota=blackout_dates_quota,
        )


        promotion_rules.additional_properties = d
        return promotion_rules

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
