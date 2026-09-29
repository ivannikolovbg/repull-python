from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_channel_health_response_200_status import GetChannelHealthResponse200Status
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_channel_health_response_200_vrbo import GetChannelHealthResponse200Vrbo





T = TypeVar("T", bound="GetChannelHealthResponse200")



@_attrs_define
class GetChannelHealthResponse200:
    """ 
        Attributes:
            status (GetChannelHealthResponse200Status | Unset):
            vrbo (GetChannelHealthResponse200Vrbo | Unset): VRBO only — the connector's own signals.
     """

    status: GetChannelHealthResponse200Status | Unset = UNSET
    vrbo: GetChannelHealthResponse200Vrbo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_channel_health_response_200_vrbo import GetChannelHealthResponse200Vrbo
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        vrbo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.vrbo, Unset):
            vrbo = self.vrbo.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if status is not UNSET:
            field_dict["status"] = status
        if vrbo is not UNSET:
            field_dict["vrbo"] = vrbo

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_channel_health_response_200_vrbo import GetChannelHealthResponse200Vrbo
        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: GetChannelHealthResponse200Status | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = GetChannelHealthResponse200Status(_status)




        _vrbo = d.pop("vrbo", UNSET)
        vrbo: GetChannelHealthResponse200Vrbo | Unset
        if isinstance(_vrbo,  Unset):
            vrbo = UNSET
        else:
            vrbo = GetChannelHealthResponse200Vrbo.from_dict(_vrbo)




        get_channel_health_response_200 = cls(
            status=status,
            vrbo=vrbo,
        )


        get_channel_health_response_200.additional_properties = d
        return get_channel_health_response_200

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
