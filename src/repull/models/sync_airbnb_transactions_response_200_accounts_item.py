from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.sync_airbnb_transactions_response_200_accounts_item_error import SyncAirbnbTransactionsResponse200AccountsItemError





T = TypeVar("T", bound="SyncAirbnbTransactionsResponse200AccountsItem")



@_attrs_define
class SyncAirbnbTransactionsResponse200AccountsItem:
    """ 
        Attributes:
            account_id (str): Airbnb host id.
            count (int):
            payouts (int): Payouts in the refreshed window.
            upcoming_removed (int): UPCOMING lines Airbnb no longer lists (paid out or cancelled) and were removed.
            error (SyncAirbnbTransactionsResponse200AccountsItemError | Unset): Present only when this account was not
                refreshed. `code` is `connection_reauth_required`, `airbnb_rejected`, `airbnb_rate_limited`, `airbnb_error`, or
                `time_budget` (the request ran out of time before reaching it: refresh it alone with `?account_id=`).
     """

    account_id: str
    count: int
    payouts: int
    upcoming_removed: int
    error: SyncAirbnbTransactionsResponse200AccountsItemError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_airbnb_transactions_response_200_accounts_item_error import SyncAirbnbTransactionsResponse200AccountsItemError
        account_id = self.account_id

        count = self.count

        payouts = self.payouts

        upcoming_removed = self.upcoming_removed

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "accountId": account_id,
            "count": count,
            "payouts": payouts,
            "upcomingRemoved": upcoming_removed,
        })
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_airbnb_transactions_response_200_accounts_item_error import SyncAirbnbTransactionsResponse200AccountsItemError
        d = dict(src_dict)
        account_id = d.pop("accountId")

        count = d.pop("count")

        payouts = d.pop("payouts")

        upcoming_removed = d.pop("upcomingRemoved")

        _error = d.pop("error", UNSET)
        error: SyncAirbnbTransactionsResponse200AccountsItemError | Unset
        if isinstance(_error,  Unset):
            error = UNSET
        else:
            error = SyncAirbnbTransactionsResponse200AccountsItemError.from_dict(_error)




        sync_airbnb_transactions_response_200_accounts_item = cls(
            account_id=account_id,
            count=count,
            payouts=payouts,
            upcoming_removed=upcoming_removed,
            error=error,
        )


        sync_airbnb_transactions_response_200_accounts_item.additional_properties = d
        return sync_airbnb_transactions_response_200_accounts_item

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
