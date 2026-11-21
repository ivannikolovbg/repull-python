from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_house_rules_response_200_data_children import UpdateVrboListingHouseRulesResponse200DataChildren
  from ..models.update_vrbo_listing_house_rules_response_200_data_events import UpdateVrboListingHouseRulesResponse200DataEvents
  from ..models.update_vrbo_listing_house_rules_response_200_data_pets import UpdateVrboListingHouseRulesResponse200DataPets
  from ..models.update_vrbo_listing_house_rules_response_200_data_smoking import UpdateVrboListingHouseRulesResponse200DataSmoking





T = TypeVar("T", bound="UpdateVrboListingHouseRulesResponse200Data")



@_attrs_define
class UpdateVrboListingHouseRulesResponse200Data:
    """ What Vrbo has stored for the section, read back after the write.

        Attributes:
            check_in_time (None | str | Unset):
            check_out_time (None | str | Unset):
            max_guests (int | None | Unset):
            max_adults (int | None | Unset):
            occupancy_note (None | str | Unset):
            minimum_age (int | None | Unset):
            minimum_age_note (None | str | Unset):
            children (UpdateVrboListingHouseRulesResponse200DataChildren | Unset):
            pets (UpdateVrboListingHouseRulesResponse200DataPets | Unset):
            smoking (UpdateVrboListingHouseRulesResponse200DataSmoking | Unset):
            events (UpdateVrboListingHouseRulesResponse200DataEvents | Unset):
            custom_rules (list[str] | Unset):
            rental_agreement (Any | Unset):
            time_options (list[str] | Unset):
     """

    check_in_time: None | str | Unset = UNSET
    check_out_time: None | str | Unset = UNSET
    max_guests: int | None | Unset = UNSET
    max_adults: int | None | Unset = UNSET
    occupancy_note: None | str | Unset = UNSET
    minimum_age: int | None | Unset = UNSET
    minimum_age_note: None | str | Unset = UNSET
    children: UpdateVrboListingHouseRulesResponse200DataChildren | Unset = UNSET
    pets: UpdateVrboListingHouseRulesResponse200DataPets | Unset = UNSET
    smoking: UpdateVrboListingHouseRulesResponse200DataSmoking | Unset = UNSET
    events: UpdateVrboListingHouseRulesResponse200DataEvents | Unset = UNSET
    custom_rules: list[str] | Unset = UNSET
    rental_agreement: Any | Unset = UNSET
    time_options: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_house_rules_response_200_data_children import UpdateVrboListingHouseRulesResponse200DataChildren
        from ..models.update_vrbo_listing_house_rules_response_200_data_events import UpdateVrboListingHouseRulesResponse200DataEvents
        from ..models.update_vrbo_listing_house_rules_response_200_data_pets import UpdateVrboListingHouseRulesResponse200DataPets
        from ..models.update_vrbo_listing_house_rules_response_200_data_smoking import UpdateVrboListingHouseRulesResponse200DataSmoking
        check_in_time: None | str | Unset
        if isinstance(self.check_in_time, Unset):
            check_in_time = UNSET
        else:
            check_in_time = self.check_in_time

        check_out_time: None | str | Unset
        if isinstance(self.check_out_time, Unset):
            check_out_time = UNSET
        else:
            check_out_time = self.check_out_time

        max_guests: int | None | Unset
        if isinstance(self.max_guests, Unset):
            max_guests = UNSET
        else:
            max_guests = self.max_guests

        max_adults: int | None | Unset
        if isinstance(self.max_adults, Unset):
            max_adults = UNSET
        else:
            max_adults = self.max_adults

        occupancy_note: None | str | Unset
        if isinstance(self.occupancy_note, Unset):
            occupancy_note = UNSET
        else:
            occupancy_note = self.occupancy_note

        minimum_age: int | None | Unset
        if isinstance(self.minimum_age, Unset):
            minimum_age = UNSET
        else:
            minimum_age = self.minimum_age

        minimum_age_note: None | str | Unset
        if isinstance(self.minimum_age_note, Unset):
            minimum_age_note = UNSET
        else:
            minimum_age_note = self.minimum_age_note

        children: dict[str, Any] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = self.children.to_dict()

        pets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pets, Unset):
            pets = self.pets.to_dict()

        smoking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.smoking, Unset):
            smoking = self.smoking.to_dict()

        events: dict[str, Any] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        custom_rules: list[str] | Unset = UNSET
        if not isinstance(self.custom_rules, Unset):
            custom_rules = self.custom_rules



        rental_agreement = self.rental_agreement

        time_options: list[str] | Unset = UNSET
        if not isinstance(self.time_options, Unset):
            time_options = self.time_options




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if check_in_time is not UNSET:
            field_dict["checkInTime"] = check_in_time
        if check_out_time is not UNSET:
            field_dict["checkOutTime"] = check_out_time
        if max_guests is not UNSET:
            field_dict["maxGuests"] = max_guests
        if max_adults is not UNSET:
            field_dict["maxAdults"] = max_adults
        if occupancy_note is not UNSET:
            field_dict["occupancyNote"] = occupancy_note
        if minimum_age is not UNSET:
            field_dict["minimumAge"] = minimum_age
        if minimum_age_note is not UNSET:
            field_dict["minimumAgeNote"] = minimum_age_note
        if children is not UNSET:
            field_dict["children"] = children
        if pets is not UNSET:
            field_dict["pets"] = pets
        if smoking is not UNSET:
            field_dict["smoking"] = smoking
        if events is not UNSET:
            field_dict["events"] = events
        if custom_rules is not UNSET:
            field_dict["customRules"] = custom_rules
        if rental_agreement is not UNSET:
            field_dict["rentalAgreement"] = rental_agreement
        if time_options is not UNSET:
            field_dict["timeOptions"] = time_options

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_house_rules_response_200_data_children import UpdateVrboListingHouseRulesResponse200DataChildren
        from ..models.update_vrbo_listing_house_rules_response_200_data_events import UpdateVrboListingHouseRulesResponse200DataEvents
        from ..models.update_vrbo_listing_house_rules_response_200_data_pets import UpdateVrboListingHouseRulesResponse200DataPets
        from ..models.update_vrbo_listing_house_rules_response_200_data_smoking import UpdateVrboListingHouseRulesResponse200DataSmoking
        d = dict(src_dict)
        def _parse_check_in_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_in_time = _parse_check_in_time(d.pop("checkInTime", UNSET))


        def _parse_check_out_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_out_time = _parse_check_out_time(d.pop("checkOutTime", UNSET))


        def _parse_max_guests(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_guests = _parse_max_guests(d.pop("maxGuests", UNSET))


        def _parse_max_adults(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_adults = _parse_max_adults(d.pop("maxAdults", UNSET))


        def _parse_occupancy_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        occupancy_note = _parse_occupancy_note(d.pop("occupancyNote", UNSET))


        def _parse_minimum_age(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        minimum_age = _parse_minimum_age(d.pop("minimumAge", UNSET))


        def _parse_minimum_age_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        minimum_age_note = _parse_minimum_age_note(d.pop("minimumAgeNote", UNSET))


        _children = d.pop("children", UNSET)
        children: UpdateVrboListingHouseRulesResponse200DataChildren | Unset
        if isinstance(_children,  Unset):
            children = UNSET
        else:
            children = UpdateVrboListingHouseRulesResponse200DataChildren.from_dict(_children)




        _pets = d.pop("pets", UNSET)
        pets: UpdateVrboListingHouseRulesResponse200DataPets | Unset
        if isinstance(_pets,  Unset):
            pets = UNSET
        else:
            pets = UpdateVrboListingHouseRulesResponse200DataPets.from_dict(_pets)




        _smoking = d.pop("smoking", UNSET)
        smoking: UpdateVrboListingHouseRulesResponse200DataSmoking | Unset
        if isinstance(_smoking,  Unset):
            smoking = UNSET
        else:
            smoking = UpdateVrboListingHouseRulesResponse200DataSmoking.from_dict(_smoking)




        _events = d.pop("events", UNSET)
        events: UpdateVrboListingHouseRulesResponse200DataEvents | Unset
        if isinstance(_events,  Unset):
            events = UNSET
        else:
            events = UpdateVrboListingHouseRulesResponse200DataEvents.from_dict(_events)




        custom_rules = cast(list[str], d.pop("customRules", UNSET))


        rental_agreement = d.pop("rentalAgreement", UNSET)

        time_options = cast(list[str], d.pop("timeOptions", UNSET))


        update_vrbo_listing_house_rules_response_200_data = cls(
            check_in_time=check_in_time,
            check_out_time=check_out_time,
            max_guests=max_guests,
            max_adults=max_adults,
            occupancy_note=occupancy_note,
            minimum_age=minimum_age,
            minimum_age_note=minimum_age_note,
            children=children,
            pets=pets,
            smoking=smoking,
            events=events,
            custom_rules=custom_rules,
            rental_agreement=rental_agreement,
            time_options=time_options,
        )


        update_vrbo_listing_house_rules_response_200_data.additional_properties = d
        return update_vrbo_listing_house_rules_response_200_data

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
