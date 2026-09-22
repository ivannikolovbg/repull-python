from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.listing_webhook_object_address import ListingWebhookObjectAddress
  from ..models.listing_webhook_object_channels_item import ListingWebhookObjectChannelsItem





T = TypeVar("T", bound="ListingWebhookObject")



@_attrs_define
class ListingWebhookObject:
    """ The listing, in the shape `GET /v1/listings/{id}` returns. Hydrated at delivery, so a receiver gets the listing
    rather than a reason to fetch one.

        Attributes:
            id (str):  Example: 6250.
            customer_id (int):  Example: 1.
            channel (None | str | Unset):  Example: airbnb.
            external_listing_id (None | str | Unset): The channel's own listing id. Airbnb's exceed 2^53, so always a
                string. Example: 1234567890123456789.
            name (None | str | Unset):  Example: R-Sable 1302 — Radium Hot Springs.
            active (bool | Unset):  Example: True.
            status (str | Unset):  Example: active.
            address (ListingWebhookObjectAddress | Unset):
            thumbnail_url (None | str | Unset):
            channels (list[ListingWebhookObjectChannelsItem] | Unset): Which channels this listing is on and whether each
                still accepts writes. `syncEnabled: false` means the channel refuses every write for this listing — the
                difference between a failing integration and a suspended listing.
            created_at (datetime.datetime | None | Unset):
            updated_at (datetime.datetime | None | Unset):
     """

    id: str
    customer_id: int
    channel: None | str | Unset = UNSET
    external_listing_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    active: bool | Unset = UNSET
    status: str | Unset = UNSET
    address: ListingWebhookObjectAddress | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    channels: list[ListingWebhookObjectChannelsItem] | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_webhook_object_address import ListingWebhookObjectAddress
        from ..models.listing_webhook_object_channels_item import ListingWebhookObjectChannelsItem
        id = self.id

        customer_id = self.customer_id

        channel: None | str | Unset
        if isinstance(self.channel, Unset):
            channel = UNSET
        else:
            channel = self.channel

        external_listing_id: None | str | Unset
        if isinstance(self.external_listing_id, Unset):
            external_listing_id = UNSET
        else:
            external_listing_id = self.external_listing_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        active = self.active

        status = self.status

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)



        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "customerId": customer_id,
        })
        if channel is not UNSET:
            field_dict["channel"] = channel
        if external_listing_id is not UNSET:
            field_dict["externalListingId"] = external_listing_id
        if name is not UNSET:
            field_dict["name"] = name
        if active is not UNSET:
            field_dict["active"] = active
        if status is not UNSET:
            field_dict["status"] = status
        if address is not UNSET:
            field_dict["address"] = address
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url
        if channels is not UNSET:
            field_dict["channels"] = channels
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_webhook_object_address import ListingWebhookObjectAddress
        from ..models.listing_webhook_object_channels_item import ListingWebhookObjectChannelsItem
        d = dict(src_dict)
        id = d.pop("id")

        customer_id = d.pop("customerId")

        def _parse_channel(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        channel = _parse_channel(d.pop("channel", UNSET))


        def _parse_external_listing_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_listing_id = _parse_external_listing_id(d.pop("externalListingId", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        active = d.pop("active", UNSET)

        status = d.pop("status", UNSET)

        _address = d.pop("address", UNSET)
        address: ListingWebhookObjectAddress | Unset
        if isinstance(_address,  Unset):
            address = UNSET
        else:
            address = ListingWebhookObjectAddress.from_dict(_address)




        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))


        _channels = d.pop("channels", UNSET)
        channels: list[ListingWebhookObjectChannelsItem] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = ListingWebhookObjectChannelsItem.from_dict(channels_item_data)



                channels.append(channels_item)


        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        listing_webhook_object = cls(
            id=id,
            customer_id=customer_id,
            channel=channel,
            external_listing_id=external_listing_id,
            name=name,
            active=active,
            status=status,
            address=address,
            thumbnail_url=thumbnail_url,
            channels=channels,
            created_at=created_at,
            updated_at=updated_at,
        )


        listing_webhook_object.additional_properties = d
        return listing_webhook_object

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
