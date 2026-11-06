from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_access_accounts_item_role import AirbnbAccessAccountsItemRole
from ..models.airbnb_access_accounts_item_state import AirbnbAccessAccountsItemState
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="AirbnbAccessAccountsItem")



@_attrs_define
class AirbnbAccessAccountsItem:
    """ 
        Attributes:
            account (str): What `account` on a send takes. Example: airbnb:228981432.
            name (None | str):  Example: Team Co-Host.
            role (AirbnbAccessAccountsItemRole):
            state (AirbnbAccessAccountsItemState): `connected` can act now; `disconnected` was connected to this workspace;
                `never_connected` is on the listing but was never connected here.
            disconnected_at (datetime.datetime | None):
     """

    account: str
    name: None | str
    role: AirbnbAccessAccountsItemRole
    state: AirbnbAccessAccountsItemState
    disconnected_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account = self.account

        name: None | str
        name = self.name

        role = self.role.value

        state = self.state.value

        disconnected_at: None | str
        if isinstance(self.disconnected_at, datetime.datetime):
            disconnected_at = self.disconnected_at.isoformat()
        else:
            disconnected_at = self.disconnected_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "account": account,
            "name": name,
            "role": role,
            "state": state,
            "disconnectedAt": disconnected_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account = d.pop("account")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))


        role = AirbnbAccessAccountsItemRole(d.pop("role"))




        state = AirbnbAccessAccountsItemState(d.pop("state"))




        def _parse_disconnected_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                disconnected_at_type_0 = isoparse(data)



                return disconnected_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        disconnected_at = _parse_disconnected_at(d.pop("disconnectedAt"))


        airbnb_access_accounts_item = cls(
            account=account,
            name=name,
            role=role,
            state=state,
            disconnected_at=disconnected_at,
        )


        airbnb_access_accounts_item.additional_properties = d
        return airbnb_access_accounts_item

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
