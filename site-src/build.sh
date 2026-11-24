#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

rm -rf .build
mkdir -p .build/docs
cp -R api common management migration image .build/docs/
cp README.md .build/docs/quickstart.md
cp site-src/index.md .build/docs/index.md
cp -R site-src/assets .build/docs/

mkdocs build "$@"
