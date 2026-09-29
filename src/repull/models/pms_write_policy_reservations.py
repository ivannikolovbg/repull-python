from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PmsWritePolicyReservations")



@_attrs_define
class PmsWritePolicyReservations:
    """ 
        Attributes:
            website (bool): Create bookings from booking websites.
            dashboard (bool): Change and cancel bookings from the dashboard.
            api (bool): Create, change and cancel bookings through the reservations API.
     """

    website: bool
    dashboard: bool
    api: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        website = self.website

        dashboard = self.dashboard

        api = self.api


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "website": website,
            "dashboard": dashboard,
            "api": api,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        website = d.pop("website")

        dashboard = d.pop("dashboard")

        api = d.pop("api")

        pms_write_policy_reservations = cls(
            website=website,
            dashboard=dashboard,
            api=api,
        )


        pms_write_policy_reservations.additional_properties = d
        return pms_write_policy_reservations

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
