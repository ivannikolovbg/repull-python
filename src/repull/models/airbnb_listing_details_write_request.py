from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_listing_details_write_request_property_type_group import AirbnbListingDetailsWriteRequestPropertyTypeGroup
from ..models.airbnb_listing_details_write_request_room_type_category import AirbnbListingDetailsWriteRequestRoomTypeCategory
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_listing_details_write_request_check_in_option import AirbnbListingDetailsWriteRequestCheckInOption
  from ..models.airbnb_listing_details_write_request_quiet_hours_item import AirbnbListingDetailsWriteRequestQuietHoursItem





T = TypeVar("T", bound="AirbnbListingDetailsWriteRequest")



@_attrs_define
class AirbnbListingDetailsWriteRequest:
    """ Update what kind of property this is, when the quiet hours are, or how the guest gets in. At least one field
    required. These are among the attributes Airbnb locks on established listings — see `blockedFields` on the response.

        Attributes:
            property_type_group (AirbnbListingDetailsWriteRequestPropertyTypeGroup | Unset): The coarse building family.
            property_type_category (str | Unset): The specific type inside the group, e.g. `apartment`, `condominium`,
                `townhouse`, `guesthouse`. Airbnb validates it against the group, so send both when you are changing the kind of
                property.
            room_type_category (AirbnbListingDetailsWriteRequestRoomTypeCategory | Unset): What the guest gets of the
                property.
            quiet_hours (list[AirbnbListingDetailsWriteRequestQuietHoursItem] | Unset): Whole hours on a 24h clock, as
                strings.
            check_in_option (AirbnbListingDetailsWriteRequestCheckInOption | Unset): How the guest lets themselves in —
                Airbnb's `check_in_option`.
     """

    property_type_group: AirbnbListingDetailsWriteRequestPropertyTypeGroup | Unset = UNSET
    property_type_category: str | Unset = UNSET
    room_type_category: AirbnbListingDetailsWriteRequestRoomTypeCategory | Unset = UNSET
    quiet_hours: list[AirbnbListingDetailsWriteRequestQuietHoursItem] | Unset = UNSET
    check_in_option: AirbnbListingDetailsWriteRequestCheckInOption | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_listing_details_write_request_check_in_option import AirbnbListingDetailsWriteRequestCheckInOption
        from ..models.airbnb_listing_details_write_request_quiet_hours_item import AirbnbListingDetailsWriteRequestQuietHoursItem
        property_type_group: str | Unset = UNSET
        if not isinstance(self.property_type_group, Unset):
            property_type_group = self.property_type_group.value


        property_type_category = self.property_type_category

        room_type_category: str | Unset = UNSET
        if not isinstance(self.room_type_category, Unset):
            room_type_category = self.room_type_category.value


        quiet_hours: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.quiet_hours, Unset):
            quiet_hours = []
            for quiet_hours_item_data in self.quiet_hours:
                quiet_hours_item = quiet_hours_item_data.to_dict()
                quiet_hours.append(quiet_hours_item)



        check_in_option: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_in_option, Unset):
            check_in_option = self.check_in_option.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if property_type_group is not UNSET:
            field_dict["property_type_group"] = property_type_group
        if property_type_category is not UNSET:
            field_dict["property_type_category"] = property_type_category
        if room_type_category is not UNSET:
            field_dict["room_type_category"] = room_type_category
        if quiet_hours is not UNSET:
            field_dict["quiet_hours"] = quiet_hours
        if check_in_option is not UNSET:
            field_dict["check_in_option"] = check_in_option

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_listing_details_write_request_check_in_option import AirbnbListingDetailsWriteRequestCheckInOption
        from ..models.airbnb_listing_details_write_request_quiet_hours_item import AirbnbListingDetailsWriteRequestQuietHoursItem
        d = dict(src_dict)
        _property_type_group = d.pop("property_type_group", UNSET)
        property_type_group: AirbnbListingDetailsWriteRequestPropertyTypeGroup | Unset
        if isinstance(_property_type_group,  Unset):
            property_type_group = UNSET
        else:
            property_type_group = AirbnbListingDetailsWriteRequestPropertyTypeGroup(_property_type_group)




        property_type_category = d.pop("property_type_category", UNSET)

        _room_type_category = d.pop("room_type_category", UNSET)
        room_type_category: AirbnbListingDetailsWriteRequestRoomTypeCategory | Unset
        if isinstance(_room_type_category,  Unset):
            room_type_category = UNSET
        else:
            room_type_category = AirbnbListingDetailsWriteRequestRoomTypeCategory(_room_type_category)




        _quiet_hours = d.pop("quiet_hours", UNSET)
        quiet_hours: list[AirbnbListingDetailsWriteRequestQuietHoursItem] | Unset = UNSET
        if _quiet_hours is not UNSET:
            quiet_hours = []
            for quiet_hours_item_data in _quiet_hours:
                quiet_hours_item = AirbnbListingDetailsWriteRequestQuietHoursItem.from_dict(quiet_hours_item_data)



                quiet_hours.append(quiet_hours_item)


        _check_in_option = d.pop("check_in_option", UNSET)
        check_in_option: AirbnbListingDetailsWriteRequestCheckInOption | Unset
        if isinstance(_check_in_option,  Unset):
            check_in_option = UNSET
        else:
            check_in_option = AirbnbListingDetailsWriteRequestCheckInOption.from_dict(_check_in_option)




        airbnb_listing_details_write_request = cls(
            property_type_group=property_type_group,
            property_type_category=property_type_category,
            room_type_category=room_type_category,
            quiet_hours=quiet_hours,
            check_in_option=check_in_option,
        )

        return airbnb_listing_details_write_request

