from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.import_from_channex_response_201_data_summary_bookings import ImportFromChannexResponse201DataSummaryBookings
  from ..models.import_from_channex_response_201_data_summary_channels import ImportFromChannexResponse201DataSummaryChannels
  from ..models.import_from_channex_response_201_data_summary_properties import ImportFromChannexResponse201DataSummaryProperties
  from ..models.import_from_channex_response_201_data_summary_rate_plans import ImportFromChannexResponse201DataSummaryRatePlans
  from ..models.import_from_channex_response_201_data_summary_room_types import ImportFromChannexResponse201DataSummaryRoomTypes
  from ..models.import_from_channex_response_201_data_summary_signing_keys import ImportFromChannexResponse201DataSummarySigningKeys
  from ..models.import_from_channex_response_201_data_summary_webhooks import ImportFromChannexResponse201DataSummaryWebhooks





T = TypeVar("T", bound="ImportFromChannexResponse201DataSummary")



@_attrs_define
class ImportFromChannexResponse201DataSummary:
    """ 
        Attributes:
            properties (ImportFromChannexResponse201DataSummaryProperties | Unset):
            room_types (ImportFromChannexResponse201DataSummaryRoomTypes | Unset):
            rate_plans (ImportFromChannexResponse201DataSummaryRatePlans | Unset):
            webhooks (ImportFromChannexResponse201DataSummaryWebhooks | Unset):
            signing_keys (ImportFromChannexResponse201DataSummarySigningKeys | Unset):
            channels (ImportFromChannexResponse201DataSummaryChannels | Unset):
            bookings (ImportFromChannexResponse201DataSummaryBookings | Unset):
     """

    properties: ImportFromChannexResponse201DataSummaryProperties | Unset = UNSET
    room_types: ImportFromChannexResponse201DataSummaryRoomTypes | Unset = UNSET
    rate_plans: ImportFromChannexResponse201DataSummaryRatePlans | Unset = UNSET
    webhooks: ImportFromChannexResponse201DataSummaryWebhooks | Unset = UNSET
    signing_keys: ImportFromChannexResponse201DataSummarySigningKeys | Unset = UNSET
    channels: ImportFromChannexResponse201DataSummaryChannels | Unset = UNSET
    bookings: ImportFromChannexResponse201DataSummaryBookings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_from_channex_response_201_data_summary_bookings import ImportFromChannexResponse201DataSummaryBookings
        from ..models.import_from_channex_response_201_data_summary_channels import ImportFromChannexResponse201DataSummaryChannels
        from ..models.import_from_channex_response_201_data_summary_properties import ImportFromChannexResponse201DataSummaryProperties
        from ..models.import_from_channex_response_201_data_summary_rate_plans import ImportFromChannexResponse201DataSummaryRatePlans
        from ..models.import_from_channex_response_201_data_summary_room_types import ImportFromChannexResponse201DataSummaryRoomTypes
        from ..models.import_from_channex_response_201_data_summary_signing_keys import ImportFromChannexResponse201DataSummarySigningKeys
        from ..models.import_from_channex_response_201_data_summary_webhooks import ImportFromChannexResponse201DataSummaryWebhooks
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
        from ..models.import_from_channex_response_201_data_summary_bookings import ImportFromChannexResponse201DataSummaryBookings
        from ..models.import_from_channex_response_201_data_summary_channels import ImportFromChannexResponse201DataSummaryChannels
        from ..models.import_from_channex_response_201_data_summary_properties import ImportFromChannexResponse201DataSummaryProperties
        from ..models.import_from_channex_response_201_data_summary_rate_plans import ImportFromChannexResponse201DataSummaryRatePlans
        from ..models.import_from_channex_response_201_data_summary_room_types import ImportFromChannexResponse201DataSummaryRoomTypes
        from ..models.import_from_channex_response_201_data_summary_signing_keys import ImportFromChannexResponse201DataSummarySigningKeys
        from ..models.import_from_channex_response_201_data_summary_webhooks import ImportFromChannexResponse201DataSummaryWebhooks
        d = dict(src_dict)
        _properties = d.pop("properties", UNSET)
        properties: ImportFromChannexResponse201DataSummaryProperties | Unset
        if isinstance(_properties,  Unset):
            properties = UNSET
        else:
            properties = ImportFromChannexResponse201DataSummaryProperties.from_dict(_properties)




        _room_types = d.pop("roomTypes", UNSET)
        room_types: ImportFromChannexResponse201DataSummaryRoomTypes | Unset
        if isinstance(_room_types,  Unset):
            room_types = UNSET
        else:
            room_types = ImportFromChannexResponse201DataSummaryRoomTypes.from_dict(_room_types)




        _rate_plans = d.pop("ratePlans", UNSET)
        rate_plans: ImportFromChannexResponse201DataSummaryRatePlans | Unset
        if isinstance(_rate_plans,  Unset):
            rate_plans = UNSET
        else:
            rate_plans = ImportFromChannexResponse201DataSummaryRatePlans.from_dict(_rate_plans)




        _webhooks = d.pop("webhooks", UNSET)
        webhooks: ImportFromChannexResponse201DataSummaryWebhooks | Unset
        if isinstance(_webhooks,  Unset):
            webhooks = UNSET
        else:
            webhooks = ImportFromChannexResponse201DataSummaryWebhooks.from_dict(_webhooks)




        _signing_keys = d.pop("signingKeys", UNSET)
        signing_keys: ImportFromChannexResponse201DataSummarySigningKeys | Unset
        if isinstance(_signing_keys,  Unset):
            signing_keys = UNSET
        else:
            signing_keys = ImportFromChannexResponse201DataSummarySigningKeys.from_dict(_signing_keys)




        _channels = d.pop("channels", UNSET)
        channels: ImportFromChannexResponse201DataSummaryChannels | Unset
        if isinstance(_channels,  Unset):
            channels = UNSET
        else:
            channels = ImportFromChannexResponse201DataSummaryChannels.from_dict(_channels)




        _bookings = d.pop("bookings", UNSET)
        bookings: ImportFromChannexResponse201DataSummaryBookings | Unset
        if isinstance(_bookings,  Unset):
            bookings = UNSET
        else:
            bookings = ImportFromChannexResponse201DataSummaryBookings.from_dict(_bookings)




        import_from_channex_response_201_data_summary = cls(
            properties=properties,
            room_types=room_types,
            rate_plans=rate_plans,
            webhooks=webhooks,
            signing_keys=signing_keys,
            channels=channels,
            bookings=bookings,
        )


        import_from_channex_response_201_data_summary.additional_properties = d
        return import_from_channex_response_201_data_summary

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
