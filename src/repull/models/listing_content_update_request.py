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
  from ..models.listing_content_update_request_checkout_tasks_type_0_item import ListingContentUpdateRequestCheckoutTasksType0Item
  from ..models.listing_content_update_request_details import ListingContentUpdateRequestDetails
  from ..models.listing_content_update_request_occupancy import ListingContentUpdateRequestOccupancy
  from ..models.listing_content_update_request_photos_item_type_1 import ListingContentUpdateRequestPhotosItemType1
  from ..models.listing_content_update_request_policies import ListingContentUpdateRequestPolicies
  from ..models.listing_content_update_request_pricing import ListingContentUpdateRequestPricing
  from ..models.listing_content_update_request_rooms_type_0_item import ListingContentUpdateRequestRoomsType0Item





T = TypeVar("T", bound="ListingContentUpdateRequest")



@_attrs_define
class ListingContentUpdateRequest:
    """ Canonical PMS-owned listing content. Every field is optional — this is a partial update, only the fields you send
    are written; absent fields are left untouched. This is a LOCAL write only: it does NOT push to Airbnb/Booking.com.
    Distribution is a separate explicit publish step. `photos` are ingested by URL and attached to the listing in order
    (full-replace by default, or append via `photosMode`).

        Attributes:
            locale (str | Unset): Which language the `title` / `description` / `summary` / `policies.houseRules` in THIS
                request are written in. Defaults to `en`. Canonical content is stored per locale — one row per (listing, locale)
                — so sending Italian copy with `locale: "it"` creates or updates the Italian row instead of overwriting the
                English one. Distribution of a non-primary locale to Airbnb is a separate call: `PUT
                /v1/channels/airbnb/listings/{id}/descriptions`. Example: it.
            title (None | str | Unset): Guest-facing title. Written to the listing name and the description row for
                `locale`.
            name (None | str | Unset): Alias for `title`.
            description (None | str | Unset): Long-form listing description.
            summary (None | str | Unset): Short summary / tagline.
            amenities (list[ListingContentUpdateRequestAmenitiesType1Item] | list[str] | Unset): FULL replacement of the
                amenity set. Accepts canonical keys as a string[] or structured rows. Omit to leave amenities untouched; send
                `[]` to clear them.
            address (ListingContentUpdateRequestAddress | Unset): Partial address. Only provided sub-fields are written; the
                ones you omit keep their current value, and an explicit `null` clears one.

                This is also the repair path for a listing that cannot be published: Airbnb requires `street` and `city` for
                every country and additionally `state` and `postalCode` for a **US** property — and a listing with no
                `countryCode` behaves as US. Send just the missing part, e.g. `{ "address": { "state": "FL" } }`. `GET
                /v1/listings/{id}/publish-status` names what is missing.
            details (ListingContentUpdateRequestDetails | Unset): What KIND of property this is. The publish path reads all
                three on every push, so setting them here is the update path for a listing that already exists — `POST
                /v1/listings` could only set the type at creation. Airbnb may lock these on an established listing; the publish
                response reports that in `lockedFields`.
            occupancy (ListingContentUpdateRequestOccupancy | Unset):
            rooms (list[ListingContentUpdateRequestRoomsType0Item] | None | Unset): The listing's rooms and the beds in each
                — what Airbnb shows as the sleeping arrangements and needs before a listing can go live. FULL replacement: the
                rooms you send become the whole set. Omit to leave rooms untouched; send `[]` to clear them.

                Every entry is checked before anything is written, so a bad entry refuses the whole request with `422
                invalid_params` naming it (e.g. `rooms[1].beds[0].quantity`) — a listing is never left with half its rooms.

                Values use Airbnb's vocabulary, which Booking.com room mapping also reads. This is a local write; publish to
                send it to a channel.
            checkout_tasks (list[ListingContentUpdateRequestCheckoutTasksType0Item] | None | Unset): What the guest is asked
                to do before leaving. FULL replacement: omit to leave untouched; send `[]` to clear. An unknown `taskType`
                refuses the whole request with `422 invalid_params`.

                Published to Airbnb, which is the only channel with checkout tasks. Airbnb accepts them only from partner apps
                it has certified for the feature; until then the publish result reports Airbnb's own refusal for this section
                and every other section still lands.
            pricing (ListingContentUpdateRequestPricing | Unset): The listing's standing rates. Partial like every other
                section: only the fields you send are written, and `null` clears one.

                Changing `defaultDailyPrice` or `weekendPrice` also moves the nights on the calendar that still carry the old
                rate and were written by us — a night you or a channel priced yourself is never touched, and neither is a
                blocked or reserved one. So a price change reaches the calendar without overwriting anyone's work.

                This is still a local write. Publish to send the new rates to a channel.
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

    locale: str | Unset = UNSET
    title: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    summary: None | str | Unset = UNSET
    amenities: list[ListingContentUpdateRequestAmenitiesType1Item] | list[str] | Unset = UNSET
    address: ListingContentUpdateRequestAddress | Unset = UNSET
    details: ListingContentUpdateRequestDetails | Unset = UNSET
    occupancy: ListingContentUpdateRequestOccupancy | Unset = UNSET
    rooms: list[ListingContentUpdateRequestRoomsType0Item] | None | Unset = UNSET
    checkout_tasks: list[ListingContentUpdateRequestCheckoutTasksType0Item] | None | Unset = UNSET
    pricing: ListingContentUpdateRequestPricing | Unset = UNSET
    policies: ListingContentUpdateRequestPolicies | Unset = UNSET
    photos: list[ListingContentUpdateRequestPhotosItemType1 | str] | Unset = UNSET
    photos_mode: ListingContentUpdateRequestPhotosMode | Unset = ListingContentUpdateRequestPhotosMode.REPLACE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_content_update_request_address import ListingContentUpdateRequestAddress
        from ..models.listing_content_update_request_amenities_type_1_item import ListingContentUpdateRequestAmenitiesType1Item
        from ..models.listing_content_update_request_checkout_tasks_type_0_item import ListingContentUpdateRequestCheckoutTasksType0Item
        from ..models.listing_content_update_request_details import ListingContentUpdateRequestDetails
        from ..models.listing_content_update_request_occupancy import ListingContentUpdateRequestOccupancy
        from ..models.listing_content_update_request_photos_item_type_1 import ListingContentUpdateRequestPhotosItemType1
        from ..models.listing_content_update_request_policies import ListingContentUpdateRequestPolicies
        from ..models.listing_content_update_request_pricing import ListingContentUpdateRequestPricing
        from ..models.listing_content_update_request_rooms_type_0_item import ListingContentUpdateRequestRoomsType0Item
        locale = self.locale

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

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        occupancy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.occupancy, Unset):
            occupancy = self.occupancy.to_dict()

        rooms: list[dict[str, Any]] | None | Unset
        if isinstance(self.rooms, Unset):
            rooms = UNSET
        elif isinstance(self.rooms, list):
            rooms = []
            for rooms_type_0_item_data in self.rooms:
                rooms_type_0_item = rooms_type_0_item_data.to_dict()
                rooms.append(rooms_type_0_item)


        else:
            rooms = self.rooms

        checkout_tasks: list[dict[str, Any]] | None | Unset
        if isinstance(self.checkout_tasks, Unset):
            checkout_tasks = UNSET
        elif isinstance(self.checkout_tasks, list):
            checkout_tasks = []
            for checkout_tasks_type_0_item_data in self.checkout_tasks:
                checkout_tasks_type_0_item = checkout_tasks_type_0_item_data.to_dict()
                checkout_tasks.append(checkout_tasks_type_0_item)


        else:
            checkout_tasks = self.checkout_tasks

        pricing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

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
        if locale is not UNSET:
            field_dict["locale"] = locale
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
        if details is not UNSET:
            field_dict["details"] = details
        if occupancy is not UNSET:
            field_dict["occupancy"] = occupancy
        if rooms is not UNSET:
            field_dict["rooms"] = rooms
        if checkout_tasks is not UNSET:
            field_dict["checkoutTasks"] = checkout_tasks
        if pricing is not UNSET:
            field_dict["pricing"] = pricing
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
        from ..models.listing_content_update_request_checkout_tasks_type_0_item import ListingContentUpdateRequestCheckoutTasksType0Item
        from ..models.listing_content_update_request_details import ListingContentUpdateRequestDetails
        from ..models.listing_content_update_request_occupancy import ListingContentUpdateRequestOccupancy
        from ..models.listing_content_update_request_photos_item_type_1 import ListingContentUpdateRequestPhotosItemType1
        from ..models.listing_content_update_request_policies import ListingContentUpdateRequestPolicies
        from ..models.listing_content_update_request_pricing import ListingContentUpdateRequestPricing
        from ..models.listing_content_update_request_rooms_type_0_item import ListingContentUpdateRequestRoomsType0Item
        d = dict(src_dict)
        locale = d.pop("locale", UNSET)

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




        _details = d.pop("details", UNSET)
        details: ListingContentUpdateRequestDetails | Unset
        if isinstance(_details,  Unset):
            details = UNSET
        else:
            details = ListingContentUpdateRequestDetails.from_dict(_details)




        _occupancy = d.pop("occupancy", UNSET)
        occupancy: ListingContentUpdateRequestOccupancy | Unset
        if isinstance(_occupancy,  Unset):
            occupancy = UNSET
        else:
            occupancy = ListingContentUpdateRequestOccupancy.from_dict(_occupancy)




        def _parse_rooms(data: object) -> list[ListingContentUpdateRequestRoomsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                rooms_type_0 = []
                _rooms_type_0 = data
                for rooms_type_0_item_data in (_rooms_type_0):
                    rooms_type_0_item = ListingContentUpdateRequestRoomsType0Item.from_dict(rooms_type_0_item_data)



                    rooms_type_0.append(rooms_type_0_item)

                return rooms_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ListingContentUpdateRequestRoomsType0Item] | None | Unset, data)

        rooms = _parse_rooms(d.pop("rooms", UNSET))


        def _parse_checkout_tasks(data: object) -> list[ListingContentUpdateRequestCheckoutTasksType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                checkout_tasks_type_0 = []
                _checkout_tasks_type_0 = data
                for checkout_tasks_type_0_item_data in (_checkout_tasks_type_0):
                    checkout_tasks_type_0_item = ListingContentUpdateRequestCheckoutTasksType0Item.from_dict(checkout_tasks_type_0_item_data)



                    checkout_tasks_type_0.append(checkout_tasks_type_0_item)

                return checkout_tasks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ListingContentUpdateRequestCheckoutTasksType0Item] | None | Unset, data)

        checkout_tasks = _parse_checkout_tasks(d.pop("checkoutTasks", UNSET))


        _pricing = d.pop("pricing", UNSET)
        pricing: ListingContentUpdateRequestPricing | Unset
        if isinstance(_pricing,  Unset):
            pricing = UNSET
        else:
            pricing = ListingContentUpdateRequestPricing.from_dict(_pricing)




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
            locale=locale,
            title=title,
            name=name,
            description=description,
            summary=summary,
            amenities=amenities,
            address=address,
            details=details,
            occupancy=occupancy,
            rooms=rooms,
            checkout_tasks=checkout_tasks,
            pricing=pricing,
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
