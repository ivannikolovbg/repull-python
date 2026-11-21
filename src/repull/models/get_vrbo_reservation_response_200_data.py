from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_reservation_response_200_data_available_actions_item import GetVrboReservationResponse200DataAvailableActionsItem
  from ..models.get_vrbo_reservation_response_200_data_guest_lines_item import GetVrboReservationResponse200DataGuestLinesItem
  from ..models.get_vrbo_reservation_response_200_data_host_lines_item import GetVrboReservationResponse200DataHostLinesItem





T = TypeVar("T", bound="GetVrboReservationResponse200Data")



@_attrs_define
class GetVrboReservationResponse200Data:
    """ The booking as Vrbo shows it; with `?options=`, Vrbo's choices for that action.

        Attributes:
            reservation_code (str | Unset):
            reservation_uuid (str | Unset):
            state (None | str | Unset):
            check_in (None | str | Unset):
            check_out (None | str | Unset):
            adults (int | None | Unset):
            children (int | None | Unset):
            pets (int | None | Unset):
            guest_name (None | str | Unset):
            currency (None | str | Unset):
            guest_lines (list[GetVrboReservationResponse200DataGuestLinesItem] | Unset):
            host_lines (list[GetVrboReservationResponse200DataHostLinesItem] | Unset):
            total_guest_payment (float | None | Unset):
            payout (float | None | Unset):
            cancellation_policy (None | str | Unset):
            damage_deposit (float | None | Unset):
            available_actions (list[GetVrboReservationResponse200DataAvailableActionsItem] | Unset):
     """

    reservation_code: str | Unset = UNSET
    reservation_uuid: str | Unset = UNSET
    state: None | str | Unset = UNSET
    check_in: None | str | Unset = UNSET
    check_out: None | str | Unset = UNSET
    adults: int | None | Unset = UNSET
    children: int | None | Unset = UNSET
    pets: int | None | Unset = UNSET
    guest_name: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    guest_lines: list[GetVrboReservationResponse200DataGuestLinesItem] | Unset = UNSET
    host_lines: list[GetVrboReservationResponse200DataHostLinesItem] | Unset = UNSET
    total_guest_payment: float | None | Unset = UNSET
    payout: float | None | Unset = UNSET
    cancellation_policy: None | str | Unset = UNSET
    damage_deposit: float | None | Unset = UNSET
    available_actions: list[GetVrboReservationResponse200DataAvailableActionsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_reservation_response_200_data_available_actions_item import GetVrboReservationResponse200DataAvailableActionsItem
        from ..models.get_vrbo_reservation_response_200_data_guest_lines_item import GetVrboReservationResponse200DataGuestLinesItem
        from ..models.get_vrbo_reservation_response_200_data_host_lines_item import GetVrboReservationResponse200DataHostLinesItem
        reservation_code = self.reservation_code

        reservation_uuid = self.reservation_uuid

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        check_in: None | str | Unset
        if isinstance(self.check_in, Unset):
            check_in = UNSET
        else:
            check_in = self.check_in

        check_out: None | str | Unset
        if isinstance(self.check_out, Unset):
            check_out = UNSET
        else:
            check_out = self.check_out

        adults: int | None | Unset
        if isinstance(self.adults, Unset):
            adults = UNSET
        else:
            adults = self.adults

        children: int | None | Unset
        if isinstance(self.children, Unset):
            children = UNSET
        else:
            children = self.children

        pets: int | None | Unset
        if isinstance(self.pets, Unset):
            pets = UNSET
        else:
            pets = self.pets

        guest_name: None | str | Unset
        if isinstance(self.guest_name, Unset):
            guest_name = UNSET
        else:
            guest_name = self.guest_name

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        guest_lines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.guest_lines, Unset):
            guest_lines = []
            for guest_lines_item_data in self.guest_lines:
                guest_lines_item = guest_lines_item_data.to_dict()
                guest_lines.append(guest_lines_item)



        host_lines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.host_lines, Unset):
            host_lines = []
            for host_lines_item_data in self.host_lines:
                host_lines_item = host_lines_item_data.to_dict()
                host_lines.append(host_lines_item)



        total_guest_payment: float | None | Unset
        if isinstance(self.total_guest_payment, Unset):
            total_guest_payment = UNSET
        else:
            total_guest_payment = self.total_guest_payment

        payout: float | None | Unset
        if isinstance(self.payout, Unset):
            payout = UNSET
        else:
            payout = self.payout

        cancellation_policy: None | str | Unset
        if isinstance(self.cancellation_policy, Unset):
            cancellation_policy = UNSET
        else:
            cancellation_policy = self.cancellation_policy

        damage_deposit: float | None | Unset
        if isinstance(self.damage_deposit, Unset):
            damage_deposit = UNSET
        else:
            damage_deposit = self.damage_deposit

        available_actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.available_actions, Unset):
            available_actions = []
            for available_actions_item_data in self.available_actions:
                available_actions_item = available_actions_item_data.to_dict()
                available_actions.append(available_actions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reservation_code is not UNSET:
            field_dict["reservationCode"] = reservation_code
        if reservation_uuid is not UNSET:
            field_dict["reservationUuid"] = reservation_uuid
        if state is not UNSET:
            field_dict["state"] = state
        if check_in is not UNSET:
            field_dict["checkIn"] = check_in
        if check_out is not UNSET:
            field_dict["checkOut"] = check_out
        if adults is not UNSET:
            field_dict["adults"] = adults
        if children is not UNSET:
            field_dict["children"] = children
        if pets is not UNSET:
            field_dict["pets"] = pets
        if guest_name is not UNSET:
            field_dict["guestName"] = guest_name
        if currency is not UNSET:
            field_dict["currency"] = currency
        if guest_lines is not UNSET:
            field_dict["guestLines"] = guest_lines
        if host_lines is not UNSET:
            field_dict["hostLines"] = host_lines
        if total_guest_payment is not UNSET:
            field_dict["totalGuestPayment"] = total_guest_payment
        if payout is not UNSET:
            field_dict["payout"] = payout
        if cancellation_policy is not UNSET:
            field_dict["cancellationPolicy"] = cancellation_policy
        if damage_deposit is not UNSET:
            field_dict["damageDeposit"] = damage_deposit
        if available_actions is not UNSET:
            field_dict["availableActions"] = available_actions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_reservation_response_200_data_available_actions_item import GetVrboReservationResponse200DataAvailableActionsItem
        from ..models.get_vrbo_reservation_response_200_data_guest_lines_item import GetVrboReservationResponse200DataGuestLinesItem
        from ..models.get_vrbo_reservation_response_200_data_host_lines_item import GetVrboReservationResponse200DataHostLinesItem
        d = dict(src_dict)
        reservation_code = d.pop("reservationCode", UNSET)

        reservation_uuid = d.pop("reservationUuid", UNSET)

        def _parse_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        state = _parse_state(d.pop("state", UNSET))


        def _parse_check_in(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_in = _parse_check_in(d.pop("checkIn", UNSET))


        def _parse_check_out(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_out = _parse_check_out(d.pop("checkOut", UNSET))


        def _parse_adults(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        adults = _parse_adults(d.pop("adults", UNSET))


        def _parse_children(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        children = _parse_children(d.pop("children", UNSET))


        def _parse_pets(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pets = _parse_pets(d.pop("pets", UNSET))


        def _parse_guest_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_name = _parse_guest_name(d.pop("guestName", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        _guest_lines = d.pop("guestLines", UNSET)
        guest_lines: list[GetVrboReservationResponse200DataGuestLinesItem] | Unset = UNSET
        if _guest_lines is not UNSET:
            guest_lines = []
            for guest_lines_item_data in _guest_lines:
                guest_lines_item = GetVrboReservationResponse200DataGuestLinesItem.from_dict(guest_lines_item_data)



                guest_lines.append(guest_lines_item)


        _host_lines = d.pop("hostLines", UNSET)
        host_lines: list[GetVrboReservationResponse200DataHostLinesItem] | Unset = UNSET
        if _host_lines is not UNSET:
            host_lines = []
            for host_lines_item_data in _host_lines:
                host_lines_item = GetVrboReservationResponse200DataHostLinesItem.from_dict(host_lines_item_data)



                host_lines.append(host_lines_item)


        def _parse_total_guest_payment(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_guest_payment = _parse_total_guest_payment(d.pop("totalGuestPayment", UNSET))


        def _parse_payout(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        payout = _parse_payout(d.pop("payout", UNSET))


        def _parse_cancellation_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cancellation_policy = _parse_cancellation_policy(d.pop("cancellationPolicy", UNSET))


        def _parse_damage_deposit(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        damage_deposit = _parse_damage_deposit(d.pop("damageDeposit", UNSET))


        _available_actions = d.pop("availableActions", UNSET)
        available_actions: list[GetVrboReservationResponse200DataAvailableActionsItem] | Unset = UNSET
        if _available_actions is not UNSET:
            available_actions = []
            for available_actions_item_data in _available_actions:
                available_actions_item = GetVrboReservationResponse200DataAvailableActionsItem.from_dict(available_actions_item_data)



                available_actions.append(available_actions_item)


        get_vrbo_reservation_response_200_data = cls(
            reservation_code=reservation_code,
            reservation_uuid=reservation_uuid,
            state=state,
            check_in=check_in,
            check_out=check_out,
            adults=adults,
            children=children,
            pets=pets,
            guest_name=guest_name,
            currency=currency,
            guest_lines=guest_lines,
            host_lines=host_lines,
            total_guest_payment=total_guest_payment,
            payout=payout,
            cancellation_policy=cancellation_policy,
            damage_deposit=damage_deposit,
            available_actions=available_actions,
        )


        get_vrbo_reservation_response_200_data.additional_properties = d
        return get_vrbo_reservation_response_200_data

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
