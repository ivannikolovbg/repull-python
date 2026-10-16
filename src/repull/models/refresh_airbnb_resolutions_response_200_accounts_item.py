from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.refresh_airbnb_resolutions_response_200_accounts_item_error_type_0 import RefreshAirbnbResolutionsResponse200AccountsItemErrorType0





T = TypeVar("T", bound="RefreshAirbnbResolutionsResponse200AccountsItem")



@_attrs_define
class RefreshAirbnbResolutionsResponse200AccountsItem:
    """ 
        Attributes:
            account_id (str):
            count (int):
            error (None | RefreshAirbnbResolutionsResponse200AccountsItemErrorType0 | Unset):
     """

    account_id: str
    count: int
    error: None | RefreshAirbnbResolutionsResponse200AccountsItemErrorType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.refresh_airbnb_resolutions_response_200_accounts_item_error_type_0 import RefreshAirbnbResolutionsResponse200AccountsItemErrorType0
        account_id = self.account_id

        count = self.count

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, RefreshAirbnbResolutionsResponse200AccountsItemErrorType0):
            error = self.error.to_dict()
        else:
            error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "account_id": account_id,
            "count": count,
        })
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.refresh_airbnb_resolutions_response_200_accounts_item_error_type_0 import RefreshAirbnbResolutionsResponse200AccountsItemErrorType0
        d = dict(src_dict)
        account_id = d.pop("account_id")

        count = d.pop("count")

        def _parse_error(data: object) -> None | RefreshAirbnbResolutionsResponse200AccountsItemErrorType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = RefreshAirbnbResolutionsResponse200AccountsItemErrorType0.from_dict(data)



                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RefreshAirbnbResolutionsResponse200AccountsItemErrorType0 | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        refresh_airbnb_resolutions_response_200_accounts_item = cls(
            account_id=account_id,
            count=count,
            error=error,
        )


        refresh_airbnb_resolutions_response_200_accounts_item.additional_properties = d
        return refresh_airbnb_resolutions_response_200_accounts_item

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
