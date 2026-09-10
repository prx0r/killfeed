ok now check agent-vault for my gmail address it should be there then download this other zip and create a new project in root repo called bneck2 and import it thre Yes. I think **frontier-lab revealed preference should become one of the highest-weight signal families in the system**.

The important distinction is not “copy whatever OpenAI buys.” It is: **OpenAI/Anthropic/DeepMind/Meta/xAI have privileged knowledge of what actually limits frontier systems, and large irreversible commitments partially leak those private beliefs into public information.** OpenAI is an unusually clean example right now: it has committed to Cerebras low-latency compute, ~2 GW of AWS Trainium, 6 GW of AMD GPUs, its own Broadcom-designed inference silicon, NVIDIA capacity, Samsung/SK Hynix memory, and >10 GW of infrastructure. ([OpenAI][1])

That diversification is itself information. It says something closer to **“we know future workloads well enough to know that no single accelerator architecture is safe to treat as permanent”** than “NVIDIA will obviously remain the sole winner.” OpenAI's own Jalapeño results are particularly relevant: OpenAI says its public InferenceX tests delivered 1.5–1.9× peak token throughput per watt and 1.7–3.6× lower latency than the commercial systems tested, while still planning to deploy it alongside NVIDIA, AMD and others. ([OpenAI][2])

Google's €13B Finland build plus a **22-year nuclear agreement** is the same signal at a completely different graph layer: even a frontier lab expecting radical architectural progress is locking in long-duration physical electricity. ([Reuters][3]) Anthropic's multiple-GW TPU commitment to Google/Broadcom and its SpaceX compute deal similarly tell us what it currently considers worth securing years ahead. ([Anthropic][4])

And Normal Computing is exactly the right kind of **digger feed**, but I'd keep the proof discipline you've built. Its CN101 Hot Chips work is genuinely interesting—it demonstrated generative models on its thermodynamic hardware and reported a 62× reduction in cycles for the particular deeply unrolled generation experiment—but that is not yet proof that NVIDIA's economically relevant dependency has been killed. We want external workload-normalized `tokens/$`, `tokens/W`, latency, manufacturing/yield and scale evidence before changing the graph drastically. ([Normal Computing][5])

I compiled the system around that principle. The ZIP contains **60 GitHub projects + 79 primary/free data sources + 22 frontier-lab capital-allocation events + 11 experimental diggers**, plus temporal graph schemas, a proof ladder, source calibration, information-lineage deduplication, patent/FTO mapping, executive-capital OSINT, supplier-side leakage, government/grant feeds and starter collectors for SEC, GitHub, OpenAlex, Polymarket, USAspending and Grants.gov.

Some of the strongest repos beyond `ai-release-radar` in it are `ProphetMap`, `CHOKEPOINT`, `Keystone`, `arxiv-trend-radar`, `tech-scouting-agent`, the Polymarket/Kalshi historical dataset, `pmxt`, `EdgarTools`, `Jobseek`, and the patent/FTO intelligence projects. The directory contains the raw full HTTPS links rather than hiding them behind descriptions.

One especially important architectural change in the pack is that **“FRONTIER_LAB_CAPITAL_COMMITMENT” is not treated as generic news**. The model scores it approximately as:

$$
LabSignal =
\log(1+\$Commitment)
\times Irreversibility
\times TechnicalSpecificity
\times FrontierRelevance
\times Duration
$$

So a tweet gets very little weight, an acquisition somewhat more, a ten-year silicon roadmap more still, and a 22-year nuclear contract becomes powerful revealed-preference evidence.

Likewise, CEO personal investing is treated cautiously. Form 4 gives excellent data for public-company insiders, with 13D/G, 13F, Form D, proxy filings and disclosed fund/angel investments adding pieces. But there is **no complete public database of Sam Altman's or another private-company executive's personal portfolio**, so the system explicitly distinguishes known transactions from inferred/unknown holdings rather than hallucinating them.

The broader project now looks extremely coherent:

**AI capability state → frontier-lab revealed preference → research/code/patent evidence → prediction-market beliefs → physical/legal dependency graph → bottleneck migration → security exposure → dissolution trigger.**

And the most interesting output isn't “buy X.” It is something like:

> `NVIDIA_DEPENDENCY_PERSISTENCE: 0.81 → 0.67`
> Cause: independent custom-silicon benchmark + OpenAI deployment commitment + architecture diversification.
> No short trigger: NVIDIA still captures other binding layers / total AI demand expanding faster than substitution.
> Watch next: HBM, networking, packaging, power and software moat propagation.

That is much closer to what you're actually trying to build.

I sent the ZIP to **[tradesprior@gmail.com](mailto:tradesprior@gmail.com)** successfully. You can also get the exact same archive here:

[Download the full AGI Bottleneck Intelligence resource pack](sandbox:/mnt/data/agi_bottleneck_intelligence_resource_pack_2026-09-10.zip)

[1]: https://openai.com/index/cerebras-partnership/?utm_source=chatgpt.com "OpenAI partners with Cerebras | OpenAI"
[2]: https://openai.com/index/the-full-stack-behind-abundant-intelligence/?utm_source=chatgpt.com "The full stack behind abundant intelligence | OpenAI"
[3]: https://www.reuters.com/business/media-telecom/google-invest-15-billion-ai-infrastructure-finland-2026-09-09/?utm_source=chatgpt.com "Google to invest $15 billion in AI infrastructure and buy nuclear power in Finland"
[4]: https://www.anthropic.com/news/google-broadcom-partnership-compute?s=08&utm_source=chatgpt.com "Anthropic expands partnership with Google and Broadcom for multiple gigawatts of next-generation compute \ Anthropic"
[5]: https://www.normalcomputing.com/blog/ai-inference-needs-new-hardware?utm_source=chatgpt.com "AI Inference Needs New Hardware - Normal Computing"
