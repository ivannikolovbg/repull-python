from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_listing_ical_response_200_vrbo_item_status import GetListingIcalResponse200VrboItemStatus
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="GetListingIcalResponse200VrboItem")



@_attrs_define
class GetListingIcalResponse200VrboItem:
    """ 
        Attributes:
            unit_id (str): The Vrbo listing number (`unitId` on `GET /v1/connections/{id}/units`). Example: 7001234.
            calendar_sync (bool): Calendar sync is on for the unit.
            status (GetListingIcalResponse200VrboItemStatus): `imported`: Vrbo imports the feed. `pending`: calendar sync is
                on and Repull has not checked the unit yet — it adds the feed itself. `failed`: Vrbo did not take it; ask the
                host to add `url` in Vrbo → Calendar → Import calendar, named "Repull". `not_imported`: checked, not there, and
                not added (for example, the feed is turned off). `off`: calendar sync is off, so Repull leaves the unit's
                imported calendars alone.
            other_feeds (list[str]): Names of other calendars the unit still imports, as Vrbo shows them.
            checked_at (datetime.datetime | None): When Repull last read the unit's imported calendars.
     """

    unit_id: str
    calendar_sync: bool
    status: GetListingIcalResponse200VrboItemStatus
    other_feeds: list[str]
    checked_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        unit_id = self.unit_id

        calendar_sync = self.calendar_sync

        status = self.status.value

        other_feeds = self.other_feeds



        checked_at: None | str
        if isinstance(self.checked_at, datetime.datetime):
            checked_at = self.checked_at.isoformat()
        else:
            checked_at = self.checked_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "unitId": unit_id,
            "calendarSync": calendar_sync,
            "status": status,
            "otherFeeds": other_feeds,
            "checkedAt": checked_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        unit_id = d.pop("unitId")

        calendar_sync = d.pop("calendarSync")

        status = GetListingIcalResponse200VrboItemStatus(d.pop("status"))




        other_feeds = cast(list[str], d.pop("otherFeeds"))


        def _parse_checked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                checked_at_type_0 = isoparse(data)



                return checked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        checked_at = _parse_checked_at(d.pop("checkedAt"))


        get_listing_ical_response_200_vrbo_item = cls(
            unit_id=unit_id,
            calendar_sync=calendar_sync,
            status=status,
            other_feeds=other_feeds,
            checked_at=checked_at,
        )


        get_listing_ical_response_200_vrbo_item.additional_properties = d
        return get_listing_ical_response_200_vrbo_item

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
