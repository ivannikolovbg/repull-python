from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_pricing_strategy_comp_position_target import ListingPricingStrategyCompPositionTarget
from ..models.listing_pricing_strategy_mode import ListingPricingStrategyMode
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_pricing_strategy_day_of_week_multipliers import ListingPricingStrategyDayOfWeekMultipliers





T = TypeVar("T", bound="ListingPricingStrategy")



@_attrs_define
class ListingPricingStrategy:
    """ Strategy that constrains the Atlas pricing model for one listing.

        Attributes:
            id (None | str | Unset):
            listing_id (str | Unset):
            customer_id (str | Unset):
            mode (ListingPricingStrategyMode | Unset): `recommend` surfaces suggestions; `auto` applies them on the next
                sync.
            min_price (float | None | Unset):
            max_price (float | None | Unset):
            max_daily_change_pct (float | Unset): Max day-over-day swing in %. Default: 15.0.
            weekend_markup_pct (float | None | Unset): % bump applied on Fri/Sat.
            day_of_week_multipliers (ListingPricingStrategyDayOfWeekMultipliers | Unset): Multiplier per ISO weekday key
                (0..6).
            target_occupancy_pct (float | None | Unset):
            target_monthly_revenue (float | None | Unset):
            owner_min_monthly_payout (float | None | Unset):
            comp_position_target (ListingPricingStrategyCompPositionTarget | Unset):  Default:
                ListingPricingStrategyCompPositionTarget.MATCH.
            comp_adjust_pct (float | Unset): Extra adjustment vs comp median (-30..+30). Default: 0.0.
            event_boost_enabled (bool | Unset):  Default: True.
            event_boost_max_pct (float | Unset):  Default: 30.0.
            is_default (bool | Unset): true when no row exists yet and the response is server-side defaults.
     """

    id: None | str | Unset = UNSET
    listing_id: str | Unset = UNSET
    customer_id: str | Unset = UNSET
    mode: ListingPricingStrategyMode | Unset = UNSET
    min_price: float | None | Unset = UNSET
    max_price: float | None | Unset = UNSET
    max_daily_change_pct: float | Unset = 15.0
    weekend_markup_pct: float | None | Unset = UNSET
    day_of_week_multipliers: ListingPricingStrategyDayOfWeekMultipliers | Unset = UNSET
    target_occupancy_pct: float | None | Unset = UNSET
    target_monthly_revenue: float | None | Unset = UNSET
    owner_min_monthly_payout: float | None | Unset = UNSET
    comp_position_target: ListingPricingStrategyCompPositionTarget | Unset = ListingPricingStrategyCompPositionTarget.MATCH
    comp_adjust_pct: float | Unset = 0.0
    event_boost_enabled: bool | Unset = True
    event_boost_max_pct: float | Unset = 30.0
    is_default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_pricing_strategy_day_of_week_multipliers import ListingPricingStrategyDayOfWeekMultipliers
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        listing_id = self.listing_id

        customer_id = self.customer_id

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value


        min_price: float | None | Unset
        if isinstance(self.min_price, Unset):
            min_price = UNSET
        else:
            min_price = self.min_price

        max_price: float | None | Unset
        if isinstance(self.max_price, Unset):
            max_price = UNSET
        else:
            max_price = self.max_price

        max_daily_change_pct = self.max_daily_change_pct

        weekend_markup_pct: float | None | Unset
        if isinstance(self.weekend_markup_pct, Unset):
            weekend_markup_pct = UNSET
        else:
            weekend_markup_pct = self.weekend_markup_pct

        day_of_week_multipliers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.day_of_week_multipliers, Unset):
            day_of_week_multipliers = self.day_of_week_multipliers.to_dict()

        target_occupancy_pct: float | None | Unset
        if isinstance(self.target_occupancy_pct, Unset):
            target_occupancy_pct = UNSET
        else:
            target_occupancy_pct = self.target_occupancy_pct

        target_monthly_revenue: float | None | Unset
        if isinstance(self.target_monthly_revenue, Unset):
            target_monthly_revenue = UNSET
        else:
            target_monthly_revenue = self.target_monthly_revenue

        owner_min_monthly_payout: float | None | Unset
        if isinstance(self.owner_min_monthly_payout, Unset):
            owner_min_monthly_payout = UNSET
        else:
            owner_min_monthly_payout = self.owner_min_monthly_payout

        comp_position_target: str | Unset = UNSET
        if not isinstance(self.comp_position_target, Unset):
            comp_position_target = self.comp_position_target.value


        comp_adjust_pct = self.comp_adjust_pct

        event_boost_enabled = self.event_boost_enabled

        event_boost_max_pct = self.event_boost_max_pct

        is_default = self.is_default


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if mode is not UNSET:
            field_dict["mode"] = mode
        if min_price is not UNSET:
            field_dict["minPrice"] = min_price
        if max_price is not UNSET:
            field_dict["maxPrice"] = max_price
        if max_daily_change_pct is not UNSET:
            field_dict["maxDailyChangePct"] = max_daily_change_pct
        if weekend_markup_pct is not UNSET:
            field_dict["weekendMarkupPct"] = weekend_markup_pct
        if day_of_week_multipliers is not UNSET:
            field_dict["dayOfWeekMultipliers"] = day_of_week_multipliers
        if target_occupancy_pct is not UNSET:
            field_dict["targetOccupancyPct"] = target_occupancy_pct
        if target_monthly_revenue is not UNSET:
            field_dict["targetMonthlyRevenue"] = target_monthly_revenue
        if owner_min_monthly_payout is not UNSET:
            field_dict["ownerMinMonthlyPayout"] = owner_min_monthly_payout
        if comp_position_target is not UNSET:
            field_dict["compPositionTarget"] = comp_position_target
        if comp_adjust_pct is not UNSET:
            field_dict["compAdjustPct"] = comp_adjust_pct
        if event_boost_enabled is not UNSET:
            field_dict["eventBoostEnabled"] = event_boost_enabled
        if event_boost_max_pct is not UNSET:
            field_dict["eventBoostMaxPct"] = event_boost_max_pct
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_pricing_strategy_day_of_week_multipliers import ListingPricingStrategyDayOfWeekMultipliers
        d = dict(src_dict)
        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        listing_id = d.pop("listingId", UNSET)

        customer_id = d.pop("customerId", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: ListingPricingStrategyMode | Unset
        if isinstance(_mode,  Unset):
            mode = UNSET
        else:
            mode = ListingPricingStrategyMode(_mode)




        def _parse_min_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_price = _parse_min_price(d.pop("minPrice", UNSET))


        def _parse_max_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_price = _parse_max_price(d.pop("maxPrice", UNSET))


        max_daily_change_pct = d.pop("maxDailyChangePct", UNSET)

        def _parse_weekend_markup_pct(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        weekend_markup_pct = _parse_weekend_markup_pct(d.pop("weekendMarkupPct", UNSET))


        _day_of_week_multipliers = d.pop("dayOfWeekMultipliers", UNSET)
        day_of_week_multipliers: ListingPricingStrategyDayOfWeekMultipliers | Unset
        if isinstance(_day_of_week_multipliers,  Unset):
            day_of_week_multipliers = UNSET
        else:
            day_of_week_multipliers = ListingPricingStrategyDayOfWeekMultipliers.from_dict(_day_of_week_multipliers)




        def _parse_target_occupancy_pct(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        target_occupancy_pct = _parse_target_occupancy_pct(d.pop("targetOccupancyPct", UNSET))


        def _parse_target_monthly_revenue(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        target_monthly_revenue = _parse_target_monthly_revenue(d.pop("targetMonthlyRevenue", UNSET))


        def _parse_owner_min_monthly_payout(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        owner_min_monthly_payout = _parse_owner_min_monthly_payout(d.pop("ownerMinMonthlyPayout", UNSET))


        _comp_position_target = d.pop("compPositionTarget", UNSET)
        comp_position_target: ListingPricingStrategyCompPositionTarget | Unset
        if isinstance(_comp_position_target,  Unset):
            comp_position_target = UNSET
        else:
            comp_position_target = ListingPricingStrategyCompPositionTarget(_comp_position_target)




        comp_adjust_pct = d.pop("compAdjustPct", UNSET)

        event_boost_enabled = d.pop("eventBoostEnabled", UNSET)

        event_boost_max_pct = d.pop("eventBoostMaxPct", UNSET)

        is_default = d.pop("isDefault", UNSET)

        listing_pricing_strategy = cls(
            id=id,
            listing_id=listing_id,
            customer_id=customer_id,
            mode=mode,
            min_price=min_price,
            max_price=max_price,
            max_daily_change_pct=max_daily_change_pct,
            weekend_markup_pct=weekend_markup_pct,
            day_of_week_multipliers=day_of_week_multipliers,
            target_occupancy_pct=target_occupancy_pct,
            target_monthly_revenue=target_monthly_revenue,
            owner_min_monthly_payout=owner_min_monthly_payout,
            comp_position_target=comp_position_target,
            comp_adjust_pct=comp_adjust_pct,
            event_boost_enabled=event_boost_enabled,
            event_boost_max_pct=event_boost_max_pct,
            is_default=is_default,
        )


        listing_pricing_strategy.additional_properties = d
        return listing_pricing_strategy

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
