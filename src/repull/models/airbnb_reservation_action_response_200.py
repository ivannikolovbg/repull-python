from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AirbnbReservationActionResponse200")



@_attrs_define
class AirbnbReservationActionResponse200:
    """ Airbnb's reservation object. Re-read `GET /v1/channels/airbnb/reservations/{code}` for the mirrored row once
    Airbnb's notification lands.

        Attributes:
            confirmation_code (str | Unset):
            status_type (str | Unset):
     """

    confirmation_code: str | Unset = UNSET
    status_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        confirmation_code = self.confirmation_code

        status_type = self.status_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if status_type is not UNSET:
            field_dict["statusType"] = status_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confirmation_code = d.pop("confirmationCode", UNSET)

        status_type = d.pop("statusType", UNSET)

        airbnb_reservation_action_response_200 = cls(
            confirmation_code=confirmation_code,
            status_type=status_type,
        )


        airbnb_reservation_action_response_200.additional_properties = d
        return airbnb_reservation_action_response_200

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
