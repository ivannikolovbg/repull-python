from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="StudioGeneration")



@_attrs_define
class StudioGeneration:
    """ A single Repull AI generation run — captures the prompt, the model output, and token accounting.

        Attributes:
            generation_id (UUID | Unset):
            project_id (UUID | Unset):
            prompt (str | Unset):
            response (str | Unset): Generated text output.
            tokens_in (int | Unset): Prompt tokens consumed.
            tokens_out (int | Unset): Completion tokens produced.
            model (str | Unset): Model identifier used to produce the response.
            created_at (datetime.datetime | Unset):
     """

    generation_id: UUID | Unset = UNSET
    project_id: UUID | Unset = UNSET
    prompt: str | Unset = UNSET
    response: str | Unset = UNSET
    tokens_in: int | Unset = UNSET
    tokens_out: int | Unset = UNSET
    model: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        generation_id: str | Unset = UNSET
        if not isinstance(self.generation_id, Unset):
            generation_id = str(self.generation_id)

        project_id: str | Unset = UNSET
        if not isinstance(self.project_id, Unset):
            project_id = str(self.project_id)

        prompt = self.prompt

        response = self.response

        tokens_in = self.tokens_in

        tokens_out = self.tokens_out

        model = self.model

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if generation_id is not UNSET:
            field_dict["generation_id"] = generation_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if prompt is not UNSET:
            field_dict["prompt"] = prompt
        if response is not UNSET:
            field_dict["response"] = response
        if tokens_in is not UNSET:
            field_dict["tokens_in"] = tokens_in
        if tokens_out is not UNSET:
            field_dict["tokens_out"] = tokens_out
        if model is not UNSET:
            field_dict["model"] = model
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

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




        _project_id = d.pop("project_id", UNSET)
        project_id: UUID | Unset
        if isinstance(_project_id,  Unset):
            project_id = UNSET
        else:
            project_id = UUID(_project_id)




        prompt = d.pop("prompt", UNSET)

        response = d.pop("response", UNSET)

        tokens_in = d.pop("tokens_in", UNSET)

        tokens_out = d.pop("tokens_out", UNSET)

        model = d.pop("model", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        studio_generation = cls(
            generation_id=generation_id,
            project_id=project_id,
            prompt=prompt,
            response=response,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            model=model,
            created_at=created_at,
        )


        studio_generation.additional_properties = d
        return studio_generation

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
