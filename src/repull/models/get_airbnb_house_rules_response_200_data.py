from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_airbnb_house_rules_response_200_data_children import GetAirbnbHouseRulesResponse200DataChildren
  from ..models.get_airbnb_house_rules_response_200_data_events import GetAirbnbHouseRulesResponse200DataEvents
  from ..models.get_airbnb_house_rules_response_200_data_expectations_item import GetAirbnbHouseRulesResponse200DataExpectationsItem
  from ..models.get_airbnb_house_rules_response_200_data_house_rules_item import GetAirbnbHouseRulesResponse200DataHouseRulesItem
  from ..models.get_airbnb_house_rules_response_200_data_infants import GetAirbnbHouseRulesResponse200DataInfants
  from ..models.get_airbnb_house_rules_response_200_data_pets import GetAirbnbHouseRulesResponse200DataPets
  from ..models.get_airbnb_house_rules_response_200_data_smoking import GetAirbnbHouseRulesResponse200DataSmoking





T = TypeVar("T", bound="GetAirbnbHouseRulesResponse200Data")



@_attrs_define
class GetAirbnbHouseRulesResponse200Data:
    """ 
        Attributes:
            check_in_time (None | str | Unset): Earliest check-in, `HH:00` or `FLEXIBLE`. Example: 16:00.
            check_in_time_end (None | str | Unset): Latest check-in (Airbnb only). Example: 22:00.
            check_out_time (None | str | Unset):  Example: 11:00.
            max_guests (int | None | Unset):
            children (GetAirbnbHouseRulesResponse200DataChildren | Unset):
            infants (GetAirbnbHouseRulesResponse200DataInfants | Unset):
            pets (GetAirbnbHouseRulesResponse200DataPets | Unset):
            smoking (GetAirbnbHouseRulesResponse200DataSmoking | Unset):
            events (GetAirbnbHouseRulesResponse200DataEvents | Unset):
            expectations (list[GetAirbnbHouseRulesResponse200DataExpectationsItem] | Unset):
            house_rules (list[GetAirbnbHouseRulesResponse200DataHouseRulesItem] | Unset):
     """

    check_in_time: None | str | Unset = UNSET
    check_in_time_end: None | str | Unset = UNSET
    check_out_time: None | str | Unset = UNSET
    max_guests: int | None | Unset = UNSET
    children: GetAirbnbHouseRulesResponse200DataChildren | Unset = UNSET
    infants: GetAirbnbHouseRulesResponse200DataInfants | Unset = UNSET
    pets: GetAirbnbHouseRulesResponse200DataPets | Unset = UNSET
    smoking: GetAirbnbHouseRulesResponse200DataSmoking | Unset = UNSET
    events: GetAirbnbHouseRulesResponse200DataEvents | Unset = UNSET
    expectations: list[GetAirbnbHouseRulesResponse200DataExpectationsItem] | Unset = UNSET
    house_rules: list[GetAirbnbHouseRulesResponse200DataHouseRulesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_airbnb_house_rules_response_200_data_children import GetAirbnbHouseRulesResponse200DataChildren
        from ..models.get_airbnb_house_rules_response_200_data_events import GetAirbnbHouseRulesResponse200DataEvents
        from ..models.get_airbnb_house_rules_response_200_data_expectations_item import GetAirbnbHouseRulesResponse200DataExpectationsItem
        from ..models.get_airbnb_house_rules_response_200_data_house_rules_item import GetAirbnbHouseRulesResponse200DataHouseRulesItem
        from ..models.get_airbnb_house_rules_response_200_data_infants import GetAirbnbHouseRulesResponse200DataInfants
        from ..models.get_airbnb_house_rules_response_200_data_pets import GetAirbnbHouseRulesResponse200DataPets
        from ..models.get_airbnb_house_rules_response_200_data_smoking import GetAirbnbHouseRulesResponse200DataSmoking
        check_in_time: None | str | Unset
        if isinstance(self.check_in_time, Unset):
            check_in_time = UNSET
        else:
            check_in_time = self.check_in_time

        check_in_time_end: None | str | Unset
        if isinstance(self.check_in_time_end, Unset):
            check_in_time_end = UNSET
        else:
            check_in_time_end = self.check_in_time_end

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

        children: dict[str, Any] | Unset = UNSET
        if not isinstance(self.children, Unset):
            children = self.children.to_dict()

        infants: dict[str, Any] | Unset = UNSET
        if not isinstance(self.infants, Unset):
            infants = self.infants.to_dict()

        pets: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pets, Unset):
            pets = self.pets.to_dict()

        smoking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.smoking, Unset):
            smoking = self.smoking.to_dict()

        events: dict[str, Any] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events.to_dict()

        expectations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.expectations, Unset):
            expectations = []
            for expectations_item_data in self.expectations:
                expectations_item = expectations_item_data.to_dict()
                expectations.append(expectations_item)



        house_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.house_rules, Unset):
            house_rules = []
            for house_rules_item_data in self.house_rules:
                house_rules_item = house_rules_item_data.to_dict()
                house_rules.append(house_rules_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if check_in_time is not UNSET:
            field_dict["checkInTime"] = check_in_time
        if check_in_time_end is not UNSET:
            field_dict["checkInTimeEnd"] = check_in_time_end
        if check_out_time is not UNSET:
            field_dict["checkOutTime"] = check_out_time
        if max_guests is not UNSET:
            field_dict["maxGuests"] = max_guests
        if children is not UNSET:
            field_dict["children"] = children
        if infants is not UNSET:
            field_dict["infants"] = infants
        if pets is not UNSET:
            field_dict["pets"] = pets
        if smoking is not UNSET:
            field_dict["smoking"] = smoking
        if events is not UNSET:
            field_dict["events"] = events
        if expectations is not UNSET:
            field_dict["expectations"] = expectations
        if house_rules is not UNSET:
            field_dict["houseRules"] = house_rules

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_airbnb_house_rules_response_200_data_children import GetAirbnbHouseRulesResponse200DataChildren
        from ..models.get_airbnb_house_rules_response_200_data_events import GetAirbnbHouseRulesResponse200DataEvents
        from ..models.get_airbnb_house_rules_response_200_data_expectations_item import GetAirbnbHouseRulesResponse200DataExpectationsItem
        from ..models.get_airbnb_house_rules_response_200_data_house_rules_item import GetAirbnbHouseRulesResponse200DataHouseRulesItem
        from ..models.get_airbnb_house_rules_response_200_data_infants import GetAirbnbHouseRulesResponse200DataInfants
        from ..models.get_airbnb_house_rules_response_200_data_pets import GetAirbnbHouseRulesResponse200DataPets
        from ..models.get_airbnb_house_rules_response_200_data_smoking import GetAirbnbHouseRulesResponse200DataSmoking
        d = dict(src_dict)
        def _parse_check_in_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_in_time = _parse_check_in_time(d.pop("checkInTime", UNSET))


        def _parse_check_in_time_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_in_time_end = _parse_check_in_time_end(d.pop("checkInTimeEnd", UNSET))


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


        _children = d.pop("children", UNSET)
        children: GetAirbnbHouseRulesResponse200DataChildren | Unset
        if isinstance(_children,  Unset):
            children = UNSET
        else:
            children = GetAirbnbHouseRulesResponse200DataChildren.from_dict(_children)




        _infants = d.pop("infants", UNSET)
        infants: GetAirbnbHouseRulesResponse200DataInfants | Unset
        if isinstance(_infants,  Unset):
            infants = UNSET
        else:
            infants = GetAirbnbHouseRulesResponse200DataInfants.from_dict(_infants)




        _pets = d.pop("pets", UNSET)
        pets: GetAirbnbHouseRulesResponse200DataPets | Unset
        if isinstance(_pets,  Unset):
            pets = UNSET
        else:
            pets = GetAirbnbHouseRulesResponse200DataPets.from_dict(_pets)




        _smoking = d.pop("smoking", UNSET)
        smoking: GetAirbnbHouseRulesResponse200DataSmoking | Unset
        if isinstance(_smoking,  Unset):
            smoking = UNSET
        else:
            smoking = GetAirbnbHouseRulesResponse200DataSmoking.from_dict(_smoking)




        _events = d.pop("events", UNSET)
        events: GetAirbnbHouseRulesResponse200DataEvents | Unset
        if isinstance(_events,  Unset):
            events = UNSET
        else:
            events = GetAirbnbHouseRulesResponse200DataEvents.from_dict(_events)




        _expectations = d.pop("expectations", UNSET)
        expectations: list[GetAirbnbHouseRulesResponse200DataExpectationsItem] | Unset = UNSET
        if _expectations is not UNSET:
            expectations = []
            for expectations_item_data in _expectations:
                expectations_item = GetAirbnbHouseRulesResponse200DataExpectationsItem.from_dict(expectations_item_data)



                expectations.append(expectations_item)


        _house_rules = d.pop("houseRules", UNSET)
        house_rules: list[GetAirbnbHouseRulesResponse200DataHouseRulesItem] | Unset = UNSET
        if _house_rules is not UNSET:
            house_rules = []
            for house_rules_item_data in _house_rules:
                house_rules_item = GetAirbnbHouseRulesResponse200DataHouseRulesItem.from_dict(house_rules_item_data)



                house_rules.append(house_rules_item)


        get_airbnb_house_rules_response_200_data = cls(
            check_in_time=check_in_time,
            check_in_time_end=check_in_time_end,
            check_out_time=check_out_time,
            max_guests=max_guests,
            children=children,
            infants=infants,
            pets=pets,
            smoking=smoking,
            events=events,
            expectations=expectations,
            house_rules=house_rules,
        )


        get_airbnb_house_rules_response_200_data.additional_properties = d
        return get_airbnb_house_rules_response_200_data

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
