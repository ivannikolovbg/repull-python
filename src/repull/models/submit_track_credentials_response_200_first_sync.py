from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="SubmitTrackCredentialsResponse200FirstSync")



@_attrs_define
class SubmitTrackCredentialsResponse200FirstSync:
    """ Whether the first import of listings and reservations was queued. When it was not, the connection still stands and
    polling syncs it.

        Attributes:
            queued (bool | Unset):
            error (str | Unset):
     """

    queued: bool | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        queued = self.queued

        error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if queued is not UNSET:
            field_dict["queued"] = queued
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        queued = d.pop("queued", UNSET)

        error = d.pop("error", UNSET)

        submit_track_credentials_response_200_first_sync = cls(
            queued=queued,
            error=error,
        )


        submit_track_credentials_response_200_first_sync.additional_properties = d
        return submit_track_credentials_response_200_first_sync

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
