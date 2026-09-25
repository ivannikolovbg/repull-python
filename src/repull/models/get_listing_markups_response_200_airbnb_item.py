from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetListingMarkupsResponse200AirbnbItem")



@_attrs_define
class GetListingMarkupsResponse200AirbnbItem:
    """ 
        Attributes:
            airbnb_id (str | Unset): Airbnb listing id.
            markup_percent (float | None | Unset): Percent added to the listing's price on Airbnb. 35 = +35%. `null` = none.
                Example: 35.
     """

    airbnb_id: str | Unset = UNSET
    markup_percent: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        airbnb_id = self.airbnb_id

        markup_percent: float | None | Unset
        if isinstance(self.markup_percent, Unset):
            markup_percent = UNSET
        else:
            markup_percent = self.markup_percent


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if airbnb_id is not UNSET:
            field_dict["airbnbId"] = airbnb_id
        if markup_percent is not UNSET:
            field_dict["markupPercent"] = markup_percent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        airbnb_id = d.pop("airbnbId", UNSET)

        def _parse_markup_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        markup_percent = _parse_markup_percent(d.pop("markupPercent", UNSET))


        get_listing_markups_response_200_airbnb_item = cls(
            airbnb_id=airbnb_id,
            markup_percent=markup_percent,
        )


        get_listing_markups_response_200_airbnb_item.additional_properties = d
        return get_listing_markups_response_200_airbnb_item

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
