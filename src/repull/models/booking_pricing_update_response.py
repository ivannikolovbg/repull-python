from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.booking_pricing_update_response_errors_item import BookingPricingUpdateResponseErrorsItem
  from ..models.booking_pricing_update_response_raw import BookingPricingUpdateResponseRaw





T = TypeVar("T", bound="BookingPricingUpdateResponse")



@_attrs_define
class BookingPricingUpdateResponse:
    """ 
        Attributes:
            hotel_id (str | Unset):
            listing_id (int | Unset):
            pushed (int | Unset): Number of updates Booking.com accepted as `success`. Falls back to total update count when
                Booking omits per-update status on full success.
            requested (int | Unset):
            errors (list[BookingPricingUpdateResponseErrorsItem] | Unset): Per-update failure rows from Booking — shape
                mirrors the Booking rates API response.
            raw (BookingPricingUpdateResponseRaw | Unset): Verbatim Booking response envelope for debugging.
     """

    hotel_id: str | Unset = UNSET
    listing_id: int | Unset = UNSET
    pushed: int | Unset = UNSET
    requested: int | Unset = UNSET
    errors: list[BookingPricingUpdateResponseErrorsItem] | Unset = UNSET
    raw: BookingPricingUpdateResponseRaw | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.booking_pricing_update_response_errors_item import BookingPricingUpdateResponseErrorsItem
        from ..models.booking_pricing_update_response_raw import BookingPricingUpdateResponseRaw
        hotel_id = self.hotel_id

        listing_id = self.listing_id

        pushed = self.pushed

        requested = self.requested

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)



        raw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.raw, Unset):
            raw = self.raw.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hotel_id is not UNSET:
            field_dict["hotel_id"] = hotel_id
        if listing_id is not UNSET:
            field_dict["listing_id"] = listing_id
        if pushed is not UNSET:
            field_dict["pushed"] = pushed
        if requested is not UNSET:
            field_dict["requested"] = requested
        if errors is not UNSET:
            field_dict["errors"] = errors
        if raw is not UNSET:
            field_dict["raw"] = raw

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.booking_pricing_update_response_errors_item import BookingPricingUpdateResponseErrorsItem
        from ..models.booking_pricing_update_response_raw import BookingPricingUpdateResponseRaw
        d = dict(src_dict)
        hotel_id = d.pop("hotel_id", UNSET)

        listing_id = d.pop("listing_id", UNSET)

        pushed = d.pop("pushed", UNSET)

        requested = d.pop("requested", UNSET)

        _errors = d.pop("errors", UNSET)
        errors: list[BookingPricingUpdateResponseErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = BookingPricingUpdateResponseErrorsItem.from_dict(errors_item_data)



                errors.append(errors_item)


        _raw = d.pop("raw", UNSET)
        raw: BookingPricingUpdateResponseRaw | Unset
        if isinstance(_raw,  Unset):
            raw = UNSET
        else:
            raw = BookingPricingUpdateResponseRaw.from_dict(_raw)




        booking_pricing_update_response = cls(
            hotel_id=hotel_id,
            listing_id=listing_id,
            pushed=pushed,
            requested=requested,
            errors=errors,
            raw=raw,
        )


        booking_pricing_update_response.additional_properties = d
        return booking_pricing_update_response

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
