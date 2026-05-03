# Changelog

All notable changes to the `repull` Python SDK are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-05-02

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
