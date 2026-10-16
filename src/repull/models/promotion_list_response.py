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

if TYPE_CHECKING:
  from ..models.promotion import Promotion





T = TypeVar("T", bound="PromotionListResponse")



@_attrs_define
class PromotionListResponse:
    """ 
        Attributes:
            data (list[Promotion] | Unset):
            synced_at (datetime.datetime | None | Unset): When the channels were last read for this listing.
            sync_error (None | str | Unset):
     """

    data: list[Promotion] | Unset = UNSET
    synced_at: datetime.datetime | None | Unset = UNSET
    sync_error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.promotion import Promotion
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)



        synced_at: None | str | Unset
        if isinstance(self.synced_at, Unset):
            synced_at = UNSET
        elif isinstance(self.synced_at, datetime.datetime):
            synced_at = self.synced_at.isoformat()
        else:
            synced_at = self.synced_at

        sync_error: None | str | Unset
        if isinstance(self.sync_error, Unset):
            sync_error = UNSET
        else:
            sync_error = self.sync_error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if synced_at is not UNSET:
            field_dict["syncedAt"] = synced_at
        if sync_error is not UNSET:
            field_dict["syncError"] = sync_error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.promotion import Promotion
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[Promotion] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = Promotion.from_dict(data_item_data)



                data.append(data_item)


        def _parse_synced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                synced_at_type_0 = isoparse(data)



                return synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        synced_at = _parse_synced_at(d.pop("syncedAt", UNSET))


        def _parse_sync_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sync_error = _parse_sync_error(d.pop("syncError", UNSET))


        promotion_list_response = cls(
            data=data,
            synced_at=synced_at,
            sync_error=sync_error,
        )


        promotion_list_response.additional_properties = d
        return promotion_list_response

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
