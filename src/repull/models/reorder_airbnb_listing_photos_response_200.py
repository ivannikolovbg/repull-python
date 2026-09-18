from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.reorder_airbnb_listing_photos_response_200_data import ReorderAirbnbListingPhotosResponse200Data





T = TypeVar("T", bound="ReorderAirbnbListingPhotosResponse200")



@_attrs_define
class ReorderAirbnbListingPhotosResponse200:
    """ 
        Attributes:
            data (ReorderAirbnbListingPhotosResponse200Data):
            stored (bool): Whether our own copy was brought in line with what landed.
     """

    data: ReorderAirbnbListingPhotosResponse200Data
    stored: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reorder_airbnb_listing_photos_response_200_data import ReorderAirbnbListingPhotosResponse200Data
        data = self.data.to_dict()

        stored = self.stored


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
            "stored": stored,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reorder_airbnb_listing_photos_response_200_data import ReorderAirbnbListingPhotosResponse200Data
        d = dict(src_dict)
        data = ReorderAirbnbListingPhotosResponse200Data.from_dict(d.pop("data"))




        stored = d.pop("stored")

        reorder_airbnb_listing_photos_response_200 = cls(
            data=data,
            stored=stored,
        )


        reorder_airbnb_listing_photos_response_200.additional_properties = d
        return reorder_airbnb_listing_photos_response_200

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
