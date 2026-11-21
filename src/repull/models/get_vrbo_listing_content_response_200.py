from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_content_response_200_listing_type_0 import GetVrboListingContentResponse200ListingType0
  from ..models.get_vrbo_listing_content_response_200_sections import GetVrboListingContentResponse200Sections





T = TypeVar("T", bound="GetVrboListingContentResponse200")



@_attrs_define
class GetVrboListingContentResponse200:
    """ 
        Attributes:
            listing_id (str):
            vrbo_listing_number (str):
            property_id (str):
            sections (GetVrboListingContentResponse200Sections): Keyed by section; each is the data of `GET
                /v1/channels/vrbo/listings/{id}/{section}`, or `{ error: { code, message } }` when that section failed.
            listing (GetVrboListingContentResponse200ListingType0 | None | Unset):
     """

    listing_id: str
    vrbo_listing_number: str
    property_id: str
    sections: GetVrboListingContentResponse200Sections
    listing: GetVrboListingContentResponse200ListingType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_content_response_200_listing_type_0 import GetVrboListingContentResponse200ListingType0
        from ..models.get_vrbo_listing_content_response_200_sections import GetVrboListingContentResponse200Sections
        listing_id = self.listing_id

        vrbo_listing_number = self.vrbo_listing_number

        property_id = self.property_id

        sections = self.sections.to_dict()

        listing: dict[str, Any] | None | Unset
        if isinstance(self.listing, Unset):
            listing = UNSET
        elif isinstance(self.listing, GetVrboListingContentResponse200ListingType0):
            listing = self.listing.to_dict()
        else:
            listing = self.listing


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "listingId": listing_id,
            "vrboListingNumber": vrbo_listing_number,
            "propertyId": property_id,
            "sections": sections,
        })
        if listing is not UNSET:
            field_dict["listing"] = listing

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_content_response_200_listing_type_0 import GetVrboListingContentResponse200ListingType0
        from ..models.get_vrbo_listing_content_response_200_sections import GetVrboListingContentResponse200Sections
        d = dict(src_dict)
        listing_id = d.pop("listingId")

        vrbo_listing_number = d.pop("vrboListingNumber")

        property_id = d.pop("propertyId")

        sections = GetVrboListingContentResponse200Sections.from_dict(d.pop("sections"))




        def _parse_listing(data: object) -> GetVrboListingContentResponse200ListingType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                listing_type_0 = GetVrboListingContentResponse200ListingType0.from_dict(data)



                return listing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboListingContentResponse200ListingType0 | None | Unset, data)

        listing = _parse_listing(d.pop("listing", UNSET))


        get_vrbo_listing_content_response_200 = cls(
            listing_id=listing_id,
            vrbo_listing_number=vrbo_listing_number,
            property_id=property_id,
            sections=sections,
            listing=listing,
        )


        get_vrbo_listing_content_response_200.additional_properties = d
        return get_vrbo_listing_content_response_200

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
