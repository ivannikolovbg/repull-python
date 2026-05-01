from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.post_v1_connect_provider_body_access_type import PostV1ConnectProviderBodyAccessType
from ..types import UNSET, Unset






T = TypeVar("T", bound="PostV1ConnectProviderBody")



@_attrs_define
class PostV1ConnectProviderBody:
    """ Provider-specific credentials (apiKey, clientId/clientSecret, etc.) or OAuth init params for Airbnb.

        Attributes:
            redirect_url (str | Unset): Airbnb only — where to redirect the user after the OAuth flow completes.
            access_type (PostV1ConnectProviderBodyAccessType | Unset): Airbnb only — selects the OAuth scope set.
                'read_only' grants calendar-only access; 'full_access' grants full host scopes (default). Default:
                PostV1ConnectProviderBodyAccessType.FULL_ACCESS.
            api_key (str | Unset): PMS providers — API key.
            client_id (str | Unset): Plumguide — client ID.
            client_secret (str | Unset): Plumguide — client secret.
     """

    redirect_url: str | Unset = UNSET
    access_type: PostV1ConnectProviderBodyAccessType | Unset = PostV1ConnectProviderBodyAccessType.FULL_ACCESS
    api_key: str | Unset = UNSET
    client_id: str | Unset = UNSET
    client_secret: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        redirect_url = self.redirect_url

        access_type: str | Unset = UNSET
        if not isinstance(self.access_type, Unset):
            access_type = self.access_type.value


        api_key = self.api_key

        client_id = self.client_id

        client_secret = self.client_secret


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if redirect_url is not UNSET:
            field_dict["redirectUrl"] = redirect_url
        if access_type is not UNSET:
            field_dict["accessType"] = access_type
        if api_key is not UNSET:
            field_dict["apiKey"] = api_key
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if client_secret is not UNSET:
            field_dict["clientSecret"] = client_secret

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        redirect_url = d.pop("redirectUrl", UNSET)

        _access_type = d.pop("accessType", UNSET)
        access_type: PostV1ConnectProviderBodyAccessType | Unset
        if isinstance(_access_type,  Unset):
            access_type = UNSET
        else:
            access_type = PostV1ConnectProviderBodyAccessType(_access_type)




        api_key = d.pop("apiKey", UNSET)

        client_id = d.pop("clientId", UNSET)

        client_secret = d.pop("clientSecret", UNSET)

        post_v1_connect_provider_body = cls(
            redirect_url=redirect_url,
            access_type=access_type,
            api_key=api_key,
            client_id=client_id,
            client_secret=client_secret,
        )


        post_v1_connect_provider_body.additional_properties = d
        return post_v1_connect_provider_body

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
