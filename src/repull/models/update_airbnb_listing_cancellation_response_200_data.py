from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_airbnb_listing_cancellation_response_200_data_cancellation import UpdateAirbnbListingCancellationResponse200DataCancellation





T = TypeVar("T", bound="UpdateAirbnbListingCancellationResponse200Data")



@_attrs_define
class UpdateAirbnbListingCancellationResponse200Data:
    """ 
        Attributes:
            applied (list[str] | Unset):
            cancellation (UpdateAirbnbListingCancellationResponse200DataCancellation | Unset):
     """

    applied: list[str] | Unset = UNSET
    cancellation: UpdateAirbnbListingCancellationResponse200DataCancellation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_airbnb_listing_cancellation_response_200_data_cancellation import UpdateAirbnbListingCancellationResponse200DataCancellation
        applied: list[str] | Unset = UNSET
        if not isinstance(self.applied, Unset):
            applied = self.applied



        cancellation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cancellation, Unset):
            cancellation = self.cancellation.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if applied is not UNSET:
            field_dict["applied"] = applied
        if cancellation is not UNSET:
            field_dict["cancellation"] = cancellation

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_airbnb_listing_cancellation_response_200_data_cancellation import UpdateAirbnbListingCancellationResponse200DataCancellation
        d = dict(src_dict)
        applied = cast(list[str], d.pop("applied", UNSET))


        _cancellation = d.pop("cancellation", UNSET)
        cancellation: UpdateAirbnbListingCancellationResponse200DataCancellation | Unset
        if isinstance(_cancellation,  Unset):
            cancellation = UNSET
        else:
            cancellation = UpdateAirbnbListingCancellationResponse200DataCancellation.from_dict(_cancellation)




        update_airbnb_listing_cancellation_response_200_data = cls(
            applied=applied,
            cancellation=cancellation,
        )


        update_airbnb_listing_cancellation_response_200_data.additional_properties = d
        return update_airbnb_listing_cancellation_response_200_data

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
