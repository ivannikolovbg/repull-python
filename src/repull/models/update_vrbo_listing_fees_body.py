from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_fees_body_cleaning_type_0 import UpdateVrboListingFeesBodyCleaningType0
  from ..models.update_vrbo_listing_fees_body_custom_item import UpdateVrboListingFeesBodyCustomItem
  from ..models.update_vrbo_listing_fees_body_extra_guests_type_0 import UpdateVrboListingFeesBodyExtraGuestsType0
  from ..models.update_vrbo_listing_fees_body_pets_type_0 import UpdateVrboListingFeesBodyPetsType0





T = TypeVar("T", bound="UpdateVrboListingFeesBody")



@_attrs_define
class UpdateVrboListingFeesBody:
    """ 
        Attributes:
            cleaning (None | Unset | UpdateVrboListingFeesBodyCleaningType0):
            pets (None | Unset | UpdateVrboListingFeesBodyPetsType0):
            extra_guests (None | Unset | UpdateVrboListingFeesBodyExtraGuestsType0):
            custom (list[UpdateVrboListingFeesBodyCustomItem] | Unset):
     """

    cleaning: None | Unset | UpdateVrboListingFeesBodyCleaningType0 = UNSET
    pets: None | Unset | UpdateVrboListingFeesBodyPetsType0 = UNSET
    extra_guests: None | Unset | UpdateVrboListingFeesBodyExtraGuestsType0 = UNSET
    custom: list[UpdateVrboListingFeesBodyCustomItem] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_fees_body_cleaning_type_0 import UpdateVrboListingFeesBodyCleaningType0
        from ..models.update_vrbo_listing_fees_body_custom_item import UpdateVrboListingFeesBodyCustomItem
        from ..models.update_vrbo_listing_fees_body_extra_guests_type_0 import UpdateVrboListingFeesBodyExtraGuestsType0
        from ..models.update_vrbo_listing_fees_body_pets_type_0 import UpdateVrboListingFeesBodyPetsType0
        cleaning: dict[str, Any] | None | Unset
        if isinstance(self.cleaning, Unset):
            cleaning = UNSET
        elif isinstance(self.cleaning, UpdateVrboListingFeesBodyCleaningType0):
            cleaning = self.cleaning.to_dict()
        else:
            cleaning = self.cleaning

        pets: dict[str, Any] | None | Unset
        if isinstance(self.pets, Unset):
            pets = UNSET
        elif isinstance(self.pets, UpdateVrboListingFeesBodyPetsType0):
            pets = self.pets.to_dict()
        else:
            pets = self.pets

        extra_guests: dict[str, Any] | None | Unset
        if isinstance(self.extra_guests, Unset):
            extra_guests = UNSET
        elif isinstance(self.extra_guests, UpdateVrboListingFeesBodyExtraGuestsType0):
            extra_guests = self.extra_guests.to_dict()
        else:
            extra_guests = self.extra_guests

        custom: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom, Unset):
            custom = []
            for custom_item_data in self.custom:
                custom_item = custom_item_data.to_dict()
                custom.append(custom_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if cleaning is not UNSET:
            field_dict["cleaning"] = cleaning
        if pets is not UNSET:
            field_dict["pets"] = pets
        if extra_guests is not UNSET:
            field_dict["extraGuests"] = extra_guests
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_fees_body_cleaning_type_0 import UpdateVrboListingFeesBodyCleaningType0
        from ..models.update_vrbo_listing_fees_body_custom_item import UpdateVrboListingFeesBodyCustomItem
        from ..models.update_vrbo_listing_fees_body_extra_guests_type_0 import UpdateVrboListingFeesBodyExtraGuestsType0
        from ..models.update_vrbo_listing_fees_body_pets_type_0 import UpdateVrboListingFeesBodyPetsType0
        d = dict(src_dict)
        def _parse_cleaning(data: object) -> None | Unset | UpdateVrboListingFeesBodyCleaningType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cleaning_type_0 = UpdateVrboListingFeesBodyCleaningType0.from_dict(data)



                return cleaning_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateVrboListingFeesBodyCleaningType0, data)

        cleaning = _parse_cleaning(d.pop("cleaning", UNSET))


        def _parse_pets(data: object) -> None | Unset | UpdateVrboListingFeesBodyPetsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pets_type_0 = UpdateVrboListingFeesBodyPetsType0.from_dict(data)



                return pets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateVrboListingFeesBodyPetsType0, data)

        pets = _parse_pets(d.pop("pets", UNSET))


        def _parse_extra_guests(data: object) -> None | Unset | UpdateVrboListingFeesBodyExtraGuestsType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                extra_guests_type_0 = UpdateVrboListingFeesBodyExtraGuestsType0.from_dict(data)



                return extra_guests_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UpdateVrboListingFeesBodyExtraGuestsType0, data)

        extra_guests = _parse_extra_guests(d.pop("extraGuests", UNSET))


        _custom = d.pop("custom", UNSET)
        custom: list[UpdateVrboListingFeesBodyCustomItem] | Unset = UNSET
        if _custom is not UNSET:
            custom = []
            for custom_item_data in _custom:
                custom_item = UpdateVrboListingFeesBodyCustomItem.from_dict(custom_item_data)



                custom.append(custom_item)


        update_vrbo_listing_fees_body = cls(
            cleaning=cleaning,
            pets=pets,
            extra_guests=extra_guests,
            custom=custom,
        )

        return update_vrbo_listing_fees_body

