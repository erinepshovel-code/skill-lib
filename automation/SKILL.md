---
name: automation
description: Manage personal reminders, recurring scans, scheduled briefings, and condition watches. Load when creating, changing, disabling, deduplicating, auditing, or summarizing scheduled personal tasks.
---

# automation

## Trigger
Remind me, every day/week, monitor, notify when, recurring summary, scheduled scan, standing briefing, or automation/task lifecycle requests.

## Non-trigger
Do not create automation for a one-time action that can and should be completed immediately.

## Sources of truth
Current automation list/state; the domain source the automation will inspect; explicit user cadence/time/condition.

## Workflow
1. Check for an existing equivalent task before creating another.
2. Classify exact schedule / flexible schedule / condition watch.
3. Preserve the user's explicit time; use daypart flexibility when no clock time was given.
4. Keep the execution prompt about one run; keep cadence in the schedule.
5. Disable obsolete tasks rather than leaving duplicate monitors running.
6. For condition watches, notify only when the condition becomes meaningful.

## Boundaries
Hourly is the maximum checking frequency. Do not create unhealthy or intrusive monitoring loops. A scheduled reminder is not evidence the underlying action happened.

## Output
Task title / behavior / schedule or condition / status / dependency / hmmm.

## Validation
Inspect resulting task identity and schedule after create/update; dedupe against existing tasks.

## hmmm
Automation should remove repetition, not automate the creation of more repetition.
