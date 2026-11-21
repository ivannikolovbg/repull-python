from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_vrbo_listing_response_200_data_item_access_type_type_1 import GetVrboListingResponse200DataItemAccessTypeType1
from ..models.get_vrbo_listing_response_200_data_item_access_type_type_2_type_1 import GetVrboListingResponse200DataItemAccessTypeType2Type1
from ..models.get_vrbo_listing_response_200_data_item_access_type_type_3_type_1 import GetVrboListingResponse200DataItemAccessTypeType3Type1
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_listing_response_200_data_item_address import GetVrboListingResponse200DataItemAddress
  from ..models.get_vrbo_listing_response_200_data_item_capacity import GetVrboListingResponse200DataItemCapacity
  from ..models.get_vrbo_listing_response_200_data_item_content import GetVrboListingResponse200DataItemContent
  from ..models.get_vrbo_listing_response_200_data_item_rating import GetVrboListingResponse200DataItemRating





T = TypeVar("T", bound="GetVrboListingResponse200DataItem")



@_attrs_define
class GetVrboListingResponse200DataItem:
    """ 
        Attributes:
            id (str | Unset): Repull's id for this link.
            listing_id (str | Unset):
            vrbo_listing_number (str | Unset): The number in the Vrbo URL (vrbo.com/5506023). Example: 5506023.
            unit_id (None | str | Unset):
            property_id (None | str | Unset): Vrbo's property id.
            advertiser_id (None | str | Unset):
            url (None | str | Unset):
            status (None | str | Unset): Vrbo's own status: `LIVE`, `InactiveByOwnerRequest` (hidden), … Example: LIVE.
            live (bool | Unset):
            connected (bool | Unset): Linked through a connected Vrbo account — the link content, calendar and messages go
                through.
            active (bool | Unset):
            sync_enabled (bool | Unset):
            account_id (None | str | Unset): The Vrbo account the unit is on, as `GET /v1/connect/vrbo-login` lists it.
                Example: vrbo:7001234.
            account_name (None | str | Unset):
            access_type (GetVrboListingResponse200DataItemAccessTypeType1 |
                GetVrboListingResponse200DataItemAccessTypeType2Type1 | GetVrboListingResponse200DataItemAccessTypeType3Type1 |
                None | Unset):
            account_status (None | str | Unset):
            headline (None | str | Unset):
            name (None | str | Unset):
            thumbnail_url (None | str | Unset):
            currency (None | str | Unset):
            markup_percent (float | None | Unset): The markup Repull adds to this unit's prices.
            booking_policy (None | str | Unset):
            capacity (GetVrboListingResponse200DataItemCapacity | Unset):
            bedrooms (int | None | Unset):
            bathrooms (float | None | Unset):
            beds (int | None | Unset):
            check_in_time (None | str | Unset):
            check_out_time (None | str | Unset):
            min_stay (int | None | Unset):
            max_stay (int | None | Unset):
            min_advance_notice_days (int | None | Unset):
            address (GetVrboListingResponse200DataItemAddress | Unset):
            rating (GetVrboListingResponse200DataItemRating | Unset):
            host_name (None | str | Unset):
            linked_at (None | str | Unset):
            disconnected_at (None | str | Unset):
            details_synced_at (None | str | Unset):
            content (GetVrboListingResponse200DataItemContent | Unset):
     """

    id: str | Unset = UNSET
    listing_id: str | Unset = UNSET
    vrbo_listing_number: str | Unset = UNSET
    unit_id: None | str | Unset = UNSET
    property_id: None | str | Unset = UNSET
    advertiser_id: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    live: bool | Unset = UNSET
    connected: bool | Unset = UNSET
    active: bool | Unset = UNSET
    sync_enabled: bool | Unset = UNSET
    account_id: None | str | Unset = UNSET
    account_name: None | str | Unset = UNSET
    access_type: GetVrboListingResponse200DataItemAccessTypeType1 | GetVrboListingResponse200DataItemAccessTypeType2Type1 | GetVrboListingResponse200DataItemAccessTypeType3Type1 | None | Unset = UNSET
    account_status: None | str | Unset = UNSET
    headline: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    thumbnail_url: None | str | Unset = UNSET
    currency: None | str | Unset = UNSET
    markup_percent: float | None | Unset = UNSET
    booking_policy: None | str | Unset = UNSET
    capacity: GetVrboListingResponse200DataItemCapacity | Unset = UNSET
    bedrooms: int | None | Unset = UNSET
    bathrooms: float | None | Unset = UNSET
    beds: int | None | Unset = UNSET
    check_in_time: None | str | Unset = UNSET
    check_out_time: None | str | Unset = UNSET
    min_stay: int | None | Unset = UNSET
    max_stay: int | None | Unset = UNSET
    min_advance_notice_days: int | None | Unset = UNSET
    address: GetVrboListingResponse200DataItemAddress | Unset = UNSET
    rating: GetVrboListingResponse200DataItemRating | Unset = UNSET
    host_name: None | str | Unset = UNSET
    linked_at: None | str | Unset = UNSET
    disconnected_at: None | str | Unset = UNSET
    details_synced_at: None | str | Unset = UNSET
    content: GetVrboListingResponse200DataItemContent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_listing_response_200_data_item_address import GetVrboListingResponse200DataItemAddress
        from ..models.get_vrbo_listing_response_200_data_item_capacity import GetVrboListingResponse200DataItemCapacity
        from ..models.get_vrbo_listing_response_200_data_item_content import GetVrboListingResponse200DataItemContent
        from ..models.get_vrbo_listing_response_200_data_item_rating import GetVrboListingResponse200DataItemRating
        id = self.id

        listing_id = self.listing_id

        vrbo_listing_number = self.vrbo_listing_number

        unit_id: None | str | Unset
        if isinstance(self.unit_id, Unset):
            unit_id = UNSET
        else:
            unit_id = self.unit_id

        property_id: None | str | Unset
        if isinstance(self.property_id, Unset):
            property_id = UNSET
        else:
            property_id = self.property_id

        advertiser_id: None | str | Unset
        if isinstance(self.advertiser_id, Unset):
            advertiser_id = UNSET
        else:
            advertiser_id = self.advertiser_id

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        live = self.live

        connected = self.connected

        active = self.active

        sync_enabled = self.sync_enabled

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        account_name: None | str | Unset
        if isinstance(self.account_name, Unset):
            account_name = UNSET
        else:
            account_name = self.account_name

        access_type: None | str | Unset
        if isinstance(self.access_type, Unset):
            access_type = UNSET
        elif isinstance(self.access_type, GetVrboListingResponse200DataItemAccessTypeType1):
            access_type = self.access_type.value
        elif isinstance(self.access_type, GetVrboListingResponse200DataItemAccessTypeType2Type1):
            access_type = self.access_type.value
        elif isinstance(self.access_type, GetVrboListingResponse200DataItemAccessTypeType3Type1):
            access_type = self.access_type.value
        else:
            access_type = self.access_type

        account_status: None | str | Unset
        if isinstance(self.account_status, Unset):
            account_status = UNSET
        else:
            account_status = self.account_status

        headline: None | str | Unset
        if isinstance(self.headline, Unset):
            headline = UNSET
        else:
            headline = self.headline

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        thumbnail_url: None | str | Unset
        if isinstance(self.thumbnail_url, Unset):
            thumbnail_url = UNSET
        else:
            thumbnail_url = self.thumbnail_url

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        markup_percent: float | None | Unset
        if isinstance(self.markup_percent, Unset):
            markup_percent = UNSET
        else:
            markup_percent = self.markup_percent

        booking_policy: None | str | Unset
        if isinstance(self.booking_policy, Unset):
            booking_policy = UNSET
        else:
            booking_policy = self.booking_policy

        capacity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.capacity, Unset):
            capacity = self.capacity.to_dict()

        bedrooms: int | None | Unset
        if isinstance(self.bedrooms, Unset):
            bedrooms = UNSET
        else:
            bedrooms = self.bedrooms

        bathrooms: float | None | Unset
        if isinstance(self.bathrooms, Unset):
            bathrooms = UNSET
        else:
            bathrooms = self.bathrooms

        beds: int | None | Unset
        if isinstance(self.beds, Unset):
            beds = UNSET
        else:
            beds = self.beds

        check_in_time: None | str | Unset
        if isinstance(self.check_in_time, Unset):
            check_in_time = UNSET
        else:
            check_in_time = self.check_in_time

        check_out_time: None | str | Unset
        if isinstance(self.check_out_time, Unset):
            check_out_time = UNSET
        else:
            check_out_time = self.check_out_time

        min_stay: int | None | Unset
        if isinstance(self.min_stay, Unset):
            min_stay = UNSET
        else:
            min_stay = self.min_stay

        max_stay: int | None | Unset
        if isinstance(self.max_stay, Unset):
            max_stay = UNSET
        else:
            max_stay = self.max_stay

        min_advance_notice_days: int | None | Unset
        if isinstance(self.min_advance_notice_days, Unset):
            min_advance_notice_days = UNSET
        else:
            min_advance_notice_days = self.min_advance_notice_days

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        rating: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rating, Unset):
            rating = self.rating.to_dict()

        host_name: None | str | Unset
        if isinstance(self.host_name, Unset):
            host_name = UNSET
        else:
            host_name = self.host_name

        linked_at: None | str | Unset
        if isinstance(self.linked_at, Unset):
            linked_at = UNSET
        else:
            linked_at = self.linked_at

        disconnected_at: None | str | Unset
        if isinstance(self.disconnected_at, Unset):
            disconnected_at = UNSET
        else:
            disconnected_at = self.disconnected_at

        details_synced_at: None | str | Unset
        if isinstance(self.details_synced_at, Unset):
            details_synced_at = UNSET
        else:
            details_synced_at = self.details_synced_at

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if vrbo_listing_number is not UNSET:
            field_dict["vrboListingNumber"] = vrbo_listing_number
        if unit_id is not UNSET:
            field_dict["unitId"] = unit_id
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if advertiser_id is not UNSET:
            field_dict["advertiserId"] = advertiser_id
        if url is not UNSET:
            field_dict["url"] = url
        if status is not UNSET:
            field_dict["status"] = status
        if live is not UNSET:
            field_dict["live"] = live
        if connected is not UNSET:
            field_dict["connected"] = connected
        if active is not UNSET:
            field_dict["active"] = active
        if sync_enabled is not UNSET:
            field_dict["syncEnabled"] = sync_enabled
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if access_type is not UNSET:
            field_dict["accessType"] = access_type
        if account_status is not UNSET:
            field_dict["accountStatus"] = account_status
        if headline is not UNSET:
            field_dict["headline"] = headline
        if name is not UNSET:
            field_dict["name"] = name
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url
        if currency is not UNSET:
            field_dict["currency"] = currency
        if markup_percent is not UNSET:
            field_dict["markupPercent"] = markup_percent
        if booking_policy is not UNSET:
            field_dict["bookingPolicy"] = booking_policy
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if bedrooms is not UNSET:
            field_dict["bedrooms"] = bedrooms
        if bathrooms is not UNSET:
            field_dict["bathrooms"] = bathrooms
        if beds is not UNSET:
            field_dict["beds"] = beds
        if check_in_time is not UNSET:
            field_dict["checkInTime"] = check_in_time
        if check_out_time is not UNSET:
            field_dict["checkOutTime"] = check_out_time
        if min_stay is not UNSET:
            field_dict["minStay"] = min_stay
        if max_stay is not UNSET:
            field_dict["maxStay"] = max_stay
        if min_advance_notice_days is not UNSET:
            field_dict["minAdvanceNoticeDays"] = min_advance_notice_days
        if address is not UNSET:
            field_dict["address"] = address
        if rating is not UNSET:
            field_dict["rating"] = rating
        if host_name is not UNSET:
            field_dict["hostName"] = host_name
        if linked_at is not UNSET:
            field_dict["linkedAt"] = linked_at
        if disconnected_at is not UNSET:
            field_dict["disconnectedAt"] = disconnected_at
        if details_synced_at is not UNSET:
            field_dict["detailsSyncedAt"] = details_synced_at
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_listing_response_200_data_item_address import GetVrboListingResponse200DataItemAddress
        from ..models.get_vrbo_listing_response_200_data_item_capacity import GetVrboListingResponse200DataItemCapacity
        from ..models.get_vrbo_listing_response_200_data_item_content import GetVrboListingResponse200DataItemContent
        from ..models.get_vrbo_listing_response_200_data_item_rating import GetVrboListingResponse200DataItemRating
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        listing_id = d.pop("listingId", UNSET)

        vrbo_listing_number = d.pop("vrboListingNumber", UNSET)

        def _parse_unit_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        unit_id = _parse_unit_id(d.pop("unitId", UNSET))


        def _parse_property_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_id = _parse_property_id(d.pop("propertyId", UNSET))


        def _parse_advertiser_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        advertiser_id = _parse_advertiser_id(d.pop("advertiserId", UNSET))


        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        live = d.pop("live", UNSET)

        connected = d.pop("connected", UNSET)

        active = d.pop("active", UNSET)

        sync_enabled = d.pop("syncEnabled", UNSET)

        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("accountId", UNSET))


        def _parse_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_name = _parse_account_name(d.pop("accountName", UNSET))


        def _parse_access_type(data: object) -> GetVrboListingResponse200DataItemAccessTypeType1 | GetVrboListingResponse200DataItemAccessTypeType2Type1 | GetVrboListingResponse200DataItemAccessTypeType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_type_type_1 = GetVrboListingResponse200DataItemAccessTypeType1(data)



                return access_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_type_type_2_type_1 = GetVrboListingResponse200DataItemAccessTypeType2Type1(data)



                return access_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_type_type_3_type_1 = GetVrboListingResponse200DataItemAccessTypeType3Type1(data)



                return access_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboListingResponse200DataItemAccessTypeType1 | GetVrboListingResponse200DataItemAccessTypeType2Type1 | GetVrboListingResponse200DataItemAccessTypeType3Type1 | None | Unset, data)

        access_type = _parse_access_type(d.pop("accessType", UNSET))


        def _parse_account_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_status = _parse_account_status(d.pop("accountStatus", UNSET))


        def _parse_headline(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        headline = _parse_headline(d.pop("headline", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_thumbnail_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        thumbnail_url = _parse_thumbnail_url(d.pop("thumbnailUrl", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_markup_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        markup_percent = _parse_markup_percent(d.pop("markupPercent", UNSET))


        def _parse_booking_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        booking_policy = _parse_booking_policy(d.pop("bookingPolicy", UNSET))


        _capacity = d.pop("capacity", UNSET)
        capacity: GetVrboListingResponse200DataItemCapacity | Unset
        if isinstance(_capacity,  Unset):
            capacity = UNSET
        else:
            capacity = GetVrboListingResponse200DataItemCapacity.from_dict(_capacity)




        def _parse_bedrooms(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bedrooms = _parse_bedrooms(d.pop("bedrooms", UNSET))


        def _parse_bathrooms(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        bathrooms = _parse_bathrooms(d.pop("bathrooms", UNSET))


        def _parse_beds(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        beds = _parse_beds(d.pop("beds", UNSET))


        def _parse_check_in_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_in_time = _parse_check_in_time(d.pop("checkInTime", UNSET))


        def _parse_check_out_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        check_out_time = _parse_check_out_time(d.pop("checkOutTime", UNSET))


        def _parse_min_stay(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_stay = _parse_min_stay(d.pop("minStay", UNSET))


        def _parse_max_stay(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_stay = _parse_max_stay(d.pop("maxStay", UNSET))


        def _parse_min_advance_notice_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_advance_notice_days = _parse_min_advance_notice_days(d.pop("minAdvanceNoticeDays", UNSET))


        _address = d.pop("address", UNSET)
        address: GetVrboListingResponse200DataItemAddress | Unset
        if isinstance(_address,  Unset):
            address = UNSET
        else:
            address = GetVrboListingResponse200DataItemAddress.from_dict(_address)




        _rating = d.pop("rating", UNSET)
        rating: GetVrboListingResponse200DataItemRating | Unset
        if isinstance(_rating,  Unset):
            rating = UNSET
        else:
            rating = GetVrboListingResponse200DataItemRating.from_dict(_rating)




        def _parse_host_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        host_name = _parse_host_name(d.pop("hostName", UNSET))


        def _parse_linked_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        linked_at = _parse_linked_at(d.pop("linkedAt", UNSET))


        def _parse_disconnected_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disconnected_at = _parse_disconnected_at(d.pop("disconnectedAt", UNSET))


        def _parse_details_synced_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        details_synced_at = _parse_details_synced_at(d.pop("detailsSyncedAt", UNSET))


        _content = d.pop("content", UNSET)
        content: GetVrboListingResponse200DataItemContent | Unset
        if isinstance(_content,  Unset):
            content = UNSET
        else:
            content = GetVrboListingResponse200DataItemContent.from_dict(_content)




        get_vrbo_listing_response_200_data_item = cls(
            id=id,
            listing_id=listing_id,
            vrbo_listing_number=vrbo_listing_number,
            unit_id=unit_id,
            property_id=property_id,
            advertiser_id=advertiser_id,
            url=url,
            status=status,
            live=live,
            connected=connected,
            active=active,
            sync_enabled=sync_enabled,
            account_id=account_id,
            account_name=account_name,
            access_type=access_type,
            account_status=account_status,
            headline=headline,
            name=name,
            thumbnail_url=thumbnail_url,
            currency=currency,
            markup_percent=markup_percent,
            booking_policy=booking_policy,
            capacity=capacity,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            beds=beds,
            check_in_time=check_in_time,
            check_out_time=check_out_time,
            min_stay=min_stay,
            max_stay=max_stay,
            min_advance_notice_days=min_advance_notice_days,
            address=address,
            rating=rating,
            host_name=host_name,
            linked_at=linked_at,
            disconnected_at=disconnected_at,
            details_synced_at=details_synced_at,
            content=content,
        )


        get_vrbo_listing_response_200_data_item.additional_properties = d
        return get_vrbo_listing_response_200_data_item

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
