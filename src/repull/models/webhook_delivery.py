from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="WebhookDelivery")



@_attrs_define
class WebhookDelivery:
    """ 
        Attributes:
            id (UUID | Unset):
            event_id (UUID | Unset): Stable across retries of the same logical event.
            event_type (str | Unset):
            status_code (int | None | Unset):
            response_time_ms (int | None | Unset):
            attempt (int | Unset):
            success (bool | Unset):
            error_message (None | str | Unset):
            created_at (datetime.datetime | Unset):
            succeeded_at (datetime.datetime | None | Unset):
            failed_at (datetime.datetime | None | Unset):
     """

    id: UUID | Unset = UNSET
    event_id: UUID | Unset = UNSET
    event_type: str | Unset = UNSET
    status_code: int | None | Unset = UNSET
    response_time_ms: int | None | Unset = UNSET
    attempt: int | Unset = UNSET
    success: bool | Unset = UNSET
    error_message: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    succeeded_at: datetime.datetime | None | Unset = UNSET
    failed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        event_id: str | Unset = UNSET
        if not isinstance(self.event_id, Unset):
            event_id = str(self.event_id)

        event_type = self.event_type

        status_code: int | None | Unset
        if isinstance(self.status_code, Unset):
            status_code = UNSET
        else:
            status_code = self.status_code

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

        succeeded_at: None | str | Unset
        if isinstance(self.succeeded_at, Unset):
            succeeded_at = UNSET
        elif isinstance(self.succeeded_at, datetime.datetime):
            succeeded_at = self.succeeded_at.isoformat()
        else:
            succeeded_at = self.succeeded_at

        failed_at: None | str | Unset
        if isinstance(self.failed_at, Unset):
            failed_at = UNSET
        elif isinstance(self.failed_at, datetime.datetime):
            failed_at = self.failed_at.isoformat()
        else:
            failed_at = self.failed_at


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
        if status_code is not UNSET:
            field_dict["statusCode"] = status_code
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
        if succeeded_at is not UNSET:
            field_dict["succeededAt"] = succeeded_at
        if failed_at is not UNSET:
            field_dict["failedAt"] = failed_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _event_id = d.pop("eventId", UNSET)
        event_id: UUID | Unset
        if isinstance(_event_id,  Unset):
            event_id = UNSET
        else:
            event_id = UUID(_event_id)




        event_type = d.pop("eventType", UNSET)

        def _parse_status_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status_code = _parse_status_code(d.pop("statusCode", UNSET))


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




        def _parse_succeeded_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                succeeded_at_type_0 = isoparse(data)



                return succeeded_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        succeeded_at = _parse_succeeded_at(d.pop("succeededAt", UNSET))


        def _parse_failed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                failed_at_type_0 = isoparse(data)



                return failed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        failed_at = _parse_failed_at(d.pop("failedAt", UNSET))


        webhook_delivery = cls(
            id=id,
            event_id=event_id,
            event_type=event_type,
            status_code=status_code,
            response_time_ms=response_time_ms,
            attempt=attempt,
            success=success,
            error_message=error_message,
            created_at=created_at,
            succeeded_at=succeeded_at,
            failed_at=failed_at,
        )


        webhook_delivery.additional_properties = d
        return webhook_delivery

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
