from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tiket_rate_plan import TiketRatePlan





T = TypeVar("T", bound="TiketRoom")



@_attrs_define
class TiketRoom:
    """ A tiket.com room type and the listing it is mapped to.

        Attributes:
            room_id (str | Unset): Repull id of the room (used by the Connect mapping).
            room_type_code (str | Unset): tiket.com room type id.
            name (None | str | Unset):
            max_adults (int | None | Unset):
            max_children (int | None | Unset):
            units (int | None | Unset): Rooms of this type at the property.
            listing_id (None | str | Unset): The mapped Repull listing, or `null` when the room is not mapped (or its
                listing is hidden by `?status=`).
            listing_hidden (bool | Unset): `true` when the room is mapped to a listing that `?status=` hides.
            rate_plans (list[TiketRatePlan] | Unset):
     """

    room_id: str | Unset = UNSET
    room_type_code: str | Unset = UNSET
    name: None | str | Unset = UNSET
    max_adults: int | None | Unset = UNSET
    max_children: int | None | Unset = UNSET
    units: int | None | Unset = UNSET
    listing_id: None | str | Unset = UNSET
    listing_hidden: bool | Unset = UNSET
    rate_plans: list[TiketRatePlan] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tiket_rate_plan import TiketRatePlan
        room_id = self.room_id

        room_type_code = self.room_type_code

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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

        units: int | None | Unset
        if isinstance(self.units, Unset):
            units = UNSET
        else:
            units = self.units

        listing_id: None | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        listing_hidden = self.listing_hidden

        rate_plans: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rate_plans, Unset):
            rate_plans = []
            for rate_plans_item_data in self.rate_plans:
                rate_plans_item = rate_plans_item_data.to_dict()
                rate_plans.append(rate_plans_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if room_id is not UNSET:
            field_dict["roomId"] = room_id
        if room_type_code is not UNSET:
            field_dict["roomTypeCode"] = room_type_code
        if name is not UNSET:
            field_dict["name"] = name
        if max_adults is not UNSET:
            field_dict["maxAdults"] = max_adults
        if max_children is not UNSET:
            field_dict["maxChildren"] = max_children
        if units is not UNSET:
            field_dict["units"] = units
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if listing_hidden is not UNSET:
            field_dict["listingHidden"] = listing_hidden
        if rate_plans is not UNSET:
            field_dict["ratePlans"] = rate_plans

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiket_rate_plan import TiketRatePlan
        d = dict(src_dict)
        room_id = d.pop("roomId", UNSET)

        room_type_code = d.pop("roomTypeCode", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


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


        def _parse_units(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        units = _parse_units(d.pop("units", UNSET))


        def _parse_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        listing_hidden = d.pop("listingHidden", UNSET)

        _rate_plans = d.pop("ratePlans", UNSET)
        rate_plans: list[TiketRatePlan] | Unset = UNSET
        if _rate_plans is not UNSET:
            rate_plans = []
            for rate_plans_item_data in _rate_plans:
                rate_plans_item = TiketRatePlan.from_dict(rate_plans_item_data)



                rate_plans.append(rate_plans_item)


        tiket_room = cls(
            room_id=room_id,
            room_type_code=room_type_code,
            name=name,
            max_adults=max_adults,
            max_children=max_children,
            units=units,
            listing_id=listing_id,
            listing_hidden=listing_hidden,
            rate_plans=rate_plans,
        )


        tiket_room.additional_properties = d
        return tiket_room

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
