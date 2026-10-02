from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_pricing_write_request_fees_type_0_item_amount_type import AirbnbPricingWriteRequestFeesType0ItemAmountType
from ..models.airbnb_pricing_write_request_fees_type_0_item_charge_period import AirbnbPricingWriteRequestFeesType0ItemChargePeriod
from ..models.airbnb_pricing_write_request_fees_type_0_item_charge_type import AirbnbPricingWriteRequestFeesType0ItemChargeType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AirbnbPricingWriteRequestFeesType0Item")



@_attrs_define
class AirbnbPricingWriteRequestFeesType0Item:
    """ 
        Attributes:
            fee_type (str): Airbnb fee type: `PASS_THROUGH_CLEANING_FEE`, `PASS_THROUGH_SHORT_TERM_CLEANING_FEE`,
                `PASS_THROUGH_PET_FEE`, `PASS_THROUGH_SECURITY_DEPOSIT`, `PASS_THROUGH_MANAGEMENT_FEE`,
                `PASS_THROUGH_RESORT_FEE`, `PASS_THROUGH_COMMUNITY_FEE`, `PASS_THROUGH_LINEN_FEE`. Example:
                PASS_THROUGH_MANAGEMENT_FEE.
            amount (float | None): `null` removes the fee. Flat: currency × 1,000,000. Percent: whole percent. Example: 10.
            amount_type (AirbnbPricingWriteRequestFeesType0ItemAmountType | Unset): Defaults to the existing fee's, else
                `flat`. Percent is accepted for management and resort fees.
            charge_type (AirbnbPricingWriteRequestFeesType0ItemChargeType | Unset): Who it is charged per. Defaults to the
                existing fee's, else `PER_GROUP`.
            charge_period (AirbnbPricingWriteRequestFeesType0ItemChargePeriod | Unset): Once per booking or per night.
                Defaults to the existing fee's, else `PER_BOOKING`.
            offline (bool | Unset): Collected offline by the host rather than through Airbnb. Default `false`.
     """

    fee_type: str
    amount: float | None
    amount_type: AirbnbPricingWriteRequestFeesType0ItemAmountType | Unset = UNSET
    charge_type: AirbnbPricingWriteRequestFeesType0ItemChargeType | Unset = UNSET
    charge_period: AirbnbPricingWriteRequestFeesType0ItemChargePeriod | Unset = UNSET
    offline: bool | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        fee_type = self.fee_type

        amount: float | None
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

        field_dict.update({
            "fee_type": fee_type,
            "amount": amount,
        })
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
        fee_type = d.pop("fee_type")

        def _parse_amount(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        amount = _parse_amount(d.pop("amount"))


        _amount_type = d.pop("amount_type", UNSET)
        amount_type: AirbnbPricingWriteRequestFeesType0ItemAmountType | Unset
        if isinstance(_amount_type,  Unset):
            amount_type = UNSET
        else:
            amount_type = AirbnbPricingWriteRequestFeesType0ItemAmountType(_amount_type)




        _charge_type = d.pop("charge_type", UNSET)
        charge_type: AirbnbPricingWriteRequestFeesType0ItemChargeType | Unset
        if isinstance(_charge_type,  Unset):
            charge_type = UNSET
        else:
            charge_type = AirbnbPricingWriteRequestFeesType0ItemChargeType(_charge_type)




        _charge_period = d.pop("charge_period", UNSET)
        charge_period: AirbnbPricingWriteRequestFeesType0ItemChargePeriod | Unset
        if isinstance(_charge_period,  Unset):
            charge_period = UNSET
        else:
            charge_period = AirbnbPricingWriteRequestFeesType0ItemChargePeriod(_charge_period)




        offline = d.pop("offline", UNSET)

        airbnb_pricing_write_request_fees_type_0_item = cls(
            fee_type=fee_type,
            amount=amount,
            amount_type=amount_type,
            charge_type=charge_type,
            charge_period=charge_period,
            offline=offline,
        )

        return airbnb_pricing_write_request_fees_type_0_item

