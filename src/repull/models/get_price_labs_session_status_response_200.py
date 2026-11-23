from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_price_labs_session_status_response_200_status import GetPriceLabsSessionStatusResponse200Status
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GetPriceLabsSessionStatusResponse200")



@_attrs_define
class GetPriceLabsSessionStatusResponse200:
    """ 
        Attributes:
            status (GetPriceLabsSessionStatusResponse200Status | Unset):
            connection_id (None | str | Unset): The PriceLabs connection once the session holds a key.
     """

    status: GetPriceLabsSessionStatusResponse200Status | Unset = UNSET
    connection_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        connection_id: None | str | Unset
        if isinstance(self.connection_id, Unset):
            connection_id = UNSET
        else:
            connection_id = self.connection_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: GetPriceLabsSessionStatusResponse200Status | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = GetPriceLabsSessionStatusResponse200Status(_status)




        def _parse_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_id = _parse_connection_id(d.pop("connectionId", UNSET))


        get_price_labs_session_status_response_200 = cls(
            status=status,
            connection_id=connection_id,
        )


        get_price_labs_session_status_response_200.additional_properties = d
        return get_price_labs_session_status_response_200

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
