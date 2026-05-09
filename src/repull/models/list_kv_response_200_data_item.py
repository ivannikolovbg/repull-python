from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ListKvResponse200DataItem")



@_attrs_define
class ListKvResponse200DataItem:
    """ 
        Attributes:
            key (str | Unset):
            value (Any | Unset):
            ttl_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | Unset):
     """

    key: str | Unset = UNSET
    value: Any | Unset = UNSET
    ttl_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        ttl_at: None | str | Unset
        if isinstance(self.ttl_at, Unset):
            ttl_at = UNSET
        elif isinstance(self.ttl_at, datetime.datetime):
            ttl_at = self.ttl_at.isoformat()
        else:
            ttl_at = self.ttl_at

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value
        if ttl_at is not UNSET:
            field_dict["ttl_at"] = ttl_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        value = d.pop("value", UNSET)

        def _parse_ttl_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ttl_at_type_0 = isoparse(data)



                return ttl_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        ttl_at = _parse_ttl_at(d.pop("ttl_at", UNSET))


        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        list_kv_response_200_data_item = cls(
            key=key,
            value=value,
            ttl_at=ttl_at,
            updated_at=updated_at,
        )


        list_kv_response_200_data_item.additional_properties = d
        return list_kv_response_200_data_item

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
