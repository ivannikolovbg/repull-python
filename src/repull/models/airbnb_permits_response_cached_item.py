from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.airbnb_permits_response_cached_item_permit_data_type_0 import AirbnbPermitsResponseCachedItemPermitDataType0





T = TypeVar("T", bound="AirbnbPermitsResponseCachedItem")



@_attrs_define
class AirbnbPermitsResponseCachedItem:
    """ 
        Attributes:
            regulatory_body (None | str | Unset):
            regulation_type (None | str | Unset):
            status (None | str | Unset):
            permit_number (None | str | Unset):
            permit_data (AirbnbPermitsResponseCachedItemPermitDataType0 | None | Unset):
            updated_at (datetime.datetime | None | Unset):
     """

    regulatory_body: None | str | Unset = UNSET
    regulation_type: None | str | Unset = UNSET
    status: None | str | Unset = UNSET
    permit_number: None | str | Unset = UNSET
    permit_data: AirbnbPermitsResponseCachedItemPermitDataType0 | None | Unset = UNSET
    updated_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_permits_response_cached_item_permit_data_type_0 import AirbnbPermitsResponseCachedItemPermitDataType0
        regulatory_body: None | str | Unset
        if isinstance(self.regulatory_body, Unset):
            regulatory_body = UNSET
        else:
            regulatory_body = self.regulatory_body

        regulation_type: None | str | Unset
        if isinstance(self.regulation_type, Unset):
            regulation_type = UNSET
        else:
            regulation_type = self.regulation_type

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        permit_number: None | str | Unset
        if isinstance(self.permit_number, Unset):
            permit_number = UNSET
        else:
            permit_number = self.permit_number

        permit_data: dict[str, Any] | None | Unset
        if isinstance(self.permit_data, Unset):
            permit_data = UNSET
        elif isinstance(self.permit_data, AirbnbPermitsResponseCachedItemPermitDataType0):
            permit_data = self.permit_data.to_dict()
        else:
            permit_data = self.permit_data

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        elif isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if regulatory_body is not UNSET:
            field_dict["regulatoryBody"] = regulatory_body
        if regulation_type is not UNSET:
            field_dict["regulationType"] = regulation_type
        if status is not UNSET:
            field_dict["status"] = status
        if permit_number is not UNSET:
            field_dict["permitNumber"] = permit_number
        if permit_data is not UNSET:
            field_dict["permitData"] = permit_data
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_permits_response_cached_item_permit_data_type_0 import AirbnbPermitsResponseCachedItemPermitDataType0
        d = dict(src_dict)
        def _parse_regulatory_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        regulatory_body = _parse_regulatory_body(d.pop("regulatoryBody", UNSET))


        def _parse_regulation_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        regulation_type = _parse_regulation_type(d.pop("regulationType", UNSET))


        def _parse_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status = _parse_status(d.pop("status", UNSET))


        def _parse_permit_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        permit_number = _parse_permit_number(d.pop("permitNumber", UNSET))


        def _parse_permit_data(data: object) -> AirbnbPermitsResponseCachedItemPermitDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                permit_data_type_0 = AirbnbPermitsResponseCachedItemPermitDataType0.from_dict(data)



                return permit_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AirbnbPermitsResponseCachedItemPermitDataType0 | None | Unset, data)

        permit_data = _parse_permit_data(d.pop("permitData", UNSET))


        def _parse_updated_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        airbnb_permits_response_cached_item = cls(
            regulatory_body=regulatory_body,
            regulation_type=regulation_type,
            status=status,
            permit_number=permit_number,
            permit_data=permit_data,
            updated_at=updated_at,
        )


        airbnb_permits_response_cached_item.additional_properties = d
        return airbnb_permits_response_cached_item

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
