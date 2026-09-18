from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_safety_disclosure import AirbnbSafetyDisclosure
  from ..models.update_airbnb_listing_safety_disclosures_response_200_result import UpdateAirbnbListingSafetyDisclosuresResponse200Result





T = TypeVar("T", bound="UpdateAirbnbListingSafetyDisclosuresResponse200")



@_attrs_define
class UpdateAirbnbListingSafetyDisclosuresResponse200:
    """ 
        Attributes:
            listing_id (str | Unset):
            airbnb_listing_id (str | Unset):
            disclosures (list[AirbnbSafetyDisclosure] | Unset): The set as Airbnb reports it after the write.
            result (UpdateAirbnbListingSafetyDisclosuresResponse200Result | Unset): Airbnb's raw booking-settings response.
     """

    listing_id: str | Unset = UNSET
    airbnb_listing_id: str | Unset = UNSET
    disclosures: list[AirbnbSafetyDisclosure] | Unset = UNSET
    result: UpdateAirbnbListingSafetyDisclosuresResponse200Result | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_safety_disclosure import AirbnbSafetyDisclosure
        from ..models.update_airbnb_listing_safety_disclosures_response_200_result import UpdateAirbnbListingSafetyDisclosuresResponse200Result
        listing_id = self.listing_id

        airbnb_listing_id = self.airbnb_listing_id

        disclosures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.disclosures, Unset):
            disclosures = []
            for disclosures_item_data in self.disclosures:
                disclosures_item = disclosures_item_data.to_dict()
                disclosures.append(disclosures_item)



        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if airbnb_listing_id is not UNSET:
            field_dict["airbnbListingId"] = airbnb_listing_id
        if disclosures is not UNSET:
            field_dict["disclosures"] = disclosures
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_safety_disclosure import AirbnbSafetyDisclosure
        from ..models.update_airbnb_listing_safety_disclosures_response_200_result import UpdateAirbnbListingSafetyDisclosuresResponse200Result
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        airbnb_listing_id = d.pop("airbnbListingId", UNSET)

        _disclosures = d.pop("disclosures", UNSET)
        disclosures: list[AirbnbSafetyDisclosure] | Unset = UNSET
        if _disclosures is not UNSET:
            disclosures = []
            for disclosures_item_data in _disclosures:
                disclosures_item = AirbnbSafetyDisclosure.from_dict(disclosures_item_data)



                disclosures.append(disclosures_item)


        _result = d.pop("result", UNSET)
        result: UpdateAirbnbListingSafetyDisclosuresResponse200Result | Unset
        if isinstance(_result,  Unset):
            result = UNSET
        else:
            result = UpdateAirbnbListingSafetyDisclosuresResponse200Result.from_dict(_result)




        update_airbnb_listing_safety_disclosures_response_200 = cls(
            listing_id=listing_id,
            airbnb_listing_id=airbnb_listing_id,
            disclosures=disclosures,
            result=result,
        )


        update_airbnb_listing_safety_disclosures_response_200.additional_properties = d
        return update_airbnb_listing_safety_disclosures_response_200

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
