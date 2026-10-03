from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.resume_connect_response_400_error import ResumeConnectResponse400Error
from ..types import UNSET, Unset






T = TypeVar("T", bound="ResumeConnectResponse400")



@_attrs_define
class ResumeConnectResponse400:
    """ 
        Attributes:
            error (ResumeConnectResponse400Error):
            reason (str | Unset): Why the token was rejected (only with `invalid_resume_token`).
            channel (str | Unset): The token's channel (only with `unsupported_channel`).
     """

    error: ResumeConnectResponse400Error
    reason: str | Unset = UNSET
    channel: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        error = self.error.value

        reason = self.reason

        channel = self.channel


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "error": error,
        })
        if reason is not UNSET:
            field_dict["reason"] = reason
        if channel is not UNSET:
            field_dict["channel"] = channel

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = ResumeConnectResponse400Error(d.pop("error"))




        reason = d.pop("reason", UNSET)

        channel = d.pop("channel", UNSET)

        resume_connect_response_400 = cls(
            error=error,
            reason=reason,
            channel=channel,
        )


        resume_connect_response_400.additional_properties = d
        return resume_connect_response_400

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
