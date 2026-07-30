from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_airbnb_offer_body_type import CreateAirbnbOfferBodyType
from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateAirbnbOfferBody")



@_attrs_define
class CreateAirbnbOfferBody:
    """ 
        Attributes:
            type_ (CreateAirbnbOfferBodyType): Which kind of offer to create.
            thread_id (str | Unset): Airbnb thread id. Required when `type` is `preapproval`.
            block_instant_booking (bool | Unset): For `preapproval` — whether to block instant booking. Default: False.
     """

    type_: CreateAirbnbOfferBodyType
    thread_id: str | Unset = UNSET
    block_instant_booking: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        thread_id = self.thread_id

        block_instant_booking = self.block_instant_booking


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if thread_id is not UNSET:
            field_dict["threadId"] = thread_id
        if block_instant_booking is not UNSET:
            field_dict["blockInstantBooking"] = block_instant_booking

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = CreateAirbnbOfferBodyType(d.pop("type"))




        thread_id = d.pop("threadId", UNSET)

        block_instant_booking = d.pop("blockInstantBooking", UNSET)

        create_airbnb_offer_body = cls(
            type_=type_,
            thread_id=thread_id,
            block_instant_booking=block_instant_booking,
        )


        create_airbnb_offer_body.additional_properties = d
        return create_airbnb_offer_body

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
