from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AirbnbPermitsWriteRequestPermitsItemAnswersItem")



@_attrs_define
class AirbnbPermitsWriteRequestPermitsItemAnswersItem:
    """ Exactly one value field applies, decided by the question's `answer_type`.

        Attributes:
            question_key (str):
            text_value (None | str | Unset):
            date_value (None | str | Unset): ISO date, YYYY-MM-DD.
            selected_options_value (list[str] | None | Unset):
     """

    question_key: str
    text_value: None | str | Unset = UNSET
    date_value: None | str | Unset = UNSET
    selected_options_value: list[str] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        question_key = self.question_key

        text_value: None | str | Unset
        if isinstance(self.text_value, Unset):
            text_value = UNSET
        else:
            text_value = self.text_value

        date_value: None | str | Unset
        if isinstance(self.date_value, Unset):
            date_value = UNSET
        else:
            date_value = self.date_value

        selected_options_value: list[str] | None | Unset
        if isinstance(self.selected_options_value, Unset):
            selected_options_value = UNSET
        elif isinstance(self.selected_options_value, list):
            selected_options_value = self.selected_options_value


        else:
            selected_options_value = self.selected_options_value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "question_key": question_key,
        })
        if text_value is not UNSET:
            field_dict["text_value"] = text_value
        if date_value is not UNSET:
            field_dict["date_value"] = date_value
        if selected_options_value is not UNSET:
            field_dict["selected_options_value"] = selected_options_value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        question_key = d.pop("question_key")

        def _parse_text_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text_value = _parse_text_value(d.pop("text_value", UNSET))


        def _parse_date_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        date_value = _parse_date_value(d.pop("date_value", UNSET))


        def _parse_selected_options_value(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                selected_options_value_type_0 = cast(list[str], data)

                return selected_options_value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        selected_options_value = _parse_selected_options_value(d.pop("selected_options_value", UNSET))


        airbnb_permits_write_request_permits_item_answers_item = cls(
            question_key=question_key,
            text_value=text_value,
            date_value=date_value,
            selected_options_value=selected_options_value,
        )

        return airbnb_permits_write_request_permits_item_answers_item

