from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_connection_sync_category import AirbnbConnectionSyncCategory
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
            id (str | Unset): Connection row id
            airbnb_id (str | Unset): Airbnb-side listing id Example: 1116939745194659457.
            account_id (None | str | Unset): Which connected Airbnb account this row belongs to — the Airbnb host id, as a
                string (they exceed 2^53). The same value `?account_id=` accepts and `GET /v1/connect/airbnb` returns as
                `accounts[].externalAccountId`. Example: 1772489413932732258.
            account_name (None | str | Unset): Display name of that connected Airbnb account. Example: Pomello.
            host_id (None | str | Unset): Alias of `accountId`, kept for compatibility — same Airbnb host id, same string.
            host_name (None | str | Unset): Alias of `accountName`, kept for compatibility.
            active (bool | Unset):
            sync_enabled (bool | Unset):
            primary (bool | Unset):
            markup (None | str | Unset): The Airbnb markup as a fraction: "0.35" = +35% on the listing's own price. Read or
                set it as a percentage with `/v1/listings/{id}/markups`.
            sync_category (AirbnbConnectionSyncCategory | Unset): Airbnb's own API sync decision for THIS listing, as Airbnb
                reports it. Airbnb authorises sync one listing at a time, so a connected account can still contain listings it
                will not accept writes for.

                - `sync_all` — Repull manages content, rates and availability.
                - `sync_rates_and_availability` — Repull manages rates and availability; listing content is managed by the host
                on Airbnb.
                - `none` — the listing is **not** connected to Repull on Airbnb's side. Every write to it is refused with `403
                listing_not_api_connected`; reconnecting the Airbnb account does not change this, the host must switch the
                listing on in Airbnb.

                `null` when the listing has not synced yet. Not to be confused with `syncEnabled`, which is a Repull-side flag
                and says nothing about what Airbnb accepts. Example: sync_all.
            writable (bool | Unset): Whether Repull will send a write for this listing to Airbnb. `false` exactly when
                `syncCategory` is `none` — such a write is refused with `403 listing_not_api_connected` before anything reaches
                Airbnb. Check this before a portfolio-wide push instead of discovering it one 403 at a time. Example: True.
            created_at (datetime.datetime | Unset):
            locked_fields (list[str] | Unset): Fields Airbnb will NOT let you change on this listing —
                `property_type_category`, `name`, `check_in_option`, `summary`, `space`, individual amenities, … Airbnb does not
                refuse a write to a locked field: it returns 200, reports the field as locked, and applies nothing. Check this
                before a content write; `[]` means nothing is known to be locked. Recorded at sync time, so a lock added on
                Airbnb since the last sync will show up on the write instead (as `blockedFields` in the response). Example:
                ['name', 'summary', 'property_type_category'].
            amenities (list[AirbnbConnectionAmenitiesType0Item] | None | Unset): Present only when `?include=amenities` is
                passed. Sourced from the local `listings_airbnb_amenities` cache (populated by the Airbnb sync worker). Returns
                `null` when the cache is empty for this connection — see the top-level `dataFreshness` envelope to disambiguate
                "never synced" vs "host disconnected" vs "fresh and genuinely empty".
            accessibility_amenities (list[AirbnbConnectionAccessibilityAmenitiesType0Item] | None | Unset): Present only
                when `?include=amenities` is passed. Accessibility-tagged subset of the local amenity cache (step-free access,
                wide doorways, grab rails, disabled parking, wheelchair, accessible-height fixtures, hoists, etc). Returns an
                empty array when amenities synced but none qualify as accessibility; returns `null` when the cache is empty for
                this connection (use `dataFreshness` to disambiguate "never synced" from "fresh and genuinely empty").
     """

    id: str | Unset = UNSET
    airbnb_id: str | Unset = UNSET
    account_id: None | str | Unset = UNSET
    account_name: None | str | Unset = UNSET
    host_id: None | str | Unset = UNSET
    host_name: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    sync_enabled: bool | Unset = UNSET
    primary: bool | Unset = UNSET
    markup: None | str | Unset = UNSET
    sync_category: AirbnbConnectionSyncCategory | Unset = UNSET
    writable: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    locked_fields: list[str] | Unset = UNSET
    amenities: list[AirbnbConnectionAmenitiesType0Item] | None | Unset = UNSET
    accessibility_amenities: list[AirbnbConnectionAccessibilityAmenitiesType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_connection_accessibility_amenities_type_0_item import AirbnbConnectionAccessibilityAmenitiesType0Item
        from ..models.airbnb_connection_amenities_type_0_item import AirbnbConnectionAmenitiesType0Item
        id = self.id

        airbnb_id = self.airbnb_id

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        account_name: None | str | Unset
        if isinstance(self.account_name, Unset):
            account_name = UNSET
        else:
            account_name = self.account_name

        host_id: None | str | Unset
        if isinstance(self.host_id, Unset):
            host_id = UNSET
        else:
            host_id = self.host_id

        host_name: None | str | Unset
        if isinstance(self.host_name, Unset):
            host_name = UNSET
        else:
            host_name = self.host_name

        active = self.active

        sync_enabled = self.sync_enabled

        primary = self.primary

        markup: None | str | Unset
        if isinstance(self.markup, Unset):
            markup = UNSET
        else:
            markup = self.markup

        sync_category: str | Unset = UNSET
        if not isinstance(self.sync_category, Unset):
            sync_category = self.sync_category.value


        writable = self.writable

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        locked_fields: list[str] | Unset = UNSET
        if not isinstance(self.locked_fields, Unset):
            locked_fields = self.locked_fields



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
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if host_id is not UNSET:
            field_dict["hostId"] = host_id
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if active is not UNSET:
            field_dict["active"] = active
        if sync_enabled is not UNSET:
            field_dict["syncEnabled"] = sync_enabled
        if primary is not UNSET:
            field_dict["primary"] = primary
        if markup is not UNSET:
            field_dict["markup"] = markup
        if sync_category is not UNSET:
            field_dict["syncCategory"] = sync_category
        if writable is not UNSET:
            field_dict["writable"] = writable
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if locked_fields is not UNSET:
            field_dict["lockedFields"] = locked_fields
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

        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("accountId", UNSET))


        def _parse_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_name = _parse_account_name(d.pop("accountName", UNSET))


        def _parse_host_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_id = _parse_host_id(d.pop("hostId", UNSET))


        def _parse_host_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_name = _parse_host_name(d.pop("hostName", UNSET))


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


        _sync_category = d.pop("syncCategory", UNSET)
        sync_category: AirbnbConnectionSyncCategory | Unset
        if isinstance(_sync_category,  Unset):
            sync_category = UNSET
        else:
            sync_category = AirbnbConnectionSyncCategory(_sync_category)




        writable = d.pop("writable", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        locked_fields = cast(list[str], d.pop("lockedFields", UNSET))


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
            account_id=account_id,
            account_name=account_name,
            host_id=host_id,
            host_name=host_name,
            active=active,
            sync_enabled=sync_enabled,
            primary=primary,
            markup=markup,
            sync_category=sync_category,
            writable=writable,
            created_at=created_at,
            locked_fields=locked_fields,
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
