from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.tiket_content_response_objects_item import TiketContentResponseObjectsItem





T = TypeVar("T", bound="TiketContentResponse")



@_attrs_define
class TiketContentResponse:
    """ Returned by `GET /v1/channels/tiket/content`.

        Attributes:
            property_id (None | str | Unset):
            partner_hotel_code (None | str | Unset):
            chain_code (None | str | Unset):
            content_mapped (bool | None | Unset):
            activation_status (None | str | Unset): Same as on `GET /v1/channels/tiket/properties`.
            objects (list[TiketContentResponseObjectsItem] | Unset): One entry per content object Repull sent: the property,
                each room type, each rate plan.
     """

    property_id: None | str | Unset = UNSET
    partner_hotel_code: None | str | Unset = UNSET
    chain_code: None | str | Unset = UNSET
    content_mapped: bool | None | Unset = UNSET
    activation_status: None | str | Unset = UNSET
    objects: list[TiketContentResponseObjectsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.tiket_content_response_objects_item import TiketContentResponseObjectsItem
        property_id: None | str | Unset
        if isinstance(self.property_id, Unset):
            property_id = UNSET
        else:
            property_id = self.property_id

        partner_hotel_code: None | str | Unset
        if isinstance(self.partner_hotel_code, Unset):
            partner_hotel_code = UNSET
        else:
            partner_hotel_code = self.partner_hotel_code

        chain_code: None | str | Unset
        if isinstance(self.chain_code, Unset):
            chain_code = UNSET
        else:
            chain_code = self.chain_code

        content_mapped: bool | None | Unset
        if isinstance(self.content_mapped, Unset):
            content_mapped = UNSET
        else:
            content_mapped = self.content_mapped

        activation_status: None | str | Unset
        if isinstance(self.activation_status, Unset):
            activation_status = UNSET
        else:
            activation_status = self.activation_status

        objects: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.objects, Unset):
            objects = []
            for objects_item_data in self.objects:
                objects_item = objects_item_data.to_dict()
                objects.append(objects_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if property_id is not UNSET:
            field_dict["propertyId"] = property_id
        if partner_hotel_code is not UNSET:
            field_dict["partnerHotelCode"] = partner_hotel_code
        if chain_code is not UNSET:
            field_dict["chainCode"] = chain_code
        if content_mapped is not UNSET:
            field_dict["contentMapped"] = content_mapped
        if activation_status is not UNSET:
            field_dict["activationStatus"] = activation_status
        if objects is not UNSET:
            field_dict["objects"] = objects

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tiket_content_response_objects_item import TiketContentResponseObjectsItem
        d = dict(src_dict)
        def _parse_property_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        property_id = _parse_property_id(d.pop("propertyId", UNSET))


        def _parse_partner_hotel_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        partner_hotel_code = _parse_partner_hotel_code(d.pop("partnerHotelCode", UNSET))


        def _parse_chain_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        chain_code = _parse_chain_code(d.pop("chainCode", UNSET))


        def _parse_content_mapped(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        content_mapped = _parse_content_mapped(d.pop("contentMapped", UNSET))


        def _parse_activation_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        activation_status = _parse_activation_status(d.pop("activationStatus", UNSET))


        _objects = d.pop("objects", UNSET)
        objects: list[TiketContentResponseObjectsItem] | Unset = UNSET
        if _objects is not UNSET:
            objects = []
            for objects_item_data in _objects:
                objects_item = TiketContentResponseObjectsItem.from_dict(objects_item_data)



                objects.append(objects_item)


        tiket_content_response = cls(
            property_id=property_id,
            partner_hotel_code=partner_hotel_code,
            chain_code=chain_code,
            content_mapped=content_mapped,
            activation_status=activation_status,
            objects=objects,
        )


        tiket_content_response.additional_properties = d
        return tiket_content_response

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
