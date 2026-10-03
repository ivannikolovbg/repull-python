from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.pms_capabilities import PmsCapabilities
  from ..models.reservation_capabilities import ReservationCapabilities





T = TypeVar("T", bound="ConnectStatusCapabilities")



@_attrs_define
class ConnectStatusCapabilities:
    """ PMS providers only. `reservations`: which reservation writes the API performs on this connection's listings — the
    connector's support combined with `writePolicy`. `pms`: everything else the API does through this PMS (review
    replies, request answers, listing content, guests, message channel/attachments, calendar). When `connected` is
    false, what the connector supports once connected.

        Attributes:
            reservations (ReservationCapabilities | Unset): Which reservation writes the API performs for this listing (or,
                on `GET /v1/connect/{provider}`, for any listing of that connection). Derived from the PMS connector, the
                connection, and its write policy — a flag is true only when all three allow it.
            pms (PmsCapabilities | Unset): What the API does through a connected PMS beyond reservation writes, read from
                the same connector table the router uses — a `false` flag is a `422 pms_write_unsupported` naming the PMS.
     """

    reservations: ReservationCapabilities | Unset = UNSET
    pms: PmsCapabilities | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.pms_capabilities import PmsCapabilities
        from ..models.reservation_capabilities import ReservationCapabilities
        reservations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reservations, Unset):
            reservations = self.reservations.to_dict()

        pms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pms, Unset):
            pms = self.pms.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if reservations is not UNSET:
            field_dict["reservations"] = reservations
        if pms is not UNSET:
            field_dict["pms"] = pms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pms_capabilities import PmsCapabilities
        from ..models.reservation_capabilities import ReservationCapabilities
        d = dict(src_dict)
        _reservations = d.pop("reservations", UNSET)
        reservations: ReservationCapabilities | Unset
        if isinstance(_reservations,  Unset):
            reservations = UNSET
        else:
            reservations = ReservationCapabilities.from_dict(_reservations)




        _pms = d.pop("pms", UNSET)
        pms: PmsCapabilities | Unset
        if isinstance(_pms,  Unset):
            pms = UNSET
        else:
            pms = PmsCapabilities.from_dict(_pms)




        connect_status_capabilities = cls(
            reservations=reservations,
            pms=pms,
        )


        connect_status_capabilities.additional_properties = d
        return connect_status_capabilities

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
