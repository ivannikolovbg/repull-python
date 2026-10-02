from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.reservation_capabilities import ReservationCapabilities





T = TypeVar("T", bound="ListingCapabilities")



@_attrs_define
class ListingCapabilities:
    """ `GET /v1/listings/{id}` only. What the API can do with this listing.

        Attributes:
            reservations (ReservationCapabilities | Unset): Which reservation writes the API performs for this listing (or,
                on `GET /v1/connect/{provider}`, for any listing of that connection). Derived from the PMS connector, the
                connection, and its write policy — a flag is true only when all three allow it.
     """

    reservations: ReservationCapabilities | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_capabilities import ReservationCapabilities
        reservations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reservations, Unset):
            reservations = self.reservations.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reservations is not UNSET:
            field_dict["reservations"] = reservations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_capabilities import ReservationCapabilities
        d = dict(src_dict)
        _reservations = d.pop("reservations", UNSET)
        reservations: ReservationCapabilities | Unset
        if isinstance(_reservations,  Unset):
            reservations = UNSET
        else:
            reservations = ReservationCapabilities.from_dict(_reservations)




        listing_capabilities = cls(
            reservations=reservations,
        )


        listing_capabilities.additional_properties = d
        return listing_capabilities

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
