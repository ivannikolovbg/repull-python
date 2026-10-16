from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.promotion_catalog_entry_channel import PromotionCatalogEntryChannel
from ..models.promotion_type import PromotionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.promotion_catalog_entry_fields import PromotionCatalogEntryFields





T = TypeVar("T", bound="PromotionCatalogEntry")



@_attrs_define
class PromotionCatalogEntry:
    """ 
        Attributes:
            channel (PromotionCatalogEntryChannel | Unset):
            type_ (PromotionType | Unset): The same idea on both channels shares a type: `mobile` is Airbnb’s mobile-only
                discount or Booking.com’s mobile rate; `new_listing` is Airbnb’s new listing promotion or Booking.com’s new
                property deal. `top_rated_guests` is Airbnb only; the deal, last-minute, early-booker, country and campaign
                types are Booking.com only; `custom` (Airbnb Custom promotion) is read-only.
            channel_type (str | Unset):
            campaign (str | Unset):
            label (str | Unset):
            description (str | Unset): One or two sentences to show hosts.
            is_new (bool | Unset): Newly available — show a “New” badge.
            available (bool | Unset):
            unavailable_reason (str | Unset):
            single (bool | Unset): Only one at a time (Airbnb types; Booking.com mobile and country rates per property).
            fields (PromotionCatalogEntryFields | Unset): Every field, supported or not, so a UI can grey out what a type
                does not take.
     """

    channel: PromotionCatalogEntryChannel | Unset = UNSET
    type_: PromotionType | Unset = UNSET
    channel_type: str | Unset = UNSET
    campaign: str | Unset = UNSET
    label: str | Unset = UNSET
    description: str | Unset = UNSET
    is_new: bool | Unset = UNSET
    available: bool | Unset = UNSET
    unavailable_reason: str | Unset = UNSET
    single: bool | Unset = UNSET
    fields: PromotionCatalogEntryFields | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.promotion_catalog_entry_fields import PromotionCatalogEntryFields
        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value


        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        channel_type = self.channel_type

        campaign = self.campaign

        label = self.label

        description = self.description

        is_new = self.is_new

        available = self.available

        unavailable_reason = self.unavailable_reason

        single = self.single

        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if channel is not UNSET:
            field_dict["channel"] = channel
        if type_ is not UNSET:
            field_dict["type"] = type_
        if channel_type is not UNSET:
            field_dict["channelType"] = channel_type
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if label is not UNSET:
            field_dict["label"] = label
        if description is not UNSET:
            field_dict["description"] = description
        if is_new is not UNSET:
            field_dict["isNew"] = is_new
        if available is not UNSET:
            field_dict["available"] = available
        if unavailable_reason is not UNSET:
            field_dict["unavailableReason"] = unavailable_reason
        if single is not UNSET:
            field_dict["single"] = single
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promotion_catalog_entry_fields import PromotionCatalogEntryFields
        d = dict(src_dict)
        _channel = d.pop("channel", UNSET)
        channel: PromotionCatalogEntryChannel | Unset
        if isinstance(_channel,  Unset):
            channel = UNSET
        else:
            channel = PromotionCatalogEntryChannel(_channel)




        _type_ = d.pop("type", UNSET)
        type_: PromotionType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = PromotionType(_type_)




        channel_type = d.pop("channelType", UNSET)

        campaign = d.pop("campaign", UNSET)

        label = d.pop("label", UNSET)

        description = d.pop("description", UNSET)

        is_new = d.pop("isNew", UNSET)

        available = d.pop("available", UNSET)

        unavailable_reason = d.pop("unavailableReason", UNSET)

        single = d.pop("single", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: PromotionCatalogEntryFields | Unset
        if isinstance(_fields,  Unset):
            fields = UNSET
        else:
            fields = PromotionCatalogEntryFields.from_dict(_fields)




        promotion_catalog_entry = cls(
            channel=channel,
            type_=type_,
            channel_type=channel_type,
            campaign=campaign,
            label=label,
            description=description,
            is_new=is_new,
            available=available,
            unavailable_reason=unavailable_reason,
            single=single,
            fields=fields,
        )


        promotion_catalog_entry.additional_properties = d
        return promotion_catalog_entry

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
