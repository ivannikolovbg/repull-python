from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.import_from_channex_response_200_data_summary_bookings import ImportFromChannexResponse200DataSummaryBookings
  from ..models.import_from_channex_response_200_data_summary_channels import ImportFromChannexResponse200DataSummaryChannels
  from ..models.import_from_channex_response_200_data_summary_properties import ImportFromChannexResponse200DataSummaryProperties
  from ..models.import_from_channex_response_200_data_summary_rate_plans import ImportFromChannexResponse200DataSummaryRatePlans
  from ..models.import_from_channex_response_200_data_summary_room_types import ImportFromChannexResponse200DataSummaryRoomTypes
  from ..models.import_from_channex_response_200_data_summary_signing_keys import ImportFromChannexResponse200DataSummarySigningKeys
  from ..models.import_from_channex_response_200_data_summary_webhooks import ImportFromChannexResponse200DataSummaryWebhooks





T = TypeVar("T", bound="ImportFromChannexResponse200DataSummary")



@_attrs_define
class ImportFromChannexResponse200DataSummary:
    """ 
        Attributes:
            properties (ImportFromChannexResponse200DataSummaryProperties | Unset):
            room_types (ImportFromChannexResponse200DataSummaryRoomTypes | Unset):
            rate_plans (ImportFromChannexResponse200DataSummaryRatePlans | Unset):
            webhooks (ImportFromChannexResponse200DataSummaryWebhooks | Unset):
            signing_keys (ImportFromChannexResponse200DataSummarySigningKeys | Unset):
            channels (ImportFromChannexResponse200DataSummaryChannels | Unset):
            bookings (ImportFromChannexResponse200DataSummaryBookings | Unset):
     """

    properties: ImportFromChannexResponse200DataSummaryProperties | Unset = UNSET
    room_types: ImportFromChannexResponse200DataSummaryRoomTypes | Unset = UNSET
    rate_plans: ImportFromChannexResponse200DataSummaryRatePlans | Unset = UNSET
    webhooks: ImportFromChannexResponse200DataSummaryWebhooks | Unset = UNSET
    signing_keys: ImportFromChannexResponse200DataSummarySigningKeys | Unset = UNSET
    channels: ImportFromChannexResponse200DataSummaryChannels | Unset = UNSET
    bookings: ImportFromChannexResponse200DataSummaryBookings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_from_channex_response_200_data_summary_bookings import ImportFromChannexResponse200DataSummaryBookings
        from ..models.import_from_channex_response_200_data_summary_channels import ImportFromChannexResponse200DataSummaryChannels
        from ..models.import_from_channex_response_200_data_summary_properties import ImportFromChannexResponse200DataSummaryProperties
        from ..models.import_from_channex_response_200_data_summary_rate_plans import ImportFromChannexResponse200DataSummaryRatePlans
        from ..models.import_from_channex_response_200_data_summary_room_types import ImportFromChannexResponse200DataSummaryRoomTypes
        from ..models.import_from_channex_response_200_data_summary_signing_keys import ImportFromChannexResponse200DataSummarySigningKeys
        from ..models.import_from_channex_response_200_data_summary_webhooks import ImportFromChannexResponse200DataSummaryWebhooks
        properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        room_types: dict[str, Any] | Unset = UNSET
        if not isinstance(self.room_types, Unset):
            room_types = self.room_types.to_dict()

        rate_plans: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_plans, Unset):
            rate_plans = self.rate_plans.to_dict()

        webhooks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webhooks, Unset):
            webhooks = self.webhooks.to_dict()

        signing_keys: dict[str, Any] | Unset = UNSET
        if not isinstance(self.signing_keys, Unset):
            signing_keys = self.signing_keys.to_dict()

        channels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels.to_dict()

        bookings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bookings, Unset):
            bookings = self.bookings.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if properties is not UNSET:
            field_dict["properties"] = properties
        if room_types is not UNSET:
            field_dict["roomTypes"] = room_types
        if rate_plans is not UNSET:
            field_dict["ratePlans"] = rate_plans
        if webhooks is not UNSET:
            field_dict["webhooks"] = webhooks
        if signing_keys is not UNSET:
            field_dict["signingKeys"] = signing_keys
        if channels is not UNSET:
            field_dict["channels"] = channels
        if bookings is not UNSET:
            field_dict["bookings"] = bookings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_from_channex_response_200_data_summary_bookings import ImportFromChannexResponse200DataSummaryBookings
        from ..models.import_from_channex_response_200_data_summary_channels import ImportFromChannexResponse200DataSummaryChannels
        from ..models.import_from_channex_response_200_data_summary_properties import ImportFromChannexResponse200DataSummaryProperties
        from ..models.import_from_channex_response_200_data_summary_rate_plans import ImportFromChannexResponse200DataSummaryRatePlans
        from ..models.import_from_channex_response_200_data_summary_room_types import ImportFromChannexResponse200DataSummaryRoomTypes
        from ..models.import_from_channex_response_200_data_summary_signing_keys import ImportFromChannexResponse200DataSummarySigningKeys
        from ..models.import_from_channex_response_200_data_summary_webhooks import ImportFromChannexResponse200DataSummaryWebhooks
        d = dict(src_dict)
        _properties = d.pop("properties", UNSET)
        properties: ImportFromChannexResponse200DataSummaryProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = ImportFromChannexResponse200DataSummaryProperties.from_dict(_properties)




        _room_types = d.pop("roomTypes", UNSET)
        room_types: ImportFromChannexResponse200DataSummaryRoomTypes | Unset
        if isinstance(_room_types,  Unset):
            room_types = UNSET
        else:
            room_types = ImportFromChannexResponse200DataSummaryRoomTypes.from_dict(_room_types)




        _rate_plans = d.pop("ratePlans", UNSET)
        rate_plans: ImportFromChannexResponse200DataSummaryRatePlans | Unset
        if isinstance(_rate_plans,  Unset):
            rate_plans = UNSET
        else:
            rate_plans = ImportFromChannexResponse200DataSummaryRatePlans.from_dict(_rate_plans)




        _webhooks = d.pop("webhooks", UNSET)
        webhooks: ImportFromChannexResponse200DataSummaryWebhooks | Unset
        if isinstance(_webhooks,  Unset):
            webhooks = UNSET
        else:
            webhooks = ImportFromChannexResponse200DataSummaryWebhooks.from_dict(_webhooks)




        _signing_keys = d.pop("signingKeys", UNSET)
        signing_keys: ImportFromChannexResponse200DataSummarySigningKeys | Unset
        if isinstance(_signing_keys,  Unset):
            signing_keys = UNSET
        else:
            signing_keys = ImportFromChannexResponse200DataSummarySigningKeys.from_dict(_signing_keys)




        _channels = d.pop("channels", UNSET)
        channels: ImportFromChannexResponse200DataSummaryChannels | Unset
        if isinstance(_channels,  Unset):
            channels = UNSET
        else:
            channels = ImportFromChannexResponse200DataSummaryChannels.from_dict(_channels)




        _bookings = d.pop("bookings", UNSET)
        bookings: ImportFromChannexResponse200DataSummaryBookings | Unset
        if isinstance(_bookings,  Unset):
            bookings = UNSET
        else:
            bookings = ImportFromChannexResponse200DataSummaryBookings.from_dict(_bookings)




        import_from_channex_response_200_data_summary = cls(
            properties=properties,
            room_types=room_types,
            rate_plans=rate_plans,
            webhooks=webhooks,
            signing_keys=signing_keys,
            channels=channels,
            bookings=bookings,
        )


        import_from_channex_response_200_data_summary.additional_properties = d
        return import_from_channex_response_200_data_summary

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
