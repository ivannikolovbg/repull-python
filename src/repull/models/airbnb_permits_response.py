from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_permits_response_cached_item import AirbnbPermitsResponseCachedItem
  from ..models.airbnb_permits_response_permits_type_0_item import AirbnbPermitsResponsePermitsType0Item





T = TypeVar("T", bound="AirbnbPermitsResponse")



@_attrs_define
class AirbnbPermitsResponse:
    """ 
        Attributes:
            permits (list[AirbnbPermitsResponsePermitsType0Item] | None | Unset): The live permit flows from Airbnb —
                present only with `?source=live`, `null` otherwise. Each flow names its `regulatory_body`, `regulation_type`,
                `status`, its `flows[]` with the `answer_key` / `type` / `choices` of every question you have to answer, plus
                the answers already on file.
            cached (list[AirbnbPermitsResponseCachedItem] | Unset): Permits as last mirrored by the sync worker: body, type,
                status, number. The RESULT of a permit, not the questions.
     """

    permits: list[AirbnbPermitsResponsePermitsType0Item] | None | Unset = UNSET
    cached: list[AirbnbPermitsResponseCachedItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_permits_response_cached_item import AirbnbPermitsResponseCachedItem
        from ..models.airbnb_permits_response_permits_type_0_item import AirbnbPermitsResponsePermitsType0Item
        permits: list[dict[str, Any]] | None | Unset
        if isinstance(self.permits, Unset):
            permits = UNSET
        elif isinstance(self.permits, list):
            permits = []
            for permits_type_0_item_data in self.permits:
                permits_type_0_item = permits_type_0_item_data.to_dict()
                permits.append(permits_type_0_item)


        else:
            permits = self.permits

        cached: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cached, Unset):
            cached = []
            for cached_item_data in self.cached:
                cached_item = cached_item_data.to_dict()
                cached.append(cached_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if permits is not UNSET:
            field_dict["permits"] = permits
        if cached is not UNSET:
            field_dict["cached"] = cached

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_permits_response_cached_item import AirbnbPermitsResponseCachedItem
        from ..models.airbnb_permits_response_permits_type_0_item import AirbnbPermitsResponsePermitsType0Item
        d = dict(src_dict)
        def _parse_permits(data: object) -> list[AirbnbPermitsResponsePermitsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permits_type_0 = []
                _permits_type_0 = data
                for permits_type_0_item_data in (_permits_type_0):
                    permits_type_0_item = AirbnbPermitsResponsePermitsType0Item.from_dict(permits_type_0_item_data)



                    permits_type_0.append(permits_type_0_item)

                return permits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AirbnbPermitsResponsePermitsType0Item] | None | Unset, data)

        permits = _parse_permits(d.pop("permits", UNSET))


        _cached = d.pop("cached", UNSET)
        cached: list[AirbnbPermitsResponseCachedItem] | Unset = UNSET
        if _cached is not UNSET:
            cached = []
            for cached_item_data in _cached:
                cached_item = AirbnbPermitsResponseCachedItem.from_dict(cached_item_data)



                cached.append(cached_item)


        airbnb_permits_response = cls(
            permits=permits,
            cached=cached,
        )


        airbnb_permits_response.additional_properties = d
        return airbnb_permits_response

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
