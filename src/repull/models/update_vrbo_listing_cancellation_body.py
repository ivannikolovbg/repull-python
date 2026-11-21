from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_cancellation_body_tiers_item import UpdateVrboListingCancellationBodyTiersItem





T = TypeVar("T", bound="UpdateVrboListingCancellationBody")



@_attrs_define
class UpdateVrboListingCancellationBody:
    """ 
        Attributes:
            policy_type (str): POLICY_TYPE_VR_RELAXED (14/7 days), _MODERATE (30/14), _FIRM (60/30), _STRICT (60), … or
                POLICY_TYPE_CUSTOM with `tiers`. The read lists Vrbo's named policies in `options`. Example:
                POLICY_TYPE_VR_MODERATE.
            tiers (list[UpdateVrboListingCancellationBodyTiersItem] | Unset):
     """

    policy_type: str
    tiers: list[UpdateVrboListingCancellationBodyTiersItem] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_cancellation_body_tiers_item import UpdateVrboListingCancellationBodyTiersItem
        policy_type = self.policy_type

        tiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tiers, Unset):
            tiers = []
            for tiers_item_data in self.tiers:
                tiers_item = tiers_item_data.to_dict()
                tiers.append(tiers_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "policyType": policy_type,
        })
        if tiers is not UNSET:
            field_dict["tiers"] = tiers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_cancellation_body_tiers_item import UpdateVrboListingCancellationBodyTiersItem
        d = dict(src_dict)
        policy_type = d.pop("policyType")

        _tiers = d.pop("tiers", UNSET)
        tiers: list[UpdateVrboListingCancellationBodyTiersItem] | Unset = UNSET
        if _tiers is not UNSET:
            tiers = []
            for tiers_item_data in _tiers:
                tiers_item = UpdateVrboListingCancellationBodyTiersItem.from_dict(tiers_item_data)



                tiers.append(tiers_item)


        update_vrbo_listing_cancellation_body = cls(
            policy_type=policy_type,
            tiers=tiers,
        )

        return update_vrbo_listing_cancellation_body

