from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.app_connection_health_status import AppConnectionHealthStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.app_connection_health_recent_errors_item import AppConnectionHealthRecentErrorsItem
  from ..models.app_connection_health_writes_per_day_item import AppConnectionHealthWritesPerDayItem





T = TypeVar("T", bound="AppConnectionHealth")



@_attrs_define
class AppConnectionHealth:
    """ How an app (PriceLabs) is doing on one connection, from its calls with the key.

        Attributes:
            status (AppConnectionHealthStatus): `active`: a successful price or minimum-stay push in the last 24 hours.
                `idle`: the app connected before but has not pushed in the last 24 hours. `failing`: more than 25% of the last
                24 hours' requests failed (at least 5 requests); read `recentErrors`. `never_connected`: the app has not used
                the key yet.
            writes_per_day (list[AppConnectionHealthWritesPerDayItem]): Successful price and minimum-stay pushes per UTC
                day, the last 7 days, oldest first.
            recent_errors (list[AppConnectionHealthRecentErrorsItem]): The 10 most recent failed requests, newest first.
            last_request_at (datetime.datetime | None | Unset): The app's last request with the key, of any kind.
            last_successful_write_at (datetime.datetime | None | Unset): The app's last successful price or minimum-stay
                push.
            requests24h (int | Unset):
            errors24h (int | Unset):
            error_rate_24_h (float | Unset): `errors24h / requests24h`; 0 when there were no requests. Example: 0.02.
            requests7d (int | Unset):
            errors7d (int | Unset):
            error_rate_7_d (float | Unset):  Example: 0.01.
     """

    status: AppConnectionHealthStatus
    writes_per_day: list[AppConnectionHealthWritesPerDayItem]
    recent_errors: list[AppConnectionHealthRecentErrorsItem]
    last_request_at: datetime.datetime | None | Unset = UNSET
    last_successful_write_at: datetime.datetime | None | Unset = UNSET
    requests24h: int | Unset = UNSET
    errors24h: int | Unset = UNSET
    error_rate_24_h: float | Unset = UNSET
    requests7d: int | Unset = UNSET
    errors7d: int | Unset = UNSET
    error_rate_7_d: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.app_connection_health_recent_errors_item import AppConnectionHealthRecentErrorsItem
        from ..models.app_connection_health_writes_per_day_item import AppConnectionHealthWritesPerDayItem
        status = self.status.value

        writes_per_day = []
        for writes_per_day_item_data in self.writes_per_day:
            writes_per_day_item = writes_per_day_item_data.to_dict()
            writes_per_day.append(writes_per_day_item)



        recent_errors = []
        for recent_errors_item_data in self.recent_errors:
            recent_errors_item = recent_errors_item_data.to_dict()
            recent_errors.append(recent_errors_item)



        last_request_at: None | str | Unset
        if isinstance(self.last_request_at, Unset):
            last_request_at = UNSET
        elif isinstance(self.last_request_at, datetime.datetime):
            last_request_at = self.last_request_at.isoformat()
        else:
            last_request_at = self.last_request_at

        last_successful_write_at: None | str | Unset
        if isinstance(self.last_successful_write_at, Unset):
            last_successful_write_at = UNSET
        elif isinstance(self.last_successful_write_at, datetime.datetime):
            last_successful_write_at = self.last_successful_write_at.isoformat()
        else:
            last_successful_write_at = self.last_successful_write_at

        requests24h = self.requests24h

        errors24h = self.errors24h

        error_rate_24_h = self.error_rate_24_h

        requests7d = self.requests7d

        errors7d = self.errors7d

        error_rate_7_d = self.error_rate_7_d


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "writesPerDay": writes_per_day,
            "recentErrors": recent_errors,
        })
        if last_request_at is not UNSET:
            field_dict["lastRequestAt"] = last_request_at
        if last_successful_write_at is not UNSET:
            field_dict["lastSuccessfulWriteAt"] = last_successful_write_at
        if requests24h is not UNSET:
            field_dict["requests24h"] = requests24h
        if errors24h is not UNSET:
            field_dict["errors24h"] = errors24h
        if error_rate_24_h is not UNSET:
            field_dict["errorRate24h"] = error_rate_24_h
        if requests7d is not UNSET:
            field_dict["requests7d"] = requests7d
        if errors7d is not UNSET:
            field_dict["errors7d"] = errors7d
        if error_rate_7_d is not UNSET:
            field_dict["errorRate7d"] = error_rate_7_d

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_connection_health_recent_errors_item import AppConnectionHealthRecentErrorsItem
        from ..models.app_connection_health_writes_per_day_item import AppConnectionHealthWritesPerDayItem
        d = dict(src_dict)
        status = AppConnectionHealthStatus(d.pop("status"))




        writes_per_day = []
        _writes_per_day = d.pop("writesPerDay")
        for writes_per_day_item_data in (_writes_per_day):
            writes_per_day_item = AppConnectionHealthWritesPerDayItem.from_dict(writes_per_day_item_data)



            writes_per_day.append(writes_per_day_item)


        recent_errors = []
        _recent_errors = d.pop("recentErrors")
        for recent_errors_item_data in (_recent_errors):
            recent_errors_item = AppConnectionHealthRecentErrorsItem.from_dict(recent_errors_item_data)



            recent_errors.append(recent_errors_item)


        def _parse_last_request_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_request_at_type_0 = isoparse(data)



                return last_request_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_request_at = _parse_last_request_at(d.pop("lastRequestAt", UNSET))


        def _parse_last_successful_write_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_successful_write_at_type_0 = isoparse(data)



                return last_successful_write_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_successful_write_at = _parse_last_successful_write_at(d.pop("lastSuccessfulWriteAt", UNSET))


        requests24h = d.pop("requests24h", UNSET)

        errors24h = d.pop("errors24h", UNSET)

        error_rate_24_h = d.pop("errorRate24h", UNSET)

        requests7d = d.pop("requests7d", UNSET)

        errors7d = d.pop("errors7d", UNSET)

        error_rate_7_d = d.pop("errorRate7d", UNSET)

        app_connection_health = cls(
            status=status,
            writes_per_day=writes_per_day,
            recent_errors=recent_errors,
            last_request_at=last_request_at,
            last_successful_write_at=last_successful_write_at,
            requests24h=requests24h,
            errors24h=errors24h,
            error_rate_24_h=error_rate_24_h,
            requests7d=requests7d,
            errors7d=errors7d,
            error_rate_7_d=error_rate_7_d,
        )


        app_connection_health.additional_properties = d
        return app_connection_health

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
