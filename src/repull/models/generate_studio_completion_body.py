from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="GenerateStudioCompletionBody")



@_attrs_define
class GenerateStudioCompletionBody:
    """ 
        Attributes:
            project_id (int | str): Project the generation belongs to (used for billing + rate limits).
            prompt (str): User prompt. Up to 32,000 characters.
            system_prompt (str | Unset): Optional system prompt to steer the response.
            temperature (float | Unset): Sampling temperature. Defaults to model preset.
            max_tokens (int | Unset): Maximum completion tokens.
     """

    project_id: int | str
    prompt: str
    system_prompt: str | Unset = UNSET
    temperature: float | Unset = UNSET
    max_tokens: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        project_id: int | str
        project_id = self.project_id

        prompt = self.prompt

        system_prompt = self.system_prompt

        temperature = self.temperature

        max_tokens = self.max_tokens


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "project_id": project_id,
            "prompt": prompt,
        })
        if system_prompt is not UNSET:
            field_dict["system_prompt"] = system_prompt
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if max_tokens is not UNSET:
            field_dict["max_tokens"] = max_tokens

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_project_id(data: object) -> int | str:
            return cast(int | str, data)

        project_id = _parse_project_id(d.pop("project_id"))


        prompt = d.pop("prompt")

        system_prompt = d.pop("system_prompt", UNSET)

        temperature = d.pop("temperature", UNSET)

        max_tokens = d.pop("max_tokens", UNSET)

        generate_studio_completion_body = cls(
            project_id=project_id,
            prompt=prompt,
            system_prompt=system_prompt,
            temperature=temperature,
            max_tokens=max_tokens,
        )


        generate_studio_completion_body.additional_properties = d
        return generate_studio_completion_body

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
