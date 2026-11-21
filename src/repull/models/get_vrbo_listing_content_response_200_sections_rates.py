from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_content_response_200_sections_rates_days_item import GetVrboListingContentResponse200SectionsRatesDaysItem





T = TypeVar("T", bound="GetVrboListingContentResponse200SectionsRates")



@_attrs_define
class GetVrboListingContentResponse200SectionsRates:
    """ 
        Attributes:
            start (str | Unset):
            end (str | Unset):
            currency (None | str | Unset):
            days (list[GetVrboListingContentResponse200SectionsRatesDaysItem] | Unset):
     """

    start: str | Unset = UNSET
    end: str | Unset = UNSET
    currency: None | str | Unset = UNSET
    days: list[GetVrboListingContentResponse200SectionsRatesDaysItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_content_response_200_sections_rates_days_item import GetVrboListingContentResponse200SectionsRatesDaysItem
        start = self.start

        end = self.end

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        days: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.days, Unset):
            days = []
            for days_item_data in self.days:
                days_item = days_item_data.to_dict()
                days.append(days_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if currency is not UNSET:
            field_dict["currency"] = currency
        if days is not UNSET:
            field_dict["days"] = days

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_content_response_200_sections_rates_days_item import GetVrboListingContentResponse200SectionsRatesDaysItem
        d = dict(src_dict)
        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        _days = d.pop("days", UNSET)
        days: list[GetVrboListingContentResponse200SectionsRatesDaysItem] | Unset = UNSET
        if _days is not UNSET:
            days = []
            for days_item_data in _days:
                days_item = GetVrboListingContentResponse200SectionsRatesDaysItem.from_dict(days_item_data)



                days.append(days_item)


        get_vrbo_listing_content_response_200_sections_rates = cls(
            start=start,
            end=end,
            currency=currency,
            days=days,
        )


        get_vrbo_listing_content_response_200_sections_rates.additional_properties = d
        return get_vrbo_listing_content_response_200_sections_rates

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
