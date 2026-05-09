from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.airbnb_connection_accessibility_amenities_type_0_item import AirbnbConnectionAccessibilityAmenitiesType0Item
  from ..models.airbnb_connection_amenities_type_0_item import AirbnbConnectionAmenitiesType0Item





T = TypeVar("T", bound="AirbnbConnection")



@_attrs_define
class AirbnbConnection:
    """ An Airbnb-side connection record for a Vanio listing. The same property may appear under multiple connections if it
    has been linked from multiple Airbnb host accounts.

        Attributes:
            id (int | Unset): Connection row id
            airbnb_id (str | Unset): Airbnb-side listing id Example: 1116939745194659457.
            host_id (str | Unset): Airbnb host user id
            active (bool | Unset):
            sync_enabled (bool | Unset):
            primary (bool | Unset):
            markup (None | str | Unset): Decimal markup (e.g. "1.10" for +10%).
            created_at (datetime.datetime | Unset):
            amenities (list[AirbnbConnectionAmenitiesType0Item] | None | Unset): Present only when `?include=amenities` is
                passed. Sourced from the local `listings_airbnb_amenities` cache (populated by the Airbnb sync worker). Returns
                `null` when the cache is empty for this connection — see the top-level `data_freshness` envelope to disambiguate
                "never synced" vs "host disconnected" vs "fresh and genuinely empty".
            accessibility_amenities (list[AirbnbConnectionAccessibilityAmenitiesType0Item] | None | Unset): Present only
                when `?include=amenities` is passed. Accessibility-tagged subset of the local amenity cache (step-free access,
                wide doorways, grab rails, disabled parking, wheelchair, accessible-height fixtures, hoists, etc). Returns an
                empty array when amenities synced but none qualify as accessibility; returns `null` when the cache is empty for
                this connection (use `data_freshness` to disambiguate "never synced" from "fresh and genuinely empty").
     """

    id: int | Unset = UNSET
    airbnb_id: str | Unset = UNSET
    host_id: str | Unset = UNSET
    active: bool | Unset = UNSET
    sync_enabled: bool | Unset = UNSET
    primary: bool | Unset = UNSET
    markup: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    amenities: list[AirbnbConnectionAmenitiesType0Item] | None | Unset = UNSET
    accessibility_amenities: list[AirbnbConnectionAccessibilityAmenitiesType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_connection_accessibility_amenities_type_0_item import AirbnbConnectionAccessibilityAmenitiesType0Item
        from ..models.airbnb_connection_amenities_type_0_item import AirbnbConnectionAmenitiesType0Item
        id = self.id

        airbnb_id = self.airbnb_id

        host_id = self.host_id

        active = self.active

        sync_enabled = self.sync_enabled

        primary = self.primary

        markup: None | str | Unset
        if isinstance(self.markup, Unset):
            markup = UNSET
        else:
            markup = self.markup

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        amenities: list[dict[str, Any]] | None | Unset
        if isinstance(self.amenities, Unset):
            amenities = UNSET
        elif isinstance(self.amenities, list):
            amenities = []
            for amenities_type_0_item_data in self.amenities:
                amenities_type_0_item = amenities_type_0_item_data.to_dict()
                amenities.append(amenities_type_0_item)


        else:
            amenities = self.amenities

        accessibility_amenities: list[dict[str, Any]] | None | Unset
        if isinstance(self.accessibility_amenities, Unset):
            accessibility_amenities = UNSET
        elif isinstance(self.accessibility_amenities, list):
            accessibility_amenities = []
            for accessibility_amenities_type_0_item_data in self.accessibility_amenities:
                accessibility_amenities_type_0_item = accessibility_amenities_type_0_item_data.to_dict()
                accessibility_amenities.append(accessibility_amenities_type_0_item)


        else:
            accessibility_amenities = self.accessibility_amenities


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if airbnb_id is not UNSET:
            field_dict["airbnbId"] = airbnb_id
        if host_id is not UNSET:
            field_dict["hostId"] = host_id
        if active is not UNSET:
            field_dict["active"] = active
        if sync_enabled is not UNSET:
            field_dict["syncEnabled"] = sync_enabled
        if primary is not UNSET:
            field_dict["primary"] = primary
        if markup is not UNSET:
            field_dict["markup"] = markup
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if amenities is not UNSET:
            field_dict["amenities"] = amenities
        if accessibility_amenities is not UNSET:
            field_dict["accessibility_amenities"] = accessibility_amenities

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_connection_accessibility_amenities_type_0_item import AirbnbConnectionAccessibilityAmenitiesType0Item
        from ..models.airbnb_connection_amenities_type_0_item import AirbnbConnectionAmenitiesType0Item
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        airbnb_id = d.pop("airbnbId", UNSET)

        host_id = d.pop("hostId", UNSET)

        active = d.pop("active", UNSET)

        sync_enabled = d.pop("syncEnabled", UNSET)

        primary = d.pop("primary", UNSET)

        def _parse_markup(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        markup = _parse_markup(d.pop("markup", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        def _parse_amenities(data: object) -> list[AirbnbConnectionAmenitiesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                amenities_type_0 = []
                _amenities_type_0 = data
                for amenities_type_0_item_data in (_amenities_type_0):
                    amenities_type_0_item = AirbnbConnectionAmenitiesType0Item.from_dict(amenities_type_0_item_data)



                    amenities_type_0.append(amenities_type_0_item)

                return amenities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AirbnbConnectionAmenitiesType0Item] | None | Unset, data)

        amenities = _parse_amenities(d.pop("amenities", UNSET))


        def _parse_accessibility_amenities(data: object) -> list[AirbnbConnectionAccessibilityAmenitiesType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                accessibility_amenities_type_0 = []
                _accessibility_amenities_type_0 = data
                for accessibility_amenities_type_0_item_data in (_accessibility_amenities_type_0):
                    accessibility_amenities_type_0_item = AirbnbConnectionAccessibilityAmenitiesType0Item.from_dict(accessibility_amenities_type_0_item_data)



                    accessibility_amenities_type_0.append(accessibility_amenities_type_0_item)

                return accessibility_amenities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AirbnbConnectionAccessibilityAmenitiesType0Item] | None | Unset, data)

        accessibility_amenities = _parse_accessibility_amenities(d.pop("accessibility_amenities", UNSET))


        airbnb_connection = cls(
            id=id,
            airbnb_id=airbnb_id,
            host_id=host_id,
            active=active,
            sync_enabled=sync_enabled,
            primary=primary,
            markup=markup,
            created_at=created_at,
            amenities=amenities,
            accessibility_amenities=accessibility_amenities,
        )


        airbnb_connection.additional_properties = d
        return airbnb_connection

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
