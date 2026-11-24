from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tiket_sync_response_results_item import TiketSyncResponseResultsItem





T = TypeVar("T", bound="TiketSyncResponse")



@_attrs_define
class TiketSyncResponse:
    """ 
        Attributes:
            synced (int | Unset):
            failed (int | Unset):
            results (list[TiketSyncResponseResultsItem] | Unset):
     """

    synced: int | Unset = UNSET
    failed: int | Unset = UNSET
    results: list[TiketSyncResponseResultsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tiket_sync_response_results_item import TiketSyncResponseResultsItem
        synced = self.synced

        failed = self.failed

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if synced is not UNSET:
            field_dict["synced"] = synced
        if failed is not UNSET:
            field_dict["failed"] = failed
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiket_sync_response_results_item import TiketSyncResponseResultsItem
        d = dict(src_dict)
        synced = d.pop("synced", UNSET)

        failed = d.pop("failed", UNSET)

        _results = d.pop("results", UNSET)
        results: list[TiketSyncResponseResultsItem] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = TiketSyncResponseResultsItem.from_dict(results_item_data)



                results.append(results_item)


        tiket_sync_response = cls(
            synced=synced,
            failed=failed,
            results=results,
        )


        tiket_sync_response.additional_properties = d
        return tiket_sync_response

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
