from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connection_access_type import ConnectionAccessType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.vrbo_import_status import VrboImportStatus





T = TypeVar("T", bound="ConnectStatusAccountsItem")



@_attrs_define
class ConnectStatusAccountsItem:
    """ 
        Attributes:
            external_account_id (None | str | Unset): Airbnb: the host id, as a string (it can exceed 2^53). Vrbo: Vrbo's
                own account id; `null` until it is captured at sign-in. Example: 79730216.
            connection_id (None | str | Unset): Our connection record (`X-Account-Id`). Airbnb: the workspace's Airbnb
                connection. Vrbo: the workspace's Vrbo connection, `null` when it has none. Example: 135.
            name (None | str | Unset):  Example: Casey.
            picture_url (None | str | Unset):
            status (None | str | Unset):  Example: active.
            connected (bool | Unset): True while the account is active and its authorization is usable. Example: True.
            email (None | str | Unset): Vrbo only: the account email.
            access_type (ConnectionAccessType | None | Unset): What this account may do. Airbnb: the tier the host's token
                was granted with (`read_only`, `messaging`, `full_access`). Vrbo: `messaging` (bookings and messages, no
                calendar push) or `full_access` (also pushes prices and availability). `null` when unknown.
            notification_email (None | str | Unset): Vrbo only. The address the host can add on Vrbo as a secondary email
                (with message and reservation notifications on) so new bookings, inquiries and messages arrive within a minute
                instead of at the scheduled check. Ask every host to add it: notifications are how Vrbo updates reach Repull,
                the scheduled check is the backup. Hosted Connect shows it on its mapping screen; show it in your own app when
                you create sessions with `mapping: "api"`.
            import_ (None | Unset | VrboImportStatus): Vrbo only: where the account import stands.
     """

    external_account_id: None | str | Unset = UNSET
    connection_id: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    picture_url: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    connected: bool | Unset = UNSET
    email: None | str | Unset = UNSET
    access_type: ConnectionAccessType | None | Unset = UNSET
    notification_email: None | str | Unset = UNSET
    import_: None | Unset | VrboImportStatus = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.vrbo_import_status import VrboImportStatus
        external_account_id: None | str | Unset
        if isinstance(self.external_account_id, Unset):
            external_account_id = UNSET
        else:
            external_account_id = self.external_account_id

        connection_id: None | str | Unset
        if isinstance(self.connection_id, Unset):
            connection_id = UNSET
        else:
            connection_id = self.connection_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        picture_url: None | str | Unset
        if isinstance(self.picture_url, Unset):
            picture_url = UNSET
        else:
            picture_url = self.picture_url

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        connected = self.connected

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        access_type: None | str | Unset
        if isinstance(self.access_type, Unset):
            access_type = UNSET
        elif isinstance(self.access_type, ConnectionAccessType):
            access_type = self.access_type.value
        else:
            access_type = self.access_type

        notification_email: None | str | Unset
        if isinstance(self.notification_email, Unset):
            notification_email = UNSET
        else:
            notification_email = self.notification_email

        import_: dict[str, Any] | None | Unset
        if isinstance(self.import_, Unset):
            import_ = UNSET
        elif isinstance(self.import_, VrboImportStatus):
            import_ = self.import_.to_dict()
        else:
            import_ = self.import_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if external_account_id is not UNSET:
            field_dict["externalAccountId"] = external_account_id
        if connection_id is not UNSET:
            field_dict["connectionId"] = connection_id
        if name is not UNSET:
            field_dict["name"] = name
        if picture_url is not UNSET:
            field_dict["pictureUrl"] = picture_url
        if status is not UNSET:
            field_dict["status"] = status
        if connected is not UNSET:
            field_dict["connected"] = connected
        if email is not UNSET:
            field_dict["email"] = email
        if access_type is not UNSET:
            field_dict["accessType"] = access_type
        if notification_email is not UNSET:
            field_dict["notificationEmail"] = notification_email
        if import_ is not UNSET:
            field_dict["import"] = import_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vrbo_import_status import VrboImportStatus
        d = dict(src_dict)
        def _parse_external_account_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        external_account_id = _parse_external_account_id(d.pop("externalAccountId", UNSET))


        def _parse_connection_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        connection_id = _parse_connection_id(d.pop("connectionId", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_picture_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        picture_url = _parse_picture_url(d.pop("pictureUrl", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        connected = d.pop("connected", UNSET)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_access_type(data: object) -> ConnectionAccessType | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                access_type_type_1 = ConnectionAccessType(data)



                return access_type_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectionAccessType | None | Unset, data)

        access_type = _parse_access_type(d.pop("accessType", UNSET))


        def _parse_notification_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notification_email = _parse_notification_email(d.pop("notificationEmail", UNSET))


        def _parse_import_(data: object) -> None | Unset | VrboImportStatus:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                import_type_1 = VrboImportStatus.from_dict(data)



                return import_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | VrboImportStatus, data)

        import_ = _parse_import_(d.pop("import", UNSET))


        connect_status_accounts_item = cls(
            external_account_id=external_account_id,
            connection_id=connection_id,
            name=name,
            picture_url=picture_url,
            status=status,
            connected=connected,
            email=email,
            access_type=access_type,
            notification_email=notification_email,
            import_=import_,
        )


        connect_status_accounts_item.additional_properties = d
        return connect_status_accounts_item

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
