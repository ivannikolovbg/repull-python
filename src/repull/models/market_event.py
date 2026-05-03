from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="MarketEvent")



@_attrs_define
class MarketEvent:
    """ 
        Attributes:
            id (str | Unset):
            title (str | Unset):
            category (None | str | Unset):
            start_date (datetime.date | Unset):
            end_date (datetime.date | None | Unset):
            lat (float | None | Unset):
            lng (float | None | Unset):
            rank (float | None | Unset):
            local_rank (float | None | Unset):
            attendance (int | None | Unset):
            demand_impact (None | str | Unset):
            labels (list[str] | None | Unset):
     """

    id: str | Unset = UNSET
    title: str | Unset = UNSET
    category: None | str | Unset = UNSET
    start_date: datetime.date | Unset = UNSET
    end_date: datetime.date | None | Unset = UNSET
    lat: float | None | Unset = UNSET
    lng: float | None | Unset = UNSET
    rank: float | None | Unset = UNSET
    local_rank: float | None | Unset = UNSET
    attendance: int | None | Unset = UNSET
    demand_impact: None | str | Unset = UNSET
    labels: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        start_date: str | Unset = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        lat: float | None | Unset
        if isinstance(self.lat, Unset):
            lat = UNSET
        else:
            lat = self.lat

        lng: float | None | Unset
        if isinstance(self.lng, Unset):
            lng = UNSET
        else:
            lng = self.lng

        rank: float | None | Unset
        if isinstance(self.rank, Unset):
            rank = UNSET
        else:
            rank = self.rank

        local_rank: float | None | Unset
        if isinstance(self.local_rank, Unset):
            local_rank = UNSET
        else:
            local_rank = self.local_rank

        attendance: int | None | Unset
        if isinstance(self.attendance, Unset):
            attendance = UNSET
        else:
            attendance = self.attendance

        demand_impact: None | str | Unset
        if isinstance(self.demand_impact, Unset):
            demand_impact = UNSET
        else:
            demand_impact = self.demand_impact

        labels: list[str] | None | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, list):
            labels = self.labels


        else:
            labels = self.labels


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if title is not UNSET:
            field_dict["title"] = title
        if category is not UNSET:
            field_dict["category"] = category
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if rank is not UNSET:
            field_dict["rank"] = rank
        if local_rank is not UNSET:
            field_dict["localRank"] = local_rank
        if attendance is not UNSET:
            field_dict["attendance"] = attendance
        if demand_impact is not UNSET:
            field_dict["demandImpact"] = demand_impact
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        title = d.pop("title", UNSET)

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))


        _start_date = d.pop("startDate", UNSET)
        start_date: datetime.date | Unset
        if isinstance(_start_date,  Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()




        def _parse_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data).date()



                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))


        def _parse_lat(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lat = _parse_lat(d.pop("lat", UNSET))


        def _parse_lng(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        lng = _parse_lng(d.pop("lng", UNSET))


        def _parse_rank(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        rank = _parse_rank(d.pop("rank", UNSET))


        def _parse_local_rank(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        local_rank = _parse_local_rank(d.pop("localRank", UNSET))


        def _parse_attendance(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        attendance = _parse_attendance(d.pop("attendance", UNSET))


        def _parse_demand_impact(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        demand_impact = _parse_demand_impact(d.pop("demandImpact", UNSET))


        def _parse_labels(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                labels_type_0 = cast(list[str], data)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))


        market_event = cls(
            id=id,
            title=title,
            category=category,
            start_date=start_date,
            end_date=end_date,
            lat=lat,
            lng=lng,
            rank=rank,
            local_rank=local_rank,
            attendance=attendance,
            demand_impact=demand_impact,
            labels=labels,
        )


        market_event.additional_properties = d
        return market_event

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
