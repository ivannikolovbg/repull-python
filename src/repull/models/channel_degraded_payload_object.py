from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.channel_degraded_payload_object_status import ChannelDegradedPayloadObjectStatus
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ChannelDegradedPayloadObject")



@_attrs_define
class ChannelDegradedPayloadObject:
    """ 
        Attributes:
            customer_id (int):
            provider (str):  Example: booking.
            status (ChannelDegradedPayloadObjectStatus):
            external_account_id (None | str | Unset): The provider's own account, host or hotel id.
            detail (None | str | Unset): What we observed, in the provider's words where possible. A bare "degraded" tells
                nobody what to fix.
     """

    customer_id: int
    provider: str
    status: ChannelDegradedPayloadObjectStatus
    external_account_id: None | str | Unset = UNSET
    detail: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        customer_id = self.customer_id

        provider = self.provider

        status = self.status.value

        external_account_id: None | str | Unset
        if isinstance(self.external_account_id, Unset):
            external_account_id = UNSET
        else:
            external_account_id = self.external_account_id

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "customerId": customer_id,
            "provider": provider,
            "status": status,
        })
        if external_account_id is not UNSET:
            field_dict["externalAccountId"] = external_account_id
        if detail is not UNSET:
            field_dict["detail"] = detail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        customer_id = d.pop("customerId")

        provider = d.pop("provider")

        status = ChannelDegradedPayloadObjectStatus(d.pop("status"))




        def _parse_external_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_account_id = _parse_external_account_id(d.pop("externalAccountId", UNSET))


        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))


        channel_degraded_payload_object = cls(
            customer_id=customer_id,
            provider=provider,
            status=status,
            external_account_id=external_account_id,
            detail=detail,
        )


        channel_degraded_payload_object.additional_properties = d
        return channel_degraded_payload_object

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
