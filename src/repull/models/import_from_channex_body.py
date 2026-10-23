from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.import_from_channex_body_environment import ImportFromChannexBodyEnvironment
from ..types import UNSET, Unset






T = TypeVar("T", bound="ImportFromChannexBody")



@_attrs_define
class ImportFromChannexBody:
    """ 
        Attributes:
            api_key (str): Your Channex API key (the `user-api-key` header value). Used for this request only.
            environment (ImportFromChannexBodyEnvironment | Unset): `production` reads app.channex.io, `staging` reads
                staging.channex.io. Default: ImportFromChannexBodyEnvironment.PRODUCTION.
            dry_run (bool | Unset): Match and report without writing anything. Default: False.
     """

    api_key: str
    environment: ImportFromChannexBodyEnvironment | Unset = ImportFromChannexBodyEnvironment.PRODUCTION
    dry_run: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        environment: str | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.value


        dry_run = self.dry_run


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "apiKey": api_key,
        })
        if environment is not UNSET:
            field_dict["environment"] = environment
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        _environment = d.pop("environment", UNSET)
        environment: ImportFromChannexBodyEnvironment | Unset
        if isinstance(_environment,  Unset):
            environment = UNSET
        else:
            environment = ImportFromChannexBodyEnvironment(_environment)




        dry_run = d.pop("dryRun", UNSET)

        import_from_channex_body = cls(
            api_key=api_key,
            environment=environment,
            dry_run=dry_run,
        )


        import_from_channex_body.additional_properties = d
        return import_from_channex_body

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
