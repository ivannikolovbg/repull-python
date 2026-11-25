from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tiket_content_response_objects_item_kind import TiketContentResponseObjectsItemKind
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.tiket_content_response_objects_item_content_type_0 import TiketContentResponseObjectsItemContentType0





T = TypeVar("T", bound="TiketContentResponseObjectsItem")



@_attrs_define
class TiketContentResponseObjectsItem:
    """ 
        Attributes:
            kind (TiketContentResponseObjectsItemKind | Unset): What the object is.
            partner_code (None | str | Unset): Repull's code for the object on tiket.com.
            listing_id (None | str | Unset):
            pushed_at (datetime.datetime | None | Unset):
            echo_token (None | str | Unset): tiket.com's reference for the push. Quote it to tiket.com support.
            content (None | TiketContentResponseObjectsItemContentType0 | Unset): The content that was sent.
     """

    kind: TiketContentResponseObjectsItemKind | Unset = UNSET
    partner_code: None | str | Unset = UNSET
    listing_id: None | str | Unset = UNSET
    pushed_at: datetime.datetime | None | Unset = UNSET
    echo_token: None | str | Unset = UNSET
    content: None | TiketContentResponseObjectsItemContentType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tiket_content_response_objects_item_content_type_0 import TiketContentResponseObjectsItemContentType0
        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value


        partner_code: None | str | Unset
        if isinstance(self.partner_code, Unset):
            partner_code = UNSET
        else:
            partner_code = self.partner_code

        listing_id: None | str | Unset
        if isinstance(self.listing_id, Unset):
            listing_id = UNSET
        else:
            listing_id = self.listing_id

        pushed_at: None | str | Unset
        if isinstance(self.pushed_at, Unset):
            pushed_at = UNSET
        elif isinstance(self.pushed_at, datetime.datetime):
            pushed_at = self.pushed_at.isoformat()
        else:
            pushed_at = self.pushed_at

        echo_token: None | str | Unset
        if isinstance(self.echo_token, Unset):
            echo_token = UNSET
        else:
            echo_token = self.echo_token

        content: dict[str, Any] | None | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, TiketContentResponseObjectsItemContentType0):
            content = self.content.to_dict()
        else:
            content = self.content


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if partner_code is not UNSET:
            field_dict["partnerCode"] = partner_code
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if pushed_at is not UNSET:
            field_dict["pushedAt"] = pushed_at
        if echo_token is not UNSET:
            field_dict["echoToken"] = echo_token
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiket_content_response_objects_item_content_type_0 import TiketContentResponseObjectsItemContentType0
        d = dict(src_dict)
        _kind = d.pop("kind", UNSET)
        kind: TiketContentResponseObjectsItemKind | Unset
        if isinstance(_kind,  Unset):
            kind = UNSET
        else:
            kind = TiketContentResponseObjectsItemKind(_kind)




        def _parse_partner_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        partner_code = _parse_partner_code(d.pop("partnerCode", UNSET))


        def _parse_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        listing_id = _parse_listing_id(d.pop("listingId", UNSET))


        def _parse_pushed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pushed_at_type_0 = isoparse(data)



                return pushed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        pushed_at = _parse_pushed_at(d.pop("pushedAt", UNSET))


        def _parse_echo_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        echo_token = _parse_echo_token(d.pop("echoToken", UNSET))


        def _parse_content(data: object) -> None | TiketContentResponseObjectsItemContentType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_0 = TiketContentResponseObjectsItemContentType0.from_dict(data)



                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TiketContentResponseObjectsItemContentType0 | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        tiket_content_response_objects_item = cls(
            kind=kind,
            partner_code=partner_code,
            listing_id=listing_id,
            pushed_at=pushed_at,
            echo_token=echo_token,
            content=content,
        )


        tiket_content_response_objects_item.additional_properties = d
        return tiket_content_response_objects_item

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
