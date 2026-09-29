from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.conversation_capabilities_offer_price_type_1 import ConversationCapabilitiesOfferPriceType1
from ..models.conversation_capabilities_offer_price_type_2_type_1 import ConversationCapabilitiesOfferPriceType2Type1
from ..models.conversation_capabilities_offer_price_type_3_type_1 import ConversationCapabilitiesOfferPriceType3Type1
from typing import cast






T = TypeVar("T", bound="ConversationCapabilities")



@_attrs_define
class ConversationCapabilities:
    """ What the inquiry actions can do on this conversation right now — one set of endpoints for every channel, so an app
    shows the right actions instead of learning from a `422`. All `false` / `null` when nothing applies (a booked or
    closed inquiry, Booking.com, direct, an Airbnb inquiry relayed by a PMS).

        Example:
            {'canPreApprove': False, 'canWithdraw': True, 'canSendOffer': True, 'offerPrice': 'breakdown',
                'canPreviewOffer': True}

        Attributes:
            can_pre_approve (bool): `POST /v1/conversations/{id}/pre-approval` would pre-approve the open inquiry (Airbnb
                connected directly, VRBO).
            can_withdraw (bool): A pre-approval or offer is live and can be withdrawn — `DELETE /v1/conversations/{id}/pre-
                approval` (VRBO) or `DELETE …/special-offers/{offerId}` (Airbnb).
            can_send_offer (bool): `POST /v1/conversations/{id}/special-offers` would send an offer.
            offer_price (ConversationCapabilitiesOfferPriceType1 | ConversationCapabilitiesOfferPriceType2Type1 |
                ConversationCapabilitiesOfferPriceType3Type1 | None): How an offer is priced here: `total` — one `totalPrice`
                for the stay (Airbnb); `breakdown` — `rentalAmount`, `fees`, `damageDeposit`, and the channel computes the guest
                total (VRBO).
            can_preview_offer (bool): `POST /v1/conversations/{id}/special-offers/preview` returns the channel’s
                recalculated offer (VRBO).
     """

    can_pre_approve: bool
    can_withdraw: bool
    can_send_offer: bool
    offer_price: ConversationCapabilitiesOfferPriceType1 | ConversationCapabilitiesOfferPriceType2Type1 | ConversationCapabilitiesOfferPriceType3Type1 | None
    can_preview_offer: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        can_pre_approve = self.can_pre_approve

        can_withdraw = self.can_withdraw

        can_send_offer = self.can_send_offer

        offer_price: None | str
        if isinstance(self.offer_price, ConversationCapabilitiesOfferPriceType1):
            offer_price = self.offer_price.value
        elif isinstance(self.offer_price, ConversationCapabilitiesOfferPriceType2Type1):
            offer_price = self.offer_price.value
        elif isinstance(self.offer_price, ConversationCapabilitiesOfferPriceType3Type1):
            offer_price = self.offer_price.value
        else:
            offer_price = self.offer_price

        can_preview_offer = self.can_preview_offer


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "canPreApprove": can_pre_approve,
            "canWithdraw": can_withdraw,
            "canSendOffer": can_send_offer,
            "offerPrice": offer_price,
            "canPreviewOffer": can_preview_offer,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        can_pre_approve = d.pop("canPreApprove")

        can_withdraw = d.pop("canWithdraw")

        can_send_offer = d.pop("canSendOffer")

        def _parse_offer_price(data: object) -> ConversationCapabilitiesOfferPriceType1 | ConversationCapabilitiesOfferPriceType2Type1 | ConversationCapabilitiesOfferPriceType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                offer_price_type_1 = ConversationCapabilitiesOfferPriceType1(data)



                return offer_price_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                offer_price_type_2_type_1 = ConversationCapabilitiesOfferPriceType2Type1(data)



                return offer_price_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                offer_price_type_3_type_1 = ConversationCapabilitiesOfferPriceType3Type1(data)



                return offer_price_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConversationCapabilitiesOfferPriceType1 | ConversationCapabilitiesOfferPriceType2Type1 | ConversationCapabilitiesOfferPriceType3Type1 | None, data)

        offer_price = _parse_offer_price(d.pop("offerPrice"))


        can_preview_offer = d.pop("canPreviewOffer")

        conversation_capabilities = cls(
            can_pre_approve=can_pre_approve,
            can_withdraw=can_withdraw,
            can_send_offer=can_send_offer,
            offer_price=offer_price,
            can_preview_offer=can_preview_offer,
        )


        conversation_capabilities.additional_properties = d
        return conversation_capabilities

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
