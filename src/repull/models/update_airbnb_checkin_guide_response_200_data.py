from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_airbnb_checkin_guide_response_200_data_steps_item import UpdateAirbnbCheckinGuideResponse200DataStepsItem





T = TypeVar("T", bound="UpdateAirbnbCheckinGuideResponse200Data")



@_attrs_define
class UpdateAirbnbCheckinGuideResponse200Data:
    """ 
        Attributes:
            listing_id (int | Unset):
            locale (str | Unset):
            published (bool | None | Unset):
            steps (list[UpdateAirbnbCheckinGuideResponse200DataStepsItem] | Unset):
     """

    listing_id: int | Unset = UNSET
    locale: str | Unset = UNSET
    published: bool | None | Unset = UNSET
    steps: list[UpdateAirbnbCheckinGuideResponse200DataStepsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_airbnb_checkin_guide_response_200_data_steps_item import UpdateAirbnbCheckinGuideResponse200DataStepsItem
        listing_id = self.listing_id

        locale = self.locale

        published: bool | None | Unset
        if isinstance(self.published, Unset):
            published = UNSET
        else:
            published = self.published

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if locale is not UNSET:
            field_dict["locale"] = locale
        if published is not UNSET:
            field_dict["published"] = published
        if steps is not UNSET:
            field_dict["steps"] = steps

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_airbnb_checkin_guide_response_200_data_steps_item import UpdateAirbnbCheckinGuideResponse200DataStepsItem
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        locale = d.pop("locale", UNSET)

        def _parse_published(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        published = _parse_published(d.pop("published", UNSET))


        _steps = d.pop("steps", UNSET)
        steps: list[UpdateAirbnbCheckinGuideResponse200DataStepsItem] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = UpdateAirbnbCheckinGuideResponse200DataStepsItem.from_dict(steps_item_data)



                steps.append(steps_item)


        update_airbnb_checkin_guide_response_200_data = cls(
            listing_id=listing_id,
            locale=locale,
            published=published,
            steps=steps,
        )


        update_airbnb_checkin_guide_response_200_data.additional_properties = d
        return update_airbnb_checkin_guide_response_200_data

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
