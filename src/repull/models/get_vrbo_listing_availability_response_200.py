from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_availability_response_200_data_freshness import GetVrboListingAvailabilityResponse200DataFreshness
  from ..models.get_vrbo_listing_availability_response_200_data_type_0_item import GetVrboListingAvailabilityResponse200DataType0Item
  from ..models.get_vrbo_listing_availability_response_200_data_type_1 import GetVrboListingAvailabilityResponse200DataType1
  from ..models.get_vrbo_listing_availability_response_200_range import GetVrboListingAvailabilityResponse200Range





T = TypeVar("T", bound="GetVrboListingAvailabilityResponse200")



@_attrs_define
class GetVrboListingAvailabilityResponse200:
    """ 
        Attributes:
            data (GetVrboListingAvailabilityResponse200DataType1 | list[GetVrboListingAvailabilityResponse200DataType0Item]
                | Unset):
            range_ (GetVrboListingAvailabilityResponse200Range | Unset):
            warning (str | Unset): Set when Vrbo did not return the bookings and blocks for the range.
            data_freshness (GetVrboListingAvailabilityResponse200DataFreshness | Unset):
            vrbo_listing_number (str | Unset):
     """

    data: GetVrboListingAvailabilityResponse200DataType1 | list[GetVrboListingAvailabilityResponse200DataType0Item] | Unset = UNSET
    range_: GetVrboListingAvailabilityResponse200Range | Unset = UNSET
    warning: str | Unset = UNSET
    data_freshness: GetVrboListingAvailabilityResponse200DataFreshness | Unset = UNSET
    vrbo_listing_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_availability_response_200_data_freshness import GetVrboListingAvailabilityResponse200DataFreshness
        from ..models.get_vrbo_listing_availability_response_200_data_type_0_item import GetVrboListingAvailabilityResponse200DataType0Item
        from ..models.get_vrbo_listing_availability_response_200_data_type_1 import GetVrboListingAvailabilityResponse200DataType1
        from ..models.get_vrbo_listing_availability_response_200_range import GetVrboListingAvailabilityResponse200Range
        data: dict[str, Any] | list[dict[str, Any]] | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, list):
            data = []
            for data_type_0_item_data in self.data:
                data_type_0_item = data_type_0_item_data.to_dict()
                data.append(data_type_0_item)


        else:
            data = self.data.to_dict()


        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        warning = self.warning

        data_freshness: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_freshness, Unset):
            data_freshness = self.data_freshness.to_dict()

        vrbo_listing_number = self.vrbo_listing_number


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if range_ is not UNSET:
            field_dict["range"] = range_
        if warning is not UNSET:
            field_dict["warning"] = warning
        if data_freshness is not UNSET:
            field_dict["dataFreshness"] = data_freshness
        if vrbo_listing_number is not UNSET:
            field_dict["vrboListingNumber"] = vrbo_listing_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_availability_response_200_data_freshness import GetVrboListingAvailabilityResponse200DataFreshness
        from ..models.get_vrbo_listing_availability_response_200_data_type_0_item import GetVrboListingAvailabilityResponse200DataType0Item
        from ..models.get_vrbo_listing_availability_response_200_data_type_1 import GetVrboListingAvailabilityResponse200DataType1
        from ..models.get_vrbo_listing_availability_response_200_range import GetVrboListingAvailabilityResponse200Range
        d = dict(src_dict)
        def _parse_data(data: object) -> GetVrboListingAvailabilityResponse200DataType1 | list[GetVrboListingAvailabilityResponse200DataType0Item] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_0 = []
                _data_type_0 = data
                for data_type_0_item_data in (_data_type_0):
                    data_type_0_item = GetVrboListingAvailabilityResponse200DataType0Item.from_dict(data_type_0_item_data)



                    data_type_0.append(data_type_0_item)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_1 = GetVrboListingAvailabilityResponse200DataType1.from_dict(data)



            return data_type_1

        data = _parse_data(d.pop("data", UNSET))


        _range_ = d.pop("range", UNSET)
        range_: GetVrboListingAvailabilityResponse200Range | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = GetVrboListingAvailabilityResponse200Range.from_dict(_range_)




        warning = d.pop("warning", UNSET)

        _data_freshness = d.pop("dataFreshness", UNSET)
        data_freshness: GetVrboListingAvailabilityResponse200DataFreshness | Unset
        if isinstance(_data_freshness,  Unset):
            data_freshness = UNSET
        else:
            data_freshness = GetVrboListingAvailabilityResponse200DataFreshness.from_dict(_data_freshness)




        vrbo_listing_number = d.pop("vrboListingNumber", UNSET)

        get_vrbo_listing_availability_response_200 = cls(
            data=data,
            range_=range_,
            warning=warning,
            data_freshness=data_freshness,
            vrbo_listing_number=vrbo_listing_number,
        )


        get_vrbo_listing_availability_response_200.additional_properties = d
        return get_vrbo_listing_availability_response_200

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
