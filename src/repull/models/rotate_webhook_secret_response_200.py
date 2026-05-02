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






T = TypeVar("T", bound="RotateWebhookSecretResponse200")



@_attrs_define
class RotateWebhookSecretResponse200:
    """ 
        Attributes:
            id (str | Unset):
            secret (str | Unset):
            rotated_at (datetime.datetime | Unset):
     """

    id: str | Unset = UNSET
    secret: str | Unset = UNSET
    rotated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        secret = self.secret

        rotated_at: str | Unset = UNSET
        if not isinstance(self.rotated_at, Unset):
            rotated_at = self.rotated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if secret is not UNSET:
            field_dict["secret"] = secret
        if rotated_at is not UNSET:
            field_dict["rotatedAt"] = rotated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        secret = d.pop("secret", UNSET)

        _rotated_at = d.pop("rotatedAt", UNSET)
        rotated_at: datetime.datetime | Unset
        if isinstance(_rotated_at,  Unset):
            rotated_at = UNSET
        else:
            rotated_at = isoparse(_rotated_at)




        rotate_webhook_secret_response_200 = cls(
            id=id,
            secret=secret,
            rotated_at=rotated_at,
        )


        rotate_webhook_secret_response_200.additional_properties = d
        return rotate_webhook_secret_response_200

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
