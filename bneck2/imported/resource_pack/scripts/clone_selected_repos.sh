#!/usr/bin/env bash
set -euo pipefail
mkdir -p third_party && cd third_party
# Review every current license before reusing code commercially.
repos=(
  https://github.com/Beltran12138/ai-release-radar.git
  https://github.com/Beltran12138/prophetmap.git
  https://github.com/Skeeter-spec/keystone.git
  https://github.com/atharvahirulkar/chokepoint.git
  https://github.com/meelod/arxiv-trend-radar.git
  https://github.com/unicodeveloper/tech-scouting-agent.git
  https://github.com/pmxt-dev/pmxt.git
  https://github.com/Jon-Becker/prediction-market-analysis.git
  https://github.com/dgunning/edgartools.git
  https://github.com/getzep/graphiti.git
)
for r in "${repos[@]}"; do git clone --depth 1 "$r" || true; done
