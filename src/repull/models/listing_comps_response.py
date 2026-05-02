from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_comp import ListingComp
  from ..models.listing_comps_response_date_range import ListingCompsResponseDateRange





T = TypeVar("T", bound="ListingCompsResponse")



@_attrs_define
class ListingCompsResponse:
    """ Returned by `GET /v1/listings/{id}/comps`. Comps without coordinates are excluded — there's no way to rank them by
    distance. May include a `warning` field when the source listing itself has no coordinates.

        Attributes:
            listing_id (int | Unset):
            date_range (ListingCompsResponseDateRange | Unset):
            radius_km (float | Unset):
            total (int | Unset):
            data (list[ListingComp] | Unset):
            warning (None | str | Unset): Present (and `data` empty) when the source listing has no coordinates.
     """

    listing_id: int | Unset = UNSET
    date_range: ListingCompsResponseDateRange | Unset = UNSET
    radius_km: float | Unset = UNSET
    total: int | Unset = UNSET
    data: list[ListingComp] | Unset = UNSET
    warning: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_comp import ListingComp
        from ..models.listing_comps_response_date_range import ListingCompsResponseDateRange
        listing_id = self.listing_id

        date_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.date_range, Unset):
            date_range = self.date_range.to_dict()

        radius_km = self.radius_km

        total = self.total

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)



        warning: None | str | Unset
        if isinstance(self.warning, Unset):
            warning = UNSET
        else:
            warning = self.warning


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if date_range is not UNSET:
            field_dict["dateRange"] = date_range
        if radius_km is not UNSET:
            field_dict["radiusKm"] = radius_km
        if total is not UNSET:
            field_dict["total"] = total
        if data is not UNSET:
            field_dict["data"] = data
        if warning is not UNSET:
            field_dict["warning"] = warning

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_comp import ListingComp
        from ..models.listing_comps_response_date_range import ListingCompsResponseDateRange
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        _date_range = d.pop("dateRange", UNSET)
        date_range: ListingCompsResponseDateRange | Unset
        if isinstance(_date_range,  Unset):
            date_range = UNSET
        else:
            date_range = ListingCompsResponseDateRange.from_dict(_date_range)




        radius_km = d.pop("radiusKm", UNSET)

        total = d.pop("total", UNSET)

        _data = d.pop("data", UNSET)
        data: list[ListingComp] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = ListingComp.from_dict(data_item_data)



                data.append(data_item)


        def _parse_warning(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        warning = _parse_warning(d.pop("warning", UNSET))


        listing_comps_response = cls(
            listing_id=listing_id,
            date_range=date_range,
            radius_km=radius_km,
            total=total,
            data=data,
            warning=warning,
        )


        listing_comps_response.additional_properties = d
        return listing_comps_response

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
