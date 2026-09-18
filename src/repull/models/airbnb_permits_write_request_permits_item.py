from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_permits_write_request_permits_item_answers_item import AirbnbPermitsWriteRequestPermitsItemAnswersItem





T = TypeVar("T", bound="AirbnbPermitsWriteRequestPermitsItem")



@_attrs_define
class AirbnbPermitsWriteRequestPermitsItem:
    """ 
        Attributes:
            regulatory_body (str): As named by the GET, e.g. the city or registry asking.
            regulation_type (str):
            answers (list[AirbnbPermitsWriteRequestPermitsItemAnswersItem]):
     """

    regulatory_body: str
    regulation_type: str
    answers: list[AirbnbPermitsWriteRequestPermitsItemAnswersItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_permits_write_request_permits_item_answers_item import AirbnbPermitsWriteRequestPermitsItemAnswersItem
        regulatory_body = self.regulatory_body

        regulation_type = self.regulation_type

        answers = []
        for answers_item_data in self.answers:
            answers_item = answers_item_data.to_dict()
            answers.append(answers_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "regulatory_body": regulatory_body,
            "regulation_type": regulation_type,
            "answers": answers,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_permits_write_request_permits_item_answers_item import AirbnbPermitsWriteRequestPermitsItemAnswersItem
        d = dict(src_dict)
        regulatory_body = d.pop("regulatory_body")

        regulation_type = d.pop("regulation_type")

        answers = []
        _answers = d.pop("answers")
        for answers_item_data in (_answers):
            answers_item = AirbnbPermitsWriteRequestPermitsItemAnswersItem.from_dict(answers_item_data)



            answers.append(answers_item)


        airbnb_permits_write_request_permits_item = cls(
            regulatory_body=regulatory_body,
            regulation_type=regulation_type,
            answers=answers,
        )

        return airbnb_permits_write_request_permits_item

