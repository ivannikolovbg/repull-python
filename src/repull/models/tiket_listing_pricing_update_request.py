from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tiket_listing_pricing_update_request_type import TiketListingPricingUpdateRequestType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tiket_ari_update import TiketAriUpdate





T = TypeVar("T", bound="TiketListingPricingUpdateRequest")



@_attrs_define
class TiketListingPricingUpdateRequest:
    """ 
        Attributes:
            updates (list[TiketAriUpdate]):
            type_ (TiketListingPricingUpdateRequestType | Unset): `availability` — rooms to sell per room type. `rates` —
                prices per room type and rate plan. `restrictions` — stay and arrival rules per room type and rate plan.
                Default: TiketListingPricingUpdateRequestType.RATES.
            hotel_id (str | Unset): tiket.com Hotel ID — only needed when the listing is mapped on more than one tiket.com
                property.
            verify (bool | Unset): Read the nights back from tiket.com after the write and report `applied`. `false` skips
                the read-back (`applied: unverified`). Default: True.
     """

    updates: list[TiketAriUpdate]
    type_: TiketListingPricingUpdateRequestType | Unset = TiketListingPricingUpdateRequestType.RATES
    hotel_id: str | Unset = UNSET
    verify: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tiket_ari_update import TiketAriUpdate
        updates = []
        for updates_item_data in self.updates:
            updates_item = updates_item_data.to_dict()
            updates.append(updates_item)



        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        hotel_id = self.hotel_id

        verify = self.verify


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "updates": updates,
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if hotel_id is not UNSET:
            field_dict["hotel_id"] = hotel_id
        if verify is not UNSET:
            field_dict["verify"] = verify

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiket_ari_update import TiketAriUpdate
        d = dict(src_dict)
        updates = []
        _updates = d.pop("updates")
        for updates_item_data in (_updates):
            updates_item = TiketAriUpdate.from_dict(updates_item_data)



            updates.append(updates_item)


        _type_ = d.pop("type", UNSET)
        type_: TiketListingPricingUpdateRequestType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = TiketListingPricingUpdateRequestType(_type_)




        hotel_id = d.pop("hotel_id", UNSET)

        verify = d.pop("verify", UNSET)

        tiket_listing_pricing_update_request = cls(
            updates=updates,
            type_=type_,
            hotel_id=hotel_id,
            verify=verify,
        )


        tiket_listing_pricing_update_request.additional_properties = d
        return tiket_listing_pricing_update_request

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
