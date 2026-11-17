from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.vrbo_calendar_access_managed_by import VrboCalendarAccessManagedBy
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="VrboCalendarAccess")



@_attrs_define
class VrboCalendarAccess:
    """ Whether another tool manages a Vrbo account's calendar. Vrbo reports it per account; Repull asks when the account
    connects and once a day. While `managedBy` is set, Vrbo refuses price and availability changes from anyone else, so
    calendar sync is off for every unit of the account and turning it on returns `409 calendar_managed_elsewhere`.
    Bookings and messages keep working.

        Attributes:
            managed_by (VrboCalendarAccessManagedBy): `integrated_software`: Vrbo says connected software (such as a PMS)
                manages the calendar. `null`: Repull may manage it.
            detected_at (datetime.datetime | None): When `managedBy` was first seen. `null` when not managed.
            checked_at (datetime.datetime | None): When Vrbo was last asked. `null` until the first check.
            docs_url (str):  Example: https://repull.dev/docs/channels/vrbo/calendar-managed-elsewhere.
     """

    managed_by: VrboCalendarAccessManagedBy
    detected_at: datetime.datetime | None
    checked_at: datetime.datetime | None
    docs_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        managed_by = self.managed_by.value

        detected_at: None | str
        if isinstance(self.detected_at, datetime.datetime):
            detected_at = self.detected_at.isoformat()
        else:
            detected_at = self.detected_at

        checked_at: None | str
        if isinstance(self.checked_at, datetime.datetime):
            checked_at = self.checked_at.isoformat()
        else:
            checked_at = self.checked_at

        docs_url = self.docs_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "managedBy": managed_by,
            "detectedAt": detected_at,
            "checkedAt": checked_at,
            "docsUrl": docs_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        managed_by = VrboCalendarAccessManagedBy(d.pop("managedBy"))




        def _parse_detected_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                detected_at_type_0 = isoparse(data)



                return detected_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        detected_at = _parse_detected_at(d.pop("detectedAt"))


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


        docs_url = d.pop("docsUrl")

        vrbo_calendar_access = cls(
            managed_by=managed_by,
            detected_at=detected_at,
            checked_at=checked_at,
            docs_url=docs_url,
        )


        vrbo_calendar_access.additional_properties = d
        return vrbo_calendar_access

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
