from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_amenities_body_groups_accessibility import UpdateVrboListingAmenitiesBodyGroupsAccessibility
  from ..models.update_vrbo_listing_amenities_body_groups_checkout_instructions import UpdateVrboListingAmenitiesBodyGroupsCheckoutInstructions
  from ..models.update_vrbo_listing_amenities_body_groups_climate_control import UpdateVrboListingAmenitiesBodyGroupsClimateControl
  from ..models.update_vrbo_listing_amenities_body_groups_enhanced_cleaning import UpdateVrboListingAmenitiesBodyGroupsEnhancedCleaning
  from ..models.update_vrbo_listing_amenities_body_groups_entertainment import UpdateVrboListingAmenitiesBodyGroupsEntertainment
  from ..models.update_vrbo_listing_amenities_body_groups_essentials import UpdateVrboListingAmenitiesBodyGroupsEssentials
  from ..models.update_vrbo_listing_amenities_body_groups_general import UpdateVrboListingAmenitiesBodyGroupsGeneral
  from ..models.update_vrbo_listing_amenities_body_groups_home_safety import UpdateVrboListingAmenitiesBodyGroupsHomeSafety
  from ..models.update_vrbo_listing_amenities_body_groups_internet import UpdateVrboListingAmenitiesBodyGroupsInternet
  from ..models.update_vrbo_listing_amenities_body_groups_kitchen_and_dining import UpdateVrboListingAmenitiesBodyGroupsKitchenAndDining
  from ..models.update_vrbo_listing_amenities_body_groups_local_attractions_and_activities import UpdateVrboListingAmenitiesBodyGroupsLocalAttractionsAndActivities
  from ..models.update_vrbo_listing_amenities_body_groups_location_and_view import UpdateVrboListingAmenitiesBodyGroupsLocationAndView
  from ..models.update_vrbo_listing_amenities_body_groups_office import UpdateVrboListingAmenitiesBodyGroupsOffice
  from ..models.update_vrbo_listing_amenities_body_groups_onsite_service import UpdateVrboListingAmenitiesBodyGroupsOnsiteService
  from ..models.update_vrbo_listing_amenities_body_groups_outdoor import UpdateVrboListingAmenitiesBodyGroupsOutdoor
  from ..models.update_vrbo_listing_amenities_body_groups_parking import UpdateVrboListingAmenitiesBodyGroupsParking
  from ..models.update_vrbo_listing_amenities_body_groups_pool_and_spa import UpdateVrboListingAmenitiesBodyGroupsPoolAndSpa
  from ..models.update_vrbo_listing_amenities_body_groups_safety_devices import UpdateVrboListingAmenitiesBodyGroupsSafetyDevices
  from ..models.update_vrbo_listing_amenities_body_groups_sustainability import UpdateVrboListingAmenitiesBodyGroupsSustainability





T = TypeVar("T", bound="UpdateVrboListingAmenitiesBodyGroups")



@_attrs_define
class UpdateVrboListingAmenitiesBodyGroups:
    """ Keyed by group: essentials, internet, climateControl, general, office, kitchenAndDining, parking, poolAndSpa,
    sustainability, entertainment, outdoor, onsiteService, accessibility, homeSafety, safetyDevices, enhancedCleaning,
    locationAndView, localAttractionsAndActivities, checkoutInstructions.

        Attributes:
            essentials (UpdateVrboListingAmenitiesBodyGroupsEssentials | Unset):
            internet (UpdateVrboListingAmenitiesBodyGroupsInternet | Unset):
            climate_control (UpdateVrboListingAmenitiesBodyGroupsClimateControl | Unset):
            general (UpdateVrboListingAmenitiesBodyGroupsGeneral | Unset):
            office (UpdateVrboListingAmenitiesBodyGroupsOffice | Unset):
            kitchen_and_dining (UpdateVrboListingAmenitiesBodyGroupsKitchenAndDining | Unset):
            parking (UpdateVrboListingAmenitiesBodyGroupsParking | Unset):
            pool_and_spa (UpdateVrboListingAmenitiesBodyGroupsPoolAndSpa | Unset):
            sustainability (UpdateVrboListingAmenitiesBodyGroupsSustainability | Unset):
            entertainment (UpdateVrboListingAmenitiesBodyGroupsEntertainment | Unset):
            outdoor (UpdateVrboListingAmenitiesBodyGroupsOutdoor | Unset):
            onsite_service (UpdateVrboListingAmenitiesBodyGroupsOnsiteService | Unset):
            accessibility (UpdateVrboListingAmenitiesBodyGroupsAccessibility | Unset):
            home_safety (UpdateVrboListingAmenitiesBodyGroupsHomeSafety | Unset):
            safety_devices (UpdateVrboListingAmenitiesBodyGroupsSafetyDevices | Unset):
            enhanced_cleaning (UpdateVrboListingAmenitiesBodyGroupsEnhancedCleaning | Unset):
            location_and_view (UpdateVrboListingAmenitiesBodyGroupsLocationAndView | Unset):
            local_attractions_and_activities (UpdateVrboListingAmenitiesBodyGroupsLocalAttractionsAndActivities | Unset):
            checkout_instructions (UpdateVrboListingAmenitiesBodyGroupsCheckoutInstructions | Unset):
     """

    essentials: UpdateVrboListingAmenitiesBodyGroupsEssentials | Unset = UNSET
    internet: UpdateVrboListingAmenitiesBodyGroupsInternet | Unset = UNSET
    climate_control: UpdateVrboListingAmenitiesBodyGroupsClimateControl | Unset = UNSET
    general: UpdateVrboListingAmenitiesBodyGroupsGeneral | Unset = UNSET
    office: UpdateVrboListingAmenitiesBodyGroupsOffice | Unset = UNSET
    kitchen_and_dining: UpdateVrboListingAmenitiesBodyGroupsKitchenAndDining | Unset = UNSET
    parking: UpdateVrboListingAmenitiesBodyGroupsParking | Unset = UNSET
    pool_and_spa: UpdateVrboListingAmenitiesBodyGroupsPoolAndSpa | Unset = UNSET
    sustainability: UpdateVrboListingAmenitiesBodyGroupsSustainability | Unset = UNSET
    entertainment: UpdateVrboListingAmenitiesBodyGroupsEntertainment | Unset = UNSET
    outdoor: UpdateVrboListingAmenitiesBodyGroupsOutdoor | Unset = UNSET
    onsite_service: UpdateVrboListingAmenitiesBodyGroupsOnsiteService | Unset = UNSET
    accessibility: UpdateVrboListingAmenitiesBodyGroupsAccessibility | Unset = UNSET
    home_safety: UpdateVrboListingAmenitiesBodyGroupsHomeSafety | Unset = UNSET
    safety_devices: UpdateVrboListingAmenitiesBodyGroupsSafetyDevices | Unset = UNSET
    enhanced_cleaning: UpdateVrboListingAmenitiesBodyGroupsEnhancedCleaning | Unset = UNSET
    location_and_view: UpdateVrboListingAmenitiesBodyGroupsLocationAndView | Unset = UNSET
    local_attractions_and_activities: UpdateVrboListingAmenitiesBodyGroupsLocalAttractionsAndActivities | Unset = UNSET
    checkout_instructions: UpdateVrboListingAmenitiesBodyGroupsCheckoutInstructions | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_amenities_body_groups_accessibility import UpdateVrboListingAmenitiesBodyGroupsAccessibility
        from ..models.update_vrbo_listing_amenities_body_groups_checkout_instructions import UpdateVrboListingAmenitiesBodyGroupsCheckoutInstructions
        from ..models.update_vrbo_listing_amenities_body_groups_climate_control import UpdateVrboListingAmenitiesBodyGroupsClimateControl
        from ..models.update_vrbo_listing_amenities_body_groups_enhanced_cleaning import UpdateVrboListingAmenitiesBodyGroupsEnhancedCleaning
        from ..models.update_vrbo_listing_amenities_body_groups_entertainment import UpdateVrboListingAmenitiesBodyGroupsEntertainment
        from ..models.update_vrbo_listing_amenities_body_groups_essentials import UpdateVrboListingAmenitiesBodyGroupsEssentials
        from ..models.update_vrbo_listing_amenities_body_groups_general import UpdateVrboListingAmenitiesBodyGroupsGeneral
        from ..models.update_vrbo_listing_amenities_body_groups_home_safety import UpdateVrboListingAmenitiesBodyGroupsHomeSafety
        from ..models.update_vrbo_listing_amenities_body_groups_internet import UpdateVrboListingAmenitiesBodyGroupsInternet
        from ..models.update_vrbo_listing_amenities_body_groups_kitchen_and_dining import UpdateVrboListingAmenitiesBodyGroupsKitchenAndDining
        from ..models.update_vrbo_listing_amenities_body_groups_local_attractions_and_activities import UpdateVrboListingAmenitiesBodyGroupsLocalAttractionsAndActivities
        from ..models.update_vrbo_listing_amenities_body_groups_location_and_view import UpdateVrboListingAmenitiesBodyGroupsLocationAndView
        from ..models.update_vrbo_listing_amenities_body_groups_office import UpdateVrboListingAmenitiesBodyGroupsOffice
        from ..models.update_vrbo_listing_amenities_body_groups_onsite_service import UpdateVrboListingAmenitiesBodyGroupsOnsiteService
        from ..models.update_vrbo_listing_amenities_body_groups_outdoor import UpdateVrboListingAmenitiesBodyGroupsOutdoor
        from ..models.update_vrbo_listing_amenities_body_groups_parking import UpdateVrboListingAmenitiesBodyGroupsParking
        from ..models.update_vrbo_listing_amenities_body_groups_pool_and_spa import UpdateVrboListingAmenitiesBodyGroupsPoolAndSpa
        from ..models.update_vrbo_listing_amenities_body_groups_safety_devices import UpdateVrboListingAmenitiesBodyGroupsSafetyDevices
        from ..models.update_vrbo_listing_amenities_body_groups_sustainability import UpdateVrboListingAmenitiesBodyGroupsSustainability
        essentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.essentials, Unset):
            essentials = self.essentials.to_dict()

        internet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.internet, Unset):
            internet = self.internet.to_dict()

        climate_control: dict[str, Any] | Unset = UNSET
        if not isinstance(self.climate_control, Unset):
            climate_control = self.climate_control.to_dict()

        general: dict[str, Any] | Unset = UNSET
        if not isinstance(self.general, Unset):
            general = self.general.to_dict()

        office: dict[str, Any] | Unset = UNSET
        if not isinstance(self.office, Unset):
            office = self.office.to_dict()

        kitchen_and_dining: dict[str, Any] | Unset = UNSET
        if not isinstance(self.kitchen_and_dining, Unset):
            kitchen_and_dining = self.kitchen_and_dining.to_dict()

        parking: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parking, Unset):
            parking = self.parking.to_dict()

        pool_and_spa: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pool_and_spa, Unset):
            pool_and_spa = self.pool_and_spa.to_dict()

        sustainability: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sustainability, Unset):
            sustainability = self.sustainability.to_dict()

        entertainment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entertainment, Unset):
            entertainment = self.entertainment.to_dict()

        outdoor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.outdoor, Unset):
            outdoor = self.outdoor.to_dict()

        onsite_service: dict[str, Any] | Unset = UNSET
        if not isinstance(self.onsite_service, Unset):
            onsite_service = self.onsite_service.to_dict()

        accessibility: dict[str, Any] | Unset = UNSET
        if not isinstance(self.accessibility, Unset):
            accessibility = self.accessibility.to_dict()

        home_safety: dict[str, Any] | Unset = UNSET
        if not isinstance(self.home_safety, Unset):
            home_safety = self.home_safety.to_dict()

        safety_devices: dict[str, Any] | Unset = UNSET
        if not isinstance(self.safety_devices, Unset):
            safety_devices = self.safety_devices.to_dict()

        enhanced_cleaning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enhanced_cleaning, Unset):
            enhanced_cleaning = self.enhanced_cleaning.to_dict()

        location_and_view: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location_and_view, Unset):
            location_and_view = self.location_and_view.to_dict()

        local_attractions_and_activities: dict[str, Any] | Unset = UNSET
        if not isinstance(self.local_attractions_and_activities, Unset):
            local_attractions_and_activities = self.local_attractions_and_activities.to_dict()

        checkout_instructions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.checkout_instructions, Unset):
            checkout_instructions = self.checkout_instructions.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if essentials is not UNSET:
            field_dict["essentials"] = essentials
        if internet is not UNSET:
            field_dict["internet"] = internet
        if climate_control is not UNSET:
            field_dict["climateControl"] = climate_control
        if general is not UNSET:
            field_dict["general"] = general
        if office is not UNSET:
            field_dict["office"] = office
        if kitchen_and_dining is not UNSET:
            field_dict["kitchenAndDining"] = kitchen_and_dining
        if parking is not UNSET:
            field_dict["parking"] = parking
        if pool_and_spa is not UNSET:
            field_dict["poolAndSpa"] = pool_and_spa
        if sustainability is not UNSET:
            field_dict["sustainability"] = sustainability
        if entertainment is not UNSET:
            field_dict["entertainment"] = entertainment
        if outdoor is not UNSET:
            field_dict["outdoor"] = outdoor
        if onsite_service is not UNSET:
            field_dict["onsiteService"] = onsite_service
        if accessibility is not UNSET:
            field_dict["accessibility"] = accessibility
        if home_safety is not UNSET:
            field_dict["homeSafety"] = home_safety
        if safety_devices is not UNSET:
            field_dict["safetyDevices"] = safety_devices
        if enhanced_cleaning is not UNSET:
            field_dict["enhancedCleaning"] = enhanced_cleaning
        if location_and_view is not UNSET:
            field_dict["locationAndView"] = location_and_view
        if local_attractions_and_activities is not UNSET:
            field_dict["localAttractionsAndActivities"] = local_attractions_and_activities
        if checkout_instructions is not UNSET:
            field_dict["checkoutInstructions"] = checkout_instructions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_amenities_body_groups_accessibility import UpdateVrboListingAmenitiesBodyGroupsAccessibility
        from ..models.update_vrbo_listing_amenities_body_groups_checkout_instructions import UpdateVrboListingAmenitiesBodyGroupsCheckoutInstructions
        from ..models.update_vrbo_listing_amenities_body_groups_climate_control import UpdateVrboListingAmenitiesBodyGroupsClimateControl
        from ..models.update_vrbo_listing_amenities_body_groups_enhanced_cleaning import UpdateVrboListingAmenitiesBodyGroupsEnhancedCleaning
        from ..models.update_vrbo_listing_amenities_body_groups_entertainment import UpdateVrboListingAmenitiesBodyGroupsEntertainment
        from ..models.update_vrbo_listing_amenities_body_groups_essentials import UpdateVrboListingAmenitiesBodyGroupsEssentials
        from ..models.update_vrbo_listing_amenities_body_groups_general import UpdateVrboListingAmenitiesBodyGroupsGeneral
        from ..models.update_vrbo_listing_amenities_body_groups_home_safety import UpdateVrboListingAmenitiesBodyGroupsHomeSafety
        from ..models.update_vrbo_listing_amenities_body_groups_internet import UpdateVrboListingAmenitiesBodyGroupsInternet
        from ..models.update_vrbo_listing_amenities_body_groups_kitchen_and_dining import UpdateVrboListingAmenitiesBodyGroupsKitchenAndDining
        from ..models.update_vrbo_listing_amenities_body_groups_local_attractions_and_activities import UpdateVrboListingAmenitiesBodyGroupsLocalAttractionsAndActivities
        from ..models.update_vrbo_listing_amenities_body_groups_location_and_view import UpdateVrboListingAmenitiesBodyGroupsLocationAndView
        from ..models.update_vrbo_listing_amenities_body_groups_office import UpdateVrboListingAmenitiesBodyGroupsOffice
        from ..models.update_vrbo_listing_amenities_body_groups_onsite_service import UpdateVrboListingAmenitiesBodyGroupsOnsiteService
        from ..models.update_vrbo_listing_amenities_body_groups_outdoor import UpdateVrboListingAmenitiesBodyGroupsOutdoor
        from ..models.update_vrbo_listing_amenities_body_groups_parking import UpdateVrboListingAmenitiesBodyGroupsParking
        from ..models.update_vrbo_listing_amenities_body_groups_pool_and_spa import UpdateVrboListingAmenitiesBodyGroupsPoolAndSpa
        from ..models.update_vrbo_listing_amenities_body_groups_safety_devices import UpdateVrboListingAmenitiesBodyGroupsSafetyDevices
        from ..models.update_vrbo_listing_amenities_body_groups_sustainability import UpdateVrboListingAmenitiesBodyGroupsSustainability
        d = dict(src_dict)
        _essentials = d.pop("essentials", UNSET)
        essentials: UpdateVrboListingAmenitiesBodyGroupsEssentials | Unset
        if isinstance(_essentials,  Unset):
            essentials = UNSET
        else:
            essentials = UpdateVrboListingAmenitiesBodyGroupsEssentials.from_dict(_essentials)




        _internet = d.pop("internet", UNSET)
        internet: UpdateVrboListingAmenitiesBodyGroupsInternet | Unset
        if isinstance(_internet,  Unset):
            internet = UNSET
        else:
            internet = UpdateVrboListingAmenitiesBodyGroupsInternet.from_dict(_internet)




        _climate_control = d.pop("climateControl", UNSET)
        climate_control: UpdateVrboListingAmenitiesBodyGroupsClimateControl | Unset
        if isinstance(_climate_control,  Unset):
            climate_control = UNSET
        else:
            climate_control = UpdateVrboListingAmenitiesBodyGroupsClimateControl.from_dict(_climate_control)




        _general = d.pop("general", UNSET)
        general: UpdateVrboListingAmenitiesBodyGroupsGeneral | Unset
        if isinstance(_general,  Unset):
            general = UNSET
        else:
            general = UpdateVrboListingAmenitiesBodyGroupsGeneral.from_dict(_general)




        _office = d.pop("office", UNSET)
        office: UpdateVrboListingAmenitiesBodyGroupsOffice | Unset
        if isinstance(_office,  Unset):
            office = UNSET
        else:
            office = UpdateVrboListingAmenitiesBodyGroupsOffice.from_dict(_office)




        _kitchen_and_dining = d.pop("kitchenAndDining", UNSET)
        kitchen_and_dining: UpdateVrboListingAmenitiesBodyGroupsKitchenAndDining | Unset
        if isinstance(_kitchen_and_dining,  Unset):
            kitchen_and_dining = UNSET
        else:
            kitchen_and_dining = UpdateVrboListingAmenitiesBodyGroupsKitchenAndDining.from_dict(_kitchen_and_dining)




        _parking = d.pop("parking", UNSET)
        parking: UpdateVrboListingAmenitiesBodyGroupsParking | Unset
        if isinstance(_parking,  Unset):
            parking = UNSET
        else:
            parking = UpdateVrboListingAmenitiesBodyGroupsParking.from_dict(_parking)




        _pool_and_spa = d.pop("poolAndSpa", UNSET)
        pool_and_spa: UpdateVrboListingAmenitiesBodyGroupsPoolAndSpa | Unset
        if isinstance(_pool_and_spa,  Unset):
            pool_and_spa = UNSET
        else:
            pool_and_spa = UpdateVrboListingAmenitiesBodyGroupsPoolAndSpa.from_dict(_pool_and_spa)




        _sustainability = d.pop("sustainability", UNSET)
        sustainability: UpdateVrboListingAmenitiesBodyGroupsSustainability | Unset
        if isinstance(_sustainability,  Unset):
            sustainability = UNSET
        else:
            sustainability = UpdateVrboListingAmenitiesBodyGroupsSustainability.from_dict(_sustainability)




        _entertainment = d.pop("entertainment", UNSET)
        entertainment: UpdateVrboListingAmenitiesBodyGroupsEntertainment | Unset
        if isinstance(_entertainment,  Unset):
            entertainment = UNSET
        else:
            entertainment = UpdateVrboListingAmenitiesBodyGroupsEntertainment.from_dict(_entertainment)




        _outdoor = d.pop("outdoor", UNSET)
        outdoor: UpdateVrboListingAmenitiesBodyGroupsOutdoor | Unset
        if isinstance(_outdoor,  Unset):
            outdoor = UNSET
        else:
            outdoor = UpdateVrboListingAmenitiesBodyGroupsOutdoor.from_dict(_outdoor)




        _onsite_service = d.pop("onsiteService", UNSET)
        onsite_service: UpdateVrboListingAmenitiesBodyGroupsOnsiteService | Unset
        if isinstance(_onsite_service,  Unset):
            onsite_service = UNSET
        else:
            onsite_service = UpdateVrboListingAmenitiesBodyGroupsOnsiteService.from_dict(_onsite_service)




        _accessibility = d.pop("accessibility", UNSET)
        accessibility: UpdateVrboListingAmenitiesBodyGroupsAccessibility | Unset
        if isinstance(_accessibility,  Unset):
            accessibility = UNSET
        else:
            accessibility = UpdateVrboListingAmenitiesBodyGroupsAccessibility.from_dict(_accessibility)




        _home_safety = d.pop("homeSafety", UNSET)
        home_safety: UpdateVrboListingAmenitiesBodyGroupsHomeSafety | Unset
        if isinstance(_home_safety,  Unset):
            home_safety = UNSET
        else:
            home_safety = UpdateVrboListingAmenitiesBodyGroupsHomeSafety.from_dict(_home_safety)




        _safety_devices = d.pop("safetyDevices", UNSET)
        safety_devices: UpdateVrboListingAmenitiesBodyGroupsSafetyDevices | Unset
        if isinstance(_safety_devices,  Unset):
            safety_devices = UNSET
        else:
            safety_devices = UpdateVrboListingAmenitiesBodyGroupsSafetyDevices.from_dict(_safety_devices)




        _enhanced_cleaning = d.pop("enhancedCleaning", UNSET)
        enhanced_cleaning: UpdateVrboListingAmenitiesBodyGroupsEnhancedCleaning | Unset
        if isinstance(_enhanced_cleaning,  Unset):
            enhanced_cleaning = UNSET
        else:
            enhanced_cleaning = UpdateVrboListingAmenitiesBodyGroupsEnhancedCleaning.from_dict(_enhanced_cleaning)




        _location_and_view = d.pop("locationAndView", UNSET)
        location_and_view: UpdateVrboListingAmenitiesBodyGroupsLocationAndView | Unset
        if isinstance(_location_and_view,  Unset):
            location_and_view = UNSET
        else:
            location_and_view = UpdateVrboListingAmenitiesBodyGroupsLocationAndView.from_dict(_location_and_view)




        _local_attractions_and_activities = d.pop("localAttractionsAndActivities", UNSET)
        local_attractions_and_activities: UpdateVrboListingAmenitiesBodyGroupsLocalAttractionsAndActivities | Unset
        if isinstance(_local_attractions_and_activities,  Unset):
            local_attractions_and_activities = UNSET
        else:
            local_attractions_and_activities = UpdateVrboListingAmenitiesBodyGroupsLocalAttractionsAndActivities.from_dict(_local_attractions_and_activities)




        _checkout_instructions = d.pop("checkoutInstructions", UNSET)
        checkout_instructions: UpdateVrboListingAmenitiesBodyGroupsCheckoutInstructions | Unset
        if isinstance(_checkout_instructions,  Unset):
            checkout_instructions = UNSET
        else:
            checkout_instructions = UpdateVrboListingAmenitiesBodyGroupsCheckoutInstructions.from_dict(_checkout_instructions)




        update_vrbo_listing_amenities_body_groups = cls(
            essentials=essentials,
            internet=internet,
            climate_control=climate_control,
            general=general,
            office=office,
            kitchen_and_dining=kitchen_and_dining,
            parking=parking,
            pool_and_spa=pool_and_spa,
            sustainability=sustainability,
            entertainment=entertainment,
            outdoor=outdoor,
            onsite_service=onsite_service,
            accessibility=accessibility,
            home_safety=home_safety,
            safety_devices=safety_devices,
            enhanced_cleaning=enhanced_cleaning,
            location_and_view=location_and_view,
            local_attractions_and_activities=local_attractions_and_activities,
            checkout_instructions=checkout_instructions,
        )

        return update_vrbo_listing_amenities_body_groups

