# Agent instructions

Start with `personal-ops/SKILL.md` when a request spans more than one personal digital domain.

Load only the domain skill(s) needed for the task. Do not load the entire library by habit.

## Resource-run invariant — binding

Read [`RESOURCE_RUN_INVARIANT.md`](RESOURCE_RUN_INVARIANT.md) before any compute run whose completion depends materially on scarce resources.

**Resource scarcity requires contemplation BEFORE a compute run begins. Once begun, let it finish. If there is doubt you can finish it, do not start it.** Do not invent a wall-clock cutoff merely to make a healthy computation bounded or falsifiable; runtime is a stopping criterion only when it is actually load-bearing to the task, safety boundary, or an externally imposed hard limit.

For every skill:

1. retrieve current state from the authoritative connected source before making state-dependent claims;
2. preserve the difference between read, draft, scheduled, sent, posted, paid, deleted, archived, and completed;
3. use the smallest sufficient write;
4. do not copy secrets into repo files, logs, handoffs, or chat summaries;
5. record unresolved constraints as `hmmm` rather than guessing;
6. keep personal and organization authority separate.

`PERSONAL_BOUNDARIES.md` and `RESOURCE_RUN_INVARIANT.md` are binding for every skill.
