from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_connect_write_policy_body_calendar import UpdateConnectWritePolicyBodyCalendar
  from ..models.update_connect_write_policy_body_reservations import UpdateConnectWritePolicyBodyReservations





T = TypeVar("T", bound="UpdateConnectWritePolicyBody")



@_attrs_define
class UpdateConnectWritePolicyBody:
    """ Only the switches you send change. Every value must be a boolean.

        Example:
            {'calendar': {'availability': False, 'rates': True}}

        Attributes:
            calendar (UpdateConnectWritePolicyBodyCalendar | Unset):
            reservations (UpdateConnectWritePolicyBodyReservations | Unset):
     """

    calendar: UpdateConnectWritePolicyBodyCalendar | Unset = UNSET
    reservations: UpdateConnectWritePolicyBodyReservations | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_connect_write_policy_body_calendar import UpdateConnectWritePolicyBodyCalendar
        from ..models.update_connect_write_policy_body_reservations import UpdateConnectWritePolicyBodyReservations
        calendar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.calendar, Unset):
            calendar = self.calendar.to_dict()

        reservations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reservations, Unset):
            reservations = self.reservations.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if calendar is not UNSET:
            field_dict["calendar"] = calendar
        if reservations is not UNSET:
            field_dict["reservations"] = reservations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_connect_write_policy_body_calendar import UpdateConnectWritePolicyBodyCalendar
        from ..models.update_connect_write_policy_body_reservations import UpdateConnectWritePolicyBodyReservations
        d = dict(src_dict)
        _calendar = d.pop("calendar", UNSET)
        calendar: UpdateConnectWritePolicyBodyCalendar | Unset
        if isinstance(_calendar,  Unset):
            calendar = UNSET
        else:
            calendar = UpdateConnectWritePolicyBodyCalendar.from_dict(_calendar)




        _reservations = d.pop("reservations", UNSET)
        reservations: UpdateConnectWritePolicyBodyReservations | Unset
        if isinstance(_reservations,  Unset):
            reservations = UNSET
        else:
            reservations = UpdateConnectWritePolicyBodyReservations.from_dict(_reservations)




        update_connect_write_policy_body = cls(
            calendar=calendar,
            reservations=reservations,
        )


        update_connect_write_policy_body.additional_properties = d
        return update_connect_write_policy_body

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
