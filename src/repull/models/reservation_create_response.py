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
  from ..models.reservation_create_response_pms import ReservationCreateResponsePms
  from ..models.reservation_create_response_unit_type_0 import ReservationCreateResponseUnitType0





T = TypeVar("T", bound="ReservationCreateResponse")



@_attrs_define
class ReservationCreateResponse:
    """ 
        Attributes:
            id (int | Unset): Pass to `GET /v1/reservations/{id}` for the full record. Example: 215708.
            confirmation_code (str | Unset):  Example: DIR-8H2K4N.
            listing_id (int | Unset):  Example: 4118.
            platform (str | Unset):  Example: direct.
            status (str | Unset): Same vocabulary as `GET /v1/reservations/{id}`. Example: confirmed.
            check_in (datetime.date | Unset):
            check_out (datetime.date | Unset):
            guest_id (int | None | Unset):
            total_price (float | None | Unset): The price the pricing engine derived for the stay. Reservations created
                through this endpoint are NOT priced from the request — see the operation description. On a Mews or Cloudbeds
                listing, the PMS prices it from its own rate.
            currency (None | str | Unset):
            unit (None | ReservationCreateResponseUnitType0 | Unset): Mews or Cloudbeds listings only: the room the PMS
                assigned. Absent for every other listing.
            pms (ReservationCreateResponsePms | Unset): Mews or Cloudbeds listings only: the booking was made in the PMS
                first, and this is what it applied.
     """

    id: int | Unset = UNSET
    confirmation_code: str | Unset = UNSET
    listing_id: int | Unset = UNSET
    platform: str | Unset = UNSET
    status: str | Unset = UNSET
    check_in: datetime.date | Unset = UNSET
    check_out: datetime.date | Unset = UNSET
    guest_id: int | None | Unset = UNSET
    total_price: float | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    unit: None | ReservationCreateResponseUnitType0 | Unset = UNSET
    pms: ReservationCreateResponsePms | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.reservation_create_response_pms import ReservationCreateResponsePms
        from ..models.reservation_create_response_unit_type_0 import ReservationCreateResponseUnitType0
        id = self.id

        confirmation_code = self.confirmation_code

        listing_id = self.listing_id

        platform = self.platform

        status = self.status

        check_in: str | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.isoformat()

        check_out: str | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.isoformat()

        guest_id: int | None | Unset
        if isinstance(self.guest_id, Unset):
            guest_id = UNSET
        else:
            guest_id = self.guest_id

        total_price: float | None | Unset
        if isinstance(self.total_price, Unset):
            total_price = UNSET
        else:
            total_price = self.total_price

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        unit: dict[str, Any] | None | Unset
        if isinstance(self.unit, Unset):
            unit = UNSET
        elif isinstance(self.unit, ReservationCreateResponseUnitType0):
            unit = self.unit.to_dict()
        else:
            unit = self.unit

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
        if platform is not UNSET:
            field_dict["platform"] = platform
        if status is not UNSET:
            field_dict["status"] = status
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if guest_id is not UNSET:
            field_dict["guestId"] = guest_id
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price
        if currency is not UNSET:
            field_dict["currency"] = currency
        if unit is not UNSET:
            field_dict["unit"] = unit
        if pms is not UNSET:
            field_dict["pms"] = pms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reservation_create_response_pms import ReservationCreateResponsePms
        from ..models.reservation_create_response_unit_type_0 import ReservationCreateResponseUnitType0
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        confirmation_code = d.pop("confirmationCode", UNSET)

        listing_id = d.pop("listingId", UNSET)

        platform = d.pop("platform", UNSET)

        status = d.pop("status", UNSET)

        _check_in = d.pop("checkIn", UNSET)
        check_in: datetime.date | Unset
        if isinstance(_check_in,  Unset):
            check_in = UNSET
        else:
            check_in = isoparse(_check_in).date()




        _check_out = d.pop("checkOut", UNSET)
        check_out: datetime.date | Unset
        if isinstance(_check_out,  Unset):
            check_out = UNSET
        else:
            check_out = isoparse(_check_out).date()




        def _parse_guest_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        guest_id = _parse_guest_id(d.pop("guestId", UNSET))


        def _parse_total_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_price = _parse_total_price(d.pop("totalPrice", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_unit(data: object) -> None | ReservationCreateResponseUnitType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                unit_type_0 = ReservationCreateResponseUnitType0.from_dict(data)



                return unit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReservationCreateResponseUnitType0 | Unset, data)

        unit = _parse_unit(d.pop("unit", UNSET))


        _pms = d.pop("pms", UNSET)
        pms: ReservationCreateResponsePms | Unset
        if isinstance(_pms,  Unset):
            pms = UNSET
        else:
            pms = ReservationCreateResponsePms.from_dict(_pms)




        reservation_create_response = cls(
            id=id,
            confirmation_code=confirmation_code,
            listing_id=listing_id,
            platform=platform,
            status=status,
            check_in=check_in,
            check_out=check_out,
            guest_id=guest_id,
            total_price=total_price,
            currency=currency,
            unit=unit,
            pms=pms,
        )


        reservation_create_response.additional_properties = d
        return reservation_create_response

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
