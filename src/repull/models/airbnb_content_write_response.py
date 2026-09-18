from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_content_write_response_result import AirbnbContentWriteResponseResult





T = TypeVar("T", bound="AirbnbContentWriteResponse")



@_attrs_define
class AirbnbContentWriteResponse:
    """ Result of a content write. **A 200 does not by itself mean the change was applied**: Airbnb locks host-managed
    fields on established listings and answers 200 while applying nothing for them. `blockedFields` is the list of
    fields YOU sent that Airbnb dropped; `blockedFields: []` is what a landed write looks like.

        Attributes:
            listing_id (str):
            written (list[str]): Fields that were applied.
            blocked_fields (list[str]): Fields you sent that Airbnb refused to change. Not retryable — the content is
                managed on Airbnb.
            airbnb_listing_id (str | Unset): The Airbnb-side listing id the write went to.
            locale (str | Unset): Descriptions only — the locale written.
            message (str | Unset): Present only when `blockedFields` is non-empty: what was not applied.
            fix (str | Unset): Present only when `blockedFields` is non-empty: what to do about it.
            result (AirbnbContentWriteResponseResult | Unset): Airbnb's raw response.
     """

    listing_id: str
    written: list[str]
    blocked_fields: list[str]
    airbnb_listing_id: str | Unset = UNSET
    locale: str | Unset = UNSET
    message: str | Unset = UNSET
    fix: str | Unset = UNSET
    result: AirbnbContentWriteResponseResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_content_write_response_result import AirbnbContentWriteResponseResult
        listing_id = self.listing_id

        written = self.written



        blocked_fields = self.blocked_fields



        airbnb_listing_id = self.airbnb_listing_id

        locale = self.locale

        message = self.message

        fix = self.fix

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "listingId": listing_id,
            "written": written,
            "blockedFields": blocked_fields,
        })
        if airbnb_listing_id is not UNSET:
            field_dict["airbnbListingId"] = airbnb_listing_id
        if locale is not UNSET:
            field_dict["locale"] = locale
        if message is not UNSET:
            field_dict["message"] = message
        if fix is not UNSET:
            field_dict["fix"] = fix
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_content_write_response_result import AirbnbContentWriteResponseResult
        d = dict(src_dict)
        listing_id = d.pop("listingId")

        written = cast(list[str], d.pop("written"))


        blocked_fields = cast(list[str], d.pop("blockedFields"))


        airbnb_listing_id = d.pop("airbnbListingId", UNSET)

        locale = d.pop("locale", UNSET)

        message = d.pop("message", UNSET)

        fix = d.pop("fix", UNSET)

        _result = d.pop("result", UNSET)
        result: AirbnbContentWriteResponseResult | Unset
        if isinstance(_result,  Unset):
            result = UNSET
        else:
            result = AirbnbContentWriteResponseResult.from_dict(_result)




        airbnb_content_write_response = cls(
            listing_id=listing_id,
            written=written,
            blocked_fields=blocked_fields,
            airbnb_listing_id=airbnb_listing_id,
            locale=locale,
            message=message,
            fix=fix,
            result=result,
        )


        airbnb_content_write_response.additional_properties = d
        return airbnb_content_write_response

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
