from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_fees_response_200_data import UpdateVrboListingFeesResponse200Data
  from ..models.update_vrbo_listing_fees_response_200_data_freshness import UpdateVrboListingFeesResponse200DataFreshness





T = TypeVar("T", bound="UpdateVrboListingFeesResponse200")



@_attrs_define
class UpdateVrboListingFeesResponse200:
    """ 
        Attributes:
            data (UpdateVrboListingFeesResponse200Data): What Vrbo has after the write, read back from Vrbo.
            written (list[str]): The fields this request sent.
            data_freshness (UpdateVrboListingFeesResponse200DataFreshness):
            vrbo_listing_number (str):
     """

    data: UpdateVrboListingFeesResponse200Data
    written: list[str]
    data_freshness: UpdateVrboListingFeesResponse200DataFreshness
    vrbo_listing_number: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_fees_response_200_data import UpdateVrboListingFeesResponse200Data
        from ..models.update_vrbo_listing_fees_response_200_data_freshness import UpdateVrboListingFeesResponse200DataFreshness
        data = self.data.to_dict()

        written = self.written



        data_freshness = self.data_freshness.to_dict()

        vrbo_listing_number = self.vrbo_listing_number


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
            "written": written,
            "dataFreshness": data_freshness,
            "vrboListingNumber": vrbo_listing_number,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_fees_response_200_data import UpdateVrboListingFeesResponse200Data
        from ..models.update_vrbo_listing_fees_response_200_data_freshness import UpdateVrboListingFeesResponse200DataFreshness
        d = dict(src_dict)
        data = UpdateVrboListingFeesResponse200Data.from_dict(d.pop("data"))




        written = cast(list[str], d.pop("written"))


        data_freshness = UpdateVrboListingFeesResponse200DataFreshness.from_dict(d.pop("dataFreshness"))




        vrbo_listing_number = d.pop("vrboListingNumber")

        update_vrbo_listing_fees_response_200 = cls(
            data=data,
            written=written,
            data_freshness=data_freshness,
            vrbo_listing_number=vrbo_listing_number,
        )


        update_vrbo_listing_fees_response_200.additional_properties = d
        return update_vrbo_listing_fees_response_200

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
