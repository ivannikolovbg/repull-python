from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_connection_summary_status import AirbnbConnectionSummaryStatus
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_connection_host import AirbnbConnectionHost





T = TypeVar("T", bound="AirbnbConnectionSummary")



@_attrs_define
class AirbnbConnectionSummary:
    """ Workspace-level Airbnb connection state. The dedicated answer to "is my Airbnb still connected?" — emit one summary
    instead of inferring from per-listing 401s.

        Attributes:
            status (AirbnbConnectionSummaryStatus): `connected` — every host is currently connected. `reconnect_required` —
                at least one host is connected, at least one is not. `disconnected` — every host has been disconnected.
                `never_connected` — the workspace has never linked an Airbnb account.
            host_count (int):  Example: 2.
            hosts (list[AirbnbConnectionHost]):
            fix_url (None | str | Unset): Self-serve recovery URL. Set whenever `status` is anything other than `connected`.
                Points at the dashboard surface where the host re-authorizes (or initiates the first OAuth flow for
                `never_connected` workspaces). Example: https://repull.dev/dashboard/connections/airbnb.
     """

    status: AirbnbConnectionSummaryStatus
    host_count: int
    hosts: list[AirbnbConnectionHost]
    fix_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_connection_host import AirbnbConnectionHost
        status = self.status.value

        host_count = self.host_count

        hosts = []
        for hosts_item_data in self.hosts:
            hosts_item = hosts_item_data.to_dict()
            hosts.append(hosts_item)



        fix_url: None | str | Unset
        if isinstance(self.fix_url, Unset):
            fix_url = UNSET
        else:
            fix_url = self.fix_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "hostCount": host_count,
            "hosts": hosts,
        })
        if fix_url is not UNSET:
            field_dict["fixUrl"] = fix_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_connection_host import AirbnbConnectionHost
        d = dict(src_dict)
        status = AirbnbConnectionSummaryStatus(d.pop("status"))




        host_count = d.pop("hostCount")

        hosts = []
        _hosts = d.pop("hosts")
        for hosts_item_data in (_hosts):
            hosts_item = AirbnbConnectionHost.from_dict(hosts_item_data)



            hosts.append(hosts_item)


        def _parse_fix_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        fix_url = _parse_fix_url(d.pop("fixUrl", UNSET))


        airbnb_connection_summary = cls(
            status=status,
            host_count=host_count,
            hosts=hosts,
            fix_url=fix_url,
        )


        airbnb_connection_summary.additional_properties = d
        return airbnb_connection_summary

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
