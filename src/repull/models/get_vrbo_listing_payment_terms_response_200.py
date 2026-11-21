from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_payment_terms_response_200_data import GetVrboListingPaymentTermsResponse200Data





T = TypeVar("T", bound="GetVrboListingPaymentTermsResponse200")



@_attrs_define
class GetVrboListingPaymentTermsResponse200:
    """ 
        Attributes:
            listing_id (str):
            vrbo_listing_number (str):
            property_id (str): Vrbo's property id for the unit.
            section (str):  Example: payment-terms.
            data (GetVrboListingPaymentTermsResponse200Data): The section as Vrbo has it now.
     """

    listing_id: str
    vrbo_listing_number: str
    property_id: str
    section: str
    data: GetVrboListingPaymentTermsResponse200Data
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_payment_terms_response_200_data import GetVrboListingPaymentTermsResponse200Data
        listing_id = self.listing_id

        vrbo_listing_number = self.vrbo_listing_number

        property_id = self.property_id

        section = self.section

        data = self.data.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "listingId": listing_id,
            "vrboListingNumber": vrbo_listing_number,
            "propertyId": property_id,
            "section": section,
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_payment_terms_response_200_data import GetVrboListingPaymentTermsResponse200Data
        d = dict(src_dict)
        listing_id = d.pop("listingId")

        vrbo_listing_number = d.pop("vrboListingNumber")

        property_id = d.pop("propertyId")

        section = d.pop("section")

        data = GetVrboListingPaymentTermsResponse200Data.from_dict(d.pop("data"))




        get_vrbo_listing_payment_terms_response_200 = cls(
            listing_id=listing_id,
            vrbo_listing_number=vrbo_listing_number,
            property_id=property_id,
            section=section,
            data=data,
        )


        get_vrbo_listing_payment_terms_response_200.additional_properties = d
        return get_vrbo_listing_payment_terms_response_200

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
