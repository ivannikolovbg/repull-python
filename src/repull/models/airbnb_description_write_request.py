from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_description_write_request_description import AirbnbDescriptionWriteRequestDescription





T = TypeVar("T", bound="AirbnbDescriptionWriteRequest")



@_attrs_define
class AirbnbDescriptionWriteRequest:
    """ Write one locale's copy. Airbnb keeps a separate description per locale, which is why the locale is explicit:
    writing Italian copy into the English row is how a translation gets lost. Only the fields you send are written.

        Attributes:
            locale (str): Language tag — `en`, `it`, `pt-BR`. `GET /v1/channels/airbnb/listings/{id}/settings?type=locales`
                lists the locales already synced for this listing. Example: it.
            description (AirbnbDescriptionWriteRequestDescription): At least one field required. `description` itself is NOT
                accepted: Airbnb composes the public description from these sections and ignores a directly-supplied one, so
                accepting it would be taking a value and discarding it. An unknown field is refused by name rather than dropped.
     """

    locale: str
    description: AirbnbDescriptionWriteRequestDescription
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_description_write_request_description import AirbnbDescriptionWriteRequestDescription
        locale = self.locale

        description = self.description.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "locale": locale,
            "description": description,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_description_write_request_description import AirbnbDescriptionWriteRequestDescription
        d = dict(src_dict)
        locale = d.pop("locale")

        description = AirbnbDescriptionWriteRequestDescription.from_dict(d.pop("description"))




        airbnb_description_write_request = cls(
            locale=locale,
            description=description,
        )


        airbnb_description_write_request.additional_properties = d
        return airbnb_description_write_request

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
