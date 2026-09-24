from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateConnectSessionBodyWorkspace")



@_attrs_define
class CreateConnectSessionBodyWorkspace:
    """ Migrate only — the property manager being moved. Required unless you send `X-Workspace-Id` to reconnect an existing
    migration.

        Attributes:
            name (str | Unset):  Example: Seaside Rentals.
            external_ref (str | Unset): Your own id for this property manager. Returned on every migration read. Example:
                acct_8812.
     """

    name: str | Unset = UNSET
    external_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        external_ref = self.external_ref


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if external_ref is not UNSET:
            field_dict["externalRef"] = external_ref

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        external_ref = d.pop("externalRef", UNSET)

        create_connect_session_body_workspace = cls(
            name=name,
            external_ref=external_ref,
        )


        create_connect_session_body_workspace.additional_properties = d
        return create_connect_session_body_workspace

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
