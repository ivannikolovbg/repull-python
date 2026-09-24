from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_permits_write_request_permits_item_answers import AirbnbPermitsWriteRequestPermitsItemAnswers





T = TypeVar("T", bound="AirbnbPermitsWriteRequestPermitsItem")



@_attrs_define
class AirbnbPermitsWriteRequestPermitsItem:
    """ 
        Attributes:
            regulatory_body (str): As returned by the GET, e.g. `maui_county_hawaii`.
            regulation_type (str): As returned by the GET.
            flow_slug (str): The `slug` of the flow you are answering, e.g. `existing_registration` or `exemption_claim`.
            answers (AirbnbPermitsWriteRequestPermitsItemAnswers): Keyed by each question's `answer_key`. Each value carries
                exactly one field, chosen by the question's `type`: TEXT → `text_value`, ATTESTATION → `attestation_value`,
                RADIO → `radio_value`, DATE → `date_value`, SELECT → `selected_options_value`.
            regulation_context (str | Unset): Echo the GET's `regulation_context` (e.g. `initial`) when present.
     """

    regulatory_body: str
    regulation_type: str
    flow_slug: str
    answers: AirbnbPermitsWriteRequestPermitsItemAnswers
    regulation_context: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_permits_write_request_permits_item_answers import AirbnbPermitsWriteRequestPermitsItemAnswers
        regulatory_body = self.regulatory_body

        regulation_type = self.regulation_type

        flow_slug = self.flow_slug

        answers = self.answers.to_dict()

        regulation_context = self.regulation_context


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "regulatory_body": regulatory_body,
            "regulation_type": regulation_type,
            "flow_slug": flow_slug,
            "answers": answers,
        })
        if regulation_context is not UNSET:
            field_dict["regulation_context"] = regulation_context

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_permits_write_request_permits_item_answers import AirbnbPermitsWriteRequestPermitsItemAnswers
        d = dict(src_dict)
        regulatory_body = d.pop("regulatory_body")

        regulation_type = d.pop("regulation_type")

        flow_slug = d.pop("flow_slug")

        answers = AirbnbPermitsWriteRequestPermitsItemAnswers.from_dict(d.pop("answers"))




        regulation_context = d.pop("regulation_context", UNSET)

        airbnb_permits_write_request_permits_item = cls(
            regulatory_body=regulatory_body,
            regulation_type=regulation_type,
            flow_slug=flow_slug,
            answers=answers,
            regulation_context=regulation_context,
        )

        return airbnb_permits_write_request_permits_item

