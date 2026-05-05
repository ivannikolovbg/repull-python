from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ReservationOccupancy")



@_attrs_define
class ReservationOccupancy:
    """ Normalized guest counts for the stay. Mirrors the legacy `guestDetails.numberOf*` fields under canonical short
    names. Omitted when no count fields are present on the reservation.

        Attributes:
            adults (int | None | Unset):
            children (int | None | Unset):
            infants (int | None | Unset):
            pets (int | None | Unset):
            total (int | None | Unset): Total guests (sum across all categories as reported by the source channel).
     """

    adults: int | None | Unset = UNSET
    children: int | None | Unset = UNSET
    infants: int | None | Unset = UNSET
    pets: int | None | Unset = UNSET
    total: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        adults: int | None | Unset
        if isinstance(self.adults, Unset):
            adults = UNSET
        else:
            adults = self.adults

        children: int | None | Unset
        if isinstance(self.children, Unset):
            children = UNSET
        else:
            children = self.children

        infants: int | None | Unset
        if isinstance(self.infants, Unset):
            infants = UNSET
        else:
            infants = self.infants

        pets: int | None | Unset
        if isinstance(self.pets, Unset):
            pets = UNSET
        else:
            pets = self.pets

        total: int | None | Unset
        if isinstance(self.total, Unset):
            total = UNSET
        else:
            total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if adults is not UNSET:
            field_dict["adults"] = adults
        if children is not UNSET:
            field_dict["children"] = children
        if infants is not UNSET:
            field_dict["infants"] = infants
        if pets is not UNSET:
            field_dict["pets"] = pets
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_adults(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        adults = _parse_adults(d.pop("adults", UNSET))


        def _parse_children(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        children = _parse_children(d.pop("children", UNSET))


        def _parse_infants(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        infants = _parse_infants(d.pop("infants", UNSET))


        def _parse_pets(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pets = _parse_pets(d.pop("pets", UNSET))


        def _parse_total(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total = _parse_total(d.pop("total", UNSET))


        reservation_occupancy = cls(
            adults=adults,
            children=children,
            infants=infants,
            pets=pets,
            total=total,
        )


        reservation_occupancy.additional_properties = d
        return reservation_occupancy

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
