# Changelog

All notable changes to the `repull` Python SDK are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
