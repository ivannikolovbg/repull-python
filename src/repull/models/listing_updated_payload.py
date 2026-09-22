from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.listing_updated_payload_area import ListingUpdatedPayloadArea
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.listing_updated_payload_previous_attributes import ListingUpdatedPayloadPreviousAttributes
  from ..models.listing_webhook_object import ListingWebhookObject





T = TypeVar("T", bound="ListingUpdatedPayload")



@_attrs_define
class ListingUpdatedPayload:
    """ Payload for `listing.updated`. Something about the listing changed on the channel — content, pricing, booking
    settings, house rules, availability or sync settings.

        Attributes:
            object_ (ListingWebhookObject): The listing, in the shape `GET /v1/listings/{id}` returns. Hydrated at delivery,
                so a receiver gets the listing rather than a reason to fetch one.
            area (ListingUpdatedPayloadArea | Unset): Which part moved. Airbnb sends one notification per area rather than a
                diff, so this is the signal for what to re-read. Example: content.
            previous_attributes (ListingUpdatedPayloadPreviousAttributes | Unset): Fields that changed and their prior
                values, when the source reports them.
            revision (datetime.datetime | None | Unset):
     """

    object_: ListingWebhookObject
    area: ListingUpdatedPayloadArea | Unset = UNSET
    previous_attributes: ListingUpdatedPayloadPreviousAttributes | Unset = UNSET
    revision: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.listing_updated_payload_previous_attributes import ListingUpdatedPayloadPreviousAttributes
        from ..models.listing_webhook_object import ListingWebhookObject
        object_ = self.object_.to_dict()

        area: str | Unset = UNSET
        if not isinstance(self.area, Unset):
            area = self.area.value


        previous_attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.previous_attributes, Unset):
            previous_attributes = self.previous_attributes.to_dict()

        revision: None | str | Unset
        if isinstance(self.revision, Unset):
            revision = UNSET
        elif isinstance(self.revision, datetime.datetime):
            revision = self.revision.isoformat()
        else:
            revision = self.revision


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "object": object_,
        })
        if area is not UNSET:
            field_dict["area"] = area
        if previous_attributes is not UNSET:
            field_dict["previousAttributes"] = previous_attributes
        if revision is not UNSET:
            field_dict["revision"] = revision

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.listing_updated_payload_previous_attributes import ListingUpdatedPayloadPreviousAttributes
        from ..models.listing_webhook_object import ListingWebhookObject
        d = dict(src_dict)
        object_ = ListingWebhookObject.from_dict(d.pop("object"))




        _area = d.pop("area", UNSET)
        area: ListingUpdatedPayloadArea | Unset
        if isinstance(_area,  Unset):
            area = UNSET
        else:
            area = ListingUpdatedPayloadArea(_area)




        _previous_attributes = d.pop("previousAttributes", UNSET)
        previous_attributes: ListingUpdatedPayloadPreviousAttributes | Unset
        if isinstance(_previous_attributes,  Unset):
            previous_attributes = UNSET
        else:
            previous_attributes = ListingUpdatedPayloadPreviousAttributes.from_dict(_previous_attributes)




        def _parse_revision(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revision_type_0 = isoparse(data)



                return revision_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        revision = _parse_revision(d.pop("revision", UNSET))


        listing_updated_payload = cls(
            object_=object_,
            area=area,
            previous_attributes=previous_attributes,
            revision=revision,
        )


        listing_updated_payload.additional_properties = d
        return listing_updated_payload

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
