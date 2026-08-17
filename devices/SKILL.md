---
name: devices
description: Manage personal Android, Termux, and device hygiene. Load for storage, installed apps, permissions, updates, backups, ADB/Termux workflows, shutdown/reboot integrity, debloat, device-access boundaries, or recovery readiness.
---

# devices

## Trigger
Phone/device storage, apps, Android, Termux, ADB, updates, backups, permissions, debloat, shutdown behavior, or device recovery.

## Non-trigger
Do not load for remote server administration unless the personal device is part of the access path.

## Sources of truth
Current device state from Android/ADB/Termux commands, package manager output, filesystem/storage checks, and manufacturer/platform settings.

## Workflow
1. Inspect before changing.
2. Separate disable from uninstall, user package from system package, and data deletion from app removal.
3. Preserve keep-lists for telephony, emergency, authentication, Knox/security, accessibility, and required Google/system components.
4. Prefer reversible disable/debloat before destructive removal.
5. Verify storage, boot, networking, and required apps after changes.

## Boundaries
No root escalation by convenience. No destructive debloat without rollback. Never paste secrets into shell history if a safer input path exists.

## Output
Observed device state, exact action, rollback, verification, and remaining hmmm.

## Validation
A change is not successful merely because the command exits zero; verify the intended device behavior still works.

## hmmm
A phone with every package removed is admirably clean and operationally similar to a brick.
