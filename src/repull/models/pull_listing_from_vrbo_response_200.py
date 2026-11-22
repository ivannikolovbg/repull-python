from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.pull_listing_from_vrbo_response_200_channel import PullListingFromVrboResponse200Channel
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="PullListingFromVrboResponse200")



@_attrs_define
class PullListingFromVrboResponse200:
    """ 
        Attributes:
            listing_id (str | Unset):
            channel (PullListingFromVrboResponse200Channel | Unset):
            connection_id (None | str | Unset): The Vrbo account the values came from.
            external_id (str | Unset): The Vrbo listing number.
            refreshed_from_channel (bool | Unset): True when Vrbo answered and at least one section was refreshed.
            sections (list[str] | Unset): Sections refreshed from Vrbo. Example: ['descriptions', 'house-rules', 'fees'].
            failed_sections (list[str] | Unset): Sections Vrbo did not return this time; their stored copy is unchanged.
            pulled_at (datetime.datetime | Unset):
            next_pull_available_at (datetime.datetime | Unset): Earliest time another pull of this listing is accepted.
            min_interval_seconds (int | Unset):  Example: 900.
     """

    listing_id: str | Unset = UNSET
    channel: PullListingFromVrboResponse200Channel | Unset = UNSET
    connection_id: None | str | Unset = UNSET
    external_id: str | Unset = UNSET
    refreshed_from_channel: bool | Unset = UNSET
    sections: list[str] | Unset = UNSET
    failed_sections: list[str] | Unset = UNSET
    pulled_at: datetime.datetime | Unset = UNSET
    next_pull_available_at: datetime.datetime | Unset = UNSET
    min_interval_seconds: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        listing_id = self.listing_id

        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value


        connection_id: None | str | Unset
        if isinstance(self.connection_id, Unset):
            connection_id = UNSET
        else:
            connection_id = self.connection_id

        external_id = self.external_id

        refreshed_from_channel = self.refreshed_from_channel

        sections: list[str] | Unset = UNSET
        if not isinstance(self.sections, Unset):
            sections = self.sections



        failed_sections: list[str] | Unset = UNSET
        if not isinstance(self.failed_sections, Unset):
            failed_sections = self.failed_sections



        pulled_at: str | Unset = UNSET
        if not isinstance(self.pulled_at, Unset):
            pulled_at = self.pulled_at.isoformat()

        next_pull_available_at: str | Unset = UNSET
        if not isinstance(self.next_pull_available_at, Unset):
            next_pull_available_at = self.next_pull_available_at.isoformat()

        min_interval_seconds = self.min_interval_seconds


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if refreshed_from_channel is not UNSET:
            field_dict["refreshedFromChannel"] = refreshed_from_channel
        if sections is not UNSET:
            field_dict["sections"] = sections
        if failed_sections is not UNSET:
            field_dict["failedSections"] = failed_sections
        if pulled_at is not UNSET:
            field_dict["pulledAt"] = pulled_at
        if next_pull_available_at is not UNSET:
            field_dict["nextPullAvailableAt"] = next_pull_available_at
        if min_interval_seconds is not UNSET:
            field_dict["minIntervalSeconds"] = min_interval_seconds

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        listing_id = d.pop("listingId", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: PullListingFromVrboResponse200Channel | Unset
        if isinstance(_channel,  Unset):
            channel = UNSET
        else:
            channel = PullListingFromVrboResponse200Channel(_channel)




        def _parse_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_id = _parse_connection_id(d.pop("connectionId", UNSET))


        external_id = d.pop("externalId", UNSET)

        refreshed_from_channel = d.pop("refreshedFromChannel", UNSET)

        sections = cast(list[str], d.pop("sections", UNSET))


        failed_sections = cast(list[str], d.pop("failedSections", UNSET))


        _pulled_at = d.pop("pulledAt", UNSET)
        pulled_at: datetime.datetime | Unset
        if isinstance(_pulled_at,  Unset):
            pulled_at = UNSET
        else:
            pulled_at = isoparse(_pulled_at)




        _next_pull_available_at = d.pop("nextPullAvailableAt", UNSET)
        next_pull_available_at: datetime.datetime | Unset
        if isinstance(_next_pull_available_at,  Unset):
            next_pull_available_at = UNSET
        else:
            next_pull_available_at = isoparse(_next_pull_available_at)




        min_interval_seconds = d.pop("minIntervalSeconds", UNSET)

        pull_listing_from_vrbo_response_200 = cls(
            listing_id=listing_id,
            channel=channel,
            connection_id=connection_id,
            external_id=external_id,
            refreshed_from_channel=refreshed_from_channel,
            sections=sections,
            failed_sections=failed_sections,
            pulled_at=pulled_at,
            next_pull_available_at=next_pull_available_at,
            min_interval_seconds=min_interval_seconds,
        )


        pull_listing_from_vrbo_response_200.additional_properties = d
        return pull_listing_from_vrbo_response_200

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
