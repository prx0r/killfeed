nice ok yeah do it i need 5 min updated pricing I think the thesis is getting sharper:

**NVIDIA probably eats a huge amount of the *compute orchestration* layer, but it cannot eat the physical bottlenecks underneath it.** And those bottlenecks are where I would hunt now.

### 1. Does NVIDIA eat Bittensor/Acurast?

Potentially part of them, yes.

Bittensor itself is not anti-NVIDIA. A lot of its actual compute economy is already effectively **NVIDIA monetization with TAO incentives wrapped around it**. ComputeHorde currently supports A6000-class NVIDIA GPUs and plans broader classes; other Bittensor subnets explicitly recommend things like A100s, A5000s and RTX 4090s. ([GitHub][1])

So today the flow is frequently:

**TAO demand → subnet miners → rent/buy NVIDIA GPUs → CUDA.**

NVIDIA wins regardless.

PAIR makes this even more threatening because NVIDIA has now built the basic local swarm scheduler itself:

**RTX PC + Mac + DGX Spark → automatic model-aware routing → one personal inference endpoint.** ([NVIDIA Developer][2])

The obvious future extensions are:

```text
PAIR 2026
home LAN
   ↓
PAIR 2027/28?
trusted friends / office / WAN
   ↓
unused compute pricing
   ↓
NVIDIA Compute Marketplace
   ↓
automatic billing
```

At that point Acurast's “rent my idle hardware” concept gets very uncomfortable.

But **Bittensor has one escape hatch:** Bittensor isn't really a scheduler. It's a mechanism for creating competitive markets around arbitrary machine intelligence/services. Compute is only one commodity.

So I currently see:

**Acurast vs NVIDIA: significant existential overlap**

**Bittensor vs NVIDIA: more complementary**

NVIDIA might become the hardware/runtime underneath Bittensor rather than replace TAO.

---

# 2. Minima is more interesting after checking the Ethereum direction

I think what you heard was probably Ethereum/Vitalik's recent **computing self-sovereignty** push.

Ethereum's own current roadmap explicitly says nodes should become sufficiently modest that they can run on:

> mobile phones, micro-computers or unobtrusively on a home computer.

The reason given is precisely that people should cryptographically verify information themselves instead of trusting centralized infrastructure. ([ethereum.org][3])

Ethereum's privacy roadmap now separately calls for **private proving on consumer-grade hardware**. ([ethereum.org][4])

And the Foundation is funding work on local/on-prem multi-GPU proving specifically to reduce cloud dependency. ([Ethereum Foundation Blog][5])

Even Ethereum's March 2026 mandate frames one of its goals as **self-sovereign computation**—users retaining control over their data, identities, agents and computation. ([ethereum.org][6])

That is almost exactly the philosophical substrate of your idea.

## And Minima has something genuinely non-bullshit here

I found independent confirmation beyond Minima's marketing.

University of Southampton + Siemens Cre8Ventures + Minima actually flew an autonomous drone with a Minima full node embedded in constrained hardware. Southampton reports roughly **500× memory-efficiency improvement** and up to **10,000% improvement in core verification performance** after hardware optimization. ([University of Southampton][7])

Siemens describes the exact problem as:

**“How do machines prove what they did?”**

and says Minima demonstrated a full L1 node on ARM-based FPGA hardware, offline-capable, with embedded verification. The next phase is explicitly exploring a blockchain-enabled SoC. ([Siemens Blog Network][8])

Arm separately confirms Minima is using Arm Flexible Access to develop a blockchain-enabled custom SoC. ([Arm Newsroom][9])

So:

### Minima technology: much more legitimate than the market cap implies.

But:

### MINIMA token value capture: still completely unproven.

It's roughly a **$3M market cap** with only about **$7K/day trading volume** right now. ([CoinGecko][10])

That's absurdly tiny.

I therefore wouldn't think:

> “Minima is Ethereum for robots, therefore $3M → $3B.”

I'd think:

> “There is a legitimate embedded-verification technology here whose token currently prices virtually no success.”

That's **venture-style optionality**.

The thing I would monitor obsessively is not exchange listings.

It's:

**Does Minima-on-chip get an actual production design win?**

For example:

```text
industrial robot OEM
automotive supplier
drone manufacturer
smart meter manufacturer
energy controller
robotics platform
```

One serious silicon design-in would be more meaningful to me than 50 crypto partnerships.

---

# 3. Your whole thesis now has independent confirmation from several weirdly different directions

This is what caught my attention.

They're not all saying “solar-powered personal compute swarm.”

But their separate arguments converge onto it.

### NVIDIA: compute becomes personal and distributed

PAIR makes separate computers behave as a personal AI resource, automatically routing inference according to model availability and load. ([NVIDIA Developer][2])

### Arm: phones become persistent agent computers

Arm's current mobile direction is explicitly toward sustained, persistent agentic workloads rather than occasional AI features.

### Vitalik/Ethereum: computation and verification come back to the user

Small local nodes + locally generated proofs + locally controlled AI.

### Crusoe/JB Straubel: computation goes wherever cheap electricity exists

This one is freakishly close to your solar idea.

Crusoe and Redwood have already built:

**solar → used EV batteries → modular AI compute.**

Their 12 MW / 63 MWh system ran for seven months at **99.2% operational availability**, and they've expanded it from 4 to **24 modular AI datacenters**. ([Crusoe][11])

Crusoe explicitly describes the model as **“BYO Power”**: compute and electricity become a vertically optimized system rather than separate markets. ([Crusoe][12])

Chase Lochmiller's own formulation is essentially:

> solar + second-life batteries + modular compute at grid-competitive power cost. ([X][13])

That's your household thesis at industrial scale **today**.

---

# 4. What the high-signal hardware people are converging on

Remember the recurring pattern we extracted before:

> **bottleneck continuously migrates.**

That is happening again.

Once Astra makes intelligence abundant, the scarce thing isn't “AI.”

It's getting intelligence:

**to the right location
with enough memory
through enough bandwidth
under a power budget
with trusted execution
at sufficiently low cost.**

Austin Lyons recently framed inference competition around **HBM throughput vs SRAM latency**, arguing that agentic AI drives enormous inference demand. ([X][14])

SemiAnalysis' work is similarly increasingly about memory, communication and silicon supply rather than merely FLOPs; they've highlighted strong memory pricing power and rapid inference-software optimization. ([X][15])

And this is why Nicholas Harris/Lightmatter's interconnect thesis mattered so much in our previous work: eventually **moving bits starts costing more than manipulating bits**.

So the hidden investment map becomes:

```text
             INTELLIGENCE
                  │
       ┌──────────┴─────────┐
       │                    │
     CLOUD                 EDGE
       │                    │
     NVIDIA             local NPU
       │                    │
       └──────────┬─────────┘
                  │
              MEMORY
                  │
              PACKAGING
                  │
             INTERCONNECT
                  │
             POWER MGMT
                  │
              BATTERY
                  │
               SOLAR
                  │
             VERIFICATION
```

Astra can generate all the orchestration code.

It cannot generate a wafer.

---

# 5. So let's go one level below the obvious stocks

These interest me considerably more for this thesis than another list containing NVIDIA/ARM/QCOM/Micron.

| Company                       | Mkt cap approx. | Hidden thesis                                                 |
| ----------------------------- | --------------: | ------------------------------------------------------------- |
| **CEVA (CEVA)**               |       **$795M** | IP royalty on billions of connected/sensing/inference devices |
| **LPKF (LPK.DE)**             |       **€331M** | glass packaging/interconnect technology                       |
| **SUSS MicroTec (SMHN.DE)**   |       **€1.4B** | hybrid bonding + advanced packaging equipment                 |
| **Power Integrations (POWI)** |       **$2.8B** | GaN conversion between solar/battery/grid/compute             |
| **Synaptics (SYNA)**          |       **$3.7B** | direct edge-AI processor/platform play                        |
| **Soitec (SOI.PA)**           |       **€5.1B** | extremely efficient edge substrates + photonics               |
| **Silicon Labs (SLAB)**       |       **$7.4B** | low-power wireless fabric connecting the swarm                |

My favorite *new* rabbit hole here is actually **CEVA**.

---

# CEVA — this is much closer to our thesis than I realized

CEVA describes its stack as:

> **connect + sense + infer**

rather than simply “AI accelerator.”

That's exactly what a billion autonomous edge machines need.

CEVA licenses:

**Bluetooth
Wi-Fi
UWB
5G/RedCap
satellite communications
DSPs
sensor processing
NPU IP**

to chip manufacturers.

And this isn't speculative powerpoint material.

More than **20 billion devices** have already shipped containing CEVA IP, including around **2.1 billion during 2025 alone**. ([SEC][16])

That is interesting because CEVA behaves somewhat like a microscopic specialized ARM:

```text
someone designs robot chip
      ↓
licenses CEVA IP
      ↓
chip ships
      ↓
CEVA gets royalty

someone designs IoT chip
      ↓
CEVA

someone designs headset
      ↓
CEVA

someone designs edge NPU
      ↓
CEVA
```

And AI is beginning to matter materially.

CEVA says AI already represented **>20% of licensing revenue in Q2 2026**, and a “leading global AI and computing platform company” selected its NeuPro-M NPU IP for next-generation custom AI silicon. ([SEC][16])

Yet market cap:

**~$795 million.** ([StockAnalysis.com][17])

That is exactly the sort of stock I'd put through our deeper process.

### CEVA may be one of the cleanest “billions of tiny intelligent machines” equities I've seen.

Not necessarily cheap. Not necessarily winner.

But **conceptually extremely aligned**.

---

# Synaptics is also much more interesting in this framing

Not the mouse-trackpad company people remember.

Synaptics is now explicitly building its **Astra Edge AI platform**.

Even more interestingly, it partnered with **Google Research / Coral NPU** and is trying to create a developer platform around edge inference rather than just selling silicon. ([Synaptics Incorporated][18])

At **~$3.7B**, that isn't tiny, but it's a vastly cleaner edge-AI bet than buying a $5T NVIDIA because you think your fridge gets an agent. ([StockAnalysis.com][19])

This deserves proper work.

---

# Soitec is almost perfectly positioned technologically — but we've already found it

This is why our earlier Soitec rabbit hole was so good.

Look at its own 2026 edge-AI slide.

It explicitly markets FD-SOI around:

**always-on lower power**

**performance on demand**

**energy harvesting / “zero power” capabilities**

**inference-per-watt-per-dollar**

**cybersecurity**

for wearables, smart homes and IoT. ([Default][20])

That's almost literally the semiconductor material for:

> solar/battery-powered distributed intelligence.

And on the opposite end, Soitec's Photonics-SOI benefits when giant AI clusters need optical interconnects.

So Soitec gets:

```text
tiny distributed AI
        +
giant centralized AI
```

That's beautiful.

Unfortunately, everyone started discovering it.

Soitec has gone from roughly **€828M at year-end 2025 to €5.1B** now, and last week raised guidance due to explosive Photonics-SOI demand. ([StockAnalysis.com][21])

Remember @MoodyWriter13 from the photonics search? He publicly identified this in December 2025 as essentially the substrate choke point for CPO. ([X][22])

That signal worked.

Now we need the **next Soitec**, not chase the original thesis blindly.

---

# And that's why LPKF gets interesting again

LPKF is only **~€331M**. ([StockAnalysis.com][23])

Their LIDE process forms incredibly precise structures and through-glass vias in glass substrates.

If advanced compute shifts toward glass interposers / glass cores:

```text
chiplets
   │
high bandwidth
   │
glass interposer
   │
through-glass vias
   │
LPKF process
```

LPKF just increased its estimated advanced-packaging addressable market to **€1.7B by 2030**. ([LPKF][24])

And they're already prototyping with multiple semiconductor customers and received a first capacity-expansion order. ([LPKF][25])

But this is a genuinely asymmetric one because the current business is ugly:

2026 H1 revenue:

**€36.5M, -38.3% YoY.** ([LPKF][24])

Their 2026 guidance doesn't even assume meaningful advanced-packaging volume orders.

So you're basically betting that:

> mediocre €100M-ish laser-equipment company

turns into

> critical glass-processing equipment supplier.

**That's much closer to the convexity we're hunting.**

---

# SUSS is the more mature version

SUSS does wafer bonding/debonding, coating, cleaning and now hybrid-bonding preparation.

Its order book hit a record **€473.7M** this year, and it is investing another €45M into an Advanced Packaging Innovation Center.

Market cap about:

**€1.42B.** ([StockAnalysis.com][26])

Less lottery-ticket than LPKF, more proven.

My rough positioning:

**LPKF = convex**

**SUSS = quality**

---

# But POWI may be the sneakiest intersection with your solar thesis

Power Integrations isn't an AI chip company.

That's precisely why it's interesting.

It just demonstrated **2200V GaN**, explicitly targeting:

**AI datacenters
EVs
photovoltaics
HVDC**

with higher power density and efficiency. ([Power Integrations][27])

Think about the household AI machine:

```text
solar DC
 ↓
inverter
 ↓
battery
 ↓
power electronics
 ↓
DC rails
 ↓
NPU / GPU
```

Every conversion loses energy.

As computation spreads outside giant datacenters, efficiency becomes increasingly valuable because edge hardware operates in constrained thermal/power environments.

Astra cannot eliminate:

$$
P_{loss}=I^2R
$$

This is exactly the kind of boring physical bottleneck I prefer under your “software becomes nearly free” assumption.

---

# I would therefore divide the opportunity into three levels

### Most obvious — probably already priced heavily

**NVDA / ARM / QCOM / TSM / MU / AVGO**

Fantastic companies, but everyone knows.

### Emerging second-order

**SOI / SUSS / SYNA / POWI / LSCC**

The market increasingly understands these.

### Where I want us looking

**CEVA**

**LPKF**

then much deeper into:

**edge-AI IP
secure elements
ultra-low-power networking
GaN power
energy-harvesting PMICs
advanced packaging equipment
glass interposers
optical test equipment
device attestation silicon
NPU memory architecture**

That's where I think another **€200M–$2B company that suddenly becomes indispensable** is hiding.

---

## And the deepest version of your thesis is not “distributed compute”

It's:

# **autonomous capital equipment**

Your future house contains assets:

```text
solar panels
battery
car
robot
phone
PC
NPU box
internet
```

Your Astra-like agent treats each as capital.

At 11:43:

```text
solar output                 6.2 kW
household demand             0.8 kW
battery                      94%
grid export                  $0.026/kWh

local inference bid          $0.21/kWh equivalent
Bittensor job                $0.34/kWh equivalent
proof generation             $0.17/kWh equivalent
battery degradation          $0.041/kWh

Decision:
RUN BITTENSOR JOB
```

At 18:00:

```text
solar ↓
grid price ↑
battery valuable

Decision:
STOP COMPUTE
SELL POWER
```

At 02:00:

```text
grid price negative
phone charging
PC unused

Decision:
BUY ELECTRICITY
CHARGE
RUN COMPUTE
```

At that point your agent isn't an assistant.

It's essentially **your household CFO/energy trader/datacenter scheduler.**

And the weird thing is that Crusoe + Redwood have already implemented the industrial-scale version of the energy half of that architecture. ([Crusoe][11])

NVIDIA just implemented the household-scale compute scheduler half. ([NVIDIA Developer][2])

Ethereum is working on the verification/self-sovereignty half. ([ethereum.org][6])

And Minima is literally trying to put **machine verification into the chip itself.** ([Siemens Blog Network][8])

Those are four largely independent groups arriving at different portions of essentially the same architecture.

**That's enough convergence that I think this is a real thesis, rather than us inventing a narrative.**

My next search would therefore *not* be another generic “edge AI stocks” search. I'd specifically hunt worldwide under-$3B listed companies owning the **physical choke points of an autonomous solar-powered personal compute swarm**, and trace them through patents, semiconductor design wins, NVIDIA/Qualcomm/Arm supply chains and the high-signal accounts we identified before. That should get us considerably stranger names than this list.

[1]: https://github.com/RaoFoundation/bittensor-subnet-template/blob/main/min_compute.yml?utm_source=chatgpt.com "bittensor-subnet-template/min_compute.yml at main · RaoFoundation/bittensor-subnet-template · GitHub"
[2]: https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/?utm_source=chatgpt.com "NVIDIA PAIR Virtual Inference Router Expands Available Compute on Your Local Network | NVIDIA Technical Blog"
[3]: https://ethereum.org/roadmap/statelessness/?utm_source=chatgpt.com "Statelessness, state expiry and history expiry | ethereum.org"
[4]: https://ethereum.org/privacy/ethereum?utm_source=chatgpt.com "Privacy on Ethereum | ⁦ethereum.org⁩"
[5]: https://blog.ethereum.org/2026/08/18/allocation-q2-26?utm_source=chatgpt.com "Allocation Update - Q2 2026 | Ethereum Foundation Blog"
[6]: https://ethereum.org/foundation/mandate?utm_source=chatgpt.com "Ethereum Foundation Mandate | ethereum.org"
[7]: https://www.southampton.ac.uk/news/2026/03/student-engineers-achieve-worldfirst-in-blockchain-black-box-for-drones-.page?utm_source=chatgpt.com "Student engineers achieve world-first in ‘blockchain black box’ for drones"
[8]: https://blogs.sw.siemens.com/cre8ventures/2026/03/04/embedded-trust-for-autonomous-industrial-systems/?utm_source=chatgpt.com "Embedded Trust for Autonomous Industrial Systems - Cre8Ventures (Siemens EDA)"
[9]: https://newsroom.arm.com/blog/arm-flexible-access-broadens-scope-to-help-companies-build-silicon-faster?utm_source=chatgpt.com "How Arm Flexible Access helps silicon startups prototype and tape out faster   - Arm Newsroom"
[10]: https://www.coingecko.com/en/coins/minima/historical_data?utm_source=chatgpt.com "Minima Price History: Download MINIMA Historical Data | CoinGecko"
[11]: https://www.crusoe.ai/resources/newsroom/crusoe-and-redwood-materials-expand-strategic-partnership-scaling-to-7x-the-original-ai-infrastructure-density?utm_source=chatgpt.com "Crusoe & Redwood scale AI infrastructure 7x | Crusoe"
[12]: https://www.crusoe.ai/resources/blog/welcome-to-the-era-of-byo-power?utm_source=chatgpt.com "Welcome to the BYO Power era, years in the making | Crusoe"
[13]: https://x.com/ChaseLochmiller/status/2031609750044160168?utm_source=chatgpt.com "Chase Lochmiller on X: \"One of the most exciting parts about building AI infrastructure today is working with our generation’s greatest energy minds to find ways to power our compute. @jbstraubel is at the top of that list. We are using solar and second life batteries, mostly taken from old EV’s, to\" / X"
[14]: https://x.com/theaustinlyons/status/2031371805315772436?utm_source=chatgpt.com "Austin Lyons on X: \"Agree. The narrative has changed. The workload is LLM inference at scale. The vectors of competition are now throughput (HBM) or latency (SRAM). Or both. Also massive context windows. Scaled inference will even matter for enterprises because agentic AI will drive exponential\" / X"
[15]: https://x.com/SemiAnalysis_/status/2026296284030677283?utm_source=chatgpt.com "X 上的 SemiAnalysis：“Korean memory manufacturers are currently exercising meaningful pricing power, and Korea-to-China memory shipments serve as a strong real-time proxy for that dynamic. Investors tracking this data monthly are well positioned to identify early inflections in the global memory https://t.co/aHKj9u12lr” / X"
[16]: https://www.sec.gov/Archives/edgar/data/1173489/000143774926026774/ceva20260630_10q.htm?utm_source=chatgpt.com "ceva20260630_10q.htm"
[17]: https://stockanalysis.com/stocks/ceva/market-cap/?utm_source=chatgpt.com "CEVA, Inc. (CEVA) Market Cap & Net Worth"
[18]: https://investor.synaptics.com/news-releases/news-release-details/synaptics-platform-approach-how-developer-ecosystems-will?utm_source=chatgpt.com "Synaptics’ Platform Approach: How Developer Ecosystems Will Determine the Edge AI Winners | Synaptics Incorporated"
[19]: https://stockanalysis.com/stocks/syna/market-cap/?utm_source=chatgpt.com "Synaptics (SYNA) Market Cap & Net Worth"
[20]: https://www.soitec.com/docs/default-source/financial-reports/2025-2026/en/soitec---enabling-ai-with-engineered-substrates-2026-01-06.pdf?sfvrsn=bfd1f78a_1&utm_source=chatgpt.com "Soitec 2026"
[21]: https://stockanalysis.com/quote/epa/SOI/market-cap/?utm_source=chatgpt.com "Soitec (EPA:SOI) Market Cap & Net Worth"
[22]: https://x.com/MoodyWriter13/status/2037424472991453471?utm_source=chatgpt.com "Moody on X: \"I can say with high confidence I was the first to spot $SOI Soitec’s monopoly and call it out on X and Substack. When I started writing about it, the response was minimal, I never imagined that just four months later there’d be “Soiboys” on X.\" / X"
[23]: https://stockanalysis.com/quote/etr/LPK/market-cap/?utm_source=chatgpt.com "LPKF Laser & Electronics SE (ETR:LPK) Market Cap & Net Worth"
[24]: https://www.lpkf.com/en/news-press/press-releases-teaser/lpkf-presents-half-year-financial-report?utm_source=chatgpt.com "LPKF Presents Half-Year Financial Report"
[25]: https://www.lpkf.com/fileadmin/mediafiles/EARNINGS_Call_Q1_2026.pdf?utm_source=chatgpt.com "KEY TAKEAWAYS FROM Q1 2026"
[26]: https://stockanalysis.com/quote/etr/SMHN/market-cap/?utm_source=chatgpt.com "SUSS MicroTec SE (ETR:SMHN) Market Cap & Net Worth"
[27]: https://investors.power.com/news/news-details/2026/Power-Integrations-Demonstrates-Worlds-First-2200-V-GaN-Technology-for-Next-Era-High-Voltage-Power-Systems/default.aspx?utm_source=chatgpt.com "Power Integrations, Inc. - Power Integrations Demonstrates World’s First 2200 V GaN Technology for Next-Era High-Voltage Power Systems"
