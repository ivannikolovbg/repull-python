from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ConnectStatusAccountsItem")



@_attrs_define
class ConnectStatusAccountsItem:
    """ 
        Attributes:
            external_account_id (str | Unset): Airbnb host ID, as a string (it can exceed 2^53). Example: 79730216.
            name (None | str | Unset):  Example: Raiden.
            picture_url (None | str | Unset):
            status (None | str | Unset):  Example: active.
            connected (bool | Unset): True while the account is active and its authorization is usable. Example: True.
     """

    external_account_id: str | Unset = UNSET
    name: None | str | Unset = UNSET
    picture_url: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    connected: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        external_account_id = self.external_account_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        picture_url: None | str | Unset
        if isinstance(self.picture_url, Unset):
            picture_url = UNSET
        else:
            picture_url = self.picture_url

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        connected = self.connected


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if external_account_id is not UNSET:
            field_dict["externalAccountId"] = external_account_id
        if name is not UNSET:
            field_dict["name"] = name
        if picture_url is not UNSET:
            field_dict["pictureUrl"] = picture_url
        if status is not UNSET:
            field_dict["status"] = status
        if connected is not UNSET:
            field_dict["connected"] = connected

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        external_account_id = d.pop("externalAccountId", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_picture_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        picture_url = _parse_picture_url(d.pop("pictureUrl", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        connected = d.pop("connected", UNSET)

        connect_status_accounts_item = cls(
            external_account_id=external_account_id,
            name=name,
            picture_url=picture_url,
            status=status,
            connected=connected,
        )


        connect_status_accounts_item.additional_properties = d
        return connect_status_accounts_item

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
