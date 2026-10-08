# Contributing to NOEMETRA

NOEMETRA is an independent research workspace. Contributions that improve reproducibility, safety, technical correctness, and evidence quality are welcome.

## Useful contributions

- A minimal reproducible bug report, with environment and expected/observed behavior.
- A regression test, synthetic fixture, or negative control.
- A correction to an unsupported claim or confusing interpretation.
- Documentation that lets another researcher repeat a controlled experiment.
- Small, reviewable fixes that preserve existing experimental results.

Before proposing substantial new functionality, open a scoped issue in the relevant repository. Not every research direction is intended to become a production feature.

## Reporting an issue

Include the repository revision or commit, platform and tool versions, minimal reproduction steps, observed output, expected behavior, and whether you reproduced it more than once. Where possible, attach sanitized logs or synthetic inputs.

**Never attach passwords, API keys, authentication tokens, personal identifiers, private network captures, or other sensitive data.** Use systems you own or are expressly authorized to test.

If you suspect a security vulnerability, **do not disclose exploit details in a public issue**. Use GitHub's private vulnerability reporting feature where enabled, or establish a private contact path with the maintainers before sharing sensitive details.

## Pull requests

- Keep the change focused and explain which hypothesis, failure, or behavior it addresses.
- Document how it was validated; distinguish automated tests, simulation, and hardware or field observations.
- Include negative or failure cases when those are material to the claim.
- Avoid asserting security efficacy, identity attribution, or production readiness without supporting evidence.
- Preserve existing safety controls, explicit authorization boundaries, and useful historical failure records.
- Run the tests and CI configured by the target repository. If there is no automated suite, state exactly which manual checks were performed.

This is a research space, not an invitation for unauthorized scanning, exploitation, data collection, or interference with real networks.
