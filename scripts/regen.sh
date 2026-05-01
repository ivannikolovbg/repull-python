#!/usr/bin/env bash
# Regenerate the Repull Python client from the live OpenAPI spec.
#
# Usage:
#   ./scripts/regen.sh                # fetch fresh from https://api.repull.dev/openapi.json
#   ./scripts/regen.sh --offline      # use the snapshot in openapi/v1.json
#
# Requires: openapi-python-client (install via `uv tool install openapi-python-client`
#           or `pipx install openapi-python-client`).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SPEC_URL="${REPULL_OPENAPI_URL:-https://api.repull.dev/openapi.json}"
SPEC_PATH="$REPO_ROOT/openapi/v1.json"

mode="online"
if [[ "${1:-}" == "--offline" ]]; then
  mode="offline"
fi

if [[ "$mode" == "online" ]]; then
  echo ">>> Fetching $SPEC_URL"
  curl -fsSL "$SPEC_URL" -o "$SPEC_PATH.tmp"
  mv "$SPEC_PATH.tmp" "$SPEC_PATH"
  echo ">>> Snapshotted to $SPEC_PATH"
else
  echo ">>> Using offline snapshot $SPEC_PATH"
fi

if ! command -v openapi-python-client >/dev/null 2>&1; then
  echo "openapi-python-client not found. Install with one of:" >&2
  echo "  uv tool install openapi-python-client" >&2
  echo "  pipx install openapi-python-client" >&2
  exit 1
fi

TMP_OUT="$(mktemp -d)"
trap 'rm -rf "$TMP_OUT"' EXIT

echo ">>> Generating client into $TMP_OUT"
openapi-python-client generate \
  --path "$SPEC_PATH" \
  --output-path "$TMP_OUT/repull" \
  --meta none \
  --overwrite

echo ">>> Replacing src/repull"
rm -rf "$REPO_ROOT/src/repull"
mv "$TMP_OUT/repull" "$REPO_ROOT/src/repull"

echo ">>> Done. Inspect with: git diff src/repull"
