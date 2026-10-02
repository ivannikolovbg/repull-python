from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.reservation_pms_outcome_quote import ReservationPmsOutcomeQuote
  from ..models.reservation_pms_section_error import ReservationPmsSectionError





T = TypeVar("T", bound="ReservationPmsOutcome")



@_attrs_define
class ReservationPmsOutcome:
    """ Present when the write was made in a PMS: what the PMS applied. `partial: true` means the booking exists in the PMS
    but the steps in `failedSections` (e.g. notes, a tentative state) did not apply — do not create it again.

        Attributes:
            provider (str | Unset):  Example: hostaway.
            reservation_id (None | str | Unset): The PMS's own id for the booking. Example: 4471923.
            applied (list[str] | Unset):  Example: ['reservation'].
            errors (list[ReservationPmsSectionError] | Unset):
            partial (bool | Unset):
            failed_sections (list[ReservationPmsSectionError] | Unset):
            quote (ReservationPmsOutcomeQuote | Unset): Create only: the PMS quote the booking was priced from, when no
                `totalPrice` was sent.
     """

    provider: str | Unset = UNSET
    reservation_id: None | str | Unset = UNSET
    applied: list[str] | Unset = UNSET
    errors: list[ReservationPmsSectionError] | Unset = UNSET
    partial: bool | Unset = UNSET
    failed_sections: list[ReservationPmsSectionError] | Unset = UNSET
    quote: ReservationPmsOutcomeQuote | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_pms_outcome_quote import ReservationPmsOutcomeQuote
        from ..models.reservation_pms_section_error import ReservationPmsSectionError
        provider = self.provider

        reservation_id: None | str | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
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



        partial = self.partial

        failed_sections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failed_sections, Unset):
            failed_sections = []
            for failed_sections_item_data in self.failed_sections:
                failed_sections_item = failed_sections_item_data.to_dict()
                failed_sections.append(failed_sections_item)



        quote: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quote, Unset):
            quote = self.quote.to_dict()


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
        if partial is not UNSET:
            field_dict["partial"] = partial
        if failed_sections is not UNSET:
            field_dict["failedSections"] = failed_sections
        if quote is not UNSET:
            field_dict["quote"] = quote

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_pms_outcome_quote import ReservationPmsOutcomeQuote
        from ..models.reservation_pms_section_error import ReservationPmsSectionError
        d = dict(src_dict)
        provider = d.pop("provider", UNSET)

        def _parse_reservation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        applied = cast(list[str], d.pop("applied", UNSET))


        _errors = d.pop("errors", UNSET)
        errors: list[ReservationPmsSectionError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ReservationPmsSectionError.from_dict(errors_item_data)



                errors.append(errors_item)


        partial = d.pop("partial", UNSET)

        _failed_sections = d.pop("failedSections", UNSET)
        failed_sections: list[ReservationPmsSectionError] | Unset = UNSET
        if _failed_sections is not UNSET:
            failed_sections = []
            for failed_sections_item_data in _failed_sections:
                failed_sections_item = ReservationPmsSectionError.from_dict(failed_sections_item_data)



                failed_sections.append(failed_sections_item)


        _quote = d.pop("quote", UNSET)
        quote: ReservationPmsOutcomeQuote | Unset
        if isinstance(_quote,  Unset):
            quote = UNSET
        else:
            quote = ReservationPmsOutcomeQuote.from_dict(_quote)




        reservation_pms_outcome = cls(
            provider=provider,
            reservation_id=reservation_id,
            applied=applied,
            errors=errors,
            partial=partial,
            failed_sections=failed_sections,
            quote=quote,
        )


        reservation_pms_outcome.additional_properties = d
        return reservation_pms_outcome

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
