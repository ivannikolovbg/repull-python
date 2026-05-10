from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_status import ListingStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.listing_address import ListingAddress
  from ..models.listing_amenity import ListingAmenity
  from ..models.listing_channel import ListingChannel
  from ..models.listing_content import ListingContent
  from ..models.listing_details import ListingDetails





T = TypeVar("T", bound="Listing")



@_attrs_define
class Listing:
    """ A vacation rental listing in your Repull workspace.

        Attributes:
            id (str | Unset): Repull listing id
            name (str | Unset):  Example: I - Stafford Apartment.
            address (ListingAddress | Unset):
            thumbnail_url (None | str | Unset):
            status (ListingStatus | Unset):
            channels (list[ListingChannel] | Unset): Channels (Airbnb, Booking, VRBO, etc.) the listing is connected to.
            amenities (list[ListingAmenity] | Unset): Amenity rows for the listing. **Only present when the caller passes
                `?include=amenities`.** Empty array (`[]`) when the listing has no amenity rows.
            content (ListingContent | None | Unset): **Only present when the caller passes `?include=content`.** Sourced
                from `listings_descriptions` for the `en` locale. `null` when the listing has no description row stored (vs the
                field being absent — that signals the caller did not opt into the expansion).
            details (ListingDetails | None | Unset): **Only present when the caller passes `?include=details`.** Sourced
                from `listings_details`. `null` when the listing has no details row stored (vs the field being absent — that
                signals the caller did not opt into the expansion).
            created_at (datetime.datetime | Unset):
            updated_at (datetime.datetime | Unset):
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    address: ListingAddress | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    status: ListingStatus | Unset = UNSET
    channels: list[ListingChannel] | Unset = UNSET
    amenities: list[ListingAmenity] | Unset = UNSET
    content: ListingContent | None | Unset = UNSET
    details: ListingDetails | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_address import ListingAddress
        from ..models.listing_amenity import ListingAmenity
        from ..models.listing_channel import ListingChannel
        from ..models.listing_content import ListingContent
        from ..models.listing_details import ListingDetails
        id = self.id

        name = self.name

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        channels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = []
            for channels_item_data in self.channels:
                channels_item = channels_item_data.to_dict()
                channels.append(channels_item)



        amenities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.amenities, Unset):
            amenities = []
            for amenities_item_data in self.amenities:
                amenities_item = amenities_item_data.to_dict()
                amenities.append(amenities_item)



        content: dict[str, Any] | None | Unset
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, ListingContent):
            content = self.content.to_dict()
        else:
            content = self.content

        details: dict[str, Any] | None | Unset
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, ListingDetails):
            details = self.details.to_dict()
        else:
            details = self.details

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if address is not UNSET:
            field_dict["address"] = address
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url
        if status is not UNSET:
            field_dict["status"] = status
        if channels is not UNSET:
            field_dict["channels"] = channels
        if amenities is not UNSET:
            field_dict["amenities"] = amenities
        if content is not UNSET:
            field_dict["content"] = content
        if details is not UNSET:
            field_dict["details"] = details
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_address import ListingAddress
        from ..models.listing_amenity import ListingAmenity
        from ..models.listing_channel import ListingChannel
        from ..models.listing_content import ListingContent
        from ..models.listing_details import ListingDetails
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _address = d.pop("address", UNSET)
        address: ListingAddress | Unset
        if isinstance(_address,  Unset):
            address = UNSET
        else:
            address = ListingAddress.from_dict(_address)




        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))


        _status = d.pop("status", UNSET)
        status: ListingStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = ListingStatus(_status)




        _channels = d.pop("channels", UNSET)
        channels: list[ListingChannel] | Unset = UNSET
        if _channels is not UNSET:
            channels = []
            for channels_item_data in _channels:
                channels_item = ListingChannel.from_dict(channels_item_data)



                channels.append(channels_item)


        _amenities = d.pop("amenities", UNSET)
        amenities: list[ListingAmenity] | Unset = UNSET
        if _amenities is not UNSET:
            amenities = []
            for amenities_item_data in _amenities:
                amenities_item = ListingAmenity.from_dict(amenities_item_data)



                amenities.append(amenities_item)


        def _parse_content(data: object) -> ListingContent | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_1 = ListingContent.from_dict(data)



                return content_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingContent | None | Unset, data)

        content = _parse_content(d.pop("content", UNSET))


        def _parse_details(data: object) -> ListingDetails | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_1 = ListingDetails.from_dict(data)



                return details_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ListingDetails | None | Unset, data)

        details = _parse_details(d.pop("details", UNSET))


        _created_at = d.pop("createdAt", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)




        listing = cls(
            id=id,
            name=name,
            address=address,
            thumbnail_url=thumbnail_url,
            status=status,
            channels=channels,
            amenities=amenities,
            content=content,
            details=details,
            created_at=created_at,
            updated_at=updated_at,
        )


        listing.additional_properties = d
        return listing

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
