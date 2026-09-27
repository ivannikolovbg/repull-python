from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cancel_reservation_response_200_pms_errors_item import CancelReservationResponse200PmsErrorsItem





T = TypeVar("T", bound="CancelReservationResponse200Pms")



@_attrs_define
class CancelReservationResponse200Pms:
    """ Present when the cancellation was made in a PMS.

        Attributes:
            provider (str | Unset):  Example: mews.
            applied (list[str] | Unset):
            errors (list[CancelReservationResponse200PmsErrorsItem] | Unset):
     """

    provider: str | Unset = UNSET
    applied: list[str] | Unset = UNSET
    errors: list[CancelReservationResponse200PmsErrorsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cancel_reservation_response_200_pms_errors_item import CancelReservationResponse200PmsErrorsItem
        provider = self.provider

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
        if applied is not UNSET:
            field_dict["applied"] = applied
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cancel_reservation_response_200_pms_errors_item import CancelReservationResponse200PmsErrorsItem
        d = dict(src_dict)
        provider = d.pop("provider", UNSET)

        applied = cast(list[str], d.pop("applied", UNSET))


        _errors = d.pop("errors", UNSET)
        errors: list[CancelReservationResponse200PmsErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = CancelReservationResponse200PmsErrorsItem.from_dict(errors_item_data)



                errors.append(errors_item)


        cancel_reservation_response_200_pms = cls(
            provider=provider,
            applied=applied,
            errors=errors,
        )


        cancel_reservation_response_200_pms.additional_properties = d
        return cancel_reservation_response_200_pms

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
