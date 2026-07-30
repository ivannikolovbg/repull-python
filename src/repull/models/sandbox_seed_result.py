from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.sandbox_fixture_ref import SandboxFixtureRef





T = TypeVar("T", bound="SandboxSeedResult")



@_attrs_define
class SandboxSeedResult:
    """ Result of provisioning the sandbox fixture set.

        Attributes:
            customer_id (str):  Example: 1.
            seeded_at (datetime.datetime):
            listings (list[SandboxFixtureRef]): 3 sample listings.
            reservations (list[SandboxFixtureRef]): 5 reservations across the lifecycle: created, modified, cancelled, date-
                changed, pending.
            connections (list[SandboxFixtureRef]): 2 fake connected provider accounts: Airbnb + Booking.com.
     """

    customer_id: str
    seeded_at: datetime.datetime
    listings: list[SandboxFixtureRef]
    reservations: list[SandboxFixtureRef]
    connections: list[SandboxFixtureRef]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sandbox_fixture_ref import SandboxFixtureRef
        customer_id = self.customer_id

        seeded_at = self.seeded_at.isoformat()

        listings = []
        for listings_item_data in self.listings:
            listings_item = listings_item_data.to_dict()
            listings.append(listings_item)



        reservations = []
        for reservations_item_data in self.reservations:
            reservations_item = reservations_item_data.to_dict()
            reservations.append(reservations_item)



        connections = []
        for connections_item_data in self.connections:
            connections_item = connections_item_data.to_dict()
            connections.append(connections_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "customerId": customer_id,
            "seededAt": seeded_at,
            "listings": listings,
            "reservations": reservations,
            "connections": connections,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_fixture_ref import SandboxFixtureRef
        d = dict(src_dict)
        customer_id = d.pop("customerId")

        seeded_at = isoparse(d.pop("seededAt"))




        listings = []
        _listings = d.pop("listings")
        for listings_item_data in (_listings):
            listings_item = SandboxFixtureRef.from_dict(listings_item_data)



            listings.append(listings_item)


        reservations = []
        _reservations = d.pop("reservations")
        for reservations_item_data in (_reservations):
            reservations_item = SandboxFixtureRef.from_dict(reservations_item_data)



            reservations.append(reservations_item)


        connections = []
        _connections = d.pop("connections")
        for connections_item_data in (_connections):
            connections_item = SandboxFixtureRef.from_dict(connections_item_data)



            connections.append(connections_item)


        sandbox_seed_result = cls(
            customer_id=customer_id,
            seeded_at=seeded_at,
            listings=listings,
            reservations=reservations,
            connections=connections,
        )


        sandbox_seed_result.additional_properties = d
        return sandbox_seed_result

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
