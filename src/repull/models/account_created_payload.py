from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="AccountCreatedPayload")



@_attrs_define
class AccountCreatedPayload:
    """ Payload for `account.created`. An OAuth or API credential connection was completed by an end user.

        Attributes:
            workspace_id (UUID | Unset):  Example: 47f8883d-28c2-4d2c-b020-c7cef1aff62c.
            account_id (str | Unset):  Example: acc_01HX5XPQ2K.
            provider (str | Unset): PMS or channel provider id (e.g. airbnb, booking, hostaway). Example: airbnb.
            access_type (str | Unset):  Example: full_access.
            created_at (datetime.datetime | Unset):  Example: 2026-05-01T12:00:00.000Z.
     """

    workspace_id: UUID | Unset = UNSET
    account_id: str | Unset = UNSET
    provider: str | Unset = UNSET
    access_type: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        workspace_id: str | Unset = UNSET
        if not isinstance(self.workspace_id, Unset):
            workspace_id = str(self.workspace_id)

        account_id = self.account_id

        provider = self.provider

        access_type = self.access_type

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if access_type is not UNSET:
            field_dict["accessType"] = access_type
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _workspace_id = d.pop("workspaceId", UNSET)
        workspace_id: UUID | Unset
        if isinstance(_workspace_id,  Unset):
            workspace_id = UNSET
        else:
            workspace_id = UUID(_workspace_id)




        account_id = d.pop("accountId", UNSET)

        provider = d.pop("provider", UNSET)

        access_type = d.pop("accessType", UNSET)

        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        account_created_payload = cls(
            workspace_id=workspace_id,
            account_id=account_id,
            provider=provider,
            access_type=access_type,
            created_at=created_at,
        )


        account_created_payload.additional_properties = d
        return account_created_payload

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
