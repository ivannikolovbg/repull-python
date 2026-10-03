from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_content_update_response_pms_type_0 import ListingContentUpdateResponsePmsType0





T = TypeVar("T", bound="ListingContentUpdateResponse")



@_attrs_define
class ListingContentUpdateResponse:
    """ 
        Attributes:
            id (str | Unset): The listing id (serialized as a string to preserve precision).
            changed (list[str] | Unset): Content slabs that were actually written, e.g. ["title","occupancy","amenities"]. A
                non-English write also reports `locale:<tag>` so you can see which row was written. A rate change reports
                `pricing`, and `calendar` as well when nights on the calendar moved to the new rate.
            deferred (list[str] | Unset): Provided-but-not-applied fields — e.g. "photos" when a non-empty photos array
                carried no valid http(s) URL. On a listing a PMS manages, also the content sections the PMS refused (`title`,
                `descriptions`, `times`, `capacity`, `amenities`, `houseRules`, `address`, `photos`), which are then not written
                here either.
            pms (ListingContentUpdateResponsePmsType0 | None | Unset): Present when the listing is managed in a PMS: the
                PMS-owned fields were written there first, and this is its per-section outcome.
     """

    id: str | Unset = UNSET
    changed: list[str] | Unset = UNSET
    deferred: list[str] | Unset = UNSET
    pms: ListingContentUpdateResponsePmsType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_content_update_response_pms_type_0 import ListingContentUpdateResponsePmsType0
        id = self.id

        changed: list[str] | Unset = UNSET
        if not isinstance(self.changed, Unset):
            changed = self.changed



        deferred: list[str] | Unset = UNSET
        if not isinstance(self.deferred, Unset):
            deferred = self.deferred



        pms: dict[str, Any] | None | Unset
        if isinstance(self.pms, Unset):
            pms = UNSET
        elif isinstance(self.pms, ListingContentUpdateResponsePmsType0):
            pms = self.pms.to_dict()
        else:
            pms = self.pms


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if changed is not UNSET:
            field_dict["changed"] = changed
        if deferred is not UNSET:
            field_dict["deferred"] = deferred
        if pms is not UNSET:
            field_dict["pms"] = pms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_content_update_response_pms_type_0 import ListingContentUpdateResponsePmsType0
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        changed = cast(list[str], d.pop("changed", UNSET))


        deferred = cast(list[str], d.pop("deferred", UNSET))


        def _parse_pms(data: object) -> ListingContentUpdateResponsePmsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pms_type_0 = ListingContentUpdateResponsePmsType0.from_dict(data)



                return pms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingContentUpdateResponsePmsType0 | None | Unset, data)

        pms = _parse_pms(d.pop("pms", UNSET))


        listing_content_update_response = cls(
            id=id,
            changed=changed,
            deferred=deferred,
            pms=pms,
        )


        listing_content_update_response.additional_properties = d
        return listing_content_update_response

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
