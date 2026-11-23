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






T = TypeVar("T", bound="AppConnectionHealthRecentErrorsItem")



@_attrs_define
class AppConnectionHealthRecentErrorsItem:
    """ 
        Attributes:
            at (datetime.datetime | Unset):
            method (str | Unset):  Example: PUT.
            endpoint (str | Unset):  Example: /calendar/batch/4118.
            status_code (int | Unset):  Example: 404.
            message (None | str | Unset):
     """

    at: datetime.datetime | Unset = UNSET
    method: str | Unset = UNSET
    endpoint: str | Unset = UNSET
    status_code: int | Unset = UNSET
    message: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        at: str | Unset = UNSET
        if not isinstance(self.at, Unset):
            at = self.at.isoformat()

        method = self.method

        endpoint = self.endpoint

        status_code = self.status_code

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if at is not UNSET:
            field_dict["at"] = at
        if method is not UNSET:
            field_dict["method"] = method
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _at = d.pop("at", UNSET)
        at: datetime.datetime | Unset
        if isinstance(_at,  Unset):
            at = UNSET
        else:
            at = isoparse(_at)




        method = d.pop("method", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        status_code = d.pop("statusCode", UNSET)

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        app_connection_health_recent_errors_item = cls(
            at=at,
            method=method,
            endpoint=endpoint,
            status_code=status_code,
            message=message,
        )


        app_connection_health_recent_errors_item.additional_properties = d
        return app_connection_health_recent_errors_item

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
