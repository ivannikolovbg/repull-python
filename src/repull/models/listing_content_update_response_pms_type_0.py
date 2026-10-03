from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_content_update_response_pms_type_0_errors_item import ListingContentUpdateResponsePmsType0ErrorsItem





T = TypeVar("T", bound="ListingContentUpdateResponsePmsType0")



@_attrs_define
class ListingContentUpdateResponsePmsType0:
    """ Present when the listing is managed in a PMS: the PMS-owned fields were written there first, and this is its per-
    section outcome.

        Attributes:
            provider (str | Unset):  Example: guesty.
            applied (list[str] | Unset): Sections the PMS applied.
            errors (list[ListingContentUpdateResponsePmsType0ErrorsItem] | Unset): Sections the PMS refused, with its
                reason.
     """

    provider: str | Unset = UNSET
    applied: list[str] | Unset = UNSET
    errors: list[ListingContentUpdateResponsePmsType0ErrorsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_content_update_response_pms_type_0_errors_item import ListingContentUpdateResponsePmsType0ErrorsItem
        provider = self.provider

        applied: list[str] | Unset = UNSET
        if not isinstance(self.applied, Unset):
            applied = self.applied



        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if provider is not UNSET:
            field_dict["provider"] = provider
        if applied is not UNSET:
            field_dict["applied"] = applied
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_content_update_response_pms_type_0_errors_item import ListingContentUpdateResponsePmsType0ErrorsItem
        d = dict(src_dict)
        provider = d.pop("provider", UNSET)

        applied = cast(list[str], d.pop("applied", UNSET))


        _errors = d.pop("errors", UNSET)
        errors: list[ListingContentUpdateResponsePmsType0ErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ListingContentUpdateResponsePmsType0ErrorsItem.from_dict(errors_item_data)



                errors.append(errors_item)


        listing_content_update_response_pms_type_0 = cls(
            provider=provider,
            applied=applied,
            errors=errors,
        )


        listing_content_update_response_pms_type_0.additional_properties = d
        return listing_content_update_response_pms_type_0

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
