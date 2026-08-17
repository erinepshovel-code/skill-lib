---
name: accounts
description: Manage digital account lifecycle: account inventory, subscriptions, authentication/recovery readiness, permissions, reconnection, cancellation, closure, provider migration, and access-state questions without storing secrets.
---

# accounts

## Trigger
Account access, subscriptions, renewals, reconnecting providers, permissions, recovery, closing accounts, or asking what online services currently require attention.

## Non-trigger
Do not load merely because another domain uses an authenticated connector; use this when account lifecycle itself is the task.

## Sources of truth
Provider/account management state, billing/subscription notices, connected-account status, authoritative recovery settings, and current user instruction.

## Workflow
1. Identify provider, account identity, current state, cost/renewal if relevant, and consequence of inaction.
2. Distinguish authentication problem from service problem.
3. Prefer supported in-product reconnect/account-management flows when available.
4. Record recovery readiness as metadata only: configured / missing / stale / hmmm.
5. For cancellation or closure, identify exported data, dependencies, and irreversible effects first.

## Boundaries
Never commit passwords, tokens, recovery codes, cookies, or security answers. Never disable recovery or close an account merely because it appears unused.

## Output
Provider / state / cost or deadline / dependency / required action / completion evidence / hmmm.

## Validation
After a change, verify the provider reports the intended state rather than assuming button-click success.

## hmmm
An account you forgot is either harmless clutter or the key to another account. Inventory before deletion.
