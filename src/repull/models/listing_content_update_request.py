from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_content_update_request_photos_mode import ListingContentUpdateRequestPhotosMode
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.listing_content_update_request_address import ListingContentUpdateRequestAddress
  from ..models.listing_content_update_request_amenities_type_1_item import ListingContentUpdateRequestAmenitiesType1Item
  from ..models.listing_content_update_request_occupancy import ListingContentUpdateRequestOccupancy
  from ..models.listing_content_update_request_photos_item_type_1 import ListingContentUpdateRequestPhotosItemType1
  from ..models.listing_content_update_request_policies import ListingContentUpdateRequestPolicies





T = TypeVar("T", bound="ListingContentUpdateRequest")



@_attrs_define
class ListingContentUpdateRequest:
    """ Canonical PMS-owned listing content. Every field is optional — this is a partial update, only the fields you send
    are written; absent fields are left untouched. This is a LOCAL write only: it does NOT push to Airbnb/Booking.com.
    Distribution is a separate explicit publish step. `photos` are ingested by URL and attached to the listing in order
    (full-replace by default, or append via `photosMode`).

        Attributes:
            title (None | str | Unset): Guest-facing title. Written to the listing name and the `en` description.
            name (None | str | Unset): Alias for `title`.
            description (None | str | Unset): Long-form listing description.
            summary (None | str | Unset): Short summary / tagline.
            amenities (list[ListingContentUpdateRequestAmenitiesType1Item] | list[str] | Unset): FULL replacement of the
                amenity set. Accepts canonical keys as a string[] or structured rows. Omit to leave amenities untouched; send
                `[]` to clear them.
            address (ListingContentUpdateRequestAddress | Unset): Partial address. Only provided sub-fields are written.
            occupancy (ListingContentUpdateRequestOccupancy | Unset):
            policies (ListingContentUpdateRequestPolicies | Unset):
            photos (list[ListingContentUpdateRequestPhotosItemType1 | str] | Unset): Photo set — full replacement by default
                (pass `photosMode: "append"` to add after existing photos, or `[]` to clear; omit to leave untouched). Each
                entry is a hosted image URL (string) or a structured ref. URL-ingest only: the URL is persisted and attached to
                the listing in order — the OTA push downloads it at publish time. Binary/multipart upload is a follow-up. A non-
                empty array with no valid http(s) URL is reported in `deferred` (existing photos left untouched).
            photos_mode (ListingContentUpdateRequestPhotosMode | Unset): How `photos` is applied: `replace` (full
                replacement of the photo set) or `append` (add after the existing photos). Ignored when `photos` is absent.
                Default: ListingContentUpdateRequestPhotosMode.REPLACE.
     """

    title: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    summary: None | str | Unset = UNSET
    amenities: list[ListingContentUpdateRequestAmenitiesType1Item] | list[str] | Unset = UNSET
    address: ListingContentUpdateRequestAddress | Unset = UNSET
    occupancy: ListingContentUpdateRequestOccupancy | Unset = UNSET
    policies: ListingContentUpdateRequestPolicies | Unset = UNSET
    photos: list[ListingContentUpdateRequestPhotosItemType1 | str] | Unset = UNSET
    photos_mode: ListingContentUpdateRequestPhotosMode | Unset = ListingContentUpdateRequestPhotosMode.REPLACE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_content_update_request_address import ListingContentUpdateRequestAddress
        from ..models.listing_content_update_request_amenities_type_1_item import ListingContentUpdateRequestAmenitiesType1Item
        from ..models.listing_content_update_request_occupancy import ListingContentUpdateRequestOccupancy
        from ..models.listing_content_update_request_photos_item_type_1 import ListingContentUpdateRequestPhotosItemType1
        from ..models.listing_content_update_request_policies import ListingContentUpdateRequestPolicies
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        amenities: list[dict[str, Any]] | list[str] | Unset
        if isinstance(self.amenities, Unset):
            amenities = UNSET
        elif isinstance(self.amenities, list):
            amenities = self.amenities


        else:
            amenities = []
            for amenities_type_1_item_data in self.amenities:
                amenities_type_1_item = amenities_type_1_item_data.to_dict()
                amenities.append(amenities_type_1_item)




        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        occupancy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occupancy, Unset):
            occupancy = self.occupancy.to_dict()

        policies: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = self.policies.to_dict()

        photos: list[dict[str, Any] | str] | Unset = UNSET
        if not isinstance(self.photos, Unset):
            photos = []
            for photos_item_data in self.photos:
                photos_item: dict[str, Any] | str
                if isinstance(photos_item_data, ListingContentUpdateRequestPhotosItemType1):
                    photos_item = photos_item_data.to_dict()
                else:
                    photos_item = photos_item_data
                photos.append(photos_item)



        photos_mode: str | Unset = UNSET
        if not isinstance(self.photos_mode, Unset):
            photos_mode = self.photos_mode.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if title is not UNSET:
            field_dict["title"] = title
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if summary is not UNSET:
            field_dict["summary"] = summary
        if amenities is not UNSET:
            field_dict["amenities"] = amenities
        if address is not UNSET:
            field_dict["address"] = address
        if occupancy is not UNSET:
            field_dict["occupancy"] = occupancy
        if policies is not UNSET:
            field_dict["policies"] = policies
        if photos is not UNSET:
            field_dict["photos"] = photos
        if photos_mode is not UNSET:
            field_dict["photosMode"] = photos_mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_content_update_request_address import ListingContentUpdateRequestAddress
        from ..models.listing_content_update_request_amenities_type_1_item import ListingContentUpdateRequestAmenitiesType1Item
        from ..models.listing_content_update_request_occupancy import ListingContentUpdateRequestOccupancy
        from ..models.listing_content_update_request_photos_item_type_1 import ListingContentUpdateRequestPhotosItemType1
        from ..models.listing_content_update_request_policies import ListingContentUpdateRequestPolicies
        d = dict(src_dict)
        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))


        def _parse_amenities(data: object) -> list[ListingContentUpdateRequestAmenitiesType1Item] | list[str] | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                amenities_type_0 = cast(list[str], data)

                return amenities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            amenities_type_1 = []
            _amenities_type_1 = data
            for amenities_type_1_item_data in (_amenities_type_1):
                amenities_type_1_item = ListingContentUpdateRequestAmenitiesType1Item.from_dict(amenities_type_1_item_data)



                amenities_type_1.append(amenities_type_1_item)

            return amenities_type_1

        amenities = _parse_amenities(d.pop("amenities", UNSET))


        _address = d.pop("address", UNSET)
        address: ListingContentUpdateRequestAddress | Unset
        if isinstance(_address,  Unset):
            address = UNSET
        else:
            address = ListingContentUpdateRequestAddress.from_dict(_address)




        _occupancy = d.pop("occupancy", UNSET)
        occupancy: ListingContentUpdateRequestOccupancy | Unset
        if isinstance(_occupancy,  Unset):
            occupancy = UNSET
        else:
            occupancy = ListingContentUpdateRequestOccupancy.from_dict(_occupancy)




        _policies = d.pop("policies", UNSET)
        policies: ListingContentUpdateRequestPolicies | Unset
        if isinstance(_policies,  Unset):
            policies = UNSET
        else:
            policies = ListingContentUpdateRequestPolicies.from_dict(_policies)




        _photos = d.pop("photos", UNSET)
        photos: list[ListingContentUpdateRequestPhotosItemType1 | str] | Unset = UNSET
        if _photos is not UNSET:
            photos = []
            for photos_item_data in _photos:
                def _parse_photos_item(data: object) -> ListingContentUpdateRequestPhotosItemType1 | str:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        photos_item_type_1 = ListingContentUpdateRequestPhotosItemType1.from_dict(data)



                        return photos_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    return cast(ListingContentUpdateRequestPhotosItemType1 | str, data)

                photos_item = _parse_photos_item(photos_item_data)

                photos.append(photos_item)


        _photos_mode = d.pop("photosMode", UNSET)
        photos_mode: ListingContentUpdateRequestPhotosMode | Unset
        if isinstance(_photos_mode,  Unset):
            photos_mode = UNSET
        else:
            photos_mode = ListingContentUpdateRequestPhotosMode(_photos_mode)




        listing_content_update_request = cls(
            title=title,
            name=name,
            description=description,
            summary=summary,
            amenities=amenities,
            address=address,
            occupancy=occupancy,
            policies=policies,
            photos=photos,
            photos_mode=photos_mode,
        )


        listing_content_update_request.additional_properties = d
        return listing_content_update_request

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
