from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_units_added_payload_provider import AccountUnitsAddedPayloadProvider
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.account_units_added_payload_hotels_item import AccountUnitsAddedPayloadHotelsItem
  from ..models.account_units_added_payload_next_steps_item import AccountUnitsAddedPayloadNextStepsItem
  from ..models.account_units_added_payload_units_item import AccountUnitsAddedPayloadUnitsItem





T = TypeVar("T", bound="AccountUnitsAddedPayload")



@_attrs_define
class AccountUnitsAddedPayload:
    """ Payload for `account.units.added`. A connected Booking.com Extranet login gained a property (the hotel added the
    same Booking.com user to it) or a room on a property it already had. One event per property; never for the first
    import of a fresh connection (`connect.session.completed` and `account.import.*` cover that), never twice for the
    same rooms.

        Attributes:
            workspace_id (int): The workspace the login is connected in.
            provider (AccountUnitsAddedPayloadProvider): The channel. Today only Booking.com Extranet logins send this
                event.
            account_id (None | str): The Booking.com account id behind the Extranet login — the same value as
                `account.externalAccountId`. Example: 20123456.
            connection_id (None | str): Our connection record id: the `X-Account-Id` value, the same as `account.id`.
                Example: 482.
            handle (str): The connection handle the units and mappings endpoints take: `booking_extranet:{accountId}`.
                Example: booking_extranet:20123456.
            hotels (list[AccountUnitsAddedPayloadHotelsItem]): The property the new units belong to.
            units (list[AccountUnitsAddedPayloadUnitsItem]): The new units, as `GET /v1/connections/{id}/units` lists them.
            added_at (datetime.datetime): When the sync found the new units.
            next_steps (list[AccountUnitsAddedPayloadNextStepsItem]): What to call next: list the units, then map them.
     """

    workspace_id: int
    provider: AccountUnitsAddedPayloadProvider
    account_id: None | str
    connection_id: None | str
    handle: str
    hotels: list[AccountUnitsAddedPayloadHotelsItem]
    units: list[AccountUnitsAddedPayloadUnitsItem]
    added_at: datetime.datetime
    next_steps: list[AccountUnitsAddedPayloadNextStepsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account_units_added_payload_hotels_item import AccountUnitsAddedPayloadHotelsItem
        from ..models.account_units_added_payload_next_steps_item import AccountUnitsAddedPayloadNextStepsItem
        from ..models.account_units_added_payload_units_item import AccountUnitsAddedPayloadUnitsItem
        workspace_id = self.workspace_id

        provider = self.provider.value

        account_id: None | str
        account_id = self.account_id

        connection_id: None | str
        connection_id = self.connection_id

        handle = self.handle

        hotels = []
        for hotels_item_data in self.hotels:
            hotels_item = hotels_item_data.to_dict()
            hotels.append(hotels_item)



        units = []
        for units_item_data in self.units:
            units_item = units_item_data.to_dict()
            units.append(units_item)



        added_at = self.added_at.isoformat()

        next_steps = []
        for next_steps_item_data in self.next_steps:
            next_steps_item = next_steps_item_data.to_dict()
            next_steps.append(next_steps_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "workspaceId": workspace_id,
            "provider": provider,
            "accountId": account_id,
            "connectionId": connection_id,
            "handle": handle,
            "hotels": hotels,
            "units": units,
            "addedAt": added_at,
            "nextSteps": next_steps,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_units_added_payload_hotels_item import AccountUnitsAddedPayloadHotelsItem
        from ..models.account_units_added_payload_next_steps_item import AccountUnitsAddedPayloadNextStepsItem
        from ..models.account_units_added_payload_units_item import AccountUnitsAddedPayloadUnitsItem
        d = dict(src_dict)
        workspace_id = d.pop("workspaceId")

        provider = AccountUnitsAddedPayloadProvider(d.pop("provider"))




        def _parse_account_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        account_id = _parse_account_id(d.pop("accountId"))


        def _parse_connection_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        connection_id = _parse_connection_id(d.pop("connectionId"))


        handle = d.pop("handle")

        hotels = []
        _hotels = d.pop("hotels")
        for hotels_item_data in (_hotels):
            hotels_item = AccountUnitsAddedPayloadHotelsItem.from_dict(hotels_item_data)



            hotels.append(hotels_item)


        units = []
        _units = d.pop("units")
        for units_item_data in (_units):
            units_item = AccountUnitsAddedPayloadUnitsItem.from_dict(units_item_data)



            units.append(units_item)


        added_at = isoparse(d.pop("addedAt"))




        next_steps = []
        _next_steps = d.pop("nextSteps")
        for next_steps_item_data in (_next_steps):
            next_steps_item = AccountUnitsAddedPayloadNextStepsItem.from_dict(next_steps_item_data)



            next_steps.append(next_steps_item)


        account_units_added_payload = cls(
            workspace_id=workspace_id,
            provider=provider,
            account_id=account_id,
            connection_id=connection_id,
            handle=handle,
            hotels=hotels,
            units=units,
            added_at=added_at,
            next_steps=next_steps,
        )


        account_units_added_payload.additional_properties = d
        return account_units_added_payload

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
