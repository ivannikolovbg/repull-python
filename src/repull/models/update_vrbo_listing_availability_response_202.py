from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_availability_response_202_data import UpdateVrboListingAvailabilityResponse202Data





T = TypeVar("T", bound="UpdateVrboListingAvailabilityResponse202")



@_attrs_define
class UpdateVrboListingAvailabilityResponse202:
    """ 
        Attributes:
            data (UpdateVrboListingAvailabilityResponse202Data | Unset):
            vrbo_listing_number (str | Unset):
     """

    data: UpdateVrboListingAvailabilityResponse202Data | Unset = UNSET
    vrbo_listing_number: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_availability_response_202_data import UpdateVrboListingAvailabilityResponse202Data
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        vrbo_listing_number = self.vrbo_listing_number


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if vrbo_listing_number is not UNSET:
            field_dict["vrboListingNumber"] = vrbo_listing_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_availability_response_202_data import UpdateVrboListingAvailabilityResponse202Data
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: UpdateVrboListingAvailabilityResponse202Data | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = UpdateVrboListingAvailabilityResponse202Data.from_dict(_data)




        vrbo_listing_number = d.pop("vrboListingNumber", UNSET)

        update_vrbo_listing_availability_response_202 = cls(
            data=data,
            vrbo_listing_number=vrbo_listing_number,
        )


        update_vrbo_listing_availability_response_202.additional_properties = d
        return update_vrbo_listing_availability_response_202

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
