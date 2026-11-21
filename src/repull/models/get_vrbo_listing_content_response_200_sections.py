from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_content_response_200_sections_additional_info import GetVrboListingContentResponse200SectionsAdditionalInfo
  from ..models.get_vrbo_listing_content_response_200_sections_amenities import GetVrboListingContentResponse200SectionsAmenities
  from ..models.get_vrbo_listing_content_response_200_sections_booking_settings import GetVrboListingContentResponse200SectionsBookingSettings
  from ..models.get_vrbo_listing_content_response_200_sections_cancellation import GetVrboListingContentResponse200SectionsCancellation
  from ..models.get_vrbo_listing_content_response_200_sections_checkin_guide import GetVrboListingContentResponse200SectionsCheckinGuide
  from ..models.get_vrbo_listing_content_response_200_sections_descriptions_item import GetVrboListingContentResponse200SectionsDescriptionsItem
  from ..models.get_vrbo_listing_content_response_200_sections_details import GetVrboListingContentResponse200SectionsDetails
  from ..models.get_vrbo_listing_content_response_200_sections_fees import GetVrboListingContentResponse200SectionsFees
  from ..models.get_vrbo_listing_content_response_200_sections_house_rules import GetVrboListingContentResponse200SectionsHouseRules
  from ..models.get_vrbo_listing_content_response_200_sections_location import GetVrboListingContentResponse200SectionsLocation
  from ..models.get_vrbo_listing_content_response_200_sections_payment_terms import GetVrboListingContentResponse200SectionsPaymentTerms
  from ..models.get_vrbo_listing_content_response_200_sections_permits import GetVrboListingContentResponse200SectionsPermits
  from ..models.get_vrbo_listing_content_response_200_sections_photos import GetVrboListingContentResponse200SectionsPhotos
  from ..models.get_vrbo_listing_content_response_200_sections_pricing import GetVrboListingContentResponse200SectionsPricing
  from ..models.get_vrbo_listing_content_response_200_sections_protection import GetVrboListingContentResponse200SectionsProtection
  from ..models.get_vrbo_listing_content_response_200_sections_rooms import GetVrboListingContentResponse200SectionsRooms
  from ..models.get_vrbo_listing_content_response_200_sections_story import GetVrboListingContentResponse200SectionsStory
  from ..models.get_vrbo_listing_content_response_200_sections_taxes import GetVrboListingContentResponse200SectionsTaxes
  from ..models.get_vrbo_listing_content_response_200_sections_videos import GetVrboListingContentResponse200SectionsVideos





T = TypeVar("T", bound="GetVrboListingContentResponse200Sections")



@_attrs_define
class GetVrboListingContentResponse200Sections:
    """ Keyed by section; each is the `data` of `GET /v1/channels/vrbo/listings/{id}/{section}`, or `{ error: { code,
    message } }` when that section failed.

        Attributes:
            descriptions (list[GetVrboListingContentResponse200SectionsDescriptionsItem] | Unset):
            details (GetVrboListingContentResponse200SectionsDetails | Unset):
            story (GetVrboListingContentResponse200SectionsStory | Unset):
            additional_info (GetVrboListingContentResponse200SectionsAdditionalInfo | Unset):
            photos (GetVrboListingContentResponse200SectionsPhotos | Unset):
            amenities (GetVrboListingContentResponse200SectionsAmenities | Unset):
            rooms (GetVrboListingContentResponse200SectionsRooms | Unset):
            location (GetVrboListingContentResponse200SectionsLocation | Unset):
            house_rules (GetVrboListingContentResponse200SectionsHouseRules | Unset):
            booking_settings (GetVrboListingContentResponse200SectionsBookingSettings | Unset):
            cancellation (GetVrboListingContentResponse200SectionsCancellation | Unset):
            fees (GetVrboListingContentResponse200SectionsFees | Unset):
            pricing (GetVrboListingContentResponse200SectionsPricing | Unset):
            payment_terms (GetVrboListingContentResponse200SectionsPaymentTerms | Unset):
            protection (GetVrboListingContentResponse200SectionsProtection | Unset):
            taxes (GetVrboListingContentResponse200SectionsTaxes | Unset):
            permits (GetVrboListingContentResponse200SectionsPermits | Unset):
            checkin_guide (GetVrboListingContentResponse200SectionsCheckinGuide | Unset):
            videos (GetVrboListingContentResponse200SectionsVideos | Unset):
     """

    descriptions: list[GetVrboListingContentResponse200SectionsDescriptionsItem] | Unset = UNSET
    details: GetVrboListingContentResponse200SectionsDetails | Unset = UNSET
    story: GetVrboListingContentResponse200SectionsStory | Unset = UNSET
    additional_info: GetVrboListingContentResponse200SectionsAdditionalInfo | Unset = UNSET
    photos: GetVrboListingContentResponse200SectionsPhotos | Unset = UNSET
    amenities: GetVrboListingContentResponse200SectionsAmenities | Unset = UNSET
    rooms: GetVrboListingContentResponse200SectionsRooms | Unset = UNSET
    location: GetVrboListingContentResponse200SectionsLocation | Unset = UNSET
    house_rules: GetVrboListingContentResponse200SectionsHouseRules | Unset = UNSET
    booking_settings: GetVrboListingContentResponse200SectionsBookingSettings | Unset = UNSET
    cancellation: GetVrboListingContentResponse200SectionsCancellation | Unset = UNSET
    fees: GetVrboListingContentResponse200SectionsFees | Unset = UNSET
    pricing: GetVrboListingContentResponse200SectionsPricing | Unset = UNSET
    payment_terms: GetVrboListingContentResponse200SectionsPaymentTerms | Unset = UNSET
    protection: GetVrboListingContentResponse200SectionsProtection | Unset = UNSET
    taxes: GetVrboListingContentResponse200SectionsTaxes | Unset = UNSET
    permits: GetVrboListingContentResponse200SectionsPermits | Unset = UNSET
    checkin_guide: GetVrboListingContentResponse200SectionsCheckinGuide | Unset = UNSET
    videos: GetVrboListingContentResponse200SectionsVideos | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_content_response_200_sections_additional_info import GetVrboListingContentResponse200SectionsAdditionalInfo
        from ..models.get_vrbo_listing_content_response_200_sections_amenities import GetVrboListingContentResponse200SectionsAmenities
        from ..models.get_vrbo_listing_content_response_200_sections_booking_settings import GetVrboListingContentResponse200SectionsBookingSettings
        from ..models.get_vrbo_listing_content_response_200_sections_cancellation import GetVrboListingContentResponse200SectionsCancellation
        from ..models.get_vrbo_listing_content_response_200_sections_checkin_guide import GetVrboListingContentResponse200SectionsCheckinGuide
        from ..models.get_vrbo_listing_content_response_200_sections_descriptions_item import GetVrboListingContentResponse200SectionsDescriptionsItem
        from ..models.get_vrbo_listing_content_response_200_sections_details import GetVrboListingContentResponse200SectionsDetails
        from ..models.get_vrbo_listing_content_response_200_sections_fees import GetVrboListingContentResponse200SectionsFees
        from ..models.get_vrbo_listing_content_response_200_sections_house_rules import GetVrboListingContentResponse200SectionsHouseRules
        from ..models.get_vrbo_listing_content_response_200_sections_location import GetVrboListingContentResponse200SectionsLocation
        from ..models.get_vrbo_listing_content_response_200_sections_payment_terms import GetVrboListingContentResponse200SectionsPaymentTerms
        from ..models.get_vrbo_listing_content_response_200_sections_permits import GetVrboListingContentResponse200SectionsPermits
        from ..models.get_vrbo_listing_content_response_200_sections_photos import GetVrboListingContentResponse200SectionsPhotos
        from ..models.get_vrbo_listing_content_response_200_sections_pricing import GetVrboListingContentResponse200SectionsPricing
        from ..models.get_vrbo_listing_content_response_200_sections_protection import GetVrboListingContentResponse200SectionsProtection
        from ..models.get_vrbo_listing_content_response_200_sections_rooms import GetVrboListingContentResponse200SectionsRooms
        from ..models.get_vrbo_listing_content_response_200_sections_story import GetVrboListingContentResponse200SectionsStory
        from ..models.get_vrbo_listing_content_response_200_sections_taxes import GetVrboListingContentResponse200SectionsTaxes
        from ..models.get_vrbo_listing_content_response_200_sections_videos import GetVrboListingContentResponse200SectionsVideos
        descriptions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.descriptions, Unset):
            descriptions = []
            for descriptions_item_data in self.descriptions:
                descriptions_item = descriptions_item_data.to_dict()
                descriptions.append(descriptions_item)



        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        story: dict[str, Any] | Unset = UNSET
        if not isinstance(self.story, Unset):
            story = self.story.to_dict()

        additional_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.additional_info, Unset):
            additional_info = self.additional_info.to_dict()

        photos: dict[str, Any] | Unset = UNSET
        if not isinstance(self.photos, Unset):
            photos = self.photos.to_dict()

        amenities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.amenities, Unset):
            amenities = self.amenities.to_dict()

        rooms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rooms, Unset):
            rooms = self.rooms.to_dict()

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        house_rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.house_rules, Unset):
            house_rules = self.house_rules.to_dict()

        booking_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.booking_settings, Unset):
            booking_settings = self.booking_settings.to_dict()

        cancellation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cancellation, Unset):
            cancellation = self.cancellation.to_dict()

        fees: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fees, Unset):
            fees = self.fees.to_dict()

        pricing: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pricing, Unset):
            pricing = self.pricing.to_dict()

        payment_terms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payment_terms, Unset):
            payment_terms = self.payment_terms.to_dict()

        protection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.protection, Unset):
            protection = self.protection.to_dict()

        taxes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = self.taxes.to_dict()

        permits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permits, Unset):
            permits = self.permits.to_dict()

        checkin_guide: dict[str, Any] | Unset = UNSET
        if not isinstance(self.checkin_guide, Unset):
            checkin_guide = self.checkin_guide.to_dict()

        videos: dict[str, Any] | Unset = UNSET
        if not isinstance(self.videos, Unset):
            videos = self.videos.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if descriptions is not UNSET:
            field_dict["descriptions"] = descriptions
        if details is not UNSET:
            field_dict["details"] = details
        if story is not UNSET:
            field_dict["story"] = story
        if additional_info is not UNSET:
            field_dict["additional-info"] = additional_info
        if photos is not UNSET:
            field_dict["photos"] = photos
        if amenities is not UNSET:
            field_dict["amenities"] = amenities
        if rooms is not UNSET:
            field_dict["rooms"] = rooms
        if location is not UNSET:
            field_dict["location"] = location
        if house_rules is not UNSET:
            field_dict["house-rules"] = house_rules
        if booking_settings is not UNSET:
            field_dict["booking-settings"] = booking_settings
        if cancellation is not UNSET:
            field_dict["cancellation"] = cancellation
        if fees is not UNSET:
            field_dict["fees"] = fees
        if pricing is not UNSET:
            field_dict["pricing"] = pricing
        if payment_terms is not UNSET:
            field_dict["payment-terms"] = payment_terms
        if protection is not UNSET:
            field_dict["protection"] = protection
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if permits is not UNSET:
            field_dict["permits"] = permits
        if checkin_guide is not UNSET:
            field_dict["checkin-guide"] = checkin_guide
        if videos is not UNSET:
            field_dict["videos"] = videos

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_content_response_200_sections_additional_info import GetVrboListingContentResponse200SectionsAdditionalInfo
        from ..models.get_vrbo_listing_content_response_200_sections_amenities import GetVrboListingContentResponse200SectionsAmenities
        from ..models.get_vrbo_listing_content_response_200_sections_booking_settings import GetVrboListingContentResponse200SectionsBookingSettings
        from ..models.get_vrbo_listing_content_response_200_sections_cancellation import GetVrboListingContentResponse200SectionsCancellation
        from ..models.get_vrbo_listing_content_response_200_sections_checkin_guide import GetVrboListingContentResponse200SectionsCheckinGuide
        from ..models.get_vrbo_listing_content_response_200_sections_descriptions_item import GetVrboListingContentResponse200SectionsDescriptionsItem
        from ..models.get_vrbo_listing_content_response_200_sections_details import GetVrboListingContentResponse200SectionsDetails
        from ..models.get_vrbo_listing_content_response_200_sections_fees import GetVrboListingContentResponse200SectionsFees
        from ..models.get_vrbo_listing_content_response_200_sections_house_rules import GetVrboListingContentResponse200SectionsHouseRules
        from ..models.get_vrbo_listing_content_response_200_sections_location import GetVrboListingContentResponse200SectionsLocation
        from ..models.get_vrbo_listing_content_response_200_sections_payment_terms import GetVrboListingContentResponse200SectionsPaymentTerms
        from ..models.get_vrbo_listing_content_response_200_sections_permits import GetVrboListingContentResponse200SectionsPermits
        from ..models.get_vrbo_listing_content_response_200_sections_photos import GetVrboListingContentResponse200SectionsPhotos
        from ..models.get_vrbo_listing_content_response_200_sections_pricing import GetVrboListingContentResponse200SectionsPricing
        from ..models.get_vrbo_listing_content_response_200_sections_protection import GetVrboListingContentResponse200SectionsProtection
        from ..models.get_vrbo_listing_content_response_200_sections_rooms import GetVrboListingContentResponse200SectionsRooms
        from ..models.get_vrbo_listing_content_response_200_sections_story import GetVrboListingContentResponse200SectionsStory
        from ..models.get_vrbo_listing_content_response_200_sections_taxes import GetVrboListingContentResponse200SectionsTaxes
        from ..models.get_vrbo_listing_content_response_200_sections_videos import GetVrboListingContentResponse200SectionsVideos
        d = dict(src_dict)
        _descriptions = d.pop("descriptions", UNSET)
        descriptions: list[GetVrboListingContentResponse200SectionsDescriptionsItem] | Unset = UNSET
        if _descriptions is not UNSET:
            descriptions = []
            for descriptions_item_data in _descriptions:
                descriptions_item = GetVrboListingContentResponse200SectionsDescriptionsItem.from_dict(descriptions_item_data)



                descriptions.append(descriptions_item)


        _details = d.pop("details", UNSET)
        details: GetVrboListingContentResponse200SectionsDetails | Unset
        if isinstance(_details,  Unset):
            details = UNSET
        else:
            details = GetVrboListingContentResponse200SectionsDetails.from_dict(_details)




        _story = d.pop("story", UNSET)
        story: GetVrboListingContentResponse200SectionsStory | Unset
        if isinstance(_story,  Unset):
            story = UNSET
        else:
            story = GetVrboListingContentResponse200SectionsStory.from_dict(_story)




        _additional_info = d.pop("additional-info", UNSET)
        additional_info: GetVrboListingContentResponse200SectionsAdditionalInfo | Unset
        if isinstance(_additional_info,  Unset):
            additional_info = UNSET
        else:
            additional_info = GetVrboListingContentResponse200SectionsAdditionalInfo.from_dict(_additional_info)




        _photos = d.pop("photos", UNSET)
        photos: GetVrboListingContentResponse200SectionsPhotos | Unset
        if isinstance(_photos,  Unset):
            photos = UNSET
        else:
            photos = GetVrboListingContentResponse200SectionsPhotos.from_dict(_photos)




        _amenities = d.pop("amenities", UNSET)
        amenities: GetVrboListingContentResponse200SectionsAmenities | Unset
        if isinstance(_amenities,  Unset):
            amenities = UNSET
        else:
            amenities = GetVrboListingContentResponse200SectionsAmenities.from_dict(_amenities)




        _rooms = d.pop("rooms", UNSET)
        rooms: GetVrboListingContentResponse200SectionsRooms | Unset
        if isinstance(_rooms,  Unset):
            rooms = UNSET
        else:
            rooms = GetVrboListingContentResponse200SectionsRooms.from_dict(_rooms)




        _location = d.pop("location", UNSET)
        location: GetVrboListingContentResponse200SectionsLocation | Unset
        if isinstance(_location,  Unset):
            location = UNSET
        else:
            location = GetVrboListingContentResponse200SectionsLocation.from_dict(_location)




        _house_rules = d.pop("house-rules", UNSET)
        house_rules: GetVrboListingContentResponse200SectionsHouseRules | Unset
        if isinstance(_house_rules,  Unset):
            house_rules = UNSET
        else:
            house_rules = GetVrboListingContentResponse200SectionsHouseRules.from_dict(_house_rules)




        _booking_settings = d.pop("booking-settings", UNSET)
        booking_settings: GetVrboListingContentResponse200SectionsBookingSettings | Unset
        if isinstance(_booking_settings,  Unset):
            booking_settings = UNSET
        else:
            booking_settings = GetVrboListingContentResponse200SectionsBookingSettings.from_dict(_booking_settings)




        _cancellation = d.pop("cancellation", UNSET)
        cancellation: GetVrboListingContentResponse200SectionsCancellation | Unset
        if isinstance(_cancellation,  Unset):
            cancellation = UNSET
        else:
            cancellation = GetVrboListingContentResponse200SectionsCancellation.from_dict(_cancellation)




        _fees = d.pop("fees", UNSET)
        fees: GetVrboListingContentResponse200SectionsFees | Unset
        if isinstance(_fees,  Unset):
            fees = UNSET
        else:
            fees = GetVrboListingContentResponse200SectionsFees.from_dict(_fees)




        _pricing = d.pop("pricing", UNSET)
        pricing: GetVrboListingContentResponse200SectionsPricing | Unset
        if isinstance(_pricing,  Unset):
            pricing = UNSET
        else:
            pricing = GetVrboListingContentResponse200SectionsPricing.from_dict(_pricing)




        _payment_terms = d.pop("payment-terms", UNSET)
        payment_terms: GetVrboListingContentResponse200SectionsPaymentTerms | Unset
        if isinstance(_payment_terms,  Unset):
            payment_terms = UNSET
        else:
            payment_terms = GetVrboListingContentResponse200SectionsPaymentTerms.from_dict(_payment_terms)




        _protection = d.pop("protection", UNSET)
        protection: GetVrboListingContentResponse200SectionsProtection | Unset
        if isinstance(_protection,  Unset):
            protection = UNSET
        else:
            protection = GetVrboListingContentResponse200SectionsProtection.from_dict(_protection)




        _taxes = d.pop("taxes", UNSET)
        taxes: GetVrboListingContentResponse200SectionsTaxes | Unset
        if isinstance(_taxes,  Unset):
            taxes = UNSET
        else:
            taxes = GetVrboListingContentResponse200SectionsTaxes.from_dict(_taxes)




        _permits = d.pop("permits", UNSET)
        permits: GetVrboListingContentResponse200SectionsPermits | Unset
        if isinstance(_permits,  Unset):
            permits = UNSET
        else:
            permits = GetVrboListingContentResponse200SectionsPermits.from_dict(_permits)




        _checkin_guide = d.pop("checkin-guide", UNSET)
        checkin_guide: GetVrboListingContentResponse200SectionsCheckinGuide | Unset
        if isinstance(_checkin_guide,  Unset):
            checkin_guide = UNSET
        else:
            checkin_guide = GetVrboListingContentResponse200SectionsCheckinGuide.from_dict(_checkin_guide)




        _videos = d.pop("videos", UNSET)
        videos: GetVrboListingContentResponse200SectionsVideos | Unset
        if isinstance(_videos,  Unset):
            videos = UNSET
        else:
            videos = GetVrboListingContentResponse200SectionsVideos.from_dict(_videos)




        get_vrbo_listing_content_response_200_sections = cls(
            descriptions=descriptions,
            details=details,
            story=story,
            additional_info=additional_info,
            photos=photos,
            amenities=amenities,
            rooms=rooms,
            location=location,
            house_rules=house_rules,
            booking_settings=booking_settings,
            cancellation=cancellation,
            fees=fees,
            pricing=pricing,
            payment_terms=payment_terms,
            protection=protection,
            taxes=taxes,
            permits=permits,
            checkin_guide=checkin_guide,
            videos=videos,
        )


        get_vrbo_listing_content_response_200_sections.additional_properties = d
        return get_vrbo_listing_content_response_200_sections

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
