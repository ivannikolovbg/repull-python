from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_vrbo_alteration_response_201_data_payment_type_0_lines_item import CreateVrboAlterationResponse201DataPaymentType0LinesItem
  from ..models.create_vrbo_alteration_response_201_data_payment_type_0_total import CreateVrboAlterationResponse201DataPaymentType0Total





T = TypeVar("T", bound="CreateVrboAlterationResponse201DataPaymentType0")



@_attrs_define
class CreateVrboAlterationResponse201DataPaymentType0:
    """ 
        Attributes:
            title (None | str | Unset):
            lines (list[CreateVrboAlterationResponse201DataPaymentType0LinesItem] | Unset):
            total (CreateVrboAlterationResponse201DataPaymentType0Total | Unset):
     """

    title: None | str | Unset = UNSET
    lines: list[CreateVrboAlterationResponse201DataPaymentType0LinesItem] | Unset = UNSET
    total: CreateVrboAlterationResponse201DataPaymentType0Total | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_vrbo_alteration_response_201_data_payment_type_0_lines_item import CreateVrboAlterationResponse201DataPaymentType0LinesItem
        from ..models.create_vrbo_alteration_response_201_data_payment_type_0_total import CreateVrboAlterationResponse201DataPaymentType0Total
        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        lines: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)



        total: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total, Unset):
            total = self.total.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if title is not UNSET:
            field_dict["title"] = title
        if lines is not UNSET:
            field_dict["lines"] = lines
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_vrbo_alteration_response_201_data_payment_type_0_lines_item import CreateVrboAlterationResponse201DataPaymentType0LinesItem
        from ..models.create_vrbo_alteration_response_201_data_payment_type_0_total import CreateVrboAlterationResponse201DataPaymentType0Total
        d = dict(src_dict)
        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        _lines = d.pop("lines", UNSET)
        lines: list[CreateVrboAlterationResponse201DataPaymentType0LinesItem] | Unset = UNSET
        if _lines is not UNSET:
            lines = []
            for lines_item_data in _lines:
                lines_item = CreateVrboAlterationResponse201DataPaymentType0LinesItem.from_dict(lines_item_data)



                lines.append(lines_item)


        _total = d.pop("total", UNSET)
        total: CreateVrboAlterationResponse201DataPaymentType0Total | Unset
        if isinstance(_total,  Unset):
            total = UNSET
        else:
            total = CreateVrboAlterationResponse201DataPaymentType0Total.from_dict(_total)




        create_vrbo_alteration_response_201_data_payment_type_0 = cls(
            title=title,
            lines=lines,
            total=total,
        )


        create_vrbo_alteration_response_201_data_payment_type_0.additional_properties = d
        return create_vrbo_alteration_response_201_data_payment_type_0

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
