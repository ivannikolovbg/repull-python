from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.market_my_listing import MarketMyListing
  from ..models.market_summary import MarketSummary
  from ..models.markets_overview_response_browse import MarketsOverviewResponseBrowse
  from ..models.markets_overview_response_subscriptions import MarketsOverviewResponseSubscriptions
  from ..models.markets_overview_response_totals import MarketsOverviewResponseTotals
  from ..models.pagination import Pagination





T = TypeVar("T", bound="MarketsOverviewResponse")



@_attrs_define
class MarketsOverviewResponse:
    """ Overview of every market the customer operates in, plus auxiliary discovery slices. Wraps the canonical `{ data,
    pagination }` envelope around the per-city KPI list (`data`) so SDK consumers see the same shape they get from every
    other list endpoint. Auxiliary fields (`totals`, `myListings`, `browse`, `freeMarket`, `subscriptions`, `tier`) are
    returned as siblings because they are NOT paginated. The overview returns every market in one shot — `nextCursor` is
    always `null` and `hasMore` is always `false`.

        Attributes:
            data (list[MarketSummary] | Unset): Per-city KPIs for every market the customer operates in.
            pagination (Pagination | Unset): Canonical cursor-based pagination envelope. Pass `nextCursor` back as
                `?cursor=` to fetch the next page; stop when `hasMore` is `false`. The cursor is opaque base64 — do not parse or
                construct it by hand.
            totals (MarketsOverviewResponseTotals | Unset):
            my_listings (list[MarketMyListing] | Unset):
            free_market (None | str | Unset): City auto-assigned as the customer's free market (largest by listing count).
                Null for customers with no listings.
            subscriptions (MarketsOverviewResponseSubscriptions | Unset): Active per-market unlocks vs the tier quota.
            tier (str | Unset): Resolved Repull tier (free / pro / scale).
            browse (MarketsOverviewResponseBrowse | Unset): Lightweight discovery summary. Use `/v1/markets/browse` for the
                full paginated catalog.
     """

    data: list[MarketSummary] | Unset = UNSET
    pagination: Pagination | Unset = UNSET
    totals: MarketsOverviewResponseTotals | Unset = UNSET
    my_listings: list[MarketMyListing] | Unset = UNSET
    free_market: None | str | Unset = UNSET
    subscriptions: MarketsOverviewResponseSubscriptions | Unset = UNSET
    tier: str | Unset = UNSET
    browse: MarketsOverviewResponseBrowse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.market_my_listing import MarketMyListing
        from ..models.market_summary import MarketSummary
        from ..models.markets_overview_response_browse import MarketsOverviewResponseBrowse
        from ..models.markets_overview_response_subscriptions import MarketsOverviewResponseSubscriptions
        from ..models.markets_overview_response_totals import MarketsOverviewResponseTotals
        from ..models.pagination import Pagination
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)



        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        my_listings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.my_listings, Unset):
            my_listings = []
            for my_listings_item_data in self.my_listings:
                my_listings_item = my_listings_item_data.to_dict()
                my_listings.append(my_listings_item)



        free_market: None | str | Unset
        if isinstance(self.free_market, Unset):
            free_market = UNSET
        else:
            free_market = self.free_market

        subscriptions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.subscriptions, Unset):
            subscriptions = self.subscriptions.to_dict()

        tier = self.tier

        browse: dict[str, Any] | Unset = UNSET
        if not isinstance(self.browse, Unset):
            browse = self.browse.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if totals is not UNSET:
            field_dict["totals"] = totals
        if my_listings is not UNSET:
            field_dict["myListings"] = my_listings
        if free_market is not UNSET:
            field_dict["freeMarket"] = free_market
        if subscriptions is not UNSET:
            field_dict["subscriptions"] = subscriptions
        if tier is not UNSET:
            field_dict["tier"] = tier
        if browse is not UNSET:
            field_dict["browse"] = browse

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.market_my_listing import MarketMyListing
        from ..models.market_summary import MarketSummary
        from ..models.markets_overview_response_browse import MarketsOverviewResponseBrowse
        from ..models.markets_overview_response_subscriptions import MarketsOverviewResponseSubscriptions
        from ..models.markets_overview_response_totals import MarketsOverviewResponseTotals
        from ..models.pagination import Pagination
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[MarketSummary] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = MarketSummary.from_dict(data_item_data)



                data.append(data_item)


        _pagination = d.pop("pagination", UNSET)
        pagination: Pagination | Unset
        if isinstance(_pagination,  Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)




        _totals = d.pop("totals", UNSET)
        totals: MarketsOverviewResponseTotals | Unset
        if isinstance(_totals,  Unset):
            totals = UNSET
        else:
            totals = MarketsOverviewResponseTotals.from_dict(_totals)




        _my_listings = d.pop("myListings", UNSET)
        my_listings: list[MarketMyListing] | Unset = UNSET
        if _my_listings is not UNSET:
            my_listings = []
            for my_listings_item_data in _my_listings:
                my_listings_item = MarketMyListing.from_dict(my_listings_item_data)



                my_listings.append(my_listings_item)


        def _parse_free_market(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        free_market = _parse_free_market(d.pop("freeMarket", UNSET))


        _subscriptions = d.pop("subscriptions", UNSET)
        subscriptions: MarketsOverviewResponseSubscriptions | Unset
        if isinstance(_subscriptions,  Unset):
            subscriptions = UNSET
        else:
            subscriptions = MarketsOverviewResponseSubscriptions.from_dict(_subscriptions)




        tier = d.pop("tier", UNSET)

        _browse = d.pop("browse", UNSET)
        browse: MarketsOverviewResponseBrowse | Unset
        if isinstance(_browse,  Unset):
            browse = UNSET
        else:
            browse = MarketsOverviewResponseBrowse.from_dict(_browse)




        markets_overview_response = cls(
            data=data,
            pagination=pagination,
            totals=totals,
            my_listings=my_listings,
            free_market=free_market,
            subscriptions=subscriptions,
            tier=tier,
            browse=browse,
        )


        markets_overview_response.additional_properties = d
        return markets_overview_response

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
