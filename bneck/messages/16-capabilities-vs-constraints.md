Yes. I think the thesis becomes substantially cleaner if you stop thinking in terms of “AI sectors” and instead divide the economy into **capabilities AGI can commoditize** and **constraints AGI must route through**.

The trade is then:

> **Short rents derived from human/technical capability scarcity as soon as AGI demonstrably destroys that scarcity. Long the residual constraints that become more valuable after the capability disappears.**

That connects the memory trade, robotics, biological computing, autonomous labs, quantum, patents, power and even regulation.

### Why the collapses can become extremely violent

A stock does not have to wait for its industry to disappear. Its price is the discounted expectation of future cash flows.

Imagine a company earning enormous margins because:

> “Producing X requires 5,000 highly skilled engineers.”

Then a frontier model demonstrates:

> “One engineer + model can produce X.”

The company's current quarter can still look fantastic.

But the market can immediately revise:

$$
PV(\text{future scarcity rents}) \rightarrow 0
$$

That's your discontinuity.

So I wouldn't model:

**AGI arrives → businesses slowly decline.**

I'd model:

**capability milestone → information shock → terminal-value discontinuity → capital repricing → operational collapse later.**

That is why the relevant kill-feed isn't mainly earnings.

It's **capability benchmarks**.

---

# The core classification

Every economic activity can be decomposed into:

$$
Output =
Cognition
+
Information
+
Physical\ Action
+
Physical\ Resources
+
Time
+
Rights
+
Permission
+
Trust
$$

AGI attacks the first two with extraordinary force.

It increasingly attacks coordination and some physical action through robotics.

But several categories remain.

### 1. Physics

AGI can't reason copper into existence.

It can:

* discover substitutes
* optimize extraction
* reduce copper/unit
* improve recycling
* redesign systems

But whatever final architecture it chooses still occupies physical state space.

So you recursively ask:

> What must physically happen for this output to exist?

That's the deepest branch of the bottleneck graph.

---

### 2. Experimentation / contact with reality

This is exactly why the Michael Levin / synthetic-life direction fits the thesis.

Suppose AGI becomes an unbelievably good biological theorist.

It can generate:

**10 million plausible morphogenetic hypotheses/hour.**

But eventually something must:

grow cells
culture tissue
measure voltage
sequence samples
image organisms
perturb pathways
wait for development
observe outcomes.

The bottleneck moves:

**scientific reasoning**

↓

~scientists thinking~~

↓

**experimental throughput**

↓

liquid handlers
microscopy
reagents
biofoundries
culturing capacity
instrumentation
sample availability
containment
experimental time.

Recent work on industrial self-driving laboratories makes essentially this distinction: AI-generated intent still has to become physically executable experiments and produce trustworthy evidence. ([Nature][1])

That's exactly our bottleneck relay.

AGI can make the **brain of science nearly free** while making access to physical reality extraordinarily valuable.

---

# 3. Time may be surprisingly irreducible

This one interests me.

Some processes simply contain elapsed time.

You can parallelize them, but there may be no algorithm that makes:

a tree mature instantly
a clinical trial observe 10-year outcomes instantly
a biological organism develop instantly
a mine get permitted instantly
concrete cure instantly
a massive fab appear instantly.

AGI will attack these too.

But this suggests another graph property:

$$
MinimumPhysicalLatency(node)
$$

A node having a three-year unavoidable ramp is potentially an incredible bottleneck during exponential demand growth.

---

# 4. And yes: **law itself can become the bottleneck**

This is a big addition.

A patent does **not** merely document an invention.

A U.S. patent gives its owner a legal right to exclude others from making, using, selling, offering to sell or importing what the patent claims. Importantly, it does not itself give the owner permission to practice the invention — another patent or another law could still block them. ([USPTO][2])

Therefore you can absolutely have:

**AGI solves technical problem**

→ technical uncertainty = zero

→ physical ability exists

→ **commercial freedom-to-operate becomes bottleneck.**

That's fascinating.

---

# Your IonQ example is possible — but I'd formulate it slightly differently

Not:

> OpenAI discovers quantum computing but IonQ owns quantum computing.

That would be too broad.

Quantum has numerous competing physical architectures and large portfolios distributed among many organizations. The EPO's quantum-computing patent landscape explicitly breaks the field into multiple physical realizations, error correction, AI/QC intersections and other subfields. ([EPO][3])

But imagine AGI discovers:

> **Architecture Q is overwhelmingly better.**

And Architecture Q requires:

A → B → C → D.

Then imagine C is covered by a cluster of broad, enforceable patents controlled by one organization.

Now:

**technical bottleneck disappeared**

but

**IP-access bottleneck appeared.**

That organization could become incredibly valuable.

---

## IonQ is actively building exactly this kind of position

IonQ said in August 2025 that its owned/licensed/controlled estate exceeded **1,000 patents and pending applications**, spanning its acquisitions and internal portfolio. ([IonQ][4])

Its networking portfolio alone was approaching 400 owned/controlled granted and pending patents by March 2025. ([IonQ][5])

Lightsynq added another 20+ patents/applications around quantum memory and interconnects. ([IonQ][6])

And then look at the other thing IonQ just did.

It completed the acquisition of **SkyWater on July 31, 2026**.

So it now combines IP with domestic semiconductor manufacturing/foundry capability and advanced packaging. ([IonQ][7])

That means IonQ is potentially accumulating several completely different constraint types:

**knowledge/IP**
+
**fabrication**
+
**packaging**
+
**government relationships**
+
**deployment experience**.

That's much more interesting than merely asking whose qubit is best.

---

# But patents aren't perfectly irreducible

This matters for the model.

A patent bottleneck can be attacked through:

**license**
→ pay owner

**acquisition**
→ buy owner

**design-around**
→ invent implementation outside claims

**invalidity challenge**
→ patent dies

**expiry**
→ protection ends

**different jurisdiction**
→ patents are territorial

**alternative architecture**
→ avoid technology entirely

**government intervention / compulsory licensing**
→ unusual, but patent systems contain such mechanisms.

WIPO notes both the territorial nature of patents and various national exceptions/limitations including research exceptions, compulsory licensing and government use. ([WIPO][8])

Therefore IP is not like the speed of light.

It's better classified as:

> **institutionally enforced scarcity**

rather than fundamental scarcity.

And that means our model can score it.

---

# CRISPR proves this is not hypothetical

Biology gives us an excellent precedent.

CRISPR wasn't simply:

**discovery → everyone can commercialize it.**

The foundational technology generated overlapping patent estates around Berkeley/UC, Broad and others, followed by complicated licensing structures and commercial licensees. ([PubMed][9])

Patent researchers have explicitly mapped CRISPR's patent/licensing network because intellectual-property rights became part of the path connecting scientific discovery to commercial products. ([PubMed Central (PMC)][10])

But notice what happened:

**patents didn't stop CRISPR science.**

They affected:

**who captured commercialization rents.**

That's much closer to what our investment model should care about.

---

# This gives us a whole new kind of graph

Previously:

```text
HBM
    requires CoWoS
        requires packaging equipment
            requires precision motion
```

Now:

```text
technology
    PHYSICALLY_REQUIRES → component
    MANUFACTURED_BY → company
    PATENT_COVERED_BY → patent family
    CONTROLLED_BY → company
    LICENSED_TO → company
    REGULATED_BY → authority
    REQUIRES_APPROVAL_FROM → authority
    CERTIFIED_BY → institution
    REQUIRES_SITE → facility/geography
    REQUIRES_TIME → process
```

This is **far more powerful**.

Because “bottleneck” no longer means merely supply shortage.

It means:

> **Anything that remains necessary after intelligence becomes arbitrarily abundant.**

---

# I'd call these the residual constraints

There are perhaps seven useful classes.

| Constraint                  | Can AGI directly eliminate it? | Typical kill                |
| --------------------------- | -----------------------------: | --------------------------- |
| **Knowledge**               |                 Extremely high | better model                |
| **Human skill**             |                 Extremely high | model/robot                 |
| **Compute architecture**    |                           High | new algorithm/hardware      |
| **Physical resources**      |                         Medium | substitution/efficiency     |
| **Physical processes/time** |                     Low–medium | parallelization/new process |
| **IP/property rights**      |                Low technically | licensing/design-around/law |
| **Regulatory permission**   |                Low technically | legal/policy change         |

And that's why the strategy isn't really:

> Find bottlenecks AGI can't solve.

Because given enough time, AGI could probably find routes around huge numbers of them.

The better question is:

> **Which constraints can't be eliminated faster than demand for their output is growing?**

That's the investable quantity.

---

# So introduce `time_to_kill`

For every node:

$$
T_k =
\text{estimated time for AI/industry to eliminate this constraint}
$$

And:

$$
T_d =
\text{time until demand overwhelms available supply}
$$

When:

$$
T_d \ll T_k
$$

you potentially have a spectacular long bottleneck.

When:

$$
T_k \rightarrow 0
$$

for a highly valued industry whose scarcity rent depends upon that capability:

**short candidate.**

This captures your entire idea.

---

# The short side is potentially the more convex side

Suppose:

**industry market cap = $500B**

because analysts assume its bottleneck persists for 20 years.

Then a frontier result demonstrates that the constraint can disappear in two.

Nothing has to happen operationally yet.

The terminal-value calculation gets destroyed.

That's why your **kill ratio** is important.

I'd extend it into:

$$
RedundancyRisk =
P(\text{AGI can perform function})
\times
P(\text{deployment})
\times
RevenuePurity
\times
OperatingLeverage
\times
ExpectationDuration
$$

And then:

$$
ShortConvexity \propto
\frac{RedundancyRisk}
{MarketProbabilityAssigned}
$$

The monster trades would therefore be companies where:

**market assumes bottleneck permanence**

while

**frontier capability is rapidly approaching substitution.**

---

# There is another beautiful reflexivity here

Imagine Company X owns a bottleneck.

Its price rises 10×.

Suddenly solving X becomes incredibly valuable.

AI labs, entrepreneurs and capital all attack it.

Therefore:

$$
ScarcityRent \uparrow
\Rightarrow
IncentiveToDestroyScarcity \uparrow
$$

The most profitable bottleneck eventually attracts the most powerful diggers.

So excessive price appreciation isn't just valuation risk.

It is **technological attack-surface growth**.

That may help explain the repeated corpse pattern you've encoded.

---

# And then AGI makes the feedback loop dramatically faster

Old capitalism:

```text
shortage
↓
prices rise
↓
capital formation
↓
new factories
↓
supply expansion
↓
prices fall

~5–15 years
```

AGI capitalism could increasingly look like:

```text
shortage detected
↓
enormous scarcity rent
↓
AI searches design space
↓
algorithm/material/process discovered
↓
constraint disappears
↓
market reprices

months / weeks / perhaps days
```

That is the central change.

Stocks don't necessarily become intrinsically impossible to predict.

Rather:

> **technological state becomes a much larger state variable in valuation, and technological state can move discontinuously.**

Therefore investors using trailing earnings become increasingly blind.

---

# This is what I think the project really is now

Not an AI bottleneck tracker.

It's an **economic dependency graph under accelerating intelligence**.

For every economically valuable node, it asks two opposing questions:

### `DESTROY(node)`

> How could sufficiently capable AI make this economic function unnecessary, abundant, substituted or nearly free?

And:

### `CONSTRAIN(node)`

> If everything cognitively upstream became free tomorrow, what would still prevent arbitrarily large production?

That recursion is extremely powerful.

For biology:

```text
biological discovery
DESTROY → human hypothesis-generation labor

CONSTRAIN
→ physical experiments
→ culture throughput
→ imaging
→ reagents
→ lab robotics
→ samples
→ biosafety approval
→ IP rights
→ clinical validation
→ elapsed biological time
```

For quantum:

```text
quantum design
DESTROY → much human architecture/search work

CONSTRAIN
→ physical qubit implementation
→ fabrication
→ lasers/control electronics
→ cryogenics or vacuum
→ photonic interconnects
→ error rates
→ scaling/manufacturing
→ patents/licenses
→ export controls
→ trusted foundries
```

This is much closer to a general theory than a stock-picking heuristic.

And I'd make **patent mapping a first-class component now**, not metadata. EPO already publishes free quantum patent-landscape data, and WIPO explicitly produces patent landscape reports for exactly this kind of technology/ownership analysis. ([EPO][3])

The potentially exceptional equity isn't necessarily the company that invents the AGI-era technology.

It could be the obscure entity that owns **the last unavoidable edge between the invention and physical reality**.

[1]: https://www.nature.com/articles/s44160-026-01120-6?utm_source=chatgpt.com "Self-driving laboratories need an autonomy safety harness | Nature Synthesis"
[2]: https://www.uspto.gov/patents/basics/essentials?utm_source=chatgpt.com "Patent essentials | USPTO"
[3]: https://www.epo.org/en/searching-for-patents/business/technology-insight-reports?utm_source=chatgpt.com "Technology insight reports | epo.org"
[4]: https://investors.ionq.com/news/news-details/2025/IonQ-Fortifies-Quantum-Leadership-with-Groundbreaking-Patents-Surpassing-1000-Total-IP-Assets/default.aspx?utm_source=chatgpt.com "IonQ - IonQ Fortifies Quantum Leadership with Groundbreaking Patents, Surpassing 1,000 Total IP Assets"
[5]: https://www.ionq.com/news/ionq-expands-quantum-networking-patent-portfolio-to-meet-strong-market?utm_source=chatgpt.com "IonQ | IonQ Expands Quantum Networking Patent Portfolio to Meet Strong Market Demand for Secure Communications"
[6]: https://www.ionq.com/news/ionq-completes-acquisition-of-lightsynq-accelerating-quantum-computing-and?utm_source=chatgpt.com "IonQ | IonQ Completes Acquisition of Lightsynq, Accelerating Quantum Computing and Networking Roadmap"
[7]: https://www.ionq.com/news/ionq-completes-acquisition-of-skywater-technology?utm_source=chatgpt.com "IonQ | IonQ Completes Acquisition of SkyWater Technology"
[8]: https://www.wipo.int/en/web/patents/faq_patents?utm_source=chatgpt.com "Frequently Asked Questions: Patents"
[9]: https://pubmed.ncbi.nlm.nih.gov/31021185/?utm_source=chatgpt.com "The CRISPR Patent Landscape: Past, Present, and Future."
[10]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8316212/?utm_source=chatgpt.com "Mapping CRISPR-Cas9 public and commercial innovation using The Lens institutional toolkit - PMC"
