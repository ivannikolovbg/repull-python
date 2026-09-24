from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="CheckMigrationCutoverBodyReservationsItem")



@_attrs_define
class CheckMigrationCutoverBodyReservationsItem:
    """ 
        Attributes:
            confirmation_code (str):
            check_in (datetime.date):
            check_out (datetime.date):
     """

    confirmation_code: str
    check_in: datetime.date
    check_out: datetime.date





    def to_dict(self) -> dict[str, Any]:
        confirmation_code = self.confirmation_code

        check_in = self.check_in.isoformat()

        check_out = self.check_out.isoformat()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "confirmationCode": confirmation_code,
            "checkIn": check_in,
            "checkOut": check_out,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        confirmation_code = d.pop("confirmationCode")

        check_in = isoparse(d.pop("checkIn")).date()




        check_out = isoparse(d.pop("checkOut")).date()




        check_migration_cutover_body_reservations_item = cls(
            confirmation_code=confirmation_code,
            check_in=check_in,
            check_out=check_out,
        )

        return check_migration_cutover_body_reservations_item

