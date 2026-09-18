from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_airbnb_listing_permits_response_200_permits_item import UpdateAirbnbListingPermitsResponse200PermitsItem





T = TypeVar("T", bound="UpdateAirbnbListingPermitsResponse200")



@_attrs_define
class UpdateAirbnbListingPermitsResponse200:
    """ 
        Attributes:
            listing_id (str | Unset):
            airbnb_listing_id (str | Unset):
            permits (list[UpdateAirbnbListingPermitsResponse200PermitsItem] | Unset): The permit flows as Airbnb reports
                them after the write, including each flow's new `status`.
     """

    listing_id: str | Unset = UNSET
    airbnb_listing_id: str | Unset = UNSET
    permits: list[UpdateAirbnbListingPermitsResponse200PermitsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_airbnb_listing_permits_response_200_permits_item import UpdateAirbnbListingPermitsResponse200PermitsItem
        listing_id = self.listing_id

        airbnb_listing_id = self.airbnb_listing_id

        permits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.permits, Unset):
            permits = []
            for permits_item_data in self.permits:
                permits_item = permits_item_data.to_dict()
                permits.append(permits_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if airbnb_listing_id is not UNSET:
            field_dict["airbnbListingId"] = airbnb_listing_id
        if permits is not UNSET:
            field_dict["permits"] = permits

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_airbnb_listing_permits_response_200_permits_item import UpdateAirbnbListingPermitsResponse200PermitsItem
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        airbnb_listing_id = d.pop("airbnbListingId", UNSET)

        _permits = d.pop("permits", UNSET)
        permits: list[UpdateAirbnbListingPermitsResponse200PermitsItem] | Unset = UNSET
        if _permits is not UNSET:
            permits = []
            for permits_item_data in _permits:
                permits_item = UpdateAirbnbListingPermitsResponse200PermitsItem.from_dict(permits_item_data)



                permits.append(permits_item)


        update_airbnb_listing_permits_response_200 = cls(
            listing_id=listing_id,
            airbnb_listing_id=airbnb_listing_id,
            permits=permits,
        )


        update_airbnb_listing_permits_response_200.additional_properties = d
        return update_airbnb_listing_permits_response_200

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
