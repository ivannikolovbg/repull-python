from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_airbnb_location_response_200_data_address_type_0 import GetAirbnbLocationResponse200DataAddressType0





T = TypeVar("T", bound="GetAirbnbLocationResponse200Data")



@_attrs_define
class GetAirbnbLocationResponse200Data:
    """ 
        Attributes:
            address (GetAirbnbLocationResponse200DataAddressType0 | None | Unset):
            address_editable (bool | Unset):
            lat (float | None | Unset):
            lng (float | None | Unset):
            show_exact_location (bool | None | Unset):
            directions (None | str | Unset):
     """

    address: GetAirbnbLocationResponse200DataAddressType0 | None | Unset = UNSET
    address_editable: bool | Unset = UNSET
    lat: float | None | Unset = UNSET
    lng: float | None | Unset = UNSET
    show_exact_location: bool | None | Unset = UNSET
    directions: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_airbnb_location_response_200_data_address_type_0 import GetAirbnbLocationResponse200DataAddressType0
        address: dict[str, Any] | None | Unset
        if isinstance(self.address, Unset):
            address = UNSET
        elif isinstance(self.address, GetAirbnbLocationResponse200DataAddressType0):
            address = self.address.to_dict()
        else:
            address = self.address

        address_editable = self.address_editable

        lat: float | None | Unset
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        lng: float | None | Unset
        if isinstance(self.lng, Unset):
            lng = UNSET
        else:
            lng = self.lng

        show_exact_location: bool | None | Unset
        if isinstance(self.show_exact_location, Unset):
            show_exact_location = UNSET
        else:
            show_exact_location = self.show_exact_location

        directions: None | str | Unset
        if isinstance(self.directions, Unset):
            directions = UNSET
        else:
            directions = self.directions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if address is not UNSET:
            field_dict["address"] = address
        if address_editable is not UNSET:
            field_dict["addressEditable"] = address_editable
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if show_exact_location is not UNSET:
            field_dict["showExactLocation"] = show_exact_location
        if directions is not UNSET:
            field_dict["directions"] = directions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_airbnb_location_response_200_data_address_type_0 import GetAirbnbLocationResponse200DataAddressType0
        d = dict(src_dict)
        def _parse_address(data: object) -> GetAirbnbLocationResponse200DataAddressType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = GetAirbnbLocationResponse200DataAddressType0.from_dict(data)



                return address_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetAirbnbLocationResponse200DataAddressType0 | None | Unset, data)

        address = _parse_address(d.pop("address", UNSET))


        address_editable = d.pop("addressEditable", UNSET)

        def _parse_lat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lat = _parse_lat(d.pop("lat", UNSET))


        def _parse_lng(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lng = _parse_lng(d.pop("lng", UNSET))


        def _parse_show_exact_location(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        show_exact_location = _parse_show_exact_location(d.pop("showExactLocation", UNSET))


        def _parse_directions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        directions = _parse_directions(d.pop("directions", UNSET))


        get_airbnb_location_response_200_data = cls(
            address=address,
            address_editable=address_editable,
            lat=lat,
            lng=lng,
            show_exact_location=show_exact_location,
            directions=directions,
        )


        get_airbnb_location_response_200_data.additional_properties = d
        return get_airbnb_location_response_200_data

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
