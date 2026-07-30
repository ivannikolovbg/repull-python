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






T = TypeVar("T", bound="GetUsageLogsResponse200DataItem")



@_attrs_define
class GetUsageLogsResponse200DataItem:
    """ 
        Attributes:
            id (str | Unset):
            request_id (None | str | Unset):
            method (str | Unset):
            path (str | Unset):
            operation_id (None | str | Unset):
            status_code (int | None | Unset):
            latency_ms (int | None | Unset):
            request_bytes (int | None | Unset):
            response_bytes (int | None | Unset):
            ip_address (None | str | Unset):
            user_agent (None | str | Unset):
            error_code (None | str | Unset):
            created_at (datetime.datetime | Unset):
     """

    id: str | Unset = UNSET
    request_id: None | str | Unset = UNSET
    method: str | Unset = UNSET
    path: str | Unset = UNSET
    operation_id: None | str | Unset = UNSET
    status_code: int | None | Unset = UNSET
    latency_ms: int | None | Unset = UNSET
    request_bytes: int | None | Unset = UNSET
    response_bytes: int | None | Unset = UNSET
    ip_address: None | str | Unset = UNSET
    user_agent: None | str | Unset = UNSET
    error_code: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        request_id: None | str | Unset
        if isinstance(self.request_id, Unset):
            request_id = UNSET
        else:
            request_id = self.request_id

        method = self.method

        path = self.path

        operation_id: None | str | Unset
        if isinstance(self.operation_id, Unset):
            operation_id = UNSET
        else:
            operation_id = self.operation_id

        status_code: int | None | Unset
        if isinstance(self.status_code, Unset):
            status_code = UNSET
        else:
            status_code = self.status_code

        latency_ms: int | None | Unset
        if isinstance(self.latency_ms, Unset):
            latency_ms = UNSET
        else:
            latency_ms = self.latency_ms

        request_bytes: int | None | Unset
        if isinstance(self.request_bytes, Unset):
            request_bytes = UNSET
        else:
            request_bytes = self.request_bytes

        response_bytes: int | None | Unset
        if isinstance(self.response_bytes, Unset):
            response_bytes = UNSET
        else:
            response_bytes = self.response_bytes

        ip_address: None | str | Unset
        if isinstance(self.ip_address, Unset):
            ip_address = UNSET
        else:
            ip_address = self.ip_address

        user_agent: None | str | Unset
        if isinstance(self.user_agent, Unset):
            user_agent = UNSET
        else:
            user_agent = self.user_agent

        error_code: None | str | Unset
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if method is not UNSET:
            field_dict["method"] = method
        if path is not UNSET:
            field_dict["path"] = path
        if operation_id is not UNSET:
            field_dict["operationId"] = operation_id
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if latency_ms is not UNSET:
            field_dict["latencyMs"] = latency_ms
        if request_bytes is not UNSET:
            field_dict["requestBytes"] = request_bytes
        if response_bytes is not UNSET:
            field_dict["responseBytes"] = response_bytes
        if ip_address is not UNSET:
            field_dict["ipAddress"] = ip_address
        if user_agent is not UNSET:
            field_dict["userAgent"] = user_agent
        if error_code is not UNSET:
            field_dict["errorCode"] = error_code
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_request_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_id = _parse_request_id(d.pop("requestId", UNSET))


        method = d.pop("method", UNSET)

        path = d.pop("path", UNSET)

        def _parse_operation_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        operation_id = _parse_operation_id(d.pop("operationId", UNSET))


        def _parse_status_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status_code = _parse_status_code(d.pop("statusCode", UNSET))


        def _parse_latency_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latency_ms = _parse_latency_ms(d.pop("latencyMs", UNSET))


        def _parse_request_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        request_bytes = _parse_request_bytes(d.pop("requestBytes", UNSET))


        def _parse_response_bytes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        response_bytes = _parse_response_bytes(d.pop("responseBytes", UNSET))


        def _parse_ip_address(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        ip_address = _parse_ip_address(d.pop("ipAddress", UNSET))


        def _parse_user_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_agent = _parse_user_agent(d.pop("userAgent", UNSET))


        def _parse_error_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_code = _parse_error_code(d.pop("errorCode", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        get_usage_logs_response_200_data_item = cls(
            id=id,
            request_id=request_id,
            method=method,
            path=path,
            operation_id=operation_id,
            status_code=status_code,
            latency_ms=latency_ms,
            request_bytes=request_bytes,
            response_bytes=response_bytes,
            ip_address=ip_address,
            user_agent=user_agent,
            error_code=error_code,
            created_at=created_at,
        )


        get_usage_logs_response_200_data_item.additional_properties = d
        return get_usage_logs_response_200_data_item

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
