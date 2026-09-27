from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.reservation_create_response_pms_errors_item import ReservationCreateResponsePmsErrorsItem





T = TypeVar("T", bound="ReservationCreateResponsePms")



@_attrs_define
class ReservationCreateResponsePms:
    """ Mews or Cloudbeds listings only: the booking was made in the PMS first, and this is what it applied.

        Attributes:
            provider (str | Unset):  Example: mews.
            reservation_id (str | Unset): The PMS's own id for the booking.
            applied (list[str] | Unset):
            errors (list[ReservationCreateResponsePmsErrorsItem] | Unset):
     """

    provider: str | Unset = UNSET
    reservation_id: str | Unset = UNSET
    applied: list[str] | Unset = UNSET
    errors: list[ReservationCreateResponsePmsErrorsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_create_response_pms_errors_item import ReservationCreateResponsePmsErrorsItem
        provider = self.provider

        reservation_id = self.reservation_id

        applied: list[str] | Unset = UNSET
        if not isinstance(self.applied, Unset):
            applied = self.applied



        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if provider is not UNSET:
            field_dict["provider"] = provider
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if applied is not UNSET:
            field_dict["applied"] = applied
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_create_response_pms_errors_item import ReservationCreateResponsePmsErrorsItem
        d = dict(src_dict)
        provider = d.pop("provider", UNSET)

        reservation_id = d.pop("reservationId", UNSET)

        applied = cast(list[str], d.pop("applied", UNSET))


        _errors = d.pop("errors", UNSET)
        errors: list[ReservationCreateResponsePmsErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ReservationCreateResponsePmsErrorsItem.from_dict(errors_item_data)



                errors.append(errors_item)


        reservation_create_response_pms = cls(
            provider=provider,
            reservation_id=reservation_id,
            applied=applied,
            errors=errors,
        )


        reservation_create_response_pms.additional_properties = d
        return reservation_create_response_pms

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
