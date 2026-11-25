from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_publish_tiket_response_result_errors import ListingPublishTiketResponseResultErrors





T = TypeVar("T", bound="ListingPublishTiketResponseResult")



@_attrs_define
class ListingPublishTiketResponseResult:
    """ 
        Attributes:
            pushed (bool | Unset): `true` when every section landed.
            reason (str | Unset): Why nothing was sent, when `pushed` is `false` and no section was tried.
            sections (list[str] | Unset): Sections tiket.com accepted (for example the property, each room type, each rate
                plan).
            errors (ListingPublishTiketResponseResultErrors | Unset): Sections that did not land, with tiket.com's reason.
     """

    pushed: bool | Unset = UNSET
    reason: str | Unset = UNSET
    sections: list[str] | Unset = UNSET
    errors: ListingPublishTiketResponseResultErrors | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_publish_tiket_response_result_errors import ListingPublishTiketResponseResultErrors
        pushed = self.pushed

        reason = self.reason

        sections: list[str] | Unset = UNSET
        if not isinstance(self.sections, Unset):
            sections = self.sections



        errors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if pushed is not UNSET:
            field_dict["pushed"] = pushed
        if reason is not UNSET:
            field_dict["reason"] = reason
        if sections is not UNSET:
            field_dict["sections"] = sections
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_publish_tiket_response_result_errors import ListingPublishTiketResponseResultErrors
        d = dict(src_dict)
        pushed = d.pop("pushed", UNSET)

        reason = d.pop("reason", UNSET)

        sections = cast(list[str], d.pop("sections", UNSET))


        _errors = d.pop("errors", UNSET)
        errors: ListingPublishTiketResponseResultErrors | Unset
        if isinstance(_errors,  Unset):
            errors = UNSET
        else:
            errors = ListingPublishTiketResponseResultErrors.from_dict(_errors)




        listing_publish_tiket_response_result = cls(
            pushed=pushed,
            reason=reason,
            sections=sections,
            errors=errors,
        )


        listing_publish_tiket_response_result.additional_properties = d
        return listing_publish_tiket_response_result

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
