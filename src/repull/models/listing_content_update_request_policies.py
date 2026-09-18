from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_content_update_request_policies_check_in_method import ListingContentUpdateRequestPoliciesCheckInMethod
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_safety_disclosure import AirbnbSafetyDisclosure





T = TypeVar("T", bound="ListingContentUpdateRequestPolicies")



@_attrs_define
class ListingContentUpdateRequestPolicies:
    """ 
        Attributes:
            check_in_time_start (None | str | Unset): e.g. "15" (3pm).
            check_in_time_end (None | str | Unset):
            check_out_time (None | str | Unset): e.g. "11" (11am).
            house_rules (None | str | Unset): Free-text house rules.
            cancellation_policy (None | str | Unset): Cancellation policy slug/label.
            cancellation (None | str | Unset): Alias for `cancellationPolicy`.
            allows_children (bool | None | Unset):
            allows_infants (bool | None | Unset):
            allows_pets (bool | None | Unset):
            allows_smoking (bool | None | Unset):
            allows_events (bool | None | Unset):
            quiet_hours_start (None | str | Unset): Quiet-hours window start, e.g. "22:00". Distributed to Airbnb by the
                publish path. Example: 22:00.
            quiet_hours_end (None | str | Unset):  Example: 07:00.
            check_in_method (ListingContentUpdateRequestPoliciesCheckInMethod | Unset): How the guest lets themselves in.
                Canonical storage only — distributing it to Airbnb is `PUT /v1/channels/airbnb/listings/{id}/details` with
                `check_in_option`.
            check_in_instruction (None | str | Unset): Instruction shown with the check-in method.
            guest_safety_disclosures (list[AirbnbSafetyDisclosure] | None | Unset): Guest-safety disclosures — exterior
                cameras, noise monitors, stairs, pets, an unfenced pool. FULL replacement of the canonical set: omit to leave
                untouched, send `[]` to clear. Canonical storage only — distributing them to Airbnb is `PUT
                /v1/channels/airbnb/listings/{id}/safety-disclosures`, which merges rather than replaces.
     """

    check_in_time_start: None | str | Unset = UNSET
    check_in_time_end: None | str | Unset = UNSET
    check_out_time: None | str | Unset = UNSET
    house_rules: None | str | Unset = UNSET
    cancellation_policy: None | str | Unset = UNSET
    cancellation: None | str | Unset = UNSET
    allows_children: bool | None | Unset = UNSET
    allows_infants: bool | None | Unset = UNSET
    allows_pets: bool | None | Unset = UNSET
    allows_smoking: bool | None | Unset = UNSET
    allows_events: bool | None | Unset = UNSET
    quiet_hours_start: None | str | Unset = UNSET
    quiet_hours_end: None | str | Unset = UNSET
    check_in_method: ListingContentUpdateRequestPoliciesCheckInMethod | Unset = UNSET
    check_in_instruction: None | str | Unset = UNSET
    guest_safety_disclosures: list[AirbnbSafetyDisclosure] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_safety_disclosure import AirbnbSafetyDisclosure
        check_in_time_start: None | str | Unset
        if isinstance(self.check_in_time_start, Unset):
            check_in_time_start = UNSET
        else:
            check_in_time_start = self.check_in_time_start

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

        house_rules: None | str | Unset
        if isinstance(self.house_rules, Unset):
            house_rules = UNSET
        else:
            house_rules = self.house_rules

        cancellation_policy: None | str | Unset
        if isinstance(self.cancellation_policy, Unset):
            cancellation_policy = UNSET
        else:
            cancellation_policy = self.cancellation_policy

        cancellation: None | str | Unset
        if isinstance(self.cancellation, Unset):
            cancellation = UNSET
        else:
            cancellation = self.cancellation

        allows_children: bool | None | Unset
        if isinstance(self.allows_children, Unset):
            allows_children = UNSET
        else:
            allows_children = self.allows_children

        allows_infants: bool | None | Unset
        if isinstance(self.allows_infants, Unset):
            allows_infants = UNSET
        else:
            allows_infants = self.allows_infants

        allows_pets: bool | None | Unset
        if isinstance(self.allows_pets, Unset):
            allows_pets = UNSET
        else:
            allows_pets = self.allows_pets

        allows_smoking: bool | None | Unset
        if isinstance(self.allows_smoking, Unset):
            allows_smoking = UNSET
        else:
            allows_smoking = self.allows_smoking

        allows_events: bool | None | Unset
        if isinstance(self.allows_events, Unset):
            allows_events = UNSET
        else:
            allows_events = self.allows_events

        quiet_hours_start: None | str | Unset
        if isinstance(self.quiet_hours_start, Unset):
            quiet_hours_start = UNSET
        else:
            quiet_hours_start = self.quiet_hours_start

        quiet_hours_end: None | str | Unset
        if isinstance(self.quiet_hours_end, Unset):
            quiet_hours_end = UNSET
        else:
            quiet_hours_end = self.quiet_hours_end

        check_in_method: str | Unset = UNSET
        if not isinstance(self.check_in_method, Unset):
            check_in_method = self.check_in_method.value


        check_in_instruction: None | str | Unset
        if isinstance(self.check_in_instruction, Unset):
            check_in_instruction = UNSET
        else:
            check_in_instruction = self.check_in_instruction

        guest_safety_disclosures: list[dict[str, Any]] | None | Unset
        if isinstance(self.guest_safety_disclosures, Unset):
            guest_safety_disclosures = UNSET
        elif isinstance(self.guest_safety_disclosures, list):
            guest_safety_disclosures = []
            for guest_safety_disclosures_type_0_item_data in self.guest_safety_disclosures:
                guest_safety_disclosures_type_0_item = guest_safety_disclosures_type_0_item_data.to_dict()
                guest_safety_disclosures.append(guest_safety_disclosures_type_0_item)


        else:
            guest_safety_disclosures = self.guest_safety_disclosures


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if check_in_time_start is not UNSET:
            field_dict["checkInTimeStart"] = check_in_time_start
        if check_in_time_end is not UNSET:
            field_dict["checkInTimeEnd"] = check_in_time_end
        if check_out_time is not UNSET:
            field_dict["checkOutTime"] = check_out_time
        if house_rules is not UNSET:
            field_dict["houseRules"] = house_rules
        if cancellation_policy is not UNSET:
            field_dict["cancellationPolicy"] = cancellation_policy
        if cancellation is not UNSET:
            field_dict["cancellation"] = cancellation
        if allows_children is not UNSET:
            field_dict["allowsChildren"] = allows_children
        if allows_infants is not UNSET:
            field_dict["allowsInfants"] = allows_infants
        if allows_pets is not UNSET:
            field_dict["allowsPets"] = allows_pets
        if allows_smoking is not UNSET:
            field_dict["allowsSmoking"] = allows_smoking
        if allows_events is not UNSET:
            field_dict["allowsEvents"] = allows_events
        if quiet_hours_start is not UNSET:
            field_dict["quietHoursStart"] = quiet_hours_start
        if quiet_hours_end is not UNSET:
            field_dict["quietHoursEnd"] = quiet_hours_end
        if check_in_method is not UNSET:
            field_dict["checkInMethod"] = check_in_method
        if check_in_instruction is not UNSET:
            field_dict["checkInInstruction"] = check_in_instruction
        if guest_safety_disclosures is not UNSET:
            field_dict["guestSafetyDisclosures"] = guest_safety_disclosures

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_safety_disclosure import AirbnbSafetyDisclosure
        d = dict(src_dict)
        def _parse_check_in_time_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_in_time_start = _parse_check_in_time_start(d.pop("checkInTimeStart", UNSET))


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


        def _parse_house_rules(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        house_rules = _parse_house_rules(d.pop("houseRules", UNSET))


        def _parse_cancellation_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancellation_policy = _parse_cancellation_policy(d.pop("cancellationPolicy", UNSET))


        def _parse_cancellation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancellation = _parse_cancellation(d.pop("cancellation", UNSET))


        def _parse_allows_children(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allows_children = _parse_allows_children(d.pop("allowsChildren", UNSET))


        def _parse_allows_infants(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allows_infants = _parse_allows_infants(d.pop("allowsInfants", UNSET))


        def _parse_allows_pets(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allows_pets = _parse_allows_pets(d.pop("allowsPets", UNSET))


        def _parse_allows_smoking(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allows_smoking = _parse_allows_smoking(d.pop("allowsSmoking", UNSET))


        def _parse_allows_events(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        allows_events = _parse_allows_events(d.pop("allowsEvents", UNSET))


        def _parse_quiet_hours_start(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quiet_hours_start = _parse_quiet_hours_start(d.pop("quietHoursStart", UNSET))


        def _parse_quiet_hours_end(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        quiet_hours_end = _parse_quiet_hours_end(d.pop("quietHoursEnd", UNSET))


        _check_in_method = d.pop("checkInMethod", UNSET)
        check_in_method: ListingContentUpdateRequestPoliciesCheckInMethod | Unset
        if isinstance(_check_in_method,  Unset):
            check_in_method = UNSET
        else:
            check_in_method = ListingContentUpdateRequestPoliciesCheckInMethod(_check_in_method)




        def _parse_check_in_instruction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_in_instruction = _parse_check_in_instruction(d.pop("checkInInstruction", UNSET))


        def _parse_guest_safety_disclosures(data: object) -> list[AirbnbSafetyDisclosure] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                guest_safety_disclosures_type_0 = []
                _guest_safety_disclosures_type_0 = data
                for guest_safety_disclosures_type_0_item_data in (_guest_safety_disclosures_type_0):
                    guest_safety_disclosures_type_0_item = AirbnbSafetyDisclosure.from_dict(guest_safety_disclosures_type_0_item_data)



                    guest_safety_disclosures_type_0.append(guest_safety_disclosures_type_0_item)

                return guest_safety_disclosures_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AirbnbSafetyDisclosure] | None | Unset, data)

        guest_safety_disclosures = _parse_guest_safety_disclosures(d.pop("guestSafetyDisclosures", UNSET))


        listing_content_update_request_policies = cls(
            check_in_time_start=check_in_time_start,
            check_in_time_end=check_in_time_end,
            check_out_time=check_out_time,
            house_rules=house_rules,
            cancellation_policy=cancellation_policy,
            cancellation=cancellation,
            allows_children=allows_children,
            allows_infants=allows_infants,
            allows_pets=allows_pets,
            allows_smoking=allows_smoking,
            allows_events=allows_events,
            quiet_hours_start=quiet_hours_start,
            quiet_hours_end=quiet_hours_end,
            check_in_method=check_in_method,
            check_in_instruction=check_in_instruction,
            guest_safety_disclosures=guest_safety_disclosures,
        )


        listing_content_update_request_policies.additional_properties = d
        return listing_content_update_request_policies

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
