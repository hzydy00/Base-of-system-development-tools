#!/usr/bin/env bash
set -euo pipefail

{
  echo "# Package Report"
  echo ""
  echo "| name | version | downloads |"
  echo "|---|---|---|"
  curl -fsS http://127.0.0.1:8000/packages.json \
    | jq -r '[.[] | select(.status == "active" and .downloads >= 100)]
             | sort_by(-.downloads, .name)
             | .[] | "| \(.name) | \(.version) | \(.downloads) |"'
} > summary.md
