from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_disconnected_payload_reason import AccountDisconnectedPayloadReason
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.account_disconnected_payload_listings_item import AccountDisconnectedPayloadListingsItem





T = TypeVar("T", bound="AccountDisconnectedPayload")



@_attrs_define
class AccountDisconnectedPayload:
    """ Payload for `account.disconnected`. A PMS or channel connection was revoked, expired, or rejected by the upstream
    provider. Sent for Airbnb, Booking.com Extranet logins, Vrbo logins and PMS connections (Hostaway, Guesty, Smoobu,
    Lodgify, Beds24, Hospitable, OwnerRez, iGMS, BookingSync, Track, Mews, Cloudbeds, Zeevou, RentalReady, CiiRUS, …). A
    PMS connection is reported when the PMS refuses its credentials (API key revoked or invalid, 401/403, token refresh
    refused); timeouts, rate limits and 5xx errors are retried and never reported. Sent once per disconnect, not on
    every failed sync. When the connection works again — credentials fixed in the PMS, or reconnected — Repull re-
    imports the changes made while it was down and sends their `reservation.*` events, so nothing missed has to be
    fetched by hand.

        Attributes:
            workspace_id (UUID | Unset):  Example: 47f8883d-28c2-4d2c-b020-c7cef1aff62c.
            account_id (None | str | Unset): The disconnected account's `externalAccountId` — the platform's own account id:
                Airbnb host id; Booking.com hotel id (`booking`); the Booking.com account id behind the Extranet login
                (`booking_extranet`); Vrbo's account id (`vrbo`); the PMS's own account or company id. `null` when the platform
                id is not known yet (a Vrbo sign-in before its account id is captured, a PMS that does not expose one); never a
                Repull id. Example: 79730216.
            connection_id (None | str | Unset): Our connection record id: the `X-Account-Id` value, the same as
                `account.id`. `null` only when the account has no connection record (e.g. a Vrbo sign-in in a workspace with no
                Vrbo connection). A string in this event. Example: 135.
            provider (str | Unset): Channel or PMS id: `airbnb`, `booking_extranet`, `vrbo`, or the PMS (`hostaway`,
                `guesty`, `smoobu`, …). Example: airbnb.
            disconnected_at (datetime.datetime | Unset):  Example: 2026-05-01T17:00:00.000Z.
            reason (AccountDisconnectedPayloadReason | Unset): Why the connection was lost. `refresh_token_rejected` —
                upstream OAuth refresh endpoint returned a hard rejection. `manual_disconnect` — host/admin disconnected via the
                dashboard. `auth_expired` — the saved credentials stopped working: an Extranet or Vrbo login was signed out, or
                a PMS rejected its API key or token (401/403). `revoked_upstream` — provider notified us the user revoked
                access. Example: refresh_token_rejected.
            listings (list[AccountDisconnectedPayloadListingsItem] | Unset): The listings this account holds in your
                workspace — the ones that stop syncing until it is reconnected. Identity only; inactive listings included.
                Matches `channels[].account` on `GET /v1/listings`. Empty when the account has no listings here.
     """

    workspace_id: UUID | Unset = UNSET
    account_id: None | str | Unset = UNSET
    connection_id: None | str | Unset = UNSET
    provider: str | Unset = UNSET
    disconnected_at: datetime.datetime | Unset = UNSET
    reason: AccountDisconnectedPayloadReason | Unset = UNSET
    listings: list[AccountDisconnectedPayloadListingsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.account_disconnected_payload_listings_item import AccountDisconnectedPayloadListingsItem
        workspace_id: str | Unset = UNSET
        if not isinstance(self.workspace_id, Unset):
            workspace_id = str(self.workspace_id)

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        connection_id: None | str | Unset
        if isinstance(self.connection_id, Unset):
            connection_id = UNSET
        else:
            connection_id = self.connection_id

        provider = self.provider

        disconnected_at: str | Unset = UNSET
        if not isinstance(self.disconnected_at, Unset):
            disconnected_at = self.disconnected_at.isoformat()

        reason: str | Unset = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value


        listings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.listings, Unset):
            listings = []
            for listings_item_data in self.listings:
                listings_item = listings_item_data.to_dict()
                listings.append(listings_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if workspace_id is not UNSET:
            field_dict["workspaceId"] = workspace_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if disconnected_at is not UNSET:
            field_dict["disconnectedAt"] = disconnected_at
        if reason is not UNSET:
            field_dict["reason"] = reason
        if listings is not UNSET:
            field_dict["listings"] = listings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_disconnected_payload_listings_item import AccountDisconnectedPayloadListingsItem
        d = dict(src_dict)
        _workspace_id = d.pop("workspaceId", UNSET)
        workspace_id: UUID | Unset
        if isinstance(_workspace_id,  Unset):
            workspace_id = UNSET
        else:
            workspace_id = UUID(_workspace_id)




        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("accountId", UNSET))


        def _parse_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_id = _parse_connection_id(d.pop("connectionId", UNSET))


        provider = d.pop("provider", UNSET)

        _disconnected_at = d.pop("disconnectedAt", UNSET)
        disconnected_at: datetime.datetime | Unset
        if isinstance(_disconnected_at,  Unset):
            disconnected_at = UNSET
        else:
            disconnected_at = isoparse(_disconnected_at)




        _reason = d.pop("reason", UNSET)
        reason: AccountDisconnectedPayloadReason | Unset
        if isinstance(_reason,  Unset):
            reason = UNSET
        else:
            reason = AccountDisconnectedPayloadReason(_reason)




        _listings = d.pop("listings", UNSET)
        listings: list[AccountDisconnectedPayloadListingsItem] | Unset = UNSET
        if _listings is not UNSET:
            listings = []
            for listings_item_data in _listings:
                listings_item = AccountDisconnectedPayloadListingsItem.from_dict(listings_item_data)



                listings.append(listings_item)


        account_disconnected_payload = cls(
            workspace_id=workspace_id,
            account_id=account_id,
            connection_id=connection_id,
            provider=provider,
            disconnected_at=disconnected_at,
            reason=reason,
            listings=listings,
        )


        account_disconnected_payload.additional_properties = d
        return account_disconnected_payload

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
