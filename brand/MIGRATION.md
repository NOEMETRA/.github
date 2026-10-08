# NOEMETRA organization migration checklist

The NOEMETRA public identity can be prepared inside `Northguard-Security/.github` without changing the organization's URL, repository remotes, or permissions.

## Before changing the GitHub organization handle

- [ ] Confirm that the exact `Noemetra` organization handle is available in GitHub's rename UI.
- [ ] Check trademarks in the jurisdictions relevant to use, legal entities and appropriate domains. A zero-result general web search is not formal clearance.
- [ ] Inventory references to `Northguard-Security` across **all public and private** repositories, actions, deployments, workflows, scripts, webhooks, integrations, badges, release downloads and external sites. Do not publish private repository names in public documentation.
- [ ] Review any GitHub Pages custom domains or package/container consumers. Verify external automation, Actions use, branch rules, integrations and secret scopes.
- [ ] Record an issue/PR checklist for updates that can be prepared ahead of the rename.

## Owner action: rename the organization

Only an organization **owner** can do this. In GitHub: **Organizations → Northguard-Security → Settings → Danger zone → Rename organization**, review the warnings, then choose `Noemetra` if available.

GitHub automatically redirects most old repository web URLs, but **not the old organization profile URL**. Calls to the old organization API URL may fail, and the old namespace may become available to another account. Do not rely on redirection as a permanent integration contract.

Official reference: https://docs.github.com/en/organizations/managing-organization-settings/renaming-an-organization

## After owner rename

- [ ] Confirm `https://github.com/Noemetra` renders the profile and the existing repositories retained visibility and permissions.
- [ ] Update hard-coded links in `profile/README.md`, the `CONTRIBUTING.md`, brand references, and dependent repositories.
- [ ] Change `repository-discovery.json` organization field and update the tests that intentionally pin the old slug. Run the metadata sync first in preview mode and apply only after verifying current repository state.
- [ ] Update remote URLs on all local clones, including private projects.
- [ ] Update actions/workflows, webhooks, tokens or integrations, APIs, GitHub Pages, package URLs and any external profile links.
- [ ] Verify CI on each public repository and a representative private project *without publishing private details*.
- [ ] Upload `brand/avatar.svg` rendered as a PNG through GitHub organization settings (the repository file by itself does not change the account avatar).
- [ ] Edit the public organization display name and description in GitHub settings.
- [ ] Remove the transitional name note only after checking old public links.

## Reversal

Before a rename, back out this public identity by reverting the branding PR; software and history remain unchanged. After renaming the organization, recovery needs a separate owner/admin decision and a repeat audit of references: changing the visible label alone does not restore the old namespace.
