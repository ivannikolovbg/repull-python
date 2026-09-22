from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="BookingUpstreamFailure")



@_attrs_define
class BookingUpstreamFailure:
    """ Why Booking.com refused one half of a write, in their words. Present on the half that was refused.

        Attributes:
            message (str | Unset): Booking.com's own reason, taken from the body they answered with — never a paraphrase of
                their status code.
            upstream_status (int | None | Unset): The HTTP status Booking.com answered with.
            booking_code (None | str | Unset): Booking.com's own error code, when their envelope named one.
            booking_ruid (None | str | Unset): Booking.com's request id. Quote it to their connectivity support to have them
                trace the call.
            body (None | str | Unset): The upstream body, trimmed and capped, for when the parsed reason is not enough.
            code (None | str | Unset): How the failure was classified internally (e.g. `BAD_REQUEST`, `RATE_LIMITED`).
     """

    message: str | Unset = UNSET
    upstream_status: int | None | Unset = UNSET
    booking_code: None | str | Unset = UNSET
    booking_ruid: None | str | Unset = UNSET
    body: None | str | Unset = UNSET
    code: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        message = self.message

        upstream_status: int | None | Unset
        if isinstance(self.upstream_status, Unset):
            upstream_status = UNSET
        else:
            upstream_status = self.upstream_status

        booking_code: None | str | Unset
        if isinstance(self.booking_code, Unset):
            booking_code = UNSET
        else:
            booking_code = self.booking_code

        booking_ruid: None | str | Unset
        if isinstance(self.booking_ruid, Unset):
            booking_ruid = UNSET
        else:
            booking_ruid = self.booking_ruid

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        code: None | str | Unset
        if isinstance(self.code, Unset):
            code = UNSET
        else:
            code = self.code


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if message is not UNSET:
            field_dict["message"] = message
        if upstream_status is not UNSET:
            field_dict["upstream_status"] = upstream_status
        if booking_code is not UNSET:
            field_dict["booking_code"] = booking_code
        if booking_ruid is not UNSET:
            field_dict["booking_ruid"] = booking_ruid
        if body is not UNSET:
            field_dict["body"] = body
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        def _parse_upstream_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        upstream_status = _parse_upstream_status(d.pop("upstream_status", UNSET))


        def _parse_booking_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        booking_code = _parse_booking_code(d.pop("booking_code", UNSET))


        def _parse_booking_ruid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        booking_ruid = _parse_booking_ruid(d.pop("booking_ruid", UNSET))


        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))


        def _parse_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        code = _parse_code(d.pop("code", UNSET))


        booking_upstream_failure = cls(
            message=message,
            upstream_status=upstream_status,
            booking_code=booking_code,
            booking_ruid=booking_ruid,
            body=body,
            code=code,
        )


        booking_upstream_failure.additional_properties = d
        return booking_upstream_failure

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
