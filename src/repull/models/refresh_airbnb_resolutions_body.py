from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.refresh_airbnb_resolutions_body_status import RefreshAirbnbResolutionsBodyStatus
from ..types import UNSET, Unset






T = TypeVar("T", bound="RefreshAirbnbResolutionsBody")



@_attrs_define
class RefreshAirbnbResolutionsBody:
    """ 
        Attributes:
            account_id (str | Unset): Limit the refresh to one Airbnb host id. Omit for all connected accounts.
            status (RefreshAirbnbResolutionsBodyStatus | Unset): Limit the refresh to one lifecycle. Omit for all.
     """

    account_id: str | Unset = UNSET
    status: RefreshAirbnbResolutionsBodyStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["account_id"] = account_id
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id", UNSET)

        _status = d.pop("status", UNSET)
        status: RefreshAirbnbResolutionsBodyStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = RefreshAirbnbResolutionsBodyStatus(_status)




        refresh_airbnb_resolutions_body = cls(
            account_id=account_id,
            status=status,
        )


        refresh_airbnb_resolutions_body.additional_properties = d
        return refresh_airbnb_resolutions_body

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
