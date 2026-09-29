from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_connection_units_response_200_status import ListConnectionUnitsResponse200Status
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.list_connection_units_response_200_listing_options_item import ListConnectionUnitsResponse200ListingOptionsItem
  from ..models.list_connection_units_response_200_units_item import ListConnectionUnitsResponse200UnitsItem





T = TypeVar("T", bound="ListConnectionUnitsResponse200")



@_attrs_define
class ListConnectionUnitsResponse200:
    """ 
        Attributes:
            connection_id (str | Unset):
            channel (str | Unset):
            status (ListConnectionUnitsResponse200Status | Unset):
            units (list[ListConnectionUnitsResponse200UnitsItem] | Unset):
            listing_options (list[ListConnectionUnitsResponse200ListingOptionsItem] | Unset):
            missing_capabilities (list[str] | Unset):
            listing_options_total (int | Unset): How many listings the workspace has to map to.
     """

    connection_id: str | Unset = UNSET
    channel: str | Unset = UNSET
    status: ListConnectionUnitsResponse200Status | Unset = UNSET
    units: list[ListConnectionUnitsResponse200UnitsItem] | Unset = UNSET
    listing_options: list[ListConnectionUnitsResponse200ListingOptionsItem] | Unset = UNSET
    missing_capabilities: list[str] | Unset = UNSET
    listing_options_total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.list_connection_units_response_200_listing_options_item import ListConnectionUnitsResponse200ListingOptionsItem
        from ..models.list_connection_units_response_200_units_item import ListConnectionUnitsResponse200UnitsItem
        connection_id = self.connection_id

        channel = self.channel

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        units: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.units, Unset):
            units = []
            for units_item_data in self.units:
                units_item = units_item_data.to_dict()
                units.append(units_item)



        listing_options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.listing_options, Unset):
            listing_options = []
            for listing_options_item_data in self.listing_options:
                listing_options_item = listing_options_item_data.to_dict()
                listing_options.append(listing_options_item)



        missing_capabilities: list[str] | Unset = UNSET
        if not isinstance(self.missing_capabilities, Unset):
            missing_capabilities = self.missing_capabilities



        listing_options_total = self.listing_options_total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if status is not UNSET:
            field_dict["status"] = status
        if units is not UNSET:
            field_dict["units"] = units
        if listing_options is not UNSET:
            field_dict["listing_options"] = listing_options
        if missing_capabilities is not UNSET:
            field_dict["missing_capabilities"] = missing_capabilities
        if listing_options_total is not UNSET:
            field_dict["listing_options_total"] = listing_options_total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_connection_units_response_200_listing_options_item import ListConnectionUnitsResponse200ListingOptionsItem
        from ..models.list_connection_units_response_200_units_item import ListConnectionUnitsResponse200UnitsItem
        d = dict(src_dict)
        connection_id = d.pop("connection_id", UNSET)

        channel = d.pop("channel", UNSET)

        _status = d.pop("status", UNSET)
        status: ListConnectionUnitsResponse200Status | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ListConnectionUnitsResponse200Status(_status)




        _units = d.pop("units", UNSET)
        units: list[ListConnectionUnitsResponse200UnitsItem] | Unset = UNSET
        if _units is not UNSET:
            units = []
            for units_item_data in _units:
                units_item = ListConnectionUnitsResponse200UnitsItem.from_dict(units_item_data)



                units.append(units_item)


        _listing_options = d.pop("listing_options", UNSET)
        listing_options: list[ListConnectionUnitsResponse200ListingOptionsItem] | Unset = UNSET
        if _listing_options is not UNSET:
            listing_options = []
            for listing_options_item_data in _listing_options:
                listing_options_item = ListConnectionUnitsResponse200ListingOptionsItem.from_dict(listing_options_item_data)



                listing_options.append(listing_options_item)


        missing_capabilities = cast(list[str], d.pop("missing_capabilities", UNSET))


        listing_options_total = d.pop("listing_options_total", UNSET)

        list_connection_units_response_200 = cls(
            connection_id=connection_id,
            channel=channel,
            status=status,
            units=units,
            listing_options=listing_options,
            missing_capabilities=missing_capabilities,
            listing_options_total=listing_options_total,
        )


        list_connection_units_response_200.additional_properties = d
        return list_connection_units_response_200

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
