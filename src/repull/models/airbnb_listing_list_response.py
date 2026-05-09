from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_data_freshness import AirbnbDataFreshness
  from ..models.airbnb_listing import AirbnbListing
  from ..models.pagination import Pagination





T = TypeVar("T", bound="AirbnbListingListResponse")



@_attrs_define
class AirbnbListingListResponse:
    """ 
        Attributes:
            data (list[AirbnbListing]):
            pagination (Pagination): Canonical cursor-based pagination envelope. Pass `nextCursor` back as `?cursor=` to
                fetch the next page; stop when `hasMore` is `false`. The cursor is opaque base64 — do not parse or construct it
                by hand.
            data_freshness (AirbnbDataFreshness): Top-level freshness indicator for any DB-backed Airbnb read. Tells
                consumers WHY a column may be `null` or stale without sprinkling per-row error envelopes through the response.
                The endpoint always returns 200 + DB data; this field is the single signal for "should I prompt the user to
                reconnect / wait for sync?".
     """

    data: list[AirbnbListing]
    pagination: Pagination
    data_freshness: AirbnbDataFreshness
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_data_freshness import AirbnbDataFreshness
        from ..models.airbnb_listing import AirbnbListing
        from ..models.pagination import Pagination
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)



        pagination = self.pagination.to_dict()

        data_freshness = self.data_freshness.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
            "pagination": pagination,
            "data_freshness": data_freshness,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_data_freshness import AirbnbDataFreshness
        from ..models.airbnb_listing import AirbnbListing
        from ..models.pagination import Pagination
        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = AirbnbListing.from_dict(data_item_data)



            data.append(data_item)


        pagination = Pagination.from_dict(d.pop("pagination"))




        data_freshness = AirbnbDataFreshness.from_dict(d.pop("data_freshness"))




        airbnb_listing_list_response = cls(
            data=data,
            pagination=pagination,
            data_freshness=data_freshness,
        )


        airbnb_listing_list_response.additional_properties = d
        return airbnb_listing_list_response

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
