---
name: calendar
description: Manage personal calendar state. Load for events, meetings, appointments, availability, conflicts, deadlines, invitations, recurring obligations, reminders tied to dates, or converting correspondence into schedule state.
---

# calendar

## Trigger
Schedule, calendar, appointment, event, deadline, availability, recurring obligation, invitation, or time-conflict requests.

## Non-trigger
Do not create calendar events for vague intentions better handled as reminders or task notes.

## Sources of truth
Google Calendar event and free/busy state; explicit user time constraints; message/source document that created the obligation.

## Workflow
1. Read existing events or availability before scheduling.
2. Preserve timezone and recurrence semantics.
3. Detect conflicts before writing.
4. Use exact events for fixed commitments; use automation for condition-based or broad-daypart reminders when appropriate.
5. After writes, report event identity, date/time, recurrence, and attendee state.

## Boundaries
Never invent a meeting time from a broad daypart. Never silently move or delete an existing commitment. Invitations are not attendance until response state says so.

## Output
Current schedule or explicit calendar mutation with conflicts and unresolved timing visible.

## Validation
Re-read the resulting event when a write materially changes time, attendees, recurrence, or location.

## hmmm
Time is deterministic; calendars are not. The gap is usually humans.
