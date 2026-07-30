from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.airbnb_pricing_write_request_type import AirbnbPricingWriteRequestType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_calendar_operation import AirbnbCalendarOperation
  from ..models.airbnb_pricing_write_request_records_type_0_item import AirbnbPricingWriteRequestRecordsType0Item
  from ..models.airbnb_pricing_write_request_rule_type_0 import AirbnbPricingWriteRequestRuleType0
  from ..models.airbnb_pricing_write_request_settings_type_0 import AirbnbPricingWriteRequestSettingsType0





T = TypeVar("T", bound="AirbnbPricingWriteRequest")



@_attrs_define
class AirbnbPricingWriteRequest:
    """ Body for `PUT /v1/channels/airbnb/listings/{id}/pricing`. The `type` discriminator selects the pricing sub-resource.
    `type: "calendar"` shares the same per-date restriction shape as the availability endpoint (min/max nights, closed-
    to-arrival/departure, stop-sell via `availability: "unavailable"`).

        Attributes:
            type_ (AirbnbPricingWriteRequestType):
            operations (list[AirbnbCalendarOperation] | Unset): Required when `type: "calendar"`. Batch of per-date price +
                restriction operations.
            model_type (None | str | Unset): Required when `type: "model"` — the pricing-availability model to switch the
                listing to.
            settings (AirbnbPricingWriteRequestSettingsType0 | None | Unset): Required for `type: "standard" | "rate-plan" |
                "fees"` — the pricing-settings object to PUT.
            records (list[AirbnbPricingWriteRequestRecordsType0Item] | None | Unset): Required for `type: "los"` — length-
                of-stay records.
            currency (None | str | Unset): Required for `type: "currency"` — ISO 4217 code.
            rule (AirbnbPricingWriteRequestRuleType0 | None | Unset): Required for `type: "rule"` — a single pricing rule
                appended to the listing.
     """

    type_: AirbnbPricingWriteRequestType
    operations: list[AirbnbCalendarOperation] | Unset = UNSET
    model_type: None | str | Unset = UNSET
    settings: AirbnbPricingWriteRequestSettingsType0 | None | Unset = UNSET
    records: list[AirbnbPricingWriteRequestRecordsType0Item] | None | Unset = UNSET
    currency: None | str | Unset = UNSET
    rule: AirbnbPricingWriteRequestRuleType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_calendar_operation import AirbnbCalendarOperation
        from ..models.airbnb_pricing_write_request_records_type_0_item import AirbnbPricingWriteRequestRecordsType0Item
        from ..models.airbnb_pricing_write_request_rule_type_0 import AirbnbPricingWriteRequestRuleType0
        from ..models.airbnb_pricing_write_request_settings_type_0 import AirbnbPricingWriteRequestSettingsType0
        type_ = self.type_.value

        operations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.operations, Unset):
            operations = []
            for operations_item_data in self.operations:
                operations_item = operations_item_data.to_dict()
                operations.append(operations_item)



        model_type: None | str | Unset
        if isinstance(self.model_type, Unset):
            model_type = UNSET
        else:
            model_type = self.model_type

        settings: dict[str, Any] | None | Unset
        if isinstance(self.settings, Unset):
            settings = UNSET
        elif isinstance(self.settings, AirbnbPricingWriteRequestSettingsType0):
            settings = self.settings.to_dict()
        else:
            settings = self.settings

        records: list[dict[str, Any]] | None | Unset
        if isinstance(self.records, Unset):
            records = UNSET
        elif isinstance(self.records, list):
            records = []
            for records_type_0_item_data in self.records:
                records_type_0_item = records_type_0_item_data.to_dict()
                records.append(records_type_0_item)


        else:
            records = self.records

        currency: None | str | Unset
        if isinstance(self.currency, Unset):
            currency = UNSET
        else:
            currency = self.currency

        rule: dict[str, Any] | None | Unset
        if isinstance(self.rule, Unset):
            rule = UNSET
        elif isinstance(self.rule, AirbnbPricingWriteRequestRuleType0):
            rule = self.rule.to_dict()
        else:
            rule = self.rule


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })
        if operations is not UNSET:
            field_dict["operations"] = operations
        if model_type is not UNSET:
            field_dict["modelType"] = model_type
        if settings is not UNSET:
            field_dict["settings"] = settings
        if records is not UNSET:
            field_dict["records"] = records
        if currency is not UNSET:
            field_dict["currency"] = currency
        if rule is not UNSET:
            field_dict["rule"] = rule

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_calendar_operation import AirbnbCalendarOperation
        from ..models.airbnb_pricing_write_request_records_type_0_item import AirbnbPricingWriteRequestRecordsType0Item
        from ..models.airbnb_pricing_write_request_rule_type_0 import AirbnbPricingWriteRequestRuleType0
        from ..models.airbnb_pricing_write_request_settings_type_0 import AirbnbPricingWriteRequestSettingsType0
        d = dict(src_dict)
        type_ = AirbnbPricingWriteRequestType(d.pop("type"))




        _operations = d.pop("operations", UNSET)
        operations: list[AirbnbCalendarOperation] | Unset = UNSET
        if _operations is not UNSET:
            operations = []
            for operations_item_data in _operations:
                operations_item = AirbnbCalendarOperation.from_dict(operations_item_data)



                operations.append(operations_item)


        def _parse_model_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model_type = _parse_model_type(d.pop("modelType", UNSET))


        def _parse_settings(data: object) -> AirbnbPricingWriteRequestSettingsType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                settings_type_0 = AirbnbPricingWriteRequestSettingsType0.from_dict(data)



                return settings_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AirbnbPricingWriteRequestSettingsType0 | None | Unset, data)

        settings = _parse_settings(d.pop("settings", UNSET))


        def _parse_records(data: object) -> list[AirbnbPricingWriteRequestRecordsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                records_type_0 = []
                _records_type_0 = data
                for records_type_0_item_data in (_records_type_0):
                    records_type_0_item = AirbnbPricingWriteRequestRecordsType0Item.from_dict(records_type_0_item_data)



                    records_type_0.append(records_type_0_item)

                return records_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AirbnbPricingWriteRequestRecordsType0Item] | None | Unset, data)

        records = _parse_records(d.pop("records", UNSET))


        def _parse_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        currency = _parse_currency(d.pop("currency", UNSET))


        def _parse_rule(data: object) -> AirbnbPricingWriteRequestRuleType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rule_type_0 = AirbnbPricingWriteRequestRuleType0.from_dict(data)



                return rule_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AirbnbPricingWriteRequestRuleType0 | None | Unset, data)

        rule = _parse_rule(d.pop("rule", UNSET))


        airbnb_pricing_write_request = cls(
            type_=type_,
            operations=operations,
            model_type=model_type,
            settings=settings,
            records=records,
            currency=currency,
            rule=rule,
        )


        airbnb_pricing_write_request.additional_properties = d
        return airbnb_pricing_write_request

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
