from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="TiketConnectClaimResponse")



@_attrs_define
class TiketConnectClaimResponse:
    """ 
        Attributes:
            connected (bool | Unset):
            connection_id (str | Unset):
            hotel_id (str | Unset):
            rooms (int | Unset): Room types imported.
            rate_plans (int | Unset): Rate plans imported.
            price_model (None | str | Unset): `Room Based` (one `price` per night) or `Occupancy Based` (`occupancyPrices`
                per number of guests). Set per property in the tiket.com extranet. Example: Room Based.
            currency (None | str | Unset):
            auto_mapped (int | Unset): Room types mapped automatically to a listing with the same name.
     """

    connected: bool | Unset = UNSET
    connection_id: str | Unset = UNSET
    hotel_id: str | Unset = UNSET
    rooms: int | Unset = UNSET
    rate_plans: int | Unset = UNSET
    price_model: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    auto_mapped: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        connected = self.connected

        connection_id = self.connection_id

        hotel_id = self.hotel_id

        rooms = self.rooms

        rate_plans = self.rate_plans

        price_model: None | str | Unset
        if isinstance(self.price_model, Unset):
            price_model = UNSET
        else:
            price_model = self.price_model

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        auto_mapped = self.auto_mapped


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if connected is not UNSET:
            field_dict["connected"] = connected
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if hotel_id is not UNSET:
            field_dict["hotelId"] = hotel_id
        if rooms is not UNSET:
            field_dict["rooms"] = rooms
        if rate_plans is not UNSET:
            field_dict["ratePlans"] = rate_plans
        if price_model is not UNSET:
            field_dict["priceModel"] = price_model
        if currency is not UNSET:
            field_dict["currency"] = currency
        if auto_mapped is not UNSET:
            field_dict["autoMapped"] = auto_mapped

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connected = d.pop("connected", UNSET)

        connection_id = d.pop("connectionId", UNSET)

        hotel_id = d.pop("hotelId", UNSET)

        rooms = d.pop("rooms", UNSET)

        rate_plans = d.pop("ratePlans", UNSET)

        def _parse_price_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_model = _parse_price_model(d.pop("priceModel", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        auto_mapped = d.pop("autoMapped", UNSET)

        tiket_connect_claim_response = cls(
            connected=connected,
            connection_id=connection_id,
            hotel_id=hotel_id,
            rooms=rooms,
            rate_plans=rate_plans,
            price_model=price_model,
            currency=currency,
            auto_mapped=auto_mapped,
        )


        tiket_connect_claim_response.additional_properties = d
        return tiket_connect_claim_response

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
