from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ReservationThreadAssignedPayloadObject")



@_attrs_define
class ReservationThreadAssignedPayloadObject:
    """ 
        Attributes:
            reservation_id (int):
            customer_id (int):
            thread_id (str): Repull conversation id.
            listing_id (int | None | Unset):
            external_thread_id (None | str | Unset): The channel's own conversation id.
            previous_reservation_id (int | None | Unset): What the thread pointed at before. Null on the common orphan-
                adoption case; set when a thread moved between bookings.
     """

    reservation_id: int
    customer_id: int
    thread_id: str
    listing_id: int | None | Unset = UNSET
    external_thread_id: None | str | Unset = UNSET
    previous_reservation_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        reservation_id = self.reservation_id

        customer_id = self.customer_id

        thread_id = self.thread_id

        listing_id: int | None | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        external_thread_id: None | str | Unset
        if isinstance(self.external_thread_id, Unset):
            external_thread_id = UNSET
        else:
            external_thread_id = self.external_thread_id

        previous_reservation_id: int | None | Unset
        if isinstance(self.previous_reservation_id, Unset):
            previous_reservation_id = UNSET
        else:
            previous_reservation_id = self.previous_reservation_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "reservationId": reservation_id,
            "customerId": customer_id,
            "threadId": thread_id,
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if external_thread_id is not UNSET:
            field_dict["externalThreadId"] = external_thread_id
        if previous_reservation_id is not UNSET:
            field_dict["previousReservationId"] = previous_reservation_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reservation_id = d.pop("reservationId")

        customer_id = d.pop("customerId")

        thread_id = d.pop("threadId")

        def _parse_listing_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        def _parse_external_thread_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_thread_id = _parse_external_thread_id(d.pop("externalThreadId", UNSET))


        def _parse_previous_reservation_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        previous_reservation_id = _parse_previous_reservation_id(d.pop("previousReservationId", UNSET))


        reservation_thread_assigned_payload_object = cls(
            reservation_id=reservation_id,
            customer_id=customer_id,
            thread_id=thread_id,
            listing_id=listing_id,
            external_thread_id=external_thread_id,
            previous_reservation_id=previous_reservation_id,
        )


        reservation_thread_assigned_payload_object.additional_properties = d
        return reservation_thread_assigned_payload_object

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
