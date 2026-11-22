from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.update_airbnb_listing_fees_body_fees_item import UpdateAirbnbListingFeesBodyFeesItem





T = TypeVar("T", bound="UpdateAirbnbListingFeesBody")



@_attrs_define
class UpdateAirbnbListingFeesBody:
    """ 
        Attributes:
            fees (list[UpdateAirbnbListingFeesBodyFeesItem]):
     """

    fees: list[UpdateAirbnbListingFeesBodyFeesItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_airbnb_listing_fees_body_fees_item import UpdateAirbnbListingFeesBodyFeesItem
        fees = []
        for fees_item_data in self.fees:
            fees_item = fees_item_data.to_dict()
            fees.append(fees_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "fees": fees,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_airbnb_listing_fees_body_fees_item import UpdateAirbnbListingFeesBodyFeesItem
        d = dict(src_dict)
        fees = []
        _fees = d.pop("fees")
        for fees_item_data in (_fees):
            fees_item = UpdateAirbnbListingFeesBodyFeesItem.from_dict(fees_item_data)



            fees.append(fees_item)


        update_airbnb_listing_fees_body = cls(
            fees=fees,
        )

        return update_airbnb_listing_fees_body

