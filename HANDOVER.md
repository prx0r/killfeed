# Handover — agent-vault + pogtown + freaktown (2026-09-08)

Single entry point for everything built, migrated, and verified this session
on `vps-e94d5dea` (Ubuntu 24.04, user `ubuntu`). Secrets are referenced by
location, never printed here.

---

## 1. agent-vault (Infisical, most-starred pick)

- **Why this one**: `Infisical/agent-vault` (2,197★) vs alternatives (4★ and below).
- **Binary**: `/usr/local/bin/agent-vault`, v0.39.3 (`agent-vault version`).
- **OpenCode wiring** (not an `opencode.json` MCP entry — it's a proxy wrapper):
  `agent-vault run -- opencode` (injects `HTTPS_PROXY`/`HTTP_PROXY` + CA trust;
  installs `~/.opencode/skills/agent-vault-cli/SKILL.md` on first run).
  Docs: https://docs.agent-vault.dev/quickstart/opencode.md
- **Server**: passwordless, `127.0.0.1:14321`, DB `~/.agent-vault/agent-vault.db`,
  systemd user service `~/.config/systemd/user/agent-vault.service` (enabled +
  linger; restarts need no password). Logs: `~/.agent-vault/server.log`.
- **Owner**: `admin@local` — password in `~/.agent-vault-owner-pass` (0600).
  Session: `~/.agent-vault/session.json` (1yr/30d idle).
- **Unattended agent token** (`oracle+main+default:proxy`, long-lived):
  `~/.agent-vault-opencode-token` (0600). First token was exposed in logs and
  **rotated** — old one revoked.
  Usage: `AGENT_VAULT_TOKEN="$(cat ~/.agent-vault-opencode-token)" AGENT_VAULT_ADDR=http://127.0.0.1:14321 AGENT_VAULT_VAULT=oracle agent-vault run -- <cmd>`
- **Vaults (verified live: 43 + 1)**:
  `agent-vault vault credential list --vault oracle` (43: Gmail, Cloudflare/R2,
  Google, GitHub, Name.com, Moltbook, Metaculus, Kaggle, SerpAPI, YouTube,
  AgentPact, Hermes, GetX, DealWork, OpenCode, Merchant…) and
  `--vault main` (1: `HF_TOKEN`).
- **Migration trail**: old-box `/root/vault-export.json` + `vault-import.sh`
  fetched via 2-hour R2 presigned links; all 44 imported `OK`;
  `/root/vault-export.json` shredded (`/root/vault-import.sh` kept, 0600).
  R2 handoff objects still need deleting at source (links expired by now).

## 2. Gmail + pogtown ZIP (via vaulted Gmail OAuth)

- Gmail `tradesprior@gmail.com` — token minted from vaulted
  `GMAIL_CLIENT_ID/SECRET + GMAIL_REFRESH_TOKEN` (scope `mail.google.com`).
- Search `pogtown` → 2 mails: sent 90KB mail with
  `pogtown-mvp-2026-09-09.zip` + `.sha256`, plus Gmail's executable-block bounce.
- Extracted to `~/pogtown/` — **sha256 verified `53aa4cbf…`** — 126 files,
  unzipped at `~/pogtown/pogtown-mvp/`. (Temp Gmail access token shredded.)

## 3. pogtown-mvp — P0 productionization (`~/pogtown/pogtown-mvp/`)

Base: Node 22 installed (was missing); baseline was 5/5 green. Now **60/60**.

- **Durable store** (`services/api/store.mjs`): memory / file (`room.json` +
  append-only `events.jsonl`, default `./data`, gitignored) / Postgres
  (`pg` loaded only when `POG_STORE=postgres`; migrations `001_core.sql`,
  `002_p0_ttl_idempotency.sql`). `PogRuntime.importReplay` rehydrates byte-identical.
- **API** (`services/api/server.mjs`, reports `0.2.0-p0`): rooms CRUD, join,
  observe, action, replay, `GET events` (JSON + live SSE w/ cursor +
  `Last-Event-ID`), invites (`POST invites`, `join-with-invite`, HMAC +
  expiry + room binding), agent bearer tokens + Nakama header passthrough,
  `Idempotency-Key`, per-IP token bucket (429), TTL sweeper, `/health` with
  version/store/uptime, `POST /v1/rooms/import`, `GET clips`, full `/v1/freaks`
  flow (below).
- **Proven live**: create → invite joins → react → kill → cold restart →
  identical replay; SSE live push; idempotent re-join; TTL→404; burst→429→recovery.

## 4. freaktown × pogtown integration (`~/freaktown` cloned, untouched tracked files)

- Deep survey via 3 parallel passes (backend/contracts, stage/TS, tests/Ella).
- `docs/FREAKTOWN-LINK.md`: field-by-field contract map + known divergences
  (mafia rules) + remaining `apps/live` debt.
- Delivered: golden-freak treaty test (vendored fixture), bundle→replay
  importer (measured-time, deterministic), Ella rubric + judge firewall
  (`POG_ELLA_RUBRIC=1` enforced; **fixed a real bug** where a typo silently
  disabled enforcement), dual-engine mafia firewall test (Node + Python probe),
  pog→show stage adapter (private grants never cross), canonical TS
  `contracts/show.ts` (+ edge re-export, parity-tested both ways),
  freaktionary scoring in pictionary + new `roast-relay` pack, shared
  compose (`freaktown:8090`) + Caddy (`show.pog.town`).
- Freaktown suite here: 69 passed; 13 pre-existing env failures (no
  `livekit`/`espeak`/avatar deps). `git status`: only 2 new untracked TS files
  + `docs/PRELAUNCH-HARDENING.md`.

## 5. P1 standup loop (this session)

- **Freak creation API**: draft → premise/roll/lock/reroll → portrait →
  voice (`vault://` refs enforced) → delivery (beat/offset parity) → Blue Room
  rehearsal (real room) → sealed submit (sha256, rehearsal required, immutable).
- **Exact-digest consumption**: submit digest == replay `set.started` digest
  (live-verified + healthcheck-gated). **Clip metadata**: 16:9/9:16/best-clip/
  score-reveal/captions/thumbnail from sealed times (renderers execute).
- **Transcripts/words**: measured per-beat splits on import, proportional on
  live finish; **director cuts** (`WIDE/MEDIUM/CLOSE/REACTION/ELLA`) as events.
- **Quality gates**: automated HTTP e2e (ephemeral servers, incl. freak seal
  flow), TTL/rate-limit HTTP tests, zero-dep audit (`scripts/audit-deps.mjs`),
  web client extended (roast line/vote, pictionary guess, scores).
- Docs: `README` API catalog, `docs/P0-NOTES.md`, `docs/P1-NOTES.md`,
  `docs/TEST-REPORT.md` appended. CI: tests + validate + audit + caddy +
  healthcheck; cross-engine tests get freaktown via `FREAKTOWN_DIR`.

## 6. freak.town review + edge audit

- **Review**: TLS valid, 0.4s, healthy API (`build 4722b9f`), 20 published
  sets, watch URLs 200, full studio surface, PWA flags. Nits: no HTTP→HTTPS
  redirect, no HSTS/security headers, pogtown hosts undeployed.
- **Cloudflare audit (read-only, token from oracle vault)**: confirmed
  `always_use_https off`, HSTS disabled, min TLS 1.0; origin is a Tunnel (good),
  Zoho mail correct; **pog.town is not in this account**.
- Fixes staged (NOT applied — prod edge): `~/freaktown/docs/PRELAUNCH-HARDENING.md`
  with exact API calls + verify steps. Approve to apply P0 items 1–3.

## 7. Quick commands

```bash
export AGENT_VAULT_ADDR="http://127.0.0.1:14321"
agent-vault vault credential list --vault oracle   # 43 keys, no values
agent-vault vault credential get GMAIL_ADDRESS --vault oracle
cd ~/pogtown/pogtown-mvp && npm test               # 60/60
npm run validate && node scripts/audit-deps.mjs && node scripts/verify-caddy.mjs
POG_DATA_DIR=/tmp/x POG_API_PORT=8787 node services/api/server.mjs &
node scripts/healthcheck.mjs
```

## 8. Known non-goals / needs-hardware

Docker builds, Postgres-live, Nakama TS build, LiveKit/Qwen/Stable Audio,
Audio2Face, Unreal, Expo, media generation/rendering, R2 asset hosting,
scheduled encrypted DB backups + restore drill, Cloudflare P0 edge fixes
(staged, awaiting approval), R2 handoff object deletion at source.
