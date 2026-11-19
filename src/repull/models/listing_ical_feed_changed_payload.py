from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_ical_feed_changed_payload_action import ListingIcalFeedChangedPayloadAction
from ..models.listing_ical_feed_changed_payload_provider import ListingIcalFeedChangedPayloadProvider
from ..models.listing_ical_feed_changed_payload_reason_type_1 import ListingIcalFeedChangedPayloadReasonType1
from ..models.listing_ical_feed_changed_payload_reason_type_2_type_1 import ListingIcalFeedChangedPayloadReasonType2Type1
from ..models.listing_ical_feed_changed_payload_reason_type_3_type_1 import ListingIcalFeedChangedPayloadReasonType3Type1
from ..models.listing_ical_feed_changed_payload_trigger import ListingIcalFeedChangedPayloadTrigger
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.listing_ical_feed_changed_payload_feed import ListingIcalFeedChangedPayloadFeed
  from ..models.listing_webhook_object import ListingWebhookObject





T = TypeVar("T", bound="ListingIcalFeedChangedPayload")



@_attrs_define
class ListingIcalFeedChangedPayload:
    """ Payload for `listing.ical_feed_changed`: Repull changed a Vrbo unit's imported calendars, or could not. Repull
    imports the listing's Repull iCal backup feed into every calendar-synced Vrbo unit, and removes other tools'
    imported feeds while Repull is the unit's master calendar.

        Attributes:
            object_ (ListingWebhookObject): The listing, in the shape `GET /v1/listings/{id}` returns. Hydrated at delivery,
                so a receiver gets the listing rather than a reason to fetch one.
            provider (ListingIcalFeedChangedPayloadProvider):
            action (ListingIcalFeedChangedPayloadAction): `repull_feed_added`: the Repull feed is now imported (`reason:
                "repull_feed_missing"` when it had been removed on Vrbo and was put back). `repull_feed_add_failed`: Vrbo did
                not take it — ask the host to add `repullFeedUrl` in Vrbo → Calendar → Import calendar, named "Repull"; nothing
                else is changed on the unit until it is there. `other_feed_removed`: another tool's imported calendar (`feed`)
                was removed. `other_feed_remove_failed`: removing it failed — ask the host to remove it in Vrbo → Calendar →
                Import calendar. Repull also emails the workspace owner when an action failed.
            feed (ListingIcalFeedChangedPayloadFeed): The imported calendar acted on, as Vrbo shows it.
            repull_feed_url (str): The listing's Repull iCal backup feed (`GET /v1/listings/{id}/ical`).
            trigger (ListingIcalFeedChangedPayloadTrigger): `calendar_sync_enabled`: calendar sync was just switched on for
                the unit. `drift_check`: the daily Vrbo calendar check.
            occurred_at (datetime.datetime):
            reason (ListingIcalFeedChangedPayloadReasonType1 | ListingIcalFeedChangedPayloadReasonType2Type1 |
                ListingIcalFeedChangedPayloadReasonType3Type1 | None | Unset): Why Repull acted.
            error (None | str | Unset): Vrbo's answer, on a failed action.
            docs_url (str | Unset):  Example: https://repull.dev/docs/channels/vrbo/ical-backup.
     """

    object_: ListingWebhookObject
    provider: ListingIcalFeedChangedPayloadProvider
    action: ListingIcalFeedChangedPayloadAction
    feed: ListingIcalFeedChangedPayloadFeed
    repull_feed_url: str
    trigger: ListingIcalFeedChangedPayloadTrigger
    occurred_at: datetime.datetime
    reason: ListingIcalFeedChangedPayloadReasonType1 | ListingIcalFeedChangedPayloadReasonType2Type1 | ListingIcalFeedChangedPayloadReasonType3Type1 | None | Unset = UNSET
    error: None | str | Unset = UNSET
    docs_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_ical_feed_changed_payload_feed import ListingIcalFeedChangedPayloadFeed
        from ..models.listing_webhook_object import ListingWebhookObject
        object_ = self.object_.to_dict()

        provider = self.provider.value

        action = self.action.value

        feed = self.feed.to_dict()

        repull_feed_url = self.repull_feed_url

        trigger = self.trigger.value

        occurred_at = self.occurred_at.isoformat()

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        elif isinstance(self.reason, ListingIcalFeedChangedPayloadReasonType1):
            reason = self.reason.value
        elif isinstance(self.reason, ListingIcalFeedChangedPayloadReasonType2Type1):
            reason = self.reason.value
        elif isinstance(self.reason, ListingIcalFeedChangedPayloadReasonType3Type1):
            reason = self.reason.value
        else:
            reason = self.reason

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        docs_url = self.docs_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "object": object_,
            "provider": provider,
            "action": action,
            "feed": feed,
            "repullFeedUrl": repull_feed_url,
            "trigger": trigger,
            "occurredAt": occurred_at,
        })
        if reason is not UNSET:
            field_dict["reason"] = reason
        if error is not UNSET:
            field_dict["error"] = error
        if docs_url is not UNSET:
            field_dict["docsUrl"] = docs_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_ical_feed_changed_payload_feed import ListingIcalFeedChangedPayloadFeed
        from ..models.listing_webhook_object import ListingWebhookObject
        d = dict(src_dict)
        object_ = ListingWebhookObject.from_dict(d.pop("object"))




        provider = ListingIcalFeedChangedPayloadProvider(d.pop("provider"))




        action = ListingIcalFeedChangedPayloadAction(d.pop("action"))




        feed = ListingIcalFeedChangedPayloadFeed.from_dict(d.pop("feed"))




        repull_feed_url = d.pop("repullFeedUrl")

        trigger = ListingIcalFeedChangedPayloadTrigger(d.pop("trigger"))




        occurred_at = isoparse(d.pop("occurredAt"))




        def _parse_reason(data: object) -> ListingIcalFeedChangedPayloadReasonType1 | ListingIcalFeedChangedPayloadReasonType2Type1 | ListingIcalFeedChangedPayloadReasonType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_1 = ListingIcalFeedChangedPayloadReasonType1(data)



                return reason_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_2_type_1 = ListingIcalFeedChangedPayloadReasonType2Type1(data)



                return reason_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reason_type_3_type_1 = ListingIcalFeedChangedPayloadReasonType3Type1(data)



                return reason_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingIcalFeedChangedPayloadReasonType1 | ListingIcalFeedChangedPayloadReasonType2Type1 | ListingIcalFeedChangedPayloadReasonType3Type1 | None | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        docs_url = d.pop("docsUrl", UNSET)

        listing_ical_feed_changed_payload = cls(
            object_=object_,
            provider=provider,
            action=action,
            feed=feed,
            repull_feed_url=repull_feed_url,
            trigger=trigger,
            occurred_at=occurred_at,
            reason=reason,
            error=error,
            docs_url=docs_url,
        )


        listing_ical_feed_changed_payload.additional_properties = d
        return listing_ical_feed_changed_payload

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
