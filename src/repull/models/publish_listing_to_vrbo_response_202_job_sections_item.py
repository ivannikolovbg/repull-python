from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.publish_listing_to_vrbo_response_202_job_sections_item_status import PublishListingToVrboResponse202JobSectionsItemStatus
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.publish_listing_to_vrbo_response_202_job_sections_item_errors_item import PublishListingToVrboResponse202JobSectionsItemErrorsItem
  from ..models.publish_listing_to_vrbo_response_202_job_sections_item_sent import PublishListingToVrboResponse202JobSectionsItemSent





T = TypeVar("T", bound="PublishListingToVrboResponse202JobSectionsItem")



@_attrs_define
class PublishListingToVrboResponse202JobSectionsItem:
    """ 
        Attributes:
            section (str | Unset):  Example: house-rules.
            status (PublishListingToVrboResponse202JobSectionsItemStatus | Unset): `rejected`: Vrbo refused something (its
                message in `errors`); `failed`: the write did not complete (e.g. Vrbo paused the account).
            sent (PublishListingToVrboResponse202JobSectionsItemSent | Unset): The partial section input sent — the body
                `PUT /v1/channels/vrbo/listings/{id}/{section}` takes.
            errors (list[PublishListingToVrboResponse202JobSectionsItemErrorsItem] | Unset):
            data (Any | Unset): What Vrbo has stored for the section after the write.
            finished_at (datetime.datetime | None | Unset):
     """

    section: str | Unset = UNSET
    status: PublishListingToVrboResponse202JobSectionsItemStatus | Unset = UNSET
    sent: PublishListingToVrboResponse202JobSectionsItemSent | Unset = UNSET
    errors: list[PublishListingToVrboResponse202JobSectionsItemErrorsItem] | Unset = UNSET
    data: Any | Unset = UNSET
    finished_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.publish_listing_to_vrbo_response_202_job_sections_item_errors_item import PublishListingToVrboResponse202JobSectionsItemErrorsItem
        from ..models.publish_listing_to_vrbo_response_202_job_sections_item_sent import PublishListingToVrboResponse202JobSectionsItemSent
        section = self.section

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        sent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sent, Unset):
            sent = self.sent.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)



        data = self.data

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
        if section is not UNSET:
            field_dict["section"] = section
        if status is not UNSET:
            field_dict["status"] = status
        if sent is not UNSET:
            field_dict["sent"] = sent
        if errors is not UNSET:
            field_dict["errors"] = errors
        if data is not UNSET:
            field_dict["data"] = data
        if finished_at is not UNSET:
            field_dict["finishedAt"] = finished_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.publish_listing_to_vrbo_response_202_job_sections_item_errors_item import PublishListingToVrboResponse202JobSectionsItemErrorsItem
        from ..models.publish_listing_to_vrbo_response_202_job_sections_item_sent import PublishListingToVrboResponse202JobSectionsItemSent
        d = dict(src_dict)
        section = d.pop("section", UNSET)

        _status = d.pop("status", UNSET)
        status: PublishListingToVrboResponse202JobSectionsItemStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = PublishListingToVrboResponse202JobSectionsItemStatus(_status)




        _sent = d.pop("sent", UNSET)
        sent: PublishListingToVrboResponse202JobSectionsItemSent | Unset
        if isinstance(_sent,  Unset):
            sent = UNSET
        else:
            sent = PublishListingToVrboResponse202JobSectionsItemSent.from_dict(_sent)




        _errors = d.pop("errors", UNSET)
        errors: list[PublishListingToVrboResponse202JobSectionsItemErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = PublishListingToVrboResponse202JobSectionsItemErrorsItem.from_dict(errors_item_data)



                errors.append(errors_item)


        data = d.pop("data", UNSET)

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


        publish_listing_to_vrbo_response_202_job_sections_item = cls(
            section=section,
            status=status,
            sent=sent,
            errors=errors,
            data=data,
            finished_at=finished_at,
        )


        publish_listing_to_vrbo_response_202_job_sections_item.additional_properties = d
        return publish_listing_to_vrbo_response_202_job_sections_item

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
