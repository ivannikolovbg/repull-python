from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.promotion_channel import PromotionChannel
from ..models.promotion_managed_by import PromotionManagedBy
from ..models.promotion_managed_key import PromotionManagedKey
from ..models.promotion_status import PromotionStatus
from ..models.promotion_type import PromotionType
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.promotion_applies_to_type_0 import PromotionAppliesToType0
  from ..models.promotion_discount import PromotionDiscount
  from ..models.promotion_rules import PromotionRules
  from ..models.promotion_usage_type_0 import PromotionUsageType0





T = TypeVar("T", bound="Promotion")



@_attrs_define
class Promotion:
    """ One promotion on one listing. Airbnb sets the discount for its promotions (`discount.setBy: channel`); Booking.com
    promotions belong to the property and list the rooms they cover in `appliesTo`.

        Attributes:
            id (str | Unset): Repull id of this promotion on this listing (use it in `/promotions/{promotionId}`).
            listing_id (str | Unset):
            channel (PromotionChannel | Unset):
            type_ (PromotionType | Unset): The same idea on both channels shares a type: `mobile` is Airbnb’s mobile-only
                discount or Booking.com’s mobile rate; `new_listing` is Airbnb’s new listing promotion or Booking.com’s new
                property deal. `top_rated_guests` is Airbnb only; the deal, last-minute, early-booker, country and campaign
                types are Booking.com only; `custom` (Airbnb Custom promotion) is read-only.
            channel_type (str | Unset): The channel’s own name, e.g. `HIGH_RATED_GUEST_DISCOUNT`, `basic`,
                `campaign_getaway`.
            external_id (str | Unset): The channel’s promotion id. Booking.com may issue a new one when a promotion is
                changed; the Repull `id` stays the same.
            channel_property_id (str | Unset): Airbnb listing id, or the Booking.com property (hotel id) the promotion
                belongs to.
            name (None | str | Unset):
            status (PromotionStatus | Unset): `eligible`: the listing qualifies but is not enrolled (Airbnb new listing
                promotion). `inactive`: switched off; Booking.com keeps deactivated promotions.
            managed_by (PromotionManagedBy | Unset): `channel`: created in the channel’s own tools and read-only here
                (Airbnb Custom promotions).
            managed_key (PromotionManagedKey | Unset): Set when it comes from the listing’s weekly or monthly discount in
                its pricing settings — change those instead.
            editable (bool | Unset):
            removable (bool | Unset):
            discount (PromotionDiscount | Unset):
            rules (PromotionRules | Unset): Which rules a type supports depends on the channel — see the catalog.
            applies_to (None | PromotionAppliesToType0 | Unset): Booking.com only. An empty `rooms` list means every room on
                the property.
            usage (None | PromotionUsageType0 | Unset):
            expires_at (datetime.datetime | None | Unset):
            synced_at (datetime.datetime | Unset):
     """

    id: str | Unset = UNSET
    listing_id: str | Unset = UNSET
    channel: PromotionChannel | Unset = UNSET
    type_: PromotionType | Unset = UNSET
    channel_type: str | Unset = UNSET
    external_id: str | Unset = UNSET
    channel_property_id: str | Unset = UNSET
    name: None | str | Unset = UNSET
    status: PromotionStatus | Unset = UNSET
    managed_by: PromotionManagedBy | Unset = UNSET
    managed_key: PromotionManagedKey | Unset = UNSET
    editable: bool | Unset = UNSET
    removable: bool | Unset = UNSET
    discount: PromotionDiscount | Unset = UNSET
    rules: PromotionRules | Unset = UNSET
    applies_to: None | PromotionAppliesToType0 | Unset = UNSET
    usage: None | PromotionUsageType0 | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    synced_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.promotion_applies_to_type_0 import PromotionAppliesToType0
        from ..models.promotion_discount import PromotionDiscount
        from ..models.promotion_rules import PromotionRules
        from ..models.promotion_usage_type_0 import PromotionUsageType0
        id = self.id

        listing_id = self.listing_id

        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value


        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        channel_type = self.channel_type

        external_id = self.external_id

        channel_property_id = self.channel_property_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        managed_by: str | Unset = UNSET
        if not isinstance(self.managed_by, Unset):
            managed_by = self.managed_by.value


        managed_key: str | Unset = UNSET
        if not isinstance(self.managed_key, Unset):
            managed_key = self.managed_key.value


        editable = self.editable

        removable = self.removable

        discount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.discount, Unset):
            discount = self.discount.to_dict()

        rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = self.rules.to_dict()

        applies_to: dict[str, Any] | None | Unset
        if isinstance(self.applies_to, Unset):
            applies_to = UNSET
        elif isinstance(self.applies_to, PromotionAppliesToType0):
            applies_to = self.applies_to.to_dict()
        else:
            applies_to = self.applies_to

        usage: dict[str, Any] | None | Unset
        if isinstance(self.usage, Unset):
            usage = UNSET
        elif isinstance(self.usage, PromotionUsageType0):
            usage = self.usage.to_dict()
        else:
            usage = self.usage

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        synced_at: str | Unset = UNSET
        if not isinstance(self.synced_at, Unset):
            synced_at = self.synced_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if type_ is not UNSET:
            field_dict["type"] = type_
        if channel_type is not UNSET:
            field_dict["channelType"] = channel_type
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if channel_property_id is not UNSET:
            field_dict["channelPropertyId"] = channel_property_id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if managed_by is not UNSET:
            field_dict["managedBy"] = managed_by
        if managed_key is not UNSET:
            field_dict["managedKey"] = managed_key
        if editable is not UNSET:
            field_dict["editable"] = editable
        if removable is not UNSET:
            field_dict["removable"] = removable
        if discount is not UNSET:
            field_dict["discount"] = discount
        if rules is not UNSET:
            field_dict["rules"] = rules
        if applies_to is not UNSET:
            field_dict["appliesTo"] = applies_to
        if usage is not UNSET:
            field_dict["usage"] = usage
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if synced_at is not UNSET:
            field_dict["syncedAt"] = synced_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promotion_applies_to_type_0 import PromotionAppliesToType0
        from ..models.promotion_discount import PromotionDiscount
        from ..models.promotion_rules import PromotionRules
        from ..models.promotion_usage_type_0 import PromotionUsageType0
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        listing_id = d.pop("listingId", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: PromotionChannel | Unset
        if isinstance(_channel,  Unset):
            channel = UNSET
        else:
            channel = PromotionChannel(_channel)




        _type_ = d.pop("type", UNSET)
        type_: PromotionType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = PromotionType(_type_)




        channel_type = d.pop("channelType", UNSET)

        external_id = d.pop("externalId", UNSET)

        channel_property_id = d.pop("channelPropertyId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        _status = d.pop("status", UNSET)
        status: PromotionStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = PromotionStatus(_status)




        _managed_by = d.pop("managedBy", UNSET)
        managed_by: PromotionManagedBy | Unset
        if isinstance(_managed_by,  Unset):
            managed_by = UNSET
        else:
            managed_by = PromotionManagedBy(_managed_by)




        _managed_key = d.pop("managedKey", UNSET)
        managed_key: PromotionManagedKey | Unset
        if isinstance(_managed_key,  Unset):
            managed_key = UNSET
        else:
            managed_key = PromotionManagedKey(_managed_key)




        editable = d.pop("editable", UNSET)

        removable = d.pop("removable", UNSET)

        _discount = d.pop("discount", UNSET)
        discount: PromotionDiscount | Unset
        if isinstance(_discount,  Unset):
            discount = UNSET
        else:
            discount = PromotionDiscount.from_dict(_discount)




        _rules = d.pop("rules", UNSET)
        rules: PromotionRules | Unset
        if isinstance(_rules,  Unset):
            rules = UNSET
        else:
            rules = PromotionRules.from_dict(_rules)




        def _parse_applies_to(data: object) -> None | PromotionAppliesToType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                applies_to_type_0 = PromotionAppliesToType0.from_dict(data)



                return applies_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PromotionAppliesToType0 | Unset, data)

        applies_to = _parse_applies_to(d.pop("appliesTo", UNSET))


        def _parse_usage(data: object) -> None | PromotionUsageType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                usage_type_0 = PromotionUsageType0.from_dict(data)



                return usage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PromotionUsageType0 | Unset, data)

        usage = _parse_usage(d.pop("usage", UNSET))


        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)



                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expiresAt", UNSET))


        _synced_at = d.pop("syncedAt", UNSET)
        synced_at: datetime.datetime | Unset
        if isinstance(_synced_at,  Unset):
            synced_at = UNSET
        else:
            synced_at = isoparse(_synced_at)




        promotion = cls(
            id=id,
            listing_id=listing_id,
            channel=channel,
            type_=type_,
            channel_type=channel_type,
            external_id=external_id,
            channel_property_id=channel_property_id,
            name=name,
            status=status,
            managed_by=managed_by,
            managed_key=managed_key,
            editable=editable,
            removable=removable,
            discount=discount,
            rules=rules,
            applies_to=applies_to,
            usage=usage,
            expires_at=expires_at,
            synced_at=synced_at,
        )


        promotion.additional_properties = d
        return promotion

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
