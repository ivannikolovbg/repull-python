from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.publish_listing_to_vrbo_body_sections_item import PublishListingToVrboBodySectionsItem
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PublishListingToVrboBody")



@_attrs_define
class PublishListingToVrboBody:
    """ 
        Attributes:
            account_id (str | Unset): The Vrbo account, as its handle (`"vrbo:7001234"`, Vrbo's own account id) or the bare
                id. Needed only when the workspace has several. The old sign-in ids (`"vrbo:13"`) still resolve until
                2027-02-12.
            property_id (str | Unset): Finish this unpublished Vrbo property (from a failed run's `job.propertyId`) instead
                of starting a new one.
            sections (list[PublishListingToVrboBodySectionsItem] | Unset): Update only: push just these sections (default:
                all of them).
            vrbo_listing_number (str | Unset): Update only: the Vrbo listing to push to, when the listing is linked to
                several.
     """

    account_id: str | Unset = UNSET
    property_id: str | Unset = UNSET
    sections: list[PublishListingToVrboBodySectionsItem] | Unset = UNSET
    vrbo_listing_number: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        property_id = self.property_id

        sections: list[str] | Unset = UNSET
        if not isinstance(self.sections, Unset):
            sections = []
            for sections_item_data in self.sections:
                sections_item = sections_item_data.value
                sections.append(sections_item)



        vrbo_listing_number = self.vrbo_listing_number


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if sections is not UNSET:
            field_dict["sections"] = sections
        if vrbo_listing_number is not UNSET:
            field_dict["vrboListingNumber"] = vrbo_listing_number

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        property_id = d.pop("propertyId", UNSET)

        _sections = d.pop("sections", UNSET)
        sections: list[PublishListingToVrboBodySectionsItem] | Unset = UNSET
        if _sections is not UNSET:
            sections = []
            for sections_item_data in _sections:
                sections_item = PublishListingToVrboBodySectionsItem(sections_item_data)



                sections.append(sections_item)


        vrbo_listing_number = d.pop("vrboListingNumber", UNSET)

        publish_listing_to_vrbo_body = cls(
            account_id=account_id,
            property_id=property_id,
            sections=sections,
            vrbo_listing_number=vrbo_listing_number,
        )

        return publish_listing_to_vrbo_body

