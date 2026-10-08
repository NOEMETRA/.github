<p align="center">
  <img src="./header.svg" alt="NOEMETRA — Systems, Signals, Evidence; independent systems research" width="100%" />
</p>

<p align="center">
  <b>Independent Systems Research</b><br />
  <sub>Build the mechanism. Measure the outcome. Preserve the uncertainty.</sub>
</p>

**NOEMETRA** is an independent experimental software and systems research workspace. We build tools to investigate how real digital systems behave—across network protocols, forensic evidence, application security, signal analysis, and observability.

Our work moves between building and investigation: a working mechanism, an instrumented experiment, a controlled measurement with negative controls, and a result that can survive independent scrutiny. We keep negative results and failed hypotheses when they tell us something useful.

> **Systems. Signals. Evidence.** Software first; verification always.

## Explore the public software

| Project | Built to explore | Inspectable output |
| :--- | :--- | :--- |
| **[PAW — Phishing Attribution Workbench](https://github.com/Northguard-Security/PAW--Phishing-Attribution-Workbench--)** | Email forensics, delivery-path hypotheses, indicators, and infrastructure correlations | Case files, original inputs, hash manifests, forensic reports, and rule-based scoring |
| **[Reverse Observer](https://github.com/Northguard-Security/Reverse-Observer)** | Observable network-path and middlebox behavior under controlled protocol variations | Experiment reports, negative findings, and offline artifact-integrity manifests |
| **[Mirage Flow](https://github.com/Northguard-Security/mirage-flow)** | Timing-pattern detection under jitter and loss, and stateful response modeling | Controlled simulations, correlation measurements, and offline contract tests |
| **[Chimera](https://github.com/Northguard-Security/Chimera)** | Clipboard-to-DOM-XSS trust-boundary failures | Deliberately vulnerable and safe control fixtures for comparison |

The repositories document their individual maturity, prerequisites and safety boundaries. Experiments, simulations and heuristics are not presented as field validation or production security guarantees.

## The research method

```text
question → build → instrument → observe
                     ↓
          compare with controls
                     ↓
         reproduce or falsify
                     ↓
         report evidence + limits
```

**Systems** — protocols, execution environments, application boundaries and infrastructure.

**Signals** — timestamps, headers, packets, RF observations and measurable state transitions.

**Evidence** — reproducible artifacts, integrity checks, controls and explicit uncertainty.

A logged event is an observation, not automatically an explanation. Correlation is not identity; a model is not a real-world measurement; a detected pattern is not proof of malicious intent.

## Research with clear boundaries

We build and test in controlled environments and on systems we own or are explicitly authorized to study. Some experiments involve active traffic, browser behavior, or suspicious inputs; isolation and observability matter as much as the code.

For reports and contributions, see [CONTRIBUTING.md](https://github.com/Northguard-Security/.github/blob/main/CONTRIBUTING.md). For the visual language, see the [NOEMETRA identity guide](https://github.com/Northguard-Security/.github/blob/main/brand/README.md).

<sub>NOEMETRA is the new public research identity of the workspace previously known as Northguard Security. The GitHub organization URL remains unchanged during the technical migration.</sub>
