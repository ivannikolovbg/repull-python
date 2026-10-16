from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.promotion_catalog_field_options_item import PromotionCatalogFieldOptionsItem





T = TypeVar("T", bound="PromotionCatalogField")



@_attrs_define
class PromotionCatalogField:
    """ 
        Attributes:
            supported (bool | Unset):
            coming_soon (bool | Unset): Shown but not yet usable on this channel.
            required (bool | Unset):
            min_ (float | Unset):
            max_ (float | Unset):
            fixed (float | Unset): Value the channel sets (e.g. Airbnb’s 15% top-rated-guests discount).
            options (list[PromotionCatalogFieldOptionsItem] | Unset):
     """

    supported: bool | Unset = UNSET
    coming_soon: bool | Unset = UNSET
    required: bool | Unset = UNSET
    min_: float | Unset = UNSET
    max_: float | Unset = UNSET
    fixed: float | Unset = UNSET
    options: list[PromotionCatalogFieldOptionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.promotion_catalog_field_options_item import PromotionCatalogFieldOptionsItem
        supported = self.supported

        coming_soon = self.coming_soon

        required = self.required

        min_ = self.min_

        max_ = self.max_

        fixed = self.fixed

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if supported is not UNSET:
            field_dict["supported"] = supported
        if coming_soon is not UNSET:
            field_dict["comingSoon"] = coming_soon
        if required is not UNSET:
            field_dict["required"] = required
        if min_ is not UNSET:
            field_dict["min"] = min_
        if max_ is not UNSET:
            field_dict["max"] = max_
        if fixed is not UNSET:
            field_dict["fixed"] = fixed
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promotion_catalog_field_options_item import PromotionCatalogFieldOptionsItem
        d = dict(src_dict)
        supported = d.pop("supported", UNSET)

        coming_soon = d.pop("comingSoon", UNSET)

        required = d.pop("required", UNSET)

        min_ = d.pop("min", UNSET)

        max_ = d.pop("max", UNSET)

        fixed = d.pop("fixed", UNSET)

        _options = d.pop("options", UNSET)
        options: list[PromotionCatalogFieldOptionsItem] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = PromotionCatalogFieldOptionsItem.from_dict(options_item_data)



                options.append(options_item)


        promotion_catalog_field = cls(
            supported=supported,
            coming_soon=coming_soon,
            required=required,
            min_=min_,
            max_=max_,
            fixed=fixed,
            options=options,
        )


        promotion_catalog_field.additional_properties = d
        return promotion_catalog_field

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
