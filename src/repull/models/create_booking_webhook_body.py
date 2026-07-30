from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="CreateBookingWebhookBody")



@_attrs_define
class CreateBookingWebhookBody:
    """ 
        Attributes:
            notification_type (str): Booking.com CNS notification type.
            callback_url (str): HTTPS endpoint Booking.com pushes notifications to.
     """

    notification_type: str
    callback_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        notification_type = self.notification_type

        callback_url = self.callback_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "notification_type": notification_type,
            "callback_url": callback_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        notification_type = d.pop("notification_type")

        callback_url = d.pop("callback_url")

        create_booking_webhook_body = cls(
            notification_type=notification_type,
            callback_url=callback_url,
        )


        create_booking_webhook_body.additional_properties = d
        return create_booking_webhook_body

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
