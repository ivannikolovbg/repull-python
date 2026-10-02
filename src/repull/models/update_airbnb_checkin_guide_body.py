from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_airbnb_checkin_guide_body_steps_item import UpdateAirbnbCheckinGuideBodyStepsItem





T = TypeVar("T", bound="UpdateAirbnbCheckinGuideBody")



@_attrs_define
class UpdateAirbnbCheckinGuideBody:
    """ 
        Attributes:
            steps (list[UpdateAirbnbCheckinGuideBodyStepsItem]): The guide's steps, in the order guests see them.
            locale (str | Unset): Language of the guide when one has to be created. Ignored when the listing already has a
                guide. Example: en.
     """

    steps: list[UpdateAirbnbCheckinGuideBodyStepsItem]
    locale: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_airbnb_checkin_guide_body_steps_item import UpdateAirbnbCheckinGuideBodyStepsItem
        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)



        locale = self.locale


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "steps": steps,
        })
        if locale is not UNSET:
            field_dict["locale"] = locale

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_airbnb_checkin_guide_body_steps_item import UpdateAirbnbCheckinGuideBodyStepsItem
        d = dict(src_dict)
        steps = []
        _steps = d.pop("steps")
        for steps_item_data in (_steps):
            steps_item = UpdateAirbnbCheckinGuideBodyStepsItem.from_dict(steps_item_data)



            steps.append(steps_item)


        locale = d.pop("locale", UNSET)

        update_airbnb_checkin_guide_body = cls(
            steps=steps,
            locale=locale,
        )

        return update_airbnb_checkin_guide_body

