from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.payout_completed_payload_channel import PayoutCompletedPayloadChannel
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_transaction import AirbnbTransaction





T = TypeVar("T", bound="PayoutCompletedPayload")



@_attrs_define
class PayoutCompletedPayload:
    """ Payload for `payout.completed`: one Airbnb payout and every line it paid. `payout` and each of `lines` are
    `AirbnbTransaction` objects, identical — ids included — to what `GET /v1/channels/airbnb/transactions?payout_id=`
    returns, so you can deduplicate on `transactionId` across webhooks and reads. The lines' signed `amount`s sum to
    `payout.payout.paidOutAmount`.

        Attributes:
            channel (PayoutCompletedPayloadChannel):
            account_id (str): The Airbnb account (host id) that was paid. Example: 10000001.
            payout (AirbnbTransaction): One line of the Airbnb settlement ledger: a Payout row (`isPayout: true`) or a line
                it paid. Money is in the payout currency; `amount` is signed (negative = taken back, e.g. an adjustment offset
                against this payout). A payout's lines sum to its `payout.paidOutAmount`.
            lines (list[AirbnbTransaction]): In payout order (`payout.lineIndex`).
            account_name (None | str | Unset):
     """

    channel: PayoutCompletedPayloadChannel
    account_id: str
    payout: AirbnbTransaction
    lines: list[AirbnbTransaction]
    account_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_transaction import AirbnbTransaction
        channel = self.channel.value

        account_id = self.account_id

        payout = self.payout.to_dict()

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)



        account_name: None | str | Unset
        if isinstance(self.account_name, Unset):
            account_name = UNSET
        else:
            account_name = self.account_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "channel": channel,
            "accountId": account_id,
            "payout": payout,
            "lines": lines,
        })
        if account_name is not UNSET:
            field_dict["accountName"] = account_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_transaction import AirbnbTransaction
        d = dict(src_dict)
        channel = PayoutCompletedPayloadChannel(d.pop("channel"))




        account_id = d.pop("accountId")

        payout = AirbnbTransaction.from_dict(d.pop("payout"))




        lines = []
        _lines = d.pop("lines")
        for lines_item_data in (_lines):
            lines_item = AirbnbTransaction.from_dict(lines_item_data)



            lines.append(lines_item)


        def _parse_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_name = _parse_account_name(d.pop("accountName", UNSET))


        payout_completed_payload = cls(
            channel=channel,
            account_id=account_id,
            payout=payout,
            lines=lines,
            account_name=account_name,
        )


        payout_completed_payload.additional_properties = d
        return payout_completed_payload

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
