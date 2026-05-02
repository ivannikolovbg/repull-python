from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.bulk_pricing_failure import BulkPricingFailure





T = TypeVar("T", bound="BulkPricingResponse")



@_attrs_define
class BulkPricingResponse:
    """ Response for `POST /v1/listings/pricing/bulk`. Per-item failures are returned granularly so the SDK consumer can
    retry just the bad entries.

        Attributes:
            processed (int | Unset): Total dates attempted across every item.
            succeeded (int | Unset): Total dates that were successfully applied (or declined).
            failed (list[BulkPricingFailure] | Unset):
     """

    processed: int | Unset = UNSET
    succeeded: int | Unset = UNSET
    failed: list[BulkPricingFailure] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_pricing_failure import BulkPricingFailure
        processed = self.processed

        succeeded = self.succeeded

        failed: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failed, Unset):
            failed = []
            for failed_item_data in self.failed:
                failed_item = failed_item_data.to_dict()
                failed.append(failed_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if processed is not UNSET:
            field_dict["processed"] = processed
        if succeeded is not UNSET:
            field_dict["succeeded"] = succeeded
        if failed is not UNSET:
            field_dict["failed"] = failed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_pricing_failure import BulkPricingFailure
        d = dict(src_dict)
        processed = d.pop("processed", UNSET)

        succeeded = d.pop("succeeded", UNSET)

        _failed = d.pop("failed", UNSET)
        failed: list[BulkPricingFailure] | Unset = UNSET
        if _failed is not UNSET:
            failed = []
            for failed_item_data in _failed:
                failed_item = BulkPricingFailure.from_dict(failed_item_data)



                failed.append(failed_item)


        bulk_pricing_response = cls(
            processed=processed,
            succeeded=succeeded,
            failed=failed,
        )


        bulk_pricing_response.additional_properties = d
        return bulk_pricing_response

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
