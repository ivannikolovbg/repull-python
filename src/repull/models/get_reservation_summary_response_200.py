from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_reservation_summary_response_200_basis import GetReservationSummaryResponse200Basis
from ..models.get_reservation_summary_response_200_group_by_item import GetReservationSummaryResponse200GroupByItem
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_reservation_summary_response_200_groups_item import GetReservationSummaryResponse200GroupsItem
  from ..models.get_reservation_summary_response_200_totals_item import GetReservationSummaryResponse200TotalsItem





T = TypeVar("T", bound="GetReservationSummaryResponse200")



@_attrs_define
class GetReservationSummaryResponse200:
    """ 
        Attributes:
            from_ (datetime.date):  Example: 2026-11-10.
            to (datetime.date):  Example: 2027-02-09.
            basis (GetReservationSummaryResponse200Basis):
            group_by (list[GetReservationSummaryResponse200GroupByItem]):
            as_of (datetime.date | None):
            listing_count (int): Active listings covered (the occupancy denominator). Example: 19.
            totals (list[GetReservationSummaryResponse200TotalsItem]):
            groups (list[GetReservationSummaryResponse200GroupsItem]):
     """

    from_: datetime.date
    to: datetime.date
    basis: GetReservationSummaryResponse200Basis
    group_by: list[GetReservationSummaryResponse200GroupByItem]
    as_of: datetime.date | None
    listing_count: int
    totals: list[GetReservationSummaryResponse200TotalsItem]
    groups: list[GetReservationSummaryResponse200GroupsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_reservation_summary_response_200_groups_item import GetReservationSummaryResponse200GroupsItem
        from ..models.get_reservation_summary_response_200_totals_item import GetReservationSummaryResponse200TotalsItem
        from_ = self.from_.isoformat()

        to = self.to.isoformat()

        basis = self.basis.value

        group_by = []
        for group_by_item_data in self.group_by:
            group_by_item = group_by_item_data.value
            group_by.append(group_by_item)



        as_of: None | str
        if isinstance(self.as_of, datetime.date):
            as_of = self.as_of.isoformat()
        else:
            as_of = self.as_of

        listing_count = self.listing_count

        totals = []
        for totals_item_data in self.totals:
            totals_item = totals_item_data.to_dict()
            totals.append(totals_item)



        groups = []
        for groups_item_data in self.groups:
            groups_item = groups_item_data.to_dict()
            groups.append(groups_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "from": from_,
            "to": to,
            "basis": basis,
            "groupBy": group_by,
            "asOf": as_of,
            "listingCount": listing_count,
            "totals": totals,
            "groups": groups,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_reservation_summary_response_200_groups_item import GetReservationSummaryResponse200GroupsItem
        from ..models.get_reservation_summary_response_200_totals_item import GetReservationSummaryResponse200TotalsItem
        d = dict(src_dict)
        from_ = isoparse(d.pop("from")).date()




        to = isoparse(d.pop("to")).date()




        basis = GetReservationSummaryResponse200Basis(d.pop("basis"))




        group_by = []
        _group_by = d.pop("groupBy")
        for group_by_item_data in (_group_by):
            group_by_item = GetReservationSummaryResponse200GroupByItem(group_by_item_data)



            group_by.append(group_by_item)


        def _parse_as_of(data: object) -> datetime.date | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_of_type_0 = isoparse(data).date()



                return as_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None, data)

        as_of = _parse_as_of(d.pop("asOf"))


        listing_count = d.pop("listingCount")

        totals = []
        _totals = d.pop("totals")
        for totals_item_data in (_totals):
            totals_item = GetReservationSummaryResponse200TotalsItem.from_dict(totals_item_data)



            totals.append(totals_item)


        groups = []
        _groups = d.pop("groups")
        for groups_item_data in (_groups):
            groups_item = GetReservationSummaryResponse200GroupsItem.from_dict(groups_item_data)



            groups.append(groups_item)


        get_reservation_summary_response_200 = cls(
            from_=from_,
            to=to,
            basis=basis,
            group_by=group_by,
            as_of=as_of,
            listing_count=listing_count,
            totals=totals,
            groups=groups,
        )


        get_reservation_summary_response_200.additional_properties = d
        return get_reservation_summary_response_200

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
