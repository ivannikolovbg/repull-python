from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.webhook_subscription_status import WebhookSubscriptionStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="WebhookSubscription")



@_attrs_define
class WebhookSubscription:
    """ A registered webhook endpoint. The `secret` field is only present in the response of `POST /v1/webhooks` and `POST
    /v1/webhooks/{id}/rotate-secret` (Stripe pattern — capture it then; it is masked everywhere else).

        Attributes:
            id (UUID | Unset):
            url (str | Unset):
            description (None | str | Unset):
            events (list[str] | Unset):  Example: ['reservation.created', 'reservation.updated'].
            api_version (str | Unset):  Example: 2026-04.
            status (WebhookSubscriptionStatus | Unset):
            consecutive_failures (int | Unset):
            last_delivered_at (datetime.datetime | None | Unset):
            last_success_at (datetime.datetime | None | Unset):
            last_failure_at (datetime.datetime | None | Unset):
            last_delivery_status (int | None | Unset):
            disabled_at (datetime.datetime | None | Unset):
            created_at (datetime.datetime | Unset):
            updated_at (datetime.datetime | Unset):
            secret_masked (None | str | Unset):  Example: whsec_a1b…f9c2.
            secret (None | str | Unset): Plaintext signing secret. Only returned by create + rotate. Capture and store
                securely.
     """

    id: UUID | Unset = UNSET
    url: str | Unset = UNSET
    description: None | str | Unset = UNSET
    events: list[str] | Unset = UNSET
    api_version: str | Unset = UNSET
    status: WebhookSubscriptionStatus | Unset = UNSET
    consecutive_failures: int | Unset = UNSET
    last_delivered_at: datetime.datetime | None | Unset = UNSET
    last_success_at: datetime.datetime | None | Unset = UNSET
    last_failure_at: datetime.datetime | None | Unset = UNSET
    last_delivery_status: int | None | Unset = UNSET
    disabled_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    secret_masked: None | str | Unset = UNSET
    secret: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        url = self.url

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events



        api_version = self.api_version

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        consecutive_failures = self.consecutive_failures

        last_delivered_at: None | str | Unset
        if isinstance(self.last_delivered_at, Unset):
            last_delivered_at = UNSET
        elif isinstance(self.last_delivered_at, datetime.datetime):
            last_delivered_at = self.last_delivered_at.isoformat()
        else:
            last_delivered_at = self.last_delivered_at

        last_success_at: None | str | Unset
        if isinstance(self.last_success_at, Unset):
            last_success_at = UNSET
        elif isinstance(self.last_success_at, datetime.datetime):
            last_success_at = self.last_success_at.isoformat()
        else:
            last_success_at = self.last_success_at

        last_failure_at: None | str | Unset
        if isinstance(self.last_failure_at, Unset):
            last_failure_at = UNSET
        elif isinstance(self.last_failure_at, datetime.datetime):
            last_failure_at = self.last_failure_at.isoformat()
        else:
            last_failure_at = self.last_failure_at

        last_delivery_status: int | None | Unset
        if isinstance(self.last_delivery_status, Unset):
            last_delivery_status = UNSET
        else:
            last_delivery_status = self.last_delivery_status

        disabled_at: None | str | Unset
        if isinstance(self.disabled_at, Unset):
            disabled_at = UNSET
        elif isinstance(self.disabled_at, datetime.datetime):
            disabled_at = self.disabled_at.isoformat()
        else:
            disabled_at = self.disabled_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        secret_masked: None | str | Unset
        if isinstance(self.secret_masked, Unset):
            secret_masked = UNSET
        else:
            secret_masked = self.secret_masked

        secret: None | str | Unset
        if isinstance(self.secret, Unset):
            secret = UNSET
        else:
            secret = self.secret


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if url is not UNSET:
            field_dict["url"] = url
        if description is not UNSET:
            field_dict["description"] = description
        if events is not UNSET:
            field_dict["events"] = events
        if api_version is not UNSET:
            field_dict["apiVersion"] = api_version
        if status is not UNSET:
            field_dict["status"] = status
        if consecutive_failures is not UNSET:
            field_dict["consecutiveFailures"] = consecutive_failures
        if last_delivered_at is not UNSET:
            field_dict["lastDeliveredAt"] = last_delivered_at
        if last_success_at is not UNSET:
            field_dict["lastSuccessAt"] = last_success_at
        if last_failure_at is not UNSET:
            field_dict["lastFailureAt"] = last_failure_at
        if last_delivery_status is not UNSET:
            field_dict["lastDeliveryStatus"] = last_delivery_status
        if disabled_at is not UNSET:
            field_dict["disabledAt"] = disabled_at
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if secret_masked is not UNSET:
            field_dict["secretMasked"] = secret_masked
        if secret is not UNSET:
            field_dict["secret"] = secret

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




        url = d.pop("url", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        events = cast(list[str], d.pop("events", UNSET))


        api_version = d.pop("apiVersion", UNSET)

        _status = d.pop("status", UNSET)
        status: WebhookSubscriptionStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = WebhookSubscriptionStatus(_status)




        consecutive_failures = d.pop("consecutiveFailures", UNSET)

        def _parse_last_delivered_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_delivered_at_type_0 = isoparse(data)



                return last_delivered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_delivered_at = _parse_last_delivered_at(d.pop("lastDeliveredAt", UNSET))


        def _parse_last_success_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_success_at_type_0 = isoparse(data)



                return last_success_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_success_at = _parse_last_success_at(d.pop("lastSuccessAt", UNSET))


        def _parse_last_failure_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_failure_at_type_0 = isoparse(data)



                return last_failure_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_failure_at = _parse_last_failure_at(d.pop("lastFailureAt", UNSET))


        def _parse_last_delivery_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_delivery_status = _parse_last_delivery_status(d.pop("lastDeliveryStatus", UNSET))


        def _parse_disabled_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                disabled_at_type_0 = isoparse(data)



                return disabled_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        disabled_at = _parse_disabled_at(d.pop("disabledAt", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        def _parse_secret_masked(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret_masked = _parse_secret_masked(d.pop("secretMasked", UNSET))


        def _parse_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret = _parse_secret(d.pop("secret", UNSET))


        webhook_subscription = cls(
            id=id,
            url=url,
            description=description,
            events=events,
            api_version=api_version,
            status=status,
            consecutive_failures=consecutive_failures,
            last_delivered_at=last_delivered_at,
            last_success_at=last_success_at,
            last_failure_at=last_failure_at,
            last_delivery_status=last_delivery_status,
            disabled_at=disabled_at,
            created_at=created_at,
            updated_at=updated_at,
            secret_masked=secret_masked,
            secret=secret,
        )


        webhook_subscription.additional_properties = d
        return webhook_subscription

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
