from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_protection_body_damage_deposit_type_0 import UpdateVrboListingProtectionBodyDamageDepositType0





T = TypeVar("T", bound="UpdateVrboListingProtectionBody")



@_attrs_define
class UpdateVrboListingProtectionBody:
    """ 
        Attributes:
            damage_deposit (float | None | Unset | UpdateVrboListingProtectionBodyDamageDepositType0):
            damage_protection (Any | Unset): In Vrbo's shape, as the read returns it.
     """

    damage_deposit: float | None | Unset | UpdateVrboListingProtectionBodyDamageDepositType0 = UNSET
    damage_protection: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_protection_body_damage_deposit_type_0 import UpdateVrboListingProtectionBodyDamageDepositType0
        damage_deposit: dict[str, Any] | float | None | Unset
        if isinstance(self.damage_deposit, Unset):
            damage_deposit = UNSET
        elif isinstance(self.damage_deposit, UpdateVrboListingProtectionBodyDamageDepositType0):
            damage_deposit = self.damage_deposit.to_dict()
        else:
            damage_deposit = self.damage_deposit

        damage_protection = self.damage_protection


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if damage_deposit is not UNSET:
            field_dict["damageDeposit"] = damage_deposit
        if damage_protection is not UNSET:
            field_dict["damageProtection"] = damage_protection

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_protection_body_damage_deposit_type_0 import UpdateVrboListingProtectionBodyDamageDepositType0
        d = dict(src_dict)
        def _parse_damage_deposit(data: object) -> float | None | Unset | UpdateVrboListingProtectionBodyDamageDepositType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                damage_deposit_type_0 = UpdateVrboListingProtectionBodyDamageDepositType0.from_dict(data)



                return damage_deposit_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(float | None | Unset | UpdateVrboListingProtectionBodyDamageDepositType0, data)

        damage_deposit = _parse_damage_deposit(d.pop("damageDeposit", UNSET))


        damage_protection = d.pop("damageProtection", UNSET)

        update_vrbo_listing_protection_body = cls(
            damage_deposit=damage_deposit,
            damage_protection=damage_protection,
        )

        return update_vrbo_listing_protection_body

