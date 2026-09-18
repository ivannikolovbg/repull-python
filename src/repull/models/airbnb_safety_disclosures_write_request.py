from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_safety_disclosure import AirbnbSafetyDisclosure





T = TypeVar("T", bound="AirbnbSafetyDisclosuresWriteRequest")



@_attrs_define
class AirbnbSafetyDisclosuresWriteRequest:
    """ A MERGE, not a replacement: Airbnb keeps one value per disclosure type, a type you leave out keeps the value it has,
    and to retract a disclosure you send it with `value: false`. A full replacement would let a partial request silently
    un-declare a security camera — which is a guest-safety statement, not a preference.

        Attributes:
            disclosures (list[AirbnbSafetyDisclosure]):
     """

    disclosures: list[AirbnbSafetyDisclosure]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_safety_disclosure import AirbnbSafetyDisclosure
        disclosures = []
        for disclosures_item_data in self.disclosures:
            disclosures_item = disclosures_item_data.to_dict()
            disclosures.append(disclosures_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "disclosures": disclosures,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_safety_disclosure import AirbnbSafetyDisclosure
        d = dict(src_dict)
        disclosures = []
        _disclosures = d.pop("disclosures")
        for disclosures_item_data in (_disclosures):
            disclosures_item = AirbnbSafetyDisclosure.from_dict(disclosures_item_data)



            disclosures.append(disclosures_item)


        airbnb_safety_disclosures_write_request = cls(
            disclosures=disclosures,
        )


        airbnb_safety_disclosures_write_request.additional_properties = d
        return airbnb_safety_disclosures_write_request

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
