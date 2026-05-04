from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="GenerateStudioCompletionResponse200Data")



@_attrs_define
class GenerateStudioCompletionResponse200Data:
    """ 
        Attributes:
            text (str | Unset): Generated completion text.
            generation_id (UUID | Unset):
            model (str | Unset): Model identifier that produced the response.
            tokens_in (int | Unset):
            tokens_out (int | Unset):
            latency_ms (int | Unset):
            cost_usd_micro (int | Unset): Cost in millionths of a USD.
            cached (bool | Unset): True if the response was served from cache.
            fallback (bool | Unset): True if the primary model failed and Repull AI fell back to the secondary.
     """

    text: str | Unset = UNSET
    generation_id: UUID | Unset = UNSET
    model: str | Unset = UNSET
    tokens_in: int | Unset = UNSET
    tokens_out: int | Unset = UNSET
    latency_ms: int | Unset = UNSET
    cost_usd_micro: int | Unset = UNSET
    cached: bool | Unset = UNSET
    fallback: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        text = self.text

        generation_id: str | Unset = UNSET
        if not isinstance(self.generation_id, Unset):
            generation_id = str(self.generation_id)

        model = self.model

        tokens_in = self.tokens_in

        tokens_out = self.tokens_out

        latency_ms = self.latency_ms

        cost_usd_micro = self.cost_usd_micro

        cached = self.cached

        fallback = self.fallback


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if text is not UNSET:
            field_dict["text"] = text
        if generation_id is not UNSET:
            field_dict["generation_id"] = generation_id
        if model is not UNSET:
            field_dict["model"] = model
        if tokens_in is not UNSET:
            field_dict["tokens_in"] = tokens_in
        if tokens_out is not UNSET:
            field_dict["tokens_out"] = tokens_out
        if latency_ms is not UNSET:
            field_dict["latency_ms"] = latency_ms
        if cost_usd_micro is not UNSET:
            field_dict["cost_usd_micro"] = cost_usd_micro
        if cached is not UNSET:
            field_dict["cached"] = cached
        if fallback is not UNSET:
            field_dict["fallback"] = fallback

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text", UNSET)

        _generation_id = d.pop("generation_id", UNSET)
        generation_id: UUID | Unset
        if isinstance(_generation_id,  Unset):
            generation_id = UNSET
        else:
            generation_id = UUID(_generation_id)




        model = d.pop("model", UNSET)

        tokens_in = d.pop("tokens_in", UNSET)

        tokens_out = d.pop("tokens_out", UNSET)

        latency_ms = d.pop("latency_ms", UNSET)

        cost_usd_micro = d.pop("cost_usd_micro", UNSET)

        cached = d.pop("cached", UNSET)

        fallback = d.pop("fallback", UNSET)

        generate_studio_completion_response_200_data = cls(
            text=text,
            generation_id=generation_id,
            model=model,
            tokens_in=tokens_in,
            tokens_out=tokens_out,
            latency_ms=latency_ms,
            cost_usd_micro=cost_usd_micro,
            cached=cached,
            fallback=fallback,
        )


        generate_studio_completion_response_200_data.additional_properties = d
        return generate_studio_completion_response_200_data

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
