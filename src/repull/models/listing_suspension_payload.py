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
  from ..models.listing_webhook_object import ListingWebhookObject





T = TypeVar("T", bound="ListingSuspensionPayload")



@_attrs_define
class ListingSuspensionPayload:
    """ Payload for `listing.suspended` and `listing.reactivated`. A suspended listing keeps accepting calendar and pricing
    writes and silently applies none of them, which is indistinguishable from an API fault unless you are told. It is
    also the one listing change a host cannot reverse alone.

        Attributes:
            object_ (ListingWebhookObject): The listing, in the shape `GET /v1/listings/{id}` returns. Hydrated at delivery,
                so a receiver gets the listing rather than a reason to fetch one.
            occurred_at (datetime.datetime):
            reason (None | str | Unset): The channel's stated reason, verbatim, when it gives one. Example:
                quality_standards.
     """

    object_: ListingWebhookObject
    occurred_at: datetime.datetime
    reason: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_webhook_object import ListingWebhookObject
        object_ = self.object_.to_dict()

        occurred_at = self.occurred_at.isoformat()

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "object": object_,
            "occurredAt": occurred_at,
        })
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_webhook_object import ListingWebhookObject
        d = dict(src_dict)
        object_ = ListingWebhookObject.from_dict(d.pop("object"))




        occurred_at = isoparse(d.pop("occurredAt"))




        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        listing_suspension_payload = cls(
            object_=object_,
            occurred_at=occurred_at,
            reason=reason,
        )


        listing_suspension_payload.additional_properties = d
        return listing_suspension_payload

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
