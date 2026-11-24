from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tiket_map_listings_response_results_item import TiketMapListingsResponseResultsItem





T = TypeVar("T", bound="TiketMapListingsResponse")



@_attrs_define
class TiketMapListingsResponse:
    """ 
        Attributes:
            property_id (str | Unset):
            results (list[TiketMapListingsResponseResultsItem] | Unset): One entry per mapping.
            replayed_reservations (int | Unset): Bookings tiket.com delivered while the room was unmapped, now recorded on
                the listing.
     """

    property_id: str | Unset = UNSET
    results: list[TiketMapListingsResponseResultsItem] | Unset = UNSET
    replayed_reservations: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tiket_map_listings_response_results_item import TiketMapListingsResponseResultsItem
        property_id = self.property_id

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)



        replayed_reservations = self.replayed_reservations


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if results is not UNSET:
            field_dict["results"] = results
        if replayed_reservations is not UNSET:
            field_dict["replayedReservations"] = replayed_reservations

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiket_map_listings_response_results_item import TiketMapListingsResponseResultsItem
        d = dict(src_dict)
        property_id = d.pop("propertyId", UNSET)

        _results = d.pop("results", UNSET)
        results: list[TiketMapListingsResponseResultsItem] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = TiketMapListingsResponseResultsItem.from_dict(results_item_data)



                results.append(results_item)


        replayed_reservations = d.pop("replayedReservations", UNSET)

        tiket_map_listings_response = cls(
            property_id=property_id,
            results=results,
            replayed_reservations=replayed_reservations,
        )


        tiket_map_listings_response.additional_properties = d
        return tiket_map_listings_response

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
