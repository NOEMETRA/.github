<p align="center">
  <img src="./header.svg" alt="Northguard Security — independent security research" width="100%" />
</p>

# Security engineering grounded in evidence

**Northguard Security** is an independent research workspace building practical tools and controlled experiments in digital forensics, network protocols, traffic analysis, and application security.

The work starts with software and a concrete technical question. The result is measured against observations, negative controls, and failure cases—not just a successful run or an impressive-looking output.

**Explore the public labs:** [PAW](https://github.com/Northguard-Security/PAW--Phishing-Attribution-Workbench--) · [Reverse Observer](https://github.com/Northguard-Security/Reverse-Observer) · [Mirage Flow](https://github.com/Northguard-Security/mirage-flow) · [Chimera](https://github.com/Northguard-Security/Chimera)

## Public research projects

| Project | What it does | Where the evidence comes from |
| :--- | :--- | :--- |
| **[PAW — Phishing Attribution Workbench](https://github.com/Northguard-Security/PAW--Phishing-Attribution-Workbench--)** | Ingests suspicious email, reconstructs delivery-path hypotheses, extracts indicators, correlates infrastructure, and produces forensic case artifacts. | Original messages, headers, hashes, case manifests, enrichment results, and explicit scoring heuristics. |
| **[Reverse Observer](https://github.com/Northguard-Security/Reverse-Observer)** | Probes network-path and middlebox responses to controlled packet and protocol variations. | Raw-packet observations, structured experiment logs, and documented negative or inconclusive results. |
| **[Mirage Flow](https://github.com/Northguard-Security/mirage-flow)** | Tests known packet-timing patterns under jitter and loss, alongside a modeled response-state controller. | Synthetic timing trials, correlation scores against comparison keys, and packet-timestamp measurements. |
| **[Chimera](https://github.com/Northguard-Security/Chimera)** | Reproduces a clipboard-to-DOM-XSS trust-boundary failure in a deliberately vulnerable web fixture. | A controlled source page, an unsafe destination sink, and observable browser/network behavior. |

These are **research tools and laboratory proofs of concept**, with different levels of implementation and validation. Read each repository's status and limitations before using or interpreting its results.

## Research areas

- **Email forensics and infrastructure correlation:** preserve source evidence, derive indicators, and separate correlation from operator attribution.
- **Network and protocol behavior:** inspect stateful devices, timing signals, and transport-specific responses under repeatable stimuli.
- **Application trust boundaries:** reproduce concrete failure modes and identify conditions under which they disappear.
- **Detection and observability:** distinguish the fact that a signal was detected from claims about malicious intent, identity, or real-world effectiveness.

Some other work remains in private research repositories. The public projects above are the documented entry points.

## From mechanism to evidence

```text
technical question
       |
       v
working prototype
       |
       v
controlled stimulus + baseline
       |
       v
measurement + negative controls
       |
       v
repetition / falsification
       |
       v
documented result + known limits
```

A result should state **what ran, what was observed, under which conditions, and what alternative explanations remain**.

We distinguish:

- **Implemented:** code exists and executes a specified operation.
- **Observed:** a measurable result occurred in a recorded environment.
- **Reproduced:** the result survives a defined repeat test.
- **Validated:** independent checks support the intended interpretation.
- **Unverified or falsified:** the evidence is insufficient, or a tested prediction did not hold.

An output is not an attribution. A correlation is not an identity. A simulation is not field validation. Negative results belong in the record.

## Working with the projects

Each repository is its own experiment: consult its README for prerequisites, safety boundaries, reproducible commands, and current status. Do not infer production suitability from a repository name or a functioning demo.

Testing is limited to systems, accounts, networks, and devices you own or are explicitly authorized to assess. Some labs intentionally exercise risky protocol or application behavior; run them in isolated, instrumented environments. Do not use real personal data, live third-party targets, or production networks as substitutes for test fixtures.

For corrections, controlled reproductions, and scoped contributions, see the [contribution guide](https://github.com/Northguard-Security/.github/blob/main/CONTRIBUTING.md). Avoid posting credentials, personal data, or undisclosed security vulnerabilities in public issues.

---

<sub>Independent security research · Build the mechanism. Measure the outcome. Preserve the uncertainty.</sub>
