from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_data_freshness import AirbnbDataFreshness
  from ..models.airbnb_reservation_detail import AirbnbReservationDetail





T = TypeVar("T", bound="AirbnbReservationDetailResponse")



@_attrs_define
class AirbnbReservationDetailResponse:
    """ 
        Attributes:
            data (AirbnbReservationDetail): One Airbnb reservation: the unified reservation (the same record as `GET
                /v1/reservations/{reservationId}`, as stored), the connected account and payout, and `airbnb` — the row `GET
                /v1/channels/airbnb/reservations` returns for it.
            data_freshness (AirbnbDataFreshness | Unset): Top-level freshness indicator for any DB-backed Airbnb read. Tells
                consumers WHY a column may be `null` or stale without sprinkling per-row error envelopes through the response.
                The endpoint always returns 200 + DB data; this field is the single signal for "should I prompt the user to
                reconnect / wait for sync?".

                A workspace can connect several Airbnb accounts, so the answer has two levels. `accounts[]` carries the verdict
                per account; the top-level fields aggregate it. Scope a request with `?account_id=` and `accounts[]` holds
                exactly that account, with the top-level fields mirroring it.
     """

    data: AirbnbReservationDetail
    data_freshness: AirbnbDataFreshness | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_data_freshness import AirbnbDataFreshness
        from ..models.airbnb_reservation_detail import AirbnbReservationDetail
        data = self.data.to_dict()

        data_freshness: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data_freshness, Unset):
            data_freshness = self.data_freshness.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "data": data,
        })
        if data_freshness is not UNSET:
            field_dict["dataFreshness"] = data_freshness

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_data_freshness import AirbnbDataFreshness
        from ..models.airbnb_reservation_detail import AirbnbReservationDetail
        d = dict(src_dict)
        data = AirbnbReservationDetail.from_dict(d.pop("data"))




        _data_freshness = d.pop("dataFreshness", UNSET)
        data_freshness: AirbnbDataFreshness | Unset
        if isinstance(_data_freshness,  Unset):
            data_freshness = UNSET
        else:
            data_freshness = AirbnbDataFreshness.from_dict(_data_freshness)




        airbnb_reservation_detail_response = cls(
            data=data,
            data_freshness=data_freshness,
        )


        airbnb_reservation_detail_response.additional_properties = d
        return airbnb_reservation_detail_response

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
