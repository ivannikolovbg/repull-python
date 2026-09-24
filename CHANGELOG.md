# Changelog

All notable changes to the `repull` Python SDK are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.18] - 2026-09-24

Regenerated against the live `https://api.repull.dev/openapi.json`
(202 → 209 operations).

### Added
- **Repull Migrate** — `repull.api.migrate`: `list_migrations`, `get_migration`,
  `get_migration_report`, `get_migration_channel_map`, `run_migration_import`,
  `check_migration_cutover`, `cutover_migration`, `delete_migration`.
- `create_connect_session` accepts `purpose="migrate"`, `workspace`, `copy`
  and `scope`; the session returns `workspace_id`.
- `migration.completed` / `migration.failed` webhook events; child-workspace
  events carry `workspace_id`.
- `ConnectProvider.migration_capabilities` — what each PMS can carry across.

### Changed
- Airbnb permits write takes Airbnb's submission shape: `flow_slug` plus
  `answers` keyed by each question's `answer_key` (the previous shape never
  reached Airbnb — its route returned 404).

### Removed
- `get_atlas_health` (the endpoint was retired).

## [0.2.17] - 2026-09-23

Regenerated against the live `https://api.repull.dev/openapi.json`
(199 → 202 operations, none removed).

### Added
- **Market state** — `repull.api.listings.take_listing_online` and
  `take_listing_offline` (`POST /v1/listings/{id}/online|offline`). Take a
  listing off sale, or put it back, on every connected channel in one call.
  This is *not* the same as deactivating a listing in Repull: going offline
  stops the listing taking bookings but leaves billing, plan limits and API
  access untouched, while `active: false` does the opposite. The answer is per
  channel item — check each `ChannelMarketStateItem.ok`, since channels fail
  independently and a partial result is the ordinary outcome. Models:
  `ListingMarketStateRequest`, `ListingMarketStateResponse`,
  `ChannelMarketStateItem`.
- **Booking.com unlist / relist** — `repull.api.booking_com.booking_property_action`
  (`POST /v1/channels/booking/properties/{id}`, where `id` is a Repull listing
  id). Booking.com has no unlist, so `unlist` closes the mapped room across the
  forward window; `relist` re-syncs the true calendar rather than opening
  everything, so genuinely blocked dates stay blocked. Pass `hotel_id` when the
  listing maps to several properties, or the call is refused with
  `409 ambiguous_booking_mapping` and nothing is written. Models:
  `BookingPropertyActionRequest`, `BookingPropertyActionResponse`.
- **Booking.com setup actions** — `POST /v1/channels/booking/setup` gains
  `create-property`, `add-room`, `add-unit` and `advance`.
- **Listing address + room type on create** — `ListingCreateRequest` gains
  `room_type_category`, `property_type_category`, `postal_code` (and the
  `zipcode` alias). Airbnb refuses to activate a listing that has not stated a
  room type, answering "Please specify a valid room type" — which reads like a
  beds problem and is not. `ListingContentUpdateRequest.address` gains `state`
  and `postal_code`.
- **Publish diagnostics** — `ListingPublishStatusChannel.push_error` (the
  channel's own reason for the last failed push, verbatim),
  `ListingPublishStatusConnection.locked_fields`, and
  `ListingPublishStatusResponse.address_readiness`
  (`ListingAddressReadiness`).
- **Publish results** — new `BookingPublishResult` (with
  `BookingPublishSectionError`); `AirbnbPublishResult` gains `live` and
  `warnings`. `published: true` with `live: false` is a real and common
  outcome — every content section landed but the listing was never activated,
  and `warnings` says why. **Absent is not `False`**: the field is omitted
  when activation was never part of the operation.
- **Errors** — the error envelope gains `previous_code`.

### Changed
- `ListingPublishResponse` is now `ListingPublishBookingResponse` (the model
  behind `POST /v1/listings/{id}/publish/booking`); the old name is gone.

## [0.2.16] - 2026-09-22

Regenerated against the live `https://api.repull.dev/openapi.json`
(191 → 199 operations, none removed).

### Added
- **Inquiries** — `repull.api.conversations.list_inquiries` (`GET /v1/inquiries`;
  `status` defaults to `open`, pass `all` for every state).
- **Pre-approval** — `repull.api.conversations.preapprove_conversation`
  (`POST /v1/conversations/{id}/pre-approval`, optional `blockInstantBooking`).
- **Special offers** — `repull.api.conversations.create_conversation_special_offer`,
  `get_conversation_special_offer`, `withdraw_conversation_special_offer`
  (`POST`/`GET`/`DELETE /v1/conversations/{id}/special-offers[/{offerId}]`),
  plus `repull.api.airbnb.get_airbnb_offer` (`GET /v1/channels/airbnb/offers?offerId=`).
- **Booking requests** — `repull.api.reservations.accept_reservation_request`
  and `decline_reservation_request` (`POST /v1/reservations/{id}/accept|decline`).
- **Message attachments** — `SendMessageRequest.attachments` (list of
  `SendMessageAttachment`, 1–5 files by public `https://` URL) on
  `send_conversation_message`; the response carries `SentAttachment`s.
- **Webhooks** — `WebhookEventType` gains `reservation.request.created`,
  `reservation.request.updated`, `inquiry.created`, `inquiry.updated`, with
  models `ReservationRequestCreatedEvent`, `ReservationRequestUpdatedEvent`,
  `InquiryCreatedEvent`, `InquiryUpdatedEvent` and `InquiryWebhookObject`.
- `Reservation` gains `status_detail` (`request_expired`) and `respond_by`.
- Optional `idempotency_key` on `create_airbnb_offer` / `airbnb_reservation_action`,
  and `cursor` / `all_` on `list_airbnb_thread_messages`.

### Changed
- `repull.api.airbnb.airbnb_reservation_action` now takes a required
  `body: AirbnbReservationActionBody` — the spec declares the action body the
  API always required.

## [0.2.15] - 2026-09-18

Regenerated against the live `https://api.repull.dev/openapi.json`
(175 → 191 operations).

### Added
- **Airbnb listing content write surface** — 13 new operations under
  `repull.api.airbnb` for editing an Airbnb listing's canonical content
  directly:
  - `GET`/`PUT .../booking-settings` (`get_airbnb_booking_settings`,
    `update_airbnb_booking_settings`) — cancellation policy (including the
    non-refundable option and short-stay policy), booking mode, instant book,
    advance notice, preparation time, booking window, check-in/check-out
    windows. Models `GetAirbnbBookingSettingsResponse200` /
    `UpdateAirbnbBookingSettingsBody` and their nested
    `*Cancellation`/`*CheckIn`/`*CheckOut`/`*AdvanceNotice`/`*BookingWindow`/
    `*InstantBook`/`*PreparationTime` model families.
  - `GET`/`PUT .../details` (`get_airbnb_listing_details`,
    `update_airbnb_listing_details`) — property type, room type, quiet hours,
    check-in method. Models `AirbnbListingDetailsResponse`,
    `AirbnbListingDetailsWriteRequest` (+ `CheckInOption`,
    `PropertyTypeGroup`, `RoomTypeCategory`, `QuietHoursItem` variants).
  - `GET`/`PUT .../permits` (`list_airbnb_listing_permits`,
    `update_airbnb_listing_permits`) — `AirbnbPermitsResponse` /
    `AirbnbPermitsWriteRequest`.
  - `GET`/`PUT .../safety-disclosures` (`list_airbnb_listing_safety_disclosures`,
    `update_airbnb_listing_safety_disclosures`) — `AirbnbSafetyDisclosure`,
    `AirbnbSafetyDisclosureType`, `AirbnbSafetyDisclosuresResponse` /
    `AirbnbSafetyDisclosuresWriteRequest`.
  - `PATCH .../photos` (`update_airbnb_listing_photo`) — per-photo caption and
    category. `UpdateAirbnbListingPhotoBody` / `...Response200`.
  - `PUT .../photos/order` (`reorder_airbnb_listing_photos`) —
    `ReorderAirbnbListingPhotosBody` / `...Response200`.
  - `PUT .../photos/cover` (`set_airbnb_listing_cover_photo`) —
    `SetAirbnbListingCoverPhotoBody` / `...Response200`.
  - `PUT .../rooms` (`update_airbnb_listing_room`) — bed/room-amenity
    updates, sharing the `UpdateAirbnbListingRoomBody` model family with
    `CreateAirbnbListingRoomBody` (beds, metadata, room amenities, room type).
  - `PUT .../amenities` (`update_airbnb_listing_amenities`) —
    `UpdateAirbnbListingAmenitiesBody` (`amenities`,
    `accessibility_amenities`) / `...Response200`.
  - `PUT .../descriptions` (`update_airbnb_listing_description`) — per-locale
    description sections. `AirbnbDescriptionWriteRequest`.
- `POST /v1/channels/airbnb/alterations/{id}/cancel`
  (`cancel_airbnb_alteration`) — `CancelAirbnbAlterationBody`.
- `POST /v1/listings/{id}/pull/airbnb` (`pull_listing_from_airbnb`) — pulls
  the listing's current state back from Airbnb into Repull's canonical
  content. `ListingPullAirbnbRequest`, typed `ListingPullResponse`
  (`ListingPullResponseChannel`).
- `unlist` and `relist` actions on `AirbnbListingActionRequestAction`
  (existing `POST /v1/channels/airbnb/listings/{id}` action endpoint), plus
  an optional `Idempotency-Key` header parameter on that call. Its 200
  response is now a typed union — `AirbnbListingActionResponse200Type0`,
  `AirbnbListingActionResponse200Type1`, or `AirbnbListingLifecycleResponse`
  — replacing the previous untyped `Any`/`None`.
- `Listing.thumbnail_url` and `ListingContent.name` — `?include=thumbnail`
  on `GET /v1/listings` / `GET /v1/properties` now adds `thumbnailUrl` even
  to reduced inactive rows; `ListingContent.name` is the stored public title
  (as opposed to `.title`, which is only the `generate-content` proposal),
  and after `POST /v1/listings/{id}/pull/airbnb` reflects Airbnb's own title.
- `Reservation.check_in_time` / `.check_out_time` — local `HH:MM` stay terms
  (property timezone), usually inherited from listing policy and overridable
  per reservation. `ReservationWebhookObject.cancellation_policy` /
  `.check_in_time` / `.check_out_time` carry the same three stay-terms fields
  on `reservation.created`/`reservation.updated`/`reservation.cancelled`
  webhook deliveries (`cancellationPolicy`, `checkInTime`, `checkOutTime` on
  the wire) — verbatim from the source channel, `null` when the channel
  didn't supply them, never defaulted.
- `AirbnbAlteration` gains `account_id`, `account_name`,
  `new_listing_id`, `new_airbnb_listing_id` — an alteration can transfer the
  reservation to a different listing under the same or another connected
  account.
- New `ErrorError` fields for the `listing_not_api_connected` error code:
  `listing_id`, `airbnb_listing_id`, `sync_category`. New error codes
  declared across affected operations: `listing_not_api_connected`,
  `airbnb_rejected`, `connection_reauth_required`, `airbnb_rate_limited`
  (`403`/`422`/`429`), plus `502` on the Airbnb listing action endpoint.
- `idempotency_key` parameter (sent as the `Idempotency-Key` header) on
  `publish_listing_to_airbnb` and `airbnb_listing_action`.
- `ConnectStatus`/`AirbnbDataFreshness` gain per-account scoping —
  `dataFreshness.accounts[]` (`AirbnbAccountFreshness`) and an `?account_id=`
  query parameter, letting a workspace with multiple connected Airbnb
  accounts scope reads to one of them.
- `select_connect_provider` docs now correctly reference the wire field
  `allowedProviders` (was documented as `allowed_providers`; no code change).

### Changed
- **Publish result is now fully typed.** `publish_listing_to_airbnb`'s 200
  response model is renamed `ListingPublishResponse` →
  `ListingPublishAirbnbResponse` and gains `result.lockedFields` — fields
  Airbnb refuses to change for this listing (200 response, nothing applied).
  A `404` response was also added. See the expanded docstring on
  `publish_listing_to_airbnb` for the per-section publish/retry semantics.
- `create_airbnb_alteration`'s request body model is renamed
  `CreateAirbnbAlterationBody` → `AirbnbAlterationCreateRequest`, and its
  `201` response is now a typed `AirbnbAlteration` object (was untyped
  `Any`/`None`). `422` and `429` error responses were also added.
- `list_listings`/`list_properties` `?include=` gains the `thumbnail` value
  (combinable, e.g. `?include=content,thumbnail`).

### BREAKING
- `repull.models.CreateAirbnbAlterationBody` no longer exists — use the
  renamed `repull.models.AirbnbAlterationCreateRequest`.
- `repull.models.ListingPublishResponse` no longer exists — use the renamed
  `repull.models.ListingPublishAirbnbResponse`.

These renames are generator-introduced by upstream OpenAPI schema-name
changes (both operations' response semantics also changed, which is why the
schemas were renamed rather than kept binary-compatible); update any code
that imports these model classes by name.

## [0.2.14] - 2026-09-15

Regenerated against the live `https://api.repull.dev/openapi.json`
(174 → 175 operations).

### Added
- `POST /v1/listings/status` (`set_listings_status`) —
  `repull.api.listings.set_listings_status`. Activate or deactivate up to 500
  listings in one all-or-nothing call. New models `ListingStatusBatchRequest`
  (`listing_ids`, `active`) and `ListingStatusBatchResponse`
  (`active`, `updated`, `unchanged`).
- `DELETE /v1/connect/{provider}` (`delete_connection`) gains an optional
  `account_id` argument (sent as the `accountId` query param) — required when a
  workspace has more than one account for the provider — and a typed response,
  `DeleteConnectionResponse200` (`disconnected`, `provider`, `account_id`,
  `listings_deactivated`). The account's listings are deactivated, not deleted.
- `ConnectStatus.accounts` (`ConnectStatusAccountsItem`) on
  `GET /v1/connect/{provider}` — every Airbnb account the workspace has connected.
- New `403 listing_inactive` error response, declared on 83 operations.
- Airbnb calendar operations gain `busy_subtype`
  (`AirbnbCalendarOperationBusySubtype`); `AirbnbPricingWriteRequest.model_type`
  is now an enum.

### Changed
- Lists default to active listings: `GET /v1/listings` accepts
  `status=active|inactive|archived|all` and `GET /v1/properties` accepts
  `status=active|inactive|all`. Inactive rows carry identity fields only, and
  reading or writing an inactive listing returns `403 listing_inactive`.
- Airbnb calendar writes (`PUT .../pricing`, `PUT .../availability`) validate
  more strictly (unknown fields such as `price` are refused with
  `422 invalid_params`) and declare new errors: `422 airbnb_rejected`,
  `403 connection_reauth_required`, `429 airbnb_rate_limited`.
- Sending `accessType` to `POST /v1/connect/airbnb` now locks the consent
  screen to that tier; omit it to let the host choose.

### Deprecated
- Booking.com webhooks endpoints (`GET`/`POST`/`DELETE
  /v1/channels/booking/webhooks`) are deprecated and always return `403`.

## [0.2.13] - 2026-09-11

### Fixed
- Regenerated against the live `https://api.repull.dev/openapi.json` to pick up
  19 schema corrections merged into the spec. Path/operation inventory is
  unchanged (124 paths / 174 operations) — only response *shapes* changed:
  - Ten fields renamed from snake_case to camelCase on the wire:
    `data_freshness`→`dataFreshness`, `last_synced_at`→`lastSyncedAt`,
    `fix_url`→`fixUrl`, `next_cursor`→`nextCursor`, `has_more`→`hasMore`,
    `monthly_requests`→`monthlyRequests`, `daily_ai_requests`→`dailyAiRequests`,
    `daily_ai`→`dailyAi`, `dynamic_pricing_listings`→`dynamicPricingListings`,
    `resets_at`→`resetsAt`. Generated model attributes keep their Pythonic
    snake_case names (e.g. `AirbnbDataFreshness.last_synced_at`); only the
    `to_dict`/`from_dict` JSON keys changed to camelCase.
  - Three list endpoints now return bare arrays instead of `{data, pagination}`
    envelopes: `list_booking_properties` (`GET /v1/channels/booking/properties`),
    `list_booking_conversations` (`GET /v1/channels/booking/conversations`), and
    `list_vrbo_listings` (`GET /v1/channels/vrbo/listings`) now return
    `list[BookingProperty]` / `list[BookingConversation]` / `list[VrboListing]`
    directly. The wrapper models `BookingPropertyListResponse`,
    `BookingConversationListResponse`, and `VrboListingListResponse` are removed.
  - Four id fields changed integer→string: `AirbnbAlteration.id`,
    `AirbnbAlteration.reservation_id`, `AirbnbConnection.id`,
    `AirbnbListing.listing_id`.
  - `Property.latitude` and `Property.longitude` changed number→string.

## [0.2.12] - 2026-09-11

### Added
- Regenerated against the live `https://api.repull.dev/openapi.json` (124 paths,
  170 → 174 operations). Four new write operations are now reachable:
  - `POST /v1/guests` (`create_guest`) — `repull.api.guests.create_guest`
  - `POST /v1/reservations` (`create_reservation`) — `repull.api.reservations.create_reservation`
  - `PATCH /v1/reservations/{id}` (`update_reservation`) — `repull.api.reservations.update_reservation`
  - `POST /v1/conversations/{id}/messages` (`send_conversation_message`) — `repull.api.conversations.send_conversation_message`
  Corresponding request/response models added: `GuestCreateRequest`/`GuestCreateResponse`,
  `ReservationCreateRequest`/`ReservationCreateResponse` (+ `ReservationGuestInput`,
  `ReservationCreateRequestPlatform`), `ReservationUpdateRequest`/`ReservationUpdateResponse`,
  `SendMessageRequest`/`SendMessageResponse` (+ `SendMessageRequestChannel`,
  `SendMessageResponseDirection`).

## [0.2.11] - 2026-09-11

### Added
- Regenerated against the live `https://api.repull.dev/openapi.json` (102 → 124
  paths). 24 previously-missing operations are now reachable, including
  `PATCH /v1/availability/batch`, Airbnb alteration accept/decline, Booking.com
  room listing, credentials-based Connect flows for Beds24/BookingSync/Guesty/
  Hospitable/Hostaway/iGMS/Lodgify/OwnerRez/Smoobu/VRBO, per-channel health
  checks (`/v1/health/atlas`, `/v1/health/auth`, `/v1/health/channels/{channel}`,
  `/v1/health/mcp`, `/v1/health/webhooks`), listing photo upload/list, `GET
  /v1/quotes`, and channel-neutral review replies.
- Note: `POST /v1/reviews/{id}/reply` is present in the spec's `paths` but the
  operation itself does not generate a client function — the live spec is
  missing the `id` path-parameter declaration for that operation, which trips
  `openapi-python-client`'s path-templating check. Upstream fix needed in
  `api.repull.dev`'s OpenAPI generation; use `POST /v1/channels/booking/reviews`
  (`reply_booking_review`) or the Airbnb review-response endpoints in the
  meantime.

### Removed
- Sandbox support end-to-end: the live API deleted the sandbox entirely
  (`/v1/sandbox/reset` and `/v1/sandbox/seed` now 404, `sk_test_*` keys now
  401). Dropped the generated `repull.api.sandbox` module and its models
  (`SandboxSeedResult`, `SandboxResetResult`, `SandboxFixtureRef`,
  `SandboxResetResultDeleted`), and removed the `sk_test_*` sandbox-key
  mention from the README's auth section.

## [0.2.6] - 2026-06-25

### Added
- Booking.com hosted connect flow on `POST /v1/connect/{provider}` (`provider=booking`):
  pass `redirectUrl` to get back a hosted `url`/`sessionId`/`expiresAt`, then drive
  the room-mapping surface via `GET /v1/connect/booking/rooms`,
  `POST /v1/connect/booking/map-rooms`, and `POST /v1/connect/booking/verify`.
- `GET /v1/properties` now accepts a `channel` filter (`ListPropertiesChannel`:
  `airbnb` / `booking` / `vrbo`) to list only properties published on a given OTA.
- `Property.channels` (`list[str]`) — the OTAs/channels a property is actively
  published on (e.g. `["airbnb", "booking"]`); empty when none.

Regenerated against the live `https://api.repull.dev/openapi.json`.

## [0.2.5] - 2026-06-24

### Added
- Add `messaging` Airbnb Connect access scope (read + send guest messages, no
  property management). `CreateConnectionBodyAccessType.MESSAGING` now joins
  `READ_ONLY` and `FULL_ACCESS` on `POST /v1/connect/{provider}`. Regenerated
  against the live `https://api.repull.dev/openapi.json`.

## [0.2.2] - 2026-05-07

### Added
- Regen against latest `https://api.repull.dev/openapi.json`.
- `GET /v1/listings/{id}` and `GET /v1/properties/{id}` accept the new
  `?include=amenities` query param (`GetListingInclude.AMENITIES` /
  `GetPropertyInclude.AMENITIES`). When passed, responses include an
  `amenities[]` array of `ListingAmenity` rows.
- New Airbnb connection + KV operations surfaced by the spec.

Refs: vanio-repull-api #59, #61.

## [0.2.0] - 2026-05-03

First public release on PyPI: <https://pypi.org/project/repull-sdk/>.

### Distribution rename — `repull` → `repull-sdk` (PyPI name only)
PyPI's name-collision filter blocked the bare `repull` distribution
name, so the package was renamed to `repull-sdk` to ship publicly.

Install with:

```
pip install repull-sdk
```

The **Python module / import path is unchanged** — keep using:

```python
import repull
from repull import AuthenticatedClient
```

Only the distribution name on PyPI (and in `pyproject.toml`) changed.
Imports, attributes, and APIs are identical to the source tree.

### Wire-format / API changes (carried over from the 0.2.0 cut)

Major bump — multiple breaking wire-format changes since `0.1.3`. This release
re-cuts the client against the canonical `api.repull.dev` spec where every
list/read endpoint returns the same envelope, every field name is camelCase,
and every entity ID is a string.

### Changed (BREAKING)
- **Canonical pagination envelope.** All paginated list endpoints now return
  `{ "data": [...], "pagination": { "nextCursor", "hasMore", "total"? } }`.
  Use `response.pagination.next_cursor` (still `nextCursor` on the wire) and
  stop when `pagination.has_more` is `False`. The `total` field is present
  when `?include_total=true` (default on most endpoints).
- **All wire field names are camelCase.** Every previously snake_case JSON
  key has flipped (`property_id` → `propertyId`, `guest_id` → `guestId`,
  `created_at` → `createdAt`, etc.). Python attribute names remain
  snake_case per PEP 8 — the `to_dict`/`from_dict` mappers handle the
  conversion. If you were calling `to_dict()` and reading raw keys, rename
  your accesses.
- **All entity IDs are strings.** `Listing.id`, `Property.id`, `Guest.id`,
  `Reservation.id`, and every foreign-key field are now `str`. Previously
  some were typed as `int`. Update your storage, comparisons, and URL
  builders accordingly. Anything that did `int(reservation.id)` will break.
- **`POST /v1/connect/airbnb` response field renamed.** `oauthUrl` → `url`.
  The hosted-OAuth response now exposes the redirect target as
  `response.url`.
- **`GET /v1/markets` response shape.** `markets` → `data`;
  `total_in_filter` → `total`. Now matches the canonical envelope.
- **`GET /v1/reviews/{id}` returns the bare `Review`.** Previously wrapped
  in `{ "data": Review }` — now the response IS a `Review`. Drop the
  `.data` access.
- **`/v1/channels/airbnb/*` list responses now wrap in
  `{ data, pagination }`.** Previously returned raw arrays. Update
  iteration code from `for item in response` to `for item in response.data`.

### Added
- **Self-documenting error envelope.** Errors now include `fix`, `docs_url`,
  `request_id`, and `field` (when applicable) alongside `code` and
  `message`. Log `error.request_id` when filing support tickets and surface
  `error.fix` to your users.
- **Rate-limit headers + first-class 429 handling.** Every read endpoint
  emits `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and
  `X-RateLimit-Reset`; over-limit requests return a structured `429`
  response. Back off using `Reset`.
- **`X-Schema` header on all read endpoints.** Pass an alternate schema
  name (registered via the schema CRUD endpoints) to receive payloads in
  your own field shape — useful for legacy mappers and CMSes that expect a
  specific JSON layout.
- **Schema CRUD endpoints.** `repull.api.schema` exposes
  `createCustomSchema`, `listCustomSchemas`, `getCustomSchema`,
  `updateCustomSchema`, `deleteCustomSchema` plus matching model classes
  — register custom response shapes once, request them via `X-Schema`
  everywhere.
- **`GET /v1/listings/{id}` and `GET /v1/reservations/{id}`.** Single-entity
  reads on listings and reservations (previously list-only).
- **`?include_total=true` opt-in.** Default-on for most endpoints; pass
  `include_total=False` on very large workspaces to skip the `COUNT(*)`.
- **`pagination.total` field.** Returned when `include_total` is on.
- **`sk_test_*` / `sk_live_*` API key prefix format** (additive — the raw
  token is unchanged on the wire; clients that just pass the value through
  as a Bearer token continue to work).
- **Strict query-param validation.** Unknown query params now `400` instead
  of being silently ignored. Typos in pagination/filter args surface
  immediately rather than returning the wrong page.

### Notes
- `openapi-python-client` keeps Python attribute names snake_case while
  serializing to camelCase JSON — your code stays idiomatic Python; the
  SDK handles the wire mapping. The breaking change is in **wire format**,
  not in attribute access (with the exception of fields/types that
  genuinely changed shape, listed above).

## [0.1.3] - 2026-05-02

### Changed
- Re-cut from `main` HEAD with the lint fix included; functionally identical
  to `0.1.2` (no API changes). The `0.1.2` tag was cut from a SHA that
  predated the ruff lint fix on the connect example, so its release
  workflow would have failed at the `ruff check` step before reaching the
  publish stage.

## [0.1.2] - 2026-05-02

### Added
- Custom-schema CRUD endpoints under `repull.api.schema` (`createCustomSchema`,
  `listCustomSchemas`, `getCustomSchema`, `updateCustomSchema`,
  `deleteCustomSchema`) plus `CustomSchema*` model classes.
- `X-Schema` header parameter on all 10 read endpoints (`listReservations`,
  `getReservation`, `listGuests`, `getGuest`, `listConversations`,
  `getConversation`, `listConversationMessages`, `listReviews`, `getReview`,
  `listListings`) so callers can request alternate response shapes.

### Changed
- **Breaking:** `Reservation` payload field names now match the API: `propertyId`
  → `listingId`, `guestFirstName`/`guestLastName` → `guestId` +
  `guestDetails` + `guestName`. Earlier `0.1.x` types misrepresented the wire
  shape; consumers who coded against the old names must rename their
  attribute accesses.

## [0.1.1] - 2026-05-01

### Added
- Conversations, guests, and reviews resource modules.
- Cursor-paginated `listReservations` operation.

## [0.1.0] - 2026-05-01

### Added
- Initial generated client from `https://api.repull.dev/openapi.json`.
