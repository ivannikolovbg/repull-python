from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.channel_market_state_item_channel import ChannelMarketStateItemChannel
from ..models.channel_market_state_item_state import ChannelMarketStateItemState
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ChannelMarketStateItem")



@_attrs_define
class ChannelMarketStateItem:
    """ What happened on ONE channel item — one Airbnb connection, or one Booking.com property. A listing can carry several
    Airbnb connections (a re-list, or a move between host accounts) and each gets its own entry.

        Attributes:
            channel (ChannelMarketStateItemChannel):
            state (ChannelMarketStateItemState): **What is now true of this item**, not what you asked for.

                `offline` — it is off the market. `online` — it is back on. `unchanged` — nothing was sent, or what was sent did
                not take; `code` and `message` say why.

                `unchanged` never means "it was already like that": it means we did not put it there, and it is still in
                whatever state it was in before the call.
            ok (bool): True only when the channel confirmed the change.
            connection_id (None | str | Unset): Airbnb connection row id — the `id` from `GET
                /v1/channels/airbnb/listings/{id}`. Present on Airbnb items.
            hotel_id (None | str | Unset): The Booking.com property acted on. Present on Booking.com items; null when the
                property could not be resolved.
            code (str | Unset): Error code when `ok` is false — the SAME code the channel-specific endpoint returns for this
                failure, so one vocabulary covers both surfaces. Absent when `ok` is true.

                The channel codes come in pairs, and the pair is the retryable split — the most useful bit in the whole item:

                - `airbnb_rejected` / `booking_rejected` — the channel refused the request AS SENT. `message` carries its own
                reason. Correct it and send again; resending the same thing is refused again.
                - `airbnb_error` / `booking_error` — the channel did not complete the request (outage, timeout, server error).
                Nothing about the request needs to change: retry with backoff.

                Plus `ambiguous_booking_mapping` (name the property with `hotelId`) and `payment_required` (a billing refusal,
                which keeps its own code rather than being buried under a channel one).
            previous_code (str | Unset): The `code` this item used to carry, for callers still branching on the old string.
                A migration aid with a deprecation window — **`code` is canonical.**

                This fan-out reaches Airbnb through an internal hop that flattens a refusal into its own 500, so an unambiguous
                Airbnb 400 ("Please specify a valid room type") was reported as `airbnb_error` — whose published advice is to
                retry with backoff, forever, for something Airbnb will never accept. It now reads Airbnb's real status and
                answers `airbnb_rejected`, and the classification covers the whole 4xx range rather than only `400`. Items whose
                code changed carry `previousCode`. **Removed in v2.** Example: airbnb_error.
            message (str | Unset): The channel's own reason, verbatim. Absent when `ok` is true.
            fix (str | Unset): What to do about it, phrased for the direction you asked for — "still live and taking
                bookings" and "still down" call for different reactions. Absent when `ok` is true.
            verified (bool | Unset): Airbnb only, and only when going offline: the listing was READ BACK after the
                deactivation and confirmed down. Airbnb accepts a deactivation and leaves some listings live, so "we sent the
                request" is a weaker claim than this one and is never reported as success.
     """

    channel: ChannelMarketStateItemChannel
    state: ChannelMarketStateItemState
    ok: bool
    connection_id: None | str | Unset = UNSET
    hotel_id: None | str | Unset = UNSET
    code: str | Unset = UNSET
    previous_code: str | Unset = UNSET
    message: str | Unset = UNSET
    fix: str | Unset = UNSET
    verified: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        channel = self.channel.value

        state = self.state.value

        ok = self.ok

        connection_id: None | str | Unset
        if isinstance(self.connection_id, Unset):
            connection_id = UNSET
        else:
            connection_id = self.connection_id

        hotel_id: None | str | Unset
        if isinstance(self.hotel_id, Unset):
            hotel_id = UNSET
        else:
            hotel_id = self.hotel_id

        code = self.code

        previous_code = self.previous_code

        message = self.message

        fix = self.fix

        verified = self.verified


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "channel": channel,
            "state": state,
            "ok": ok,
        })
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if hotel_id is not UNSET:
            field_dict["hotelId"] = hotel_id
        if code is not UNSET:
            field_dict["code"] = code
        if previous_code is not UNSET:
            field_dict["previousCode"] = previous_code
        if message is not UNSET:
            field_dict["message"] = message
        if fix is not UNSET:
            field_dict["fix"] = fix
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = ChannelMarketStateItemChannel(d.pop("channel"))




        state = ChannelMarketStateItemState(d.pop("state"))




        ok = d.pop("ok")

        def _parse_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_id = _parse_connection_id(d.pop("connectionId", UNSET))


        def _parse_hotel_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        hotel_id = _parse_hotel_id(d.pop("hotelId", UNSET))


        code = d.pop("code", UNSET)

        previous_code = d.pop("previousCode", UNSET)

        message = d.pop("message", UNSET)

        fix = d.pop("fix", UNSET)

        verified = d.pop("verified", UNSET)

        channel_market_state_item = cls(
            channel=channel,
            state=state,
            ok=ok,
            connection_id=connection_id,
            hotel_id=hotel_id,
            code=code,
            previous_code=previous_code,
            message=message,
            fix=fix,
            verified=verified,
        )


        channel_market_state_item.additional_properties = d
        return channel_market_state_item

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
