from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_response_200_data_item_capacity_pets import GetVrboListingResponse200DataItemCapacityPets





T = TypeVar("T", bound="GetVrboListingResponse200DataItemCapacity")



@_attrs_define
class GetVrboListingResponse200DataItemCapacity:
    """ 
        Attributes:
            max_guests (int | None | Unset):
            max_adults (int | None | Unset):
            max_children (int | None | Unset):
            pets (GetVrboListingResponse200DataItemCapacityPets | Unset):
     """

    max_guests: int | None | Unset = UNSET
    max_adults: int | None | Unset = UNSET
    max_children: int | None | Unset = UNSET
    pets: GetVrboListingResponse200DataItemCapacityPets | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_response_200_data_item_capacity_pets import GetVrboListingResponse200DataItemCapacityPets
        max_guests: int | None | Unset
        if isinstance(self.max_guests, Unset):
            max_guests = UNSET
        else:
            max_guests = self.max_guests

        max_adults: int | None | Unset
        if isinstance(self.max_adults, Unset):
            max_adults = UNSET
        else:
            max_adults = self.max_adults

        max_children: int | None | Unset
        if isinstance(self.max_children, Unset):
            max_children = UNSET
        else:
            max_children = self.max_children

        pets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pets, Unset):
            pets = self.pets.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if max_guests is not UNSET:
            field_dict["maxGuests"] = max_guests
        if max_adults is not UNSET:
            field_dict["maxAdults"] = max_adults
        if max_children is not UNSET:
            field_dict["maxChildren"] = max_children
        if pets is not UNSET:
            field_dict["pets"] = pets

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_response_200_data_item_capacity_pets import GetVrboListingResponse200DataItemCapacityPets
        d = dict(src_dict)
        def _parse_max_guests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_guests = _parse_max_guests(d.pop("maxGuests", UNSET))


        def _parse_max_adults(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_adults = _parse_max_adults(d.pop("maxAdults", UNSET))


        def _parse_max_children(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_children = _parse_max_children(d.pop("maxChildren", UNSET))


        _pets = d.pop("pets", UNSET)
        pets: GetVrboListingResponse200DataItemCapacityPets | Unset
        if isinstance(_pets,  Unset):
            pets = UNSET
        else:
            pets = GetVrboListingResponse200DataItemCapacityPets.from_dict(_pets)




        get_vrbo_listing_response_200_data_item_capacity = cls(
            max_guests=max_guests,
            max_adults=max_adults,
            max_children=max_children,
            pets=pets,
        )


        get_vrbo_listing_response_200_data_item_capacity.additional_properties = d
        return get_vrbo_listing_response_200_data_item_capacity

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
