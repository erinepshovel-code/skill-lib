---
name: social-media
description: Manage personal social-media publishing and archive. Load for topic inventories, recovering actual posts, indexing or updating the social-media post database, distinguishing drafts from published content, checking platform-specific character/media/tier constraints, preparing cross-platform variants, publication provenance, or maintaining the user's social-media corpus.
---

# social-media

## Trigger
X, LinkedIn, social posts, replies/comments, article drafts, publication archive, topic inventory, post database/index, character-limit checks, or cross-platform reuse.

## Non-trigger
Do not load for private DMs unless the user is explicitly managing private communications; those belong primarily to `communications`. Do not load for organization-owned publication state merely because the subject matter overlaps with The Interdependency.

## Sources of truth
1. Current platform-visible post/account state, direct platform links/exports, and exact screenshots when publication state is at issue.
2. The current user-owned social-media index retrieved from connected files/Library. Known exports are `social_media_post_index.xlsx` and `social_media_post_index.csv`; when the SQLite source is available it carries full long-form bodies and `posts_fts` full-text search.
3. `social-media/index_schema.json` for the public-safe update contract and field/status semantics.
4. `social-media/platform_rules.json` for timestamped public platform constraints. It is a cache, not canon: reverify stale or contradicted rules against the current platform UI and official documentation.
5. Exact publication artifacts, chat-history drafts, user-provided links, and source documents from which a post was derived.

The repository contains the procedure/schema/rule cache, not the managed personal corpus.

## Workflow
1. Retrieve the current index before making corpus claims or appending anything. Resolve which artifact is the richest current writable source; do not let an older CSV overwrite newer SQLite/XLSX state.
2. When the task involves drafting, replying, publishing, or shortening, load `platform_rules.json`. If its rule is stale, contradicted by the live client, or account-tier dependent, reverify before enforcing a limit.
3. Recover the candidate text and provenance. Classify each user-authored item as `confirmed_posted`, `publication_ready`, `publication_ready_partial`, `draft`, or `superseded_draft`; preserve `body_recovery` separately.
4. Establish authorship before inclusion. Other people's posts and private messages stay outside the user's post corpus; an unattributable screenshot remains unresolved rather than being converted into a user post.
5. Deduplicate before allocating an ID. Compare stable ID, source locator, exact body, and materially equivalent recovered artifacts. Cross-platform variants get distinct records linked back to their source rather than overwriting it.
6. Allocate the next unused monotonic `P####` only after deduplication. Never renumber or recycle an existing ID.
7. Preserve the index fields and semantics in `index_schema.json`: date, platform, format, status, authorship/confidence, publication evidence, topic IDs/topics, title, recovery state, character count, body, source kind/locator, and notes.
8. Preserve exact text when recoverable; never rewrite a recovered post while calling it exact. Preserve source-declared character counts when available. For a publishing decision, also calculate current platform fit using the platform/form/tier rule; near a hard limit, validate in the live composer.
9. Write the authoritative index, then rebuild/verify `posts_fts` when SQLite is available and regenerate synchronized CSV/XLSX exports. Long bodies may remain in SQLite while spreadsheet views chunk them; do not truncate the authoritative body.
10. Read the new/changed record back by `post_id` and search terms. A write is incomplete until provenance, status, and retrieval survive the round trip.

## Platform constraint discipline
- Platform rules change. Every cached rule carries `checked_at`; reverify after the staleness window or immediately when the UI disagrees.
- Account tier is runtime personal state. Do not commit the user's subscription/eligibility to this public repository.
- Current cached X rules distinguish the 280-character standard post from Premium long posts up to 25,000 characters; X URLs count as 23 characters through t.co and posts support up to four media items. Apply the live account's eligibility before choosing the long-post ceiling.
- Current cached LinkedIn rules distinguish 3,000-character feed posts from 125,000-character articles. The 1,250-character comment/reply ceiling is retained as an observed current constraint because LinkedIn's current general-comment help does not publish the numeric limit; the live composer wins if it changes.
- Do not assume simple Unicode string length always equals a platform's effective counter.

## Boundaries
Publication-ready is not published. A screenshot of a feed is not proof the visible post is the user's. Do not infer authorship from topic similarity. Do not store other people's posts merely because they prompted a reply. Do not promote partial recovery to exact text. Do not silently migrate the corpus schema because a new platform exposes different metadata. Do not commit private corpus bodies or changing personal account state to this public repository.

## Output
For an index update, report: `post_id / platform / format / status / recovery / character fit / source evidence / index write / FTS-export verification / hmmm`.

For a draft or reply, return the platform-ready text plus `effective count / applicable limit / rule freshness / hmmm` when the limit matters.

## Validation
- Every `confirmed_posted` label has visible or platform-source publication evidence.
- Every exact-text claim has exact source text.
- New rows obey `index_schema.json`, stable IDs do not change, and duplicates are not silently appended.
- When SQLite/FTS is available, the record is retrievable through `posts_fts`; synchronized exports preserve the same ID/status/provenance.
- Platform-fit claims use current rules; stale/contradicted metadata is reverified instead of guessed.

## hmmm
The current SQLite artifact's exact Library identity is runtime state and must be discovered when an update is requested. Social platforms remain excellent databases except for the parts where they are social platforms, and excellent standards documents except for the parts where they change without asking.
