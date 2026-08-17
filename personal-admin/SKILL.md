---
name: personal-admin
description: Manage personal administrative obligations such as taxes, benefits, insurance, legal/civic paperwork, official deadlines, receipts, evidence packets, applications, notices, and submission state.
---

# personal-admin

## Trigger
Taxes, benefits, insurance, legal/civic paperwork, government forms, official notices, applications, receipts, evidence packets, renewal dates, or administrative deadlines.

## Non-trigger
Do not load for legal advice or medical advice merely because a document is legal/medical; this skill manages custody, state, and obligations, not professional judgment.

## Sources of truth
Official notices and documents; Gmail; Calendar; Files/Drive; authoritative agency/provider status; explicit receipts and confirmation numbers.

## Workflow
1. Identify obligation, authority, due date, required evidence, submission channel, and consequence of missing it.
2. Gather the minimum complete evidence packet with provenance.
3. Distinguish prepared / submitted / received / accepted / denied / appealed / hmmm.
4. Put fixed deadlines on Calendar and condition-based follow-up in automation when useful.
5. Preserve receipts and confirmation evidence with the submission record.

## Boundaries
Do not invent filing status, legal interpretation, eligibility, or successful receipt. Sensitive identifiers should remain in authoritative documents, not copied into repo metadata.

## Output
Administrative ledger entry: matter / authority / due / evidence / status / next action / receipt / hmmm.

## Validation
No matter becomes 'complete' without the appropriate acceptance, receipt, or terminal status evidence.

## hmmm
Bureaucracy is a distributed state machine with unusually expensive undocumented transitions.
