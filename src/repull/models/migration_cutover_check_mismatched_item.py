from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.migration_reservation_ref import MigrationReservationRef





T = TypeVar("T", bound="MigrationCutoverCheckMismatchedItem")



@_attrs_define
class MigrationCutoverCheckMismatchedItem:
    """ 
        Attributes:
            source (MigrationReservationRef | Unset):
            destination (MigrationReservationRef | Unset):
     """

    source: MigrationReservationRef | Unset = UNSET
    destination: MigrationReservationRef | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.migration_reservation_ref import MigrationReservationRef
        source: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        destination: dict[str, Any] | Unset = UNSET
        if not isinstance(self.destination, Unset):
            destination = self.destination.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if source is not UNSET:
            field_dict["source"] = source
        if destination is not UNSET:
            field_dict["destination"] = destination

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migration_reservation_ref import MigrationReservationRef
        d = dict(src_dict)
        _source = d.pop("source", UNSET)
        source: MigrationReservationRef | Unset
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = MigrationReservationRef.from_dict(_source)




        _destination = d.pop("destination", UNSET)
        destination: MigrationReservationRef | Unset
        if isinstance(_destination,  Unset):
            destination = UNSET
        else:
            destination = MigrationReservationRef.from_dict(_destination)




        migration_cutover_check_mismatched_item = cls(
            source=source,
            destination=destination,
        )


        migration_cutover_check_mismatched_item.additional_properties = d
        return migration_cutover_check_mismatched_item

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
