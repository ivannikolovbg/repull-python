from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.check_migration_cutover_body_reservations_item import CheckMigrationCutoverBodyReservationsItem





T = TypeVar("T", bound="CheckMigrationCutoverBody")



@_attrs_define
class CheckMigrationCutoverBody:
    """ 
        Attributes:
            reservations (list[CheckMigrationCutoverBodyReservationsItem]):
     """

    reservations: list[CheckMigrationCutoverBodyReservationsItem]





    def to_dict(self) -> dict[str, Any]:
        from ..models.check_migration_cutover_body_reservations_item import CheckMigrationCutoverBodyReservationsItem
        reservations = []
        for reservations_item_data in self.reservations:
            reservations_item = reservations_item_data.to_dict()
            reservations.append(reservations_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "reservations": reservations,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_migration_cutover_body_reservations_item import CheckMigrationCutoverBodyReservationsItem
        d = dict(src_dict)
        reservations = []
        _reservations = d.pop("reservations")
        for reservations_item_data in (_reservations):
            reservations_item = CheckMigrationCutoverBodyReservationsItem.from_dict(reservations_item_data)



            reservations.append(reservations_item)


        check_migration_cutover_body = cls(
            reservations=reservations,
        )

        return check_migration_cutover_body

