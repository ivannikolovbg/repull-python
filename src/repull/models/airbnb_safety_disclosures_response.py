from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_safety_disclosure import AirbnbSafetyDisclosure





T = TypeVar("T", bound="AirbnbSafetyDisclosuresResponse")



@_attrs_define
class AirbnbSafetyDisclosuresResponse:
    """ 
        Attributes:
            disclosures (list[AirbnbSafetyDisclosure] | Unset): Every supported disclosure type, including the ones this
                listing has not declared (`value: false`), so "does this property have cameras?" has an answer rather than a
                missing key. Types Airbnb returns that are not in the documented set are passed through, never dropped.
            declared (list[str] | Unset): Just the types that are true of this property.
     """

    disclosures: list[AirbnbSafetyDisclosure] | Unset = UNSET
    declared: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_safety_disclosure import AirbnbSafetyDisclosure
        disclosures: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.disclosures, Unset):
            disclosures = []
            for disclosures_item_data in self.disclosures:
                disclosures_item = disclosures_item_data.to_dict()
                disclosures.append(disclosures_item)



        declared: list[str] | Unset = UNSET
        if not isinstance(self.declared, Unset):
            declared = self.declared




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if disclosures is not UNSET:
            field_dict["disclosures"] = disclosures
        if declared is not UNSET:
            field_dict["declared"] = declared

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_safety_disclosure import AirbnbSafetyDisclosure
        d = dict(src_dict)
        _disclosures = d.pop("disclosures", UNSET)
        disclosures: list[AirbnbSafetyDisclosure] | Unset = UNSET
        if _disclosures is not UNSET:
            disclosures = []
            for disclosures_item_data in _disclosures:
                disclosures_item = AirbnbSafetyDisclosure.from_dict(disclosures_item_data)



                disclosures.append(disclosures_item)


        declared = cast(list[str], d.pop("declared", UNSET))


        airbnb_safety_disclosures_response = cls(
            disclosures=disclosures,
            declared=declared,
        )


        airbnb_safety_disclosures_response.additional_properties = d
        return airbnb_safety_disclosures_response

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
