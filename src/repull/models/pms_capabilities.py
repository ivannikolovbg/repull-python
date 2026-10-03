from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.pms_capabilities_calendar import PmsCapabilitiesCalendar
  from ..models.pms_capabilities_conversations import PmsCapabilitiesConversations
  from ..models.pms_capabilities_guests import PmsCapabilitiesGuests
  from ..models.pms_capabilities_listings import PmsCapabilitiesListings
  from ..models.pms_capabilities_notes import PmsCapabilitiesNotes
  from ..models.pms_capabilities_payments import PmsCapabilitiesPayments
  from ..models.pms_capabilities_reservations import PmsCapabilitiesReservations
  from ..models.pms_capabilities_reviews import PmsCapabilitiesReviews
  from ..models.pms_capabilities_tasks import PmsCapabilitiesTasks





T = TypeVar("T", bound="PmsCapabilities")



@_attrs_define
class PmsCapabilities:
    """ What the API does through a connected PMS beyond reservation writes, read from the same connector table the router
    uses — a `false` flag is a `422 pms_write_unsupported` naming the PMS.

        Attributes:
            provider (str | Unset):  Example: guesty.
            connected (bool | Unset): `false`: what the connector supports once connected (on a listing: a dead link — every
                write answers `409 no_connection`).
            reservations (PmsCapabilitiesReservations | Unset):
            reviews (PmsCapabilitiesReviews | Unset):
            listings (PmsCapabilitiesListings | Unset): Sections `PUT /v1/listings/{id}/content` writes to the PMS.
            guests (PmsCapabilitiesGuests | Unset):
            conversations (PmsCapabilitiesConversations | Unset):
            calendar (PmsCapabilitiesCalendar | Unset):
            payments (PmsCapabilitiesPayments | Unset):
            tasks (PmsCapabilitiesTasks | Unset):
            notes (PmsCapabilitiesNotes | Unset): The connector's own notes per family (limits, required access).
     """

    provider: str | Unset = UNSET
    connected: bool | Unset = UNSET
    reservations: PmsCapabilitiesReservations | Unset = UNSET
    reviews: PmsCapabilitiesReviews | Unset = UNSET
    listings: PmsCapabilitiesListings | Unset = UNSET
    guests: PmsCapabilitiesGuests | Unset = UNSET
    conversations: PmsCapabilitiesConversations | Unset = UNSET
    calendar: PmsCapabilitiesCalendar | Unset = UNSET
    payments: PmsCapabilitiesPayments | Unset = UNSET
    tasks: PmsCapabilitiesTasks | Unset = UNSET
    notes: PmsCapabilitiesNotes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.pms_capabilities_calendar import PmsCapabilitiesCalendar
        from ..models.pms_capabilities_conversations import PmsCapabilitiesConversations
        from ..models.pms_capabilities_guests import PmsCapabilitiesGuests
        from ..models.pms_capabilities_listings import PmsCapabilitiesListings
        from ..models.pms_capabilities_notes import PmsCapabilitiesNotes
        from ..models.pms_capabilities_payments import PmsCapabilitiesPayments
        from ..models.pms_capabilities_reservations import PmsCapabilitiesReservations
        from ..models.pms_capabilities_reviews import PmsCapabilitiesReviews
        from ..models.pms_capabilities_tasks import PmsCapabilitiesTasks
        provider = self.provider

        connected = self.connected

        reservations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reservations, Unset):
            reservations = self.reservations.to_dict()

        reviews: dict[str, Any] | Unset = UNSET
        if not isinstance(self.reviews, Unset):
            reviews = self.reviews.to_dict()

        listings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.listings, Unset):
            listings = self.listings.to_dict()

        guests: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guests, Unset):
            guests = self.guests.to_dict()

        conversations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.conversations, Unset):
            conversations = self.conversations.to_dict()

        calendar: dict[str, Any] | Unset = UNSET
        if not isinstance(self.calendar, Unset):
            calendar = self.calendar.to_dict()

        payments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payments, Unset):
            payments = self.payments.to_dict()

        tasks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = self.tasks.to_dict()

        notes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if provider is not UNSET:
            field_dict["provider"] = provider
        if connected is not UNSET:
            field_dict["connected"] = connected
        if reservations is not UNSET:
            field_dict["reservations"] = reservations
        if reviews is not UNSET:
            field_dict["reviews"] = reviews
        if listings is not UNSET:
            field_dict["listings"] = listings
        if guests is not UNSET:
            field_dict["guests"] = guests
        if conversations is not UNSET:
            field_dict["conversations"] = conversations
        if calendar is not UNSET:
            field_dict["calendar"] = calendar
        if payments is not UNSET:
            field_dict["payments"] = payments
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pms_capabilities_calendar import PmsCapabilitiesCalendar
        from ..models.pms_capabilities_conversations import PmsCapabilitiesConversations
        from ..models.pms_capabilities_guests import PmsCapabilitiesGuests
        from ..models.pms_capabilities_listings import PmsCapabilitiesListings
        from ..models.pms_capabilities_notes import PmsCapabilitiesNotes
        from ..models.pms_capabilities_payments import PmsCapabilitiesPayments
        from ..models.pms_capabilities_reservations import PmsCapabilitiesReservations
        from ..models.pms_capabilities_reviews import PmsCapabilitiesReviews
        from ..models.pms_capabilities_tasks import PmsCapabilitiesTasks
        d = dict(src_dict)
        provider = d.pop("provider", UNSET)

        connected = d.pop("connected", UNSET)

        _reservations = d.pop("reservations", UNSET)
        reservations: PmsCapabilitiesReservations | Unset
        if isinstance(_reservations,  Unset):
            reservations = UNSET
        else:
            reservations = PmsCapabilitiesReservations.from_dict(_reservations)




        _reviews = d.pop("reviews", UNSET)
        reviews: PmsCapabilitiesReviews | Unset
        if isinstance(_reviews,  Unset):
            reviews = UNSET
        else:
            reviews = PmsCapabilitiesReviews.from_dict(_reviews)




        _listings = d.pop("listings", UNSET)
        listings: PmsCapabilitiesListings | Unset
        if isinstance(_listings,  Unset):
            listings = UNSET
        else:
            listings = PmsCapabilitiesListings.from_dict(_listings)




        _guests = d.pop("guests", UNSET)
        guests: PmsCapabilitiesGuests | Unset
        if isinstance(_guests,  Unset):
            guests = UNSET
        else:
            guests = PmsCapabilitiesGuests.from_dict(_guests)




        _conversations = d.pop("conversations", UNSET)
        conversations: PmsCapabilitiesConversations | Unset
        if isinstance(_conversations,  Unset):
            conversations = UNSET
        else:
            conversations = PmsCapabilitiesConversations.from_dict(_conversations)




        _calendar = d.pop("calendar", UNSET)
        calendar: PmsCapabilitiesCalendar | Unset
        if isinstance(_calendar,  Unset):
            calendar = UNSET
        else:
            calendar = PmsCapabilitiesCalendar.from_dict(_calendar)




        _payments = d.pop("payments", UNSET)
        payments: PmsCapabilitiesPayments | Unset
        if isinstance(_payments,  Unset):
            payments = UNSET
        else:
            payments = PmsCapabilitiesPayments.from_dict(_payments)




        _tasks = d.pop("tasks", UNSET)
        tasks: PmsCapabilitiesTasks | Unset
        if isinstance(_tasks,  Unset):
            tasks = UNSET
        else:
            tasks = PmsCapabilitiesTasks.from_dict(_tasks)




        _notes = d.pop("notes", UNSET)
        notes: PmsCapabilitiesNotes | Unset
        if isinstance(_notes,  Unset):
            notes = UNSET
        else:
            notes = PmsCapabilitiesNotes.from_dict(_notes)




        pms_capabilities = cls(
            provider=provider,
            connected=connected,
            reservations=reservations,
            reviews=reviews,
            listings=listings,
            guests=guests,
            conversations=conversations,
            calendar=calendar,
            payments=payments,
            tasks=tasks,
            notes=notes,
        )


        pms_capabilities.additional_properties = d
        return pms_capabilities

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
