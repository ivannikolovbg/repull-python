from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_fees_response_200_data_cleaning_type_0 import GetVrboListingFeesResponse200DataCleaningType0
  from ..models.get_vrbo_listing_fees_response_200_data_custom_item import GetVrboListingFeesResponse200DataCustomItem
  from ..models.get_vrbo_listing_fees_response_200_data_extra_guests_type_0 import GetVrboListingFeesResponse200DataExtraGuestsType0
  from ..models.get_vrbo_listing_fees_response_200_data_pets_type_0 import GetVrboListingFeesResponse200DataPetsType0





T = TypeVar("T", bound="GetVrboListingFeesResponse200Data")



@_attrs_define
class GetVrboListingFeesResponse200Data:
    """ The section as Vrbo has it.

        Attributes:
            currency (None | str | Unset):
            cleaning (GetVrboListingFeesResponse200DataCleaningType0 | None | Unset):
            pets (GetVrboListingFeesResponse200DataPetsType0 | None | Unset):
            extra_guests (GetVrboListingFeesResponse200DataExtraGuestsType0 | None | Unset):
            custom (list[GetVrboListingFeesResponse200DataCustomItem] | Unset):
            custom_fee_codes (list[str] | Unset):
            fee_types (list[str] | Unset):
            extra_guest_fee_types (list[str] | Unset):
     """

    currency: None | str | Unset = UNSET
    cleaning: GetVrboListingFeesResponse200DataCleaningType0 | None | Unset = UNSET
    pets: GetVrboListingFeesResponse200DataPetsType0 | None | Unset = UNSET
    extra_guests: GetVrboListingFeesResponse200DataExtraGuestsType0 | None | Unset = UNSET
    custom: list[GetVrboListingFeesResponse200DataCustomItem] | Unset = UNSET
    custom_fee_codes: list[str] | Unset = UNSET
    fee_types: list[str] | Unset = UNSET
    extra_guest_fee_types: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_fees_response_200_data_cleaning_type_0 import GetVrboListingFeesResponse200DataCleaningType0
        from ..models.get_vrbo_listing_fees_response_200_data_custom_item import GetVrboListingFeesResponse200DataCustomItem
        from ..models.get_vrbo_listing_fees_response_200_data_extra_guests_type_0 import GetVrboListingFeesResponse200DataExtraGuestsType0
        from ..models.get_vrbo_listing_fees_response_200_data_pets_type_0 import GetVrboListingFeesResponse200DataPetsType0
        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        cleaning: dict[str, Any] | None | Unset
        if isinstance(self.cleaning, Unset):
            cleaning = UNSET
        elif isinstance(self.cleaning, GetVrboListingFeesResponse200DataCleaningType0):
            cleaning = self.cleaning.to_dict()
        else:
            cleaning = self.cleaning

        pets: dict[str, Any] | None | Unset
        if isinstance(self.pets, Unset):
            pets = UNSET
        elif isinstance(self.pets, GetVrboListingFeesResponse200DataPetsType0):
            pets = self.pets.to_dict()
        else:
            pets = self.pets

        extra_guests: dict[str, Any] | None | Unset
        if isinstance(self.extra_guests, Unset):
            extra_guests = UNSET
        elif isinstance(self.extra_guests, GetVrboListingFeesResponse200DataExtraGuestsType0):
            extra_guests = self.extra_guests.to_dict()
        else:
            extra_guests = self.extra_guests

        custom: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom, Unset):
            custom = []
            for custom_item_data in self.custom:
                custom_item = custom_item_data.to_dict()
                custom.append(custom_item)



        custom_fee_codes: list[str] | Unset = UNSET
        if not isinstance(self.custom_fee_codes, Unset):
            custom_fee_codes = self.custom_fee_codes



        fee_types: list[str] | Unset = UNSET
        if not isinstance(self.fee_types, Unset):
            fee_types = self.fee_types



        extra_guest_fee_types: list[str] | Unset = UNSET
        if not isinstance(self.extra_guest_fee_types, Unset):
            extra_guest_fee_types = self.extra_guest_fee_types




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if currency is not UNSET:
            field_dict["currency"] = currency
        if cleaning is not UNSET:
            field_dict["cleaning"] = cleaning
        if pets is not UNSET:
            field_dict["pets"] = pets
        if extra_guests is not UNSET:
            field_dict["extraGuests"] = extra_guests
        if custom is not UNSET:
            field_dict["custom"] = custom
        if custom_fee_codes is not UNSET:
            field_dict["customFeeCodes"] = custom_fee_codes
        if fee_types is not UNSET:
            field_dict["feeTypes"] = fee_types
        if extra_guest_fee_types is not UNSET:
            field_dict["extraGuestFeeTypes"] = extra_guest_fee_types

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_fees_response_200_data_cleaning_type_0 import GetVrboListingFeesResponse200DataCleaningType0
        from ..models.get_vrbo_listing_fees_response_200_data_custom_item import GetVrboListingFeesResponse200DataCustomItem
        from ..models.get_vrbo_listing_fees_response_200_data_extra_guests_type_0 import GetVrboListingFeesResponse200DataExtraGuestsType0
        from ..models.get_vrbo_listing_fees_response_200_data_pets_type_0 import GetVrboListingFeesResponse200DataPetsType0
        d = dict(src_dict)
        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_cleaning(data: object) -> GetVrboListingFeesResponse200DataCleaningType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cleaning_type_0 = GetVrboListingFeesResponse200DataCleaningType0.from_dict(data)



                return cleaning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboListingFeesResponse200DataCleaningType0 | None | Unset, data)

        cleaning = _parse_cleaning(d.pop("cleaning", UNSET))


        def _parse_pets(data: object) -> GetVrboListingFeesResponse200DataPetsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pets_type_0 = GetVrboListingFeesResponse200DataPetsType0.from_dict(data)



                return pets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboListingFeesResponse200DataPetsType0 | None | Unset, data)

        pets = _parse_pets(d.pop("pets", UNSET))


        def _parse_extra_guests(data: object) -> GetVrboListingFeesResponse200DataExtraGuestsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_guests_type_0 = GetVrboListingFeesResponse200DataExtraGuestsType0.from_dict(data)



                return extra_guests_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboListingFeesResponse200DataExtraGuestsType0 | None | Unset, data)

        extra_guests = _parse_extra_guests(d.pop("extraGuests", UNSET))


        _custom = d.pop("custom", UNSET)
        custom: list[GetVrboListingFeesResponse200DataCustomItem] | Unset = UNSET
        if _custom is not UNSET:
            custom = []
            for custom_item_data in _custom:
                custom_item = GetVrboListingFeesResponse200DataCustomItem.from_dict(custom_item_data)



                custom.append(custom_item)


        custom_fee_codes = cast(list[str], d.pop("customFeeCodes", UNSET))


        fee_types = cast(list[str], d.pop("feeTypes", UNSET))


        extra_guest_fee_types = cast(list[str], d.pop("extraGuestFeeTypes", UNSET))


        get_vrbo_listing_fees_response_200_data = cls(
            currency=currency,
            cleaning=cleaning,
            pets=pets,
            extra_guests=extra_guests,
            custom=custom,
            custom_fee_codes=custom_fee_codes,
            fee_types=fee_types,
            extra_guest_fee_types=extra_guest_fee_types,
        )


        get_vrbo_listing_fees_response_200_data.additional_properties = d
        return get_vrbo_listing_fees_response_200_data

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
