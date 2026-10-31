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





T = TypeVar("T", bound="ListingChannel")



@_attrs_define
class ListingChannel:
    """ Per-platform connection for a listing — one row per channel the listing is published to.

        Attributes:
            platform (str | Unset):  Example: airbnb.
            external_id (str | Unset): ID in the platform (Airbnb listing id, Booking room id, etc.)
            active (bool | Unset):
            sync_enabled (bool | Unset):
            account (None | RecordAccountType0 | Unset): The connected account this listing belongs to on this channel — for
                Airbnb the host account (`externalAccountId` is the Airbnb host id). The same account `account.disconnected`
                names, so a disconnect can be matched to its listings. Null when it cannot be resolved.
     """

    platform: str | Unset = UNSET
    external_id: str | Unset = UNSET
    active: bool | Unset = UNSET
    sync_enabled: bool | Unset = UNSET
    account: None | RecordAccountType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.record_account_type_0 import RecordAccountType0
        platform = self.platform

        external_id = self.external_id

        active = self.active

        sync_enabled = self.sync_enabled

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


        listing_channel = cls(
            platform=platform,
            external_id=external_id,
            active=active,
            sync_enabled=sync_enabled,
            account=account,
        )


        listing_channel.additional_properties = d
        return listing_channel

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
