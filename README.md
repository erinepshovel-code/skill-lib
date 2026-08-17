# Personal skill-lib

A public-safe skill library for managing Erin Spencer's digital personal life.

This repository is intentionally separate from `The-Interdependency/skill-lib`.
The organization library governs project and engineering work; this library governs personal digital operations.

## Operating rule

Personal data is not canon. It is current state with provenance, timestamps, and revocable authority.

This repository is public. Do not store secrets or personal state in this repository. Skills may describe how to locate, rotate, verify, or recover credentials, but never commit passwords, API keys, recovery codes, full financial account numbers, government identifiers, or private message bodies merely for convenience.

## Skills

| Skill | Purpose |
|---|---|
| `personal-ops` | Orchestrates personal digital work across domains without silently crossing permission boundaries. |
| `communications` | Gmail, contacts, correspondence triage, drafts, follow-up, and recipient resolution. |
| `calendar` | Events, availability, deadlines, reminders, recurring obligations, and schedule conflict handling. |
| `files` | Personal file custody, Drive/Library organization, naming, provenance, duplicates, and retrieval. |
| `finances` | Personal accounts, cash flow, bills, subscriptions, liabilities, holdings, and financial-data coverage limits. |
| `accounts` | Account inventory, subscriptions, authentication state, recovery paths, permissions, and closure/reconnection workflows. |
| `social-media` | Post inventory, drafts, published-state separation, social archive, cross-platform reuse, and provenance. |
| `devices` | Android/Termux/device hygiene, storage, app inventory, permissions, updates, backups, and non-destructive debloat. |
| `personal-admin` | Taxes, benefits, insurance, legal/civic paperwork, official deadlines, receipts, and administrative evidence. |
| `personal-github` | Personal repositories, issues, PRs, profile surfaces, and separation from organization authority. |
| `automation` | Reminders, recurring scans, condition watches, standing personal briefings, and task lifecycle. |
| `digital-continuity` | Backups, exports, recovery, account survivability, migration, and failure-safe access to important personal data. |

## Validation

```bash
python tools/check_skills.py
```

The checker verifies that every registered skill exists, has a concrete trigger, names its sources of truth, states boundaries, defines validation, and preserves `hmmm`.

## hmmm

This repository contains management doctrine, not the managed personal data itself. Current personal state must be retrieved from its authoritative source when needed; unresolved or inaccessible state remains `hmmm`.
