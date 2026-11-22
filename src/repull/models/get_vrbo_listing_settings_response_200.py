from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_settings_response_200_data_freshness import GetVrboListingSettingsResponse200DataFreshness
  from ..models.get_vrbo_listing_settings_response_200_data_type_0 import GetVrboListingSettingsResponse200DataType0
  from ..models.get_vrbo_listing_settings_response_200_data_type_2 import GetVrboListingSettingsResponse200DataType2





T = TypeVar("T", bound="GetVrboListingSettingsResponse200")



@_attrs_define
class GetVrboListingSettingsResponse200:
    """ 
        Attributes:
            data (GetVrboListingSettingsResponse200DataType0 | GetVrboListingSettingsResponse200DataType2 | list[str]): The
                section as Vrbo has it.
            data_freshness (GetVrboListingSettingsResponse200DataFreshness):
            vrbo_listing_number (str): The Vrbo listing number this is about.
     """

    data: GetVrboListingSettingsResponse200DataType0 | GetVrboListingSettingsResponse200DataType2 | list[str]
    data_freshness: GetVrboListingSettingsResponse200DataFreshness
    vrbo_listing_number: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_settings_response_200_data_freshness import GetVrboListingSettingsResponse200DataFreshness
        from ..models.get_vrbo_listing_settings_response_200_data_type_0 import GetVrboListingSettingsResponse200DataType0
        from ..models.get_vrbo_listing_settings_response_200_data_type_2 import GetVrboListingSettingsResponse200DataType2
        data: dict[str, Any] | list[str]
        if isinstance(self.data, GetVrboListingSettingsResponse200DataType0):
            data = self.data.to_dict()
        elif isinstance(self.data, list):
            data = self.data


        else:
            data = self.data.to_dict()


        data_freshness = self.data_freshness.to_dict()

        vrbo_listing_number = self.vrbo_listing_number


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
            "dataFreshness": data_freshness,
            "vrboListingNumber": vrbo_listing_number,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_settings_response_200_data_freshness import GetVrboListingSettingsResponse200DataFreshness
        from ..models.get_vrbo_listing_settings_response_200_data_type_0 import GetVrboListingSettingsResponse200DataType0
        from ..models.get_vrbo_listing_settings_response_200_data_type_2 import GetVrboListingSettingsResponse200DataType2
        d = dict(src_dict)
        def _parse_data(data: object) -> GetVrboListingSettingsResponse200DataType0 | GetVrboListingSettingsResponse200DataType2 | list[str]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = GetVrboListingSettingsResponse200DataType0.from_dict(data)



                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                data_type_1 = cast(list[str], data)

                return data_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            data_type_2 = GetVrboListingSettingsResponse200DataType2.from_dict(data)



            return data_type_2

        data = _parse_data(d.pop("data"))


        data_freshness = GetVrboListingSettingsResponse200DataFreshness.from_dict(d.pop("dataFreshness"))




        vrbo_listing_number = d.pop("vrboListingNumber")

        get_vrbo_listing_settings_response_200 = cls(
            data=data,
            data_freshness=data_freshness,
            vrbo_listing_number=vrbo_listing_number,
        )


        get_vrbo_listing_settings_response_200.additional_properties = d
        return get_vrbo_listing_settings_response_200

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
