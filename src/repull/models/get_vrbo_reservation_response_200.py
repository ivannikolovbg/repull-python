from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_reservation_response_200_data import GetVrboReservationResponse200Data
  from ..models.get_vrbo_reservation_response_200_data_freshness import GetVrboReservationResponse200DataFreshness





T = TypeVar("T", bound="GetVrboReservationResponse200")



@_attrs_define
class GetVrboReservationResponse200:
    """ 
        Attributes:
            data (GetVrboReservationResponse200Data | Unset): The booking as Vrbo shows it; with `?options=`, Vrbo's choices
                for that action.
            confirmation_code (str | Unset):
            listing_id (None | str | Unset):
            data_freshness (GetVrboReservationResponse200DataFreshness | Unset):
     """

    data: GetVrboReservationResponse200Data | Unset = UNSET
    confirmation_code: str | Unset = UNSET
    listing_id: None | str | Unset = UNSET
    data_freshness: GetVrboReservationResponse200DataFreshness | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_reservation_response_200_data import GetVrboReservationResponse200Data
        from ..models.get_vrbo_reservation_response_200_data_freshness import GetVrboReservationResponse200DataFreshness
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        confirmation_code = self.confirmation_code

        listing_id: None | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        data_freshness: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_freshness, Unset):
            data_freshness = self.data_freshness.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if confirmation_code is not UNSET:
            field_dict["confirmationCode"] = confirmation_code
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if data_freshness is not UNSET:
            field_dict["dataFreshness"] = data_freshness

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_reservation_response_200_data import GetVrboReservationResponse200Data
        from ..models.get_vrbo_reservation_response_200_data_freshness import GetVrboReservationResponse200DataFreshness
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: GetVrboReservationResponse200Data | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = GetVrboReservationResponse200Data.from_dict(_data)




        confirmation_code = d.pop("confirmationCode", UNSET)

        def _parse_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        _data_freshness = d.pop("dataFreshness", UNSET)
        data_freshness: GetVrboReservationResponse200DataFreshness | Unset
        if isinstance(_data_freshness,  Unset):
            data_freshness = UNSET
        else:
            data_freshness = GetVrboReservationResponse200DataFreshness.from_dict(_data_freshness)




        get_vrbo_reservation_response_200 = cls(
            data=data,
            confirmation_code=confirmation_code,
            listing_id=listing_id,
            data_freshness=data_freshness,
        )


        get_vrbo_reservation_response_200.additional_properties = d
        return get_vrbo_reservation_response_200

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
