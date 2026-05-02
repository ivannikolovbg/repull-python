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

if TYPE_CHECKING:
  from ..models.webhook_delivery_detail_payload import WebhookDeliveryDetailPayload
  from ..models.webhook_delivery_detail_request_headers_type_0 import WebhookDeliveryDetailRequestHeadersType0
  from ..models.webhook_delivery_detail_response_headers_type_0 import WebhookDeliveryDetailResponseHeadersType0





T = TypeVar("T", bound="WebhookDeliveryDetail")



@_attrs_define
class WebhookDeliveryDetail:
    """ 
        Attributes:
            id (str | Unset):
            event_id (str | Unset):
            event_type (str | Unset):
            payload (WebhookDeliveryDetailPayload | Unset):
            request_headers (None | Unset | WebhookDeliveryDetailRequestHeadersType0):
            status_code (int | None | Unset):
            response_headers (None | Unset | WebhookDeliveryDetailResponseHeadersType0):
            response_body (None | str | Unset):
            response_time_ms (int | None | Unset):
            attempt (int | Unset):
            success (bool | Unset):
            error_message (None | str | Unset):
            created_at (datetime.datetime | Unset):
     """

    id: str | Unset = UNSET
    event_id: str | Unset = UNSET
    event_type: str | Unset = UNSET
    payload: WebhookDeliveryDetailPayload | Unset = UNSET
    request_headers: None | Unset | WebhookDeliveryDetailRequestHeadersType0 = UNSET
    status_code: int | None | Unset = UNSET
    response_headers: None | Unset | WebhookDeliveryDetailResponseHeadersType0 = UNSET
    response_body: None | str | Unset = UNSET
    response_time_ms: int | None | Unset = UNSET
    attempt: int | Unset = UNSET
    success: bool | Unset = UNSET
    error_message: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_delivery_detail_payload import WebhookDeliveryDetailPayload
        from ..models.webhook_delivery_detail_request_headers_type_0 import WebhookDeliveryDetailRequestHeadersType0
        from ..models.webhook_delivery_detail_response_headers_type_0 import WebhookDeliveryDetailResponseHeadersType0
        id = self.id

        event_id = self.event_id

        event_type = self.event_type

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        request_headers: dict[str, Any] | None | Unset
        if isinstance(self.request_headers, Unset):
            request_headers = UNSET
        elif isinstance(self.request_headers, WebhookDeliveryDetailRequestHeadersType0):
            request_headers = self.request_headers.to_dict()
        else:
            request_headers = self.request_headers

        status_code: int | None | Unset
        if isinstance(self.status_code, Unset):
            status_code = UNSET
        else:
            status_code = self.status_code

        response_headers: dict[str, Any] | None | Unset
        if isinstance(self.response_headers, Unset):
            response_headers = UNSET
        elif isinstance(self.response_headers, WebhookDeliveryDetailResponseHeadersType0):
            response_headers = self.response_headers.to_dict()
        else:
            response_headers = self.response_headers

        response_body: None | str | Unset
        if isinstance(self.response_body, Unset):
            response_body = UNSET
        else:
            response_body = self.response_body

        response_time_ms: int | None | Unset
        if isinstance(self.response_time_ms, Unset):
            response_time_ms = UNSET
        else:
            response_time_ms = self.response_time_ms

        attempt = self.attempt

        success = self.success

        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if payload is not UNSET:
            field_dict["payload"] = payload
        if request_headers is not UNSET:
            field_dict["requestHeaders"] = request_headers
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
        if response_headers is not UNSET:
            field_dict["responseHeaders"] = response_headers
        if response_body is not UNSET:
            field_dict["responseBody"] = response_body
        if response_time_ms is not UNSET:
            field_dict["responseTimeMs"] = response_time_ms
        if attempt is not UNSET:
            field_dict["attempt"] = attempt
        if success is not UNSET:
            field_dict["success"] = success
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_delivery_detail_payload import WebhookDeliveryDetailPayload
        from ..models.webhook_delivery_detail_request_headers_type_0 import WebhookDeliveryDetailRequestHeadersType0
        from ..models.webhook_delivery_detail_response_headers_type_0 import WebhookDeliveryDetailResponseHeadersType0
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        event_id = d.pop("eventId", UNSET)

        event_type = d.pop("eventType", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: WebhookDeliveryDetailPayload | Unset
        if isinstance(_payload,  Unset):
            payload = UNSET
        else:
            payload = WebhookDeliveryDetailPayload.from_dict(_payload)




        def _parse_request_headers(data: object) -> None | Unset | WebhookDeliveryDetailRequestHeadersType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                request_headers_type_0 = WebhookDeliveryDetailRequestHeadersType0.from_dict(data)



                return request_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WebhookDeliveryDetailRequestHeadersType0, data)

        request_headers = _parse_request_headers(d.pop("requestHeaders", UNSET))


        def _parse_status_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status_code = _parse_status_code(d.pop("statusCode", UNSET))


        def _parse_response_headers(data: object) -> None | Unset | WebhookDeliveryDetailResponseHeadersType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_headers_type_0 = WebhookDeliveryDetailResponseHeadersType0.from_dict(data)



                return response_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WebhookDeliveryDetailResponseHeadersType0, data)

        response_headers = _parse_response_headers(d.pop("responseHeaders", UNSET))


        def _parse_response_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        response_body = _parse_response_body(d.pop("responseBody", UNSET))


        def _parse_response_time_ms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        response_time_ms = _parse_response_time_ms(d.pop("responseTimeMs", UNSET))


        attempt = d.pop("attempt", UNSET)

        success = d.pop("success", UNSET)

        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("errorMessage", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        webhook_delivery_detail = cls(
            id=id,
            event_id=event_id,
            event_type=event_type,
            payload=payload,
            request_headers=request_headers,
            status_code=status_code,
            response_headers=response_headers,
            response_body=response_body,
            response_time_ms=response_time_ms,
            attempt=attempt,
            success=success,
            error_message=error_message,
            created_at=created_at,
        )


        webhook_delivery_detail.additional_properties = d
        return webhook_delivery_detail

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
