---
name: social-media
description: Manage personal social-media publishing and archive. Load for topic inventories, recovering actual posts, indexing posts, distinguishing drafts from published content, preparing cross-platform variants, publication provenance, or maintaining the user's social-media corpus.
---

# social-media

## Trigger
X, LinkedIn, social posts, replies, article drafts, publication archive, topic inventory, post database, or cross-platform reuse.

## Non-trigger
Do not load for private DMs unless the user is explicitly managing private communications; those belong primarily to communications.

## Sources of truth
Platform-visible screenshots/exports when available; exact publication artifacts; chat-history drafts; user-provided links; source documents from which a post was derived.

## Workflow
1. Classify each item: confirmed posted / publication-ready / draft / partial recovery / superseded / other-author.
2. Preserve exact text when recoverable; never rewrite a recovered post while calling it exact.
3. Tag topic, date, platform, format, source, and publication evidence.
4. Keep other people's posts and private messages out of the user's post corpus.
5. Reuse across platforms by deriving a new variant linked to the source, not overwriting the source.

## Boundaries
Publication-ready is not published. A screenshot of a feed is not proof the visible post is the user's. Do not infer authorship from topic similarity.

## Output
Indexed post records plus topic inventory, provenance, recovery confidence, and hmmm.

## Validation
Every 'published' label requires visible or platform-source evidence; every exact-text claim requires exact source text.

## hmmm
Social platforms are excellent databases except for the parts where they are social platforms.
