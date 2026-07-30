from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_data_freshness import AirbnbDataFreshness
  from ..models.list_airbnb_listing_amenities_response_200_data import ListAirbnbListingAmenitiesResponse200Data





T = TypeVar("T", bound="ListAirbnbListingAmenitiesResponse200")



@_attrs_define
class ListAirbnbListingAmenitiesResponse200:
    """ 
        Attributes:
            data (ListAirbnbListingAmenitiesResponse200Data):
            data_freshness (AirbnbDataFreshness): Top-level freshness indicator for any DB-backed Airbnb read. Tells
                consumers WHY a column may be `null` or stale without sprinkling per-row error envelopes through the response.
                The endpoint always returns 200 + DB data; this field is the single signal for "should I prompt the user to
                reconnect / wait for sync?".
     """

    data: ListAirbnbListingAmenitiesResponse200Data
    data_freshness: AirbnbDataFreshness
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_data_freshness import AirbnbDataFreshness
        from ..models.list_airbnb_listing_amenities_response_200_data import ListAirbnbListingAmenitiesResponse200Data
        data = self.data.to_dict()

        data_freshness = self.data_freshness.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
            "data_freshness": data_freshness,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_data_freshness import AirbnbDataFreshness
        from ..models.list_airbnb_listing_amenities_response_200_data import ListAirbnbListingAmenitiesResponse200Data
        d = dict(src_dict)
        data = ListAirbnbListingAmenitiesResponse200Data.from_dict(d.pop("data"))




        data_freshness = AirbnbDataFreshness.from_dict(d.pop("data_freshness"))




        list_airbnb_listing_amenities_response_200 = cls(
            data=data,
            data_freshness=data_freshness,
        )


        list_airbnb_listing_amenities_response_200.additional_properties = d
        return list_airbnb_listing_amenities_response_200

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
