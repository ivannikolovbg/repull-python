from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_vrbo_listing_taxes_body_partner_tax_settings import UpdateVrboListingTaxesBodyPartnerTaxSettings
  from ..models.update_vrbo_listing_taxes_body_stay_tax import UpdateVrboListingTaxesBodyStayTax
  from ..models.update_vrbo_listing_taxes_body_tax import UpdateVrboListingTaxesBodyTax





T = TypeVar("T", bound="UpdateVrboListingTaxesBody")



@_attrs_define
class UpdateVrboListingTaxesBody:
    """ 
        Attributes:
            tax (UpdateVrboListingTaxesBodyTax | Unset):
            stay_tax (UpdateVrboListingTaxesBodyStayTax | Unset):
            partner_tax_settings (UpdateVrboListingTaxesBodyPartnerTaxSettings | Unset):
     """

    tax: UpdateVrboListingTaxesBodyTax | Unset = UNSET
    stay_tax: UpdateVrboListingTaxesBodyStayTax | Unset = UNSET
    partner_tax_settings: UpdateVrboListingTaxesBodyPartnerTaxSettings | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_vrbo_listing_taxes_body_partner_tax_settings import UpdateVrboListingTaxesBodyPartnerTaxSettings
        from ..models.update_vrbo_listing_taxes_body_stay_tax import UpdateVrboListingTaxesBodyStayTax
        from ..models.update_vrbo_listing_taxes_body_tax import UpdateVrboListingTaxesBodyTax
        tax: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tax, Unset):
            tax = self.tax.to_dict()

        stay_tax: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stay_tax, Unset):
            stay_tax = self.stay_tax.to_dict()

        partner_tax_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.partner_tax_settings, Unset):
            partner_tax_settings = self.partner_tax_settings.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if tax is not UNSET:
            field_dict["tax"] = tax
        if stay_tax is not UNSET:
            field_dict["stayTax"] = stay_tax
        if partner_tax_settings is not UNSET:
            field_dict["partnerTaxSettings"] = partner_tax_settings

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_vrbo_listing_taxes_body_partner_tax_settings import UpdateVrboListingTaxesBodyPartnerTaxSettings
        from ..models.update_vrbo_listing_taxes_body_stay_tax import UpdateVrboListingTaxesBodyStayTax
        from ..models.update_vrbo_listing_taxes_body_tax import UpdateVrboListingTaxesBodyTax
        d = dict(src_dict)
        _tax = d.pop("tax", UNSET)
        tax: UpdateVrboListingTaxesBodyTax | Unset
        if isinstance(_tax,  Unset):
            tax = UNSET
        else:
            tax = UpdateVrboListingTaxesBodyTax.from_dict(_tax)




        _stay_tax = d.pop("stayTax", UNSET)
        stay_tax: UpdateVrboListingTaxesBodyStayTax | Unset
        if isinstance(_stay_tax,  Unset):
            stay_tax = UNSET
        else:
            stay_tax = UpdateVrboListingTaxesBodyStayTax.from_dict(_stay_tax)




        _partner_tax_settings = d.pop("partnerTaxSettings", UNSET)
        partner_tax_settings: UpdateVrboListingTaxesBodyPartnerTaxSettings | Unset
        if isinstance(_partner_tax_settings,  Unset):
            partner_tax_settings = UNSET
        else:
            partner_tax_settings = UpdateVrboListingTaxesBodyPartnerTaxSettings.from_dict(_partner_tax_settings)




        update_vrbo_listing_taxes_body = cls(
            tax=tax,
            stay_tax=stay_tax,
            partner_tax_settings=partner_tax_settings,
        )

        return update_vrbo_listing_taxes_body

