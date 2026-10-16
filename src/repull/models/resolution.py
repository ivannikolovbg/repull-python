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
  from ..models.resolution_initiator_type_0 import ResolutionInitiatorType0
  from ..models.resolution_responder_type_0 import ResolutionResponderType0





T = TypeVar("T", bound="Resolution")



@_attrs_define
class Resolution:
    """ An Airbnb Resolution Center case (AirCover / damage, extra-guest, refund or change request). Read-only — Airbnb
    exposes no create/evidence/status API. The money a resolution moved rides in the transactions ledger as `Resolution
    Payout` / `Resolution Adjustment` rows sharing the same reference; join on `resolutionId`.

        Attributes:
            resolution_id (str): Airbnb's resolution id — the `{id}` path value and the join key to a transaction's
                `reference`. Example: CLSF-06464054.
            status (None | str): OPEN or CLOSED, as Airbnb reports it. Example: OPEN.
            confirmation_code (None | str | Unset): Airbnb confirmation code of the reservation the case is on. Example:
                HMZKMYCBC5.
            reservation_id (int | None | Unset): Repull's internal reservation id, when the reservation is in this
                workspace.
            listing_name (None | str | Unset):
            reason (None | str | Unset): Why the resolution was opened.
            case_status (None | str | Unset): Airbnb's case-status label.
            status_text (None | str | Unset): Human-readable status detail.
            suggested_action_text (None | str | Unset): Airbnb's hint on whose turn it is to act next — track progress with
                it.
            customer_support_initiated (bool | None | Unset): True when Airbnb Customer Support (not the host/guest) opened
                the case.
            product_type (None | str | Unset):
            initiator (None | ResolutionInitiatorType0 | Unset): Who opened the case (id + name).
            responder (None | ResolutionResponderType0 | Unset): Who responds (id + name).
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
            synced_at (datetime.datetime | None | Unset): When Repull last refreshed this case from Airbnb.
     """

    resolution_id: str
    status: None | str
    confirmation_code: None | str | Unset = UNSET
    reservation_id: int | None | Unset = UNSET
    listing_name: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    case_status: None | str | Unset = UNSET
    status_text: None | str | Unset = UNSET
    suggested_action_text: None | str | Unset = UNSET
    customer_support_initiated: bool | None | Unset = UNSET
    product_type: None | str | Unset = UNSET
    initiator: None | ResolutionInitiatorType0 | Unset = UNSET
    responder: None | ResolutionResponderType0 | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    synced_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.resolution_initiator_type_0 import ResolutionInitiatorType0
        from ..models.resolution_responder_type_0 import ResolutionResponderType0
        resolution_id = self.resolution_id

        status: None | str
        status = self.status

        confirmation_code: None | str | Unset
        if isinstance(self.confirmation_code, Unset):
            confirmation_code = UNSET
        else:
            confirmation_code = self.confirmation_code

        reservation_id: int | None | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        listing_name: None | str | Unset
        if isinstance(self.listing_name, Unset):
            listing_name = UNSET
        else:
            listing_name = self.listing_name

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        case_status: None | str | Unset
        if isinstance(self.case_status, Unset):
            case_status = UNSET
        else:
            case_status = self.case_status

        status_text: None | str | Unset
        if isinstance(self.status_text, Unset):
            status_text = UNSET
        else:
            status_text = self.status_text

        suggested_action_text: None | str | Unset
        if isinstance(self.suggested_action_text, Unset):
            suggested_action_text = UNSET
        else:
            suggested_action_text = self.suggested_action_text

        customer_support_initiated: bool | None | Unset
        if isinstance(self.customer_support_initiated, Unset):
            customer_support_initiated = UNSET
        else:
            customer_support_initiated = self.customer_support_initiated

        product_type: None | str | Unset
        if isinstance(self.product_type, Unset):
            product_type = UNSET
        else:
            product_type = self.product_type

        initiator: dict[str, Any] | None | Unset
        if isinstance(self.initiator, Unset):
            initiator = UNSET
        elif isinstance(self.initiator, ResolutionInitiatorType0):
            initiator = self.initiator.to_dict()
        else:
            initiator = self.initiator

        responder: dict[str, Any] | None | Unset
        if isinstance(self.responder, Unset):
            responder = UNSET
        elif isinstance(self.responder, ResolutionResponderType0):
            responder = self.responder.to_dict()
        else:
            responder = self.responder

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at

        synced_at: None | str | Unset
        if isinstance(self.synced_at, Unset):
            synced_at = UNSET
        elif isinstance(self.synced_at, datetime.datetime):
            synced_at = self.synced_at.isoformat()
        else:
            synced_at = self.synced_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "resolutionId": resolution_id,
            "status": status,
        })
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if listing_name is not UNSET:
            field_dict["listingName"] = listing_name
        if reason is not UNSET:
            field_dict["reason"] = reason
        if case_status is not UNSET:
            field_dict["caseStatus"] = case_status
        if status_text is not UNSET:
            field_dict["statusText"] = status_text
        if suggested_action_text is not UNSET:
            field_dict["suggestedActionText"] = suggested_action_text
        if customer_support_initiated is not UNSET:
            field_dict["customerSupportInitiated"] = customer_support_initiated
        if product_type is not UNSET:
            field_dict["productType"] = product_type
        if initiator is not UNSET:
            field_dict["initiator"] = initiator
        if responder is not UNSET:
            field_dict["responder"] = responder
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if synced_at is not UNSET:
            field_dict["syncedAt"] = synced_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resolution_initiator_type_0 import ResolutionInitiatorType0
        from ..models.resolution_responder_type_0 import ResolutionResponderType0
        d = dict(src_dict)
        resolution_id = d.pop("resolutionId")

        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))


        def _parse_confirmation_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confirmation_code = _parse_confirmation_code(d.pop("confirmationCode", UNSET))


        def _parse_reservation_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        def _parse_listing_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_name = _parse_listing_name(d.pop("listingName", UNSET))


        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        def _parse_case_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        case_status = _parse_case_status(d.pop("caseStatus", UNSET))


        def _parse_status_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_text = _parse_status_text(d.pop("statusText", UNSET))


        def _parse_suggested_action_text(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        suggested_action_text = _parse_suggested_action_text(d.pop("suggestedActionText", UNSET))


        def _parse_customer_support_initiated(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        customer_support_initiated = _parse_customer_support_initiated(d.pop("customerSupportInitiated", UNSET))


        def _parse_product_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_type = _parse_product_type(d.pop("productType", UNSET))


        def _parse_initiator(data: object) -> None | ResolutionInitiatorType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                initiator_type_0 = ResolutionInitiatorType0.from_dict(data)



                return initiator_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResolutionInitiatorType0 | Unset, data)

        initiator = _parse_initiator(d.pop("initiator", UNSET))


        def _parse_responder(data: object) -> None | ResolutionResponderType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                responder_type_0 = ResolutionResponderType0.from_dict(data)



                return responder_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResolutionResponderType0 | Unset, data)

        responder = _parse_responder(d.pop("responder", UNSET))


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        def _parse_synced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                synced_at_type_0 = isoparse(data)



                return synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        synced_at = _parse_synced_at(d.pop("syncedAt", UNSET))


        resolution = cls(
            resolution_id=resolution_id,
            status=status,
            confirmation_code=confirmation_code,
            reservation_id=reservation_id,
            listing_name=listing_name,
            reason=reason,
            case_status=case_status,
            status_text=status_text,
            suggested_action_text=suggested_action_text,
            customer_support_initiated=customer_support_initiated,
            product_type=product_type,
            initiator=initiator,
            responder=responder,
            created_at=created_at,
            updated_at=updated_at,
            synced_at=synced_at,
        )


        resolution.additional_properties = d
        return resolution

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
