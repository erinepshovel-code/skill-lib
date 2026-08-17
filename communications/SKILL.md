---
name: communications
description: Manage personal Gmail and contacts. Load for inbox triage, finding or reading messages, action extraction, recipient resolution, drafting/sending/replying/forwarding, archive/label operations, contact lookup, or follow-up tracking.
---

# communications

## Trigger
Personal email, inbox, correspondence, recipients, contacts, drafts, replies, follow-up, or message-status requests.

## Non-trigger
Do not load for public social posts, organization issue threads, or generic writing with no personal communications state.

## Sources of truth
Gmail for message/draft/sent state; Google Contacts for saved contact identity; Calendar when a message creates a scheduling obligation.

## Workflow
1. Search/read before summarizing or drafting from mailbox state.
2. Resolve people through Contacts when identity is ambiguous.
3. Classify messages: action / awaiting / reference / noise.
4. Preserve message IDs and exact sender addresses when replying.
5. Distinguish draft from sent.
6. When a deadline or meeting is created, hand off explicitly to calendar or automation.

## Boundaries
Do not invent recipients. Do not expose private message content unnecessarily. Spam, receipts, and automated notices remain lower priority unless they create money, legal, security, or deadline consequences.

## Output
Actionable correspondence state: who / what / due / message state / next action / hmmm.

## Validation
Read the actual thread before representing its contents; after a write, verify the resulting draft/sent/label/archive state.

## hmmm
Silence can mean no reply, no delivery, no attention, or merely Tuesday. Preserve which one is actually known.
