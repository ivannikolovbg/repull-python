from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_vrbo_alteration_response_201_data_after import CreateVrboAlterationResponse201DataAfter
  from ..models.create_vrbo_alteration_response_201_data_before import CreateVrboAlterationResponse201DataBefore
  from ..models.create_vrbo_alteration_response_201_data_payment_type_0 import CreateVrboAlterationResponse201DataPaymentType0





T = TypeVar("T", bound="CreateVrboAlterationResponse201Data")



@_attrs_define
class CreateVrboAlterationResponse201Data:
    """ 
        Attributes:
            confirmation_code (str | Unset):
            preview (bool | Unset):
            committed (bool | Unset):
            before (CreateVrboAlterationResponse201DataBefore | Unset):
            after (CreateVrboAlterationResponse201DataAfter | Unset):
            payment (CreateVrboAlterationResponse201DataPaymentType0 | None | Unset):
     """

    confirmation_code: str | Unset = UNSET
    preview: bool | Unset = UNSET
    committed: bool | Unset = UNSET
    before: CreateVrboAlterationResponse201DataBefore | Unset = UNSET
    after: CreateVrboAlterationResponse201DataAfter | Unset = UNSET
    payment: CreateVrboAlterationResponse201DataPaymentType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_vrbo_alteration_response_201_data_after import CreateVrboAlterationResponse201DataAfter
        from ..models.create_vrbo_alteration_response_201_data_before import CreateVrboAlterationResponse201DataBefore
        from ..models.create_vrbo_alteration_response_201_data_payment_type_0 import CreateVrboAlterationResponse201DataPaymentType0
        confirmation_code = self.confirmation_code

        preview = self.preview

        committed = self.committed

        before: dict[str, Any] | Unset = UNSET
        if not isinstance(self.before, Unset):
            before = self.before.to_dict()

        after: dict[str, Any] | Unset = UNSET
        if not isinstance(self.after, Unset):
            after = self.after.to_dict()

        payment: dict[str, Any] | None | Unset
        if isinstance(self.payment, Unset):
            payment = UNSET
        elif isinstance(self.payment, CreateVrboAlterationResponse201DataPaymentType0):
            payment = self.payment.to_dict()
        else:
            payment = self.payment


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if preview is not UNSET:
            field_dict["preview"] = preview
        if committed is not UNSET:
            field_dict["committed"] = committed
        if before is not UNSET:
            field_dict["before"] = before
        if after is not UNSET:
            field_dict["after"] = after
        if payment is not UNSET:
            field_dict["payment"] = payment

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_vrbo_alteration_response_201_data_after import CreateVrboAlterationResponse201DataAfter
        from ..models.create_vrbo_alteration_response_201_data_before import CreateVrboAlterationResponse201DataBefore
        from ..models.create_vrbo_alteration_response_201_data_payment_type_0 import CreateVrboAlterationResponse201DataPaymentType0
        d = dict(src_dict)
        confirmation_code = d.pop("confirmationCode", UNSET)

        preview = d.pop("preview", UNSET)

        committed = d.pop("committed", UNSET)

        _before = d.pop("before", UNSET)
        before: CreateVrboAlterationResponse201DataBefore | Unset
        if isinstance(_before,  Unset):
            before = UNSET
        else:
            before = CreateVrboAlterationResponse201DataBefore.from_dict(_before)




        _after = d.pop("after", UNSET)
        after: CreateVrboAlterationResponse201DataAfter | Unset
        if isinstance(_after,  Unset):
            after = UNSET
        else:
            after = CreateVrboAlterationResponse201DataAfter.from_dict(_after)




        def _parse_payment(data: object) -> CreateVrboAlterationResponse201DataPaymentType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payment_type_0 = CreateVrboAlterationResponse201DataPaymentType0.from_dict(data)



                return payment_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateVrboAlterationResponse201DataPaymentType0 | None | Unset, data)

        payment = _parse_payment(d.pop("payment", UNSET))


        create_vrbo_alteration_response_201_data = cls(
            confirmation_code=confirmation_code,
            preview=preview,
            committed=committed,
            before=before,
            after=after,
            payment=payment,
        )


        create_vrbo_alteration_response_201_data.additional_properties = d
        return create_vrbo_alteration_response_201_data

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
