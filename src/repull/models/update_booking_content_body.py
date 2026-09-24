from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_booking_content_body_type import UpdateBookingContentBodyType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_booking_content_body_contacts_item import UpdateBookingContentBodyContactsItem
  from ..models.update_booking_content_body_content_data_item import UpdateBookingContentBodyContentDataItem
  from ..models.update_booking_content_body_facilities_item import UpdateBookingContentBodyFacilitiesItem
  from ..models.update_booking_content_body_methods_item import UpdateBookingContentBodyMethodsItem
  from ..models.update_booking_content_body_photos_item import UpdateBookingContentBodyPhotosItem
  from ..models.update_booking_content_body_settings import UpdateBookingContentBodySettings





T = TypeVar("T", bound="UpdateBookingContentBody")



@_attrs_define
class UpdateBookingContentBody:
    """ 
        Attributes:
            type_ (UpdateBookingContentBodyType):
            property_id (str): Booking.com property id.
            room_id (str | Unset): A Booking.com room id, for `facilities`, `photos` (gallery) and `licences`.
            text (str | Unset): `description`: the property description, up to 65,535 characters.
            language (str | Unset): `description`: language code, e.g. `en` or `es`.
            facilities (list[UpdateBookingContentBodyFacilitiesItem] | Unset):
            photos (list[UpdateBookingContentBodyPhotosItem] | Unset):
            photo_ids (list[str] | Unset):
            settings (UpdateBookingContentBodySettings | Unset):
            policy_code (int | Unset):
            policy_id (str | Unset):
            prepayment_required (bool | Unset):
            variant_id (int | Unset):
            content_data (list[UpdateBookingContentBodyContentDataItem] | Unset):
            methods (list[UpdateBookingContentBodyMethodsItem] | Unset): `checkin_methods`: [{ checkin_method }].
            contacts (list[UpdateBookingContentBodyContactsItem] | Unset):
     """

    type_: UpdateBookingContentBodyType
    property_id: str
    room_id: str | Unset = UNSET
    text: str | Unset = UNSET
    language: str | Unset = UNSET
    facilities: list[UpdateBookingContentBodyFacilitiesItem] | Unset = UNSET
    photos: list[UpdateBookingContentBodyPhotosItem] | Unset = UNSET
    photo_ids: list[str] | Unset = UNSET
    settings: UpdateBookingContentBodySettings | Unset = UNSET
    policy_code: int | Unset = UNSET
    policy_id: str | Unset = UNSET
    prepayment_required: bool | Unset = UNSET
    variant_id: int | Unset = UNSET
    content_data: list[UpdateBookingContentBodyContentDataItem] | Unset = UNSET
    methods: list[UpdateBookingContentBodyMethodsItem] | Unset = UNSET
    contacts: list[UpdateBookingContentBodyContactsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_booking_content_body_contacts_item import UpdateBookingContentBodyContactsItem
        from ..models.update_booking_content_body_content_data_item import UpdateBookingContentBodyContentDataItem
        from ..models.update_booking_content_body_facilities_item import UpdateBookingContentBodyFacilitiesItem
        from ..models.update_booking_content_body_methods_item import UpdateBookingContentBodyMethodsItem
        from ..models.update_booking_content_body_photos_item import UpdateBookingContentBodyPhotosItem
        from ..models.update_booking_content_body_settings import UpdateBookingContentBodySettings
        type_ = self.type_.value

        property_id = self.property_id

        room_id = self.room_id

        text = self.text

        language = self.language

        facilities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.facilities, Unset):
            facilities = []
            for facilities_item_data in self.facilities:
                facilities_item = facilities_item_data.to_dict()
                facilities.append(facilities_item)



        photos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.photos, Unset):
            photos = []
            for photos_item_data in self.photos:
                photos_item = photos_item_data.to_dict()
                photos.append(photos_item)



        photo_ids: list[str] | Unset = UNSET
        if not isinstance(self.photo_ids, Unset):
            photo_ids = self.photo_ids



        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        policy_code = self.policy_code

        policy_id = self.policy_id

        prepayment_required = self.prepayment_required

        variant_id = self.variant_id

        content_data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content_data, Unset):
            content_data = []
            for content_data_item_data in self.content_data:
                content_data_item = content_data_item_data.to_dict()
                content_data.append(content_data_item)



        methods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.methods, Unset):
            methods = []
            for methods_item_data in self.methods:
                methods_item = methods_item_data.to_dict()
                methods.append(methods_item)



        contacts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contacts, Unset):
            contacts = []
            for contacts_item_data in self.contacts:
                contacts_item = contacts_item_data.to_dict()
                contacts.append(contacts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "property_id": property_id,
        })
        if room_id is not UNSET:
            field_dict["room_id"] = room_id
        if text is not UNSET:
            field_dict["text"] = text
        if language is not UNSET:
            field_dict["language"] = language
        if facilities is not UNSET:
            field_dict["facilities"] = facilities
        if photos is not UNSET:
            field_dict["photos"] = photos
        if photo_ids is not UNSET:
            field_dict["photo_ids"] = photo_ids
        if settings is not UNSET:
            field_dict["settings"] = settings
        if policy_code is not UNSET:
            field_dict["policyCode"] = policy_code
        if policy_id is not UNSET:
            field_dict["policyId"] = policy_id
        if prepayment_required is not UNSET:
            field_dict["prepaymentRequired"] = prepayment_required
        if variant_id is not UNSET:
            field_dict["variantId"] = variant_id
        if content_data is not UNSET:
            field_dict["contentData"] = content_data
        if methods is not UNSET:
            field_dict["methods"] = methods
        if contacts is not UNSET:
            field_dict["contacts"] = contacts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_booking_content_body_contacts_item import UpdateBookingContentBodyContactsItem
        from ..models.update_booking_content_body_content_data_item import UpdateBookingContentBodyContentDataItem
        from ..models.update_booking_content_body_facilities_item import UpdateBookingContentBodyFacilitiesItem
        from ..models.update_booking_content_body_methods_item import UpdateBookingContentBodyMethodsItem
        from ..models.update_booking_content_body_photos_item import UpdateBookingContentBodyPhotosItem
        from ..models.update_booking_content_body_settings import UpdateBookingContentBodySettings
        d = dict(src_dict)
        type_ = UpdateBookingContentBodyType(d.pop("type"))




        property_id = d.pop("property_id")

        room_id = d.pop("room_id", UNSET)

        text = d.pop("text", UNSET)

        language = d.pop("language", UNSET)

        _facilities = d.pop("facilities", UNSET)
        facilities: list[UpdateBookingContentBodyFacilitiesItem] | Unset = UNSET
        if _facilities is not UNSET:
            facilities = []
            for facilities_item_data in _facilities:
                facilities_item = UpdateBookingContentBodyFacilitiesItem.from_dict(facilities_item_data)



                facilities.append(facilities_item)


        _photos = d.pop("photos", UNSET)
        photos: list[UpdateBookingContentBodyPhotosItem] | Unset = UNSET
        if _photos is not UNSET:
            photos = []
            for photos_item_data in _photos:
                photos_item = UpdateBookingContentBodyPhotosItem.from_dict(photos_item_data)



                photos.append(photos_item)


        photo_ids = cast(list[str], d.pop("photo_ids", UNSET))


        _settings = d.pop("settings", UNSET)
        settings: UpdateBookingContentBodySettings | Unset
        if isinstance(_settings,  Unset):
            settings = UNSET
        else:
            settings = UpdateBookingContentBodySettings.from_dict(_settings)




        policy_code = d.pop("policyCode", UNSET)

        policy_id = d.pop("policyId", UNSET)

        prepayment_required = d.pop("prepaymentRequired", UNSET)

        variant_id = d.pop("variantId", UNSET)

        _content_data = d.pop("contentData", UNSET)
        content_data: list[UpdateBookingContentBodyContentDataItem] | Unset = UNSET
        if _content_data is not UNSET:
            content_data = []
            for content_data_item_data in _content_data:
                content_data_item = UpdateBookingContentBodyContentDataItem.from_dict(content_data_item_data)



                content_data.append(content_data_item)


        _methods = d.pop("methods", UNSET)
        methods: list[UpdateBookingContentBodyMethodsItem] | Unset = UNSET
        if _methods is not UNSET:
            methods = []
            for methods_item_data in _methods:
                methods_item = UpdateBookingContentBodyMethodsItem.from_dict(methods_item_data)



                methods.append(methods_item)


        _contacts = d.pop("contacts", UNSET)
        contacts: list[UpdateBookingContentBodyContactsItem] | Unset = UNSET
        if _contacts is not UNSET:
            contacts = []
            for contacts_item_data in _contacts:
                contacts_item = UpdateBookingContentBodyContactsItem.from_dict(contacts_item_data)



                contacts.append(contacts_item)


        update_booking_content_body = cls(
            type_=type_,
            property_id=property_id,
            room_id=room_id,
            text=text,
            language=language,
            facilities=facilities,
            photos=photos,
            photo_ids=photo_ids,
            settings=settings,
            policy_code=policy_code,
            policy_id=policy_id,
            prepayment_required=prepayment_required,
            variant_id=variant_id,
            content_data=content_data,
            methods=methods,
            contacts=contacts,
        )


        update_booking_content_body.additional_properties = d
        return update_booking_content_body

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
