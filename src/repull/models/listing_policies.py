from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_policies_check_in import ListingPoliciesCheckIn
  from ..models.listing_policies_check_out import ListingPoliciesCheckOut
  from ..models.listing_policies_quiet_hours_type_0 import ListingPoliciesQuietHoursType0





T = TypeVar("T", bound="ListingPolicies")



@_attrs_define
class ListingPolicies:
    """ 
        Attributes:
            cancellation_policy (None | str | Unset):  Example: flexible.
            house_rules (None | str | Unset):
            check_in (ListingPoliciesCheckIn | Unset):
            check_out (ListingPoliciesCheckOut | Unset):
            allows_pets (bool | None | Unset):
            allows_smoking (bool | None | Unset):
            allows_events (bool | None | Unset):
            allows_children (bool | None | Unset):
            allows_infants (bool | None | Unset):
            children_min_age (int | None | Unset):
            quiet_hours (ListingPoliciesQuietHoursType0 | None | Unset):
            security_deposit (float | None | Unset): In the listing currency.
     """

    cancellation_policy: None | str | Unset = UNSET
    house_rules: None | str | Unset = UNSET
    check_in: ListingPoliciesCheckIn | Unset = UNSET
    check_out: ListingPoliciesCheckOut | Unset = UNSET
    allows_pets: bool | None | Unset = UNSET
    allows_smoking: bool | None | Unset = UNSET
    allows_events: bool | None | Unset = UNSET
    allows_children: bool | None | Unset = UNSET
    allows_infants: bool | None | Unset = UNSET
    children_min_age: int | None | Unset = UNSET
    quiet_hours: ListingPoliciesQuietHoursType0 | None | Unset = UNSET
    security_deposit: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_policies_check_in import ListingPoliciesCheckIn
        from ..models.listing_policies_check_out import ListingPoliciesCheckOut
        from ..models.listing_policies_quiet_hours_type_0 import ListingPoliciesQuietHoursType0
        cancellation_policy: None | str | Unset
        if isinstance(self.cancellation_policy, Unset):
            cancellation_policy = UNSET
        else:
            cancellation_policy = self.cancellation_policy

        house_rules: None | str | Unset
        if isinstance(self.house_rules, Unset):
            house_rules = UNSET
        else:
            house_rules = self.house_rules

        check_in: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_in, Unset):
            check_in = self.check_in.to_dict()

        check_out: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_out, Unset):
            check_out = self.check_out.to_dict()

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

        children_min_age: int | None | Unset
        if isinstance(self.children_min_age, Unset):
            children_min_age = UNSET
        else:
            children_min_age = self.children_min_age

        quiet_hours: dict[str, Any] | None | Unset
        if isinstance(self.quiet_hours, Unset):
            quiet_hours = UNSET
        elif isinstance(self.quiet_hours, ListingPoliciesQuietHoursType0):
            quiet_hours = self.quiet_hours.to_dict()
        else:
            quiet_hours = self.quiet_hours

        security_deposit: float | None | Unset
        if isinstance(self.security_deposit, Unset):
            security_deposit = UNSET
        else:
            security_deposit = self.security_deposit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cancellation_policy is not UNSET:
            field_dict["cancellationPolicy"] = cancellation_policy
        if house_rules is not UNSET:
            field_dict["houseRules"] = house_rules
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if allows_pets is not UNSET:
            field_dict["allowsPets"] = allows_pets
        if allows_smoking is not UNSET:
            field_dict["allowsSmoking"] = allows_smoking
        if allows_events is not UNSET:
            field_dict["allowsEvents"] = allows_events
        if allows_children is not UNSET:
            field_dict["allowsChildren"] = allows_children
        if allows_infants is not UNSET:
            field_dict["allowsInfants"] = allows_infants
        if children_min_age is not UNSET:
            field_dict["childrenMinAge"] = children_min_age
        if quiet_hours is not UNSET:
            field_dict["quietHours"] = quiet_hours
        if security_deposit is not UNSET:
            field_dict["securityDeposit"] = security_deposit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_policies_check_in import ListingPoliciesCheckIn
        from ..models.listing_policies_check_out import ListingPoliciesCheckOut
        from ..models.listing_policies_quiet_hours_type_0 import ListingPoliciesQuietHoursType0
        d = dict(src_dict)
        def _parse_cancellation_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancellation_policy = _parse_cancellation_policy(d.pop("cancellationPolicy", UNSET))


        def _parse_house_rules(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        house_rules = _parse_house_rules(d.pop("houseRules", UNSET))


        _check_in = d.pop("checkIn", UNSET)
        check_in: ListingPoliciesCheckIn | Unset
        if isinstance(_check_in,  Unset):
            check_in = UNSET
        else:
            check_in = ListingPoliciesCheckIn.from_dict(_check_in)




        _check_out = d.pop("checkOut", UNSET)
        check_out: ListingPoliciesCheckOut | Unset
        if isinstance(_check_out,  Unset):
            check_out = UNSET
        else:
            check_out = ListingPoliciesCheckOut.from_dict(_check_out)




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


        def _parse_children_min_age(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        children_min_age = _parse_children_min_age(d.pop("childrenMinAge", UNSET))


        def _parse_quiet_hours(data: object) -> ListingPoliciesQuietHoursType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                quiet_hours_type_0 = ListingPoliciesQuietHoursType0.from_dict(data)



                return quiet_hours_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingPoliciesQuietHoursType0 | None | Unset, data)

        quiet_hours = _parse_quiet_hours(d.pop("quietHours", UNSET))


        def _parse_security_deposit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        security_deposit = _parse_security_deposit(d.pop("securityDeposit", UNSET))


        listing_policies = cls(
            cancellation_policy=cancellation_policy,
            house_rules=house_rules,
            check_in=check_in,
            check_out=check_out,
            allows_pets=allows_pets,
            allows_smoking=allows_smoking,
            allows_events=allows_events,
            allows_children=allows_children,
            allows_infants=allows_infants,
            children_min_age=children_min_age,
            quiet_hours=quiet_hours,
            security_deposit=security_deposit,
        )


        listing_policies.additional_properties = d
        return listing_policies

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
