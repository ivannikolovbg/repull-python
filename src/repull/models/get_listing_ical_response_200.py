from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_listing_ical_response_200_calendar_name import GetListingIcalResponse200CalendarName
from typing import cast

if TYPE_CHECKING:
  from ..models.get_listing_ical_response_200_vrbo_item import GetListingIcalResponse200VrboItem





T = TypeVar("T", bound="GetListingIcalResponse200")



@_attrs_define
class GetListingIcalResponse200:
    """ 
        Attributes:
            listing_id (str):  Example: 1001.
            url (str): The feed address. Import it on any channel that reads iCal. Example:
                https://api.repull.dev/ical/4f9c2d7e1a8b3c6d5e0f9a2b7c4d1e8f3a6b9c2d5e8f1a4b7c0d3e6f9a2b5c8d.ics.
            calendar_name (GetListingIcalResponse200CalendarName): The calendar name the feed carries, and the name to give
                it when importing it by hand.
            enabled (bool): False when the listing's feed was turned off; the address then answers 404.
            vrbo (list[GetListingIcalResponse200VrboItem]): One entry per Vrbo unit mapped to the listing.
     """

    listing_id: str
    url: str
    calendar_name: GetListingIcalResponse200CalendarName
    enabled: bool
    vrbo: list[GetListingIcalResponse200VrboItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_listing_ical_response_200_vrbo_item import GetListingIcalResponse200VrboItem
        listing_id = self.listing_id

        url = self.url

        calendar_name = self.calendar_name.value

        enabled = self.enabled

        vrbo = []
        for vrbo_item_data in self.vrbo:
            vrbo_item = vrbo_item_data.to_dict()
            vrbo.append(vrbo_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "listingId": listing_id,
            "url": url,
            "calendarName": calendar_name,
            "enabled": enabled,
            "vrbo": vrbo,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_listing_ical_response_200_vrbo_item import GetListingIcalResponse200VrboItem
        d = dict(src_dict)
        listing_id = d.pop("listingId")

        url = d.pop("url")

        calendar_name = GetListingIcalResponse200CalendarName(d.pop("calendarName"))




        enabled = d.pop("enabled")

        vrbo = []
        _vrbo = d.pop("vrbo")
        for vrbo_item_data in (_vrbo):
            vrbo_item = GetListingIcalResponse200VrboItem.from_dict(vrbo_item_data)



            vrbo.append(vrbo_item)


        get_listing_ical_response_200 = cls(
            listing_id=listing_id,
            url=url,
            calendar_name=calendar_name,
            enabled=enabled,
            vrbo=vrbo,
        )


        get_listing_ical_response_200.additional_properties = d
        return get_listing_ical_response_200

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
