from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateConversationSpecialOfferBodyGuests")



@_attrs_define
class CreateConversationSpecialOfferBodyGuests:
    """ 
        Attributes:
            adults (int):  Example: 2.
            children (int | Unset):  Default: 0.
            infants (int | Unset):  Default: 0.
            pets (int | Unset):  Default: 0.
     """

    adults: int
    children: int | Unset = 0
    infants: int | Unset = 0
    pets: int | Unset = 0





    def to_dict(self) -> dict[str, Any]:
        adults = self.adults

        children = self.children

        infants = self.infants

        pets = self.pets


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "adults": adults,
        })
        if children is not UNSET:
            field_dict["children"] = children
        if infants is not UNSET:
            field_dict["infants"] = infants
        if pets is not UNSET:
            field_dict["pets"] = pets

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        adults = d.pop("adults")

        children = d.pop("children", UNSET)

        infants = d.pop("infants", UNSET)

        pets = d.pop("pets", UNSET)

        create_conversation_special_offer_body_guests = cls(
            adults=adults,
            children=children,
            infants=infants,
            pets=pets,
        )

        return create_conversation_special_offer_body_guests

