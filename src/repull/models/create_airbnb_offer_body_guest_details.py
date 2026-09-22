from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateAirbnbOfferBodyGuestDetails")



@_attrs_define
class CreateAirbnbOfferBodyGuestDetails:
    """ Offer only (required). `number_of_guests` is adults + children; if omitted it is computed from them.

        Attributes:
            number_of_guests (int | Unset):  Example: 3.
            number_of_adults (int | Unset):  Example: 2.
            number_of_children (int | Unset):  Example: 1.
            number_of_infants (int | Unset):
            number_of_pets (int | Unset):
     """

    number_of_guests: int | Unset = UNSET
    number_of_adults: int | Unset = UNSET
    number_of_children: int | Unset = UNSET
    number_of_infants: int | Unset = UNSET
    number_of_pets: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        number_of_guests = self.number_of_guests

        number_of_adults = self.number_of_adults

        number_of_children = self.number_of_children

        number_of_infants = self.number_of_infants

        number_of_pets = self.number_of_pets


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if number_of_guests is not UNSET:
            field_dict["number_of_guests"] = number_of_guests
        if number_of_adults is not UNSET:
            field_dict["number_of_adults"] = number_of_adults
        if number_of_children is not UNSET:
            field_dict["number_of_children"] = number_of_children
        if number_of_infants is not UNSET:
            field_dict["number_of_infants"] = number_of_infants
        if number_of_pets is not UNSET:
            field_dict["number_of_pets"] = number_of_pets

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number_of_guests = d.pop("number_of_guests", UNSET)

        number_of_adults = d.pop("number_of_adults", UNSET)

        number_of_children = d.pop("number_of_children", UNSET)

        number_of_infants = d.pop("number_of_infants", UNSET)

        number_of_pets = d.pop("number_of_pets", UNSET)

        create_airbnb_offer_body_guest_details = cls(
            number_of_guests=number_of_guests,
            number_of_adults=number_of_adults,
            number_of_children=number_of_children,
            number_of_infants=number_of_infants,
            number_of_pets=number_of_pets,
        )


        create_airbnb_offer_body_guest_details.additional_properties = d
        return create_airbnb_offer_body_guest_details

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
