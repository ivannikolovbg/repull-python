from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.import_from_channex_response_201_data_channels_item_provider_switch import ImportFromChannexResponse201DataChannelsItemProviderSwitch
from ..models.import_from_channex_response_201_data_channels_item_status import ImportFromChannexResponse201DataChannelsItemStatus
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="ImportFromChannexResponse201DataChannelsItem")



@_attrs_define
class ImportFromChannexResponse201DataChannelsItem:
    """ 
        Attributes:
            channex_id (UUID | Unset): The Channex id, which keeps resolving on `/channex/api/v1`.
            title (None | str | Unset):
            status (ImportFromChannexResponse201DataChannelsItemStatus | Unset):
            detail (None | str | Unset): How it was matched, or what to do.
            repull_listing_id (int | None | Unset):
            channel (str | Unset): Channex adapter code (BookingCom, AirBNB, VRBO…).
            provider_switch (ImportFromChannexResponse201DataChannelsItemProviderSwitch | Unset):
            instructions (None | str | Unset):
     """

    channex_id: UUID | Unset = UNSET
    title: None | str | Unset = UNSET
    status: ImportFromChannexResponse201DataChannelsItemStatus | Unset = UNSET
    detail: None | str | Unset = UNSET
    repull_listing_id: int | None | Unset = UNSET
    channel: str | Unset = UNSET
    provider_switch: ImportFromChannexResponse201DataChannelsItemProviderSwitch | Unset = UNSET
    instructions: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        channex_id: str | Unset = UNSET
        if not isinstance(self.channex_id, Unset):
            channex_id = str(self.channex_id)

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        repull_listing_id: int | None | Unset
        if isinstance(self.repull_listing_id, Unset):
            repull_listing_id = UNSET
        else:
            repull_listing_id = self.repull_listing_id

        channel = self.channel

        provider_switch: str | Unset = UNSET
        if not isinstance(self.provider_switch, Unset):
            provider_switch = self.provider_switch.value


        instructions: None | str | Unset
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        else:
            instructions = self.instructions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if channex_id is not UNSET:
            field_dict["channexId"] = channex_id
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if detail is not UNSET:
            field_dict["detail"] = detail
        if repull_listing_id is not UNSET:
            field_dict["repullListingId"] = repull_listing_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if provider_switch is not UNSET:
            field_dict["providerSwitch"] = provider_switch
        if instructions is not UNSET:
            field_dict["instructions"] = instructions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _channex_id = d.pop("channexId", UNSET)
        channex_id: UUID | Unset
        if isinstance(_channex_id,  Unset):
            channex_id = UNSET
        else:
            channex_id = UUID(_channex_id)




        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        _status = d.pop("status", UNSET)
        status: ImportFromChannexResponse201DataChannelsItemStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ImportFromChannexResponse201DataChannelsItemStatus(_status)




        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))


        def _parse_repull_listing_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        repull_listing_id = _parse_repull_listing_id(d.pop("repullListingId", UNSET))


        channel = d.pop("channel", UNSET)

        _provider_switch = d.pop("providerSwitch", UNSET)
        provider_switch: ImportFromChannexResponse201DataChannelsItemProviderSwitch | Unset
        if isinstance(_provider_switch,  Unset):
            provider_switch = UNSET
        else:
            provider_switch = ImportFromChannexResponse201DataChannelsItemProviderSwitch(_provider_switch)




        def _parse_instructions(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))


        import_from_channex_response_201_data_channels_item = cls(
            channex_id=channex_id,
            title=title,
            status=status,
            detail=detail,
            repull_listing_id=repull_listing_id,
            channel=channel,
            provider_switch=provider_switch,
            instructions=instructions,
        )


        import_from_channex_response_201_data_channels_item.additional_properties = d
        return import_from_channex_response_201_data_channels_item

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
