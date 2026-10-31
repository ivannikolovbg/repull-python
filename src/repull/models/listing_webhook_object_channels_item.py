from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.record_account_type_0 import RecordAccountType0





T = TypeVar("T", bound="ListingWebhookObjectChannelsItem")



@_attrs_define
class ListingWebhookObjectChannelsItem:
    """ 
        Attributes:
            platform (str | Unset):  Example: airbnb.
            external_id (str | Unset):  Example: 21466093.
            active (bool | Unset):
            sync_enabled (bool | Unset):
            sync_category (None | str | Unset):  Example: sync_all.
            account (None | RecordAccountType0 | Unset): The connected account this listing belongs to on this channel — for
                Airbnb the host account (`externalAccountId` is the Airbnb host id). The same account `account.disconnected`
                names, so a disconnect can be matched to its listings. Null when it cannot be resolved.
     """

    platform: str | Unset = UNSET
    external_id: str | Unset = UNSET
    active: bool | Unset = UNSET
    sync_enabled: bool | Unset = UNSET
    sync_category: None | str | Unset = UNSET
    account: None | RecordAccountType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.record_account_type_0 import RecordAccountType0
        platform = self.platform

        external_id = self.external_id

        active = self.active

        sync_enabled = self.sync_enabled

        sync_category: None | str | Unset
        if isinstance(self.sync_category, Unset):
            sync_category = UNSET
        else:
            sync_category = self.sync_category

        account: dict[str, Any] | None | Unset
        if isinstance(self.account, Unset):
            account = UNSET
        elif isinstance(self.account, RecordAccountType0):
            account = self.account.to_dict()
        else:
            account = self.account


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if platform is not UNSET:
            field_dict["platform"] = platform
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if active is not UNSET:
            field_dict["active"] = active
        if sync_enabled is not UNSET:
            field_dict["syncEnabled"] = sync_enabled
        if sync_category is not UNSET:
            field_dict["syncCategory"] = sync_category
        if account is not UNSET:
            field_dict["account"] = account

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.record_account_type_0 import RecordAccountType0
        d = dict(src_dict)
        platform = d.pop("platform", UNSET)

        external_id = d.pop("externalId", UNSET)

        active = d.pop("active", UNSET)

        sync_enabled = d.pop("syncEnabled", UNSET)

        def _parse_sync_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sync_category = _parse_sync_category(d.pop("syncCategory", UNSET))


        def _parse_account(data: object) -> None | RecordAccountType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_record_account_type_0 = RecordAccountType0.from_dict(data)



                return componentsschemas_record_account_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RecordAccountType0 | Unset, data)

        account = _parse_account(d.pop("account", UNSET))


        listing_webhook_object_channels_item = cls(
            platform=platform,
            external_id=external_id,
            active=active,
            sync_enabled=sync_enabled,
            sync_category=sync_category,
            account=account,
        )


        listing_webhook_object_channels_item.additional_properties = d
        return listing_webhook_object_channels_item

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
