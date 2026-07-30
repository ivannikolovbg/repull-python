from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.sandbox_reset_result_deleted import SandboxResetResultDeleted





T = TypeVar("T", bound="SandboxResetResult")



@_attrs_define
class SandboxResetResult:
    """ Result of clearing the sandbox fixture set. Only ever deletes rows in the isolated sandbox data space.

        Attributes:
            customer_id (str):  Example: 1.
            reset_at (datetime.datetime):
            deleted (SandboxResetResultDeleted):
     """

    customer_id: str
    reset_at: datetime.datetime
    deleted: SandboxResetResultDeleted
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sandbox_reset_result_deleted import SandboxResetResultDeleted
        customer_id = self.customer_id

        reset_at = self.reset_at.isoformat()

        deleted = self.deleted.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "customerId": customer_id,
            "resetAt": reset_at,
            "deleted": deleted,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_reset_result_deleted import SandboxResetResultDeleted
        d = dict(src_dict)
        customer_id = d.pop("customerId")

        reset_at = isoparse(d.pop("resetAt"))




        deleted = SandboxResetResultDeleted.from_dict(d.pop("deleted"))




        sandbox_reset_result = cls(
            customer_id=customer_id,
            reset_at=reset_at,
            deleted=deleted,
        )


        sandbox_reset_result.additional_properties = d
        return sandbox_reset_result

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
