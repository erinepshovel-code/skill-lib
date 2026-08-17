---
name: digital-continuity
description: Manage backups, exports, account/data migration, recovery paths, device or provider failure planning, and survivable access to important personal digital state. Load when the user asks what would be lost if a device/account/provider failed or how to preserve access through change.
---

# digital-continuity

## Trigger
Backup, export, recovery, migration, provider shutdown, lost device, inaccessible account, data survivability, restore test, or digital estate/continuity requests.

## Non-trigger
Do not load for routine file organization unless failure/recovery is the reason for the work.

## Sources of truth
Actual backup/export state, provider capabilities, account recovery configuration, file custody, device state, and verified restore tests.

## Workflow
1. Inventory critical data classes and the systems that currently hold them.
2. Identify single points of failure: one device, one account, one provider, one credential path.
3. Prefer at least one independently recoverable copy for critical non-secret data.
4. Keep secret recovery material outside this repository and record only whether a recovery path exists.
5. Test restore/retrieval for representative critical items.
6. Record last verified date and hmmm for untested paths.

## Boundaries
A sync service is not automatically a backup. An export file is not useful until it can be opened. Do not centralize all recovery secrets into one convenient catastrophic bundle.

## Output
Asset / current copies / failure mode / recovery path / last verified / next action / hmmm.

## Validation
At least one representative restore/retrieval test must succeed before calling a continuity path verified.

## hmmm
Backups are Schrödinger's files until restored.
