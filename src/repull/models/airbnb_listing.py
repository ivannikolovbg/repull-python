from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_connection import AirbnbConnection





T = TypeVar("T", bound="AirbnbListing")



@_attrs_define
class AirbnbListing:
    """ A Vanio listing paired with its Airbnb connection rows. The list endpoint groups every `listings_airbnb` row that
    points at the same Vanio `listingId` under a single `connections[]` array.

        Attributes:
            listing_id (int | Unset): Vanio (Repull) listing id Example: 6248.
            name (str | Unset): Listing title Example: Oceanview Villa.
            city (None | str | Unset):  Example: Malibu.
            connections (list[AirbnbConnection] | Unset):
     """

    listing_id: int | Unset = UNSET
    name: str | Unset = UNSET
    city: None | str | Unset = UNSET
    connections: list[AirbnbConnection] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_connection import AirbnbConnection
        listing_id = self.listing_id

        name = self.name

        city: None | str | Unset
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        connections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.connections, Unset):
            connections = []
            for connections_item_data in self.connections:
                connections_item = connections_item_data.to_dict()
                connections.append(connections_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if name is not UNSET:
            field_dict["name"] = name
        if city is not UNSET:
            field_dict["city"] = city
        if connections is not UNSET:
            field_dict["connections"] = connections

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_connection import AirbnbConnection
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        name = d.pop("name", UNSET)

        def _parse_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        city = _parse_city(d.pop("city", UNSET))


        _connections = d.pop("connections", UNSET)
        connections: list[AirbnbConnection] | Unset = UNSET
        if _connections is not UNSET:
            connections = []
            for connections_item_data in _connections:
                connections_item = AirbnbConnection.from_dict(connections_item_data)



                connections.append(connections_item)


        airbnb_listing = cls(
            listing_id=listing_id,
            name=name,
            city=city,
            connections=connections,
        )


        airbnb_listing.additional_properties = d
        return airbnb_listing

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
