from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.cancel_reservation_response_200_status import CancelReservationResponse200Status
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.reservation_pms_outcome import ReservationPmsOutcome





T = TypeVar("T", bound="CancelReservationResponse200")



@_attrs_define
class CancelReservationResponse200:
    """ 
        Attributes:
            id (str | Unset):
            confirmation_code (None | str | Unset):
            listing_id (None | str | Unset):
            status (CancelReservationResponse200Status | Unset):
            check_in (datetime.date | None | Unset):
            check_out (datetime.date | None | Unset):
            updated_at (None | str | Unset):
            already_cancelled (bool | Unset): Present and true when the reservation was already cancelled.
            pms (ReservationPmsOutcome | Unset): Present when the write was made in a PMS: what the PMS applied. `partial:
                true` means the booking exists in the PMS but the steps in `failedSections` (e.g. notes, a tentative state) did
                not apply — do not create it again.
     """

    id: str | Unset = UNSET
    confirmation_code: None | str | Unset = UNSET
    listing_id: None | str | Unset = UNSET
    status: CancelReservationResponse200Status | Unset = UNSET
    check_in: datetime.date | None | Unset = UNSET
    check_out: datetime.date | None | Unset = UNSET
    updated_at: None | str | Unset = UNSET
    already_cancelled: bool | Unset = UNSET
    pms: ReservationPmsOutcome | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_pms_outcome import ReservationPmsOutcome
        id = self.id

        confirmation_code: None | str | Unset
        if isinstance(self.confirmation_code, Unset):
            confirmation_code = UNSET
        else:
            confirmation_code = self.confirmation_code

        listing_id: None | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        check_in: None | str | Unset
        if isinstance(self.check_in, Unset):
            check_in = UNSET
        elif isinstance(self.check_in, datetime.date):
            check_in = self.check_in.isoformat()
        else:
            check_in = self.check_in

        check_out: None | str | Unset
        if isinstance(self.check_out, Unset):
            check_out = UNSET
        elif isinstance(self.check_out, datetime.date):
            check_out = self.check_out.isoformat()
        else:
            check_out = self.check_out

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at

        already_cancelled = self.already_cancelled

        pms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pms, Unset):
            pms = self.pms.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if status is not UNSET:
            field_dict["status"] = status
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if already_cancelled is not UNSET:
            field_dict["alreadyCancelled"] = already_cancelled
        if pms is not UNSET:
            field_dict["pms"] = pms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_pms_outcome import ReservationPmsOutcome
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_confirmation_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        confirmation_code = _parse_confirmation_code(d.pop("confirmationCode", UNSET))


        def _parse_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        _status = d.pop("status", UNSET)
        status: CancelReservationResponse200Status | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = CancelReservationResponse200Status(_status)




        def _parse_check_in(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_in_type_0 = isoparse(data).date()



                return check_in_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        check_in = _parse_check_in(d.pop("checkIn", UNSET))


        def _parse_check_out(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_out_type_0 = isoparse(data).date()



                return check_out_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        check_out = _parse_check_out(d.pop("checkOut", UNSET))


        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        already_cancelled = d.pop("alreadyCancelled", UNSET)

        _pms = d.pop("pms", UNSET)
        pms: ReservationPmsOutcome | Unset
        if isinstance(_pms,  Unset):
            pms = UNSET
        else:
            pms = ReservationPmsOutcome.from_dict(_pms)




        cancel_reservation_response_200 = cls(
            id=id,
            confirmation_code=confirmation_code,
            listing_id=listing_id,
            status=status,
            check_in=check_in,
            check_out=check_out,
            updated_at=updated_at,
            already_cancelled=already_cancelled,
            pms=pms,
        )


        cancel_reservation_response_200.additional_properties = d
        return cancel_reservation_response_200

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
