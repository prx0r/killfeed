# Forecasting organism — quantitative role per source (2026-09-10)

Each stream as an organ: latency (how fast it moves after reality),
horizon (how far ahead it sees), reliability profile, and MEASURED
lead-lag where we have it (NVDA 17-week panel, E021–E024) vs priors
where we don't. Numbers beat adjectives; priors are labelled.

## Measured lead-lag (real data, directional n≈13–14)

| Pair | Peak | Reading |
|---|---|---|
| SEC filings → NVDA returns | lag +4w, r=-0.32 (E021 CONFIRMED) | filings lead, NEGATIVELY — filing bursts mark tops to fade, not entries |
| HN chatter → NVDA returns | lag -3w, r=+0.69 (E022: price leads) | narrative FOLLOWS price by ~3 weeks — chatter is an echo, not a signal |
| SEC vs HN | lag -4w, r=+0.75 (E023: HN leads filings) | chatter precedes filings — rumors/news circulate weeks before Form 4s land |

Chain (directional): **event → price moves fast → HN echoes +3w →
filings cluster +4w after chatter**. Insiders file into strength (E018:
heavy-sell months +3.4%). The naive "insiders know first" story is
backwards here: most filings are sales, sales follow rallies.

## Per-source quantitative theses

- **Prices (Yahoo/CoinGecko)**: latency 0 (reality itself), horizon 0.
  Fastest stream by construction. Role: ground truth + target. E022 proves
  even HN lags it 3 weeks.
- **Prediction markets**: latency minutes–hours (money reprices on news),
  horizon = event date (days–years), reliability = liquidity tier
  (high 0.82 / mid 0.60 / low 0.50). Role: fastest BELIEF readout; use as
  early signal for slower streams, never as long-horizon truth (thin books
  mean-revert; resolved linger). H-LEAD-4 preregistered: PM leads X by days.
- **Whale wallets**: latency days (positions accumulate), horizon weeks.
  Role: conviction filter on PM reads (E004: 2/3). Correlation with PM
  direction expected — independence must be checked, not assumed.
- **SEC filings**: latency weeks (file after trade), horizon negative
  (mark tops). Role: regime attention + fade signal (E021), NOT entry.
  Burst = "something is happening", direction from price context.
- **HN narrative**: latency +3w BEHIND price, horizon 0. Role: saturation
  gauge (crowdedness cross-check), never a leading signal. High heat +
  high crowdedness = WATCH.
- **OpenAlex research**: latency years, horizon years. Role: slow attack
  clock (technological pressure), useless for timing, essential for
  direction. Never trade the print; trade the migration it implies.
- **Insider buys (OpenInsider)**: latency days, horizon months. Role:
  highest-conviction single primitive (own-money buys). NVDA: zero buys
  in 100 rows — absence noted, not filled.
- **FINRA short flow**: latency T+1 day, horizon weeks. Role: positioning
  gauge (squeeze fuel vs informed exit) — read WITH crowdedness.
- **HN/HF/GitHub implementation**: latency weeks–months. Role: diffusion
  stage tracker (talk→build→deploy); stage mismatches are the signal.
- **Lab RSS/hiring**: latency weeks (posts) / quarters (hiring). Role:
  capability direction + slow revealed preference. Never trade the post.
- **Permissions (FedRegister/FDA/trials/House)**: latency months,
  horizon years. Role: deployment clock — gates cash-flow timing (third
  clock), not direction.
- **Macro (BLS/Treasury/WorldBank)**: latency quarters, horizon years.
  Role: anchors for duration math, never signals.
- **X (planned)**: predicted latency days (between PM-minutes and HN-weeks),
  predicted role: primary-source corpus for corroboration + falsification
  attempts in replies. Test on keying (H-LEAD-4).

## Organism order (fast → slow)

prices ≈ PM books > whale flow > SEC filings > HN echo > HF/GH building >
lab posts > hiring > OpenAlex years > permissions years > macro.

Trade the fast streams for timing, the slow streams for direction, and
never invert the two. The most expensive mistake in this stack would be
trading HN chatter as if it led (it lags 3 weeks, r=0.69) or buying
filing bursts as if they were entries (they mark +3.4% tops).
