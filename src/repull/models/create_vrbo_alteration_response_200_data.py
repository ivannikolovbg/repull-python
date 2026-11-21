from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_vrbo_alteration_response_200_data_after import CreateVrboAlterationResponse200DataAfter
  from ..models.create_vrbo_alteration_response_200_data_before import CreateVrboAlterationResponse200DataBefore
  from ..models.create_vrbo_alteration_response_200_data_due_date import CreateVrboAlterationResponse200DataDueDate
  from ..models.create_vrbo_alteration_response_200_data_payment_type_0 import CreateVrboAlterationResponse200DataPaymentType0





T = TypeVar("T", bound="CreateVrboAlterationResponse200Data")



@_attrs_define
class CreateVrboAlterationResponse200Data:
    """ 
        Attributes:
            confirmation_code (str | Unset):
            preview (bool | Unset):
            before (CreateVrboAlterationResponse200DataBefore | Unset):
            after (CreateVrboAlterationResponse200DataAfter | Unset):
            price_unchanged (bool | Unset):
            payment (CreateVrboAlterationResponse200DataPaymentType0 | None | Unset):
            due_date (CreateVrboAlterationResponse200DataDueDate | Unset):
     """

    confirmation_code: str | Unset = UNSET
    preview: bool | Unset = UNSET
    before: CreateVrboAlterationResponse200DataBefore | Unset = UNSET
    after: CreateVrboAlterationResponse200DataAfter | Unset = UNSET
    price_unchanged: bool | Unset = UNSET
    payment: CreateVrboAlterationResponse200DataPaymentType0 | None | Unset = UNSET
    due_date: CreateVrboAlterationResponse200DataDueDate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_vrbo_alteration_response_200_data_after import CreateVrboAlterationResponse200DataAfter
        from ..models.create_vrbo_alteration_response_200_data_before import CreateVrboAlterationResponse200DataBefore
        from ..models.create_vrbo_alteration_response_200_data_due_date import CreateVrboAlterationResponse200DataDueDate
        from ..models.create_vrbo_alteration_response_200_data_payment_type_0 import CreateVrboAlterationResponse200DataPaymentType0
        confirmation_code = self.confirmation_code

        preview = self.preview

        before: dict[str, Any] | Unset = UNSET
        if not isinstance(self.before, Unset):
            before = self.before.to_dict()

        after: dict[str, Any] | Unset = UNSET
        if not isinstance(self.after, Unset):
            after = self.after.to_dict()

        price_unchanged = self.price_unchanged

        payment: dict[str, Any] | None | Unset
        if isinstance(self.payment, Unset):
            payment = UNSET
        elif isinstance(self.payment, CreateVrboAlterationResponse200DataPaymentType0):
            payment = self.payment.to_dict()
        else:
            payment = self.payment

        due_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if preview is not UNSET:
            field_dict["preview"] = preview
        if before is not UNSET:
            field_dict["before"] = before
        if after is not UNSET:
            field_dict["after"] = after
        if price_unchanged is not UNSET:
            field_dict["priceUnchanged"] = price_unchanged
        if payment is not UNSET:
            field_dict["payment"] = payment
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_vrbo_alteration_response_200_data_after import CreateVrboAlterationResponse200DataAfter
        from ..models.create_vrbo_alteration_response_200_data_before import CreateVrboAlterationResponse200DataBefore
        from ..models.create_vrbo_alteration_response_200_data_due_date import CreateVrboAlterationResponse200DataDueDate
        from ..models.create_vrbo_alteration_response_200_data_payment_type_0 import CreateVrboAlterationResponse200DataPaymentType0
        d = dict(src_dict)
        confirmation_code = d.pop("confirmationCode", UNSET)

        preview = d.pop("preview", UNSET)

        _before = d.pop("before", UNSET)
        before: CreateVrboAlterationResponse200DataBefore | Unset
        if isinstance(_before,  Unset):
            before = UNSET
        else:
            before = CreateVrboAlterationResponse200DataBefore.from_dict(_before)




        _after = d.pop("after", UNSET)
        after: CreateVrboAlterationResponse200DataAfter | Unset
        if isinstance(_after,  Unset):
            after = UNSET
        else:
            after = CreateVrboAlterationResponse200DataAfter.from_dict(_after)




        price_unchanged = d.pop("priceUnchanged", UNSET)

        def _parse_payment(data: object) -> CreateVrboAlterationResponse200DataPaymentType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_type_0 = CreateVrboAlterationResponse200DataPaymentType0.from_dict(data)



                return payment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateVrboAlterationResponse200DataPaymentType0 | None | Unset, data)

        payment = _parse_payment(d.pop("payment", UNSET))


        _due_date = d.pop("dueDate", UNSET)
        due_date: CreateVrboAlterationResponse200DataDueDate | Unset
        if isinstance(_due_date,  Unset):
            due_date = UNSET
        else:
            due_date = CreateVrboAlterationResponse200DataDueDate.from_dict(_due_date)




        create_vrbo_alteration_response_200_data = cls(
            confirmation_code=confirmation_code,
            preview=preview,
            before=before,
            after=after,
            price_unchanged=price_unchanged,
            payment=payment,
            due_date=due_date,
        )


        create_vrbo_alteration_response_200_data.additional_properties = d
        return create_vrbo_alteration_response_200_data

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
