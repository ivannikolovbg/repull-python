from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_content_response_200_data_freshness import GetVrboListingContentResponse200DataFreshness
  from ..models.get_vrbo_listing_content_response_200_sections import GetVrboListingContentResponse200Sections





T = TypeVar("T", bound="GetVrboListingContentResponse200")



@_attrs_define
class GetVrboListingContentResponse200:
    """ 
        Attributes:
            sections (GetVrboListingContentResponse200Sections): Keyed by section; each is the `data` of `GET
                /v1/channels/vrbo/listings/{id}/{section}`, or `{ error: { code, message } }` when that section failed.
            data_freshness (GetVrboListingContentResponse200DataFreshness):
            vrbo_listing_number (str):
     """

    sections: GetVrboListingContentResponse200Sections
    data_freshness: GetVrboListingContentResponse200DataFreshness
    vrbo_listing_number: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_content_response_200_data_freshness import GetVrboListingContentResponse200DataFreshness
        from ..models.get_vrbo_listing_content_response_200_sections import GetVrboListingContentResponse200Sections
        sections = self.sections.to_dict()

        data_freshness = self.data_freshness.to_dict()

        vrbo_listing_number = self.vrbo_listing_number


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "sections": sections,
            "dataFreshness": data_freshness,
            "vrboListingNumber": vrbo_listing_number,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_content_response_200_data_freshness import GetVrboListingContentResponse200DataFreshness
        from ..models.get_vrbo_listing_content_response_200_sections import GetVrboListingContentResponse200Sections
        d = dict(src_dict)
        sections = GetVrboListingContentResponse200Sections.from_dict(d.pop("sections"))




        data_freshness = GetVrboListingContentResponse200DataFreshness.from_dict(d.pop("dataFreshness"))




        vrbo_listing_number = d.pop("vrboListingNumber")

        get_vrbo_listing_content_response_200 = cls(
            sections=sections,
            data_freshness=data_freshness,
            vrbo_listing_number=vrbo_listing_number,
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
