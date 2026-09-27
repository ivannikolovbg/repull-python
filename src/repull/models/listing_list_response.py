from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cursor_pagination import CursorPagination
  from ..models.listing import Listing
  from ..models.plan_notice import PlanNotice





T = TypeVar("T", bound="ListingListResponse")



@_attrs_define
class ListingListResponse:
    """ 
        Attributes:
            plan_notice (PlanNotice | Unset): Added to the body of EVERY JSON response (success or error, except bare arrays
                and 5xx) while the workspace is connected to more listings than its plan lets it use — so a developer reading
                any payload, or an AI assistant relaying it, sees it. Connect keeps every listing it finds, but on a capped plan
                only as many as the plan allows are active; the rest are held back inactive and keep syncing. The same responses
                also carry the `X-Repull-Listings-Held-Back` and `X-Repull-Active-Listing-Limit` headers. Using a held-back
                listing answers `403 listing_inactive` with `reason: "plan_limit"`. Tell the user: they can see the held-back
                listings with `GET /v1/listings?status=all`, choose which are active with `POST /v1/listings/status`, or
                upgrade.
            data (list[Listing] | Unset):
            pagination (CursorPagination | Unset): Canonical cursor-based pagination envelope. Pass `nextCursor` back as
                `?cursor=` to fetch the next page; stop when `hasMore` is `false`. The cursor is opaque base64 — do not parse or
                construct it by hand.
     """

    plan_notice: PlanNotice | Unset = UNSET
    data: list[Listing] | Unset = UNSET
    pagination: CursorPagination | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cursor_pagination import CursorPagination
        from ..models.listing import Listing
        from ..models.plan_notice import PlanNotice
        plan_notice: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plan_notice, Unset):
            plan_notice = self.plan_notice.to_dict()

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)



        pagination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if plan_notice is not UNSET:
            field_dict["planNotice"] = plan_notice
        if data is not UNSET:
            field_dict["data"] = data
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cursor_pagination import CursorPagination
        from ..models.listing import Listing
        from ..models.plan_notice import PlanNotice
        d = dict(src_dict)
        _plan_notice = d.pop("planNotice", UNSET)
        plan_notice: PlanNotice | Unset
        if isinstance(_plan_notice,  Unset):
            plan_notice = UNSET
        else:
            plan_notice = PlanNotice.from_dict(_plan_notice)




        _data = d.pop("data", UNSET)
        data: list[Listing] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = Listing.from_dict(data_item_data)



                data.append(data_item)


        _pagination = d.pop("pagination", UNSET)
        pagination: CursorPagination | Unset
        if isinstance(_pagination,  Unset):
            pagination = UNSET
        else:
            pagination = CursorPagination.from_dict(_pagination)




        listing_list_response = cls(
            plan_notice=plan_notice,
            data=data,
            pagination=pagination,
        )


        listing_list_response.additional_properties = d
        return listing_list_response

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
