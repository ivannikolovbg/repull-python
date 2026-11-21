from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.get_vrbo_connection_response_200_data_accounts_item_access_type_type_1 import GetVrboConnectionResponse200DataAccountsItemAccessTypeType1
from ..models.get_vrbo_connection_response_200_data_accounts_item_access_type_type_2_type_1 import GetVrboConnectionResponse200DataAccountsItemAccessTypeType2Type1
from ..models.get_vrbo_connection_response_200_data_accounts_item_access_type_type_3_type_1 import GetVrboConnectionResponse200DataAccountsItemAccessTypeType3Type1
from ..models.get_vrbo_connection_response_200_data_accounts_item_status import GetVrboConnectionResponse200DataAccountsItemStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_vrbo_connection_response_200_data_accounts_item_import_type_0 import GetVrboConnectionResponse200DataAccountsItemImportType0
  from ..models.get_vrbo_connection_response_200_data_accounts_item_sync import GetVrboConnectionResponse200DataAccountsItemSync





T = TypeVar("T", bound="GetVrboConnectionResponse200DataAccountsItem")



@_attrs_define
class GetVrboConnectionResponse200DataAccountsItem:
    """ 
        Attributes:
            account_id (str | Unset):  Example: vrbo:7001234.
            account_name (None | str | Unset):
            status (GetVrboConnectionResponse200DataAccountsItemStatus | Unset):
            session_status (None | str | Unset):
            access_type (GetVrboConnectionResponse200DataAccountsItemAccessTypeType1 |
                GetVrboConnectionResponse200DataAccountsItemAccessTypeType2Type1 |
                GetVrboConnectionResponse200DataAccountsItemAccessTypeType3Type1 | None | Unset):
            linked_units (int | Unset):
            connected_at (None | str | Unset):
            last_synced_at (None | str | Unset):
            sync (GetVrboConnectionResponse200DataAccountsItemSync | Unset):
            import_ (GetVrboConnectionResponse200DataAccountsItemImportType0 | None | Unset): The account's import progress,
                as `GET /v1/connect/vrbo-login` reports it.
            fix_url (str | Unset):
     """

    account_id: str | Unset = UNSET
    account_name: None | str | Unset = UNSET
    status: GetVrboConnectionResponse200DataAccountsItemStatus | Unset = UNSET
    session_status: None | str | Unset = UNSET
    access_type: GetVrboConnectionResponse200DataAccountsItemAccessTypeType1 | GetVrboConnectionResponse200DataAccountsItemAccessTypeType2Type1 | GetVrboConnectionResponse200DataAccountsItemAccessTypeType3Type1 | None | Unset = UNSET
    linked_units: int | Unset = UNSET
    connected_at: None | str | Unset = UNSET
    last_synced_at: None | str | Unset = UNSET
    sync: GetVrboConnectionResponse200DataAccountsItemSync | Unset = UNSET
    import_: GetVrboConnectionResponse200DataAccountsItemImportType0 | None | Unset = UNSET
    fix_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_vrbo_connection_response_200_data_accounts_item_import_type_0 import GetVrboConnectionResponse200DataAccountsItemImportType0
        from ..models.get_vrbo_connection_response_200_data_accounts_item_sync import GetVrboConnectionResponse200DataAccountsItemSync
        account_id = self.account_id

        account_name: None | str | Unset
        if isinstance(self.account_name, Unset):
            account_name = UNSET
        else:
            account_name = self.account_name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        session_status: None | str | Unset
        if isinstance(self.session_status, Unset):
            session_status = UNSET
        else:
            session_status = self.session_status

        access_type: None | str | Unset
        if isinstance(self.access_type, Unset):
            access_type = UNSET
        elif isinstance(self.access_type, GetVrboConnectionResponse200DataAccountsItemAccessTypeType1):
            access_type = self.access_type.value
        elif isinstance(self.access_type, GetVrboConnectionResponse200DataAccountsItemAccessTypeType2Type1):
            access_type = self.access_type.value
        elif isinstance(self.access_type, GetVrboConnectionResponse200DataAccountsItemAccessTypeType3Type1):
            access_type = self.access_type.value
        else:
            access_type = self.access_type

        linked_units = self.linked_units

        connected_at: None | str | Unset
        if isinstance(self.connected_at, Unset):
            connected_at = UNSET
        else:
            connected_at = self.connected_at

        last_synced_at: None | str | Unset
        if isinstance(self.last_synced_at, Unset):
            last_synced_at = UNSET
        else:
            last_synced_at = self.last_synced_at

        sync: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sync, Unset):
            sync = self.sync.to_dict()

        import_: dict[str, Any] | None | Unset
        if isinstance(self.import_, Unset):
            import_ = UNSET
        elif isinstance(self.import_, GetVrboConnectionResponse200DataAccountsItemImportType0):
            import_ = self.import_.to_dict()
        else:
            import_ = self.import_

        fix_url = self.fix_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_name is not UNSET:
            field_dict["accountName"] = account_name
        if status is not UNSET:
            field_dict["status"] = status
        if session_status is not UNSET:
            field_dict["sessionStatus"] = session_status
        if access_type is not UNSET:
            field_dict["accessType"] = access_type
        if linked_units is not UNSET:
            field_dict["linkedUnits"] = linked_units
        if connected_at is not UNSET:
            field_dict["connectedAt"] = connected_at
        if last_synced_at is not UNSET:
            field_dict["lastSyncedAt"] = last_synced_at
        if sync is not UNSET:
            field_dict["sync"] = sync
        if import_ is not UNSET:
            field_dict["import"] = import_
        if fix_url is not UNSET:
            field_dict["fixUrl"] = fix_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_vrbo_connection_response_200_data_accounts_item_import_type_0 import GetVrboConnectionResponse200DataAccountsItemImportType0
        from ..models.get_vrbo_connection_response_200_data_accounts_item_sync import GetVrboConnectionResponse200DataAccountsItemSync
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        def _parse_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        account_name = _parse_account_name(d.pop("accountName", UNSET))


        _status = d.pop("status", UNSET)
        status: GetVrboConnectionResponse200DataAccountsItemStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = GetVrboConnectionResponse200DataAccountsItemStatus(_status)




        def _parse_session_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        session_status = _parse_session_status(d.pop("sessionStatus", UNSET))


        def _parse_access_type(data: object) -> GetVrboConnectionResponse200DataAccountsItemAccessTypeType1 | GetVrboConnectionResponse200DataAccountsItemAccessTypeType2Type1 | GetVrboConnectionResponse200DataAccountsItemAccessTypeType3Type1 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_type_type_1 = GetVrboConnectionResponse200DataAccountsItemAccessTypeType1(data)



                return access_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_type_type_2_type_1 = GetVrboConnectionResponse200DataAccountsItemAccessTypeType2Type1(data)



                return access_type_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_type_type_3_type_1 = GetVrboConnectionResponse200DataAccountsItemAccessTypeType3Type1(data)



                return access_type_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboConnectionResponse200DataAccountsItemAccessTypeType1 | GetVrboConnectionResponse200DataAccountsItemAccessTypeType2Type1 | GetVrboConnectionResponse200DataAccountsItemAccessTypeType3Type1 | None | Unset, data)

        access_type = _parse_access_type(d.pop("accessType", UNSET))


        linked_units = d.pop("linkedUnits", UNSET)

        def _parse_connected_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connected_at = _parse_connected_at(d.pop("connectedAt", UNSET))


        def _parse_last_synced_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_synced_at = _parse_last_synced_at(d.pop("lastSyncedAt", UNSET))


        _sync = d.pop("sync", UNSET)
        sync: GetVrboConnectionResponse200DataAccountsItemSync | Unset
        if isinstance(_sync,  Unset):
            sync = UNSET
        else:
            sync = GetVrboConnectionResponse200DataAccountsItemSync.from_dict(_sync)




        def _parse_import_(data: object) -> GetVrboConnectionResponse200DataAccountsItemImportType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                import_type_0 = GetVrboConnectionResponse200DataAccountsItemImportType0.from_dict(data)



                return import_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(GetVrboConnectionResponse200DataAccountsItemImportType0 | None | Unset, data)

        import_ = _parse_import_(d.pop("import", UNSET))


        fix_url = d.pop("fixUrl", UNSET)

        get_vrbo_connection_response_200_data_accounts_item = cls(
            account_id=account_id,
            account_name=account_name,
            status=status,
            session_status=session_status,
            access_type=access_type,
            linked_units=linked_units,
            connected_at=connected_at,
            last_synced_at=last_synced_at,
            sync=sync,
            import_=import_,
            fix_url=fix_url,
        )


        get_vrbo_connection_response_200_data_accounts_item.additional_properties = d
        return get_vrbo_connection_response_200_data_accounts_item

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
