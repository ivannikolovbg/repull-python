from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_permits_write_request_permits_item_answers_additional_property import AirbnbPermitsWriteRequestPermitsItemAnswersAdditionalProperty





T = TypeVar("T", bound="AirbnbPermitsWriteRequestPermitsItemAnswers")



@_attrs_define
class AirbnbPermitsWriteRequestPermitsItemAnswers:
    """ Keyed by each question's `answer_key`. Each value carries exactly one `<type>_value` field named after the
    question's `type` (lower-case): `text_value`, `attestation_value` (boolean), `radio_value`, `dropdown_value`,
    `email_value`, `future_date_value` (YYYY-MM-DD) and `file_upload_value` (object with the base64 file) are the ones
    Airbnb returns in production; other question types follow the same pattern. Airbnb validates the value against its
    question. Example: `{"email": {"email_value": "host@example.com"}, "expiration_date": {"future_date_value":
    "2029-02-04"}, "attestation": {"attestation_value": true}}`.

     """

    additional_properties: dict[str, AirbnbPermitsWriteRequestPermitsItemAnswersAdditionalProperty] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_permits_write_request_permits_item_answers_additional_property import AirbnbPermitsWriteRequestPermitsItemAnswersAdditionalProperty
        
        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()


        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_permits_write_request_permits_item_answers_additional_property import AirbnbPermitsWriteRequestPermitsItemAnswersAdditionalProperty
        d = dict(src_dict)
        airbnb_permits_write_request_permits_item_answers = cls(
        )


        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AirbnbPermitsWriteRequestPermitsItemAnswersAdditionalProperty.from_dict(prop_dict)



            additional_properties[prop_name] = additional_property

        airbnb_permits_write_request_permits_item_answers.additional_properties = additional_properties
        return airbnb_permits_write_request_permits_item_answers

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> AirbnbPermitsWriteRequestPermitsItemAnswersAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: AirbnbPermitsWriteRequestPermitsItemAnswersAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
