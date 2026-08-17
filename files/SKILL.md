---
name: files
description: Manage personal files across ChatGPT Library and Google Drive. Load for locating, reading, organizing, renaming, moving, deduplicating, archiving, uploading, provenance tracking, or deciding which copy is authoritative.
---

# files

## Trigger
Personal documents, screenshots, PDFs, Drive files, Library files, folders, duplicates, archives, or provenance/custody questions.

## Non-trigger
Do not load for source code that belongs in GitHub unless personal file custody is also part of the request.

## Sources of truth
Files/Library metadata and content; Google Drive file identity/version where applicable; producing system for generated artifacts.

## Workflow
1. Search content when location is unknown; list when browsing filenames/folders.
2. Identify the exact file ID before mutation.
3. Distinguish original, generated derivative, export, screenshot, and duplicate.
4. Prefer stable names and provenance metadata over filename folklore.
5. Use create-only behavior when an external system cannot update in place.
6. Verify destination after move/upload/rename.

## Boundaries
A filename is not content. A local mount is not persistent storage. Do not delete the last verified copy. Do not upload private data to public destinations by inference.

## Output
File identity, location, authority/provenance, requested mutation, and remaining duplicate or custody risk.

## Validation
Every destructive or relocating operation must identify source and verified destination first.

## hmmm
A duplicate is sometimes waste and sometimes the only reason tomorrow is survivable.
