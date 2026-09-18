from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_content_update_request_details_room_type_category import ListingContentUpdateRequestDetailsRoomTypeCategory
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListingContentUpdateRequestDetails")



@_attrs_define
class ListingContentUpdateRequestDetails:
    """ What KIND of property this is. The publish path reads all three on every push, so setting them here is the update
    path for a listing that already exists — `POST /v1/listings` could only set the type at creation. Airbnb may lock
    these on an established listing; the publish response reports that in `lockedFields`.

        Attributes:
            property_type (None | str | Unset): Free-form property type; mapped to Airbnb's property-type group at publish
                time. Example: apartment.
            property_type_category (None | str | Unset): Airbnb's `property_type_category`, e.g. `apartment`, `condominium`,
                `townhouse`.
            room_type_category (ListingContentUpdateRequestDetailsRoomTypeCategory | Unset): What the guest gets of the
                property.
     """

    property_type: None | str | Unset = UNSET
    property_type_category: None | str | Unset = UNSET
    room_type_category: ListingContentUpdateRequestDetailsRoomTypeCategory | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        property_type: None | str | Unset
        if isinstance(self.property_type, Unset):
            property_type = UNSET
        else:
            property_type = self.property_type

        property_type_category: None | str | Unset
        if isinstance(self.property_type_category, Unset):
            property_type_category = UNSET
        else:
            property_type_category = self.property_type_category

        room_type_category: str | Unset = UNSET
        if not isinstance(self.room_type_category, Unset):
            room_type_category = self.room_type_category.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if property_type is not UNSET:
            field_dict["propertyType"] = property_type
        if property_type_category is not UNSET:
            field_dict["propertyTypeCategory"] = property_type_category
        if room_type_category is not UNSET:
            field_dict["roomTypeCategory"] = room_type_category

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_property_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_type = _parse_property_type(d.pop("propertyType", UNSET))


        def _parse_property_type_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_type_category = _parse_property_type_category(d.pop("propertyTypeCategory", UNSET))


        _room_type_category = d.pop("roomTypeCategory", UNSET)
        room_type_category: ListingContentUpdateRequestDetailsRoomTypeCategory | Unset
        if isinstance(_room_type_category,  Unset):
            room_type_category = UNSET
        else:
            room_type_category = ListingContentUpdateRequestDetailsRoomTypeCategory(_room_type_category)




        listing_content_update_request_details = cls(
            property_type=property_type,
            property_type_category=property_type_category,
            room_type_category=room_type_category,
        )


        listing_content_update_request_details.additional_properties = d
        return listing_content_update_request_details

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
