from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.publish_section_error import PublishSectionError





T = TypeVar("T", bound="AirbnbPublishResult")



@_attrs_define
class AirbnbPublishResult:
    """ A publish is not one call to Airbnb: it is up to eight independent ones (details, description, amenities, rooms,
    policies, photos, pricing, checkout_tasks), each of which can fail on its own. A PARTIAL publish is normal — what
    succeeded stays applied; there is no rollback.

    **Content landing and the listing being live are two different answers.** `published` is about content; `live` is
    about whether the listing takes bookings. Read both.

        Attributes:
            published (bool): True only when EVERY attempted section reached Airbnb.
            sections (list[str]): Sections that landed on Airbnb. Example: ['details', 'pricing', 'photos'].
            errors (list[PublishSectionError]): Per-section failures. Empty when `published` is true.
            warnings (list[str]): Steps that failed WITHOUT failing the publish — optional work the push carried on past,
                each in the push's own words. These used to be swallowed silently, so the only sign of one was a listing that
                was somehow not quite right afterwards. A publish can be `published: true` and still carry warnings; read them
                before concluding nothing needs doing. Example: ['instant booking could not be confirmed off — listing left
                inactive'].
            locked_fields (list[str]): Fields Airbnb will not let this listing change — collected from the failures above
                and from the `locked_attributes` Airbnb recorded for the listing. Sending them again returns success and changes
                nothing.
            live (bool | Unset): Whether the listing is active and bookable on Airbnb — that is, whether activation was
                actually performed and succeeded.

                `published: true` with `live: false` is a real and common outcome: every content section landed, but the listing
                was never activated, because activation is skipped when instant-booking cannot be confirmed to be off.
                `warnings` says why.

                **Absent is not `false`.** The field is omitted entirely when activation was never part of the operation —
                publishing to an already-mapped Airbnb listing updates content and activates nothing, so there is nothing to
                report. Only treat the listing as not-live when `live` is present and false.
            reason (str | Unset): Set when the publish never started at all (no connection, address missing, subscription
                gate).
     """

    published: bool
    sections: list[str]
    errors: list[PublishSectionError]
    warnings: list[str]
    locked_fields: list[str]
    live: bool | Unset = UNSET
    reason: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.publish_section_error import PublishSectionError
        published = self.published

        sections = self.sections



        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)



        warnings = self.warnings



        locked_fields = self.locked_fields



        live = self.live

        reason = self.reason


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "published": published,
            "sections": sections,
            "errors": errors,
            "warnings": warnings,
            "lockedFields": locked_fields,
        })
        if live is not UNSET:
            field_dict["live"] = live
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.publish_section_error import PublishSectionError
        d = dict(src_dict)
        published = d.pop("published")

        sections = cast(list[str], d.pop("sections"))


        errors = []
        _errors = d.pop("errors")
        for errors_item_data in (_errors):
            errors_item = PublishSectionError.from_dict(errors_item_data)



            errors.append(errors_item)


        warnings = cast(list[str], d.pop("warnings"))


        locked_fields = cast(list[str], d.pop("lockedFields"))


        live = d.pop("live", UNSET)

        reason = d.pop("reason", UNSET)

        airbnb_publish_result = cls(
            published=published,
            sections=sections,
            errors=errors,
            warnings=warnings,
            locked_fields=locked_fields,
            live=live,
            reason=reason,
        )


        airbnb_publish_result.additional_properties = d
        return airbnb_publish_result

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
