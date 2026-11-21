from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetVrboListingContentResponse200SectionsLocation")



@_attrs_define
class GetVrboListingContentResponse200SectionsLocation:
    """ 
        Attributes:
            address (Any | Unset): The address (read-only: Vrbo changes it only through its support).
            address_editable (bool | Unset):
            show_exact_location (bool | None | Unset):
     """

    address: Any | Unset = UNSET
    address_editable: bool | Unset = UNSET
    show_exact_location: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        address = self.address

        address_editable = self.address_editable

        show_exact_location: bool | None | Unset
        if isinstance(self.show_exact_location, Unset):
            show_exact_location = UNSET
        else:
            show_exact_location = self.show_exact_location


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if address is not UNSET:
            field_dict["address"] = address
        if address_editable is not UNSET:
            field_dict["addressEditable"] = address_editable
        if show_exact_location is not UNSET:
            field_dict["showExactLocation"] = show_exact_location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address = d.pop("address", UNSET)

        address_editable = d.pop("addressEditable", UNSET)

        def _parse_show_exact_location(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_exact_location = _parse_show_exact_location(d.pop("showExactLocation", UNSET))


        get_vrbo_listing_content_response_200_sections_location = cls(
            address=address,
            address_editable=address_editable,
            show_exact_location=show_exact_location,
        )


        get_vrbo_listing_content_response_200_sections_location.additional_properties = d
        return get_vrbo_listing_content_response_200_sections_location

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
