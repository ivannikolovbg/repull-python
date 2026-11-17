from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.vrbo_notifications_state import VrboNotificationsState
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="VrboNotifications")



@_attrs_define
class VrboNotifications:
    """ Whether Vrbo's notification emails for this account reach Repull. Each one brings a new guest message or booking in
    within about a minute; without them Repull relies on its scheduled check, which is slower.

        Attributes:
            state (VrboNotificationsState): `active`: notifications arrive for this account's guest messages. `missing`:
                Repull found new guest messages and no notification came for them — ask the host to add `address` on Vrbo (or
                turn its notifications back on). `unknown`: no guest messages yet to judge by.
            last_received_at (datetime.datetime | None): When the last Vrbo notification reached `address`. `null` when none
                ever has.
            address (None | str): The address the host adds on Vrbo as a secondary email, with message and reservation
                notifications on. Example: in+vrbo-1474-33@repull.dev.
     """

    state: VrboNotificationsState
    last_received_at: datetime.datetime | None
    address: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        last_received_at: None | str
        if isinstance(self.last_received_at, datetime.datetime):
            last_received_at = self.last_received_at.isoformat()
        else:
            last_received_at = self.last_received_at

        address: None | str
        address = self.address


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "state": state,
            "lastReceivedAt": last_received_at,
            "address": address,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = VrboNotificationsState(d.pop("state"))




        def _parse_last_received_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_received_at_type_0 = isoparse(data)



                return last_received_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_received_at = _parse_last_received_at(d.pop("lastReceivedAt"))


        def _parse_address(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        address = _parse_address(d.pop("address"))


        vrbo_notifications = cls(
            state=state,
            last_received_at=last_received_at,
            address=address,
        )


        vrbo_notifications.additional_properties = d
        return vrbo_notifications

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
