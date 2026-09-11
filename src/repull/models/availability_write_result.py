from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.availability_write_result_synced import AvailabilityWriteResultSynced





T = TypeVar("T", bound="AvailabilityWriteResult")



@_attrs_define
class AvailabilityWriteResult:
    """ 
        Attributes:
            listing_ids (list[str] | Unset):
            dates (int | Unset): How many dates were written.
            synced (AvailabilityWriteResultSynced | Unset): Per-channel push outcome. A partial failure is surfaced, not
                swallowed: "saved locally but the channel rejected it" is precisely the state a caller must know about.
            warning (str | Unset): Present only when one or more channel pushes failed.
     """

    listing_ids: list[str] | Unset = UNSET
    dates: int | Unset = UNSET
    synced: AvailabilityWriteResultSynced | Unset = UNSET
    warning: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.availability_write_result_synced import AvailabilityWriteResultSynced
        listing_ids: list[str] | Unset = UNSET
        if not isinstance(self.listing_ids, Unset):
            listing_ids = self.listing_ids



        dates = self.dates

        synced: dict[str, Any] | Unset = UNSET
        if not isinstance(self.synced, Unset):
            synced = self.synced.to_dict()

        warning = self.warning


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_ids is not UNSET:
            field_dict["listingIds"] = listing_ids
        if dates is not UNSET:
            field_dict["dates"] = dates
        if synced is not UNSET:
            field_dict["synced"] = synced
        if warning is not UNSET:
            field_dict["warning"] = warning

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.availability_write_result_synced import AvailabilityWriteResultSynced
        d = dict(src_dict)
        listing_ids = cast(list[str], d.pop("listingIds", UNSET))


        dates = d.pop("dates", UNSET)

        _synced = d.pop("synced", UNSET)
        synced: AvailabilityWriteResultSynced | Unset
        if isinstance(_synced,  Unset):
            synced = UNSET
        else:
            synced = AvailabilityWriteResultSynced.from_dict(_synced)




        warning = d.pop("warning", UNSET)

        availability_write_result = cls(
            listing_ids=listing_ids,
            dates=dates,
            synced=synced,
            warning=warning,
        )


        availability_write_result.additional_properties = d
        return availability_write_result

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
