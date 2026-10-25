# robloxdumper

Auto-fetcher for Roblox Windows offsets. Pulls the latest (or pinned) verified offsets from the public
[rbxoffsets.com](https://rbxoffsets.com) API and stores them per-build, plus a converter that regenerates
an `offsets.h` in the armedium style.

## Usage

```bash
# Fetch latest verified offsets
python fetch_offsets.py

# Fetch a specific build
python fetch_offsets.py --version version-9ac8595712b447a7

# Regenerate armedium-style offsets.h from a fetched dump
python convert_to_armedium.py --version version-9ac8595712b447a7
```

## Auto-update

A GitHub Actions workflow (`.github/workflows/update.yml`) runs daily, fetches the latest build, and commits
new offset sets. Maintained by the owner; PRs welcome.

## Layout

```
offsets/<build>/offsets.hpp   # raw dump from rbxoffsets.com
offsets/<build>/offsets.json
converted/<build>/offsets.h   # armedium-style header
```
