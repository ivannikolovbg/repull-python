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






T = TypeVar("T", bound="AirbnbAlteration")



@_attrs_define
class AirbnbAlteration:
    """ An Airbnb reservation alteration request (date change, guest-count change, or price change), mirrored locally in
    `reservation_alterations`. Fields prefixed `original*` describe the reservation as it stands today; `new*` fields
    describe the proposed change. Compare them to render a diff and decide whether to accept (`POST .../{id}/accept`) or
    decline (`POST .../{id}/decline`).

        Attributes:
            id (int | Unset): Internal Repull mirror-row id (not the Airbnb alteration id — use `alterationId` for the
                `{id}` path param on the get / accept / decline routes).
            alteration_id (None | str | Unset): Airbnb alteration id. This is the `{id}` you pass to `GET/POST
                /v1/channels/airbnb/alterations/{id}` and the accept / decline sub-routes.
            reservation_id (int | None | Unset): Repull reservation id the alteration belongs to.
            platform (str | Unset): Always `airbnb` on this surface. Example: airbnb.
            status (None | str | Unset): Alteration lifecycle status — e.g. `pending` (awaiting a decision), `accepted`,
                `declined`, `canceled`.
            initiator (None | str | Unset): Who proposed the alteration — e.g. `host` or `guest`.
            reason (None | str | Unset): Free-text reason supplied with the alteration request.
            notes (None | str | Unset): Additional notes attached to the alteration.
            original_check_in (datetime.datetime | None | Unset): Check-in on the reservation BEFORE the proposed change.
            original_check_out (datetime.datetime | None | Unset): Check-out on the reservation BEFORE the proposed change.
            original_guest_count (int | None | Unset): Guest count BEFORE the proposed change.
            original_total_price (None | str | Unset): Total price (decimal string) BEFORE the proposed change.
            new_check_in (datetime.datetime | None | Unset): Proposed new check-in.
            new_check_out (datetime.datetime | None | Unset): Proposed new check-out.
            new_guest_count (int | None | Unset): Proposed new guest count.
            new_total_price (None | str | Unset): Proposed new total price (decimal string).
            created_at (datetime.datetime | None | Unset): When the alteration was first mirrored locally.
            updated_at (datetime.datetime | None | Unset): When the alteration mirror row was last updated.
     """

    id: int | Unset = UNSET
    alteration_id: None | str | Unset = UNSET
    reservation_id: int | None | Unset = UNSET
    platform: str | Unset = UNSET
    status: None | str | Unset = UNSET
    initiator: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    notes: None | str | Unset = UNSET
    original_check_in: datetime.datetime | None | Unset = UNSET
    original_check_out: datetime.datetime | None | Unset = UNSET
    original_guest_count: int | None | Unset = UNSET
    original_total_price: None | str | Unset = UNSET
    new_check_in: datetime.datetime | None | Unset = UNSET
    new_check_out: datetime.datetime | None | Unset = UNSET
    new_guest_count: int | None | Unset = UNSET
    new_total_price: None | str | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        alteration_id: None | str | Unset
        if isinstance(self.alteration_id, Unset):
            alteration_id = UNSET
        else:
            alteration_id = self.alteration_id

        reservation_id: int | None | Unset
        if isinstance(self.reservation_id, Unset):
            reservation_id = UNSET
        else:
            reservation_id = self.reservation_id

        platform = self.platform

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        initiator: None | str | Unset
        if isinstance(self.initiator, Unset):
            initiator = UNSET
        else:
            initiator = self.initiator

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        original_check_in: None | str | Unset
        if isinstance(self.original_check_in, Unset):
            original_check_in = UNSET
        elif isinstance(self.original_check_in, datetime.datetime):
            original_check_in = self.original_check_in.isoformat()
        else:
            original_check_in = self.original_check_in

        original_check_out: None | str | Unset
        if isinstance(self.original_check_out, Unset):
            original_check_out = UNSET
        elif isinstance(self.original_check_out, datetime.datetime):
            original_check_out = self.original_check_out.isoformat()
        else:
            original_check_out = self.original_check_out

        original_guest_count: int | None | Unset
        if isinstance(self.original_guest_count, Unset):
            original_guest_count = UNSET
        else:
            original_guest_count = self.original_guest_count

        original_total_price: None | str | Unset
        if isinstance(self.original_total_price, Unset):
            original_total_price = UNSET
        else:
            original_total_price = self.original_total_price

        new_check_in: None | str | Unset
        if isinstance(self.new_check_in, Unset):
            new_check_in = UNSET
        elif isinstance(self.new_check_in, datetime.datetime):
            new_check_in = self.new_check_in.isoformat()
        else:
            new_check_in = self.new_check_in

        new_check_out: None | str | Unset
        if isinstance(self.new_check_out, Unset):
            new_check_out = UNSET
        elif isinstance(self.new_check_out, datetime.datetime):
            new_check_out = self.new_check_out.isoformat()
        else:
            new_check_out = self.new_check_out

        new_guest_count: int | None | Unset
        if isinstance(self.new_guest_count, Unset):
            new_guest_count = UNSET
        else:
            new_guest_count = self.new_guest_count

        new_total_price: None | str | Unset
        if isinstance(self.new_total_price, Unset):
            new_total_price = UNSET
        else:
            new_total_price = self.new_total_price

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


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if alteration_id is not UNSET:
            field_dict["alterationId"] = alteration_id
        if reservation_id is not UNSET:
            field_dict["reservationId"] = reservation_id
        if platform is not UNSET:
            field_dict["platform"] = platform
        if status is not UNSET:
            field_dict["status"] = status
        if initiator is not UNSET:
            field_dict["initiator"] = initiator
        if reason is not UNSET:
            field_dict["reason"] = reason
        if notes is not UNSET:
            field_dict["notes"] = notes
        if original_check_in is not UNSET:
            field_dict["originalCheckIn"] = original_check_in
        if original_check_out is not UNSET:
            field_dict["originalCheckOut"] = original_check_out
        if original_guest_count is not UNSET:
            field_dict["originalGuestCount"] = original_guest_count
        if original_total_price is not UNSET:
            field_dict["originalTotalPrice"] = original_total_price
        if new_check_in is not UNSET:
            field_dict["newCheckIn"] = new_check_in
        if new_check_out is not UNSET:
            field_dict["newCheckOut"] = new_check_out
        if new_guest_count is not UNSET:
            field_dict["newGuestCount"] = new_guest_count
        if new_total_price is not UNSET:
            field_dict["newTotalPrice"] = new_total_price
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_alteration_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alteration_id = _parse_alteration_id(d.pop("alterationId", UNSET))


        def _parse_reservation_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        reservation_id = _parse_reservation_id(d.pop("reservationId", UNSET))


        platform = d.pop("platform", UNSET)

        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_initiator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        initiator = _parse_initiator(d.pop("initiator", UNSET))


        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))


        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))


        def _parse_original_check_in(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                original_check_in_type_0 = isoparse(data)



                return original_check_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        original_check_in = _parse_original_check_in(d.pop("originalCheckIn", UNSET))


        def _parse_original_check_out(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                original_check_out_type_0 = isoparse(data)



                return original_check_out_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        original_check_out = _parse_original_check_out(d.pop("originalCheckOut", UNSET))


        def _parse_original_guest_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        original_guest_count = _parse_original_guest_count(d.pop("originalGuestCount", UNSET))


        def _parse_original_total_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original_total_price = _parse_original_total_price(d.pop("originalTotalPrice", UNSET))


        def _parse_new_check_in(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                new_check_in_type_0 = isoparse(data)



                return new_check_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        new_check_in = _parse_new_check_in(d.pop("newCheckIn", UNSET))


        def _parse_new_check_out(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                new_check_out_type_0 = isoparse(data)



                return new_check_out_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        new_check_out = _parse_new_check_out(d.pop("newCheckOut", UNSET))


        def _parse_new_guest_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        new_guest_count = _parse_new_guest_count(d.pop("newGuestCount", UNSET))


        def _parse_new_total_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        new_total_price = _parse_new_total_price(d.pop("newTotalPrice", UNSET))


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


        airbnb_alteration = cls(
            id=id,
            alteration_id=alteration_id,
            reservation_id=reservation_id,
            platform=platform,
            status=status,
            initiator=initiator,
            reason=reason,
            notes=notes,
            original_check_in=original_check_in,
            original_check_out=original_check_out,
            original_guest_count=original_guest_count,
            original_total_price=original_total_price,
            new_check_in=new_check_in,
            new_check_out=new_check_out,
            new_guest_count=new_guest_count,
            new_total_price=new_total_price,
            created_at=created_at,
            updated_at=updated_at,
        )


        airbnb_alteration.additional_properties = d
        return airbnb_alteration

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
