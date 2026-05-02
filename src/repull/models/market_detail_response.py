from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.market_detail_response_bedroom_breakdown_item import MarketDetailResponseBedroomBreakdownItem
  from ..models.market_detail_response_benchmarks_item import MarketDetailResponseBenchmarksItem
  from ..models.market_detail_response_capacity_gap import MarketDetailResponseCapacityGap
  from ..models.market_detail_response_health_summary_type_0 import MarketDetailResponseHealthSummaryType0
  from ..models.market_detail_response_market_position_type_0 import MarketDetailResponseMarketPositionType0
  from ..models.market_detail_response_price_distribution_item import MarketDetailResponsePriceDistributionItem
  from ..models.market_detail_response_property_type_mix_item import MarketDetailResponsePropertyTypeMixItem
  from ..models.market_detail_response_supply_trend_item import MarketDetailResponseSupplyTrendItem
  from ..models.market_detail_response_top_comps import MarketDetailResponseTopComps
  from ..models.market_detail_response_wheelhouse_trends_item import MarketDetailResponseWheelhouseTrendsItem
  from ..models.market_event import MarketEvent





T = TypeVar("T", bound="MarketDetailResponse")



@_attrs_define
class MarketDetailResponse:
    """ Detailed view for a single city. Several sub-objects are passed through verbatim from upstream — keys mirror the
    underlying SQL aggregations.

        Attributes:
            city (str | Unset):
            price_distribution (list[MarketDetailResponsePriceDistributionItem] | Unset):
            bedroom_breakdown (list[MarketDetailResponseBedroomBreakdownItem] | Unset):
            property_type_mix (list[MarketDetailResponsePropertyTypeMixItem] | Unset):
            events (list[MarketEvent] | Unset):
            wheelhouse_trends (list[MarketDetailResponseWheelhouseTrendsItem] | Unset):
            benchmarks (list[MarketDetailResponseBenchmarksItem] | Unset):
            health_summary (MarketDetailResponseHealthSummaryType0 | None | Unset):
            top_comps (MarketDetailResponseTopComps | Unset):
            market_position (MarketDetailResponseMarketPositionType0 | None | Unset):
            capacity_gap (MarketDetailResponseCapacityGap | Unset):
            supply_trend (list[MarketDetailResponseSupplyTrendItem] | Unset):
     """

    city: str | Unset = UNSET
    price_distribution: list[MarketDetailResponsePriceDistributionItem] | Unset = UNSET
    bedroom_breakdown: list[MarketDetailResponseBedroomBreakdownItem] | Unset = UNSET
    property_type_mix: list[MarketDetailResponsePropertyTypeMixItem] | Unset = UNSET
    events: list[MarketEvent] | Unset = UNSET
    wheelhouse_trends: list[MarketDetailResponseWheelhouseTrendsItem] | Unset = UNSET
    benchmarks: list[MarketDetailResponseBenchmarksItem] | Unset = UNSET
    health_summary: MarketDetailResponseHealthSummaryType0 | None | Unset = UNSET
    top_comps: MarketDetailResponseTopComps | Unset = UNSET
    market_position: MarketDetailResponseMarketPositionType0 | None | Unset = UNSET
    capacity_gap: MarketDetailResponseCapacityGap | Unset = UNSET
    supply_trend: list[MarketDetailResponseSupplyTrendItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.market_detail_response_bedroom_breakdown_item import MarketDetailResponseBedroomBreakdownItem
        from ..models.market_detail_response_benchmarks_item import MarketDetailResponseBenchmarksItem
        from ..models.market_detail_response_capacity_gap import MarketDetailResponseCapacityGap
        from ..models.market_detail_response_health_summary_type_0 import MarketDetailResponseHealthSummaryType0
        from ..models.market_detail_response_market_position_type_0 import MarketDetailResponseMarketPositionType0
        from ..models.market_detail_response_price_distribution_item import MarketDetailResponsePriceDistributionItem
        from ..models.market_detail_response_property_type_mix_item import MarketDetailResponsePropertyTypeMixItem
        from ..models.market_detail_response_supply_trend_item import MarketDetailResponseSupplyTrendItem
        from ..models.market_detail_response_top_comps import MarketDetailResponseTopComps
        from ..models.market_detail_response_wheelhouse_trends_item import MarketDetailResponseWheelhouseTrendsItem
        from ..models.market_event import MarketEvent
        city = self.city

        price_distribution: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.price_distribution, Unset):
            price_distribution = []
            for price_distribution_item_data in self.price_distribution:
                price_distribution_item = price_distribution_item_data.to_dict()
                price_distribution.append(price_distribution_item)



        bedroom_breakdown: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.bedroom_breakdown, Unset):
            bedroom_breakdown = []
            for bedroom_breakdown_item_data in self.bedroom_breakdown:
                bedroom_breakdown_item = bedroom_breakdown_item_data.to_dict()
                bedroom_breakdown.append(bedroom_breakdown_item)



        property_type_mix: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.property_type_mix, Unset):
            property_type_mix = []
            for property_type_mix_item_data in self.property_type_mix:
                property_type_mix_item = property_type_mix_item_data.to_dict()
                property_type_mix.append(property_type_mix_item)



        events: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)



        wheelhouse_trends: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.wheelhouse_trends, Unset):
            wheelhouse_trends = []
            for wheelhouse_trends_item_data in self.wheelhouse_trends:
                wheelhouse_trends_item = wheelhouse_trends_item_data.to_dict()
                wheelhouse_trends.append(wheelhouse_trends_item)



        benchmarks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.benchmarks, Unset):
            benchmarks = []
            for benchmarks_item_data in self.benchmarks:
                benchmarks_item = benchmarks_item_data.to_dict()
                benchmarks.append(benchmarks_item)



        health_summary: dict[str, Any] | None | Unset
        if isinstance(self.health_summary, Unset):
            health_summary = UNSET
        elif isinstance(self.health_summary, MarketDetailResponseHealthSummaryType0):
            health_summary = self.health_summary.to_dict()
        else:
            health_summary = self.health_summary

        top_comps: dict[str, Any] | Unset = UNSET
        if not isinstance(self.top_comps, Unset):
            top_comps = self.top_comps.to_dict()

        market_position: dict[str, Any] | None | Unset
        if isinstance(self.market_position, Unset):
            market_position = UNSET
        elif isinstance(self.market_position, MarketDetailResponseMarketPositionType0):
            market_position = self.market_position.to_dict()
        else:
            market_position = self.market_position

        capacity_gap: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capacity_gap, Unset):
            capacity_gap = self.capacity_gap.to_dict()

        supply_trend: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.supply_trend, Unset):
            supply_trend = []
            for supply_trend_item_data in self.supply_trend:
                supply_trend_item = supply_trend_item_data.to_dict()
                supply_trend.append(supply_trend_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if city is not UNSET:
            field_dict["city"] = city
        if price_distribution is not UNSET:
            field_dict["priceDistribution"] = price_distribution
        if bedroom_breakdown is not UNSET:
            field_dict["bedroomBreakdown"] = bedroom_breakdown
        if property_type_mix is not UNSET:
            field_dict["propertyTypeMix"] = property_type_mix
        if events is not UNSET:
            field_dict["events"] = events
        if wheelhouse_trends is not UNSET:
            field_dict["wheelhouseTrends"] = wheelhouse_trends
        if benchmarks is not UNSET:
            field_dict["benchmarks"] = benchmarks
        if health_summary is not UNSET:
            field_dict["healthSummary"] = health_summary
        if top_comps is not UNSET:
            field_dict["topComps"] = top_comps
        if market_position is not UNSET:
            field_dict["marketPosition"] = market_position
        if capacity_gap is not UNSET:
            field_dict["capacityGap"] = capacity_gap
        if supply_trend is not UNSET:
            field_dict["supplyTrend"] = supply_trend

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_detail_response_bedroom_breakdown_item import MarketDetailResponseBedroomBreakdownItem
        from ..models.market_detail_response_benchmarks_item import MarketDetailResponseBenchmarksItem
        from ..models.market_detail_response_capacity_gap import MarketDetailResponseCapacityGap
        from ..models.market_detail_response_health_summary_type_0 import MarketDetailResponseHealthSummaryType0
        from ..models.market_detail_response_market_position_type_0 import MarketDetailResponseMarketPositionType0
        from ..models.market_detail_response_price_distribution_item import MarketDetailResponsePriceDistributionItem
        from ..models.market_detail_response_property_type_mix_item import MarketDetailResponsePropertyTypeMixItem
        from ..models.market_detail_response_supply_trend_item import MarketDetailResponseSupplyTrendItem
        from ..models.market_detail_response_top_comps import MarketDetailResponseTopComps
        from ..models.market_detail_response_wheelhouse_trends_item import MarketDetailResponseWheelhouseTrendsItem
        from ..models.market_event import MarketEvent
        d = dict(src_dict)
        city = d.pop("city", UNSET)

        _price_distribution = d.pop("priceDistribution", UNSET)
        price_distribution: list[MarketDetailResponsePriceDistributionItem] | Unset = UNSET
        if _price_distribution is not UNSET:
            price_distribution = []
            for price_distribution_item_data in _price_distribution:
                price_distribution_item = MarketDetailResponsePriceDistributionItem.from_dict(price_distribution_item_data)



                price_distribution.append(price_distribution_item)


        _bedroom_breakdown = d.pop("bedroomBreakdown", UNSET)
        bedroom_breakdown: list[MarketDetailResponseBedroomBreakdownItem] | Unset = UNSET
        if _bedroom_breakdown is not UNSET:
            bedroom_breakdown = []
            for bedroom_breakdown_item_data in _bedroom_breakdown:
                bedroom_breakdown_item = MarketDetailResponseBedroomBreakdownItem.from_dict(bedroom_breakdown_item_data)



                bedroom_breakdown.append(bedroom_breakdown_item)


        _property_type_mix = d.pop("propertyTypeMix", UNSET)
        property_type_mix: list[MarketDetailResponsePropertyTypeMixItem] | Unset = UNSET
        if _property_type_mix is not UNSET:
            property_type_mix = []
            for property_type_mix_item_data in _property_type_mix:
                property_type_mix_item = MarketDetailResponsePropertyTypeMixItem.from_dict(property_type_mix_item_data)



                property_type_mix.append(property_type_mix_item)


        _events = d.pop("events", UNSET)
        events: list[MarketEvent] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = MarketEvent.from_dict(events_item_data)



                events.append(events_item)


        _wheelhouse_trends = d.pop("wheelhouseTrends", UNSET)
        wheelhouse_trends: list[MarketDetailResponseWheelhouseTrendsItem] | Unset = UNSET
        if _wheelhouse_trends is not UNSET:
            wheelhouse_trends = []
            for wheelhouse_trends_item_data in _wheelhouse_trends:
                wheelhouse_trends_item = MarketDetailResponseWheelhouseTrendsItem.from_dict(wheelhouse_trends_item_data)



                wheelhouse_trends.append(wheelhouse_trends_item)


        _benchmarks = d.pop("benchmarks", UNSET)
        benchmarks: list[MarketDetailResponseBenchmarksItem] | Unset = UNSET
        if _benchmarks is not UNSET:
            benchmarks = []
            for benchmarks_item_data in _benchmarks:
                benchmarks_item = MarketDetailResponseBenchmarksItem.from_dict(benchmarks_item_data)



                benchmarks.append(benchmarks_item)


        def _parse_health_summary(data: object) -> MarketDetailResponseHealthSummaryType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                health_summary_type_0 = MarketDetailResponseHealthSummaryType0.from_dict(data)



                return health_summary_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MarketDetailResponseHealthSummaryType0 | None | Unset, data)

        health_summary = _parse_health_summary(d.pop("healthSummary", UNSET))


        _top_comps = d.pop("topComps", UNSET)
        top_comps: MarketDetailResponseTopComps | Unset
        if isinstance(_top_comps,  Unset):
            top_comps = UNSET
        else:
            top_comps = MarketDetailResponseTopComps.from_dict(_top_comps)




        def _parse_market_position(data: object) -> MarketDetailResponseMarketPositionType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                market_position_type_0 = MarketDetailResponseMarketPositionType0.from_dict(data)



                return market_position_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MarketDetailResponseMarketPositionType0 | None | Unset, data)

        market_position = _parse_market_position(d.pop("marketPosition", UNSET))


        _capacity_gap = d.pop("capacityGap", UNSET)
        capacity_gap: MarketDetailResponseCapacityGap | Unset
        if isinstance(_capacity_gap,  Unset):
            capacity_gap = UNSET
        else:
            capacity_gap = MarketDetailResponseCapacityGap.from_dict(_capacity_gap)




        _supply_trend = d.pop("supplyTrend", UNSET)
        supply_trend: list[MarketDetailResponseSupplyTrendItem] | Unset = UNSET
        if _supply_trend is not UNSET:
            supply_trend = []
            for supply_trend_item_data in _supply_trend:
                supply_trend_item = MarketDetailResponseSupplyTrendItem.from_dict(supply_trend_item_data)



                supply_trend.append(supply_trend_item)


        market_detail_response = cls(
            city=city,
            price_distribution=price_distribution,
            bedroom_breakdown=bedroom_breakdown,
            property_type_mix=property_type_mix,
            events=events,
            wheelhouse_trends=wheelhouse_trends,
            benchmarks=benchmarks,
            health_summary=health_summary,
            top_comps=top_comps,
            market_position=market_position,
            capacity_gap=capacity_gap,
            supply_trend=supply_trend,
        )


        market_detail_response.additional_properties = d
        return market_detail_response

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
