from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.import_from_channex_response_201_data_environment import ImportFromChannexResponse201DataEnvironment
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.import_from_channex_response_201_data_channels_item import ImportFromChannexResponse201DataChannelsItem
  from ..models.import_from_channex_response_201_data_properties_item import ImportFromChannexResponse201DataPropertiesItem
  from ..models.import_from_channex_response_201_data_rate_plans_item import ImportFromChannexResponse201DataRatePlansItem
  from ..models.import_from_channex_response_201_data_room_types_item import ImportFromChannexResponse201DataRoomTypesItem
  from ..models.import_from_channex_response_201_data_signing_keys_item import ImportFromChannexResponse201DataSigningKeysItem
  from ..models.import_from_channex_response_201_data_summary import ImportFromChannexResponse201DataSummary
  from ..models.import_from_channex_response_201_data_webhooks_item import ImportFromChannexResponse201DataWebhooksItem





T = TypeVar("T", bound="ImportFromChannexResponse201Data")



@_attrs_define
class ImportFromChannexResponse201Data:
    """ 
        Attributes:
            id (UUID | Unset):
            environment (ImportFromChannexResponse201DataEnvironment | Unset):
            dry_run (bool | Unset):
            complete (bool | Unset): False when the time budget ran out; run the same request again to continue.
            started_at (datetime.datetime | Unset):
            finished_at (datetime.datetime | Unset):
            summary (ImportFromChannexResponse201DataSummary | Unset):
            properties (list[ImportFromChannexResponse201DataPropertiesItem] | Unset):
            room_types (list[ImportFromChannexResponse201DataRoomTypesItem] | Unset):
            rate_plans (list[ImportFromChannexResponse201DataRatePlansItem] | Unset):
            webhooks (list[ImportFromChannexResponse201DataWebhooksItem] | Unset):
            signing_keys (list[ImportFromChannexResponse201DataSigningKeysItem] | Unset):
            channels (list[ImportFromChannexResponse201DataChannelsItem] | Unset):
            warnings (list[str] | Unset):
            next_steps (list[str] | Unset):
     """

    id: UUID | Unset = UNSET
    environment: ImportFromChannexResponse201DataEnvironment | Unset = UNSET
    dry_run: bool | Unset = UNSET
    complete: bool | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    finished_at: datetime.datetime | Unset = UNSET
    summary: ImportFromChannexResponse201DataSummary | Unset = UNSET
    properties: list[ImportFromChannexResponse201DataPropertiesItem] | Unset = UNSET
    room_types: list[ImportFromChannexResponse201DataRoomTypesItem] | Unset = UNSET
    rate_plans: list[ImportFromChannexResponse201DataRatePlansItem] | Unset = UNSET
    webhooks: list[ImportFromChannexResponse201DataWebhooksItem] | Unset = UNSET
    signing_keys: list[ImportFromChannexResponse201DataSigningKeysItem] | Unset = UNSET
    channels: list[ImportFromChannexResponse201DataChannelsItem] | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    next_steps: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.import_from_channex_response_201_data_channels_item import ImportFromChannexResponse201DataChannelsItem
        from ..models.import_from_channex_response_201_data_properties_item import ImportFromChannexResponse201DataPropertiesItem
        from ..models.import_from_channex_response_201_data_rate_plans_item import ImportFromChannexResponse201DataRatePlansItem
        from ..models.import_from_channex_response_201_data_room_types_item import ImportFromChannexResponse201DataRoomTypesItem
        from ..models.import_from_channex_response_201_data_signing_keys_item import ImportFromChannexResponse201DataSigningKeysItem
        from ..models.import_from_channex_response_201_data_summary import ImportFromChannexResponse201DataSummary
        from ..models.import_from_channex_response_201_data_webhooks_item import ImportFromChannexResponse201DataWebhooksItem
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        environment: str | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value


        dry_run = self.dry_run

        complete = self.complete

        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        finished_at: str | Unset = UNSET
        if not isinstance(self.finished_at, Unset):
            finished_at = self.finished_at.isoformat()

        summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)



        room_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.room_types, Unset):
            room_types = []
            for room_types_item_data in self.room_types:
                room_types_item = room_types_item_data.to_dict()
                room_types.append(room_types_item)



        rate_plans: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rate_plans, Unset):
            rate_plans = []
            for rate_plans_item_data in self.rate_plans:
                rate_plans_item = rate_plans_item_data.to_dict()
                rate_plans.append(rate_plans_item)



        webhooks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.webhooks, Unset):
            webhooks = []
            for webhooks_item_data in self.webhooks:
                webhooks_item = webhooks_item_data.to_dict()
                webhooks.append(webhooks_item)



        signing_keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.signing_keys, Unset):
            signing_keys = []
            for signing_keys_item_data in self.signing_keys:
                signing_keys_item = signing_keys_item_data.to_dict()
                signing_keys.append(signing_keys_item)



        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)



        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings



        next_steps: list[str] | Unset = UNSET
        if not isinstance(self.next_steps, Unset):
            next_steps = self.next_steps




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if environment is not UNSET:
            field_dict["environment"] = environment
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run
        if complete is not UNSET:
            field_dict["complete"] = complete
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at
        if summary is not UNSET:
            field_dict["summary"] = summary
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
        if warnings is not UNSET:
            field_dict["warnings"] = warnings
        if next_steps is not UNSET:
            field_dict["nextSteps"] = next_steps

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_from_channex_response_201_data_channels_item import ImportFromChannexResponse201DataChannelsItem
        from ..models.import_from_channex_response_201_data_properties_item import ImportFromChannexResponse201DataPropertiesItem
        from ..models.import_from_channex_response_201_data_rate_plans_item import ImportFromChannexResponse201DataRatePlansItem
        from ..models.import_from_channex_response_201_data_room_types_item import ImportFromChannexResponse201DataRoomTypesItem
        from ..models.import_from_channex_response_201_data_signing_keys_item import ImportFromChannexResponse201DataSigningKeysItem
        from ..models.import_from_channex_response_201_data_summary import ImportFromChannexResponse201DataSummary
        from ..models.import_from_channex_response_201_data_webhooks_item import ImportFromChannexResponse201DataWebhooksItem
        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id,  Unset):
            id = UNSET
        else:
            id = UUID(_id)




        _environment = d.pop("environment", UNSET)
        environment: ImportFromChannexResponse201DataEnvironment | Unset
        if isinstance(_environment,  Unset):
            environment = UNSET
        else:
            environment = ImportFromChannexResponse201DataEnvironment(_environment)




        dry_run = d.pop("dryRun", UNSET)

        complete = d.pop("complete", UNSET)

        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)




        _finished_at = d.pop("finishedAt", UNSET)
        finished_at: datetime.datetime | Unset
        if isinstance(_finished_at,  Unset):
            finished_at = UNSET
        else:
            finished_at = isoparse(_finished_at)




        _summary = d.pop("summary", UNSET)
        summary: ImportFromChannexResponse201DataSummary | Unset
        if isinstance(_summary,  Unset):
            summary = UNSET
        else:
            summary = ImportFromChannexResponse201DataSummary.from_dict(_summary)




        _properties = d.pop("properties", UNSET)
        properties: list[ImportFromChannexResponse201DataPropertiesItem] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = ImportFromChannexResponse201DataPropertiesItem.from_dict(properties_item_data)



                properties.append(properties_item)


        _room_types = d.pop("roomTypes", UNSET)
        room_types: list[ImportFromChannexResponse201DataRoomTypesItem] | Unset = UNSET
        if _room_types is not UNSET:
            room_types = []
            for room_types_item_data in _room_types:
                room_types_item = ImportFromChannexResponse201DataRoomTypesItem.from_dict(room_types_item_data)



                room_types.append(room_types_item)


        _rate_plans = d.pop("ratePlans", UNSET)
        rate_plans: list[ImportFromChannexResponse201DataRatePlansItem] | Unset = UNSET
        if _rate_plans is not UNSET:
            rate_plans = []
            for rate_plans_item_data in _rate_plans:
                rate_plans_item = ImportFromChannexResponse201DataRatePlansItem.from_dict(rate_plans_item_data)



                rate_plans.append(rate_plans_item)


        _webhooks = d.pop("webhooks", UNSET)
        webhooks: list[ImportFromChannexResponse201DataWebhooksItem] | Unset = UNSET
        if _webhooks is not UNSET:
            webhooks = []
            for webhooks_item_data in _webhooks:
                webhooks_item = ImportFromChannexResponse201DataWebhooksItem.from_dict(webhooks_item_data)



                webhooks.append(webhooks_item)


        _signing_keys = d.pop("signingKeys", UNSET)
        signing_keys: list[ImportFromChannexResponse201DataSigningKeysItem] | Unset = UNSET
        if _signing_keys is not UNSET:
            signing_keys = []
            for signing_keys_item_data in _signing_keys:
                signing_keys_item = ImportFromChannexResponse201DataSigningKeysItem.from_dict(signing_keys_item_data)



                signing_keys.append(signing_keys_item)


        _channels = d.pop("channels", UNSET)
        channels: list[ImportFromChannexResponse201DataChannelsItem] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = ImportFromChannexResponse201DataChannelsItem.from_dict(channels_item_data)



                channels.append(channels_item)


        warnings = cast(list[str], d.pop("warnings", UNSET))


        next_steps = cast(list[str], d.pop("nextSteps", UNSET))


        import_from_channex_response_201_data = cls(
            id=id,
            environment=environment,
            dry_run=dry_run,
            complete=complete,
            started_at=started_at,
            finished_at=finished_at,
            summary=summary,
            properties=properties,
            room_types=room_types,
            rate_plans=rate_plans,
            webhooks=webhooks,
            signing_keys=signing_keys,
            channels=channels,
            warnings=warnings,
            next_steps=next_steps,
        )


        import_from_channex_response_201_data.additional_properties = d
        return import_from_channex_response_201_data

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
