from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_data_freshness import AirbnbDataFreshness





T = TypeVar("T", bound="GetAirbnbListingSettingsResponse200")



@_attrs_define
class GetAirbnbListingSettingsResponse200:
    """ 
        Attributes:
            data (Any): Shape depends on `type`: `{ hosts, locales }` for `all`, or an array for
                `hosts`/`permits`/`locales`.
            data_freshness (AirbnbDataFreshness): Top-level freshness indicator for any DB-backed Airbnb read. Tells
                consumers WHY a column may be `null` or stale without sprinkling per-row error envelopes through the response.
                The endpoint always returns 200 + DB data; this field is the single signal for "should I prompt the user to
                reconnect / wait for sync?".
     """

    data: Any
    data_freshness: AirbnbDataFreshness
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_data_freshness import AirbnbDataFreshness
        data = self.data

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
        d = dict(src_dict)
        data = d.pop("data")

        data_freshness = AirbnbDataFreshness.from_dict(d.pop("data_freshness"))




        get_airbnb_listing_settings_response_200 = cls(
            data=data,
            data_freshness=data_freshness,
        )


        get_airbnb_listing_settings_response_200.additional_properties = d
        return get_airbnb_listing_settings_response_200

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
