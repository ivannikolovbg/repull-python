from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_billing_response_200_limits import GetBillingResponse200Limits
  from ..models.get_billing_response_200_used import GetBillingResponse200Used





T = TypeVar("T", bound="GetBillingResponse200")



@_attrs_define
class GetBillingResponse200:
    """ 
        Attributes:
            plan (str | Unset):  Example: starter.
            limits (GetBillingResponse200Limits | Unset):
            used (GetBillingResponse200Used | Unset):
            resets_at (datetime.datetime | Unset):
            manage_url (str | Unset):  Example: https://repull.dev/dashboard/settings.
     """

    plan: str | Unset = UNSET
    limits: GetBillingResponse200Limits | Unset = UNSET
    used: GetBillingResponse200Used | Unset = UNSET
    resets_at: datetime.datetime | Unset = UNSET
    manage_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_billing_response_200_limits import GetBillingResponse200Limits
        from ..models.get_billing_response_200_used import GetBillingResponse200Used
        plan = self.plan

        limits: dict[str, Any] | Unset = UNSET
        if not isinstance(self.limits, Unset):
            limits = self.limits.to_dict()

        used: dict[str, Any] | Unset = UNSET
        if not isinstance(self.used, Unset):
            used = self.used.to_dict()

        resets_at: str | Unset = UNSET
        if not isinstance(self.resets_at, Unset):
            resets_at = self.resets_at.isoformat()

        manage_url = self.manage_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if plan is not UNSET:
            field_dict["plan"] = plan
        if limits is not UNSET:
            field_dict["limits"] = limits
        if used is not UNSET:
            field_dict["used"] = used
        if resets_at is not UNSET:
            field_dict["resetsAt"] = resets_at
        if manage_url is not UNSET:
            field_dict["manageUrl"] = manage_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_billing_response_200_limits import GetBillingResponse200Limits
        from ..models.get_billing_response_200_used import GetBillingResponse200Used
        d = dict(src_dict)
        plan = d.pop("plan", UNSET)

        _limits = d.pop("limits", UNSET)
        limits: GetBillingResponse200Limits | Unset
        if isinstance(_limits,  Unset):
            limits = UNSET
        else:
            limits = GetBillingResponse200Limits.from_dict(_limits)




        _used = d.pop("used", UNSET)
        used: GetBillingResponse200Used | Unset
        if isinstance(_used,  Unset):
            used = UNSET
        else:
            used = GetBillingResponse200Used.from_dict(_used)




        _resets_at = d.pop("resetsAt", UNSET)
        resets_at: datetime.datetime | Unset
        if isinstance(_resets_at,  Unset):
            resets_at = UNSET
        else:
            resets_at = isoparse(_resets_at)




        manage_url = d.pop("manageUrl", UNSET)

        get_billing_response_200 = cls(
            plan=plan,
            limits=limits,
            used=used,
            resets_at=resets_at,
            manage_url=manage_url,
        )


        get_billing_response_200.additional_properties = d
        return get_billing_response_200

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
