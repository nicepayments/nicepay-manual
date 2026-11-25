#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

rm -rf .build
mkdir -p .build/docs
cp -R api common management migration image .build/docs/
cp README.md .build/docs/quickstart.md
cp site-src/index.md .build/docs/index.md
cp -R site-src/assets .build/docs/
python3 site-src/diagrams/render.py .build/diagrams > /dev/null
for svg in .build/diagrams/*.svg; do
  if ! cmp -s "$svg" "image/$(basename "$svg")"; then
    echo "image/$(basename "$svg") is out of date. Run: python3 site-src/diagrams/render.py image" >&2
    exit 1
  fi
done
python3 site-src/diagrams/render.py .build/docs/image/dark dark > /dev/null
mkdir -p .build/docs/reference
cp site-src/reference/index.html .build/docs/reference/index.html
python3 site-src/openapi/convert.py .build/docs/reference/openapi.json > /dev/null

mkdocs build "$@"
