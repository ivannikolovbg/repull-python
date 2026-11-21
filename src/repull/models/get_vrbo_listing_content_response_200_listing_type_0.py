from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetVrboListingContentResponse200ListingType0")



@_attrs_define
class GetVrboListingContentResponse200ListingType0:
    """ 
        Attributes:
            triad (None | str | Unset):
            listing_number (None | str | Unset):
            unit_number (None | str | Unset):
            unit_url (None | str | Unset):
            enabled (bool | None | Unset):
            address (Any | Unset):
     """

    triad: None | str | Unset = UNSET
    listing_number: None | str | Unset = UNSET
    unit_number: None | str | Unset = UNSET
    unit_url: None | str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    address: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        triad: None | str | Unset
        if isinstance(self.triad, Unset):
            triad = UNSET
        else:
            triad = self.triad

        listing_number: None | str | Unset
        if isinstance(self.listing_number, Unset):
            listing_number = UNSET
        else:
            listing_number = self.listing_number

        unit_number: None | str | Unset
        if isinstance(self.unit_number, Unset):
            unit_number = UNSET
        else:
            unit_number = self.unit_number

        unit_url: None | str | Unset
        if isinstance(self.unit_url, Unset):
            unit_url = UNSET
        else:
            unit_url = self.unit_url

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        address = self.address


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if triad is not UNSET:
            field_dict["triad"] = triad
        if listing_number is not UNSET:
            field_dict["listingNumber"] = listing_number
        if unit_number is not UNSET:
            field_dict["unitNumber"] = unit_number
        if unit_url is not UNSET:
            field_dict["unitUrl"] = unit_url
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_triad(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        triad = _parse_triad(d.pop("triad", UNSET))


        def _parse_listing_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_number = _parse_listing_number(d.pop("listingNumber", UNSET))


        def _parse_unit_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_number = _parse_unit_number(d.pop("unitNumber", UNSET))


        def _parse_unit_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_url = _parse_unit_url(d.pop("unitUrl", UNSET))


        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))


        address = d.pop("address", UNSET)

        get_vrbo_listing_content_response_200_listing_type_0 = cls(
            triad=triad,
            listing_number=listing_number,
            unit_number=unit_number,
            unit_url=unit_url,
            enabled=enabled,
            address=address,
        )


        get_vrbo_listing_content_response_200_listing_type_0.additional_properties = d
        return get_vrbo_listing_content_response_200_listing_type_0

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
