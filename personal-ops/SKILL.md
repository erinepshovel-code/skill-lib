---
name: personal-ops
description: Orchestrate personal digital-life work that spans two or more domains, including communications, calendar, files, finances, accounts, social media, devices, administration, personal GitHub, automations, or continuity. Load when the user asks for a personal SITREP, asks what needs attention, or requests a workflow crossing domain boundaries.
---

# personal-ops

## Trigger
Load for cross-domain personal operations, personal digital-life SITREPs, priority queues, or requests whose completion depends on more than one personal system.

## Non-trigger
Do not load for a single narrow domain task when its dedicated skill is sufficient. Do not treat organization/project work as personal merely because the same human owns both.

## Sources of truth
Current connected-source state; `PERSONAL_BOUNDARIES.md`; domain skills named in `skills.json`; explicit user instructions.

## Workflow
1. Identify the domains actually required.
2. Read current state from each authoritative source before drawing conclusions.
3. Normalize state into: obligation, evidence, deadline, dependency, authority, next action, completion condition.
4. Separate read-only findings from writes.
5. Execute the smallest sufficient authorized writes in dependency order.
6. Return one compact SITREP: established / changed / blocked / next / hmmm.

## Boundaries
Never use one domain's access as implicit authority in another. Never move secrets into the repo. Do not convert a project obligation into a personal obligation or vice versa without an explicit relation.

## Output
A concise cross-domain state with source-aware next actions and no duplicate tasks.

## Validation
Every state-dependent claim must have a current source; every write must have an explicit completion result; unresolved dependencies remain visible.

## hmmm
A personal operating system is useful only if it reduces forgotten obligations without becoming one more obligation to maintain.
