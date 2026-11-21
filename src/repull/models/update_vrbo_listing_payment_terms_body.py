from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_payment_terms_body_payments_item import UpdateVrboListingPaymentTermsBodyPaymentsItem





T = TypeVar("T", bound="UpdateVrboListingPaymentTermsBody")



@_attrs_define
class UpdateVrboListingPaymentTermsBody:
    """ 
        Attributes:
            percent_due_now (float):
            payments (list[UpdateVrboListingPaymentTermsBodyPaymentsItem] | Unset):
     """

    percent_due_now: float
    payments: list[UpdateVrboListingPaymentTermsBodyPaymentsItem] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_payment_terms_body_payments_item import UpdateVrboListingPaymentTermsBodyPaymentsItem
        percent_due_now = self.percent_due_now

        payments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.payments, Unset):
            payments = []
            for payments_item_data in self.payments:
                payments_item = payments_item_data.to_dict()
                payments.append(payments_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "percentDueNow": percent_due_now,
        })
        if payments is not UNSET:
            field_dict["payments"] = payments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_payment_terms_body_payments_item import UpdateVrboListingPaymentTermsBodyPaymentsItem
        d = dict(src_dict)
        percent_due_now = d.pop("percentDueNow")

        _payments = d.pop("payments", UNSET)
        payments: list[UpdateVrboListingPaymentTermsBodyPaymentsItem] | Unset = UNSET
        if _payments is not UNSET:
            payments = []
            for payments_item_data in _payments:
                payments_item = UpdateVrboListingPaymentTermsBodyPaymentsItem.from_dict(payments_item_data)



                payments.append(payments_item)


        update_vrbo_listing_payment_terms_body = cls(
            percent_due_now=percent_due_now,
            payments=payments,
        )

        return update_vrbo_listing_payment_terms_body

