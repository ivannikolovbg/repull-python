from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_payment_terms_response_200_data_payments_item import UpdateVrboListingPaymentTermsResponse200DataPaymentsItem





T = TypeVar("T", bound="UpdateVrboListingPaymentTermsResponse200Data")



@_attrs_define
class UpdateVrboListingPaymentTermsResponse200Data:
    """ What Vrbo has stored for the section, read back after the write.

        Attributes:
            percent_due_now (float | None | Unset):
            payments (list[UpdateVrboListingPaymentTermsResponse200DataPaymentsItem] | Unset):
     """

    percent_due_now: float | None | Unset = UNSET
    payments: list[UpdateVrboListingPaymentTermsResponse200DataPaymentsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_payment_terms_response_200_data_payments_item import UpdateVrboListingPaymentTermsResponse200DataPaymentsItem
        percent_due_now: float | None | Unset
        if isinstance(self.percent_due_now, Unset):
            percent_due_now = UNSET
        else:
            percent_due_now = self.percent_due_now

        payments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.payments, Unset):
            payments = []
            for payments_item_data in self.payments:
                payments_item = payments_item_data.to_dict()
                payments.append(payments_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if percent_due_now is not UNSET:
            field_dict["percentDueNow"] = percent_due_now
        if payments is not UNSET:
            field_dict["payments"] = payments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_payment_terms_response_200_data_payments_item import UpdateVrboListingPaymentTermsResponse200DataPaymentsItem
        d = dict(src_dict)
        def _parse_percent_due_now(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        percent_due_now = _parse_percent_due_now(d.pop("percentDueNow", UNSET))


        _payments = d.pop("payments", UNSET)
        payments: list[UpdateVrboListingPaymentTermsResponse200DataPaymentsItem] | Unset = UNSET
        if _payments is not UNSET:
            payments = []
            for payments_item_data in _payments:
                payments_item = UpdateVrboListingPaymentTermsResponse200DataPaymentsItem.from_dict(payments_item_data)



                payments.append(payments_item)


        update_vrbo_listing_payment_terms_response_200_data = cls(
            percent_due_now=percent_due_now,
            payments=payments,
        )


        update_vrbo_listing_payment_terms_response_200_data.additional_properties = d
        return update_vrbo_listing_payment_terms_response_200_data

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
