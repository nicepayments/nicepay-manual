#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

rm -rf .build
mkdir -p .build/docs
cp -R README.md api common management migration image .build/docs/
cp -R site-src/assets .build/docs/

mkdocs build "$@"
