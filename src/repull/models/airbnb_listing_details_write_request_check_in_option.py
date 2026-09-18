from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_listing_details_write_request_check_in_option_category import AirbnbListingDetailsWriteRequestCheckInOptionCategory
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AirbnbListingDetailsWriteRequestCheckInOption")



@_attrs_define
class AirbnbListingDetailsWriteRequestCheckInOption:
    """ How the guest lets themselves in — Airbnb's `check_in_option`.

        Attributes:
            category (AirbnbListingDetailsWriteRequestCheckInOptionCategory):
            instruction (None | str | Unset):
     """

    category: AirbnbListingDetailsWriteRequestCheckInOptionCategory
    instruction: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        category = self.category.value

        instruction: None | str | Unset
        if isinstance(self.instruction, Unset):
            instruction = UNSET
        else:
            instruction = self.instruction


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "category": category,
        })
        if instruction is not UNSET:
            field_dict["instruction"] = instruction

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = AirbnbListingDetailsWriteRequestCheckInOptionCategory(d.pop("category"))




        def _parse_instruction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instruction = _parse_instruction(d.pop("instruction", UNSET))


        airbnb_listing_details_write_request_check_in_option = cls(
            category=category,
            instruction=instruction,
        )

        return airbnb_listing_details_write_request_check_in_option

