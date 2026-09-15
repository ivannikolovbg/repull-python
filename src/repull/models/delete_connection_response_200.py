from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="DeleteConnectionResponse200")



@_attrs_define
class DeleteConnectionResponse200:
    """ 
        Attributes:
            disconnected (bool): Always `true` on success.
            provider (str): The provider the account belonged to.
            account_id (None | str): The account that was disconnected. `null` only when the workspace had a stale
                connection record with no account to name, which was cleared.
            listings_deactivated (list[str]): Ids of the listings this call deactivated. Listings still connected through
                another account or channel are not included and stay active.
     """

    disconnected: bool
    provider: str
    account_id: None | str
    listings_deactivated: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        disconnected = self.disconnected

        provider = self.provider

        account_id: None | str
        account_id = self.account_id

        listings_deactivated = self.listings_deactivated




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "disconnected": disconnected,
            "provider": provider,
            "accountId": account_id,
            "listingsDeactivated": listings_deactivated,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        disconnected = d.pop("disconnected")

        provider = d.pop("provider")

        def _parse_account_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        account_id = _parse_account_id(d.pop("accountId"))


        listings_deactivated = cast(list[str], d.pop("listingsDeactivated"))


        delete_connection_response_200 = cls(
            disconnected=disconnected,
            provider=provider,
            account_id=account_id,
            listings_deactivated=listings_deactivated,
        )


        delete_connection_response_200.additional_properties = d
        return delete_connection_response_200

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
