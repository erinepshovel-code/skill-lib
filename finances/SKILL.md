---
name: finances
description: Manage and analyze the user's own financial data. Load for spending, transactions, cash flow, income, balances, bills, subscriptions, liabilities, APR, utilization, holdings, dividends, allocation, account sync, or finance-grounded planning.
---

# finances

## Trigger
Any question grounded in the user's actual money, accounts, transactions, liabilities, investments, subscriptions, balances, or sync state.

## Non-trigger
Do not load for generic financial education that does not use the user's records.

## Sources of truth
Connected Finances accounts and their explicit history coverage, sync state, as-of time, transactions, liabilities, recurring charges, and holdings.

## Workflow
1. Check linked-account coverage before transaction-grounded conclusions.
2. Preserve posted/pending distinction and transfer semantics.
3. For cash flow or income, retrieve broad inflow candidates before classifying them.
4. State partial-period or partial-sync limits in the same sentence as totals.
5. For debt, use real balances/APRs/minimums before prioritizing.
6. For investments, distinguish holdings from watchlists and never imply a trade occurred.

## Boundaries
Never infer complete coverage from a connected account. Never classify transfers as income solely because they are inflows. Do not store sensitive account data in this repo.

## Output
Numbers with period, coverage, account scope, classification basis, and next decision.

## Validation
Reconcile totals to retrieved rows and state unresolved/ambiguous transactions explicitly.

## hmmm
Money is excellent at becoming precise exactly where the data stopped syncing.
