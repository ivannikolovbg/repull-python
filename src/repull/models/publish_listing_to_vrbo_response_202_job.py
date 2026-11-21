from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.publish_listing_to_vrbo_response_202_job_mode import PublishListingToVrboResponse202JobMode
from ..models.publish_listing_to_vrbo_response_202_job_status import PublishListingToVrboResponse202JobStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.publish_listing_to_vrbo_response_202_job_rejected_photos_item import PublishListingToVrboResponse202JobRejectedPhotosItem
  from ..models.publish_listing_to_vrbo_response_202_job_sections_item import PublishListingToVrboResponse202JobSectionsItem
  from ..models.publish_listing_to_vrbo_response_202_job_skipped_item import PublishListingToVrboResponse202JobSkippedItem





T = TypeVar("T", bound="PublishListingToVrboResponse202Job")



@_attrs_define
class PublishListingToVrboResponse202Job:
    """ 
        Attributes:
            job_id (str | Unset): Pass to `GET /v1/listings/{id}/publish/vrbo?jobId=`. A creation is `vrbo_<n>_<n>`, a push
                onto an existing Vrbo listing `vrbo_push_<n>_<n>`.
            mode (PublishListingToVrboResponse202JobMode | Unset): `create`: the listing is being created on Vrbo. `update`:
                it was already on Vrbo and its content is being pushed onto that listing.
            status (PublishListingToVrboResponse202JobStatus | Unset):
            listing_id (int | Unset):
            account_id (None | str | Unset): The Vrbo account the listing is created in, as its handle `vrbo:{Vrbo account
                id}`. `null` until Vrbo's account id is captured for the sign-in.
            steps (list[str] | Unset): Steps Vrbo has finished, in order: create, amenities, property type, rooms, photos,
                headline + description, house rules, rate, booking options, publish, fees, cancellation policy, …
            error (None | str | Unset): Vrbo's reason when `status` is `failed`.
            vrbo_listing_number (None | str | Unset): The new Vrbo listing number, once Vrbo has published it.
            property_id (None | str | Unset): The Vrbo property being built. Send it back as `propertyId` to finish a run
                that failed part-way.
            linked (bool | Unset): The new Vrbo unit is linked to the listing with calendar sync on, and the whole calendar
                has been queued to Vrbo.
            rejected_photos (list[PublishListingToVrboResponse202JobRejectedPhotosItem] | Unset): Photos Vrbo's review
                refused (position in the listing's order, and Vrbo's reason).
            adjustments (list[str] | Unset): POST only: where the Vrbo listing departs from the listing's content because of
                a Vrbo rule.
            resumed_property_id (None | str | Unset): POST only: set when an unfinished Vrbo property of this listing is
                completed instead of starting a new one.
            sections (list[PublishListingToVrboResponse202JobSectionsItem] | Unset): Update only: each section pushed, in
                order, with what was sent, Vrbo's refusals and what Vrbo has stored after the write.
            skipped (list[PublishListingToVrboResponse202JobSkippedItem] | Unset): Update only: sections the push leaves as
                they are on Vrbo, and why (rooms, photos, permits, or no value in the listing content).
            started_at (datetime.datetime | Unset): Update only.
            finished_at (datetime.datetime | None | Unset): Update only.
     """

    job_id: str | Unset = UNSET
    mode: PublishListingToVrboResponse202JobMode | Unset = UNSET
    status: PublishListingToVrboResponse202JobStatus | Unset = UNSET
    listing_id: int | Unset = UNSET
    account_id: None | str | Unset = UNSET
    steps: list[str] | Unset = UNSET
    error: None | str | Unset = UNSET
    vrbo_listing_number: None | str | Unset = UNSET
    property_id: None | str | Unset = UNSET
    linked: bool | Unset = UNSET
    rejected_photos: list[PublishListingToVrboResponse202JobRejectedPhotosItem] | Unset = UNSET
    adjustments: list[str] | Unset = UNSET
    resumed_property_id: None | str | Unset = UNSET
    sections: list[PublishListingToVrboResponse202JobSectionsItem] | Unset = UNSET
    skipped: list[PublishListingToVrboResponse202JobSkippedItem] | Unset = UNSET
    started_at: datetime.datetime | Unset = UNSET
    finished_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.publish_listing_to_vrbo_response_202_job_rejected_photos_item import PublishListingToVrboResponse202JobRejectedPhotosItem
        from ..models.publish_listing_to_vrbo_response_202_job_sections_item import PublishListingToVrboResponse202JobSectionsItem
        from ..models.publish_listing_to_vrbo_response_202_job_skipped_item import PublishListingToVrboResponse202JobSkippedItem
        job_id = self.job_id

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value


        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        listing_id = self.listing_id

        account_id: None | str | Unset
        if isinstance(self.account_id, Unset):
            account_id = UNSET
        else:
            account_id = self.account_id

        steps: list[str] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = self.steps



        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        vrbo_listing_number: None | str | Unset
        if isinstance(self.vrbo_listing_number, Unset):
            vrbo_listing_number = UNSET
        else:
            vrbo_listing_number = self.vrbo_listing_number

        property_id: None | str | Unset
        if isinstance(self.property_id, Unset):
            property_id = UNSET
        else:
            property_id = self.property_id

        linked = self.linked

        rejected_photos: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rejected_photos, Unset):
            rejected_photos = []
            for rejected_photos_item_data in self.rejected_photos:
                rejected_photos_item = rejected_photos_item_data.to_dict()
                rejected_photos.append(rejected_photos_item)



        adjustments: list[str] | Unset = UNSET
        if not isinstance(self.adjustments, Unset):
            adjustments = self.adjustments



        resumed_property_id: None | str | Unset
        if isinstance(self.resumed_property_id, Unset):
            resumed_property_id = UNSET
        else:
            resumed_property_id = self.resumed_property_id

        sections: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sections, Unset):
            sections = []
            for sections_item_data in self.sections:
                sections_item = sections_item_data.to_dict()
                sections.append(sections_item)



        skipped: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skipped, Unset):
            skipped = []
            for skipped_item_data in self.skipped:
                skipped_item = skipped_item_data.to_dict()
                skipped.append(skipped_item)



        started_at: str | Unset = UNSET
        if not isinstance(self.started_at, Unset):
            started_at = self.started_at.isoformat()

        finished_at: None | str | Unset
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        elif isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if job_id is not UNSET:
            field_dict["jobId"] = job_id
        if mode is not UNSET:
            field_dict["mode"] = mode
        if status is not UNSET:
            field_dict["status"] = status
        if listing_id is not UNSET:
            field_dict["listingId"] = listing_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if steps is not UNSET:
            field_dict["steps"] = steps
        if error is not UNSET:
            field_dict["error"] = error
        if vrbo_listing_number is not UNSET:
            field_dict["vrboListingNumber"] = vrbo_listing_number
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if linked is not UNSET:
            field_dict["linked"] = linked
        if rejected_photos is not UNSET:
            field_dict["rejectedPhotos"] = rejected_photos
        if adjustments is not UNSET:
            field_dict["adjustments"] = adjustments
        if resumed_property_id is not UNSET:
            field_dict["resumedPropertyId"] = resumed_property_id
        if sections is not UNSET:
            field_dict["sections"] = sections
        if skipped is not UNSET:
            field_dict["skipped"] = skipped
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.publish_listing_to_vrbo_response_202_job_rejected_photos_item import PublishListingToVrboResponse202JobRejectedPhotosItem
        from ..models.publish_listing_to_vrbo_response_202_job_sections_item import PublishListingToVrboResponse202JobSectionsItem
        from ..models.publish_listing_to_vrbo_response_202_job_skipped_item import PublishListingToVrboResponse202JobSkippedItem
        d = dict(src_dict)
        job_id = d.pop("jobId", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: PublishListingToVrboResponse202JobMode | Unset
        if isinstance(_mode,  Unset):
            mode = UNSET
        else:
            mode = PublishListingToVrboResponse202JobMode(_mode)




        _status = d.pop("status", UNSET)
        status: PublishListingToVrboResponse202JobStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = PublishListingToVrboResponse202JobStatus(_status)




        listing_id = d.pop("listingId", UNSET)

        def _parse_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_id = _parse_account_id(d.pop("accountId", UNSET))


        steps = cast(list[str], d.pop("steps", UNSET))


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        def _parse_vrbo_listing_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        vrbo_listing_number = _parse_vrbo_listing_number(d.pop("vrboListingNumber", UNSET))


        def _parse_property_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_id = _parse_property_id(d.pop("propertyId", UNSET))


        linked = d.pop("linked", UNSET)

        _rejected_photos = d.pop("rejectedPhotos", UNSET)
        rejected_photos: list[PublishListingToVrboResponse202JobRejectedPhotosItem] | Unset = UNSET
        if _rejected_photos is not UNSET:
            rejected_photos = []
            for rejected_photos_item_data in _rejected_photos:
                rejected_photos_item = PublishListingToVrboResponse202JobRejectedPhotosItem.from_dict(rejected_photos_item_data)



                rejected_photos.append(rejected_photos_item)


        adjustments = cast(list[str], d.pop("adjustments", UNSET))


        def _parse_resumed_property_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resumed_property_id = _parse_resumed_property_id(d.pop("resumedPropertyId", UNSET))


        _sections = d.pop("sections", UNSET)
        sections: list[PublishListingToVrboResponse202JobSectionsItem] | Unset = UNSET
        if _sections is not UNSET:
            sections = []
            for sections_item_data in _sections:
                sections_item = PublishListingToVrboResponse202JobSectionsItem.from_dict(sections_item_data)



                sections.append(sections_item)


        _skipped = d.pop("skipped", UNSET)
        skipped: list[PublishListingToVrboResponse202JobSkippedItem] | Unset = UNSET
        if _skipped is not UNSET:
            skipped = []
            for skipped_item_data in _skipped:
                skipped_item = PublishListingToVrboResponse202JobSkippedItem.from_dict(skipped_item_data)



                skipped.append(skipped_item)


        _started_at = d.pop("startedAt", UNSET)
        started_at: datetime.datetime | Unset
        if isinstance(_started_at,  Unset):
            started_at = UNSET
        else:
            started_at = isoparse(_started_at)




        def _parse_finished_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = isoparse(data)



                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        finished_at = _parse_finished_at(d.pop("finishedAt", UNSET))


        publish_listing_to_vrbo_response_202_job = cls(
            job_id=job_id,
            mode=mode,
            status=status,
            listing_id=listing_id,
            account_id=account_id,
            steps=steps,
            error=error,
            vrbo_listing_number=vrbo_listing_number,
            property_id=property_id,
            linked=linked,
            rejected_photos=rejected_photos,
            adjustments=adjustments,
            resumed_property_id=resumed_property_id,
            sections=sections,
            skipped=skipped,
            started_at=started_at,
            finished_at=finished_at,
        )


        publish_listing_to_vrbo_response_202_job.additional_properties = d
        return publish_listing_to_vrbo_response_202_job

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
