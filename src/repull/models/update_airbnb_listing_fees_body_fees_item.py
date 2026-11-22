from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_airbnb_listing_fees_body_fees_item_amount_type import UpdateAirbnbListingFeesBodyFeesItemAmountType
from ..models.update_airbnb_listing_fees_body_fees_item_charge_period import UpdateAirbnbListingFeesBodyFeesItemChargePeriod
from ..models.update_airbnb_listing_fees_body_fees_item_charge_type import UpdateAirbnbListingFeesBodyFeesItemChargeType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateAirbnbListingFeesBodyFeesItem")



@_attrs_define
class UpdateAirbnbListingFeesBodyFeesItem:
    """ 
        Attributes:
            fee_type (str | Unset):  Example: PASS_THROUGH_CLEANING_FEE.
            amount (float | None | Unset):
            amount_type (UpdateAirbnbListingFeesBodyFeesItemAmountType | Unset):
            charge_type (UpdateAirbnbListingFeesBodyFeesItemChargeType | Unset):
            charge_period (UpdateAirbnbListingFeesBodyFeesItemChargePeriod | Unset):
            offline (bool | Unset):
     """

    fee_type: str | Unset = UNSET
    amount: float | None | Unset = UNSET
    amount_type: UpdateAirbnbListingFeesBodyFeesItemAmountType | Unset = UNSET
    charge_type: UpdateAirbnbListingFeesBodyFeesItemChargeType | Unset = UNSET
    charge_period: UpdateAirbnbListingFeesBodyFeesItemChargePeriod | Unset = UNSET
    offline: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        fee_type = self.fee_type

        amount: float | None | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        amount_type: str | Unset = UNSET
        if not isinstance(self.amount_type, Unset):
            amount_type = self.amount_type.value


        charge_type: str | Unset = UNSET
        if not isinstance(self.charge_type, Unset):
            charge_type = self.charge_type.value


        charge_period: str | Unset = UNSET
        if not isinstance(self.charge_period, Unset):
            charge_period = self.charge_period.value


        offline = self.offline


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fee_type is not UNSET:
            field_dict["fee_type"] = fee_type
        if amount is not UNSET:
            field_dict["amount"] = amount
        if amount_type is not UNSET:
            field_dict["amount_type"] = amount_type
        if charge_type is not UNSET:
            field_dict["charge_type"] = charge_type
        if charge_period is not UNSET:
            field_dict["charge_period"] = charge_period
        if offline is not UNSET:
            field_dict["offline"] = offline

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fee_type = d.pop("fee_type", UNSET)

        def _parse_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))


        _amount_type = d.pop("amount_type", UNSET)
        amount_type: UpdateAirbnbListingFeesBodyFeesItemAmountType | Unset
        if isinstance(_amount_type,  Unset):
            amount_type = UNSET
        else:
            amount_type = UpdateAirbnbListingFeesBodyFeesItemAmountType(_amount_type)




        _charge_type = d.pop("charge_type", UNSET)
        charge_type: UpdateAirbnbListingFeesBodyFeesItemChargeType | Unset
        if isinstance(_charge_type,  Unset):
            charge_type = UNSET
        else:
            charge_type = UpdateAirbnbListingFeesBodyFeesItemChargeType(_charge_type)




        _charge_period = d.pop("charge_period", UNSET)
        charge_period: UpdateAirbnbListingFeesBodyFeesItemChargePeriod | Unset
        if isinstance(_charge_period,  Unset):
            charge_period = UNSET
        else:
            charge_period = UpdateAirbnbListingFeesBodyFeesItemChargePeriod(_charge_period)




        offline = d.pop("offline", UNSET)

        update_airbnb_listing_fees_body_fees_item = cls(
            fee_type=fee_type,
            amount=amount,
            amount_type=amount_type,
            charge_type=charge_type,
            charge_period=charge_period,
            offline=offline,
        )


        update_airbnb_listing_fees_body_fees_item.additional_properties = d
        return update_airbnb_listing_fees_body_fees_item

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
