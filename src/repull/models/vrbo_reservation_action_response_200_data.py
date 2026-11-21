from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.vrbo_reservation_action_response_200_data_payment_type_0 import VrboReservationActionResponse200DataPaymentType0
  from ..models.vrbo_reservation_action_response_200_data_penalties import VrboReservationActionResponse200DataPenalties
  from ..models.vrbo_reservation_action_response_200_data_terms_item import VrboReservationActionResponse200DataTermsItem





T = TypeVar("T", bound="VrboReservationActionResponse200Data")



@_attrs_define
class VrboReservationActionResponse200Data:
    """ 
        Attributes:
            action (str | Unset):
            preview (bool | Unset):
            committed (bool | Unset):
            reservation_code (str | Unset):
            refund_to_guest (None | str | Unset): `cancel`: what the guest gets back.
            penalties (VrboReservationActionResponse200DataPenalties | Unset): `cancel`: Vrbo's terms for a host
                cancellation.
            terms (list[VrboReservationActionResponse200DataTermsItem] | Unset):
            payment (None | Unset | VrboReservationActionResponse200DataPaymentType0): `charge`: the guest's payment with
                taxes.
     """

    action: str | Unset = UNSET
    preview: bool | Unset = UNSET
    committed: bool | Unset = UNSET
    reservation_code: str | Unset = UNSET
    refund_to_guest: None | str | Unset = UNSET
    penalties: VrboReservationActionResponse200DataPenalties | Unset = UNSET
    terms: list[VrboReservationActionResponse200DataTermsItem] | Unset = UNSET
    payment: None | Unset | VrboReservationActionResponse200DataPaymentType0 = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.vrbo_reservation_action_response_200_data_payment_type_0 import VrboReservationActionResponse200DataPaymentType0
        from ..models.vrbo_reservation_action_response_200_data_penalties import VrboReservationActionResponse200DataPenalties
        from ..models.vrbo_reservation_action_response_200_data_terms_item import VrboReservationActionResponse200DataTermsItem
        action = self.action

        preview = self.preview

        committed = self.committed

        reservation_code = self.reservation_code

        refund_to_guest: None | str | Unset
        if isinstance(self.refund_to_guest, Unset):
            refund_to_guest = UNSET
        else:
            refund_to_guest = self.refund_to_guest

        penalties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.penalties, Unset):
            penalties = self.penalties.to_dict()

        terms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.terms, Unset):
            terms = []
            for terms_item_data in self.terms:
                terms_item = terms_item_data.to_dict()
                terms.append(terms_item)



        payment: dict[str, Any] | None | Unset
        if isinstance(self.payment, Unset):
            payment = UNSET
        elif isinstance(self.payment, VrboReservationActionResponse200DataPaymentType0):
            payment = self.payment.to_dict()
        else:
            payment = self.payment


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if action is not UNSET:
            field_dict["action"] = action
        if preview is not UNSET:
            field_dict["preview"] = preview
        if committed is not UNSET:
            field_dict["committed"] = committed
        if reservation_code is not UNSET:
            field_dict["reservationCode"] = reservation_code
        if refund_to_guest is not UNSET:
            field_dict["refundToGuest"] = refund_to_guest
        if penalties is not UNSET:
            field_dict["penalties"] = penalties
        if terms is not UNSET:
            field_dict["terms"] = terms
        if payment is not UNSET:
            field_dict["payment"] = payment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vrbo_reservation_action_response_200_data_payment_type_0 import VrboReservationActionResponse200DataPaymentType0
        from ..models.vrbo_reservation_action_response_200_data_penalties import VrboReservationActionResponse200DataPenalties
        from ..models.vrbo_reservation_action_response_200_data_terms_item import VrboReservationActionResponse200DataTermsItem
        d = dict(src_dict)
        action = d.pop("action", UNSET)

        preview = d.pop("preview", UNSET)

        committed = d.pop("committed", UNSET)

        reservation_code = d.pop("reservationCode", UNSET)

        def _parse_refund_to_guest(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refund_to_guest = _parse_refund_to_guest(d.pop("refundToGuest", UNSET))


        _penalties = d.pop("penalties", UNSET)
        penalties: VrboReservationActionResponse200DataPenalties | Unset
        if isinstance(_penalties,  Unset):
            penalties = UNSET
        else:
            penalties = VrboReservationActionResponse200DataPenalties.from_dict(_penalties)




        _terms = d.pop("terms", UNSET)
        terms: list[VrboReservationActionResponse200DataTermsItem] | Unset = UNSET
        if _terms is not UNSET:
            terms = []
            for terms_item_data in _terms:
                terms_item = VrboReservationActionResponse200DataTermsItem.from_dict(terms_item_data)



                terms.append(terms_item)


        def _parse_payment(data: object) -> None | Unset | VrboReservationActionResponse200DataPaymentType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_type_0 = VrboReservationActionResponse200DataPaymentType0.from_dict(data)



                return payment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VrboReservationActionResponse200DataPaymentType0, data)

        payment = _parse_payment(d.pop("payment", UNSET))


        vrbo_reservation_action_response_200_data = cls(
            action=action,
            preview=preview,
            committed=committed,
            reservation_code=reservation_code,
            refund_to_guest=refund_to_guest,
            penalties=penalties,
            terms=terms,
            payment=payment,
        )


        vrbo_reservation_action_response_200_data.additional_properties = d
        return vrbo_reservation_action_response_200_data

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
