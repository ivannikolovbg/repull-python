from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="CreateStudioProjectGenerationResponse201Data")



@_attrs_define
class CreateStudioProjectGenerationResponse201Data:
    """ 
        Attributes:
            generation_id (UUID | Unset):
            response (str | Unset):
            tokens_out (int | Unset):
     """

    generation_id: UUID | Unset = UNSET
    response: str | Unset = UNSET
    tokens_out: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        generation_id: str | Unset = UNSET
        if not isinstance(self.generation_id, Unset):
            generation_id = str(self.generation_id)

        response = self.response

        tokens_out = self.tokens_out


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if generation_id is not UNSET:
            field_dict["generation_id"] = generation_id
        if response is not UNSET:
            field_dict["response"] = response
        if tokens_out is not UNSET:
            field_dict["tokens_out"] = tokens_out

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _generation_id = d.pop("generation_id", UNSET)
        generation_id: UUID | Unset
        if isinstance(_generation_id,  Unset):
            generation_id = UNSET
        else:
            generation_id = UUID(_generation_id)




        response = d.pop("response", UNSET)

        tokens_out = d.pop("tokens_out", UNSET)

        create_studio_project_generation_response_201_data = cls(
            generation_id=generation_id,
            response=response,
            tokens_out=tokens_out,
        )


        create_studio_project_generation_response_201_data.additional_properties = d
        return create_studio_project_generation_response_201_data

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
