# Personal digital boundaries

## Authority

- The human owner remains the authority for personal decisions.
- An agent may retrieve, compare, draft, organize, and execute explicitly authorized reversible changes.
- Destructive, financial, legal, identity, security, or account-closure actions require the authority appropriate to the connected tool and must not be inferred from convenience.

## Data

Never commit:

- passwords or passphrases;
- API keys, PATs, OAuth secrets, session cookies, recovery codes;
- full bank/card/account numbers;
- Social Security or other government identifiers;
- private medical records or correspondence merely to improve agent convenience;
- raw authentication exports.

Prefer references, provider/account labels, last-four digits where necessary, timestamps, coverage state, and retrieval instructions.

## Storage classes

Use three distinct storage classes:

1. **ChatGPT Library — personal working data.** Library may hold private personal working artifacts, indexes, drafts, screenshots, exports, and other non-secret data when persistence and retrieval are useful. Treat Library as private account cloud storage, not as a zero-knowledge or secret vault.
2. **Personal GitHub skill-lib — public procedures only.** GitHub holds skills, schemas, platform rules, validation logic, public-safe examples, and pointers needed to locate authoritative personal state. Do not commit current personal state merely for agent convenience.
3. **Secret storage — secrets only.** Passwords, API keys, PATs, OAuth/session material, recovery codes, full financial identifiers, government identifiers, and equivalent high-impact credentials or identity material stay outside both the public repository and ordinary Library working corpora. Use the provider's protected credential surface or dedicated encrypted secret storage.

When a Library artifact is the authoritative working corpus, GitHub should describe its schema and retrieval/update procedure rather than duplicate its contents. Stable file IDs, provider IDs, timestamps, and provenance are preferred over copied private bodies.

## Truth and state

- Distinguish observed state from inferred state.
- Timestamp changing facts.
- A draft is not sent.
- A reminder is not completed work.
- A publication-ready post is not a published post.
- A linked financial account is not necessarily fully synced.
- A file title is not proof of file content.
- A deleted local copy is not proof a cloud copy is gone.

## Separation

Personal GitHub work must not silently inherit authority, canon, claims, secrets, or publication state from The Interdependency organization repositories. Cross-boundary reuse must name the source and purpose.

## hmmm

Personal digital life changes faster than documentation. Unknown state is a first-class state; stale certainty is worse than a visible gap.
