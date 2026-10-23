from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.channel_sync_failure_payload_object_operation import ChannelSyncFailurePayloadObjectOperation
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ChannelSyncFailurePayloadObject")



@_attrs_define
class ChannelSyncFailurePayloadObject:
    """ 
        Attributes:
            listing_id (int):
            customer_id (int):
            operation (ChannelSyncFailurePayloadObjectOperation): Which wire failed. A refused rate and a closed connection
                call for different responses.
            total (bool): true when NO mapping accepted the push. false means some did — the more dangerous case, because
                the listing is live somewhere and inconsistent.
            from_ (datetime.date | None | Unset): Start of the date range the push covered, when the operation is date-
                scoped.
            to (datetime.date | None | Unset):
     """

    listing_id: int
    customer_id: int
    operation: ChannelSyncFailurePayloadObjectOperation
    total: bool
    from_: datetime.date | None | Unset = UNSET
    to: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        listing_id = self.listing_id

        customer_id = self.customer_id

        operation = self.operation.value

        total = self.total

        from_: None | str | Unset
        if isinstance(self.from_, Unset):
            from_ = UNSET
        elif isinstance(self.from_, datetime.date):
            from_ = self.from_.isoformat()
        else:
            from_ = self.from_

        to: None | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        elif isinstance(self.to, datetime.date):
            to = self.to.isoformat()
        else:
            to = self.to


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "listingId": listing_id,
            "customerId": customer_id,
            "operation": operation,
            "total": total,
        })
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listing_id = d.pop("listingId")

        customer_id = d.pop("customerId")

        operation = ChannelSyncFailurePayloadObjectOperation(d.pop("operation"))




        total = d.pop("total")

        def _parse_from_(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                from_type_0 = isoparse(data).date()



                return from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        from_ = _parse_from_(d.pop("from", UNSET))


        def _parse_to(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                to_type_0 = isoparse(data).date()



                return to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        to = _parse_to(d.pop("to", UNSET))


        channel_sync_failure_payload_object = cls(
            listing_id=listing_id,
            customer_id=customer_id,
            operation=operation,
            total=total,
            from_=from_,
            to=to,
        )


        channel_sync_failure_payload_object.additional_properties = d
        return channel_sync_failure_payload_object

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
