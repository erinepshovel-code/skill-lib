---
name: personal-github
description: Manage the user's personal GitHub repositories, issues, pull requests, profile surfaces, releases, and repository hygiene while preserving strict separation from The Interdependency organization authority. Load when a GitHub task is personal rather than organization-owned.
---

# personal-github

## Trigger
Personal repositories, personal profile, personal issues/PRs/releases, repo creation/bootstrap, archiving, publication surfaces, or moving personal work between repositories.

## Non-trigger
Do not load for `The-Interdependency/*` repositories except to document an explicit cross-boundary relation. Organization work uses organization doctrine.

## Sources of truth
GitHub repository state, branch/commit/PR/issue identity, repository ownership, and explicit source provenance for imported content.

## Workflow
1. Confirm repository owner before writes.
2. Fetch current file/branch state before modifying.
3. Preserve source history/provenance when copying from organization repos.
4. Keep personal workflows and personal data out of organization canon unless explicitly promoted through the organization process.
5. Use branches/PRs when changes benefit from review; direct writes only when appropriate for the personal repo.

## Boundaries
Ownership is authority. Similar filenames do not make personal and organization skill libraries interchangeable. Never copy organization-only secrets or internal data into personal repos.

## Output
Repo / branch / commit or PR / changed files / source boundary / validation / hmmm.

## Validation
Verify resulting GitHub state and exact commit identity after writes.

## hmmm
Forking an idea is easy. Forking its authority without noticing is the expensive part.
