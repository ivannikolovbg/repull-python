from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_permits_write_request_permits_item import AirbnbPermitsWriteRequestPermitsItem





T = TypeVar("T", bound="AirbnbPermitsWriteRequest")



@_attrs_define
class AirbnbPermitsWriteRequest:
    """ Answer the regulatory permit questions Airbnb asks for this listing, in Airbnb's Listing Permits shape. Read them
    first with `?source=live` on the GET: each permit lists its `flows[]`, and each flow its `questions[]` with an
    `answer_key` and a `type`.

        Example:
            {'permits': [{'regulatory_body': 'maui_county_hawaii', 'regulation_type': 'registration', 'regulation_context':
                'initial', 'flow_slug': 'existing_registration', 'answers': {'attestation': {'attestation_value': True},
                'permit_number': {'text_value': 'TMK-2-3-004-005'}}}]}

        Attributes:
            permits (list[AirbnbPermitsWriteRequestPermitsItem]):
     """

    permits: list[AirbnbPermitsWriteRequestPermitsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_permits_write_request_permits_item import AirbnbPermitsWriteRequestPermitsItem
        permits = []
        for permits_item_data in self.permits:
            permits_item = permits_item_data.to_dict()
            permits.append(permits_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "permits": permits,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_permits_write_request_permits_item import AirbnbPermitsWriteRequestPermitsItem
        d = dict(src_dict)
        permits = []
        _permits = d.pop("permits")
        for permits_item_data in (_permits):
            permits_item = AirbnbPermitsWriteRequestPermitsItem.from_dict(permits_item_data)



            permits.append(permits_item)


        airbnb_permits_write_request = cls(
            permits=permits,
        )


        airbnb_permits_write_request.additional_properties = d
        return airbnb_permits_write_request

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
