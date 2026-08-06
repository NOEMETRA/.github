<p align="center">
  <img src="./header.svg" alt="Northguard Security — Independent Experimental Security Research" width="100%" />
</p>

Northguard Security is a research workspace for building and testing technical ideas across network behavior, protocol analysis, digital forensics, attribution, systems observability, wireless security, and defensive security engineering.

The projects here are experiments first.

The objective is not to make a capability sound impressive. It is to determine whether the underlying mechanism can actually be observed, reproduced, measured, and falsified.

## Research approach

A capability is not considered demonstrated because a program produced the expected output.

The working method is closer to:

```text
hypothesis
    ↓
controlled stimulus
    ↓
observable signal
    ↓
measurement
    ↓
negative controls
    ↓
repetition
    ↓
verdict
```

Results are treated according to the evidence available: simulated, observed under controlled conditions, reproduced on a real system, falsified, or still unverified.

Negative results are retained when they help define the boundary of an experiment.

## Areas of exploration

- Network-path and middlebox behavior
- Protocol state machines and timing signals
- Digital forensics and infrastructure attribution
- Wireless and 802.11 experimentation
- Kernel and system observability
- Detection and correlation of weak signals
- Browser and application trust boundaries
- RF, sensing and signal-processing prototypes
- Controlled security research environments

These areas are not a product roadmap. They reflect different technical questions explored over time.

## Research status

Northguard projects are intentionally experimental.

A repository may contain:

- a validated mechanism;
- a controlled proof of concept;
- an unfinished research direction;
- simulation code;
- failed hypotheses;
- historical experiments;
- components that were deliberately never developed into operational systems.

Documentation aims to distinguish these states explicitly.

## Principle

> **No capability exists until there is evidence that distinguishes success from coincidence, an intermediate output, or an incorrect interpretation.**

**The code is the experiment. The measurement is the result.**
