from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AirbnbPermitsWriteRequestPermitsItemAnswersAdditionalProperty")



@_attrs_define
class AirbnbPermitsWriteRequestPermitsItemAnswersAdditionalProperty:
    """ 
        Attributes:
            text_value (str | Unset):
            attestation_value (bool | Unset):
            radio_value (str | Unset):
            date_value (str | Unset): ISO date, YYYY-MM-DD.
            selected_options_value (list[str] | Unset):
     """

    text_value: str | Unset = UNSET
    attestation_value: bool | Unset = UNSET
    radio_value: str | Unset = UNSET
    date_value: str | Unset = UNSET
    selected_options_value: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        text_value = self.text_value

        attestation_value = self.attestation_value

        radio_value = self.radio_value

        date_value = self.date_value

        selected_options_value: list[str] | Unset = UNSET
        if not isinstance(self.selected_options_value, Unset):
            selected_options_value = self.selected_options_value




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if text_value is not UNSET:
            field_dict["text_value"] = text_value
        if attestation_value is not UNSET:
            field_dict["attestation_value"] = attestation_value
        if radio_value is not UNSET:
            field_dict["radio_value"] = radio_value
        if date_value is not UNSET:
            field_dict["date_value"] = date_value
        if selected_options_value is not UNSET:
            field_dict["selected_options_value"] = selected_options_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text_value = d.pop("text_value", UNSET)

        attestation_value = d.pop("attestation_value", UNSET)

        radio_value = d.pop("radio_value", UNSET)

        date_value = d.pop("date_value", UNSET)

        selected_options_value = cast(list[str], d.pop("selected_options_value", UNSET))


        airbnb_permits_write_request_permits_item_answers_additional_property = cls(
            text_value=text_value,
            attestation_value=attestation_value,
            radio_value=radio_value,
            date_value=date_value,
            selected_options_value=selected_options_value,
        )

        return airbnb_permits_write_request_permits_item_answers_additional_property

