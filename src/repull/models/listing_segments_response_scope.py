from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingSegmentsResponseScope")



@_attrs_define
class ListingSegmentsResponseScope:
    """ When `level=comp_set` carries `radiusKm`; when `level=market` carries `city`. May be empty when neither could be
    resolved.

        Attributes:
            radius_km (float | None | Unset):
            city (None | str | Unset):
     """

    radius_km: float | None | Unset = UNSET
    city: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        radius_km: float | None | Unset
        if isinstance(self.radius_km, Unset):
            radius_km = UNSET
        else:
            radius_km = self.radius_km

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if radius_km is not UNSET:
            field_dict["radiusKm"] = radius_km
        if city is not UNSET:
            field_dict["city"] = city

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_radius_km(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        radius_km = _parse_radius_km(d.pop("radiusKm", UNSET))


        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))


        listing_segments_response_scope = cls(
            radius_km=radius_km,
            city=city,
        )


        listing_segments_response_scope.additional_properties = d
        return listing_segments_response_scope

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
