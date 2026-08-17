# Repository boundary

`erinepshovel-code/skill-lib` is a public skill/doctrine repository for personal digital-life management.

It may contain:

- workflows;
- source-of-truth routing rules;
- permission and mutation boundaries;
- schemas, checkers, and generated adapters;
- examples that contain no private personal state.

It must not contain:

- passwords, tokens, recovery codes, session material, or private keys;
- private messages or raw email bodies;
- financial transaction exports or full account identifiers;
- government identifiers, medical records, legal evidence, or other sensitive source documents;
- current personal state copied from connected services merely for convenience.

Skills retrieve changing personal state from the authoritative connected source at execution time. If that source is unavailable, preserve the gap as `hmmm`.

## hmmm

A public operations manual can safely say how to find the fire extinguisher. It should not publish where the spare house key is hidden.
