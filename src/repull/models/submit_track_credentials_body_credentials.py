from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.submit_track_credentials_body_credentials_auth_mode import SubmitTrackCredentialsBodyCredentialsAuthMode
from ..models.submit_track_credentials_body_credentials_key_type import SubmitTrackCredentialsBodyCredentialsKeyType
from ..types import UNSET, Unset






T = TypeVar("T", bound="SubmitTrackCredentialsBodyCredentials")



@_attrs_define
class SubmitTrackCredentialsBodyCredentials:
    """ The Track domain and an API key + secret.

        Attributes:
            domain (str): Your Track domain: `acme.trackhs.com`, or just the subdomain `acme`. A full URL is accepted; only
                the host is kept. Example: acme.trackhs.com.
            api_key (str): Track API key.
            api_secret (str): Track API secret, shown next to the key in Track.
            key_type (SubmitTrackCredentialsBodyCredentialsKeyType | Unset): `server` — a Server Key (Company Setup → API
                Keys), full access, recommended. `channel` — a Channel Key (PMS Setup → Distribution Channels), booking only.
                Default: SubmitTrackCredentialsBodyCredentialsKeyType.SERVER.
            auth_mode (SubmitTrackCredentialsBodyCredentialsAuthMode | Unset): How requests to Track are signed. Leave the
                default unless Track support told you otherwise. Default: SubmitTrackCredentialsBodyCredentialsAuthMode.HMAC.
            hmac_realm (str | Unset): HMAC realm. Defaults to `Acquia`, the realm Track's HMAC signing uses.
            secret_is_base_64 (bool | Unset): Whether `apiSecret` is base64-encoded, as Track issues it. Set false to sign
                with the secret's raw text. Default: True.
            payment_type_id (int | Unset): The Track payment type that payments recorded through this connection are posted
                to.
            move_reason_id (int | Unset): The Track move reason used when a reservation is moved to another unit. Without
                it, unit changes are refused.
     """

    domain: str
    api_key: str
    api_secret: str
    key_type: SubmitTrackCredentialsBodyCredentialsKeyType | Unset = SubmitTrackCredentialsBodyCredentialsKeyType.SERVER
    auth_mode: SubmitTrackCredentialsBodyCredentialsAuthMode | Unset = SubmitTrackCredentialsBodyCredentialsAuthMode.HMAC
    hmac_realm: str | Unset = UNSET
    secret_is_base_64: bool | Unset = True
    payment_type_id: int | Unset = UNSET
    move_reason_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        domain = self.domain

        api_key = self.api_key

        api_secret = self.api_secret

        key_type: str | Unset = UNSET
        if not isinstance(self.key_type, Unset):
            key_type = self.key_type.value


        auth_mode: str | Unset = UNSET
        if not isinstance(self.auth_mode, Unset):
            auth_mode = self.auth_mode.value


        hmac_realm = self.hmac_realm

        secret_is_base_64 = self.secret_is_base_64

        payment_type_id = self.payment_type_id

        move_reason_id = self.move_reason_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "domain": domain,
            "apiKey": api_key,
            "apiSecret": api_secret,
        })
        if key_type is not UNSET:
            field_dict["keyType"] = key_type
        if auth_mode is not UNSET:
            field_dict["authMode"] = auth_mode
        if hmac_realm is not UNSET:
            field_dict["hmacRealm"] = hmac_realm
        if secret_is_base_64 is not UNSET:
            field_dict["secretIsBase64"] = secret_is_base_64
        if payment_type_id is not UNSET:
            field_dict["paymentTypeId"] = payment_type_id
        if move_reason_id is not UNSET:
            field_dict["moveReasonId"] = move_reason_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        domain = d.pop("domain")

        api_key = d.pop("apiKey")

        api_secret = d.pop("apiSecret")

        _key_type = d.pop("keyType", UNSET)
        key_type: SubmitTrackCredentialsBodyCredentialsKeyType | Unset
        if isinstance(_key_type,  Unset):
            key_type = UNSET
        else:
            key_type = SubmitTrackCredentialsBodyCredentialsKeyType(_key_type)




        _auth_mode = d.pop("authMode", UNSET)
        auth_mode: SubmitTrackCredentialsBodyCredentialsAuthMode | Unset
        if isinstance(_auth_mode,  Unset):
            auth_mode = UNSET
        else:
            auth_mode = SubmitTrackCredentialsBodyCredentialsAuthMode(_auth_mode)




        hmac_realm = d.pop("hmacRealm", UNSET)

        secret_is_base_64 = d.pop("secretIsBase64", UNSET)

        payment_type_id = d.pop("paymentTypeId", UNSET)

        move_reason_id = d.pop("moveReasonId", UNSET)

        submit_track_credentials_body_credentials = cls(
            domain=domain,
            api_key=api_key,
            api_secret=api_secret,
            key_type=key_type,
            auth_mode=auth_mode,
            hmac_realm=hmac_realm,
            secret_is_base_64=secret_is_base_64,
            payment_type_id=payment_type_id,
            move_reason_id=move_reason_id,
        )


        submit_track_credentials_body_credentials.additional_properties = d
        return submit_track_credentials_body_credentials

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
