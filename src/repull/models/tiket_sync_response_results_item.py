from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tiket_sync_response_results_item_step import TiketSyncResponseResultsItemStep
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tiket_sync_response_results_item_result_type_0 import TiketSyncResponseResultsItemResultType0





T = TypeVar("T", bound="TiketSyncResponseResultsItem")



@_attrs_define
class TiketSyncResponseResultsItem:
    """ 
        Attributes:
            property_id (str | Unset):
            listing_id (str | Unset):
            step (TiketSyncResponseResultsItemStep | Unset):
            ok (bool | Unset):
            skipped (str | Unset): `listing_inactive` — an inactive listing is not sold, so its calendar is not sent.
            result (None | TiketSyncResponseResultsItemResultType0 | Unset):
            error (str | Unset):
     """

    property_id: str | Unset = UNSET
    listing_id: str | Unset = UNSET
    step: TiketSyncResponseResultsItemStep | Unset = UNSET
    ok: bool | Unset = UNSET
    skipped: str | Unset = UNSET
    result: None | TiketSyncResponseResultsItemResultType0 | Unset = UNSET
    error: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tiket_sync_response_results_item_result_type_0 import TiketSyncResponseResultsItemResultType0
        property_id = self.property_id

        listing_id = self.listing_id

        step: str | Unset = UNSET
        if not isinstance(self.step, Unset):
            step = self.step.value


        ok = self.ok

        skipped = self.skipped

        result: dict[str, Any] | None | Unset
        if isinstance(self.result, Unset):
            result = UNSET
        elif isinstance(self.result, TiketSyncResponseResultsItemResultType0):
            result = self.result.to_dict()
        else:
            result = self.result

        error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if step is not UNSET:
            field_dict["step"] = step
        if ok is not UNSET:
            field_dict["ok"] = ok
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiket_sync_response_results_item_result_type_0 import TiketSyncResponseResultsItemResultType0
        d = dict(src_dict)
        property_id = d.pop("propertyId", UNSET)

        listing_id = d.pop("listingId", UNSET)

        _step = d.pop("step", UNSET)
        step: TiketSyncResponseResultsItemStep | Unset
        if isinstance(_step,  Unset):
            step = UNSET
        else:
            step = TiketSyncResponseResultsItemStep(_step)




        ok = d.pop("ok", UNSET)

        skipped = d.pop("skipped", UNSET)

        def _parse_result(data: object) -> None | TiketSyncResponseResultsItemResultType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                result_type_0 = TiketSyncResponseResultsItemResultType0.from_dict(data)



                return result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TiketSyncResponseResultsItemResultType0 | Unset, data)

        result = _parse_result(d.pop("result", UNSET))


        error = d.pop("error", UNSET)

        tiket_sync_response_results_item = cls(
            property_id=property_id,
            listing_id=listing_id,
            step=step,
            ok=ok,
            skipped=skipped,
            result=result,
            error=error,
        )


        tiket_sync_response_results_item.additional_properties = d
        return tiket_sync_response_results_item

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
