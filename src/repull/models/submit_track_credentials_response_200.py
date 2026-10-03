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
  from ..models.submit_track_credentials_response_200_account_info import SubmitTrackCredentialsResponse200AccountInfo
  from ..models.submit_track_credentials_response_200_first_sync import SubmitTrackCredentialsResponse200FirstSync





T = TypeVar("T", bound="SubmitTrackCredentialsResponse200")



@_attrs_define
class SubmitTrackCredentialsResponse200:
    """ 
        Attributes:
            provider (str | Unset):  Example: track.
            connected (bool | Unset):
            pms_connection_id (str | Unset): Id of the stored connection.
            created (bool | Unset): False when an existing connection was updated.
            session_id (None | str | Unset):
            account_info (SubmitTrackCredentialsResponse200AccountInfo | Unset):
            first_sync (SubmitTrackCredentialsResponse200FirstSync | Unset): Whether the first import of listings and
                reservations was queued. When it was not, the connection still stands and polling syncs it.
            write_policy (PmsWritePolicy | Unset): What the app may change in a connected PMS. Hotel PMSs (Cloudbeds, Mews)
                start with every `calendar` switch off, because the PMS owns its room inventory; every other PMS starts with
                everything on. Reading from the PMS is never affected. Example: {'calendar': {'availability': False, 'rates':
                True, 'restrictions': False}, 'reservations': {'website': True, 'dashboard': True, 'api': True}}.
     """

    provider: str | Unset = UNSET
    connected: bool | Unset = UNSET
    pms_connection_id: str | Unset = UNSET
    created: bool | Unset = UNSET
    session_id: None | str | Unset = UNSET
    account_info: SubmitTrackCredentialsResponse200AccountInfo | Unset = UNSET
    first_sync: SubmitTrackCredentialsResponse200FirstSync | Unset = UNSET
    write_policy: PmsWritePolicy | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.pms_write_policy import PmsWritePolicy
        from ..models.submit_track_credentials_response_200_account_info import SubmitTrackCredentialsResponse200AccountInfo
        from ..models.submit_track_credentials_response_200_first_sync import SubmitTrackCredentialsResponse200FirstSync
        provider = self.provider

        connected = self.connected

        pms_connection_id = self.pms_connection_id

        created = self.created

        session_id: None | str | Unset
        if isinstance(self.session_id, Unset):
            session_id = UNSET
        else:
            session_id = self.session_id

        account_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_info, Unset):
            account_info = self.account_info.to_dict()

        first_sync: dict[str, Any] | Unset = UNSET
        if not isinstance(self.first_sync, Unset):
            first_sync = self.first_sync.to_dict()

        write_policy: dict[str, Any] | Unset = UNSET
        if not isinstance(self.write_policy, Unset):
            write_policy = self.write_policy.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if provider is not UNSET:
            field_dict["provider"] = provider
        if connected is not UNSET:
            field_dict["connected"] = connected
        if pms_connection_id is not UNSET:
            field_dict["pmsConnectionId"] = pms_connection_id
        if created is not UNSET:
            field_dict["created"] = created
        if session_id is not UNSET:
            field_dict["sessionId"] = session_id
        if account_info is not UNSET:
            field_dict["accountInfo"] = account_info
        if first_sync is not UNSET:
            field_dict["firstSync"] = first_sync
        if write_policy is not UNSET:
            field_dict["writePolicy"] = write_policy

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pms_write_policy import PmsWritePolicy
        from ..models.submit_track_credentials_response_200_account_info import SubmitTrackCredentialsResponse200AccountInfo
        from ..models.submit_track_credentials_response_200_first_sync import SubmitTrackCredentialsResponse200FirstSync
        d = dict(src_dict)
        provider = d.pop("provider", UNSET)

        connected = d.pop("connected", UNSET)

        pms_connection_id = d.pop("pmsConnectionId", UNSET)

        created = d.pop("created", UNSET)

        def _parse_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_id = _parse_session_id(d.pop("sessionId", UNSET))


        _account_info = d.pop("accountInfo", UNSET)
        account_info: SubmitTrackCredentialsResponse200AccountInfo | Unset
        if isinstance(_account_info,  Unset):
            account_info = UNSET
        else:
            account_info = SubmitTrackCredentialsResponse200AccountInfo.from_dict(_account_info)




        _first_sync = d.pop("firstSync", UNSET)
        first_sync: SubmitTrackCredentialsResponse200FirstSync | Unset
        if isinstance(_first_sync,  Unset):
            first_sync = UNSET
        else:
            first_sync = SubmitTrackCredentialsResponse200FirstSync.from_dict(_first_sync)




        _write_policy = d.pop("writePolicy", UNSET)
        write_policy: PmsWritePolicy | Unset
        if isinstance(_write_policy,  Unset):
            write_policy = UNSET
        else:
            write_policy = PmsWritePolicy.from_dict(_write_policy)




        submit_track_credentials_response_200 = cls(
            provider=provider,
            connected=connected,
            pms_connection_id=pms_connection_id,
            created=created,
            session_id=session_id,
            account_info=account_info,
            first_sync=first_sync,
            write_policy=write_policy,
        )


        submit_track_credentials_response_200.additional_properties = d
        return submit_track_credentials_response_200

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
