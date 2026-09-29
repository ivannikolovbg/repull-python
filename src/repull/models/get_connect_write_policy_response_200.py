from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.pms_write_policy import PmsWritePolicy





T = TypeVar("T", bound="GetConnectWritePolicyResponse200")



@_attrs_define
class GetConnectWritePolicyResponse200:
    """ 
        Attributes:
            provider (str | Unset):  Example: cloudbeds.
            write_policy (PmsWritePolicy | Unset): What the app may change in a connected PMS. Hotel PMSs (Cloudbeds, Mews)
                start with every `calendar` switch off, because the PMS owns its room inventory; every other PMS starts with
                everything on. Reading from the PMS is never affected. Example: {'calendar': {'availability': False, 'rates':
                True, 'restrictions': False}, 'reservations': {'website': True, 'dashboard': True, 'api': True}}.
            defaults (PmsWritePolicy | Unset): What the app may change in a connected PMS. Hotel PMSs (Cloudbeds, Mews)
                start with every `calendar` switch off, because the PMS owns its room inventory; every other PMS starts with
                everything on. Reading from the PMS is never affected. Example: {'calendar': {'availability': False, 'rates':
                True, 'restrictions': False}, 'reservations': {'website': True, 'dashboard': True, 'api': True}}.
     """

    provider: str | Unset = UNSET
    write_policy: PmsWritePolicy | Unset = UNSET
    defaults: PmsWritePolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.pms_write_policy import PmsWritePolicy
        provider = self.provider

        write_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.write_policy, Unset):
            write_policy = self.write_policy.to_dict()

        defaults: dict[str, Any] | Unset = UNSET
        if not isinstance(self.defaults, Unset):
            defaults = self.defaults.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if provider is not UNSET:
            field_dict["provider"] = provider
        if write_policy is not UNSET:
            field_dict["writePolicy"] = write_policy
        if defaults is not UNSET:
            field_dict["defaults"] = defaults

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pms_write_policy import PmsWritePolicy
        d = dict(src_dict)
        provider = d.pop("provider", UNSET)

        _write_policy = d.pop("writePolicy", UNSET)
        write_policy: PmsWritePolicy | Unset
        if isinstance(_write_policy,  Unset):
            write_policy = UNSET
        else:
            write_policy = PmsWritePolicy.from_dict(_write_policy)




        _defaults = d.pop("defaults", UNSET)
        defaults: PmsWritePolicy | Unset
        if isinstance(_defaults,  Unset):
            defaults = UNSET
        else:
            defaults = PmsWritePolicy.from_dict(_defaults)




        get_connect_write_policy_response_200 = cls(
            provider=provider,
            write_policy=write_policy,
            defaults=defaults,
        )


        get_connect_write_policy_response_200.additional_properties = d
        return get_connect_write_policy_response_200

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
