from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.hospitable_webhook_status import HospitableWebhookStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="HospitableWebhook")



@_attrs_define
class HospitableWebhook:
    """ Hospitable only. Hospitable has no API to subscribe webhooks, so the host adds one in Hospitable: **Apps → Webhooks
    → + Add new**, pastes `url`, ticks Reservations, Messages, Properties and Reviews, and saves (Hospitable's **Test**
    button sends a sample right away). Each connection has its own `url`; a reconnect keeps it. Every delivery is
    checked against Hospitable's signature before it is used.

    **Polling.** While `status` is `receiving` the connection is updated from the webhooks alone and is not polled. When
    it is `not_configured` or `stale` it is polled every minute, and the first poll after going stale re-reads the whole
    silent window, so nothing is lost. A quiet account (no bookings or messages for a day) can read `stale` while its
    webhook still works; the next delivery flips it back to `receiving`.

        Attributes:
            url (str): The webhook URL to paste into Hospitable. Unique to this connection. Example:
                https://api.repull.dev/webhooks/pms/hospitable?token=4f9c2a7e1b3d5f60a8c9e2b4d6f8a0c1.
            status (HospitableWebhookStatus): `not_configured`: no delivery yet (the host has not added the URL).
                `receiving`: a delivery arrived in the last 24 hours. `stale`: deliveries arrived before, none in the last 24
                hours. Example: receiving.
            last_received_at (datetime.datetime | None): When the last verified delivery arrived; `null` before the first.
            events (list[str] | Unset): The webhook types to tick in Hospitable. Example: ['Reservations', 'Messages',
                'Properties', 'Reviews'].
     """

    url: str
    status: HospitableWebhookStatus
    last_received_at: datetime.datetime | None
    events: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        status = self.status.value

        last_received_at: None | str
        if isinstance(self.last_received_at, datetime.datetime):
            last_received_at = self.last_received_at.isoformat()
        else:
            last_received_at = self.last_received_at

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "url": url,
            "status": status,
            "lastReceivedAt": last_received_at,
        })
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        status = HospitableWebhookStatus(d.pop("status"))




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


        events = cast(list[str], d.pop("events", UNSET))


        hospitable_webhook = cls(
            url=url,
            status=status,
            last_received_at=last_received_at,
            events=events,
        )


        hospitable_webhook.additional_properties = d
        return hospitable_webhook

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
