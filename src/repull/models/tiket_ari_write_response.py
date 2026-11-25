from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tiket_ari_write_response_applied import TiketAriWriteResponseApplied
from ..models.tiket_ari_write_response_type import TiketAriWriteResponseType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tiket_ari_mismatch import TiketAriMismatch
  from ..models.tiket_ari_write_response_warnings_item import TiketAriWriteResponseWarningsItem





T = TypeVar("T", bound="TiketAriWriteResponse")



@_attrs_define
class TiketAriWriteResponse:
    """ Result of a tiket.com rates / availability / restrictions write.

        Attributes:
            property_id (str): tiket.com Hotel ID.
            type_ (TiketAriWriteResponseType):
            updates (int): Update rows sent (on the listing route, one per targeted rate plan).
            requests (int): Requests made to tiket.com.
            applied (TiketAriWriteResponseApplied): `verified` — the read-back matches what was sent. `mismatch` — tiket.com
                holds something else for at least one night (see `mismatches`). `unverified` — `verify: false` was sent.
            listing_id (str | Unset): Present on `PUT /v1/channels/tiket/listings/{id}/pricing`.
            room_type_code (str | Unset): Present on `PUT /v1/channels/tiket/listings/{id}/pricing`.
            echo_tokens (list[str] | Unset): tiket.com's reference for each request. Quote them to tiket.com support.
            warnings (list[TiketAriWriteResponseWarningsItem] | Unset): tiket.com's own warnings, verbatim (for example
                `ARI_PARTIALLY_ERROR` when part of a request was not applied).
            mismatches (list[TiketAriMismatch] | Unset): Present when `applied` is `mismatch`. At most 100; `mismatchCount`
                is the total.
            mismatch_count (int | Unset):
     """

    property_id: str
    type_: TiketAriWriteResponseType
    updates: int
    requests: int
    applied: TiketAriWriteResponseApplied
    listing_id: str | Unset = UNSET
    room_type_code: str | Unset = UNSET
    echo_tokens: list[str] | Unset = UNSET
    warnings: list[TiketAriWriteResponseWarningsItem] | Unset = UNSET
    mismatches: list[TiketAriMismatch] | Unset = UNSET
    mismatch_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tiket_ari_mismatch import TiketAriMismatch
        from ..models.tiket_ari_write_response_warnings_item import TiketAriWriteResponseWarningsItem
        property_id = self.property_id

        type_ = self.type_.value

        updates = self.updates

        requests = self.requests

        applied = self.applied.value

        listing_id = self.listing_id

        room_type_code = self.room_type_code

        echo_tokens: list[str] | Unset = UNSET
        if not isinstance(self.echo_tokens, Unset):
            echo_tokens = self.echo_tokens



        warnings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()
                warnings.append(warnings_item)



        mismatches: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mismatches, Unset):
            mismatches = []
            for mismatches_item_data in self.mismatches:
                mismatches_item = mismatches_item_data.to_dict()
                mismatches.append(mismatches_item)



        mismatch_count = self.mismatch_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "propertyId": property_id,
            "type": type_,
            "updates": updates,
            "requests": requests,
            "applied": applied,
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if room_type_code is not UNSET:
            field_dict["roomTypeCode"] = room_type_code
        if echo_tokens is not UNSET:
            field_dict["echoTokens"] = echo_tokens
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if mismatches is not UNSET:
            field_dict["mismatches"] = mismatches
        if mismatch_count is not UNSET:
            field_dict["mismatchCount"] = mismatch_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiket_ari_mismatch import TiketAriMismatch
        from ..models.tiket_ari_write_response_warnings_item import TiketAriWriteResponseWarningsItem
        d = dict(src_dict)
        property_id = d.pop("propertyId")

        type_ = TiketAriWriteResponseType(d.pop("type"))




        updates = d.pop("updates")

        requests = d.pop("requests")

        applied = TiketAriWriteResponseApplied(d.pop("applied"))




        listing_id = d.pop("listingId", UNSET)

        room_type_code = d.pop("roomTypeCode", UNSET)

        echo_tokens = cast(list[str], d.pop("echoTokens", UNSET))


        _warnings = d.pop("warnings", UNSET)
        warnings: list[TiketAriWriteResponseWarningsItem] | Unset = UNSET
        if _warnings is not UNSET:
            warnings = []
            for warnings_item_data in _warnings:
                warnings_item = TiketAriWriteResponseWarningsItem.from_dict(warnings_item_data)



                warnings.append(warnings_item)


        _mismatches = d.pop("mismatches", UNSET)
        mismatches: list[TiketAriMismatch] | Unset = UNSET
        if _mismatches is not UNSET:
            mismatches = []
            for mismatches_item_data in _mismatches:
                mismatches_item = TiketAriMismatch.from_dict(mismatches_item_data)



                mismatches.append(mismatches_item)


        mismatch_count = d.pop("mismatchCount", UNSET)

        tiket_ari_write_response = cls(
            property_id=property_id,
            type_=type_,
            updates=updates,
            requests=requests,
            applied=applied,
            listing_id=listing_id,
            room_type_code=room_type_code,
            echo_tokens=echo_tokens,
            warnings=warnings,
            mismatches=mismatches,
            mismatch_count=mismatch_count,
        )


        tiket_ari_write_response.additional_properties = d
        return tiket_ari_write_response

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
