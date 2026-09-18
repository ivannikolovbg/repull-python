from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.airbnb_publish_result import AirbnbPublishResult





T = TypeVar("T", bound="AirbnbListingActionResponse200Type1")



@_attrs_define
class AirbnbListingActionResponse200Type1:
    """ `push` / `publish` — the per-section publish result.

        Attributes:
            id (str | Unset):
            action (str | Unset):
            channel (str | Unset):
            result (AirbnbPublishResult | Unset): A publish is not one call to Airbnb: it is up to eight independent ones
                (details, description, amenities, rooms, policies, photos, pricing, checkout_tasks), each of which can fail on
                its own. A PARTIAL publish is normal — what succeeded stays applied; there is no rollback.
     """

    id: str | Unset = UNSET
    action: str | Unset = UNSET
    channel: str | Unset = UNSET
    result: AirbnbPublishResult | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.airbnb_publish_result import AirbnbPublishResult
        id = self.id

        action = self.action

        channel = self.channel

        result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if action is not UNSET:
            field_dict["action"] = action
        if channel is not UNSET:
            field_dict["channel"] = channel
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.airbnb_publish_result import AirbnbPublishResult
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        action = d.pop("action", UNSET)

        channel = d.pop("channel", UNSET)

        _result = d.pop("result", UNSET)
        result: AirbnbPublishResult | Unset
        if isinstance(_result,  Unset):
            result = UNSET
        else:
            result = AirbnbPublishResult.from_dict(_result)




        airbnb_listing_action_response_200_type_1 = cls(
            id=id,
            action=action,
            channel=channel,
            result=result,
        )


        airbnb_listing_action_response_200_type_1.additional_properties = d
        return airbnb_listing_action_response_200_type_1

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
